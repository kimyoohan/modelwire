---
title: "AWS quietly doubled Bedrock prices for legacy Claude models — and cost trackers haven't caught up"
date: 2026-07-04
slug: bedrock-extended-access-price-doubling
summary: "Amazon Bedrock's 'Public Extended Access' pricing, effective December 1, 2025, doubled per-token prices for Claude 3.5 Sonnet v2. Seven months later, at least one widely used open-source cost tracker still carried the old prices — we verified against the primary source and submitted the fix."
---

# AWS quietly doubled Bedrock prices for legacy Claude models — and cost trackers haven't caught up

If your cost dashboard says a Bedrock call to Claude 3.5 Sonnet v2 costs $3 per million
input tokens, your dashboard is seven months out of date — and it is off by exactly 2x.

## What changed

Amazon moved Claude 3.5 Sonnet v2 on Bedrock to what its pricing page calls
**Public Extended Access**, effective December 1, 2025. The AWS Bedrock pricing page
(https://aws.amazon.com/bedrock/pricing/, accessed 2026-07-04) lists for
Anthropic Claude 3.5 Sonnet v2:

> "$6.00" per 1M input tokens, "$30.00" per 1M output tokens,
> cache write "$7.50" per 1M, cache read "$0.60" per 1M
> (Public Extended Access, effective December 1, 2025)

That is double the long-familiar $3.00 / $15.00 — the price most of the ecosystem
memorized in 2024 and hardcoded everywhere.

## Why it went unnoticed

Prices that change on a provider's page do not change in the JSON files, cost packages,
and dashboards that were built when the old price was true. Facts rot silently.

While cross-auditing community datasets against primary sources on 2026-07-04, we found
[Helicone](https://github.com/Helicone/helicone)'s cost package still carried
$3.00 / $15.00 for `claude-3.5-sonnet-v2:bedrock`. The code is correct code — it is
simply code that does not know the world changed underneath it. We verified the current
values against the AWS pricing page and submitted the correction upstream:
[Helicone/helicone#5709](https://github.com/Helicone/helicone/pull/5709).

Notably, the entry's cache multipliers (1.25x write, 0.1x read) were still exactly right
against the *new* base price — evidence the structure was sound and only the base facts
had drifted.

## The FactQuire entry

Our machine-readable record for this model, with the verbatim source quote and access
timestamp, is here:

- https://factquire.com/models/amazon/anthropic_claude-3-5-sonnet-20241022-v2_0.json

Every field in the FactQuire feed carries a quote from the primary source and the time
we read it, so anyone can re-verify the claim without trusting us — including when we
are the ones who turn out to be wrong. (Our own published corrections are at
https://factquire.com/corrections.html.)

## The general lesson

Model pricing is not static reference data; it is news. Prices change with an effective
date, quietly, on a page nobody re-reads. Any system that stores a price without storing
*when and where it was read* will eventually report costs that are confidently wrong —
in this case, by 2x for seven months.
