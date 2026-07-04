# EXPANSION2_ORDER — Wave-2 gap fill (candidate models found missing vs research)

## Context
data/facts.json currently has 123 models. Cross-checking against research/wave2 output
found the candidate models below missing. Your job: **verify each against the provider's
LIVE primary source today** and add ONLY the ones currently listed/offered. Some candidates
may be deprecated (especially the Groq ones) — if a model is not on the provider's current
docs/pricing page, DO NOT add it; record it in gaps.md instead with the reason.

## Candidates to verify and (if live) add

### perplexity (high value — we only have sonar)
- sonar-pro
- sonar-reasoning
- sonar-reasoning-pro
- Source: https://docs.perplexity.ai/getting-started/pricing (JS-rendered; use the docs
  markdown endpoints or any official plain source you can fetch; quote verbatim)

### alibaba (we only have qwen3-max line; the plus/turbo/flash lines are missing)
- Current non-max commercial lines on https://www.alibabacloud.com/help/en/model-studio/models
  (e.g. qwen-plus / qwen-turbo / qwen-flash or their current qwen3.x equivalents —
  add whatever the page lists TODAY as the current plus/turbo/flash tier, with exact IDs)

### fireworks
- llama-v3p3-70b-instruct
- qwen3-235b-a22b
- qwen2p5-vl-32b-instruct
- firefunction-v2
- Source: https://fireworks.ai/pricing + model library. Add only if currently listed.

### together
- Qwen2.5-7B-Instruct-Turbo (exact current ID from together.ai/pricing)

### groq (VERIFY CAREFULLY — likely deprecated)
- mixtral-8x7b-32768
- gemma2-9b-it
- Source: https://console.groq.com/docs/models (raw HTML is fetchable). If these are gone
  or marked deprecated, do NOT add; note in gaps.md.

### amazon bedrock (third-party hosted model — include hosting note)
- anthropic.claude-3-5-sonnet (current v1/v2 ID on the Bedrock pricing page).
  provider stays "amazon", note must say "hosted third-party model (Anthropic) on Bedrock".
  Add only if it is on the current Bedrock pricing page with explicit per-token prices.

## Rules (same as EXPANSION_ORDER)
1. Primary sources only. Every entry: every source has url + accessed_at + verbatim quote
   covering the values you record. No guesses; unknown → null + gaps.md entry.
2. Schema: follow schema/model_fact.schema.json exactly (pricing.input_per_mtok etc.),
   match the style of existing entries in data/facts.json.
3. Before editing, archive data/facts.json → data/archive/facts-2026-07-04-pre-exp2.json
   (if a file of that name exists, use -pre-exp2b).
4. After adding: run `py scripts/diff_facts.py <archive> data/facts.json`, create a new
   release entry v0.4 in data/changelog.json ("Wave-2 gap fill"), summary of adds.
5. Run `py scripts/validate.py` — must exit 0.
6. Run `py scripts/build_site.py` — must complete without error.
7. Commit everything on main with message "Wave-2 gap fill: <N> models added".
   **DO NOT PUSH.** The reviewer publishes after independent cross-verification.

## Definition of done
- Every candidate above either added (with quotes) or recorded in gaps.md with reason
- validate.py exit 0, build_site.py OK, committed (not pushed)
- Print a final summary table: model | added/skipped | source URL
