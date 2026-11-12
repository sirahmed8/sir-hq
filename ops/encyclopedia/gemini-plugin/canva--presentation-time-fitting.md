# presentation-time-fitting

- Tool: `gemini-plugin` (plugin: `canva`)
- Category: build
- Source: `C:\Users\a7med\.gemini\config\plugins\canva\inactive-skills\presentation-time-fitting\SKILL.md`
- SKILL.md size: 8444 chars

## What it does

Fit a Canva presentation to a target speaking duration by generating or rewriting presenter notes only (visible slide text is not edited). Use when users say "make this a 10-minute presentation", "split time evenly across slides", "generate speaker notes for a 15-minute talk", "fit my deck to [duration]", or "how long per slide for a 20-minute slot".

## Structure (headings inside SKILL.md)

- Presentation Time-Fitting
- Primary workflow (time-balanced presenter notes)
- Step 1: Collect design and duration (before other Canva tool calls)
- Step 2: Resolve the design
- Step 3: Work on a copy (required)
- Step 4: Read slide content
- Step 5: Calculate time per slide
- Step 6: Generate speaker notes (in this session)
- Step 7: Write notes back to Canva
- Step 8: Hand off
- Scope: notes only
- When `start-editing-transaction` fails or times out
- Rules
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP exposes, MCP gateway, MCP timeout

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - Gather everything you need **before** calling `Canva:resize-design`, `Canva:get-design-content` or other editing/content tools:
2. - If either design or duration is missing, **ask and wait** before proceeding
3. - If the user provides a **design ID** directly (typically starts with `D`, e.g. `DABcd1234ef`), use it as `design_id`; **do not** use `Canva:search-designs` for a raw ID
4. - Use `Canva:resize-design` with the **same dimensions** as the source to clone the presentation; **do not** modify the original
5. - **Generate the notes directly in this response**; no external API call is required. For **each slide**, using that slide’s **text from Step 4** plus the **per-slide time/word budget from Step 5**, compose **presenter notes** (this is the only content you may author or edit for timing):

## Files inside the skill

- (SKILL.md only)
