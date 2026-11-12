# invideo-timeline (invideo plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\invideo\skills\invideo-timeline\SKILL.md` (2.4 KB; invideo plugin; `references/{keyframes,color-and-effects,audio}.md` exist).

## Summary
The operations-depth manual for editing an invideo timeline: an edit is a list of operations applied all-or-none; look up each op's fields via `timeline_catalog` before first use and `dry_run: true` before big changes land. It teaches frame math (`_f` fields are frames at the timeline's own rate — read the rate, never assume; ranges are start-inclusive/end-exclusive; reads return `{value, rate}`), track layering (higher video tracks draw over lower; build footage → grade adjustment clip → type/overlays; a video's sound is its own linked audio clip; one job per track, named and locked), the "locality test" (a small edit must move nothing else — prefer `roll`/`slip_clip` over rippling ops like `edit_gap`/`retime`/`edit_time_range` unless the shift is the point), and points to reference docs for keyframes/easing/speed ramps, grades/LUTs/masks/transitions/shaders, and buses/ducking/loudness.

## When to use / when NOT
Use for precise timeline work: frame-accurate cuts, keyframes, grades, effects, audio mixing. Not for high-level project flow (`/invideo`) or media sourcing (`/invideo-media`).

## Inputs, outputs, tools
- Inputs: timeline URL/ops list, op field specs from `timeline_catalog`, dry-run validation.
- Outputs: applied timeline edits (all-or-none), verified by frame captures.
- Tools: `invideo edit change`/`edit_timeline`, `timeline_catalog`, `dry_run`; docs reference/edit-operations.

## 5 most important rules
1. Read `/invideo` first; every edit is an op list applied atomically — look up fields before first use of each op.
2. `dry_run: true` before any big edit lands.
3. Frame math: `_f` = frames at the timeline's OWN rate (read it); ranges exclude the end; never assume 24/30fps.
4. Locality test: prefer ops that hold the rest still (`roll`, `slip_clip`); rippling ops (`edit_gap`, `delete_clip`+close_gap, `retime`, `edit_time_range`) only when shifting everything later is intended.
5. Layer deliberately: footage → adjustment-clip grade → type/overlays; name and lock tracks; verify by capturing the changed moment plus neighbors.

## Risks / owner notes
Rippling ops can silently shift the whole timeline — the before/after capture comparison is the only catch. Wrong frame-rate assumptions corrupt every timestamp.

## Category and tags
Category: media. Tags: invideo, timeline, keyframes, color-grading, audio-mixing, frame-math.
