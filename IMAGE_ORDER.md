# IMAGE_ORDER — site visual assets (favicon + OG card)

Produce brand-neutral visual assets for the ModelWire site ("ModelWire" is a provisional name —
do NOT render the name into any image; use an abstract mark only).

## Assets

### 1. Abstract mark → favicon
- Use your BUILT-IN IMAGE GENERATION tool (mandatory — see Rules) to create ONE abstract mark:
  a clean geometric "signal pulse / wire" motif (a horizontal line with a sharp pulse spike),
  2-color: near-black (#111) mark on transparent background, flat vector-look, thick strokes,
  centered, generous margins. No text, no letters, no gradients.
- Post-process with PIL: trim margins, produce `site/assets/favicon-512.png` (512x512 RGBA),
  `site/assets/favicon-32.png`, and `site/favicon.ico` (32px). Keep the transparent background.

### 2. OG card
- Compose `site/assets/og-card.png` (1200x630) WITH CODE (PIL) — not the image model:
  off-white background (#FAFAF7), the mark placed left, and text rendered by PIL using a
  system font (e.g. Segoe UI / Arial): title "Verified facts about commercial LLM APIs",
  subtitle "40+ models · 7 providers · every number source-quoted". Dark text (#111).
  Text via PIL guarantees crisp rendering at this size; the image model is only for the mark.

### 3. Wire-up
- Add to all three pages' <head>: favicon links and OG/Twitter meta tags
  (og:title "ModelWire — verified LLM API facts", og:description, og:image with the FULL URL
  https://kimyoohan.github.io/modelwire/assets/og-card.png, twitter:card summary_large_image).
- Ensure build_site.py does not delete site/assets/.

## Rules (from the org image-generation playbook — mandatory)
- The mark MUST come from the built-in image generation tool. Code-drawn (PIL/SVG) marks are
  REJECTED. Record in `ops/GENERATION_LOG.md`: the original path under
  `C:\Users\USER\.codex\generated_images\<uuid>\`, generation prompt, and timestamp.
- Run only ONE image-generation call at a time (no parallel image calls).
- Transparency QA on the favicon source (script, then report numbers in GENERATION_LOG.md):
  outer 5px band fully alpha==0; no interior transparent holes <500px inside the mark strokes;
  the mark must not contain green/mint hues (avoid chroma-key artifacts).
- Copy the correct file: visually confirm the mark motif matches the prompt (pulse/wire, not
  something from another session's uuid folder).

## Definition of done
1. favicon files + og-card.png exist at the exact paths above; og-card is 1200x630.
2. All three HTML pages reference favicon + OG meta; pages still render (open index.html).
3. ops/GENERATION_LOG.md contains source path + QA numbers.
4. Committed (do not push).
