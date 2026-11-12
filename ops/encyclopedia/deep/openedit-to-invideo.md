# openedit-to-invideo

Tools: gemini-plugin (invideo plugin). Source: C:\Users\a7med\.gemini\config\plugins\invideo\skills\openedit-to-invideo\SKILL.md (14 lines, read in full)

## Summary
A thin handoff skill: when a user has an OpenEdit plan and wants it finished in invideo, it says to read the `/invideo` skill first, then render the plan to MP4 at the final video's size/frame rate, upload it via `/invideo-media`, inspect it, and edit it as footage (cuts, captions, music, voice) before exporting. Points to docs.invideo.io/integrations/openedit for the full call sequence.

## When to use / not use
Use only for the OpenEdit→invideo pipeline handoff. All actual invideo work (upload, edit, export) belongs to the `/invideo` skill; this file is a router, not a procedure.

## Inputs, outputs, dependencies
Input: an existing OpenEdit plan plus the `/invideo` skill's tooling. Output: an MP4 rendered at target specs, then a finished invideo export. Needs the invideo plugin's render/upload/edit capabilities and its media tools.

## Key rules
1. Read `/invideo` first — this skill delegates everything substantive.
2. Render at the final video's exact size and frame rate before upload.
3. Look at the uploaded footage before editing (verify, don't assume).
4. Check the edited video before export.

## Risks / owner items
- Depends entirely on the `/invideo` skill and plugin being installed; without them this file is dead weight.
- Requires an OpenEdit plan as input — it does not create one.

## Category and tags
media — invideo, openedit, video, workflow-handoff, mcp-plugin.

## Revision note
Single plugin revision; minimal router skill by design.
