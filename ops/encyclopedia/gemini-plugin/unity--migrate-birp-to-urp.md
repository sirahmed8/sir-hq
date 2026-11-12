# migrate-birp-to-urp (unity plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\unity\skills\migrate-birp-to-urp\SKILL.md` (52 KB; unity plugin; `SECURITY.md` + `references/` incl. implementation-patterns.md with an Execution Regression Checklist). Planned BIRP→URP migration workflow.

## Summary
Phased Built-in Render Pipeline → URP migration with a strict honesty contract. Mandatory: read `references/implementation-patterns.md` before the first `script eval` that edits settings/materials/scenes. Flow: classify request (standard 3D URP / URP 2D / material-only / planning / troubleshooting) → inspect risks (opaque+particle/VFX materials, custom shaders, PPv2, cameras, baked lighting/lightmaps/reflection probes, Quality levels, representative scenes) → STOP before any pipeline-mutating work until rollback point confirmed (branch/backup/disposable copy) → execute in phases, each ending `Phase complete|partial|Blocked`: P0 inspect+plan, P1 URP setup+supported material conversion, P2 post-processing/camera migration (persistent URP VolumeProfiles, disable PPv2 for validation, SSR=unsupported), P3 lighting/lightmaps/probes, P4 save/reload/re-query validation. Generic-upgrade contract: discover features yourself, never ask the user to enumerate them; continue within a phase without "would you like me to continue?"; interrupted phases resume from saved state. Success gate is saved-state verification, not tool logs: Graphics+Quality→URP asset with valid default renderer, no "Default Renderer is missing", materials keep source maps/colors (no all-white `_BaseColor`), PPv2→persisted Volume with non-null components + scene Volume reference, lighting/probe state re-serialized correctly, representative scene captured, Console clean. "Complete" wording allowed ONLY when every gate passes; unsupported items (SSR, GrabPass, Surface Shaders, OnRenderImage, replacement/package shaders) must be named precisely as manual.

## When to use / when NOT
Use for converting a Unity project/scene/material/shader from Built-in RP to URP, or fixing visuals broken by the change. Not for HDRP targets, projects already on URP (troubleshooting path D covers partial states), or blind asset edits without a live Editor.

## Inputs, outputs, tools
- Inputs: Unity project state, user permission level (audit-only vs modify), rollback confirmation, target (URP vs URP 2D).
- Outputs: URP assets assigned, converted materials, Volume profiles, lighting/probe refresh, phase-status reports.
- Tools: `unity command script eval` via the unity-cli skill (needs `com.unity.pipeline` package = Editor 6000.3+; older Editors fail with misleading CS0246 on `IPreprocessBuildWithContext`/`BuildCallbackContext`), UnityEditor APIs.

## 5 most important rules
1. STOP before pipeline-mutating work (URP install, Graphics/Quality assignment, converters, material/scene edits) until a rollback point is confirmed — but keep auditing/planning freely.
2. Run `implementation-patterns.md` first; lower confidence and don't claim completion if it can't load.
3. Phase boundaries are honest: `Phase complete/partial/Blocked`; never force all phases into one turn or over-claim "fully migrated".
4. Success = saved-state re-query (URP asset+renderer, material fidelity vs pre-conversion snapshot, Volume persistence, lighting settings GUIDs, Console clean) — tool logs alone prove nothing.
5. Custom shaders/GrabPass/Surface Shaders/OnRenderImage/replacement shaders are scoped manual follow-ups, never automatic converter work; name unsupported PPv2 effects (SSR) precisely.

## Risks / owner notes
Real project mutation: magenta materials, broken lighting, lost post-processing are the classic failure modes — hence the rollback gate. Editor <6000.3 can't run the Pipeline package (migration targets are often old Editors — check first). Long lighting bakes cause phase interruptions; resume, don't restart.

## Category and tags
Category: mobile. Tags: unity, urp, render-pipeline, migration, post-processing, lighting, validation.
