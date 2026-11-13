# Verify r71 AHome profile fixes (verifier, not builder)
Project: D:/Projects/AHome. Commit 7163267 claims: crop sheet modal, pinch zoom, rotate pan, keyboard-safe screens, toggle drag cleanup.
Steps:
1. Run the AHome web tests and typecheck the way the repo documents. Paste exact commands and pass/fail counts.
2. Open the profile editor at 390 px and 768 px. Take screenshots with synthetic test data only (never real Habiba or AHome private content).
3. Check: slider under the profile photo sits right; crop sheet works; text inputs stay visible above the phone keyboard; buttons and the round frame are not clipped.
4. Write ops/agy-runs/reports/verify-r71-ahome.md with PASS or FAIL per item and evidence paths.
5. Do not change product code. If a check fails, list the exact file and line in the report.
Done = report written, checkpoint in AHome .sir/CHECKPOINT.md updated, commit and push to main.
