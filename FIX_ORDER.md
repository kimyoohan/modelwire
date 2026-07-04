# FIX_ORDER — ModelWire MVP review findings (2026-07-04)

Independent cross-review was done against LIVE official pages using samples different
from the WORK_ORDER spot-check contract. Result: FAIL on one blocking issue.

## Issue 1 (BLOCKING): xAI cached input pricing not supported by the live source

- Affected: all 5 `xai` entries — `cached_input_per_mtok` is `0.2` on every one.
- Your source quote for grok-4.3 claims the Chat API table at
  https://docs.x.ai/developers/pricing has columns
  `Model Context Input Cached input Output` with `$0.20` values.
- Reproduction (verified 2026-07-04 during review): fetching that page shows the Chat API
  table has exactly 4 columns — `Model | Context | Input / 1M tokens | Output / 1M tokens`.
  The grok-4.3 row is `grok-4.3 | 1M | $1.25 | $2.50`. There is NO "Cached input" column
  and no `$0.20` figure in the table. The page mentions cached prompt tokens only as a
  token-cost concept, with no separate published rate.
- Required fix:
  1. Re-fetch the live page yourself and record what it actually says.
  2. If cached input pricing for xAI models is published on some OTHER official xAI page
     (models page, caching docs), cite THAT url with a verbatim quote containing the number.
  3. If no official published rate exists, set `cached_input_per_mtok` to `null` for all
     xai entries, remove the claim from the quotes, and add a line per model to `gaps.md`.
  4. Quotes must be text actually present on the cited page at fetch time. Never reconstruct
     a table from memory.

## Issue 2 (MINOR): Cohere legacy status check

- `command-r-plus-08-2024`, `command-r-03-2024`, `command-r-plus-04-2024`, `command`,
  `command-light` pricing appears on https://cohere.com/pricing only under the
  "legacy models" FAQ, not as current offerings.
- Check https://docs.cohere.com/docs/models for each: if docs mark them "Live", keep
  `status: "ga"` but add `notes: "Listed as legacy on Cohere pricing page"`. If docs mark
  them deprecated/retired, set status accordingly with a supporting quote.

## Definition of done
1. Both issues resolved as specified; every changed value backed by a verbatim quote from
   the cited live page.
2. `py scripts/validate.py` exits 0.
3. `py scripts/build_site.py` re-run so `site/feed.json` matches `data/facts.json`.
4. Changes committed with a message referencing this FIX_ORDER.
