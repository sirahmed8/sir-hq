# create-tile-palette-or-rule-tiles

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\create-tile-palette-or-rule-tiles\SKILL.md`
- SKILL.md size: 1195 chars

## What it does

Create a 2D tile palette from sprites or textures, or make tiles change based on their neighbours. Use for tile palettes or self-connecting tiles, even when the user doesn't name them.

## Structure (headings inside SKILL.md)

- Create a tile palette
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **Tile Palette** — [references/palette-create.md](references/palette-create.md) — when the user wants to organize tiles for 2D level design or create a new rectangular, hexagonal, isometric, or isometric Z as Y grid layout.
2. - **Blank/empty RuleTile** (no sprites provided) — [references/ruletile-createempty.md](references/ruletile-createempty.md) — when the user wants a blank RuleTile (rectangular grid), HexagonalRuleTile, or IsometricRuleTile for custom rule configuration and has not provided or referenced any sprites.
3. - **RuleTile built from existing sprites** (sprites, terrain art, edge tiles provided) — [references/ruletile-createfromsegment.md](references/ruletile-createfromsegment.md) — when the user wants tiles that autotile as they paint, or a RuleTile built from existing terrain or edge sprites so tiles co

## Files inside the skill

- `references/hexagonalruletile.md` — "Skill: Advanced Hexagonal RuleTile Creation"
- `references/palette-create.md` — "Tilemap Palette Creation"
- `references/ruletile-createempty.md` — "Tilemap RuleTile Create Empty"
- `references/ruletile-createfromsegment.md` — "Tilemap RuleTile Create From Segment"
- `references/ruletile.md` — "Skill: Advanced RuleTile Creation"
- `scripts/CreatePaletteTemplate.cs`
- `scripts/ManualWorkflowExample.cs`
- `scripts/RuleTileGenerator.cs`
- `scripts/TilemapRuleTileCreateFromSegment.cs`
