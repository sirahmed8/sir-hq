# figma-use-figjam

## Summary
FigJam-specific addendum to the figma-use skill: context and per-node-type reference docs for driving FigJam boards (`figma.com/board/...`) through the `use_figma` plugin API. It exists because FigJam differs fundamentally from Design files — no `createPage()`, a single implicit page, `get_metadata` unsupported, `get_figjam` as the inspection tool, and a different color/layout model. The 14 reference files cover every board primitive: sections, stickies, connectors, text, shapes-with-text, code blocks, tables, labels, positioning, batch edits, colors, and board-content planning.

## When to use / when NOT
Use for ANY `use_figma` work on a FigJam file (boards, retros, brainstorms, planning walls). Always include `figma-use-figjam` (prefixed `resource:` when MCP-loaded) in `skillNames`. Do NOT apply Design-file assumptions: `figma.createPage()` throws on FigJam, `get_metadata` fails, and `get_screenshot` needs a real nodeId.

## Inputs, outputs, tools
- Inputs: FigJam file URL/key, desired board content (template/retro/brainstorm/icebreaker), node operations.
- Outputs: board nodes (sections, stickies, connectors, text, shapes, tables, code blocks, labels) created/edited/positioned on the canvas.
- Tools: `use_figma`, `get_figjam` (returns full node tree as XML — the ONLY reliable way to discover node/page/section IDs since console.log is not returned), `get_screenshot` (needs nodeId), `upload_assets` (the ONLY way to add images), `create_new_file`, `whoami`; load figma-use first for foundation.

## 5 most important rules
1. Call `get_figjam` UPFRONT to get node IDs — never try to discover them via inspection scripts, because `use_figma` console output is not returned to the agent; only `return` values come back.
2. Never call `figma.createPage()` in FigJam (throws) and never use `get_metadata` (design-mode only); organize with sections instead.
3. Text mutations follow the canonical recipe: load font → await → mutate → return IDs; always load from `node.text.fontName`, never hardcode Inter Regular (FigJam sublayer defaults differ).
4. Batch tool-schema loading: one ToolSearch `select:` call for all deferred MCP tools, and issue all reference reads in a single parallel batch.
5. Images go through `upload_assets` only — POST raw bytes to returned single-use URLs; `nodeIds` attaches as fills, omit to drop onto the board.

## Risks / owner needs
Requires authenticated Figma MCP with FigJam file access. Large board builds should follow plan-board-content.md to avoid chaotic layouts.

## Category and tags
Category: design. Tags: figma, figjam, mcp, whiteboard, plugin-api, collaboration.

## Revisions
Single gemini-plugin figma copy; no competing revisions.
