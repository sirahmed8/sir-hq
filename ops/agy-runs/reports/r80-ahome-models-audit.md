# r80-ahome-models-audit Report

Date: 2026-11-14  
Repo: `D:/Projects/AHome`  
Hardware baseline: 24 GB system RAM, NVIDIA RTX 4050 Laptop (6 GB VRAM), `D:` 18.1 GB free, Ollama `OLLAMA_MODELS=D:\Projects\AI_Models_Hub\ollama`, `OLLAMA_CONTEXT_LENGTH=16384`, `OLLAMA_MAX_LOADED_MODELS=2`, `OLLAMA_NUM_PARALLEL=1`, `OLLAMA_FLASH_ATTENTION=1`, `OLLAMA_KV_CACHE_TYPE=q8_0`.

## 1. Installed Models Inventory (Verified Live)
`ollama list`:
- `qwen3.5:9b` (6.6 GB disk, Q4_K_M ~5.6 GB VRAM; `ollama show` capabilities: `completion`, `vision`, `tools`, `thinking`)
- `gemma4:e4b` (6.6 GB disk, Q4_K_M; `ollama show` capabilities: `completion`, `vision`, `audio`, `tools`, `thinking`; deliberately unused by default)
- `qwen3:4b` (2.5 GB disk)
- `nemotron-3-nano:4b` (2.8 GB disk)
- `bge-m3:latest` (1.2 GB disk)
- `nomic-embed-text:latest` (274 MB disk)

Non-Ollama local assets verified:
- Whisper STT: `D:/Projects/AI_Models_Hub/whisper/faster-whisper-base/model.bin` present (runs CPU `int8`).
- Windows SAPI TTS (`System.Speech`): only `Microsoft David Desktop|en-US|True` and `Microsoft Zira Desktop|en-US|True` installed (`has_arabic=false`).
- Windows WinRT OCR helper: `apps/local-core/data/ocr/windows_ocr.ps1` (`ar-SA` and `en-US`).

## 2. Feature-by-Feature Coverage & Gaps
1. **Primary Chat & Assistant Routing** (`data/smart_ai_router.py`, `domain/ai_profiles.py`, `domain/assistant_policy.py`, `data/ollama_stream.py`, `presentation/openai_router.py`, `presentation/assistant_router.py`):
   - Uses `qwen3.5:9b` with `CHAT_CONTEXT = 65536` (shared with Hermes so one runner stays hot), `keep_alive = -1`, profiles `fast` (`think=False`, 400 tokens, 120s), `balanced` (`medium`, 1500 tokens, 150s), `deeper`/`code` (`high`, 1500 tokens, 170s).
   - Covered completely by `qwen3.5:9b`.
   - Fixed 5 stale assertions in `tests/test_game_mode.py` and `tests/test_local_model_profiles.py` plus synced `docs/LOCAL_MODELS.md` to match commit `fbda5b3`.
2. **Telegram Gateway** (`infra-daemons/telegram_assistant.py`, `presentation/bot_router.py`, `presentation/telegram_router.py`):
   - Routes via n8n webhook (`:5678`) or `/v1/assistant/reply` (`qwen3.5:9b`, `HISTORY_TURNS=2`). Covered by `qwen3.5:9b`.
3. **Notes Semantic Search & Q&A** (`data/notes_search.py`, `domain/notes_ranking.py`, `data/notes_ask.py`):
   - Embeddings use `bge-m3` -> `nomic-embed-text` (`/api/embed`), Q&A uses hot `qwen3.5:9b` (`think="low"`, `temperature=0.2`). Covered; no pull needed.
4. **Background Classification / Tagging / Summary / Automation** (`data/background_models.py`, `data/conn_ai.py`):
   - `background_models.py` uses `qwen3:4b` and `nemotron-3-nano:4b` strictly on CPU (`num_gpu=0`, 4096 ctx, `keep_alive=30s`, `MIN_AVAILABLE_MB=2500`).
   - Flagged bug in `data/conn_ai.py`: `classify_with_ai` calls `/api/generate` with `qwen3.5:9b` without `num_ctx`, inheriting `OLLAMA_CONTEXT_LENGTH=16384` and risking hot-runner eviction/reload. Should pass `num_ctx: 65536` or route to CPU `qwen3:4b`.
5. **Voice STT & TTS** (`data/speech_service.py`, `data/tts_local.py`, `presentation/audio_router.py`):
   - STT: CPU `faster-whisper-base` (~145 MB RAM, 0 VRAM). Works locally; optional upgrade to `Systran/faster-whisper-small` (~250 MB int8 RAM, CPU, 0 VRAM) for better Egyptian Arabic accuracy.
   - TTS: Windows SAPI only. Gap confirmed live: no Arabic voice installed (`has_arabic=false`), so `/v1/audio/speech` returns `503 no_arabic_voice` on Arabic text. Fix without Ollama: install Windows Arabic Speech language pack (~100 MB) or add offline `piper-tts` Arabic (`ar_JO-kareem-medium`, ~63 MB RAM, CPU).
6. **Photo / Vision & Media Generation** (`presentation/chat_media_router.py`, `data/ocr_windows.py`, `presentation/media_router.py`):
   - Photo OCR (`/v1/chat/ocr`): Windows WinRT OCR extracts text at 0 VRAM, no scene/diagram/handwriting VQA yet. `qwen3.5:9b` already has `vision` capability in Ollama (`ollama show`), so multimodal image Q&A needs backend wiring rather than pulling another VLM.
   - Image/Video generation (`/v1/media/jobs`): intentionally gated `503` (ComfyUI absent); keeping `qwen3.5:9b` resident leaves <0.5 GB VRAM headroom, so heavy media gen must unload `qwen3.5:9b` via `vram_orchestrator`.
7. **Smart Home / Assistant Commands & Bounded Escalation** (`domain/assistant_policy.py`, `data/escalation.py`, `data/free_cli_pool.py`):
   - Assistant commands/reminders/Spotify are handled by deterministic routing + `qwen3.5:9b` (`tools` capability built-in). No MQTT/HomeAssistant bridge exists in `local-core` yet.
   - Non-private P0/P1 escalation is opt-in (`AHOME_ALLOW_CLOUD_ESCALATION=false` default); P2/P3 personal chats stay strictly local-only.

## 3. Concrete Model Pull / Cleanup Recommendations
- **Do NOT pull extra Ollama LLMs/VLMs**: `qwen3.5:9b` (chat/code/vision), `qwen3:4b` + `nemotron-3-nano:4b` (CPU background), `bge-m3` + `nomic-embed-text` (embeddings) cover all Ollama pipelines within 6 GB VRAM and 24 GB RAM.
- **Avoid bloat**: `gemma4:e4b` (6.6 GB) is unused; `infra-daemons/pull_models.ps1` still lists `qwen3:8b` (redundant with `qwen3.5:9b`).
- **Tiny non-Ollama fixes (0 VRAM)**: Windows Arabic Speech voice pack (~100 MB) or CPU `piper-tts` Arabic (~63 MB RAM); optional CPU `faster-whisper-small` int8 (~250 MB RAM) if Egyptian Arabic STT accuracy needs a boost.

## 4. Verification
- `apps/local-core`: `.\.venv\Scripts\python.exe -m pytest -q` -> `1090 passed in 99.71s`.
- `apps/web`: `npx tsc --noEmit` -> exit 0.
- Findings recorded in `D:/Projects/AHome/.sir/CHECKPOINT.md` (`.sir/` is excluded via `.git/info/exclude`) and `docs/LOCAL_MODELS.md` synced; `.gitignore`, fixed test files, and `docs/LOCAL_MODELS.md` committed and pushed to `main`.
