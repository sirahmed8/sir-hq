# magnific-to-invideo (invideo plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\invideo\skills\magnific-to-invideo\SKILL.md` (554 bytes — thin hand-off skill, structurally identical to higgsfield-to-invideo).

## Summary
Bridge skill for users holding clips generated in Magnific who want a finished invideo video: upload the clips, review each, order them on a timeline with per-clip trimming, add captions/music/voice via `invideo-media` and `invideo-generate`, verify, export. Delegates procedure to `/invideo` and `docs.invideo.io/integrations/magnific` (`.md` suffix for markdown).

## When to use / when NOT
Use only for Magnific-sourced clips going into invideo. Not for Higgsfield footage (use higgsfield-to-invideo), HyperFrames compositions (hyperframes-to-invideo), or non-invideo workflows.

## Inputs, outputs, tools
- Inputs: Magnific-generated clip files.
- Outputs: finished, captioned, exported invideo project.
- Tools: invideo skills (`/invideo`, `/invideo-media`, `/invideo-generate`); invideo API per the linked doc.

## 5 most important rules
1. Read `/invideo` first — this skill carries no procedure of its own.
2. Upload then inspect every clip before sequencing.
3. Trim each clip to its best segment; do not concatenate raw footage.
4. All finishing (captions, music, voice) goes through the invideo media/generate skills.
5. Verify before export; the magnific integration doc has the exact calls and known fixes.

## Risks / owner notes
Same as sibling bridge skills: depends on live invideo API and the external doc remaining accurate.

## Category and tags
Category: media. Tags: invideo, magnific, video-editing, handoff, captions.
