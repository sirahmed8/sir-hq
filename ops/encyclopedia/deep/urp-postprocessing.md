# urp-postprocessing (gemini-plugin: unity)

## Summary
urp-postprocessing sets up, configures and debugs URP's Volume-based post-processing (Bloom, Tonemapping, ColorAdjustments, DepthOfField, Vignette, etc.). Goal stated upfront: working visual result with zero console errors. Requires a live Editor reachable via unity-cli, specifically `script eval`. The workflow: mandatory pre-flight checks first (URP is active pipeline, HDR enabled for Tonemapping, camera `renderPostProcessing` true, Volume GameObject layer inside camera `volumeLayerMask`, Volume enabled with non-null profile and overrides with `overrideState=true`), then Volume setup (global `isGlobal=true` vs local trigger collider with priority/blendDistance/weight), effect configuration via `profile.Add<T>()`, and an ordered 8-step debugging checklist ending in Game view (not Scene view). Includes wrong→correct API mapping (PostProcessVolume→Volume, PostProcessLayer→UniversalAdditionalCameraData.renderPostProcessing, GetSetting→TryGet, AddSettings→Add, sharedProfile vs profile runtime cloning), recipe presets (Cinematic/Stylized/Horror/Clean-Mobile), and references/effect-reference.md (all VolumeComponent properties) + code-templates.md.

## When to use / when NOT
Use for any URP post-processing effect request or "post-processing not working" debug. Do NOT use for Built-in pipeline projects, for shader-level effects, or when no Editor/`script eval` is available — say so and stop rather than guessing.

## Inputs, outputs, tools
- Inputs: effect list or bug description; live Editor via `unity command script eval`.
- Outputs: VolumeProfile asset with overrides, scene Volume/camera changes, a confirmation report.
- Tools: unity-cli + `script eval` C# snippets; two reference files.

## 5 most important rules
1. `script eval` takes a STATEMENT BLOCK: no `using` directives (CS0210), fully qualified types only, `return` gives the result back.
2. `overrideState = true` on every VolumeParameter you set — the #1 scripting mistake; unset params are silently ignored.
3. Pre-flight before effects: HDR on URP asset, camera renderPostProcessing, volumeLayerMask covers the Volume's layer (default is layer 0 only).
4. `sharedProfile` edits persist to the asset; `profile` auto-clones for runtime-safe edits — pick deliberately.
5. Verify in Game view; Scene view has its own post-processing toggle and lies about results.

## Risks / things needing the owner
Missing `script eval` (Pipeline version dependent) is a hard stop reported to the user. Local volumes need trigger colliders and correct layer masks — easy to misconfigure silently. HDR off breaks Tonemapping and constrains Bloom threshold. Nothing needs the owner beyond a running Editor.

## Category / tags
build · unity, urp, post-processing, rendering, volumes

## Revisions
Only one revision exists: `C:\Users\a7med\.gemini\config\plugins\unity\skills\urp-postprocessing\` with references/. No divergent copies.
