Fix every item that failed verification of r45-jobs-scout-fixes.

Verification file: D:/Projects/_SIR/ops/verifications/r45-jobs-scout-fixes.md
Project: D:/Projects/SIR Jobs

Failed items:
- Item 2: No text input did per-character bidi detection: every input/textarea inherited direction:rtl in Arabic mode with dir attribute null (L8 violation). -> The four scout-identified inputs are fixed: live probe shows `dir="auto"` on #pipeline-search, #jobs-search, #palette-input and #prop-personal-note (proposals.js:137). BUT the same defect persists on the contacts form added later in r46 (commit 80844ec): live probe at 390px AR shows #contact-name, #contact-role, #contact-company, #contact-notes all `{dirAttr: null, dirCss: "rtl"}` — typing a Latin company name or mixed notes still keeps RTL caret/alignment, the exact L8 symptom the finding describes. `src/public/index.html:555,559,563,575` have no dir attribute (only email/date inputs are intentionally dir="ltr"). Fix needed: add `dir="auto"` to those four fields.

Rules: fix the cause, not the report. Add or update a test for each fixed item where the project has tests. Check the shared lessons in D:/Projects/_SIR/ops/LESSONS.md for the touched screens. Run the project's checks and CI until green, commit and push to main, update the project checkpoint, and write a short report with the real command output.
