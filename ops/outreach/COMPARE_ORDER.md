# COMPARE_ORDER — bulk dataset comparison for upstream outreach (Codex step 1 only)

Today is 2026-07-05.

## Task
Compare THIS repo's `data/facts.json` (135 verified model records, each with pricing,
context_window_tokens, max_output_tokens, and source quotes) against external community
model-metadata datasets, and produce a candidates file of discrepancies. DO NOT contact
anyone, DO NOT open any PR/issue, DO NOT edit any external repo. Only produce the file.

## Datasets to fetch FRESH (they may have changed since last week)
(a) LiteLLM:   https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
(b) models.dev: https://models.dev/api.json

## What counts as a candidate
For every model that overlaps between our facts.json and a dataset, where a numeric field
(input price per 1M, output price per 1M, cache read/write price, context window, max output)
DIFFERS by more than rounding:
  - Record: {repo, dataset, model_key_theirs, model_key_ours, field, theirs, ours,
             our_source_url, our_quote, our_verified_at}
  - Only include fields where we have a stored source quote containing our number
    (no quote → skip; we can't defend it).

## EXCLUDE (already contacted 2026-07-04 — do not re-list)
- BerriAI/litellm: any field already in issue #32111 / PR #32113
- anomalyco/models.dev: mistral-medium pricing (issue #3025, already fixed)
- Helicone/helicone: claude-3.5-sonnet-v2 bedrock pricing (PR #5709)
Read ops/outreach/candidates-2026-07-04.json and skip any (model_key, field) pair already present there.

## Output
Write ops/outreach/candidates-2026-07-05.json — a JSON array of candidate objects.
If there are zero NEW discrepancies, write an empty array []. Zero is a valid, successful result —
do not invent differences to fill the file. Also write a one-paragraph summary at
ops/outreach/candidates-2026-07-05-summary.md (how many models compared, how many raw diffs,
how many survived the has-quote filter, how many excluded as already-contacted).

## Definition of done
- ops/outreach/candidates-2026-07-05.json exists (array, possibly empty)
- ops/outreach/candidates-2026-07-05-summary.md exists
- No external repo was contacted or modified
