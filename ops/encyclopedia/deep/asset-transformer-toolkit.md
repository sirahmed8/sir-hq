# asset-transformer-toolkit

Source read: `C:\Users\a7med\.gemini\config\plugins\unity\skills\asset-transformer-toolkit\SKILL.md` (gemini-plugin revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
An Unity asset management skill that automates the transformation, conversion, and optimization of game assets (textures, models, audio, animations). It handles texture compression format conversion (ASTC, ETC2, DXT), model format migration (FBX, GLTF, OBJ), audio sample rate conversion, and animation clip optimization. The skill can batch-process assets across a project and generate editor scripts for ongoing pipeline integration.

## When to use / when NOT
Use when setting up or revamping a Unity asset pipeline, or when migrating assets between graphics APIs or platforms. Do NOT run asset conversion without backing up the original project files — the skill modifies files in-place and the skill will warn if it cannot find the project backup directory. Do NOT ignore the texture size limits per platform — the skill will flag textures that exceed platform-specific maximums (e.g., 8K on PC, 4K on mobile) and must be re-compressed.

## Inputs, outputs, tools
- Inputs: source asset directory, target platforms, compression settings, batch size, backup directory path.
- Outputs: transformed assets with platform-specific optimizations, conversion report (successes/failures), updated import settings, backup of original assets.
- Tools: Unity Editor, `texturecompressor` CLI, `fbx-converter`, `ffmpeg` for audio, `animator-controller` optimizer. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always specify a backup directory** — the skill will create a timestamped backup before any conversion; do not skip this or you cannot recover original assets.
2. **Configure platform-specific texture settings** — the skill supports ASTC (mobile), ETC2 (WebGL), DXT (PC); mixing formats across platforms will cause build failures.
3. **Run texture size validation after conversion** — the skill reports if any texture exceeds the maximum allowed size for the target platform; these must be addressed before building.
4. **Use batch sizes of 50-100 assets per run** — the skill can process larger batches but may run into memory issues; smaller batches are more reliable.
5. **Update import settings after batch conversion** — the skill modifies asset import settings; the Unity Editor must be restarted or the project reloaded for changes to take effect.

## Risks / owner notes
The most common data loss scenario is failing to specify a backup directory — converted assets cannot be reverted without the backup. The owner should always let the skill create the backup and verify it before proceeding. Texture format mismatches are the second most common issue; the skill's platform detection is generally reliable but should be verified for edge cases (e.g., Android vs. iOS).

## Category / tags
game-development · unity, asset-pipeline, texture, model, audio, optimization, pipeline

## Revisions
The gemini-plugin copy is the only revision available; no codex, kilo, or cursor copies exist. This is the canonical source for this skill.