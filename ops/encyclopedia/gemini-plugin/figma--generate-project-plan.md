# generate-project-plan

- Tool: `gemini-plugin` (plugin: `figma`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\figma\workflow-skills\generate-project-plan\SKILL.md`
- SKILL.md size: 27333 chars

## What it does

Generate a FigJam project plan board from a PRD plus codebase context. Interactive flow: research → propose sections → per-section deep research → per-section content + block-shape proposal → create FigJam → skeleton → fill → diagrams → wrap. Each content block (section, nested section, intro callout, table, multi-column text, sticky column, diagram section, metadata strip) has its own subskill reference file. Use when the user asks for 'project plan in FigJam', 'interactive project plan', '/generate-project-plan', or provides a PRD and wants per-section confirmation on content + rendering.

## When to use (from skill text)

- 4. Fire `AskUserQuestion`: "Use this content + shape? [Yes / Edit / Skip this section]."
- ## Trigger phrases

## Structure (headings inside SKILL.md)

- generate-project-plan
- Mandatory prerequisites
- Visual UI conventions — STRICT, do not deviate
- Colors (two-tone per section)
- Typography (font sizes)
- Section properties
- Outer wrapper + column alignment (STRICT defaults)
- Vertical spacing (STRICT)
- Tables
- Diagrams (right column)
- What NOT to use (common wrong defaults)
- Step template
- Step N — <Name>  [Type: Research | Confirm | Write]
- Step 1 — Gather context  [Research]
- Step 2 — Propose candidate sections  [Confirm]
- Step 3 — Per-section deep research  [Research]
- Step 4 — Per-section content + block proposal  [Confirm]
- Step 5 — Create FigJam file  [Write]
- Step 6 — Skeleton pass  [Write]
- Step 7 — Fill pass (one call per section)  [Write]
- Step 8 — Diagrams  [Write]
- Step 9 — Final review + report  [Write, then Read]
- Operational rules
- Trigger phrases
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP tool

## Risks / cautions found in text

- 1. Read the PRD. Extract: title, problem, goals, non-goals, owner, audience, success metrics, rollout hints, risks.
- 3. Produce the **tech-context object**: `files_read`, `services`, `external_deps`, `key_modules`, `architecture_notes`, `ownership`, `expansion_truncated`.
- 2. For each qualifying candidate, produce a card:
- 3. Produce a **gap list per section**: specific facts the user must supply, framed as answerable questions (no "figure it out yourself" gaps).

## Key rules (verbatim lines from SKILL.md)

1. - `figma-use-figjam` — **Re-load before every `use_figma` call.**
2. - `figma-generate-diagram` — **Re-load before every `generate_diagram` call.**
3. - Headers do NOT use white-on-dark — that's wrong for this board style.
4. 3. Produce a **gap list per section**: specific facts the user must supply, framed as answerable questions (no "figure it out yourself" gaps).
5. 5. Edit → accept free-text amendments, re-show, re-ask. Skip → mark the section as `skipped`; do not write it to the board.

## Files inside the skill

- `references/blocks/diagram-section.md` — "Block: Diagram section"
- `references/blocks/intro-callout.md` — "Block: Intro callout"
- `references/blocks/metadata-strip.md` — "Block: Metadata strip"
- `references/blocks/multi-column-text.md` — "Block: Multi-column text"
- `references/blocks/nested-section.md` — "Block: Nested section"
- `references/blocks/section.md` — "Block: Top-level section"
- `references/blocks/sticky-column.md` — "Block: Sticky column"
- `references/blocks/table.md` — "Block: Table"
- `references/blocks/text-primitives.md` — "Block: Text primitives (body, H3, bulleted list)"
- `references/foundation/codebase-grounding.md` — "Codebase grounding"
- `references/foundation/layout.md` — "Layout"
- `references/foundation/palette.md` — "Palette"
- `references/foundation/plugin-api-traps.md` — "Plugin API Traps"
- `references/section-catalog.md` — "Section catalog"
