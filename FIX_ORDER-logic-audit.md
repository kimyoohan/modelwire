# FIX_ORDER-logic-audit — triage and fix the 295 logic-audit findings

Input: ops/reports/logic-audit-2026-07-04.md (commit 504a818). The reviewer has already
live-verified one cluster; use that triage below as ground truth for approach.

## Reviewer's triage (already live-verified 2026-07-04)

**Cluster 1 — fireworks *-fast pricing CRITICALs: VALUES ARE CORRECT, QUOTES ARE DEFICIENT.**
https://docs.fireworks.ai/serverless/pricing.md (fetchable as raw markdown) shows
"GLM 5.1 Fast $2.80 / $0.52 / $8.80", "Kimi K2.6 Fast $2.00 / $0.30 / $8.00",
"GLM 5.2 Fast $2.10 / $0.21 / $6.60" — matching stored values exactly (format:
input / cached input / output). Fix = re-capture quotes: for EVERY fireworks entry
flagged CRITICAL or UNSUPPORTED on pricing, replace/add a source entry citing
https://docs.fireworks.ai/serverless/pricing with a verbatim quote CONTAINING that
model's actual price row. Do not change the pricing values.

## What to do with the rest

### A. status CRITICALs ("quote implies preview, stored ga")
Case by case. For each: read the actual quote. If the model itself is labeled
preview/beta on the provider page (e.g. alibaba qwen3.7-max-preview — the ID literally
says preview), change status to "preview". If the word "preview" in the quote refers to
a DIFFERENT model or feature (likely for anthropic/claude-opus-4-6 etc.), the value
stands — instead extend the quote or note so the evidence is unambiguous, and record
the false positive so the checker can be improved.

### B. Other pricing/context CRITICALs and all 162 UNSUPPORTED
For each: fetch the entry's cited source live. Three outcomes:
1. Live page states the stored value → re-capture the quote to CONTAIN the number. 
2. Live page states a DIFFERENT value → this is a REAL data error: fix the value,
   add changelog entry (type "corrected") in a new v0.5 release.
3. Nothing on any official page states it → set field to null + gaps.md entry.

### C. AMBIGUOUS (71 — mostly "1M/128k decimal vs binary")
Do NOT chase these individually. Instead implement a notation policy:
- Add to logic_check.py a documented convention: K-suffix and M-suffix quotes are
  accepted as entailing EITHER decimal or binary reading; store the provider's exact
  printed token (e.g. "128K") in a new optional field `context_window_notation` when
  re-capturing quotes anyway. AMBIGUOUS becomes a WARNING class, not a failure.

### D. Severity gating (IMPORTANT — pipeline is currently broken)
validate.py now exits 1 because it enforces all findings. Change gating:
- logic_check.py exit 1 ONLY on CRITICAL findings.
- UNSUPPORTED/AMBIGUOUS/RULE-* print as warnings (exit 0).
- Add ops/logic-baseline.json: a snapshot of currently-accepted finding keys. validate
  fails only on NEW findings not in the baseline; after this fix round, regenerate the
  baseline so the pipeline is green, and any future regression trips it.

### E. Finish
- py scripts/logic_check.py → must exit 0 after fixes+gating
- py scripts/validate.py → exit 0; py -m unittest discover -s tests → all pass
- py scripts/build_site.py runs clean
- Update ops/reports/logic-audit-2026-07-04.md with a "Resolution" section: counts of
  quote-recaptured / value-corrected / nulled / status-changed / false-positive.
- Commit on main ("Logic audit triage: quote re-capture, real corrections, severity gating").
  DO NOT PUSH. Print the resolution summary table.
