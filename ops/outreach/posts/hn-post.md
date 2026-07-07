# HN Show HN 포스트 (최종 검증본 2026-07-05)

발송 창: 화·수·목 21:00–24:00 KST (US 오전). 올리기 직전 클로드에게 "HN 올릴게" → 숫자 재검증.

---

## Title (submit 화면 title 칸)
```
Show HN: FactQuire – LLM API prices and limits, each with a primary-source quote
```
(78자, HN 80자 이내)

## URL (submit 화면 url 칸)
```
https://factquire.com
```
※ text 칸은 비운다. submit 직후 아래 본문을 **자기 글 첫 댓글**로 붙여넣는다.

---

## First comment (제출 직후 첫 댓글로)

I built FactQuire because model pricing and limits get treated as static reference data, but they're really news — they change on an effective date, quietly, on a page nobody re-reads.

The one rule the whole site is built on: every number (price, context window, max output) carries a verbatim quote from the primary source plus the timestamp I read it. So you can re-verify any claim without trusting me — including when I'm the one who turns out to be wrong. The corrections log is public: https://factquire.com/corrections.html

A concrete example of why per-field provenance matters: AWS moved Claude 3.5 Sonnet v2 on Bedrock to "Public Extended Access" pricing effective Dec 1 2025 — $6.00/$30.00 per 1M tokens, exactly 2x the familiar $3.00/$15.00. Seven months later I found a widely-used open-source cost tracker still carrying the old $3/$15. The code wasn't buggy; it just didn't know the world had changed underneath it. I verified against the AWS pricing page and sent the fix upstream. (A separate correction I filed — Mistral pricing — was already accepted into models.dev.)

Coverage today: 135 models across 16 providers. Everything is machine-readable — /feed.json, per-model JSON, llms.txt, RSS. Data is CC BY 4.0, code MIT.

Honest limitations: coverage is still narrow, verification is scripted + manual rather than fully automated, and "verified_at" means "true when I read it," not "still true this second." That last gap is the whole problem I'm chasing, which is why there's a weekly refresh and a public corrections log rather than a claim of permanent accuracy.

I'd love feedback on two things: (1) which providers/fields you'd want next, and (2) whether the per-field source quote is genuinely useful to you or just noise.

---

## 검증 상태 (2026-07-05 재확인)
- factquire.com / www / feed.json / bedrock JSON / corrections: 전부 200
- http→https 301 리다이렉트 작동
- Bedrock JSON 실측: input_per_mtok 6.0, output_per_mtok 30.0 ✅
- models.dev 이슈 #3025 (Mistral 가격): CLOSED COMPLETED = 수용됨 ✅
- Helicone PR #5709 (Bedrock $3→$6): OPEN = "sent the fix upstream" 정확
- 135 모델 · 16 프로바이더 ✅
