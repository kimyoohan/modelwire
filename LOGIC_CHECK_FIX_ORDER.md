# LOGIC_CHECK_FIX_ORDER — remove logic_check false positives WITHOUT creating false negatives

Today is 2026-07-07. Model reasoning: high. This touches product integrity — the whole
value proposition is "every number is backed by a primary-source quote." A checker that is
too LOOSE (misses a wrong number) is far worse than one that is too strict. Optimize for
zero false negatives first, then reduce false positives.

## Background
`scripts/logic_check.py` runs quote-entailment: for each numeric field, the stored value
must appear as numeric evidence in a stored source quote. It currently produces FALSE
POSITIVES that were all dumped into `ops/logic-baseline.json` (191 UNSUPPORTED), making the
gate meaningless. We verified by hand (2026-07-07) that at least these 7 are false positives
— the value is CORRECT and the quote DOES contain it, the parser just fails to see it:

Two known false-positive mechanisms:
1. **Bare-number price tables (no `$`).** `price_candidates()` only matches `$`-prefixed
   numbers. Perplexity quotes list prices as bare numbers, e.g. the stored quote for
   `perplexity/sonar` is: "... `perplexity/sonar` 0.25 2.50 0.0625". Value 0.25 is right
   there but has no `$`, so the parser finds nothing → UNSUPPORTED.
2. **Multi-row quotes tripping the tiered-pricing rule.** `perplexity/sonar-pro` and
   `sonar-reasoning-pro` quotes captured several models' rows, so multiple numbers appear
   (10,14,15,2,3,6). The tiered-pricing rule reads that as "one model, undocumented tier"
   and flags it, when really they are different models' prices.

## Task
Fix `scripts/logic_check.py` so both mechanisms stop firing, WITHOUT weakening detection of
genuinely-wrong numbers. Guidance on how (you may choose better):
- For (1): allow a bare-number match for price fields, but ONLY when the matched number is
  an EXACT match to the stored value AND its surrounding window (± ~40 chars) contains a
  price cue (any of: `$`, `/1M`, `/1K`, `per 1M`, `per 1K`, `input`, `output`, `cache`,
  `price`, `token`, `$/1M`). This keeps specificity: an unrelated bare number elsewhere in
  the quote must not count as evidence.
- For (2): the tiered-pricing rule must not fire merely because a quote contains several
  numbers. Only treat it as tiered when actual tier markers (e.g. "tier", "first N",
  ">N tokens", "context size", volume thresholds) sit in the SAME row/clause as the price.
  Different models on different rows are not tiers.

## PASS CRITERIA — these are hard, non-negotiable, test both directions

### A. These must STOP being flagged (false positives eliminated).
After the fix, running logic_check over `data/facts.json`, NONE of these may appear as a
finding (they are all verified-correct as of 2026-07-07):
- perplexity/sonar : pricing.input_per_mtok (0.25), output_per_mtok (2.5), cached_input_per_mtok (0.0625)
- perplexity/sonar-pro : pricing.input_per_mtok (3), output_per_mtok (15)
- perplexity/sonar-reasoning-pro : pricing.input_per_mtok (2), output_per_mtok (8)

### B. These deliberately-WRONG values MUST still be flagged (no false negatives).
Create a throwaway copy of facts.json in a temp path, mutate ONLY the listed field to the
wrong value shown, run logic_check on the copy, and confirm each still produces an
UNSUPPORTED (or equivalent CRITICAL/warning) finding. DO NOT mutate the real facts.json.
- perplexity/sonar input_per_mtok changed 0.25 → 0.99  → MUST flag (0.99 not in quote)
- perplexity/sonar-pro output_per_mtok changed 15 → 44 → MUST flag (44 not in quote)
- perplexity/sonar cached_input changed 0.0625 → 0.5  → MUST flag
- any groq model max_output_tokens changed to 999999   → MUST flag
Write the exact before/after finding counts for each mutation to prove the checker still bites.

### C. Regenerate the baseline honestly.
After the fix, regenerate `ops/logic-baseline.json` from the CURRENT clean run. Then produce
`ops/reports/baseline-regen-2026-07-07.md` with:
- old UNSUPPORTED count (191) vs new count,
- a breakdown of what REMAINS by field/class,
- for each REMAINING finding, one line: is it a real evidence gap (quote genuinely lacks the
  number) or a still-unhandled parser case? Be honest — remaining real gaps are fine and
  expected; do not force them to zero by loosening the parser.

## Definition of done
- scripts/logic_check.py updated; `py scripts/logic_check.py` (or however validate.py calls it) runs clean.
- Pass criteria A (0 of the 7 flagged) and B (all 4 mutations still flagged) both demonstrably met,
  with the command outputs saved to ops/reports/logic-check-fix-2026-07-07.md.
- Baseline regenerated + ops/reports/baseline-regen-2026-07-07.md written.
- data/facts.json UNCHANGED. No external repo touched.
