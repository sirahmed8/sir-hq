# invideo-timeline

- Tool: `gemini-plugin` (plugin: `invideo`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\invideo\skills\invideo-timeline\SKILL.md`
- SKILL.md size: 2423 chars

## What it does

Use for operations depth on an invideo timeline: frame math, tracks and layering, keyframes and motion, speed ramps, grades, LUTs, effects and custom shaders, audio buses, ducking and loudness.

## Structure (headings inside SKILL.md)

- Timeline operations
- Frame math
- Tracks and layering
- The locality test
- What to read
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - A video's sound is its own audio clip, linked to the picture. They move, trim and delete together.
- - Rippling ops shift everything later on the track: `edit_gap`, `delete_clip` with `close_gap`, `retime`, `edit_time_range` across every unlocked track. Use them when that shift is the point.

## Key rules (verbatim lines from SKILL.md)

1. - Read the rate from the timeline; never assume it.
2. - Prefer the op that holds the rest still. `roll` moves a cut and nothing after it; `slip_clip` changes what a clip shows without moving it.
3. - Before you send, say what should change. After, capture that moment and its neighbors and compare.

## Files inside the skill

- `references/audio.md` — "Audio: buses, effects and loudness"
- `references/color-and-effects.md` — "Color and effects"
- `references/keyframes.md` — "Keyframes and motion"
