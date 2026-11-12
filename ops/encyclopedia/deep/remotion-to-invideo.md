# remotion-to-invideo

Tools: gemini-plugin (invideo). Source: C:\Users\a7med\.gemini\config\plugins\invideo\skills\remotion-to-invideo\SKILL.md (14 lines, read in full)

## Summary
A 3-step handoff: take an existing Remotion composition, render it to MP4 at final size/frame rate, upload it into invideo as footage, then edit it there (cuts, captions, music, voice) and export. Delegates all detail to the parent `/invideo` skill and the invideo Remotion-integration docs.

## When to use / not use
Use when the user has a Remotion composition and wants it finished inside invideo's editor pipeline. NOT for creating the composition itself (that's Remotion work) or for pure invideo-native projects with no Remotion source.

## Inputs, outputs, dependencies
Input: a Remotion composition. Output: an exported invideo video. Needs: Remotion toolchain to render MP4, `/invideo` skill loaded first, `/invideo-media` upload path, docs at docs.invideo.io/integrations/remotion.

## Key rules
1. Read `/invideo` first — this skill is a thin adapter, not standalone.
2. Render at the FINAL video's size and frame rate — mismatched specs create re-work downstream.
3. Upload then LOOK at it before editing — verify the render landed correctly.
4. Treat the MP4 as footage: cuts/captions/music/voice are invideo edits, not Remotion re-renders.
5. Check the video, then export — verification precedes export.

## Risks / owner items
- Entirely dependent on the invideo plugin's other skills and docs; if `/invideo` is absent this file alone is insufficient.
- No guidance on render settings beyond "final size/frame rate" — codec/bitrate choices are delegated.
- Docs URL is external; skill content may drift from invideo's actual API.

## Category and tags
media — remotion, invideo, video, handoff, pipeline.

## Revision note
Single 14-line adapter skill; intentionally minimal, points to parent skill + vendor docs.
