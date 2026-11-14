Scout finding approved by HQ.

Project: _SIR
Severity: high
Category: bug

Finding: AI chat toggle unmounts on open so keyboard focus is dropped to <body> and never moved into the dialog; on close, focus is not restored to the toggle, forcing keyboard users to re-tab through the whole page to reach the chat input.

Evidence: src/components/AIChat.tsx:342-358 ({!isOpen && <button>} unmounts, no focus effect); tab probe D:/Projects/_SIR/ops/scout-evidence/tabprobe.py output

Do this: reproduce the finding with the evidence above, fix the cause (not the report), add or update a test where the project has tests, and check the shared lessons in D:/Projects/_SIR/ops/LESSONS.md for the touched screens. Run the project's checks and CI until green, commit and push to main, update the project checkpoint, write a short report with the real command output, then tick this item in ops/SUGGESTIONS.md (Status: done) so the next scout does not propose it again.
