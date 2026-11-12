# optimize-audio

Tools: gemini-plugin (unity plugin). Source: C:\Users\a7med\.gemini\config\plugins\unity\skills\optimize-audio\SKILL.md (199 lines) + resources/platform-settings.md, resources/audio-import-api.md

## Summary
A gated, measurement-first workflow for optimizing Unity audio: memory (import Load Types, Force To Mono, sample-rate overrides), DSP CPU (mixer group depth, effects on silent groups, buffer size), and playback quality (Vorbis/AAC settings, 3D stereo pitfalls). Every change runs through a live Editor via `unity command script eval`, is reported before/after, and verified in a device build — Editor stats are indicative only.

## When to use / not use
Use for Unity projects with audio memory bloat, DSP CPU spikes, slow loads, wrong 3D audio, or quality artifacts. Requires a reachable Editor with the Pipeline package and `script eval` — without it, the skill stops rather than hand-editing .meta files.

## Inputs, outputs, dependencies
Input: a Unity project with an open Editor connected to unity-cli. Output: audited AudioSources/importers/mixer with applied, verified setting changes. Needs: `unity-cli` skill, `com.unity.pipeline` package, `script eval` capability, and the two resources files for API recipes and platform matrices.

## Key rules
1. Never change before reporting findings; STOP at every WAIT checkpoint for user approval (assessment and mixer changes each gate).
2. `script eval` takes a statement block: no `using` directives, fully-qualified type names only.
3. Triage table routes symptoms: memory→import audit, CPU→mixer audit, 3D wrong→Force To Mono, artifacts→compression, mobile→sample rate, streaming→Load Type.
4. Key technical facts: stereo clip + spatialBlend=1 plays only left channel; effects run DSP even on silent groups; reverb on Master/high groups is the most expensive; halving sample rate halves PCM memory; lossy MP3 sources can't recover quality.
5. Validate by re-reading importer/source values after reimport, report before/after deltas, max 3 adjust-verify cycles.

## Risks / owner items
- Verify on device builds; Editor numbers mislead.
- `Load In Background` causes first-play silence — mitigate with preload or PlayScheduled, or use CompressedInMemory for immediate playback.
- Multiple AudioListeners = unpredictable spatialization; zero = silence.

## Category and tags
build, mobile — unity, audio, optimization, performance, game-dev.

## Revision note
Single plugin revision; unusually rigorous gating (WAIT checkpoints, measure-before-change) among the Unity skills.
