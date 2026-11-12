# edit-design (canva-edit-design)

## Summary
The canonical safe edit engine for Canva designs, which other Canva skills build on: Transaction Protocol — `start-editing-transaction` (get transaction_id + pages, always show thumbnails) → `perform-editing-operations` (batched ops: replace/find_and_replace text, format_text, update/insert/delete media, position/resize, update_title, autofill) → `commit-editing-transaction` (explicit user approval gate) or `cancel-editing-transaction`. Documents the CAN/CANNOT capability boundary and the restricted op set on responsive pages.

## When to use / when NOT
Use for any change to an existing Canva design — text fixes, translations, media replacement, reformatting, repositioning. Other skills (implement-feedback etc.) delegate here. Do NOT attempt unsupported changes (font family, new text elements, backgrounds, page add/remove/reorder, animations, grouping) — tell the user it's manual in the editor.

## Inputs, outputs, tools
- Inputs: design ID/URL/shortlink, element_ids from the transaction's page content, operations array.
- Outputs: draft changes → committed permanent edit + link.
- Tools (MCP): Canva:resolve-shortlink, start-editing-transaction, perform-editing-operations, commit-editing-transaction, cancel-editing-transaction.

## 5 most important rules
1. ALWAYS start a transaction; changes are draft-only and permanently lost if not committed.
2. commit requires explicit user approval after showing preview + plain-language change list — never commit silently, never claim saved before commit succeeds.
3. Batch operations into one perform-editing-operations call; reuse transaction_id + pages array.
4. Responsive pages (`is_responsive: true`) allow ONLY update_title, replace_text, update_fill, delete_element, find_and_replace_text — check before calling.
5. After commit the transaction_id is invalid — a new edit needs a new transaction; always tell the user if a draft was discarded.

## Risks / things needing the owner
Commits are permanent — approval gate is mandatory. find_and_replace_text can hit unintended instances; confirm scope for destructive/broad ops. Skills with up-front batch approval (implement-feedback) may treat that as covering the commit.

## Category / tags
design · canva, editing, transaction, mcp

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\canva\skills\edit-design\SKILL.md` (active plugin copy, unlike the inactive-skills siblings). Only gemini-plugin holds it.
