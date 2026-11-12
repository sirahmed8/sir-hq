# music-prompter

Source read: `C:\Users\a7med\.codex\skills\music-prompter\SKILL.md` (3.3 KB; codex revision; cursor/kilo/opencode/windsurf listed).

## Summary
Prompt-engineering playbook for AI music models (Suno v3.5/v4, Udio, ElevenLabs Music, MusicGen). Core formula: `[Genre & Era] + [Key Instruments] + [BPM & Time Signature] + [Vocal Profile] + [Mixing/Production Vibe]`, plus bracketed structural metatags in lyrics (`[Intro]`, `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Post-Chorus]`, `[Bridge]`, `[Solo]`, `[Drop]`, `[Outro]`) with energy/delivery notes per section. Gives a Suno formula (dense comma-separated style descriptors + metatagged lyrics with rhythm/cadence pairing) and a Udio formula (explicit genre lineages for vocal nuance). Safeguards: no vanity adjectives ("catchy", "amazing" — models lack semantic anchors; use `syncopated rhythm`, `pentatonic hook`, `minor 7th chords`), dynamic range management across sections, explicit vocal customization (gender/tone/delivery like `raspy baritone`, `autotuned hyperpop`).

## When to use / when NOT
Use when crafting prompts for Suno/Udio/ElevenLabs Music generation. Not for mixing/mastering existing tracks or for non-music audio (use sfx/voice tools).

## Inputs, outputs, tools
- Inputs: musical idea, emotion, genre, vocal/language needs, target platform.
- Outputs: ready-to-paste style prompts + fully metatagged lyric sheets.
- Tools: Suno, Udio, ElevenLabs Music, MusicGen (external services, owner accounts).

## 5 most important rules
1. Structure every prompt as genre+instruments+BPM+vocal profile+production vibe — multi-tier, not a sentence.
2. Use bracketed structural metatags with per-section energy/delivery direction.
3. Replace vanity adjectives with technical descriptors (intervals, rhythm, mixing terms).
4. Alternate high-density and stripped-back sections for dynamic range.
5. Specify vocals concretely: gender, tone, delivery style.

## Risks / owner notes
Generated music may imitate copyrighted styles/artists — keep prompts original and respect platform content policies. Output quality varies by model; expect multiple generations. Service costs/quota belong to the owner's accounts.

## Category and tags
Category: media. Tags: music-generation, suno, udio, prompt-engineering, lyrics, metatags.
