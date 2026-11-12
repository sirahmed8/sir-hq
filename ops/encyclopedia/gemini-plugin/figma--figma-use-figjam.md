# figma-use-figjam

- Tool: `gemini-plugin` (plugin: `figma`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\figma\skills\figma-use-figjam\SKILL.md`
- SKILL.md size: 6818 chars

## What it does

Use Figma's use_figma MCP tool in the FigJam.

## Structure (headings inside SKILL.md)

- use_figma — Figma Plugin API Skill for FigJam
- Inspecting FigJam Files
- Loading Reference Docs Efficiently
- Deferred Tools — Batch-Load Schemas
- Text Mutations — Canonical Recipe
- Adding Images to a FigJam Board
- Reference Docs
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP tool, MCP as, MCP resource, MCP tools

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **Use `get_figjam` upfront** before writing any `use_figma` code that needs to reference existing nodes (page IDs, section IDs, etc.). Don't try to discover IDs by running an inspection script — `console.log` output from `use_figma` is **not returned to the agent** (see [figma-use Critical Rule #4
2. - **`get_screenshot` requires a valid `nodeId`** — passing an empty nodeId returns "invalid nodeId" error. Get IDs from `get_figjam` first.

## Files inside the skill

- `references/batch-modify.md` — "Batch Operations Pattern"
- `references/create-code-block.md` — "Create Code Blocks"
- `references/create-connector.md` — "Create Connectors"
- `references/create-label.md` — "Create Label Nodes"
- `references/create-section.md` — "Create Sections"
- `references/create-shape-with-text.md` — "Create Shapes with Text"
- `references/create-sticky.md` — "Create Sticky Notes"
- `references/create-table.md` — "Create Tables"
- `references/create-text.md` — "Create Text Nodes"
- `references/edit-text.md` — "Text Operations"
- `references/figjam-colors.md` — "FigJam Colors"
- `references/plan-board-content.md` — "Plan Content for FigJam Boards"
- `references/position-figjam-nodes.md` — "FigJam Node Positioning Tutorial"
