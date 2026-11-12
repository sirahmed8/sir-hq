# get-design-feedback

- Tool: `gemini-plugin` (plugin: `canva`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\canva\skills\get-design-feedback\SKILL.md`
- SKILL.md size: 4682 chars

## What it does

Read a Canva design and return structured, actionable design feedback — visual hierarchy, copy/messaging, layout & spacing, consistency, readability, and accessibility. Read-only; makes no changes to the design. Use when the user asks to "review my design", "give me feedback on this", "critique my deck/poster/flyer", "how can I improve this design", or "what's wrong with this slide".

## When to use (from skill text)

- - **Element positions, sizes, and text** are reliably available from a **read-only** editing transaction: `Canva:start-editing-transaction`, inspect the returned `richtexts`/`fills`, then `Canva:cancel-editing-transaction` (never commit — you are not changing anything). Use this for layout/spacing/a

## Structure (headings inside SKILL.md)

- Get Design Feedback
- What you can actually read (and the gap to know about)
- Workflow
- Step 1: Resolve the design
- Step 2: Read the design
- Step 3: Evaluate across dimensions
- Step 4: Return structured feedback
- Feedback — "<design title>" (N pages)
- Top priorities
- Page-by-page
- What's working
- Step 5: Offer to act
- Rules
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **`Canva:get-design-thumbnail`** gives you the rendered image — this is how you "see" layout, hierarchy, balance, color, and contrast. Always pull this; visual critique depends on it.
2. - **Element positions, sizes, and text** are reliably available from a **read-only** editing transaction: `Canva:start-editing-transaction`, inspect the returned `richtexts`/`fills`, then `Canva:cancel-editing-transaction` (never commit — you are not changing anything). Use this for layout/spacing/a
3. - Never edit or commit anything — this skill is strictly read-only. If you open a transaction to inspect, always `cancel-editing-transaction`.
4. - Be candid but constructive; always pair a problem with a specific fix.

## Files inside the skill

- (SKILL.md only)
