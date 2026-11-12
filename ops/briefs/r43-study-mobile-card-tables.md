Scout finding approved by HQ.

Project: SIR Study
Severity: high
Category: bug

Finding: 14 study tables across 7 guide pages (data-structures, sad, or, human-rights, business-admin, hci, electronics) are 1.6x-4.3x wider than their .table-responsive wrapper at 320/390px (e.g. electronics 'نوع المادة' table 1052px in a 254px wrap), forcing horizontal scrolling to read cell labels with no scroll affordance - violates shared lesson L4 which requires card layout for narrow tables on phones.

Evidence: D:/Projects/_SIR/ops/scout-evidence/scout-mobile-refined.json (tableW vs wrapW per page); guides/electronics.html:411-417,760-781 (.table-responsive is overflow-x:auto with no mobile card fallback); screenshots refined-elec-320-rtl.png, refined-ds-320-rtl.png

Do this: reproduce the finding with the evidence above, fix the cause (not the report), add or update a test where the project has tests, and check the shared lessons in D:/Projects/_SIR/ops/LESSONS.md for the touched screens. Run the project's checks and CI until green, commit and push to main, update the project checkpoint, write a short report with the real command output, then tick this item in ops/SUGGESTIONS.md (Status: done) so the next scout does not propose it again.
