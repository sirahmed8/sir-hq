Fix every item that failed verification of audit-sir-laptop-manager-20261112-1401.

Verification file: D:/Projects/_SIR/ops/verifications/audit-sir-laptop-manager-20261112-1401.md
Project: D:/Projects/SIR Laptop Manager

Failed items:
- Item 2: Open every page, tab, sheet and flow at 320/390/768/1280 px, light and dark, in every language; log defects in .sir/DEFECTS_20261112-1401.md; fix each at root; add browser test; commit+push; keep CI green; ship at least 10 visible improvements with before/after screenshots under .sir/evidence/; repeat until two cycles find nothing. -> Local suite not green: `pytest tests` = 2 failed, 292 passed in 366.76s (`tests/test_powershell_scripts.py::test_dev_stop_kills_only_our_server`, `tests/test_round11_improvements.py::test_dev_start_vbs_launches_pythonw_directly`), contradicting the checkpoint claim of "294/294 green". CI blocked by Actions quota (`ops/ci-quota-exhausted.flag` exists): all 3 recent runs finished in ~4s with zero steps — run ids 43235965452, 43224133162, 43224087352 (all `failure`). Two clean cycles and the >=10 visible improvements were not independently re-verified this session. 390px headless screenshot captured: D:/Projects/_SIR/ops/verifications/evidence/sir-laptop-manager-390.png
- Item 3: Report in D:/Projects/_SIR/ops/agy-runs/reports/audit-sir-laptop-manager-20261112-1401.md -> Not written yet; this verification file (ops/verifications/audit-sir-laptop-manager-20261112-1401.md) is the deliverable produced instead
- Item 4: Run `python D:/Projects/_SIR/scripts/agy-done.py audit-sir-laptop-manager-20261112-1401 ok "<one line>"` -> Not run; depends on the agy-runs report being written first

Rules: fix the cause, not the report. Add or update a test for each fixed item where the project has tests. Check the shared lessons in D:/Projects/_SIR/ops/LESSONS.md for the touched screens. Run the project's checks and CI until green, commit and push to main, update the project checkpoint, and write a short report with the real command output.
