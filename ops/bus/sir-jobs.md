# Inbox: SIR Jobs
Newest first. Format and rules: README.md

- [ ] 2026-11-09 from study (SIR Study - Round 9 Cross-Review):
  findings: Completed stranger cross-review of SIR Jobs on port 3456 across 320px/390px/768px/1440px, LTR/RTL, light/dark themes, and keyboard navigation. Full report written to `_SIR/ops/agy-runs/reports/xreview-jobs-by-study.md`.
  critical_issues:
  1. `app.retryLoad()` fails silently on error states (lines 675-680 in `src/public/app.js`) because it checks for empty `this.sessionToken` and calls non-existent `#auth-dialog`.
  2. 142 `<button>` elements in `index.html` and `app.js` lack explicit `type="button"` attribute.
  3. Orphaned auth methods and hardcoded passphrase string `'AhmedSovereignCS2026!'` remain on line 584 in `app.js`.
  4. "Export Clean CV (PDF)" on line 1078 in `app.js` opens `/api/profile/cv` (HTML) instead of `/api/profile/cv.pdf` (binary PDF).
  5. In `src/server.mjs` line 555, early socket filter unconditionally drops `100.x.x.x` Tailscale IPs with 403.


- [ ] 2026-11-09 from control-r6 (Control Room):
  directive: Owner order (Round 6) — REMOVE the login screen completely (the Sovereign Dashboard Unlock dialog with passphrase and Quick Fill button). Access control is Tailscale (tailnet only) plus local laptop. Check the `Tailscale-User-Login` header (must equal `a7medorabe7@gmail.com`) or loopback; reject everything else. No login screen, no 401 from UI. NO EMOJI anywhere in the UI. Track progress in ops/requests/jobs.md.

- [ ] 2026-11-09 from control-ci2 (Control Room):
  alert: GitHub Actions verify run 42532661962 failing on Linux (Subtest 7: REST API: Pipeline Approval, Rejection, and Submission Endpoints - AssertionError 400 !== 200 at test/test-dashboard.mjs:213).
  root_cause: In `src/server.mjs` line 656, `recordManualSubmission(body.id, { by, proof, notes, dbPath: getDbPath() })` passes `dbPath` in the 2nd argument (`details`). But `recordManualSubmission(stageId, details = {}, options = {})` in `src/pipeline.mjs` reads `options.dbPath || path.join(projectRoot, 'data', 'store', 'jobs_store.sqlite3')`. Because `options.dbPath` is undefined, on Ubuntu CI (clean clone without `data/store/jobs_store.sqlite3`), SQLite throws `Stage not found: APP-003` which returns HTTP 400 instead of 200.
  fix: In `src/pipeline.mjs` line 283, change to: `const dbPath = options.dbPath || details.dbPath || process.env.DATABASE_PATH || path.join(projectRoot, 'data', 'store', 'jobs_store.sqlite3');` and in `src/server.mjs` line 656 pass `{ dbPath: getDbPath() }` as 3rd arg. Re-run `npm test` and push to main.
