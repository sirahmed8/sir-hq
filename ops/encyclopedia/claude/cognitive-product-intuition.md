# cognitive-product-intuition

- Tool: `claude`
- Category: design
- Source: `C:\Users\a7med\.claude\skills\cognitive-product-intuition\SKILL.md`
- SKILL.md size: 2986 chars

## What it does

Use when a UI or flow feels confusing, clone-like, or high-friction and needs checking against human mental models and wizard step order.

## Structure (headings inside SKILL.md)

- Cognitive Product Intuition & Anti-Clone Architecture Protocol
- 1. Eradicate "Clone Syndrome" (Distinct Mental Models)
- 2. The Causality & State Sequence Law (Linear Wizards)
- 3. The "Human Friction" & Common-Sense Checklist
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Previous Steps are Revisitable**: Users can click backward to review prior steps, with clear warnings if changing earlier inputs invalidates downstream progress.
- - **Confirmation for Destructive Actions**: Purging files, deleting accounts, or resetting configurations must require an explicit confirmation modal with the destructive action styled in high-visibility danger red.

## Key rules (verbatim lines from SKILL.md)

1. - **Future Steps are STRICTLY LOCKED**: Users must **never** be able to click on future steps before completing and validating earlier steps. Stepper numbers or progress bars are read-only visual milestones, NOT arbitrary navigation links.
2. - **Zero Premature Success**: Never display "Done!" or "Completed!" while background disk writes, network downloads, or indexing workers are still active.
3. - **Confirmation for Destructive Actions**: Purging files, deleting accounts, or resetting configurations must require an explicit confirmation modal with the destructive action styled in high-visibility danger red.
4. - **No Misleading Clickables**: Any element with hover styling or a pointer cursor must have a real, functioning click handler.
5. - **Zero Dead-End States**: If an error occurs during an operation, never trap the user. Always provide an explicit "Back", "Retry", or "Cancel" action.

## Files inside the skill

- (SKILL.md only)
