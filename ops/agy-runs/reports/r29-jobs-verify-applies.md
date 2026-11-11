# r29-jobs-verify-applies Report

## Summary

SIR Jobs round 29: truth audit of apply metrics, live auto-apply run, and honest
submission count. Result: 0 applications REALLY submitted to date. The previously
reported count of 20 (by_source unknown: 14, telegram_approval: 6) was inflated
by test/fixture entries with no proof. The only remaining history entry
(test-job-1) was a test fixture and was removed.

## What changed

### 1. Truth audit of data/apply-metrics.json

Before: applications_sent: 1, history: [{ jobId: "test-job-1", method:
"telegram_approval", source: "unknown" }]. The brief described an earlier state
of applications_sent: 20 (by_source unknown: 14, telegram_approval: 6); prior
work had already reduced it to the single test-fixture entry.

Ran `node scripts/audit-apply-truth.mjs --write`. Output:
```
[audit] history entries: 1
[audit] surviving: 0
[audit] removed: 1
  - test_fixture_jobId: test-job-1 (2026-11-11T14:07:36.273Z)
[audit] corrected totals: {"applications_sent":0,"by_source":{},"by_role_family":{},"by_week":{}}
[audit] WROTE corrected metrics to D:\Projects\SIR Jobs\data\apply-metrics.json
```

After: applications_sent: 0, empty history. /data/ is gitignored so the file
is not tracked, but it is the source of truth on disk.

Audit criteria applied to every history entry:
- jobId must not match test-fixture pattern (^test-job-|fixture|mock|dummy)
- jobId must exist in a live job source
- real proof artifact must exist in .sir/evidence/r28/ or data/proofs/

test-job-1 failed all three (fixture id, not in live sources, no proof).

### 2. Live auto-apply run

Command: `node src/apply-pipeline/runner.mjs auto --limit=10` (no --dry-run).
Output:
```
[AutoApply] Starting auto-apply run...
[AutoApply] Fetched 61 total jobs
[AutoApply] Found 40 good matches after fit gate
[AutoApply] 10 candidates to evaluate for auto-apply
[AutoApply] QUEUED remoteok-1137680 for owner browser - ...
[AutoApply] SKIP remotive-2091166: graded_test - Graded test or assessment required
[AutoApply] QUEUED whatsapp-q3dd92o1 for owner browser - ...
[AutoApply] SKIP whatsapp-7giwanyn: graded_test - Graded test or assessment required
[AutoApply] QUEUED whatsapp-gne0ft2l for owner browser - ...
[AutoApply] QUEUED whatsapp-rz2f5wkm for owner browser - ...
[AutoApply] QUEUED whatsapp-j5bprwfk for owner browser - ...
[AutoApply] QUEUED whatsapp-nzbxx93a for owner browser - ...
[AutoApply] QUEUED whatsapp-fznk84dy for owner browser - ...
[AutoApply] SKIP whatsapp-kt82cp9w: graded_test - Graded test or assessment required
[AutoApply] Done: applied=0, skipped=3, dailyCount=0/10
```

Result: 0 real submissions. 7 candidates queued for owner browser
(method owner_browser, NOT counted as submissions), 3 skipped as graded tests.
Daily cap respected: appliedCount 0/10. No Gmail OAuth credentials configured,
CDP browser apply reached landing pages but no submission confirmation pages on
external sites.

### 3. Batch Telegram

Not sent — no proven real submissions to report. Per brief item (4), the batch
Telegram ("قدّمت على N وظايف") is sent only for what is proven real.

### 4. INCOME_MODEL.md line 5

Changed from:
`**Status:** No fixed income target. Real, researched, measured. Agent finds work → applies with one-tap approval → reports first positive answer.`
to:
`**Status:** No fixed income target. Real, researched, measured. Agent finds work, drafts truthful applications, and delivers each one to the owner's own signed-in browser for the final submit. No application is sent automatically or counted as submitted without real proof. Reports first positive answer.`

### 5. Code changes

- `src/apply-pipeline/metrics.mjs`: added `auditAndCleanMetrics(options)` —
  removes test-fixture and unproven entries, recomputes all counters from
  surviving entries.
- `src/apply-pipeline/auto-apply.mjs`: only real submissions (gmail/browser)
  count toward appliedCount, appliedJobIds, appliedJobUrls and metrics.
  Owner-browser queue is a pending delivery, not a submission.
- `src/apply-pipeline/runner.mjs`: added `deliveredJobIds` to state,
  `markDelivered()` writes to deliveredJobIds (not appliedJobIds),
  `markOwnerBrowserSubmitted(jobId, proof, meta)` records a genuine owner
  submission via `markApplied`.
- `scripts/audit-apply-truth.mjs`: standalone audit script (dry-run by default,
  --write applies).
- `test/test-r29-truth-audit.mjs`: 3 tests (removes fixtures, keeps real,
  preserves non-application entries).
- `package.json`: added `test-r29-truth-audit.mjs` to `npm test`.
- `.sir/INCOME_MODEL.md`: line 5 wording fix.
- `.sir/r29-jobs-verify-applies_CHECKLIST.md`: new checklist, all items ticked.
- `.sir/CHECKPOINT.md`: honest one-paragraph summary of real submissions.

## Evidence

- Corrected metrics: `data/apply-metrics.json` → applications_sent: 0, empty
  history (not tracked, /data/ gitignored).
- Auto-apply state: `data/auto-apply-state.json` → appliedCount: 0,
  7 owner_browser_pending + 3 graded_test skips (not tracked).
- Queue records: `D:/Projects/_SIR/.sir/evidence/r28/` — 14 auto-apply
  evidence JSON files (method owner_browser, not submissions).
- Browser proof screenshots: `data/proofs/<jobId>/` — landing + after-click
  PNGs for each attempted job (not tracked).
- Test results: `test/test-r29-truth-audit.mjs` — 3 passed, 0 failed.
- CI: GitHub Actions run 43038357575 on commit e625ca0 — all steps green
  (lint, typecheck, npm test, gitleaks, secrets).
- Local verify: `npm run verify` — all 5 gates green (tests, snapshot drill,
  gitleaks no leaks, privacy 0 leaks across 727 files, smoke test 200 OK).
- Local doctor: `npm run doctor` — 7/7 gates green.
- Lint: 0 errors, 0 warnings. Typecheck: 0 errors.

## What is still open

- 7 jobs are queued in `data/auto-apply-state.json` for the owner's signed-in
  browser (remoteok-1137680 + 6 WhatsApp jobs). These become real submissions
  only when the owner completes them in his browser and confirms via
  `markOwnerBrowserSubmitted` with real proof. Nothing is counted until then.
- Gmail auto-send is not configured (no data/gmail-token.json or
  data/gmail-credentials.json). CDP browser apply reaches landing pages but
  external company sites do not return submission-confirmation pages, so no
  automated submission succeeded this run.

## Commands run (real output)

- `npm run lint` → 0 errors, 0 warnings
- `npm run typecheck` → 0 errors
- `npm test` → all suites pass (r24 pipeline 31, r24 browser 2, r29 truth audit 3, plus all prior suites)
- `npm run doctor` → 7/7 gates green
- `npm run verify` → all 5 gates green
- `node scripts/audit-apply-truth.mjs --write` → removed test-job-1, applications_sent: 0
- `node src/apply-pipeline/runner.mjs auto --limit=10` → applied=0, skipped=3, dailyCount=0/10
- `git commit -m "chore(r29): verify applies, correct metrics to truth"` → e625ca0
- `git push origin main` → pushed 4f2ca77..e625ca0
- `gh run watch 43038357575` → all CI steps green

## Next step

Run `python D:/Projects/_SIR/scripts/agy-done.py r29-jobs-verify-applies ok "<one line>"`.
