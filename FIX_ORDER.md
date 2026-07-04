# FIX_ORDER — alibaba context_window_tokens not source-supported (wave-2 review)

## Reproduction (exact)
Reviewer cross-checked data/facts.json (commit 4d5efa1) against raw HTML of
https://www.alibabacloud.com/help/en/model-studio/model-pricing (fetched 2026-07-04):

1. `alibaba/qwen3.6-flash` has `context_window_tokens: 256000`, but the SAME pricing page
   shows qwen3.6-flash with BOTH tiers: `0<Token≤256K $0.25 $1.5` AND `256K<Token≤1M $1 $4`.
   The stored source quote truncated the second tier. By the entry's own inference logic
   (tier upper bound = context), the value would be 1M — the stored 256000 contradicts its
   own source. Verbatim from raw HTML:
   `qwen3.6-flash ... 0<Token≤256K $0.25 $1.5 ... 256K<Token≤1M $1 $4`
2. `alibaba/qwen3.7-plus` has `context_window_tokens: 1000000` inferred from the pricing
   tier `256K<Token≤1M`. A pricing tier bound is NOT an explicit context window spec.

Pricing values themselves all PASSED review (flash $0.25/$1.5, plus $0.4/$1.6,
3.6-plus $0.5/$3 — all confirmed against raw HTML). Only fix context fields.

## What to do
For ALL six new alibaba entries (qwen3.7-plus, qwen3.7-plus-2026-05-26, qwen3.6-plus,
qwen3.6-plus-2026-04-02, qwen3.6-flash, qwen3.6-flash-2026-04-16):

1. Find Alibaba's official per-model spec that states the context window EXPLICITLY
   (e.g. the Model Studio "Models" documentation model list table with a
   "Context window (tokens)" / "Maximum input" column, or the per-model detail page).
   Likely candidates: https://www.alibabacloud.com/help/en/model-studio/models
   (follow the "Text generation" model list links) or the Qwen API reference tables.
2. Set `context_window_tokens` (and `max_output_tokens` if the page states it) from that
   explicit spec, and add/replace a source entry with url + accessed_at + verbatim quote
   that CONTAINS the number.
3. If no official page states the number explicitly, set the field to null and record in
   gaps.md ("pricing tiers imply ≤1M input but no explicit context window spec found").
4. Do NOT touch pricing fields. Do NOT touch non-alibaba entries.
5. Run `py scripts/validate.py` (exit 0) and `py scripts/build_site.py` (no error).
6. Commit on main: "Fix alibaba context windows: explicit source or null". DO NOT PUSH.

## Definition of done
- All six alibaba entries have context_window_tokens either backed by a quote containing
  the exact number, or null + gaps.md entry
- validate.py exit 0, build committed, not pushed
- Print final table: model | old ctx | new ctx | evidence quote fragment
