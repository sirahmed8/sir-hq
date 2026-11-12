# gemini-omni-flash-api

- Tool: `codex`
- Category: media
- Source: `C:\Users\a7med\.codex\skills\gemini-omni-flash-api\SKILL.md`
- SKILL.md size: 25785 chars

## What it does

Use this skill for generative video editing, text-to-video, image-referenced video generation, first-frame-to-video, first-and-last-frame transitions, and video extensions using Gemini Omni 1.1 Flash (gemini-omni-1.1-flash) via the official google-genai SDK. Includes workflows for pre-processing/optimizing high-resolution or long source videos with ffmpeg, stripping audio for full sound regeneration, and handling turn-by-turn video editing and parallel execution.

## When to use (from skill text)

- 2. **[generate_video.py](scripts/video/generate_video.py)**: Performs end-to-end video generation and downloads the output video. It detects and uploads local media references (images or videos) before calling the Interactions API. Large video assets (>25MB) will trigger informative pre-processing r
- * **Keep original audio**: By default, Gemini Omni Flash preserves the existing audio layer (though it may modify or adapt it slightly during generation). Use this when the original background music, dialogue, or sound effects are desired.
- * For a starting frame: `"Use this image as the starting frame."`

## Structure (headings inside SKILL.md)

- Gemini Omni Flash Skill
- Core capabilities
- Workflow
- Reference Documentation
- Dependencies and Prerequisites
- Available scripts
- Audio handling in video editing
- Prompting Gemini Omni Flash
- Single scene
- Removing unwanted elements
- Prompts for editing
- Prompting the audio
- Timing events
- Meta prompting
- Text in videos
- Prompts for extending a video
- Video extension constraints and guidelines
- Using tags in prompts to set image and video roles
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 1. **[upload_file.py](scripts/upload_file.py)**: Uploads local media (images and videos) to the Files API and polls until `ACTIVE`. If uploading a video larger than 25MB, it prints an informative warning/tip highlighting that Gemini Omni Flash is optimized for editing 10s videos at 720p/24fps, and r

## Key rules (verbatim lines from SKILL.md)

1. 3. **First and last frame transition**: Generating videos interpolating between a starting image and a final image (`--first-frame` and `--last-frame`; note: `--last-frame` must be used with `--first-frame`).
2. * **Files API**: Input media files (such as reference images and videos) must be uploaded via the [Files API](https://ai.google.dev/gemini-api/docs/files) first before being referenced in generations. The uploaded file URI and MIME type are then included in the `interactions.create` input parts arra
3. * **Python SDK (`google-genai`)**: Requires `google-genai >= 2.19.0` (Python) to support the `interactions` client and full video output resolution configuration (`360p`, `720p`, `1080p`, `4k`). Install or upgrade using:
4. * **Python Runtime**: Requires **Python >= 3.10** (for compatibility with modern `google-genai` SDK types and methods).
5. * **ffmpeg & ffprobe**: `prep_video.py`, `inspect_video.py`, and `generate_video.py` (when stripping audio via `--strip-audio`) require `ffmpeg` and `ffprobe` binaries installed and available in your system `PATH`.

## Files inside the skill

- `scripts/upload_file.py`
- `scripts/video/generate_video.py`
- `scripts/video/inspect_video.py`
- `scripts/video/prep_video.py`
