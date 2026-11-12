# motion-graphics-engine

Source read: `C:\Users\a7med\.claude\skills\motion-graphics-engine\SKILL.md` (1.6 KB; claude revision; codex/cursor/gemini-plugin/kilo/opencode/windsurf listed).

## Summary
Programmatic motion-graphics pipeline: story/scene script → React Remotion timeline component → Remotion bundle + FFmpeg encoder → MP4/WebM. Three aesthetic styles: retro collage documentary (paper textures, torn borders, grain, 12fps step motion, Ken Burns), kinetic typography/tech explainers (word-synced caption pops with spring bounce, code diffs, terminal typing, animated SVG node diagrams), and production rules — all timing in frames (30/60fps) not wall-clock, `interpolate(frame, [start,end], [from,to], {extrapolateRight:'clamp'})` for pacing, audio normalized to -14 LUFS with ducking under voiceover.

## When to use / when NOT
Use for code-generated videos: explainers, kinetic type, collages, data-driven video at scale. Not for editing existing footage (that's an NLE/invideo) or for one-off manual motion design in After Effects.

## Inputs, outputs, tools
- Inputs: scene script, assets (images/audio/type), style choice, fps.
- Outputs: rendered MP4/WebM video files.
- Tools: React Remotion, FFmpeg, Canvas APIs; `interpolate` for animation.

## 5 most important rules
1. Time is frames, never seconds — pick 30 or 60fps and stay consistent.
2. Use `interpolate` with `extrapolateRight: 'clamp'` for all pacing.
3. Audio normalized to -14 LUFS with ducking under voiceover.
4. Match the aesthetic deliberately: collage-doc vs kinetic-type are different pipelines.
5. Script → timeline component → bundle+encode is the fixed architecture; don't hand-assemble frames.

## Risks / owner notes
Remotion/FFmpeg rendering is CPU-heavy and slow for long videos; license/plan limits on Remotion for companies may apply (Remotion has a company license requirement). Generated audio/video must not infringe music/footage rights.

## Category and tags
Category: media. Tags: remotion, ffmpeg, motion-graphics, kinetic-typography, video-generation, react.
