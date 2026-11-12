# 2d-pixel-perfect

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\2d-pixel-perfect\SKILL.md`
- SKILL.md size: 9874 chars

## What it does

Sets up, diagnoses, and fixes pixel perfect 2D rendering with PixelPerfectCamera in URP or Built-in. Use when a retro-style or pixel art 2D game looks blurry, jittery, or misaligned. Not for HD 2D or high-resolution art.

## When to use (from skill text)

- ## When NOT to use this skill

## Structure (headings inside SKILL.md)

- ⚠ There Are Two Completely Separate Implementations
- When NOT to use this skill
- Critical Reminders
- Key Principles
- 1. Pipeline Detection & Camera Component Selection
- 2. Diagnostic-First Approach
- 3. Work in the correct scope
- Diagnostic Checklist
- API Reference
- Reference Resolution
- Migration & Compatibility
- URP project with the Built-in standalone component
- Old URP namespace (pre-Unity 2022 / URP pre-13.x)
- Common Issues & Solutions
- Blurry sprites
- Tilemap gaps between tiles
- Cinemachine conflict
- Post-processing blur with `upscaleRT`
- UI text blurry with `upscaleRT`
- Physics / render desync (micro-stutter)
- Non-integer scaling / pixel decimation
- Missing URP 2D Renderer
- HDRP fallback
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 3. Requires `com.unity.render-pipelines.universal` 12.0+

## Files inside the skill

- `references/api-reference.md` — "PixelPerfect Skill — Full API Reference"
- `references/camera-setup-builtin.cs`
- `references/camera-setup-urp.cs`
- `references/pipeline-detection.cs`
- `references/sprite-settings.cs`
