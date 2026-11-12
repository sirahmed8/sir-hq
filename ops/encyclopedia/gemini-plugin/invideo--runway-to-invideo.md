# runway-to-invideo

Tools: gemini-plugin (invideo). Source: C:\Users\a7med\.gemini\config\plugins\invideo\skills\runway-to-invideo\SKILL.md (14 lines, read in full)

## Summary
A 3-step adapter like its Remotion sibling: take Runway-generated clips, upload them into invideo, watch each one, order them on a timeline trimming to best segments, then add captions/music/voice via sibling skills and export. Delegates detail to `/invideo` and vendor docs.

## When to use / not use
Use when the user has clips generated in Runway (Gen-3 etc.) and wants a finished edited video. NOT for creating the clips (that's Runway's job) or for non-Runway footage sources.

## Inputs, outputs, dependencies
Input: Runway clip files. Output: exported invideo video. Needs: `/invideo` skill loaded first, `/invideo-media` for upload, `/invideo-generate` for captions/music/voice, docs at docs.invideo.io/integrations/runway.

## Key rules
1. Read `/invideo` first — thin adapter, not standalone.
2. LOOK at each clip after upload before ordering — verify assets landed correctly.
3. Timeline discipline: order clips, trim each to its best part — selection/editing happens in invideo, not by re-generating.
4. Captions/music/voice come from the sibling invideo skills, not ad-hoc tools.
5. Check the video, then export — verify before final render.

## Risks / owner items
- Same dependency profile as remotion-to-invideo: needs the full invideo plugin stack.
- No guidance on clip format/codecs or Runway-specific quirks — assumes upload compatibility.
- External docs URL may drift from actual API.

## Category and tags
media — runway, invideo, video, ai-generation, handoff.

## Revision note
Single 14-line adapter; identical structure to remotion-to-invideo, differing only in source tool.
