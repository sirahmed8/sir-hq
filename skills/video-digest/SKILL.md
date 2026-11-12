---
name: video-digest
description: >
  Understand a short video the owner sends (TikTok, Instagram Reel, YouTube Short,
  or any link/local file yt-dlp supports) by producing a Markdown digest: transcript,
  scene notes from sampled frames, 5 key takeaways and product ideas. Use when the
  user pastes a video link or drops a video file and asks what it is about, wants it
  summarized, or wants ideas from it. Read-only analysis; never posts or downloads
  beyond the local _local/videos folder.
---

# Video Digest

Turns one video into `_local/videos/<id>/digest.md` (title, source, language,
full transcript, scene notes, 5 takeaways, ideas for SIR products).

## How to run

From `D:/Projects/_SIR` (Windows, Git Bash or PowerShell):

```bash
python scripts/video_digest.py "<URL-or-local-file>"
python scripts/video_digest.py "<URL>" --force        # re-digest an existing one
python scripts/video_digest.py "<URL>" --no-vision     # transcript only, no Gemini calls
python scripts/video_digest_batch.py --urls list.txt   # one URL per line
python scripts/video_digest_batch.py --dir "D:/path/to/mp4s"   # folder of videos
```

The last stdout line is the digest path. Finished videos are skipped on re-run
(`digest.md` already exists); use `--force` to redo.

## What happens inside (do not re-implement)

1. yt-dlp downloads the video (tries without cookies first; retries once with
   `--cookies-from-browser chrome` only if needed; cookies are never printed).
2. ffmpeg extracts 16 kHz mono audio and 6 evenly spaced JPEG frames.
3. Groq `whisper-large-v3-turbo` transcribes (`GROQ_API_KEY`); on failure it falls
   back to local faster-whisper (`base` model, needs
   `C:\Users\a7med\AppData\Local\Python\bin\python.exe`; override with
   `VIDEO_LOCAL_PYTHON` / `VIDEO_LOCAL_WHISPER_MODEL`).
4. Gemini (`GOOGLE_AI_STUDIO_KEY`, model chain `gemini-3.6-flash` then
   `gemini-3.5-flash`/`gemini-flash-latest`, retries 503/429) describes the
   frames and writes takeaways + product ideas.

Keys come from `_local/api-keys.env` (gitignored). Never print key values.
Override models via `VIDEO_GROQ_MODEL`, `VIDEO_GEMINI_MODELS`,
`VIDEO_LOCAL_WHISPER_MODEL`, `VIDEO_LOCAL_PYTHON`.

## Rules

- Output stays in `D:/Projects/_SIR/_local/videos/` which is gitignored. Never copy
  video files, transcripts, frames or digests into git or into other projects.
- If the owner sends private/personal videos, the digest is for him only; do not
  paste its content into shared reports, bus files or messages.
- If a platform blocks download (login wall, CAPTCHA), report the platform name and
  the error plainly; do not retry in a loop or try to bypass verification.
- TikTok and some Instagram posts may need the Chrome-cookie retry; that is
  automatic. If it still fails, try `agent-reach read <url>` for text/captions and
  say what could not be obtained.
- Batch mode processes items sequentially and continues past failures; check the
  final `done:` line for the real counts.
