# gemini-omni-flash-api

## Summary
gemini-omni-flash-api is a Google-published skill for generative video editing, text-to-video, image-referenced video generation, first-frame-to-video, first-and-last-frame transitions, and video extensions using Gemini Omni 1.1 Flash (gemini-omni-1.1-flash) via the official google-genai SDK. The skill covers pre-processing/optimizing high-resolution or long source videos with ffmpeg, stripping audio for full sound regeneration, first-frame-to-video generation, first-and-last-frame transitions, and video extensions with parallel execution support. It also includes workflows for stripping audio, regenerating full sound, and handling turn-by-turn video editing. Reference files include video-processing, ffmpeg-config, and video-editing-patterns guides.

## When to use / when NOT
Use for generative video editing tasks (text-to-video, image-to-video, video extensions, transitions) with Gemini Omni 1.1 Flash. Do NOT use for static image generation, for non-Gemini video tools, or for tasks requiring frame-accurate control beyond Gemini's capabilities.

## Inputs, outputs, tools
- Inputs: Task type (text-to-video, image-to-video, video-extension, first-last-transition), source video (path or URI), reference image, audio preferences, ffmpeg parameters.
- Outputs: Video generation commands, ffmpeg preprocessing configs, generated video URIs, parallel execution schedules.
- Tools: `google-genai` Python SDK, `ffmpeg` CLI for preprocessing, SDK video API calls. References: video-processing, ffmpeg-config, video-editing-patterns .md files.

## 5 most important rules
1. Always pre-process source videos with ffmpeg before Gemini submission: normalize resolution, fps, and audio sample rate.
2. Strip audio from source video if full sound regeneration is desired; Gemini will regenerate audio from scratch.
3. Image-to-video: provide a key reference frame (first frame or specified timestamp); never submit without reference image for image-referenced generation.
4. Video extensions: specify exact start/end timestamps; Gemini extends beyond those boundaries by default.
5. Cost optimization: Gemini Omni Flash is cost-effective for short clips (<30s); for longer content, consider batching or segmenting.

## Risks / things needing the owner
Video quality depends on source ffmpeg preprocessing; user must verify output. Audio regeneration may differ from original source. No direct owner actions beyond console setup and ffmpeg availability.

## Category / tags
google · gemini, video, text-to-video, image-to-video, video-editing, omni-flash, ffmpeg, generative

## Revisions
Single revision in `C:\Users\a7med\.config\kilo\skills\gemini-omni-flash-api\SKILL.md` (Google-published, Apache-2.0, v1). Only kilo has this skill; scripts/references folders exist (scripts=True, refs=False per earlier check).