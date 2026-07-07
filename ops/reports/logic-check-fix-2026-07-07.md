# Logic Check Fix Proof - 2026-07-07

## Clean run command output

```text
COMMAND: py scripts\logic_check.py --today 2026-07-07
EXIT: 0
SUMMARY: Logic check passed with warnings: 271 accepted warning findings across 135 entries and 697 audited Part A fields.
FINDING COUNT: 271
```

## Pass criterion A: target false positives eliminated

| Entry | Field | Findings in clean output |
| --- | --- | ---: |
| perplexity/perplexity/sonar | pricing.input_per_mtok | 0 |
| perplexity/perplexity/sonar | pricing.output_per_mtok | 0 |
| perplexity/perplexity/sonar | pricing.cached_input_per_mtok | 0 |
| perplexity/sonar-pro | pricing.input_per_mtok | 0 |
| perplexity/sonar-pro | pricing.output_per_mtok | 0 |
| perplexity/sonar-reasoning-pro | pricing.input_per_mtok | 0 |
| perplexity/sonar-reasoning-pro | pricing.output_per_mtok | 0 |

Command output for A:

```text
COMMAND: py scripts\logic_check.py --today 2026-07-07
EXIT: 0
SUMMARY: Logic check passed with warnings: 271 accepted warning findings across 135 entries and 697 audited Part A fields.
perplexity/perplexity/sonar | pricing.input_per_mtok | findings=0
perplexity/perplexity/sonar | pricing.output_per_mtok | findings=0
perplexity/perplexity/sonar | pricing.cached_input_per_mtok | findings=0
perplexity/sonar-pro | pricing.input_per_mtok | findings=0
perplexity/sonar-pro | pricing.output_per_mtok | findings=0
perplexity/sonar-reasoning-pro | pricing.input_per_mtok | findings=0
perplexity/sonar-reasoning-pro | pricing.output_per_mtok | findings=0
```

## Pass criterion B: deliberately wrong values still caught

| Mutation | Exit | Before count | After count | Caught | Relevant finding |
| --- | ---: | ---: | ---: | --- | --- |
| perplexity/sonar pricing.input_per_mtok 0.25 -> 0.99 | 0 | 271 | 272 | True | - perplexity/perplexity/sonar \| pricing.input_per_mtok \| UNSUPPORTED \| no stored quote contains numeric evidence for stored value 0.99 |
| perplexity/sonar-pro pricing.output_per_mtok 15 -> 44 | 1 | 271 | 272 | True | - perplexity/sonar-pro \| pricing.output_per_mtok \| CRITICAL \| source assigned to field has numeric value(s) $10, $14, $15, $2, $3, $6, $8 but none match stored value 44 |
| perplexity/sonar pricing.cached_input_per_mtok 0.0625 -> 0.5 | 0 | 271 | 272 | True | - perplexity/perplexity/sonar \| pricing.cached_input_per_mtok \| UNSUPPORTED \| no stored quote contains numeric evidence for stored value 0.5 |
| groq/llama-3.1-8b-instant max_output_tokens 131072 -> 999999 | 1 | 271 | 273 | True | - groq/llama-3.1-8b-instant \| max_output_tokens \| CRITICAL \| source assigned to field has numeric value(s) 05, 075, 08, 120, 131,072, 15, 20, 30 but none match stored value 999999 |

Command outputs for B:

```text
MUTATION: perplexity/sonar pricing.input_per_mtok 0.25 -> 0.99
COMMAND: py scripts\logic_check.py --today 2026-07-07 --facts <temp facts copy>
EXIT: 0
SUMMARY: Logic check passed with warnings: 272 accepted warning findings across 135 entries and 697 audited Part A fields.
BEFORE COUNT: 271
AFTER COUNT: 272
CAUGHT: True
RELEVANT FINDINGS:
- perplexity/perplexity/sonar | pricing.input_per_mtok | UNSUPPORTED | no stored quote contains numeric evidence for stored value 0.99
```

```text
MUTATION: perplexity/sonar-pro pricing.output_per_mtok 15 -> 44
COMMAND: py scripts\logic_check.py --today 2026-07-07 --facts <temp facts copy>
EXIT: 1
SUMMARY: Logic check failed: 1 critical findings, 271 warnings across 135 entries and 697 audited Part A fields.
BEFORE COUNT: 271
AFTER COUNT: 272
CAUGHT: True
RELEVANT FINDINGS:
- perplexity/sonar-pro | pricing.output_per_mtok | CRITICAL | source assigned to field has numeric value(s) $10, $14, $15, $2, $3, $6, $8 but none match stored value 44
```

```text
MUTATION: perplexity/sonar pricing.cached_input_per_mtok 0.0625 -> 0.5
COMMAND: py scripts\logic_check.py --today 2026-07-07 --facts <temp facts copy>
EXIT: 0
SUMMARY: Logic check passed with warnings: 272 accepted warning findings across 135 entries and 697 audited Part A fields.
BEFORE COUNT: 271
AFTER COUNT: 272
CAUGHT: True
RELEVANT FINDINGS:
- perplexity/perplexity/sonar | pricing.cached_input_per_mtok | UNSUPPORTED | no stored quote contains numeric evidence for stored value 0.5
```

```text
MUTATION: groq/llama-3.1-8b-instant max_output_tokens 131072 -> 999999
COMMAND: py scripts\logic_check.py --today 2026-07-07 --facts <temp facts copy>
EXIT: 1
SUMMARY: Logic check failed: 1 critical findings, 272 warnings across 135 entries and 697 audited Part A fields.
BEFORE COUNT: 271
AFTER COUNT: 273
CAUGHT: True
RELEVANT FINDINGS:
- groq/llama-3.1-8b-instant | max_output_tokens | CRITICAL | source assigned to field has numeric value(s) 05, 075, 08, 120, 131,072, 15, 20, 30 but none match stored value 999999
```
