# urp-postprocessing

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: build
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\urp-postprocessing\SKILL.md`
- SKILL.md size: 11268 chars

## What it does

Sets up, configures, and debugs URP post-processing with the Volume framework. Use for bloom, tonemapping, color adjustments, depth of field, vignette, or other Volume overrides.

## When to use (from skill text)

- **Local Volume (optional, but takes precedence)**: GameObject with trigger `Collider` + `Volume` component, `isGlobal = false`. Properties:
- 5. `volume.isGlobal = true` (for global), or camera is inside the Volume's trigger `Collider` (for local)?

## Structure (headings inside SKILL.md)

- 0. Prerequisite: an Editor you can run C# in
- Passing C# to `script eval`
- 0. Pre-Flight Checks
- Pre-Flight Check Snippet
- 1. Volume Setup
- 2. Post-Processing Effects
- 3. Anti-Hallucination Rules
- Required Usings
- Wrong → Correct API Mapping
- Key Facts
- 4. Debugging Checklist
- 5. Common Recipes
- 6. Final Confirmation
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **Types must be fully qualified.** A bare `AssetDatabase` or `Volume` does not resolve
2. 2. **HDR is enabled on the URP Asset** — Required for Tonemapping. Bloom works best with HDR; in SDR it still works but `threshold` must be < 1.
3. 3. **Camera has post-processing enabled** — `renderPostProcessing` must be `true` (defaults to `false`). Camera Stacking: only a `CameraRenderType.Base` camera (or the last `Overlay` in the stack) should enable post-processing. Also verify the Renderer's PostProcessData asset is not null — if it is,
4. 4. **The Volume's GameObject layer is in the Camera's Volume Layer Mask** — `volumeLayerMask` defaults to layer 0 "Default" only. The Volume's `GameObject.layer` must be included, otherwise the camera ignores it.
5. 5. **Volume exists with `enabled = true`, a valid Profile, and at least one override** — The `Volume` component must be enabled, have a non-null `profile` (or `sharedProfile`), and at least one `VolumeComponent` with `overrideState = true` on its properties.

## Files inside the skill

- `references/code-templates.md` — ""
- `references/effect-reference.md` — ""
- `SECURITY.md` — "Security notes: urp-postprocessing"
