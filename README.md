# ModelWire

ModelWire is a machine-readable, source-verified facts feed for commercial LLM APIs. The MVP tracks model identifiers, pricing, lifecycle status, token limits, modalities, and primary-source evidence.

## Files

- `schema/model_fact.schema.json` defines one model fact entry.
- `data/facts.json` is the source facts array.
- `site/feed.json` is the public feed wrapper generated from `data/facts.json`.
- `gaps.md` lists fields left null because collected primary sources did not confirm them.

## Validate

```bash
python scripts/validate.py
```

On this Windows workspace, use the Python launcher if `python` resolves to the Microsoft Store alias:

```bash
py scripts/validate.py
```

## Build Site Feed

```bash
python scripts/build_site.py
```

Then open `site/index.html` in a browser. The table supports provider filtering, status filtering, and input/output price sorting.

## Sourcing Policy

ModelWire uses primary sources only: official provider docs, official pricing pages, official changelogs, and official blogs. Every source record includes the source URL, access timestamp, covered fields, and a verbatim quote supporting the values. Values that could not be confirmed from a collected primary source remain `null` and are recorded in `gaps.md`.

Prices are normalized to USD per 1M tokens. When providers publish multiple tiers for the same model, notes identify which cited tier was recorded.
