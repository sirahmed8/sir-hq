# sprite-editor (gemini-plugin: unity)

## Summary
sprite-editor is a Unity plugin skill that edits sprite metadata (rectangles, borders, pivots, outlines, slicing) by generating C# editor scripts that run inside a live Unity Editor through the `unity-cli` `script eval` command. Sprite import settings live inside the TextureImporter/PSBImporter, not in editable files, so the only safe path is executing C# via `ISpriteEditorDataProvider`. The skill provides a "Safe Core Pattern" with mandatory capability checks (never attempt an operation if its capability check fails, to prevent corruption), nine example scripts (auto-slice, grid slice, isometric slice, set pivot, sprite-to-PNG, etc.), and references for the API, background and templates. It explicitly forbids AssetPostprocessor/MenuItem patterns and hand-editing .meta files.

## When to use / when NOT
Use when the user needs to programmatically change sprite slicing, pivots, borders or outlines on a sprite sheet inside a Unity project. Do NOT use when no Unity Editor is connected (it is a hard stop, not a cue to hand-edit .meta files), for non-sprite texture work, or for runtime sprite code (this is editor-time only).

## Inputs, outputs, tools
- Inputs: the target sprite/texture asset and the desired metadata change, expressed as a C# snippet passed to `unity command script eval --caller plugin --skill sprite-editor --code '<snippet>'`.
- Outputs: modified sprite importer data inside the Unity project, verified in the Unity console and Project window.
- Tools: `unity-cli` (install, connected-Editor check, `com.unity.pipeline` package, command catalog discovery), the live Unity Editor, and the bundled C# templates in `scripts/` and `references/templates.md`. Needs `script eval` specifically, which depends on the Pipeline package version.

## 5 most important rules
1. Follow the unity-cli skill first for Editor connectivity; `script eval` must appear in the command catalog before use.
2. `script eval` compiles a statement block, not a file: NO `using` directives (CS0210) and all types must be fully qualified (CS0246/CS0103/CS0104).
3. Never hand-edit `.meta` files for sprite metadata; the importer owns that data.
4. Every generated script must follow the Safe Core Pattern with mandatory capability checks; skip the operation entirely if a check fails.
5. Use enum values cast to numeric types, never magic numbers; generate standalone snippets without AssetPostprocessor or MenuItem.

## Risks / things needing the owner
Running C# inside the Editor can corrupt sprite importers if capability checks are bypassed; that is why the pattern is mandatory. Requires a licensed/running Unity Editor and the com.unity.pipeline package installed in the project. `unity command` defaults to a 30s timeout, so long operations need care. Nothing else needs the owner.

## Category / tags
build · unity, sprites, csharp, editor-scripting, game-dev

## Revisions
Only one revision exists in the gemini-plugin unity skills folder, with SECURITY.md, three reference docs and nine C# scripts beside it. No divergent copies.
