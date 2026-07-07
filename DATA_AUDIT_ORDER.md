# DATA_AUDIT_ORDER — re-source 12 suspect numeric fields against primary sources

Today is 2026-07-07. You (Codex) have network access. Your job is EVIDENCE COLLECTION only.
DO NOT edit data/facts.json. DO NOT touch any external repo. Produce ONE findings file.

## Why
FactQuire's entire promise is "every number carries a primary-source quote." A cross-check
against LiteLLM + our own logic-baseline surfaced 12 numeric fields that are either
unsupported by their stored quote or contradicted by an external dataset. We must re-verify
each against the PROVIDER'S OWN primary source and record the truth with a verbatim quote.

## The 12 targets

### Group A — pricing with NO supporting quote (from ops/logic-baseline.json UNSUPPORTED)
1. perplexity/sonar        pricing.input_per_mtok   (we store 0.25)
2. perplexity/sonar        pricing.output_per_mtok  (we store 2.5)
3. perplexity/sonar        pricing.cached_input_per_mtok (we store 0.0625)
4. perplexity/sonar-pro    pricing.input_per_mtok   (we store a value; quote is tiered, tier not documented)
5. perplexity/sonar-pro    pricing.output_per_mtok
6. perplexity/sonar-reasoning-pro pricing.input_per_mtok
7. perplexity/sonar-reasoning-pro pricing.output_per_mtok
   Primary source: https://docs.perplexity.ai/guides/pricing  and  https://www.perplexity.ai/ (API pricing).
   NOTE: Perplexity pricing has per-token AND per-request/search fees, and varies by tier.
   If the per-token price genuinely depends on an undocumented tier, say so — mark AMBIGUOUS,
   do NOT invent a single number.

### Group B — values an external dataset (LiteLLM) contradicts (possible OUR error)
8.  groq/llama-3.1-8b-instant  max_output_tokens  (we store 131072 = full context window; LiteLLM says 8192)
9.  groq/openai/gpt-oss-120b   max_output_tokens  (we store 65536; LiteLLM says 32766)
10. groq/openai/gpt-oss-20b    max_output_tokens  (we store 65536; LiteLLM says 32768)
    Primary source: https://console.groq.com/docs/models  (try the JSON/API list too:
    https://api.groq.com/openai/v1/models is auth-gated; the docs page is the public source).
11. fireworks/deepseek-v4-pro  pricing.input_per_mtok  (we store 1.74; LiteLLM says 0.435 — exactly 4x)
12. together/deepseek-v4-pro   pricing.input_per_mtok  (we store 1.74; LiteLLM says 0.435 — exactly 4x)
    Primary sources: https://fireworks.ai/pricing , https://docs.fireworks.ai/ ,
    https://www.together.ai/pricing . Also sanity-check: does "DeepSeek V4" even exist as a
    real released model on these hosts, or is our record itself spurious? Report what you find.

## Method (per target)
1. Fetch the provider's primary source. If the page is JS-rendered and returns no numbers,
   try the docs markdown endpoint, an API pricing endpoint, or the provider's pricing JSON.
   Record which URL actually yielded the number.
2. Extract the CURRENT real value with a VERBATIM quote (exact substring, incl. $ and units).
3. Compare to our stored value.

## Output: write ops/audit/data-audit-2026-07-07.json — array of:
{
  "model": "<provider>/<model_id>",
  "field": "<field>",
  "our_value": <current stored value>,
  "primary_value": <value found in primary source, or null if unobtainable>,
  "verbatim_quote": "<exact substring containing the number, or empty>",
  "source_url": "<url that actually yielded it>",
  "accessed_at": "2026-07-07T..Z",
  "verdict": "OURS_RIGHT" | "OURS_WRONG" | "AMBIGUOUS" | "SOURCE_UNREACHABLE",
  "note": "<one line: e.g. tier that applies, or 'model may not exist'>"
}
Also write ops/audit/data-audit-2026-07-07-summary.md: counts per verdict, and any target
where you could not reach a clean primary source (be honest — SOURCE_UNREACHABLE is a valid,
useful result; do NOT guess a number to fill a cell).

## Definition of done
- ops/audit/data-audit-2026-07-07.json exists with all 12 targets.
- ops/audit/data-audit-2026-07-07-summary.md exists.
- data/facts.json is UNCHANGED (git status clean for it). No external repo contacted.
