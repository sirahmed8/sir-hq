# higgsfield-to-invideo (invideo plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\invideo\skills\higgsfield-to-invideo\SKILL.md` (568 bytes — a thin hand-off skill).

## Summary
A three-step bridge skill for users who have generated clips in Higgsfield and want a finished video in invideo: upload the clips, inspect each one, order them on a timeline trimming to the best part, then add captions/music/voice via `invideo-media` and `invideo-generate`, verify, and export. It defers all real procedure to the `/invideo` skill and the external doc `docs.invideo.io/integrations/higgsfield` (markdown variant by appending `.md`).

## When to use / when NOT
Use only when the input assets are Higgsfield-generated clips destined for an invideo finish. Do NOT use for other footage sources (see magnific-to-invideo, hyperframes-to-invideo) or for general video editing without invideo.

## Inputs, outputs, tools
- Inputs: local/remote Higgsfield clip files.
- Outputs: a finished, captioned, exported invideo project.
- Tools: invideo plugin skills (`/invideo`, `/invideo-media`, `/invideo-generate`); invideo API per the linked integration doc.

## 5 most important rules
1. Read `/invideo` first — this skill is a pointer, not a standalone procedure.
2. Upload clips then LOOK at each one before ordering (content check, not blind assembly).
3. Trim each clip to its best part rather than concatenating raw.
4. Captions, music, and voice go through `invideo-media`/`invideo-generate`.
5. Always verify the video before export; consult the higgsfield integration doc for exact calls and fixes.

## Risks / owner notes
Requires invideo account/API access. The skill itself contains no API details — everything lives in the external doc, so behaviour depends on that page staying accurate.

## Category and tags
Category: media. Tags: invideo, higgsfield, video-editing, handoff, captions.
