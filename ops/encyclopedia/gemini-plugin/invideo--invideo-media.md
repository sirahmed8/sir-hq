# invideo-media (invideo plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\invideo\skills\invideo-media\SKILL.md` (1.1 KB; invideo plugin; `references/voice-music.md` exists).

## Summary
The media-sourcing sub-skill of invideo, ordered by preference: (1) the person's own files via `invideo asset upload`/`start_upload`, (2) stock via `invideo library search`/`search_library` + `invideo asset add`/`add_media`, (3) generation via `/invideo-generate` only as last resort. Before anything hits the timeline it mandates probing every file — `invideo media metadata`, `media video.frames`, `media audio.waveform` — and checking commercial-use rights for stock and generated media (stock arrives watermarked; exports render clean). `references/voice-music.md` covers voice-over, music, SFX, dialogue cleanup, and dubbing craft.

## When to use / when NOT
Use whenever a video needs footage, images, music, or voice and you must decide upload-vs-stock-vs-generate, or when verifying rights/quality of media before timeline placement. Not for timeline editing itself (`/invideo-timeline`) or pure generation (`/invideo-generate`).

## Inputs, outputs, tools
- Inputs: local files to upload, stock search queries, rights requirements.
- Outputs: project assets ready for the timeline, with metadata/frames/waveform verified.
- Tools: `invideo asset upload|add`, `library search`, `media metadata|video.frames|audio.waveform`; invideo library rights data.

## 5 most important rules
1. Source order is strict: own files → stock → generation (cheapest/most authentic first).
2. Probe EVERY file (metadata, frames, waveform) before timeline placement — never assemble blind.
3. Check commercial-use rights for stock AND generated media; stock previews are watermarked but export clean.
4. Read `/invideo` first; read `references/voice-music.md` for VO/music/SFX/dubbing craft.
5. Escalate to `/invideo-generate` only for gaps neither files nor stock fill.

## Risks / owner notes
Rights violations are a legal exposure — the rights check is mandatory, not optional. Uploading private footage into a cloud project needs the person's consent.

## Category and tags
Category: media. Tags: invideo, stock-footage, uploads, rights-check, voice-over, music.
