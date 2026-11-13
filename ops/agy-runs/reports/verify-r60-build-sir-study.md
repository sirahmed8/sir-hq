# verify-r60-build-sir-study — verification report (2026-11-13, OpenCode)

## Verdict: FAIL

## Scope
Re-verified the "done" claim in `ops/agy-runs/reports/r60-build-sir-study.md`, which states "FINAL: ALL CHECKS PASSED: SIR Study is Green & Verified!" and "Unit Tests 51 tests (2 skipped)". Ran `scripts/verify.ps1` against `D:/Projects/SIR Study`.

## Command run
`powershell -ExecutionPolicy Bypass -File scripts/verify.ps1` (17 checks).

## Result
`EXIT=False` — "VERIFICATION FAILED: Address the issues above!"

## Exact failure
- Check [15/17] Running Unit Tests: 1 failure, 2 skipped.
  - `FAIL: test_no_machine_specific_paths_in_scripts (test_hygiene_guards.TestPortablePaths.test_no_machine_specific_paths_in_scripts)`
  - AssertionError: hard-coded paths found:
    - `scripts/dev-start.vbs:1` → `D:\Projects\SIR Study`
    - `scripts/dev-stop.vbs:1` → `D:\Projects\SIR Study`
  - Both files are single-line launchers that embed the absolute project path.
- 2 skips are environment-only (Playwright/Chromium unavailable on this machine: "This installation of Playwright does not include Node.js"), not code failures.

## Checks that passed
- [1/17] Core Files & Assets: OK
- [2/17] Python Syntax Check: OK (all 31 scripts compile)
- [3/17] HTML Linting (htmlhint): WARN (6 files, non-blocking, pre-existing)
- [4/17] JavaScript Linting (ESLint): OK
- [5/17] Code Formatting (Prettier): WARN (non-blocking)
- [6/17] Ruff: INFO (not installed)
- [7/17] MyPy: INFO (not installed)
- [8/17] HTML Structure & Mobile Viewports: WARN (8 files missing manifest link)
- [9/17] Inter-Guide Hyperlinks: OK
- [10/17] Button & Interaction Wiring: OK
- [11/17] Math/Theoretical Accuracy: OK
- [12/17] Academic Integrity Guard: OK (105/105)
- [13/17] Dev Server Scripts: OK
- [14/17] Gitleaks: WARN (2 known false positives in gitignored .env)
- [16/17] Shared Asset Drift Guard: OK
- [17/17] Search Index & Data Integrity: OK

## Evidence (file:line)
- `D:/Projects/SIR Study/scripts/dev-start.vbs:1`
- `D:/Projects/SIR Study/scripts/dev-stop.vbs:1`

## Honest notes
- The original report's "51 tests (2 skipped)" count is accurate (51 ran, 1 failed, 2 skipped in this run). But its "ALL CHECKS PASSED" claim is not supported: one test fails.
- The failing files are in the working tree as modified (uncommitted) per `git status`; they were not changed by this verification.
- No product code was changed by this verification.
- Playwright-based browser tests could not run on this machine (Node.js not found by the Python Playwright install); those are environment skips, not regressions.

## Conclusion
Verdict: FAIL. Fix `scripts/dev-start.vbs:1` and `scripts/dev-stop.vbs:1` to remove the hard-coded `D:\Projects\SIR Study` paths (make them relative/portable), then re-run `verify.ps1`.
