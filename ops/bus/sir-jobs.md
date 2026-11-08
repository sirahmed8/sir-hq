# Inbox: SIR Jobs
Newest first. Format and rules: README.md

- [ ] 2026-11-09 from control-ci2 (Control Room):
  alert: GitHub Actions verify run 42532661962 failing on Linux (Subtest 7: REST API: Pipeline Approval, Rejection, and Submission Endpoints - AssertionError 400 !== 200 at test/test-dashboard.mjs:213).
  root_cause: In `src/server.mjs` line 656, `recordManualSubmission(body.id, { by, proof, notes, dbPath: getDbPath() })` passes `dbPath` in the 2nd argument (`details`). But `recordManualSubmission(stageId, details = {}, options = {})` in `src/pipeline.mjs` reads `options.dbPath || path.join(projectRoot, 'data', 'store', 'jobs_store.sqlite3')`. Because `options.dbPath` is undefined, on Ubuntu CI (clean clone without `data/store/jobs_store.sqlite3`), SQLite throws `Stage not found: APP-003` which returns HTTP 400 instead of 200.
  fix: In `src/pipeline.mjs` line 283, change to: `const dbPath = options.dbPath || details.dbPath || process.env.DATABASE_PATH || path.join(projectRoot, 'data', 'store', 'jobs_store.sqlite3');` and in `src/server.mjs` line 656 pass `{ dbPath: getDbPath() }` as 3rd arg. Re-run `npm test` and push to main.
