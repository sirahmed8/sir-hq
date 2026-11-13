# review-old-tasks — verification of three unverified "done" claims (2026-11-13, OpenCode)

## Task
Verify three old "done" claims that have no PASS report: `r60-build-sir-jobs`, `r60-build-sir-study`, `r60-build-sir-portfolio`. For each: read its report, run the test command it names, record exact counts, write `ops/agy-runs/reports/verify-<name>.md` with PASS or FAIL and evidence. Do not change product code. Commit reports only, push to main.

## What was done
- Read `ops/AUTOPILOT_QUEUE.json`: all three are `done: true`, folders confirmed (SIR Jobs, SIR Study, SIR Portfolio).
- Read each original report to extract the named test commands.
- Ran the commands locally (CI quota flag `ops/ci-quota-exhausted.flag` present → local gates substitute per preamble rule 18).
- Wrote three verify reports and committed/pushed them (commit `a637bd6`).

## Results
| Claim | Named command | Result | Counts |
|---|---|---|---|
| r60-build-sir-jobs | npm test (+ lint, typecheck, doctor, proof-report) | PASS | All suites `fail 0`; lint 0 problems; typecheck 0 errors; doctor HEALTHY; proof-report 0 missing |
| r60-build-sir-study | scripts/verify.ps1 | FAIL | 17 checks: 1 failure (`test_no_machine_specific_paths_in_scripts` in `scripts/dev-start.vbs:1` and `scripts/dev-stop.vbs:1`); 51 tests ran, 1 failed, 2 skipped (Playwright unavailable) |
| r60-build-sir-portfolio | npm test (+ typecheck, build) | PASS | 843/843 pass, 22 suites, 0 fail; typecheck 0 errors/warnings; build success |

## Files created
- `ops/agy-runs/reports/verify-r60-build-sir-jobs.md` (PASS)
- `ops/agy-runs/reports/verify-r60-build-sir-study.md` (FAIL)
- `ops/agy-runs/reports/verify-r60-build-sir-portfolio.md` (PASS)

## Commands run (with real output)
- SIR Jobs: `npm test` → exit 0, all `fail 0`; `npm run lint` → exit 0; `npm run typecheck` → exit 0; `npm run doctor` → HEALTHY; `npm run proof-report` → OK 0 missing.
- SIR Study: `powershell -ExecutionPolicy Bypass -File scripts/verify.ps1` → exit 1 (FAIL). Failure: `scripts/dev-start.vbs:1` and `scripts/dev-stop.vbs:1` contain hard-coded `D:\Projects\SIR Study`.
- SIR Portfolio: `npm test` → 843/843 pass; `npm run typecheck` → 0 errors; `npm run build` → success.

## What is still open
- SIR Study has one real, reproducible test failure. Fix the two `.vbs` launchers to use relative/portable paths, then re-run `verify.ps1`. (Not fixed here: brief forbids product-code changes.)
- Axe/keyboard/Lighthouse claims in the portfolio report were not re-run this session (no browser automation available); code-level gates are green.
- GitHub Actions remain unavailable (quota flag); local gates are the substitute.

## Commit
- `a637bd6` "review-old-tasks: add verify reports for r60 jobs/study/portfolio" pushed to `main` (origin/main updated).
