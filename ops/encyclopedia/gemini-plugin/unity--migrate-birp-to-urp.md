# migrate-birp-to-urp

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\migrate-birp-to-urp\SKILL.md`
- SKILL.md size: 52394 chars

## What it does

Plans, executes, and troubleshoots migration from the Built-in Render Pipeline to URP. Use when asked to convert a project, scene, material, or shader to URP, or to fix visuals broken by the change.

## When to use (from skill text)

- 5. Do not rely on the user writing a detailed checklist prompt to get correct behavior. The detailed checklist is for benchmarking or stress testing; normal user prompts should still trigger this phased contract.
- 2. The URP asset has a valid default renderer in saved state, and current Console output does not contain unresolved render-pipeline errors such as "Default Renderer is missing". If a renderer error appears after assignment, re-query the saved renderer list/default index, clear stale Console output 
- timeout, which matters here: installing URP triggers a package refresh and domain reload that will

## Structure (headings inside SKILL.md)

- Mandatory Execution Reference
- Critical Default
- Generic Upgrade Contract
- Generic Migration Success Gate
- Execution path: running C# in the Editor
- Passing C# to `script eval`
- Two execution modes — pick by the snippet's shape
- Detecting the active render pipeline
- 0. Pre-Flight: Pipeline Detection and Reference Loading
- 1. Assess Current Migration State
- 2. Gather Requirements
- Information to Gather
- 3. Safety Gate
- 4. Choose the Migration Path
- Path A: Standard 3D Built-in to URP
- Path B: Built-in 2D to URP 2D
- Path C: Targeted Material-Only Conversion
- Path D: Troubleshooting an Existing Migration
- 5. URP Setup Workflow
- 6. Conversion Workflow
- 7. Shader and Material Triage
- 8. Post-Processing, Cameras, and Rendering-Effect Triage
- 9. Quality, Lighting, and Visual Parity Review
- 10. Validation
- 11. Troubleshooting Decision Tree
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 3. Inspect migration risks before recommending changes: opaque materials, particle/VFX materials, custom shaders, post-processing, camera effects, baked lighting/lightmaps/reflection probes, Quality levels, and representative scenes.
- - Phase 0: Inspect and plan. Detect pipeline state, representative scenes, rollback safety, PPv2, material/shader risks, Quality levels, lighting/lightmap/probe state, and custom render code.
- 6. A generic migration request gives permission to inspect and plan, but it does not prove rollback safety. If no rollback point is confirmed, stop before package install or URP assignment and ask for confirmation. Do not leave the project in a magenta partial state just to reach the backup question
- 8. At the end of a phase, give a concise next-phase prompt or say what phase should run next. Ask for confirmation before the next phase only when it introduces a new costly or risky operation, such as a long lighting bake, deletion/cleanup of legacy assets, or a custom shader rewrite.

## Key rules (verbatim lines from SKILL.md)

1. 3. Inspect migration risks before recommending changes: opaque materials, particle/VFX materials, custom shaders, post-processing, camera effects, baked lighting/lightmaps/reflection probes, Quality levels, and representative scenes.
2. 4. Stop before any pipeline-mutating work until the user confirms a rollback point such as a branch, backup, archive, or disposable copy. Pipeline-mutating work includes installing URP, assigning a URP asset in Graphics/Quality settings, running converters, and editing materials or scenes.
3. 7. Validate representative scenes, Console output, camera rendering, lighting/baked GI state, materials, post-processing persistence, and quality-level assignments before declaring full migration success.
4. 1. Do not ask the user to enumerate known Built-in features before inspection. Discover them.
5. 5. Do not rely on the user writing a detailed checklist prompt to get correct behavior. The detailed checklist is for benchmarking or stress testing; normal user prompts should still trigger this phased contract.

## Files inside the skill

- `references/capturing-the-editor.md` — "Capturing the Editor for visual checks"
- `references/complex-shader-situations.md` — "Complex Shader Situations"
- `references/custom-shader-triage.md` — "Custom Shader Triage"
- `references/implementation-patterns.md` — "Built-in to URP Implementation Patterns"
- `references/migration-workflow.md` — "Built-in to URP Migration Workflow"
- `references/quality-settings-map.md` — "Quality Settings Map"
- `SECURITY.md` — "Security notes: migrate-birp-to-urp"
