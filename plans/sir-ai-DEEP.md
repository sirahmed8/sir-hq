# DEEP PLAN & MASTER SPEC: SIR AI
**Project**: SIR AI (`D:/Projects/SIR AI`)  
**Mission**: Sovereign Autonomous Personal AI ("Jarvis"), Multi-Agent CLI Orchestrator & Workstation Companion  
**Owner Mandate (2026-11-08)**: Jarvis for laptop: Telegram bot, iOS/Android apps, manage laptop and every CLI agent, subscriptions for users  
**Version**: 1.0.0 (Strictly enforced)  
**Standard**: `_SIR/standard/23-premium-code-bar.md` & `_SIR/plans/GEMINI_QUALITY_CHARTER.md`

---

## 1. Executive Summary & Product Purpose
SIR AI is Ahmed Alaa's personal sovereign intelligence system ("Jarvis"). It bridges voice, Telegram messaging, mobile applications, and local desktop automation into a unified AI interface. It acts as an autonomous executive orchestrator capable of monitoring laptop telemetry, delegating work across CLI agents (Antigravity, Claude Code, OpenCode, Kilo), serving as an offline speech assistant, and providing a privacy-preserving local AI gateway across all SIR products.

---

## 2. Legacy Forensic Audit & Porting Strategy

### 2.1 Existing Legacy Assets (`SIR AI/legacy/`)
1. **`SIR AI (v1)`**: Python FastAPI service with early LangChain/LlamaIndex experiments, vector storage prototypes, and basic agent loops.
2. **`SIR Tele Gateway` & `Desktop_SIR_Tele_Gateway`**: Telegram bot integration for executing remote system scripts, receiving status alerts, and bridging messages.
3. **`AgentsRoom`**: React/Electron workspace for viewing multi-agent CLI status, project backlogs, and message logs.
4. **`Odysseus app`**: Autonomous web research and scraping engine (read-only reference; Odysseus upstream).

### 2.2 What is Valuable to Port
- **Telegram Bot Ingress**: Robust long-polling / webhook architecture from `SIR Tele Gateway` for remote mobile command execution.
- **CLI Agent Process Supervision**: Process spawning, stdout/stderr capture, and IPC messaging from `AgentsRoom`.
- **Model Fallback Routing**: Multi-provider fallback chain (Local Ollama -> Gemini Flash -> DeepSeek) with strict privacy boundary routing.

### 2.3 What Must Be Discarded / Quarantined
- Deprecated LangChain v0.1 wrappers and bloated vector abstractions in `SIR AI (v1)`.
- Hardcoded plaintext bot tokens and leaked API keys.
- Odysseus web scraper binaries and non-sovereign dependencies.

---

## 3. Architecture & Design Identity

### 3.1 Technical Architecture
- **Core Server**: Python 3.12+ FastAPI & WebSocket daemon on port 8900.
- **Local Model Subsystem**: Direct interface to `D:\Projects\AI_Models_Hub` via Ollama (`qwen2.5-coder:7b`, `qwen3:8b`, faster-whisper, piper-tts).
- **Transport**: Loopback (`127.0.0.1`) and Tailscale P2P WireGuard (`Tailscale-User-Login: a7medorabe7@gmail.com`).
- **Client Shells**: Web/PWA, Capacitor Android/iOS shell, and Windows Desktop background companion.

### 3.2 Design Identity
- **Look**: Cybernetic Neural Obsidian. Voice-first, fluid, intelligent, and authoritative.
- **Palette**:
  - Primary Neural Violet: `#8B5CF6` (Violet 500) / `#7C3AED` (Violet 600)
  - Secondary Electric Cyan: `#06B6D4` (Cyan 500)
  - Dark Surface: Deep Obsidian (`#070A12` / `#0D111D`)
  - Elevated Glass: Translucent Slate (`rgba(17, 24, 39, 0.75)` with `backdrop-filter: blur(16px)`)
  - **Zero Yellow Buttons**: Enforced semantic palette.
- **Typography**: Precision typography (`Inter`, `Cairo`, `JetBrains Mono`).
- **Motion**: Dynamic Island spring transitions (`cubic-bezier(0.16, 1, 0.3, 1)`), morphing voice waveform visualizers, active-only tab labels.
- **Logo**: Vector SVG neural iris aperture with pulsing central core.

---

## 4. Dependencies, Cross-Project Links & Risks
- **Provides**: The unified AI Proxy and fallback routing engine to all other SIR products; system voice recognition to `SIR Laptop Manager` and `SIR Study`.
- **Consumes**: `AI_Models_Hub` model weights, `SIR Laptop Manager` process APIs.
- **Risks**: High GPU VRAM contention with 3D games; API rate limits during heavy fallback usage; socket timeouts during large context generation.

---

## 5. The First 25 Prioritized Tasks

### AI-101 | Core FastAPI Sovereign Daemon & Zero-Trust Ingress
- **Files**: `src/server.py`, `src/auth.py`
- **Steps**: Initialize FastAPI server on port 8900; enforce loopback and `Tailscale-User-Login: a7medorabe7@gmail.com` with RFC 9110 security headers.
- **Acceptance**: Server returns HTTP 200 over tailnet and 403 on untrusted origins.

### AI-102 | Telegram Executive Bot Gateway Integration
- **Files**: `src/bot/telegram_bot.py`, `scripts/start-bot.ps1`
- **Steps**: Re-architect Telegram bot from legacy gateway; implement warm Arabic/English command interface with zero emojis.
- **Acceptance**: Bot responds to `/status`, `/ask`, and `/run` commands in under 1 second.

### AI-103 | Local Ollama & AI_Models_Hub Direct Provider Bridge
- **Files**: `src/providers/local_ollama.py`, `src/providers/base.py`
- **Steps**: Build high-throughput client for `D:\Projects\AI_Models_Hub` models with automatic token streaming over WebSockets.
- **Acceptance**: Streams 25+ tokens/sec locally without cloud round-trip.

### AI-104 | Dynamic Island Morphing Voice Waveform Visualizer
- **Files**: `src/public/components/VoiceIsland.tsx`, `src/public/app.css`
- **Steps**: Connect Web Audio API microphone stream to Dynamic Island; render spring-animated waveform bars during speech.
- **Acceptance**: Dynamic Island expands smoothly from idle pill to audio visualizer on voice capture.

### AI-105 | On-Device Whisper Voice Transcription Pipeline
- **Files**: `src/voice/transcriber.py`
- **Steps**: Integrate faster-whisper model from `AI_Models_Hub`; expose WebSocket endpoint for real-time speech-to-text.
- **Acceptance**: Accurately transcribes Arabic and English voice input with latency <500ms.

### AI-106 | Piper-TTS Neural Voice Synthesis Engine
- **Files**: `src/voice/synthesizer.py`
- **Steps**: Connect offline piper-tts engine for high-fidelity Arabic and English vocal responses.
- **Acceptance**: Returns natural speech audio buffer within 400ms.

### AI-107 | Multi-Provider Fallback Routing & Privacy Gate
- **Files**: `src/router/fallback_router.py`
- **Steps**: Implement privacy router: private prompts locked to local models; public prompts fallback (Local -> Gemini -> DeepSeek).
- **Acceptance**: Automatically switches provider on rate-limit while strictly blocking private text from external APIs.

### AI-108 | CLI Agent Process Supervisor (Antigravity & Claude Code)
- **Files**: `src/supervisor/agent_manager.py`
- **Steps**: Track active CLI agent processes; parse stdout/stderr; expose kill/pause/resume controls via API and Telegram.
- **Acceptance**: `/agents` command lists active agents with CPU/memory and last output line.

### AI-109 | Game Mode Agent Throttling Coordinator
- **Files**: `src/supervisor/game_guard.py`
- **Steps**: Listen to `SIR Laptop Manager` Game Mode events; pause non-essential background agent tasks during gaming.
- **Acceptance**: AI workers suspend automatically within 2 seconds of game launch.

### AI-110 | SQLite Conversation Memory & Vector FTS5 Index
- **Files**: `src/memory/conversation_store.py`
- **Steps**: Store user chat history and session context in SQLite with FTS5 keyword indexing.
- **Acceptance**: Instant retrieval of historical discussions and code snippets in under 20ms.

### AI-111 | 30-Prompt Rigorous Quality Evaluation Suite
- **Files**: `tests/ai_eval/test_quality_benchmark.py`
- **Steps**: Author 30-prompt evaluation test (15 Arabic, 15 English) asserting zero loops, zero emojis, and accurate responses.
- **Acceptance**: Test suite passes with >=90% quality score.

### AI-112 | Mobile Capacitor Shell for iOS and Android
- **Files**: `mobile/capacitor.config.ts`, `mobile/android/`
- **Steps**: Scaffold Capacitor mobile wrapper connecting to port 8900 over Tailscale; configure background audio permissions.
- **Acceptance**: APK installs cleanly and streams Jarvis voice interactions on phone.

### AI-113 | Push Notification Interactive Voice Triggers
- **Files**: `src/notifications/fcm_dispatcher.py`
- **Steps**: Dispatch high-priority push notifications with actionable reply prompts to user's phone.
- **Acceptance**: Tapping push opens voice input composer directly.

### AI-114 | Autonomous Workspace Code Search & Refactoring Lab
- **Files**: `src/tools/code_search.py`
- **Steps**: AST-based code search across `D:\Projects`; provide semantic code snippet retrieval to agent prompts.
- **Acceptance**: Natural language query returns exact function definitions with file paths.

### AI-115 | Multi-User Subscription & Quota Enforcement Engine
- **Files**: `src/billing/quota_manager.py`
- **Steps**: Implement API key authentication, sliding-window rate limiting, and subscription tiers (Free, Pro, Unlimited).
- **Acceptance**: Enforces token caps and returns HTTP 429 when quota is exceeded.

### AI-116 | Dynamic Island Active-Only Tab Navigation
- **Files**: `src/public/index.html`, `src/public/app.css`
- **Steps**: Overhaul navigation with spring physics, active-tab labels only, and zero focus outline glitches.
- **Acceptance**: Inactive tabs show crisp SVG icons; active tab smoothly reveals text label.

### AI-117 | Autonomous Daily Schedule & Task Dispatcher
- **Files**: `src/routines/daily_planner.py`
- **Steps**: Aggregate calendar events, GitHub tasks, and study exams into morning audio briefing delivered to Telegram.
- **Acceptance**: Scheduled task delivers executive audio brief at 08:00 AM Cairo time.

### AI-118 | System Shell Safe Command Execution Sandbox
- **Files**: `src/tools/shell_sandbox.py`
- **Steps**: Execute Tier 0-1 read-only shell commands safely with timeouts, stdout capture, and command allow-listing.
- **Acceptance**: Blocks unauthorized destructive commands and logs execution results.

### AI-119 | GPU VRAM Memory Pressure Telemetry Watchdog
- **Files**: `src/telemetry/vram_watchdog.py`
- **Steps**: Sample Nvidia GPU memory usage; dynamically offload or quantize models if VRAM usage exceeds 90%.
- **Acceptance**: Prevents CUDA out-of-memory crashes by gracefully unloading inactive weights.

### AI-120 | Desktop Windows System Tray Companion
- **Files**: `src/tray/tray_app.py`, `scripts/run-tray.vbs`
- **Steps**: Build lightweight background system tray icon displaying AI status, active models, and quick voice activation hotkey.
- **Acceptance**: Global hotkey (Win+Shift+J) opens Jarvis voice overlay instantly.

### AI-121 | Arabic Dialect Linguistic Calibrator
- **Files**: `src/router/dialect_calibrator.py`
- **Steps**: Fine-tune prompt formatting to understand Egyptian Arabic dialect nuances and respond in clean, natural Arabic.
- **Acceptance**: Zero robotic or unnatural phrasing in Arabic conversational responses.

### AI-122 | Automated Token Budget Usage Ledger & Cost Tracker
- **Files**: `src/billing/cost_ledger.py`
- **Steps**: Track token consumption across local and fallback cloud providers; calculate virtual savings from running locally.
- **Acceptance**: Dashboard displays cumulative tokens served and dollar savings.

### AI-123 | Interactive Prompt Engineering & Playground Lab
- **Files**: `src/public/playground.html`
- **Steps**: In-browser prompt testing workbench with side-by-side temperature, top-p, and system instruction comparisons.
- **Acceptance**: Developers can test prompts across local and cloud models in real time.

### AI-124 | Silent Windows Logon Scheduled Task
- **Files**: `scripts/install-autostart.ps1`, `scripts/dev-start.vbs`
- **Steps**: Register `SIR_AI_Server` scheduled task running windowless via `pythonw.exe` on user login.
- **Acceptance**: Daemon starts silently on boot with zero console windows.

### AI-125 | End-to-End Automated Verification Suite
- **Files**: `scripts/verify.ps1`, `tests/test_master_plan_ai.py`
- **Steps**: Author comprehensive integration test validating daemon ingress, bot commands, voice pipeline, and security gates.
- **Acceptance**: `verify.ps1` runs in under 3 seconds with 100% green gates.
