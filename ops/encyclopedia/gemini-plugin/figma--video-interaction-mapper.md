# video-interaction-mapper

- Tool: `gemini-plugin` (plugin: `figma`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\figma\workflow-skills\video-interaction-mapper\SKILL.md`
- SKILL.md size: 12943 chars

## What it does

This skill should be used when the user asks to analyze a UI screen recording and map interaction states into Figma. Trigger for requests such as "put video frames in Figma", "extract states from my recording", "map interactions from video to Figma", "analyze this screen recording", "create a storyboard from my video", "deconstruct this interaction in Figma", "annotate the UI states in my recording", or "pull the key moments from this video into Figma". Also trigger when the user references a video file (.mp4, .mov, .webm, .avi) together with Figma, design review, interaction analysis, prototypes, or UI states. The skill extracts key visual moments from a video, infers interaction triggers, and builds an annotated Figma Design storyboard using native Figma annotations and uploaded screenshot assets.

## When to use (from skill text)

- before/after states, infer what triggered each change, then place clean screenshots,
- - Trigger: click, tap, keyboard input, hover, scroll, swipe, form submit, auto/timer,
- or unknown trigger when the cause is ambiguous.

## Structure (headings inside SKILL.md)

- Video Interaction Mapper
- Required Inputs and Tools
- Workflow
- 1. Validate and Prepare
- 2. Scout the Timeline Quickly
- 3. Analyze Key Moments
- 4. Resolve Selected Frames
- 5. Prepare Uploadable Screenshot Assets
- 6. Generate Figma Call Files
- 7. Execute in Figma and Upload Assets
- 8. Verify
- Output Expectations
- Edge Cases

## Tools / MCPs it needs

- MCP mentions: MCP tools

## Risks / cautions found in text

- - Visual change: modal, drawer, dropdown, tooltip, snackbar, overlay, navigation,

## Key rules (verbatim lines from SKILL.md)

1. - Native annotations use human labels and do not expose coordinate values.
2. - Missing trigger evidence: use `Unknown trigger` instead of guessing.
3. - `upload_assets` succeeds but images do not render: run the generated fill pass

## Files inside the skill

- `README.md` — "Video Interaction Mapper"
- `scripts/extract_key_frames.py`
- `scripts/generate_figma_calls.py`
- `scripts/prepare_upload_frames.py`
- `scripts/resolve_moment_frames.py`
- `scripts/update_run_manifest.py`
