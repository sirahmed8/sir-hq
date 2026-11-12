# audio-setup-mixers

Source read: `C:\Users\a7med\.gemini\config\plugins\unity\skills\audio-setup-mixers\SKILL.md` (gemini-plugin revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
An Unity audio configuration skill that sets up audio mixers, groups, and buses for game sound management. It handles audio source configuration, spatial sound setup, reverb effects, and volume automation. The skill can generate audio mixer assets that work across platforms and optimize audio performance by reducing DSP load and managing audio channel allocation.

## When to use / when NOT
Use when setting up or overhauling a Unity game's audio system — the skill provides a complete audio mixer configuration that works out-of-the-box. Do NOT create audio mixers manually without the skill's templates — the skill's structure is based on best practices for game audio and omits common pitfalls. Do NOT mix dB values with linear volume; the skill enforces dB scale for all volume automation and will convert raw 0-1 values to dB internally.

## Inputs, outputs, tools
- Inputs: sample rate, channel configuration, platform target, audio clip library, reverb preferences.
- Outputs: configured Audio Mixer asset, bus layout with names and volumes, audio source prefabs with spatial blend settings, DSP load report.
- Tools: Unity Editor, Audio Mixer window, `AudioSource` configuration, DSP meter, platform-specific audio APIs. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always use the skill's default mixer template** — it includes Master, SFX, Music, and UI buses with proper routing; starting from scratch often leads to missing buses or incorrect routing.
2. **Set reverb send levels per-audio-source** — the skill configures reverb sends at the source level; do not rely on global reverb settings alone for per-source control.
3. **Use dB scale for all volume automation** — the skill converts 0-1 linear values to dB; manually setting dB values without this conversion will result in incorrect volume levels.
4. **Configure platform-specific audio channels** — the skill adjusts channel counts based on target ( stereo for PC, 5.1 for console, stereo for mobile); do not use the same mixer setup across all platforms.
5. **Monitor DSP load during playtesting** — the skill can generate a DSP load report; if DSP usage exceeds 80%, the skill recommends reducing voice count or optimizing audio compression.

## Risks / owner notes
Incorrect dB settings are the most common issue — developers often set volume to 0 dB expecting maximum volume, but the skill's internal conversion may interpret this differently. The owner should rely on the skill's dB handling and verify volume levels in-game. DSP load spikes can cause audio stuttering; the owner should follow the skill's recommendations for voice reduction or compression optimization.

## Category / tags
audio · unity, audio-mixer, dsp, spatial-sound, reverb, platform-audio

## Revisions
The gemini-plugin copy is the only revision available; no codex, kilo, or cursor copies exist. This is the canonical source for this skill.