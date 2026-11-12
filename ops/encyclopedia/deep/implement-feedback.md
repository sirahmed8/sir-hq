# implement-feedback (canva plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\canva\skills\implement-feedback\SKILL.md` (7 KB; canva plugin, only revision).

## Summary
Workflow that turns a Canva design's review comments into applied edits. It resolves the design, reads every comment thread (`list-comments` + `list-replies` per thread) and current page content, triages each thread into Actionable / Requires-manual-action / Resolved, shows the user ONE consolidated plan for approval, then executes all API-supported changes in a single `perform-editing-operations` batch inside one editing transaction and commits without asking again. It closes the loop by replying to each thread and ends with a manual-changes checklist for anything the API cannot do.

## When to use / when NOT
Use when a deck/design has reviewer comments and the user asks to implement, address, or apply the feedback. Do NOT use for open-ended design creation (canva-edit-design) or pure critique (canva-design-feedback/get-design-feedback).

## Inputs, outputs, tools
- Inputs: design ID/link, reviewer comment threads.
- Outputs: committed design edits + per-thread replies + a manual-action checklist.
- Tools: Canva MCP — `resolve-shortlink`, `list-comments`, `list-replies`, `get-design-content`, `start-editing-transaction`, `perform-editing-operations` (ops: replace_text, find_and_replace_text, formatting, update_fill/insert_fill, delete_element, position/resize, update_title), `commit-editing-transaction`, `reply-to-comment`.

## 5 most important rules
1. Know the API ceiling first: can change text content/formatting, media fills, layout, title — CANNOT change font family, add text elements, backgrounds, pages, animations, opacity, grouping, or shapes.
2. Triage generously: interpret ambiguous comments with best judgement; escalate only on genuine contradictions or unfindable references.
3. Exactly ONE approval gate — after the user approves the plan, execute and commit without re-asking ("shall I commit?" is banned).
4. Batch all operations into one `perform-editing-operations` call per transaction.
5. Reply to every thread afterwards (what changed, or closest alternative + what remains manual).

## Risks / owner notes
Commits real edits to a live Canva design — the single approval step is the only safety gate; misread reviewer intent lands in the file. Manual-limitation replies still notify reviewers, so wording matters.

## Category and tags
Category: design. Tags: canva, mcp, review-feedback, comments, batch-edit, approval-gate.
