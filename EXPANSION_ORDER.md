# EXPANSION_ORDER — coverage expansion to 100+ models

Depth makes the feed citable. Expand data/facts.json from 40 to **≥ 100 models** while keeping
the sourcing discipline EXACTLY as strict as before (WORK_ORDER phase 1 rules: primary sources
only, verbatim quote containing every number, null + gaps.md when unconfirmed, never guess,
never reconstruct tables from memory). Quota is not a constraint — thoroughness is the product.

## New providers to add (official first-party APIs only)
- amazon (Nova family via AWS Bedrock pricing — us-east-1 on-demand, note region in `notes`)
- meta (Llama API, if commercially purchasable today; else skip and record in gaps.md)
- alibaba (Qwen via Model Studio / DashScope international pricing)
- moonshot (Kimi API), zhipu (Z.ai / GLM API), minimax, deepseek (already have — extend if more SKUs)
- groq, together, fireworks (serving platforms: only THEIR official per-token prices for openly
  listed models; set provider to the platform, put upstream model family in display_name/notes)
- perplexity (Sonar API), cohere (extend), xai/google/openai/anthropic/mistral (any missing
  currently-purchasable SKUs, e.g. embeddings excluded — chat/completion models only)

## Rules refinements
- Chat/completion/reasoning models only (skip embedding/rerank/image/audio-only SKUs for now).
- Platform (groq/together/fireworks) entries: status "ga" only if listed on their public pricing
  page today; capture context window from their model pages, not upstream vendor docs.
- Tiered pricing (e.g. long-context surcharges): record the BASE tier in pricing fields and the
  tier structure in `notes`, quote must cover the base numbers.
- Currency: if a provider prices in non-USD (e.g. CNY), convert ONLY if the provider publishes
  official USD prices on an international page; otherwise record in gaps.md and skip the model.
- Update alias_map.json for new models present in LiteLLM/models.dev (audit coverage grows too).

## Definition of done
1. data/facts.json ≥ 100 entries, ≥ 13 providers; `py scripts/validate.py` exits 0 (update the
   validator's minimums to 100/13).
2. New changelog release (minor bump): summary "Coverage expansion", `added` entries for every
   new model (use diff_facts.py against the pre-expansion archive copy — archive first, as in
   UPDATE_ORDER step 1).
3. gaps.md updated; `py scripts/build_site.py` regenerated; tests still pass.
4. Spot-check contract: reviewer will re-verify random new entries against live official pages —
   same standard as phase 1.
5. Incremental commits per provider. DO NOT PUSH.
