---
title: "The same DeepSeek V4 Pro costs 4x more on Together and Fireworks than on DeepSeek's own API"
date: 2026-07-07
slug: deepseek-v4-pro-host-pricing-4x
summary: "DeepSeek V4 Pro is an open-weight model you can call three ways. On DeepSeek's own API it is $0.435 per 1M input tokens; on Together and Fireworks the same model is $1.74 — exactly 4x more. A per-model price is a category error for open-weight models, and at least one widely used cost tracker had the hosted entries at the native price."
---

# The same DeepSeek V4 Pro costs 4x more on Together and Fireworks than on DeepSeek's own API

If your cost model has one number for "DeepSeek V4 Pro," it is wrong for two of the three
places you can actually call it. The model is open-weight, so it is served by multiple
providers — and each provider prices its own serving, not DeepSeek's.

## The three prices for one model

All figures per 1M tokens, from each host's own pricing page, accessed 2026-07-07:

- **DeepSeek** (native API) — input **$0.435**, output **$0.87**, cache-hit $0.003625
- **Together** — input **$1.74**, output **$3.48**, cached input $0.20
- **Fireworks** — input **$1.74**, output **$3.48**, cache $0.145

Sources, verbatim:

- DeepSeek, https://api-docs.deepseek.com/quick_start/pricing —
  the `deepseek-v4-pro` column reads cache-miss input **$0.435**, output **$0.87**,
  cache-hit **$0.003625** per 1M tokens.
- Together, https://www.together.ai/pricing —
  "DeepSeek V4 Pro ... **$1.74** ... $0.20 (cached) ... **$3.48**".
- Fireworks, https://fireworks.ai/pricing —
  "DeepSeek V4 Pro" serverless: "**$1.74 / $0.145 / $3.48**" (input / cache / output).

The hosted input price ($1.74) is **exactly 4x** the DeepSeek-native price ($0.435).
Output ($3.48) is exactly 4x native ($0.87). This is not a rounding artifact — it is the
gap between a model author's first-party API and third-party serving of the same weights.

## Why the same weights cost 4x

An open-weight model is not one product with one price. DeepSeek sets the price for its own
hosted API. Together and Fireworks each stand up their own inference stack — GPUs, batching,
uptime, margins — and price that. So "DeepSeek V4 Pro pricing" has no single answer; it is a
property of the *host*, not the model. A cost estimate that stores one number per model,
rather than one per model-and-host, will be off by multiples the moment traffic moves to a
different provider — which is exactly what a router or gateway is built to do.

## Where it already bit

While cross-auditing community datasets against primary sources on 2026-07-07, we found
[LiteLLM](https://github.com/BerriAI/litellm)'s widely used
`model_prices_and_context_window.json` listing the **Together and Fireworks** DeepSeek V4 Pro
entries at **$0.435** input — the DeepSeek-*native* price, not the hosts' $1.74. Any cost
dashboard built on that entry would under-report the true hosted spend by 4x. The code is
not buggy; it simply inherited DeepSeek's native price for a row that is billed by Together
and Fireworks. We verified the current host prices against each host's own page and are
contributing the correction upstream.

(Our own data drifts too. When we are the ones who turn out to be wrong, we publish it:
https://factquire.com/corrections.html)

## The general rule

For any open-weight model — DeepSeek, Llama, Qwen, Mixtral, GPT-OSS — "the price" is a
question that only makes sense once you name the host. Store the host with the price, or your
cost math is right only by coincidence.

Machine-readable records for each host, every field carrying its primary-source quote:

- https://factquire.com/models/deepseek/deepseek-v4-pro.json
- https://factquire.com/models/together/deepseek-v4-pro.json
- https://factquire.com/models/fireworks/deepseek-v4-pro.json
