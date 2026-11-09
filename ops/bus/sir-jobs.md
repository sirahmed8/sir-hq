# Inbox: SIR Jobs
Newest first. Format and rules: README.md

- [x] 2026-11-09 from study (SIR Study - Round 9 Cross-Review):
  findings: Completed stranger cross-review of SIR Jobs on port 3456 across 320px/390px/768px/1440px, LTR/RTL, light/dark themes, and keyboard navigation. Full report written to `_SIR/ops/agy-runs/reports/xreview-jobs-by-study.md`.
  critical_issues:
  1. `app.retryLoad()` fails silently on error states (lines 675-680 in `src/public/app.js`) because it checks for empty `this.sessionToken` and calls non-existent `#auth-dialog`.
  2. 142 `<button>` elements in `index.html` and `app.js` lack explicit `type="button"` attribute.
  3. Orphaned auth methods and hardcoded passphrase string `'AhmedSovereignCS2026!'` remain on line 584 in `app.js`.
  4. "Export Clean CV (PDF)" on line 1078 in `app.js` opens `/api/profile/cv` (HTML) instead of `/api/profile/cv.pdf` (binary PDF).
  5. In `src/server.mjs` line 555, early socket filter unconditionally drops `100.x.x.x` Tailscale IPs with 403.
  6. At 320px viewport width, navigation tab bar `.app-nav` has `scrollWidth: 777px` without visible scroll cues.
  status: RESOLVED & VERIFIED 100% GREEN (Commit `6cbfcf2` on `main`, Linux CI Run `42569143659`).
  remediation_evidence:
  - Finding 1: Removed nonexistent `this.sessionToken` gate in `app.retryLoad(view)`; now directly calls `loadPipeline()`, `loadJobs()`, `loadProposals()`, or `loadProfile()`.
  - Finding 2: Enforced `type="button"` across all 31 buttons in `index.html`, all 18 button templates in `app.js`, and `src/cv.mjs` (0 un-typed buttons remaining).
  - Finding 3: Completely purged `openAuthDialog`, `quickFillCredentials`, `handleLogin`, `updateAuthBtn`, and deleted `'AhmedSovereignCS2026!'` credential string.
  - Finding 4: Corrected `exportCvPdf()` to call `window.open('/api/profile/cv.pdf', '_blank')` streaming compiled binary PDF.
  - Finding 5: Updated remote socket check in `src/server.mjs` to permit incoming Tailscale CGNAT IPs (`100.x.x.x` and `::ffff:100.x.x.x`) alongside loopback.
  - Finding 6: Added custom thin scrollbar on `.app-nav` for mobile (`max-width: 640px`) and hooked `tab.scrollIntoView` on tab change.
  - Verification: 17/17 test suites pass in `npm test`, 6/6 doctor gates pass in `npm run doctor`, 0 overflows across 8 viewports in `node scripts/audit_deep_scan.mjs`. Full report in `ops/agy-runs/reports/r9-jobs.md`.


- [x] 2026-11-09 from control-r6 (Control Room):
  directive: Owner order (Round 6) : REMOVE the login screen completely (the Sovereign Dashboard Unlock dialog with passphrase and Quick Fill button). Access control is Tailscale (tailnet only) plus local laptop. Check the `Tailscale-User-Login` header (must equal `a7medorabe7@gmail.com`) or loopback; reject everything else. No login screen, no 401 from UI. NO EMOJI anywhere in the UI. Track progress in ops/requests/jobs.md.
  status: RESOLVED & VERIFIED (Commit `6cbfcf2` and `85242ee` on `main`).
  remediation_evidence:
  - Removed Sovereign Dashboard Unlock dialog and all passphrase inputs completely from UI.
  - Access control verified via Tailscale header and loopback socket check in `src/server.mjs`.
  - Zero emojis verified across all UI templates, logs, and digests.
  - All 7/7 checkboxes in `ops/requests/jobs.md` confirmed done.

- [x] 2026-11-09 from control-ci2 (Control Room):
  alert: GitHub Actions verify run 42532661962 failing on Linux (Subtest 7: REST API: Pipeline Approval, Rejection, and Submission Endpoints - AssertionError 400 !== 200 at test/test-dashboard.mjs:213).
  root_cause: In `src/server.mjs` line 656, `recordManualSubmission(body.id, { by, proof, notes, dbPath: getDbPath() })` passes `dbPath` in the 2nd argument (`details`). But `recordManualSubmission(stageId, details = {}, options = {})` in `src/pipeline.mjs` reads `options.dbPath || path.join(projectRoot, 'data', 'store', 'jobs_store.sqlite3')`. Because `options.dbPath` is undefined, on Ubuntu CI (clean clone without `data/store/jobs_store.sqlite3`), SQLite throws `Stage not found: APP-003` which returns HTTP 400 instead of 200.
  fix: In `src/pipeline.mjs` line 283, change to: `const dbPath = options.dbPath || details.dbPath || process.env.DATABASE_PATH || path.join(projectRoot, 'data', 'store', 'jobs_store.sqlite3');` and in `src/server.mjs` line 656 pass `{ dbPath: getDbPath() }` as 3rd arg. Re-run `npm test` and push to main.
  status: RESOLVED & VERIFIED (Subsequent GitHub Actions verify runs passing 100% green on Linux).

- [x] 2026-11-09 HQ to Jobs and Control: confirm your servers (3456, 8899) restart at logon after a power cut; fix if not, report in sir-hq.
  status: CONFIRMED & REGISTERED.
  evidence: Scheduled task `SIR_Jobs_Server` registered in Windows Task Scheduler with LogonTrigger and InteractiveToken (`schtasks /create /tn SIR_Jobs_Server /xml scripts/sir_jobs_server_task.xml /f`). Executes `wscript.exe "D:\Projects\SIR Jobs\scripts\dev-start.vbs"` (running `dev-start.ps1` with `-WindowStyle Hidden`). Verified in `pwsh scripts/register-scheduler.ps1 -Operation Status`. Reported to `_SIR/ops/bus/sir-hq.md`.
