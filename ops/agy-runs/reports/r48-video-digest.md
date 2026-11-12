# r48-video-digest — report (2026-11-12)

## What was built

A working pipeline that turns any short video (TikTok, Instagram Reel, YouTube Short,
YouTube video, or a local file) into a Markdown digest for any SIR agent.

- `D:/Projects/_SIR/scripts/video_digest.py` — single-source digest.
  yt-dlp download (plain first, `--cookies-from-browser chrome` only as automatic
  retry, cookies never printed) -> ffmpeg 16 kHz mono audio + 6 evenly spaced JPEG
  frames -> Groq `whisper-large-v3-turbo` transcription (`verbose_json`, gives
  language) -> local faster-whisper `base` fallback via
  `C:\Users\a7med\AppData\Local\Python\bin\python.exe` -> Gemini vision scene notes
  + one text call for summary/5 takeaways/product ideas ->
  `_local/videos/<id>/digest.md`. `_local/` is gitignored (verified with
  `git check-ignore`). Stdlib only; keys read from `_local/api-keys.env`, never printed.
- `D:/Projects/_SIR/scripts/video_digest_batch.py` — `--urls file.txt` and/or
  `--dir folder`; sequential, skips items whose `digest.md` exists, continues past
  failures, prints real counts.
- `D:/Projects/_SIR/scripts/video_transcribe_local.py` — faster-whisper runner used
  by the fallback.
- `D:/Projects/_SIR/skills/video-digest/SKILL.md` — agent-facing usage doc; copied
  to `C:/Users/a7med/.claude/skills/video-digest/`,
  `C:/Users/a7med/.codex/skills/video-digest/`,
  `C:/Users/a7med/.gemini/skills/video-digest/` (Antigravity skills folder).
- `D:/Projects/_SIR/ops/research/video-tools-2026-11-12.md` — 10-option comparison
  (yt-dlp, agent-reach, ffmpeg, Groq, faster-whisper, legacy whisper, Gemini vision,
  instaloader/gallery-dl, TikTok-Api) + verified timings.

## What already existed (checked first)

- `agent-reach` 1.6.0 (CLI + skill): read-only; YouTube subtitle/transcribe and
  Instagram posts, no TikTok, text only, no frames. Kept as a cheap first try for
  captioned YouTube; the digest pipeline covers everything else.
- `youtube-video-research` skill in Claude/Codex: transcript/packaging research,
  not a general video-understanding tool.
- Legacy `whisper` in `D:/Projects/SIR AI/legacy/agentic-os-research/whisper`:
  source only, no env; faster-whisper 1.2.1 already installed on the AppData Python
  with `tiny`+`base` models cached — used instead.
- yt-dlp 2026.10.26 and ffmpeg 8.1.1 already on PATH; instaloader/gallery-dl not
  installed and not needed.

## Real verification output

- `python -m py_compile` on all three scripts: OK.
- Local 6 s mp4 (ffmpeg testsrc+sine): full run **28 s**, digest 2,731 bytes;
  Groq transcript + Gemini scene notes (correctly identified the test pattern),
  5 takeaways, 5 product ideas.
- `https://www.youtube.com/watch?v=jNQXAC9IVRw` (19 s): download+digest **3 m 33 s**;
  digest 2,680 bytes; transcript accurate ("Alright, so here we are, one of the
  elephants..."); 6 scene frames described; language field populated after the
  `verbose_json` fix. Gemini 3.6-flash returned 503 twice and the built-in retry
  recovered.
- Batch: `done: 2 digested, 0 failed, 2 total`; finished item skipped with
  `digest already exists`.

## Bugs found and fixed during testing

1. Groq returned HTTP 403 (Cloudflare 1010) to bare urllib — fixed with a browser
   User-Agent header.
2. Gemini `gemini-2.5-flash`/`gemini-2.5-flash-lite` return 404 "no longer available
   to new users" on this key; `gemini-3.8-flash` hangs >150 s. Working chain set to
   `gemini-3.6-flash,gemini-3.5-flash,gemini-flash-latest` (all verified ~2-3 s).
3. Local whisper treated an empty transcript (no speech) as failure — fixed; it now
   counts as a successful transcription with empty text.
4. `response_format=json` gave no language — switched to `verbose_json`.

## Git / CI

- HQ's commit `b5f79e7` swept the three scripts into main at 15:29 (content
  identical to what was tested). My follow-up commit `830dfd5` pushed the SKILL.md,
  research file, `verbose_json` fix and the bus line. `main` is pushed.
- CI: `ops/ci-quota-exhausted.flag` exists (Actions minutes exhausted until ~Dec 1);
  per preamble rule 18 verification was local: py_compile + two real end-to-end
  runs + batch run, all green. No CI loop attempted.

## Still open / notes

- TikTok and login-walled Instagram were not exercised (no sample links); yt-dlp
  supports both, cookies retry is automatic, failures degrade to a clear error.
- Gemini free-tier 503s happen under load; retries cover it, worst case the digest
  still ships transcript + "scene description unavailable".
- Very long videos (>30 min) may hit Groq's ~25 MB upload cap — audio auto-re-encodes
  to 32 kbps mp3 above 24 MB wav; extreme lengths may still need chunking (not built,
  YAGNI for shorts).
