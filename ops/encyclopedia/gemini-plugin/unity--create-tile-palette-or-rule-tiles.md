# create-tile-palette-or-rule-tiles (Unity)

## Summary
Router skill for Unity 2D tilemap work: picks one of three reference workflows — creating a Tile Palette (rectangular/hex/isometric/isometric-Z-as-Y grids) via `references/palette-create.md`, a blank RuleTile for custom rules via `ruletile-createempty.md`, or a RuleTile built from existing terrain/edge sprites for autotiling via `ruletile-createfromsegment.md` — plus helper C# scripts (CreatePaletteTemplate, RuleTileGenerator, TilemapRuleTileCreateFromSegment).

## When to use / when NOT
Use when the user wants a tile palette for level design, self-connecting/autotiling tiles, or mentions palettes/RuleTiles even without naming them. Do NOT use for tileset art creation or non-Unity engines.

## Inputs, outputs, tools
- Inputs: what the user wants (palette vs empty RuleTile vs sprite-driven RuleTile), optionally provided sprites.
- Outputs: a configured Tile Palette asset or RuleTile with neighbor-based rules.
- Tools: 5 reference docs under `references/` (palette-create, ruletile-createempty, ruletile-createfromsegment, ruletile, hexagonalruletile) and 3 editor scripts under `scripts/`.

## 5 most important rules
1. Route first: palette request → palette-create; blank rules → ruletile-createempty; existing sprites → ruletile-createfromsegment.
2. Read the matching reference before acting — it carries the exact steps.
3. Use the provided scripts/templates rather than hand-building palette assets.
4. Match grid type to the game (rectangular, hexagonal, isometric, isometric Z-as-Y).
5. Scope to what's asked — don't regenerate unrelated tile assets.

## Risks / things needing the owner
Creates/edits Unity assets in the project; wrong grid orientation is costly to redo. Requires Unity project context.

## Category / tags
build · unity, 2d, tilemap, gamedev, tooling

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\unity\skills\create-tile-palette-or-rule-tiles\SKILL.md` + references/scripts. Only gemini-plugin holds it.
