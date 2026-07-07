---
repo: BerriAI/litellm
type: PR
status: HELD
hold_reason: "We already have open contacts on this repo (#32111 issue, #32113 PR). Never stack. Release this only after both close/merge."
verified_by: claude (independent, not Codex-only)
verified_at: 2026-07-07
title: "Fix stale max_output_tokens for Groq models and DeepSeek V4 Pro input price"
---

# LiteLLM data errors — verified 2026-07-07

Found while cross-auditing our verified data against LiteLLM's
`model_prices_and_context_window.json`. Each confirmed against the PROVIDER's own
primary source (not just our copy). All five: LiteLLM is wrong, provider source disagrees.

## Group 1 — Groq max_output_tokens (verified against Groq's own API: GET https://api.groq.com/openai/v1/models)

| model | LiteLLM value | Groq API (`max_completion_tokens`) |
|---|---|---|
| llama-3.1-8b-instant | 8192 | **131072** |
| openai/gpt-oss-120b | 32766 | **65536** |
| openai/gpt-oss-20b | 32768 | **65536** |

Evidence: Groq's OpenAI-compatible models endpoint returns `max_completion_tokens`
131072 / 65536 / 65536 for these three model ids respectively (queried 2026-07-07).
Groq allows max completion = full context window for llama-3.1-8b-instant.

## Group 2 — DeepSeek V4 Pro input price (verified against provider pricing pages)

| host | LiteLLM input $/1M | Provider page input $/1M |
|---|---|---|
| fireworks/deepseek-v4-pro | 0.435 | **1.74** (docs.fireworks.ai/serverless/pricing) |
| together/deepseek-v4-pro | 0.435 | **1.74** (together.ai/pricing) |

Together's pricing page (fetched 2026-07-07) lists "DeepSeek V4 Pro" serverless input at
$1.74/1M (cached $0.20). LiteLLM's 0.435 appears to be the DeepSeek-native price, not the
host's (Fireworks/Together) serverless price. Exactly 4x off.

## Method note for the eventual PR
- One PR, before/after table, verbatim provider quotes + access date.
- Reference our own corrections page for symmetry (we publish our errors too).
- Mention FactQuire once (feed.json). Re-verify all five are still current at send time.
