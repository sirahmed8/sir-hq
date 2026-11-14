# 7-ahome-audit-models report (2026-11-14)

## Current chain (source: apps/local-core)
Chat (domain/ai_profiles.py): every effort (fast, balanced, deeper, code) uses `qwen3.5:9b`, ctx `CHAT_CONTEXT=16384` (changed from 65536 in the working tree by the previous round to keep a 100% GPU runner), keep_alive -1.
Background (data/background_models.py, CPU, num_gpu 0): `qwen3:4b` (classify/tag/summarize), `nemotron-3-nano:4b` (automation; now also section classification in data/conn_ai.py).
Embeddings (data/notes_search.py): `bge-m3` then `nomic-embed-text`, then word fallback.
Non-private escalation (data/free_cli_pool.py, opt-in, off by default): kilo, opencode, devin, aider/NVIDIA Nemotron Ultra, agy, cline, pi (two aider Groq/Cloudflare entries removed by previous round).
Voice: faster-whisper-base (CPU), Windows SAPI TTS (en-US only), Windows OCR.

## Live availability (ollama list / API, 2026-11-14 15:55)
Installed: nemotron-3-nano:4b, qwen3.5:9b, gemma4:e4b (unused), qwen3:4b, bge-m3, nomic-embed-text. Nothing missing from the chain.
`ollama ps`: qwen3.5:9b 5.6 GB 100% GPU ctx 16384; nemotron-3-nano:4b loaded.
"Say hello" through /api/chat: qwen3.5:9b OK (14 s, cold), nemotron-3-nano:4b OK (6 s), qwen3:4b OK in 8 s but answers with its own reasoning text (not usable for one-word tasks, confirms the conn_ai change). bge-m3 embeds 1024 dims, nomic-embed-text 768 dims.
LM Studio (:1234) is not running and is not referenced by the chain (not applicable).

## Issues
1. Doc/comment drift: checkpoint r80 and docs/LOCAL_MODELS.md say ctx 65536, code now says 16384; a comment in ai_profiles.py still mentions "65536-context" cold load. Needs a docs sync.
2. Hermes shares the runner only if its ctx equals 16384 (now true per live ps).
3. qwen3:4b classify role may return reasoning text; consider routing classify to nemotron-3-nano:4b too.
4. TTS has no Arabic voice (en-US only); gemma4:e4b (6.6 GB) unused.
5. Repo tree had uncommitted previous work (conn_ai on nemotron, ctx 16384, stream limits 40/90/35 s, single-instance Telegram mutex, game-mode process list); reviewed, tests pass, committed.

## Verification
`apps/local-core/.venv/Scripts/python.exe -m pytest tests -q` -> `1090 passed in 103.86s`.
CI: ops/ci-quota-exhausted.flag exists, so local verification replaces CI (rule 18).

## Recommendations
Sync docs/LOCAL_MODELS.md to 16384; move classify to nemotron-3-nano:4b; optionally remove gemma4:e4b; add Arabic TTS (piper) in a separate task. No installs done.
