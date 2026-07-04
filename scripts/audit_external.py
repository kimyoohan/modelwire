#!/usr/bin/env python3
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FACTS_PATH = ROOT / "data" / "facts.json"
ALIAS_PATH = ROOT / "data" / "external" / "alias_map.json"
LITELLM_PATH = ROOT / "data" / "external" / "litellm.json"
MODELSDEV_PATH = ROOT / "data" / "external" / "modelsdev.json"
OUT_PATH = ROOT / "data" / "external" / "mismatches.json"

FIELDS = [
    "pricing.input_per_mtok",
    "pricing.output_per_mtok",
    "pricing.cached_input_per_mtok",
    "context_window_tokens",
    "max_output_tokens",
]


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def our_value(fact, field):
    if field.startswith("pricing."):
        return fact.get("pricing", {}).get(field.split(".", 1)[1])
    return fact.get(field)


def litellm_value(record, field):
    if field == "pricing.input_per_mtok":
        return multiply_maybe(record.get("input_cost_per_token"), 1_000_000)
    if field == "pricing.output_per_mtok":
        return multiply_maybe(record.get("output_cost_per_token"), 1_000_000)
    if field == "pricing.cached_input_per_mtok":
        return multiply_maybe(record.get("cache_read_input_token_cost"), 1_000_000)
    if field == "context_window_tokens":
        return first_present(record, ["max_input_tokens", "max_tokens"])
    if field == "max_output_tokens":
        return record.get("max_output_tokens")
    raise KeyError(field)


def modelsdev_value(record, field):
    if field == "pricing.input_per_mtok":
        return (record.get("cost") or {}).get("input")
    if field == "pricing.output_per_mtok":
        return (record.get("cost") or {}).get("output")
    if field == "pricing.cached_input_per_mtok":
        return (record.get("cost") or {}).get("cache_read")
    if field == "context_window_tokens":
        return (record.get("limit") or {}).get("context")
    if field == "max_output_tokens":
        return (record.get("limit") or {}).get("output")
    raise KeyError(field)


def multiply_maybe(value, factor):
    if value is None:
        return None
    return value * factor


def first_present(record, keys):
    for key in keys:
        value = record.get(key)
        if value is not None:
            return value
    return None


def classify(ours, theirs, field, rel_tol=0.005):
    if ours is None and theirs is None:
        return "match"
    if ours is None:
        return "we_lack"
    if theirs is None:
        return "they_lack"

    if field in {"context_window_tokens", "max_output_tokens"}:
        return "match" if int(ours) == int(theirs) else "mismatch"

    ours_num = float(ours)
    theirs_num = float(theirs)
    if ours_num == theirs_num:
        return "match"
    baseline = max(abs(ours_num), 1e-12)
    return "mismatch" if abs(ours_num - theirs_num) / baseline > rel_tol else "match"


def compare_record(external, provider, model_id, field, ours, theirs, alias):
    status = classify(ours, theirs, field)
    return {
        "external": external,
        "provider": provider,
        "model_id": model_id,
        "field": field,
        "ours": ours,
        "theirs": theirs,
        "status": status,
        "alias": alias,
    }


def compare_litellm(fact, aliases, litellm):
    provider = fact["provider"]
    model_id = fact["model_id"]
    keys = aliases.get("litellm", [])
    if not keys:
        return [{
            "external": "litellm",
            "provider": provider,
            "model_id": model_id,
            "status": "not_present",
            "alias": None,
        }]

    rows = []
    for key in keys:
        record = litellm.get(key)
        if record is None:
            rows.append({
                "external": "litellm",
                "provider": provider,
                "model_id": model_id,
                "status": "not_present",
                "alias": key,
            })
            continue
        for field in FIELDS:
            rows.append(compare_record("litellm", provider, model_id, field, our_value(fact, field), litellm_value(record, field), key))
    return rows


def compare_modelsdev(fact, aliases, modelsdev):
    provider = fact["provider"]
    model_id = fact["model_id"]
    refs = aliases.get("modelsdev", [])
    if not refs:
        return [{
            "external": "modelsdev",
            "provider": provider,
            "model_id": model_id,
            "status": "not_present",
            "alias": None,
        }]

    rows = []
    for ref in refs:
        ext_provider = ref["provider"]
        key = ref["model"]
        record = (modelsdev.get(ext_provider, {}).get("models") or {}).get(key)
        alias = f"{ext_provider}/{key}"
        if record is None:
            rows.append({
                "external": "modelsdev",
                "provider": provider,
                "model_id": model_id,
                "status": "not_present",
                "alias": alias,
            })
            continue
        for field in FIELDS:
            rows.append(compare_record("modelsdev", provider, model_id, field, our_value(fact, field), modelsdev_value(record, field), alias))
    return rows


def main():
    facts = load_json(FACTS_PATH)
    aliases = load_json(ALIAS_PATH)
    litellm = load_json(LITELLM_PATH)
    modelsdev = load_json(MODELSDEV_PATH)
    alias_by_model = {(item["provider"], item["model_id"]): item for item in aliases["models"]}

    rows = []
    for fact in facts:
        key = (fact["provider"], fact["model_id"])
        alias = alias_by_model.get(key, {"litellm": [], "modelsdev": []})
        rows.extend(compare_litellm(fact, alias, litellm))
        rows.extend(compare_modelsdev(fact, alias, modelsdev))

    stats = {}
    for row in rows:
        stats[row["status"]] = stats.get(row["status"], 0) + 1

    result = {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "field_tolerance": "relative difference > 0.5% for prices; any integer token-limit difference",
        "stats": dict(sorted(stats.items())),
        "comparisons": rows,
    }
    OUT_PATH.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_PATH.relative_to(ROOT)}")
    print(json.dumps(result["stats"], sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
