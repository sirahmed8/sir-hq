# optimize-text-mesh-pro

Tools: gemini-plugin (unity plugin). Source: C:\Users\a7med\.gemini\config\plugins\unity\skills\optimize-text-mesh-pro\SKILL.md (172 lines, read in full)

## Summary
A symptom-triage guide for TextMeshPro optimization in Unity: memory/atlas bloat, visual quality, CPU spikes, build size, and CJK/Latin alignment issues. Core pattern is a static main font with dynamic fallbacks, consistent padding ratios, and disabling runtime costs (AutoSize, worldspace UGUI) once layout locks.

## When to use / not use
Use for TMP font, multilingual/CJK text, atlas memory, or text performance questions in Unity. Triage first: if the user hasn't named a symptom, ask which category (memory, quality, CPU, build size, localization) before advising.

## Inputs, outputs, dependencies
Input: a Unity project using TMP plus a described symptom. Output: targeted recommendations (font stack changes, import settings, component swaps). Needs Unity Editor access for applying changes; TMP 3.2.0-pre.3+ for the Dynamic OS atlas option.

## Key rules
1. Main font = static asset with glyphs baked; dynamic fallbacks via Fallback list at 512-1024 atlas; NEVER ship a dynamic fallback without `Clear Dynamic Data On Build` (editor-baked glyphs ship otherwise).
2. Keep padding-to-sampling-point-size ratio consistent across all fonts in the chain (10% safe default); Latin sampling 70-90, CJK 36-50; Font Asset Scale must be 1.
3. Disable AutoSize once layout locks; use `TextMeshPro` (not UGUI) for worldspace text; parent volatile text to its own Canvas to bound rebuild cost.
4. Material presets beat duplicated font assets for style variants; SDF16 render mode for point sizes ≥72; sprite source textures must be Default type, not Sprite.
5. For multilingual mobile builds, evaluate `Atlas Population Mode = Dynamic OS` (uses system fonts: NotoSans Android, PingFang iOS) to cut build size and memory.

## Risks / owner items
- Importing TMP Examples & Extras can infinite-loop on some project layouts (close/reopen Unity fixes).
- iOS uses different CJK font families per language — check fallback chains when shipping Chinese+Japanese+Korean.
- Editor Memory Profiler overstates font cost unless `Include Font Data` is deselected on .ttf/.ttc imports.

## Category and tags
build, mobile — unity, textmeshpro, fonts, localization, optimization, game-dev.

## Revision note
Single plugin revision; practical TMP-specific rule set with measured defaults.
