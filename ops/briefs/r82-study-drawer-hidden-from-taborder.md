Scout finding approved by HQ.

Project: SIR Study
Severity: high
Category: bug

Finding: The closed side drawer is hidden only by CSS transform (translateX off-screen) with no visibility:hidden, aria-hidden or inert, so all ~12 drawer links/buttons remain in the keyboard Tab order and accessibility tree on every page; Tab trace shows drawer-brand, drawer-close-btn and drawer-nav-items as stops 9-15+ before main content is reached.

Evidence: D:/Projects/_SIR/ops/scout-evidence/scout-a11y-20261114.json tab_first15 for hub/data-structures/sad/or/electronics; guides/study-r11.css:369-394 (.side-drawer has no closed-state visibility rule, unlike .settings-modal at study-r11.css:206-233 which correctly uses visibility:hidden); guides/study-shell.js:79-93 toggleSideDrawer toggles only .open class

Do this: reproduce the finding with the evidence above, fix the cause (not the report), add or update a test where the project has tests, and check the shared lessons in D:/Projects/_SIR/ops/LESSONS.md for the touched screens. Run the project's checks and CI until green, commit and push to main, update the project checkpoint, write a short report with the real command output, then tick this item in ops/SUGGESTIONS.md (Status: done) so the next scout does not propose it again.
