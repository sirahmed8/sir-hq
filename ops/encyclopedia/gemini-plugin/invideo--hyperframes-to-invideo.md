# hyperframes-to-invideo (invideo plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\invideo\skills\hyperframes-to-invideo\SKILL.md` (599 bytes — thin hand-off skill).

## Summary
Bridge skill for a HyperFrames composition that must be finished inside invideo: render the composition to MP4 at the final video's size and frame rate, upload it via `/invideo-media`, inspect it, then treat it as footage — cuts, captions, music, voice — verify, and export. Like its siblings it mandates reading `/invideo` first and points to `docs.invideo.io/integrations/hyperframes` (`.md` for markdown) for the full call sequence and fixes.

## When to use / when NOT
Use only when the source is a HyperFrames composition needing an invideo finishing pass. Not for raw camera footage or other motion tools; not for work that stays inside HyperFrames.

## Inputs, outputs, tools
- Inputs: a HyperFrames composition project; target resolution/frame rate.
- Outputs: MP4 intermediate, then a finished invideo export.
- Tools: HyperFrames renderer, invideo skills (`/invideo`, `/invideo-media`, `/invideo-generate`), invideo API per the linked doc.

## 5 most important rules
1. Read `/invideo` first; this file is only a routing stub.
2. Render to MP4 matching the FINAL video's dimensions and frame rate — mismatches cause rework downstream.
3. Upload via `/invideo-media` and actually look at the rendered footage before editing.
4. Treat the render as footage: cuts, captions, music, voice all happen in invideo.
5. Check the video before export; follow the hyperframes integration doc for exact calls.

## Risks / owner notes
Needs both HyperFrames (local render) and invideo (cloud) working; render settings must match delivery specs or the whole pass is wasted.

## Category and tags
Category: media. Tags: invideo, hyperframes, video-editing, render-handoff, mp4.
