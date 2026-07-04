# AUDIT_ORDER — external dataset audit (LiteLLM + models.dev), full adjudication

Build ModelWire's key differentiator: nobody else VERIFIES this data. We compare the two most
widely consumed model-metadata datasets against our source-verified facts, adjudicate EVERY
mismatch against primary sources, and publish the audit. Codex quota is not a constraint —
adjudicate all mismatches, do not sample.

Tone rule (mandatory): respectful and factual. LiteLLM and models.dev are valuable community
projects (link their repos). No mocking language anywhere. Frame: "independent verification of
widely-used datasets", state that confirmed upstream errors are candidates for upstream fixes.

## Deliverables

### 1. `scripts/fetch_external.py`
Downloads to `data/external/`:
- https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json → `litellm.json`
- https://models.dev/api.json → `modelsdev.json`
- writes `data/external/meta.json` {accessed_at (UTC ISO), urls, sha256 of each file}

### 2. `data/external/alias_map.json` + `scripts/audit_external.py`
- alias_map: explicit mapping from our (provider, model_id) → list of LiteLLM keys and the
  models.dev (provider, model key). Build it by hand-inspecting both datasets. A model absent
  from an external dataset is simply skipped for that dataset (record as "not_present", not a
  mismatch). Prefer the external dataset's canonical direct-provider entry (e.g. plain
  "claude-x" over "bedrock/..." or "openrouter/..." variants).
- audit script compares, for each mapped model: input price, output price, cached input price,
  context window, max output tokens.
  - LiteLLM prices are per-token → multiply by 1e6. models.dev `cost` is already per-1M.
  - Tolerance: relative difference > 0.5% (or any absolute difference in integer token limits)
    = mismatch. Null on our side vs value on theirs → "we_lack" record (not a mismatch verdict);
    value on ours vs null/absent theirs → "they_lack".
- Output: `data/external/mismatches.json` (raw comparison result).

### 3. Adjudication → `data/audit.json`
For EVERY mismatch: fetch the primary source fresh (official pricing/docs page — same sourcing
rules as WORK_ORDER phase 1; never trust either dataset as evidence) and decide:
- `verdict: "modelwire_correct"` — primary source matches us → external value is outdated/wrong
- `verdict: "modelwire_wrong"` — primary source matches them → FIX data/facts.json (value +
  quote + accessed_at + verified_at), and append a `corrected` entry to a new release in
  data/changelog.json (version bump, summary mentions the audit)
- `verdict: "both_wrong"` — fix ours as above, record theirs as wrong too
- `verdict: "ambiguous"` — page genuinely supports neither/both (e.g. tiered pricing) — explain in note
Every adjudication carries evidence: {url, accessed_at, verbatim quote containing the number}.
Schema: `{date, external: "litellm"|"modelsdev", provider, model_id, field, ours, theirs,
verdict, evidence, note?}` inside `{"audits":[{date, summary, stats:{...}, findings:[...]}]}`.

### 4. `site/audit.html`
Renders data/audit.json (build_site.py copies it to site/): stats banner (N models compared,
M mismatches, breakdown by verdict), findings table with evidence quotes expandable, method
note (primary-sources-only, full adjudication, corrections to our own data listed first —
self-corrections displayed prominently, that is the point of trust). Nav link on all pages
(index/changelog/about/audit).

### 5. Weekly integration + tests
- Append to UPDATE_ORDER.md a step 4b: "run fetch_external.py + audit_external.py, adjudicate
  new mismatches, append a new audit entry to data/audit.json".
- `tests/test_audit_external.py`: unit-conversion correctness (per-token→per-mtok), tolerance
  logic, alias resolution, not_present/we_lack/they_lack classification. Runnable like existing tests.

## Definition of done
1. fetch + audit scripts run clean; every mismatch in mismatches.json appears in audit.json
   with a verdict and evidence quote (zero unadjudicated).
2. Any modelwire_wrong findings are fixed in facts.json + changelog `corrected` release;
   `py scripts/validate.py` exits 0; tests pass; `py scripts/build_site.py` regenerates site.
3. site/audit.html renders with real data; nav updated on all pages.
4. Incremental commits. DO NOT PUSH (independent review pushes).
