# edit-design

- Tool: `gemini-plugin` (plugin: `canva`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\canva\skills\edit-design\SKILL.md`
- SKILL.md size: 5733 chars

## What it does

Make edits to an existing Canva design — change or fix text, replace/insert/delete images and videos, reformat text (size, weight, style, color, alignment, lists, line height), reposition or resize elements, and update the title. Use when the user wants to change, edit, update, fix, translate, replace, or reformat content in a specific Canva design. This is the safe edit engine that other Canva skills (e.g. implement-feedback) build on.

## Structure (headings inside SKILL.md)

- Canva Design Editing
- The Transaction Protocol (always these steps, in order)
- Capabilities — what the API CAN and CANNOT do
- CAN (operations on `perform-editing-operations`)
- CANNOT
- Responsive pages — restricted operation set
- The commit approval gate (required)
- Workflow
- Step 1: Resolve the design
- Step 2: Start the transaction and inspect
- Step 3: Build and perform operations
- Step 4: Preview and commit
- Rules
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Media**: `update_fill` (replace image/video), `insert_fill` (add image/video), `delete_element`
- - For destructive ops (`delete_element`, large `find_and_replace_text`), confirm scope before performing.

## Key rules (verbatim lines from SKILL.md)

1. 1. **`Canva:start-editing-transaction`** — pass the `design_id`. Remember the returned `transaction_id` and the `pages` array; both are required by later calls. ALWAYS show the user the thumbnail(s) returned here.
2. 3. **`Canva:commit-editing-transaction`** — save. See the approval gate below. After committing, the `transaction_id` is invalid; a new edit needs a new transaction.
3. 4. **`Canva:cancel-editing-transaction`** — discard the draft instead of saving (e.g. the user rejects the preview, or you opened a transaction only to inspect the design).
4. - Do NOT commit without approval.
5. - Do NOT tell the user changes are saved before the commit call has succeeded.

## Files inside the skill

- (SKILL.md only)
