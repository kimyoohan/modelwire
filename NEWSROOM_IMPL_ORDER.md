# NEWSROOM_IMPL_ORDER — explicit implementation checklist

The existing scripts/build_site.py is a stub (83 lines, only copies JSON). Replace it with a
full generator that implements EVERY item below. Do not run the existing stub — rewrite it.

## STEP 1: Rewrite scripts/build_site.py as a complete site generator

The script must, in one `python scripts/build_site.py` run, produce ALL of the following:

### 1a. Per-model pages
- `site/models/<provider>/<model_id>.html` — one page per model in data/facts.json
  - Shows: all fields, every source with verbatim quote, verified_at, changelog history for this model
  - Safe filename rule: replace any char not in [a-zA-Z0-9_-] with underscore
- `site/models/<provider>/<model_id>.json` — the raw JSON entry (machine permalink)
- `site/models/index.html` — links to all model pages grouped by provider
- Add `"permalink": "/models/<provider>/<model_id>.html"` to each entry in site/feed.json

### 1b. News article pages
- Read `content/articles/*.md` (markdown with YAML front-matter: title, date, slug, summary)
- Render each to `site/news/<slug>.html` using a minimal md→html renderer (NO external deps)
  - md renderer must handle: # headings, **bold**, [links](url), - bullet lists, paragraphs
- `site/news/index.html` — reverse-chronological list with title, date, summary

### 1c. Trust pages (render from content/pages/*.md or inline if missing)
- `site/corrections.html` — all changelog entries where type=="corrected", newest first;
  if none, write: "No corrections to date. Correction policy: [link to editorial.html]"
- `site/editorial.html` — render content/pages/editorial-standards.md if it exists, else
  write inline editorial standards (primary sources only, verbatim quotes, collector/reviewer split)
- `site/cite.html` — citation guide: stable URL patterns, BibTeX example, JSON example,
  note to cite BOTH FactQuire AND the primary source

### 1d. Machine discovery files
- `site/rss.xml` — valid RSS 2.0 with ALL news articles + ALL changelog releases as items
  - guid = full URL (https://factquire.com/...), pubDate in RFC 822 format
  - At least 1 item always (use changelog v0.1 if no articles yet)
- `site/llms.txt` — llmstxt.org format:
  ```
  # FactQuire
  > Source-verified facts about commercial LLM APIs — pricing, limits, lifecycle, with primary-source quotes.

  ## Data
  - [Verified model facts feed](https://factquire.com/feed.json): JSON feed, 40+ models, 7+ providers
  - [Full dataset as plain text](https://factquire.com/llms-full.txt): human+machine readable

  ## Updates
  - [Changelog](https://factquire.com/changelog.html): versioned release history
  - [RSS feed](https://factquire.com/rss.xml): subscribe to fact changes and news

  ## Trust
  - [Editorial standards](https://factquire.com/editorial.html): sourcing and verification policy
  - [Corrections](https://factquire.com/corrections.html): all corrections with before/after values
  - [Cite this feed](https://factquire.com/cite.html): citation guide
  - [Audit](https://factquire.com/audit.html): independent comparison vs LiteLLM and models.dev
  ```
- `site/llms-full.txt` — full dataset as plain text: per provider, tab-separated table of
  model_id, input $/1M, output $/1M, context, max_output, status; then changelog summary
- `site/robots.txt` — allow all crawlers, explicitly list AI bots:
  ```
  User-agent: *
  Allow: /

  User-agent: GPTBot
  Allow: /
  User-agent: ClaudeBot
  Allow: /
  User-agent: Claude-Web
  Allow: /
  User-agent: PerplexityBot
  Allow: /
  User-agent: Google-Extended
  Allow: /
  User-agent: Bytespider
  Allow: /
  User-agent: CCBot
  Allow: /
  User-agent: Yeti
  Allow: /

  Sitemap: https://factquire.com/sitemap.xml
  ```
- `site/sitemap.xml` — all pages with <loc>, <lastmod>, <changefreq>, <priority>

### 1e. IndexNow key
- Generate a random 32-char hex key, write it as `site/<key>.txt` (content = key itself)
- Write the key to `ops/indexnow-key.txt`
- Write `scripts/ping_indexnow.py` — reads the key + sitemap URLs, POSTs to
  https://api.indexnow.org/indexnow (do NOT run it in this phase)

### 1f. Verification file passthrough
- Copy any files in `content/rootfiles/` verbatim to `site/`
- Copy any files in `content/well-known/` verbatim to `site/.well-known/`
- Create these content directories if they don't exist

### 1g. Page polish
- Every page: `<title>`, `<meta name="description">`, `<link rel="canonical">`,
  OG tags with `https://factquire.com/...` URLs, RSS autodiscovery link tag
- Footer on every page: links to corrections | editorial | cite
- Nav on every page: Models | News | Changelog | Audit | About
- JSON-LD: Organization on index, NewsArticle on article pages, Dataset on model pages

## STEP 2: Run the generator and validate output

```
python scripts/build_site.py
```

Validate:
- `site/rss.xml` exists and is well-formed XML with ≥1 item
- `site/llms.txt` and `site/llms-full.txt` exist
- `site/robots.txt` exists with GPTBot and Yeti entries
- `site/sitemap.xml` exists
- At least 1 file in `site/models/`
- `site/corrections.html`, `site/editorial.html`, `site/cite.html` exist
- `site/news/index.html` exists

## STEP 3: Write tests

In `tests/test_build_site.py`:
- Test the md→html renderer (headings, bold, links, lists, paragraphs)
- Test the filename sanitizer (special chars → underscore)
- Run `python scripts/validate.py` and confirm exit code 0

## STEP 4: Commit (DO NOT PUSH)

```
git add -A
git commit -m "Implement full newsroom generator: per-model pages, RSS, llms.txt, trust pages, sitemap"
```

## Definition of done
1. `python scripts/build_site.py` runs without errors
2. All files listed in Step 2 validation exist and are non-empty
3. `python tests/test_build_site.py` passes
4. Committed on branch `newsroom` (no push)
