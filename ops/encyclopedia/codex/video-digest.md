# video-digest (claude revision)

## Summary
video-digest turns a short video link (TikTok/Reel/Short/anything yt-dlp supports) or local file into `_local/videos/<id>/digest.md` containing title, source, language, full transcript, scene notes, 5 key takeaways and product ideas for SIR. It's a wrapper skill around repo scripts: `scripts/video_digest.py <URL|file>` (flags: `--force` re-digest, `--no-vision` transcript only) and `video_digest_batch.py` (`--urls list.txt` or `--dir`). Pipeline inside the script: yt-dlp downloads (cookie-less first, one `--cookies-from-browser chrome` retry; cookies never printed) → ffmpeg extracts 16kHz mono audio + 6 JPEG frames → Groq whisper-large-v3-turbo transcribes (`GROQ_API_KEY`, falls back to local faster-whisper) → Gemini (GOOGLE_AI_STUDIO_KEY, model chain gemini-3.6-flash→3.5-flash/latest, retries 503/429) describes frames and writes takeaways. Keys live in gitignored `_local/api-keys.env`; models overridable via VIDEO_* env vars.

## When to use / when NOT
Use when the owner sends a video link/file asking what it's about, a summary, or product ideas. Read-only analysis — it never posts or downloads beyond `_local/videos/`. Do NOT use for long-form research (it's built for shorts), and don't paste private video digest content into shared reports/bus/messages.

## Inputs, outputs, tools
- Inputs: URL or local video path; batch via URL list file or directory.
- Outputs: `digest.md` per video (last stdout line is the path); skips finished ones unless --force.
- Tools: yt-dlp, ffmpeg, Groq Whisper API, local faster-whisper fallback, Gemini API, `agent-reach` as text fallback.

## 5 most important rules
1. Output stays in gitignored `_local/videos/` — never copy videos/transcripts/digests into git or other projects.
2. Private/personal videos: digest is for the owner only — never paste into shared files.
3. Login walls/CAPTCHA: report platform + error plainly; no retry loops, no bypass attempts; try `agent-reach read <url>` for captions.
4. Never print API key values; keys come from `_local/api-keys.env`.
5. Batch mode continues past failures — check final `done:` line for real counts.

## Risks / things needing the owner
Needs GROQ_API_KEY and GOOGLE_AI_STUDIO_KEY configured locally (owner-held secrets). Platform login walls may block some videos — that's reported, not worked around. Cookie retry touches the owner's Chrome profile read-only. No other owner actions.

## Category / tags
media · video, transcription, digest, yt-dlp, gemini

## Revisions
Single source read: `C:\Users\a7med\.claude\skills\video-digest\SKILL.md` (61 lines). Slice lists claude/codex/gemini; claude revision preferred.
