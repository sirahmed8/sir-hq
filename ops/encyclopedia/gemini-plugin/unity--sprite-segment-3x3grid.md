# sprite-segment-3x3grid (gemini-plugin: unity)

## Summary
sprite-segment-3x3grid is a Unity plugin skill that analyzes a sprite's texture by dividing its rect into a 3x3 grid and printing a compact text signature of its color structure. It finds the majority color of the center cell, then marks each of the 8 surrounding cells as `.` (meets the match threshold, default 75% of pixels matching) or `X` (does not), with `*` always marking the center. Output is three space-separated triplets like `. X X / X * X / X X .`. The skill ships one C# template (`scripts/SpriteGridAnalysis.cs`, `AnalyzeSpriteGrid(sprite, matchThreshold, colorTolerance)`) that implements majority-color detection with an RGB tolerance and Y-flip for Unity texture coordinates.

## When to use / when NOT
Use when documenting, testing, cataloging or comparing sprites by their color distribution, or verifying a sprite has the expected symmetric/asymmetric structure. Do NOT use for actually editing sprites (that is sprite-editor), for sprites with gradients/many colors where a 3x3 majority-color test is meaningless, or for runtime gameplay logic.

## Inputs, outputs, tools
- Inputs: a `Sprite` object (its `rect` and `texture`), a match threshold (50%/75%/90%, default 75%) and a color tolerance for "same color" comparisons.
- Outputs: a single-line text signature of 9 symbols in `row / row / row` format.
- Tools: Unity's `Sprite`, `Texture2D` pixel APIs and the bundled C# template; runs inside the Unity Editor context (via the same unity-cli pipeline as sprite-editor). No external services.

## 5 most important rules
1. The center cell [1,1] is always `*` and defines the majority color everything else is compared against.
2. Default threshold is 75% pixel match; expose it as a parameter (50/75/90 map to lenient/moderate/strict).
3. Use a color tolerance (e.g. RGB distance) rather than exact equality, and decide explicitly how transparent pixels are treated.
4. Divide `sprite.rect.width/height` by 3 for cell bounds; flip the Y axis to get top-to-bottom output.
5. Tie-break majority color by first-encountered; document edge cases (tiny sprites, <3px cells) before running.

## Risks / things needing the owner
Low risk: read-only pixel analysis. Edge cases are sprites smaller than 3x3 pixels or fully transparent textures, which produce degenerate output; the skill does not guard against them. Requires a running Unity Editor like the rest of the plugin. Nothing needs the owner.

## Category / tags
build · unity, sprites, analysis, csharp, game-dev, testing

## Revisions
Only one revision exists: `C:\Users\a7med\.gemini\config\plugins\unity\skills\sprite-segment-3x3grid\` (SKILL.md plus SpriteGridAnalysis.cs). No divergent copies.
