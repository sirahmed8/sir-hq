# 2d-pixel-perfect

Source read: `C:\Users\a7med\.gemini\config\plugins\unity\skills\2d-pixel-perfect\SKILL.md` (gemini-plugin/unity revision; only source).

## Summary
A Unity skill that sets up, diagnoses and fixes pixel-perfect 2D rendering with PixelPerfectCamera in URP or Built-in pipelines. It detects which render pipeline the project uses (the two implementations are separate and incompatible), then walks a diagnostic checklist covering sprite import settings, editor snap grid, camera setup, and project quality settings, fixing the usual causes of blurry, jittery or misaligned pixel art (bilinear filtering, anti-aliasing, non-integer scaling, PPU mismatches).

## When to use / when NOT
Use for retro-style or pixel-art 2D Unity games that look blurry, jittery or misaligned. Do NOT use for HD 2D or high-resolution art (point filtering ruins smooth art), UI-only scenes (use Canvas Scaler), or HDRP projects (Pixel Perfect Camera unsupported there).

## Inputs, outputs, tools
- Inputs: Unity project path, render pipeline type, target sprites/tilemaps/cameras.
- Outputs: diagnostic report plus applied fixes to sprite import settings, camera components, quality settings, editor grid.
- Tools: Unity Editor, URP/Built-in PixelPerfectCamera, `com.unity.2d.pixel-perfect` package (Built-in only), CinemachinePixelPerfect extension. No MCP.

## 5 most important rules
1. **Detect the render pipeline first** — URP uses `UnityEngine.Rendering.Universal.PixelPerfectCamera` (enums), Built-in uses `UnityEngine.U2D.PixelPerfectCamera` (booleans); never install the standalone package in a URP project.
2. **Filter Mode = Point (no filter)** on all in-scope sprites; bilinear filtering is Unity's default and the #1 cause of blurry sprites.
3. **Anti-aliasing must be disabled** in Quality Settings and on the camera; AA actively blurs pixel edges.
4. **Choose the reference resolution before producing assets** (e.g. 320x180) and never change it afterward; use `cropFrame = Windowbox` when no integer fit exists.
5. **Sprite pivots in Pixels mode** for odd-dimension sprites (e.g. 15x15) so the pivot lands on a whole pixel, avoiding 0.5px misalignment.

## Risks / owner notes
Wrong pipeline detection leads to adding the wrong component and subtle bugs. Changing reference resolution mid-project breaks all assets. Cinemachine blends between virtual cameras are never pixel-perfect. Owner must confirm target platforms/resolutions and that art is actually pixel art before applying point filtering. No secrets involved.

## Category / tags
build · unity, 2d, pixel-art, rendering, urp, camera, graphics

## Revisions
Single source (gemini-plugin/unity). No other tool ships this skill, so no revision comparison.