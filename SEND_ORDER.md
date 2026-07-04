# SEND_ORDER — scheduled outreach dispatch (executed by Claude, Tue 23:00 KST = Tue morning ET)

You are the dispatcher. This runs in the US-morning attention window. Your job: send
what is queued, safely, and nothing else.

## Protocol
1. List ops/outreach/queue/*.md. Empty → write ops/outreach/log.md line
   "<date> | dispatch | none | queue empty" and STOP (positive confirmation required).
2. For each queued item (front-matter: repo, type[issue|pr-comment|pr|discussion],
   title, body-or-branch, verified_at, evidence):
   a. **Freshness re-verification**: re-check the claim against the primary source AND
      the target repo's current state (their file may have been fixed since queueing;
      our previous issue/PR may have been answered). Stale/already-fixed → do NOT send;
      move to ops/outreach/queue/dropped/ with a one-line reason.
   b. Respect caps: max 3 sends per run, max 1 per repo, skip repos where our previous
      item is still open and unanswered (but DO reply if a maintainer asked us something —
      replies don't count against the cap and take priority).
   c. Send via gh (issue create / pr create / discussion GraphQL — patterns in
      AUDIT_OUTREACH_ORDER.md). PR fixes and send bodies must have passed the calibrated
      second-opinion audit at queue time (REVIEW_REPORT verdict file referenced in
      front-matter); if missing, skip and flag.
3. Record every action in ops/outreach/log.md and update USER_ACTIONS.md 완료 섹션.
4. Check for replies on ALL previously sent items (log.md history). Maintainer questions
   → draft answers, send them (replies are always allowed), log.
5. Commit ops/ changes ("Outreach dispatch <date>"), push NOT required (ops only).
   Mandatory report: ops/reports/dispatch-<date>.md (sent / dropped / replied / skipped).
