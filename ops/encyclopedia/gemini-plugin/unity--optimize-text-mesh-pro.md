# optimize-text-mesh-pro

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: ops
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\optimize-text-mesh-pro\SKILL.md`
- SKILL.md size: 9575 chars

## What it does

Optimizes TextMeshPro rendering, memory, and font setup, including font asset stacks, fallback atlases, SDF quality, and worldspace text. Use when the user asks about TMP fonts, CJK or multilingual text, or text performance.

## Structure (headings inside SKILL.md)

- Optimize TextMeshPro
- Triage — identify the symptom first
- Core Rules
- Font Stack & Dynamic Fallbacks
- Padding & Sampling Ratios
- Font Asset Scale
- Sprite Assets
- AutoSize
- Atlas Render Mode: SDF16
- Font Normalization
- Material Presets
- Dynamic OS Atlas Population (TMP 3.2.0-pre.3)
- Memory Profiler: Include Font Data
- Worldspace vs Canvas Text
- Common Pitfalls
- References
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Keep Padding-to-Sampling-Point-Size ratio consistent across primary + fallback fonts.** Mismatch produces inconsistent glyph weight on the same line.
- - A primary font with one ratio and a fallback with a different ratio produces **inconsistent stroke widths** on the same line.
- - **CJK scripts**: 36-50 (CJK glyphs are visually denser; smaller sampling sizes still produce clean SDF and save atlas memory).
- 5. On the TMP Text component, pick the preset from the **Material Preset dropdown**.

## Key rules (verbatim lines from SKILL.md)

1. - One giant dynamic font asset for all languages instead of static main + dynamic fallback - the dynamic atlas balloons.

## Files inside the skill

- (SKILL.md only)
