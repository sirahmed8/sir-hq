SIR Jobs, round 19 (2026-11-10). Read AGENTS.md and .sir/CHECKPOINT.md first. HQ checked round 16 today: `npm test` passes locally and most review fixes are present in code, but the claim "all gates green" was false. Fix what is below, in order.

Rules: no pull requests, commit and push to main after every item. Version stays 1.0.0. No emoji, no invented numbers. Auto-submit of job applications stays OFF. Never revert the edits of another tool.

1. GitHub Actions is red on main (last 4 runs of workflow `verify`, for example run 42814192102). The `windows` job fails in test/test-theme-interaction.mjs: "not ok 1 - Theme Dropdown: End-to-end headless browser interaction (Open, Close Button, Backdrop, Escape)" with an AssertionError. Read the log with `gh run view <id> --log-failed`, find the real cause (browser missing on the runner, a timing wait, or a real bug), and fix it properly. Do not skip or delete the test. After the push, wait for the run and confirm with `gh run list --limit 3` that it is green. A round is not done while CI is red.
2. Lint prints 66 warnings (unused caught errors and similar). Bring it to 0 warnings and make CI fail on warnings (`--max-warnings 0`).
3. Files still over the 300 line rule: src/inbox.mjs (709), src/telegram-ledger.mjs (495), src/money-engine.mjs (418), src/pipeline.mjs (386), src/fit-evaluator.mjs (334), src/drafter.mjs (323). Split each into focused modules, behavior unchanged, tests still pass.
4. Review finding M6 is still open: the cookie `sir_jobs_session` (src/auth.mjs, src/routes/auth.mjs). If it is a real session, it must be HttpOnly, SameSite=Strict, random per login and checked on the server; if it is only a constant marker, remove it.
5. Review finding H2: prove no horizontal scroll. Add a headless test that loads every view at 320, 390, 768, 1280 and 1920 px and asserts `document.documentElement.scrollWidth === innerWidth`.
6. Review finding H5: prove the server comes back after a crash. Kill the node process on port 3456, wait for the supervisor task, show the port answers again. Paste the commands and output into the report.
7. Read D:/Projects/_SIR/ops/reviews/2026-11-10/review-jobs.md fully. For every finding (H1 to H5, M1 to M6, L1 to L5) write one line in .sir/R19_CHECKLIST.md: fixed (with file and line as proof) or still open. Fix every one still open.
8. Then one improvement cycle: open the running dashboard at 390 px and 1280 px, Arabic and English, light and dark, and ship at least 10 visible improvements with before and after screenshots under .sir/evidence/r19/. List them under "Found without being told" in the checkpoint.

Finish: update .sir/CHECKPOINT.md (Now, exact Next step, Open promises), append one line to D:/Projects/_SIR/ops/bus/sir-hq.md, commit and push.
