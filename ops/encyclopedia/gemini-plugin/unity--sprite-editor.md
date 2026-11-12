# sprite-editor

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\sprite-editor\SKILL.md`
- SKILL.md size: 3617 chars

## What it does

Edits Unity sprite rectangles, borders, pivots, outlines, and slicing by generating C# scripts. Use when the user works with sprite sheets or sprite slicing.

## Structure (headings inside SKILL.md)

- Sprite Editor
- Passing C# to `script eval`
- Workflow
- Common Operations
- Important Notes
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **Never hand-edit a `.meta` file to change sprite metadata.** The importer owns that data
2. - **Types must be fully qualified.** A bare `AssetDatabase` or `Volume` does not resolve
3. - Requires: `EditSpriteName`, `EditSpriteRect`, `EditBorder`, or `EditPivot`
4. - Requires: `CreateAndDeleteSprite`
5. - Do NOT use AssetPostprocessor or MenuItem patterns

## Files inside the skill

- `references/api_reference.md` — "Unity Sprite Editor API Reference"
- `references/background.md` — "Sprite Editor Background Information"
- `references/templates.md` — "Sprite Editor Code Templates"
- `scripts/AutomaticSliceTexture.cs`
- `scripts/GenerateNewSpriteRects.cs`
- `scripts/GetTextureSourceImageSize.cs`
- `scripts/GetTextureToSlice.cs`
- `scripts/GridSliceTexture.cs`
- `scripts/IsometricSliceTexture.cs`
- `scripts/README.md` — "Sprite Editor Utility Examples"
- `scripts/SetPivotExample.cs`
- `scripts/SpriteToPng.cs`
- `SECURITY.md` — "Security notes: sprite-editor"
