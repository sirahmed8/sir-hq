# branded-presentation

- Tool: `gemini-plugin` (plugin: `canva`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\canva\inactive-skills\branded-presentation\SKILL.md`
- SKILL.md size: 3080 chars

## What it does

Create on-brand Canva presentations from an outline or brief. Use when the user asks to create a branded presentation, make an on-brand deck, turn an outline into slides, or generate a presentation from a brief. Input can be text directly in the message, a Canva design ID, a reference to a Canva doc by name, or a Canva design link (e.g., https://www.canva.com/design/...).

## Structure (headings inside SKILL.md)

- Canva Branded Presentation Creator
- Workflow
- Presentation Query Format
- Notes
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - If the user provides a **Canva design ID** directly (typically starts with `D`, e.g. `DABcd1234ef`), use it as `design_id` with `Canva:start-editing-transaction` to read its contents; **do not** use `Canva:search-designs` for a raw ID
2. - If multiple brand kits exist, confirm selection before generating; if only one, use it automatically
3. - Autofill requires a Canva Enterprise plan

## Files inside the skill

- (SKILL.md only)
