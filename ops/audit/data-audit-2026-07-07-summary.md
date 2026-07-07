# Data audit summary - 2026-07-07

## Verdict counts

| Verdict | Count |
| --- | ---: |
| OURS_RIGHT | 12 |
| OURS_WRONG | 0 |
| AMBIGUOUS | 0 |
| SOURCE_UNREACHABLE | 0 |

## Source reachability

All 12 targets were resolved from provider primary sources. No target required `SOURCE_UNREACHABLE`.

## Notes

- `perplexity/sonar` is supported by the Perplexity Agent API Models table at $0.25 input, $2.50 output, and $0.0625 cache per 1M tokens. The separate Sonar API pricing table lists `Sonar` at $1/$1 plus request fees, so the API surface matters.
- `perplexity/sonar-pro` and `perplexity/sonar-reasoning-pro` have fixed token prices in the Perplexity pricing table. Their request fees are separately tiered by search context size, but the token prices audited here are not tier-dependent.
- Groq's public models page lists `llama-3.1-8b-instant` max completion tokens as 131,072 and both `openai/gpt-oss-*` models as 65,536.
- Fireworks and Together both currently list DeepSeek V4 Pro as a hosted model. Fireworks standard serverless input is $1.74 per 1M tokens; Together serverless input is also $1.74 per 1M tokens.
