# 2d-pixel-perfect

Source read: `C:\Users\a7med\.gemini\config\plugins\unity\skills\2d-pixel-perfect\SKILL.md` plus `references/` (pipeline-detection.cs, sprite-settings.cs, camera-setup-urp.cs, camera-setup-builtin.cs, api-reference.md).

## Summary
This Unity skill configures, diagnoses, and repairs pixel-perfect 2D rendering for URP or Built-in projects. It first detects the render pipeline because the two `PixelPerfectCamera` implementations are separate and incompatible, then checks sprite imports, editor snap settings, camera setup, and quality settings for the usual causes of blurry, jittery, or misaligned pixel art.

## When to use / when NOT
Use for retro or pixel-art 2D Unity games that look soft, unstable, or off-grid. Do not use for HD-2D or high-resolution art, UI-only scenes better handled by Canvas Scaler, or HDRP projects where Pixel Perfect Camera is unsupported.

## Inputs, outputs, tools
Inputs are the Unity project or scene scope, target sprites/tilemaps/cameras, desired reference resolution, and target PPU. Outputs are a diagnostic result plus applied import, camera, quality, and snap fixes. Tools are Unity Editor, URP `UnityEngine.Rendering.Universal.PixelPerfectCamera`, Built-in `UnityEngine.U2D.PixelPerfectCamera`, `com.unity.2d.pixel-perfect` for Built-in, CinemachinePixelPerfect, and the bundled C# reference snippets. No MCP is required.

## 5 most important rules
1. Detect the pipeline before any setup or diagnosis; never install the Built-in package in a URP project.
2. Diagnose before changing anything, and default to scene scope unless the user asks for project-wide work.
3. Force Point filtering, no mipmaps, uncompressed textures, consistent PPU, even sprite dimensions, and pixel-mode pivots.
4. Pick the reference resolution before producing assets and prefer `Windowbox` when the screen has no integer fit.
5. Disable AA, HDR, MSAA, and dynamic resolution, then use the correct enum API for URP or boolean API for Built-in.

## Risks / owner notes
The highest risk is treating the two camera systems as interchangeable or changing the reference resolution after assets exist. `UpscaleRenderTexture` can break post-processing and UI text, and Cinemachine blends are not pixel-perfect during transitions. The owner should confirm the art style, target resolutions, and platforms before applying point filtering.

## Category / tags
build · unity, 2d, pixel-art, rendering, urp, camera, graphics

## Revisions
Single source in the gemini-plugin Unity plugin. No other tool copy exists, so there is no revision comparison.
