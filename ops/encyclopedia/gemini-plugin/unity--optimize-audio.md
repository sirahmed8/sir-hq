# optimize-audio

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: media
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\optimize-audio\SKILL.md`
- SKILL.md size: 14602 chars

## What it does

Optimizes audio memory, CPU cost, and playback quality through import settings and mixer configuration. Use when asked to reduce audio memory or Audio Mixer CPU cost, change clip Load Types, sample rates or codecs, or force 3D audio to mono.

## Structure (headings inside SKILL.md)

- Critical Rules
- 0. Set up the execution path
- Passing C# to `script eval`
- 1. Pre-Flight: Detect Audio System
- 2. Assess Current State
- 3. Understand Request
- 4. Primary Diagnostic Workflow
- 4A. Force To Mono and Spatial Settings
- 4B. AudioMixer Audit
- 4C. Compression Quality Tuning
- 4D. Mobile Sample Rate Override
- 4E. Load Type and Streaming
- 5. Validation
- 6. Troubleshooting
- Stereo clip on a 3D AudioSource — only left channel audible
- Decompress On Load clip causes memory spike
- AudioMixer CPU spike — DSP thread hot
- Vorbis quality artifacts on dialogue
- AudioListener count is not exactly one
- `Load In Background` causes first-play silence
- 7. Completion
- Detailed References
- See Also
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 3. **Detect AudioListener:** Use the scene-component query recipe in [resources/audio-import-api.md](resources/audio-import-api.md) for `UnityEngine.AudioListener` to confirm exactly one listener is present. Multiple listeners produce incorrect spatialization; zero listeners produce silence.
- 4. **Report findings before making changes:** Summarize ALL detected sources, the listener count, and mixer depth to the user. Flag any immediate risks (e.g., stereo clip with `spatialBlend = 1`, Decompress On Load on a clip > 1 MB, reverb on the Master group).
- - **Multiple listeners:** Unity uses the last enabled one, producing unpredictable spatialization. Use the scene-component query recipe for `UnityEngine.AudioListener` and disable all but the intended one.

## Key rules (verbatim lines from SKILL.md)

1. - Do not make changes before reporting findings to the user
2. - Follow steps in strict order; never jump ahead
3. - STOP at every `WAIT` checkpoint and await the user's response before continuing
4. - Quality is more important than speed: measure before and after every change
5. - Always verify results in a device build; Editor audio stats are indicative only

## Files inside the skill

- `resources/audio-import-api.md` — "Audio Import API Recipes"
- `resources/platform-settings.md` — "Audio Platform Settings Reference"
- `SECURITY.md` — "Security notes: optimize-audio"
