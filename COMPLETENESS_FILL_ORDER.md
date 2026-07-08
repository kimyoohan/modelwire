# COMPLETENESS_FILL_ORDER — fill missing context_window / max_output from primary sources

Today is 2026-07-08. Model reasoning: medium. You (Codex) have web access. This is EVIDENCE
COLLECTION. Do NOT edit data/facts.json. Produce ONE proposals file. Claude verifies a sample
against raw sources before anything is applied.

## Why
98 of our 135 records have a null `context_window_tokens` and/or `max_output_tokens` — the
two most-searched fields for LLM APIs. For a "every fact carries a primary-source quote"
product, blank high-intent fields are the worst kind of gap. Fill them where a primary source
states the value; leave null (honestly) where none does.

## Scope
Every entry in data/facts.json where `context_window_tokens` OR `max_output_tokens` is null.
(Run over facts.json yourself to enumerate them — ~98 across together, fireworks, zhipu,
google, mistral, alibaba, xai, minimax, moonshot, perplexity, anthropic, amazon.)

## Method (per model, per missing field)
1. Find the PRIMARY source for that model's spec:
   - Native providers (google, anthropic, mistral, xai, zhipu, alibaba, moonshot, minimax,
     perplexity): the provider's own model/docs page.
   - Hosted open-weight (together, fireworks): the host's model page; if the host does not
     publish a context/output limit, the underlying model's official card is acceptable ONLY
     if the host clearly serves that same model — otherwise leave null.
2. Extract the value WITH a verbatim quote (exact substring containing the number) + the URL.
3. Watch the units: "1M" / "128k" shorthand — record the exact token integer AND flag if the
   source only gives ambiguous shorthand (256K could be 256000 or 262144); if ambiguous,
   record BOTH the shorthand quote and your best integer, mark ambiguous, do not guess silently.

## CALIBRATION (critical)
- If no primary source publishes the field for that model (common for TTS / audio / embedding
  / some hosted SKUs), leave it null and record it as a genuine gap. "No source" is a correct,
  useful outcome. DO NOT invent a number, DO NOT copy a sibling model's number, DO NOT infer
  max_output from context_window.
- A model that is not a text-generation model (TTS, audio-in, embeddings) may legitimately have
  no max_output_tokens — say so rather than forcing a value.

## Output: ops/audit/completeness-fill-2026-07-08.json — array of:
{
  "model": "<provider>/<model_id>",
  "field": "context_window_tokens" | "max_output_tokens",
  "proposed_value": <integer> | null,
  "verbatim_quote": "<exact substring>" | "",
  "source_url": "<url>",
  "accessed_at": "2026-07-08T..Z",
  "status": "FOUND" | "NO_SOURCE" | "AMBIGUOUS" | "NOT_APPLICABLE",
  "note": "<one line, e.g. 'TTS model, no output cap published'>"
}
Also ops/audit/completeness-fill-2026-07-08-summary.md: counts per status per provider, and
the total of FOUND (fillable) vs NO_SOURCE/NOT_APPLICABLE (honest gaps).

## Definition of done
- ops/audit/completeness-fill-2026-07-08.json covers every currently-null field, each with a status.
- Summary written. data/facts.json UNCHANGED. No external repo touched.
