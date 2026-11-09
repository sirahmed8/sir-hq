# Inbox: SIR Jobs
Newest first. Format and rules: README.md

- [ ] 2026-11-09 from control-r6 (Control Room):
  directive: Owner order (Round 6) — REMOVE the login screen completely (the Sovereign Dashboard Unlock dialog with passphrase and Quick Fill button). Access control is Tailscale (tailnet only) plus local laptop. Check the `Tailscale-User-Login` header (must equal `a7medorabe7@gmail.com`) or loopback; reject everything else. No login screen, no 401 from UI. NO EMOJI anywhere in the UI. Track progress in ops/requests/jobs.md.

- [ ] 2026-11-09 from control-ci2 (Control Room):
  alert: GitHub Actions verify run 42532661962 failing on Linux (Subtest 7: REST API: Pipeline Approval, Rejection, and Submission Endpoints - AssertionError 400 !== 200 at test/test-dashboard.mjs:213).
  root_cause: In `src/server.mjs` line 656, `recordManualSubmission(body.id, { by, proof, notes, dbPath: getDbPath() })` passes `dbPath` in the 2nd argument (`details`). But `recordManualSubmission(stageId, details = {}, options = {})` in `src/pipeline.mjs` reads `options.dbPath || path.join(projectRoot, 'data', 'store', 'jobs_store.sqlite3')`. Because `options.dbPath` is undefined, on Ubuntu CI (clean clone without `data/store/jobs_store.sqlite3`), SQLite throws `Stage not found: APP-003` which returns HTTP 400 instead of 200.
  fix: In `src/pipeline.mjs` line 283, change to: `const dbPath = options.dbPath || details.dbPath || process.env.DATABASE_PATH || path.join(projectRoot, 'data', 'store', 'jobs_store.sqlite3');` and in `src/server.mjs` line 656 pass `{ dbPath: getDbPath() }` as 3rd arg. Re-run `npm test` and push to main.
