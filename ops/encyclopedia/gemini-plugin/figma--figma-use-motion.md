# figma-use-motion

- Tool: `gemini-plugin` (plugin: `figma`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\figma\skills\figma-use-motion\SKILL.md`
- SKILL.md size: 8571 chars

## What it does

Add, inspect, and edit animations, easing.

## When to use (from skill text)

- ## When to use this skill

## Structure (headings inside SKILL.md)

- use_figma — Figma Plugin API Skill for Motion
- Runtime Gating
- When to use this skill
- Exposed motion API surface
- Reference docs
- Verifying the animation
- Pre-flight checklist
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP tool

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - Animating characters, words, lines, or paragraphs within editable text, including typewriter reveals and edits to the styles inside a text animation. Load [text-animation.md](references/text-animation.md) before writing.
2. 2. **Size to what you must read.** Start small — `constraint: { type: 'WIDTH', value: 320 }`, `quality: "low"` — but text and small elements blur there, so raise `WIDTH` (768+) when you need to judge fine detail. Omitting `constraint` = full size (1x; server clamps to 10x / 4096px).
3. - [ ] Ease-in-out uses the exact public enum `EASE_IN_AND_OUT` (or `EASE_IN_AND_OUT_BACK`); never emit the invalid alias `EASE_IN_OUT`.
4. - [ ] Timeline values are seconds in the public Plugin API. Extend via `setTimelineDuration`; never shorten unless the user asked.

## Files inside the skill

- `references/motion-custom-styles.md` — "Custom Animation Styles"
- `references/motion-easing.md` — "Motion Easing"
- `references/motion-patterns.md` — "Motion Patterns"
- `references/text-animation.md` — "Text animation"
