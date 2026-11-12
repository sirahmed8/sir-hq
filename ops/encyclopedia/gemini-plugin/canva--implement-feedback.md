# implement-feedback

- Tool: `gemini-plugin` (plugin: `canva`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\canva\skills\implement-feedback\SKILL.md`
- SKILL.md size: 7126 chars

## What it does

Implement reviewer feedback on a Canva design. Reads all comment threads, synthesises what reviewers want, makes the clear-cut changes directly, and flags anything that needs a human decision. Use when the user asks to "implement feedback on my deck", "address comments on a design", "apply review feedback", "fix the comments on my presentation", or "implement the feedback".

## Structure (headings inside SKILL.md)

- Feedback to Finished
- Canva Editing API — What You Can and Cannot Do
- What the API CAN do (via `perform-editing-operations`)
- What the API CANNOT do
- Triage rule
- Workflow
- Step 1: Resolve the Design
- Step 2: Read All Feedback
- Step 3: Triage the Feedback
- Step 4: Get User Approval — ONE time only
- Step 5: Apply and Commit the Changes
- Step 7: Present Remaining Manual Changes
- Changes to make manually in Canva
- Step 8: Resolve Comment Threads
- Rules
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Media**: replace images/videos (`update_fill`), insert new images/videos (`insert_fill`), delete elements (`delete_element`)

## Key rules (verbatim lines from SKILL.md)

1. - If the user provides a **design ID** directly (typically starts with `D`, e.g. `DABcd1234ef`), use it as `design_id`; **do not** use `Canva:search-designs` for a raw ID
2. - **Requires manual action** — the reviewer wants something the API cannot do (font family change, new text element, background change, page reorder, etc.). Note these briefly in the summary — full details go in the manual changes checklist (Step 7).
3. - Call `Canva:commit-editing-transaction` to save — do NOT ask "shall I commit?" or "ready to save?"
4. - After committing, call `Canva:reply-to-comment` on each actionable thread to note what was changed
5. - For "Requires manual action" threads, reply noting what was done as the closest alternative and what still needs manual attention

## Files inside the skill

- (SKILL.md only)
