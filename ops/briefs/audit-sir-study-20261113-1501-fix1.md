Fix every item that failed verification of audit-sir-study-20261113-1501.

Verification file: D:\Projects\_SIR\ops\verifications\audit-sir-study-20261113-1501.md
Project: D:/Projects/SIR Study

Failed items:
- Item 7: Run `python D:/Projects/_SIR/scripts/agy-done.py audit-sir-study-20261113-1501 ok "<one line>"` -> Checkpoint states "Task COMPLETE" but no `agy-done` command output found in logs; the done signal was not verified as executed
- Item L18: Native-App Feel (Disable Browser Defaults) -> No evidence found that default text selection/right-click context menu is disabled site-wide; `verify.ps1` does not check this; manual inspection needed

Rules: fix the cause, not the report. Add or update a test for each fixed item where the project has tests. Check the shared lessons in D:/Projects/_SIR/ops/LESSONS.md for the touched screens. Run the project's checks and CI until green, commit and push to main, update the project checkpoint, and write a short report with the real command output.
