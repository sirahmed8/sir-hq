Fix every item that failed verification of audit-sir-jobs-20261113-1821.

Verification file: D:\Projects\_SIR\ops\verifications\audit-sir-jobs-20261113-1821.md
Project: D:/Projects/SIR Jobs

Failed items:
- Item 4: Ship at least 10 visible improvements with before and after screenshots under .sir/evidence/ -> Zero visible improvements shipped. Two audit cycles found zero on-screen defects; the only fix was test wiring (D1), which is not a visible UI improvement. The worker's report argues manufacturing cosmetic changes would violate the no-slop bar, but the brief's literal requirement of >=10 improvements with before/after evidence is unmet; `.sir/evidence/audit-20261113-1821/` contains only `after/` screenshots, no before/after pairs

Rules: fix the cause, not the report. Add or update a test for each fixed item where the project has tests. Check the shared lessons in D:/Projects/_SIR/ops/LESSONS.md for the touched screens. Run the project's checks and CI until green, commit and push to main, update the project checkpoint, and write a short report with the real command output.
