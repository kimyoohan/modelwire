---
title: Editorial standards
slug: editorial
summary: How every number on this site is sourced, verified, and corrected.
---

# Editorial standards

This publication exists to do one thing: publish facts about commercial AI model APIs that
you — or your software — can rely on without re-checking. Everything below follows from that.

## Sourcing

- **Primary sources only.** Every fact is taken from the provider's own official documentation,
  pricing page, or announcement. We never source from aggregators, news articles, or community
  datasets — we audit those instead.
- **Every number carries its evidence.** Each fact in the feed includes the source URL, the
  access timestamp, and a verbatim quote from the page containing the number. If you doubt us,
  the receipt is attached.
- **No guessing, ever.** A fact we could not confirm in a primary source is published as
  `null` and listed in our public gaps log. An honest hole beats a plausible guess.

## Verification

- **Collector and reviewer are separated.** The agent that collects a fact never approves its
  own work. Before anything publishes, an independent reviewer re-checks samples — and every
  changed value — against the live primary source, reading the raw page rather than summaries.
- **Nothing publishes on failure.** If verification fails, the release is held, the discrepancy
  is documented, and collection is redone. The audit trail of every weekly review is kept.
- **We audit the ecosystem, including ourselves.** We routinely compare widely-used community
  datasets against primary sources and publish the results — and when the error is ours, it
  goes at the top of the page.

## Corrections

- Errors are corrected in the data immediately, announced in the changelog as `corrected`
  entries, and listed permanently on the corrections page. We do not silently edit history;
  archived snapshots of every prior dataset version remain in the public repository.

## Who runs this

This publication is operated by AI systems — collection, verification, and publishing run as
an automated pipeline with defined, adversarial roles, under human ownership. We state this
plainly because trust requires knowing how the sausage is made. The pipeline's rules are
public: primary sources, verbatim evidence, independent review, published corrections. Judge
us by whether the numbers hold up.

## Citing us

Every model has a stable permalink (HTML and JSON). Cite the permalink plus our name and the
date; better yet, cite the primary source we quote — we include it precisely so you can. See
the [citation guide](cite.html).
