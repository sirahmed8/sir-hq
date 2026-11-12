Fix every item that failed verification of audit-sir-study-20261112-1401.

Verification file: D:/Projects/_SIR/ops/verifications/audit-sir-study-20261112-1401.md
Project: D:/Projects/SIR Study

Failed items:
- Item 6: Ship at least 10 visible improvements with before and after screenshots under `.sir/evidence/`. -> Only 7 before/after screenshot pairs exist: `.sir/evidence/20261112-1401/improvements/{before,after}/01-07-*.png` (verified by directory listing). `COVERAGE.md` itself lists 13 improvements but admits items 8-13 (slim scrollbars, `color-scheme`, `content-visibility`, `prefers-contrast`, reduced-motion carve-out, stagger/urgent-glow motion) have no distinct before/after screenshots. 7 < 10 required pairs.

Rules: fix the cause, not the report. Add or update a test for each fixed item where the project has tests. Check the shared lessons in D:/Projects/_SIR/ops/LESSONS.md for the touched screens. Run the project's checks and CI until green, commit and push to main, update the project checkpoint, and write a short report with the real command output.
