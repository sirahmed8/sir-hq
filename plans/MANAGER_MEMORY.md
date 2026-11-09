# MANAGER MEMORY: Sovereign Portfolio Digest
**Target**: SIR HQ Manager (Claude Sonnet 5.5 / Gemini Manager) & Autonomous Agents  
**Scope**: All 17 Projects across `D:\Projects` · Single-Truth Operating Reference  
**Length**: Compact Digest (Strictly under 400 lines) · Version: 1.0.0

---

## 1. Operating Rules for Every Manager Turn
1. **Never Ask Ahmed & Never Wait**: Decide, log in `_SIR/ops/MISSION_LOG.md`, maintain reversibility, and proceed. Only passkeys, 2FA, biometric checks, payments, and typing secrets into external forms go to `_SIR/ops/OWNER_ACTIONS.md`.
2. **HQ Never Writes Product Code**: HQ manages, reviews diffs, verifies on-screen proof, and publishes artifacts. Builders in Antigravity do all code implementation to conserve manager quota.
3. **No Pull Requests**: Ahmed owns every repository. Commit and push directly to `main` once `verify.ps1` is green.
4. **Strict Truth Rule**: All apps are being rebuilt from scratch. Never claim an app is "live" or "shipped" unless verified today with real output/commands. Old projects in `legacy\` are prototypes.
5. **Sacred Privacy**: AHome and Habiba data NEVER leave local systems. Local models only; zero cloud AI.
6. **Design Floor**: Dynamic Island spring motion, active-only tab labels, zero emojis, zero yellow buttons, 320px–4K computed layout, version 1.0.0 locked.
7. **Operator Execution**: Screen control uses Haiku low effort (`computer_batch`). Type pointer command (`Read D:/Projects/_SIR/ops/briefs/<name>.prompt.txt...`), queue continue line, avoid clipboard image clobber. Rotate accounts at <=15% quota remaining.

---

## 2. Project Memory & Next 5 Tasks (Per-Project Digest)

### 2.1 SIR Control Room (HQ) | `_SIR`
- **Status (Verified 2026-11-09)**: Central command console serving on port 8899 via `scripts/serve-control-room.py` with sub-ms ETag 304 caching. Single-source build generator (`plans/generate_dashboard.py`) produces byte-identical `ops/dashboard.html` and `ops/artifact/control-room.html`. Silent scheduled refresh (`SIR_ControlRoom_Refresh`) running headlessly via `wscript.exe`/`pythonw.exe` with zero console flashes. Gemini handover panel indexes 166 tasks across 17 projects.
- **Next 5 Tasks**: (1) `CR-101`: Universal subprocess window silencing in generator (`CREATE_NO_WINDOW = 0x08000000`). (2) `CR-102`: Consolidated Dynamic Island settings popover modal. (3) `CR-103`: Responsive off-canvas mobile drawer with mirrored RTL animation. (4) `CR-104`: Sticky mobile top anchor bar for critical sections. (5) `CR-105`: Bidirectional logical CSS property conversion.
- **Risks**: Artifact version desynchronization if manual edits bypass generator; transient console flashes if `CREATE_NO_WINDOW` flag is missing in CLI subprocesses.
- **Plan Links**: [Master Plan](file:///D:/Projects/_SIR/.sir/MASTER_PLAN.md) · [Working Method](file:///D:/Projects/_SIR/plans/WORKING_METHOD.md) · [Design Family](file:///D:/Projects/_SIR/plans/DESIGN_FAMILY.md)

### 2.2 AHome | `AHome`
- **Status (Verified 2026-11-09)**: Private dual-user sanctuary app for Ahmed and Habiba. Local core running on port 8090 with DPAPI AES-256-GCM vault; web client on port 3000. 12 pure Arabic Android notification channels verified on phone via dumpsys with distinct vibration waveforms. Safe visualViewport 100dvh flex column prevents mobile keyboard overlap. Habiba's private corner verified with prominent privacy notice and zero fake data. 30-prompt local AI benchmark passing with 0 loops and 0 emojis.
- **Next 5 Tasks**: (1) `AH-101`: On-device Whisper voice note transcription via local model on `AI_Models_Hub`. (2) `AH-102`: P2P local Wi-Fi mesh synchronization when off-tailnet. (3) `AH-103`: Automated shadow database restore verification drill. (4) `AH-104`: Bi-directional private CalDAV calendar bridge. (5) `AH-105`: Wear OS companion glance tile.
- **Risks**: Sacred privacy violation if personal notes or Habiba's data are ever exposed to external models or public git; mobile keyboard displacement across iOS WebKit updates.
- **Plan Links**: [Master Plan](file:///D:/Projects/AHome/.sir/MASTER_PLAN.md)

### 2.3 SIR Study | `SIR Study`
- **Status (Verified 2026-11-09)**: Offline-first academic companion for Ahmed's CS Year 2 curriculum at Obour Higher Institute. Serves headlessly on port 3300 via `scripts/serve.py` (`pythonw.exe`) with silent Windows logon task `SIR_Study_Server`. All 8 standalone HTML guides feature CSS-only `:target` tabs with `<noscript>` fallback and zero white outline focus flashes. PyMuPDF pipeline verified 8/8 PDFs (195 pgs) with 100% zero blank pages. Delivered updated OR guide to iPhone via `@PersonalAI_1Bot`.
- **Next 5 Tasks**: (1) `ST-101`: Consolidated timed multi-subject exam simulation engine. (2) `ST-102`: Persistent SuperMemo SM-2 spaced repetition flashcard scheduler. (3) `ST-103`: Interactive AVL tree balancing & BST rotation visualizer. (4) `ST-104`: Infix to postfix stack simulation lab. (5) `ST-105`: Interactive 2-to-4 variable Karnaugh Map (K-Map) solver in Electronics.
- **Risks**: Academic integrity violation if agents build automated quiz solvers (strictly prohibited by rule 14; learning and schedule support only); PDF frame-freeze during headless render.
- **Plan Links**: [Master Plan](file:///D:/Projects/SIR%20Study/.sir/MASTER_PLAN.md)

### 2.4 SIR Jobs | `SIR Jobs`
- **Status (Verified 2026-11-09)**: Career intelligence and cash generation engine running on port 3456 via Node.js ESM. Tailnet WireGuard access control verified (HTTP 200 via `Tailscale-User-Login`, 403 on foreign hosts, zero login dialogs). Scrapes 5 global feeds; filters US-only and >3yr seniority jobs. AI fit scorer verified >=95% precision against Ahmed's honest sophomore profile. Multi-tone proposal drafter active. 13,475 EGP target model and A4 CV PDF generator active. Zero emojis, zero yellow buttons.
- **Next 5 Tasks**: (1) `JB-101`: Background scraping poller daemon with jitter. (2) `JB-102`: Mostaql & regional Arabic freelance platform RSS scraper. (3) `JB-103`: High-fit (>=90%) instant Telegram cash alert. (4) `JB-104`: Interactive tailored interview Q&A flashcard generator. (5) `JB-105`: Freelance milestone invoicing & EGP payment tracker.
- **Risks**: IP rate-limiting from public job boards during scraping; ungrounded experience claims in staged proposals (must strictly maintain sophomore student truth).
- **Plan Links**: [Master Plan](file:///D:/Projects/SIR%20Jobs/.sir/MASTER_PLAN.md)

### 2.5 SIR Laptop Manager | `SIR Laptop Manager`
- **Status (Verified 2026-11-09)**: Workstation operations console and hardware guardian running on port 8765 via Python 3.14 OpsServer. Tailscale WireGuard access verified with RFC 9110 status codes and CSRF HMAC tokens. Real-time CPU, RAM, GPU (Nvidia SMI), battery wear, and disk telemetry live. Safe quarantine cleaner freed 3.72 GB on C: with verifiable SHA-256 rollback bucket. Desktop shortcut doctor audited 53 shortcuts and isolated stale entries. macOS Sonoma Pro look pack V2 verified. 147 unit tests green.
- **Next 5 Tasks**: (1) `LP-101`: Windows system tray companion (`pystray`) with 1-click Game Mode toggle. (2) `LP-102`: Thermal spike (>85°C) Telegram alert dispatcher. (3) `LP-103`: Windows Update agent-aware deferral policy. (4) `LP-104`: Orphaned AI model blob garbage collector for `AI_Models_Hub`. (5) `LP-105`: Interactive Game Mode per-game process relief profile customizer.
- **Risks**: Deleting unrecoverable system files during cleanup (mitigated by mandatory SHA-256 quarantine buckets); Windows Update triggering unannounced reboots during agent runs.
- **Plan Links**: [Master Plan](file:///D:/Projects/SIR%20Laptop%20Manager/.sir/MASTER_PLAN.md)

### 2.6 SIR AI | `SIR AI`
- **Status (M0 Ready, Plan Completed 2026-11-09)**: Sovereign personal intelligence system ("Jarvis") for Ahmed's laptop workstation and mobile companion. Integrates speech-to-text (Whisper), neural TTS (Piper), Telegram bot control, and local CLI agent supervision. Connects directly to `AI_Models_Hub` models via Ollama (`qwen2.5-coder:7b`, `qwen3:8b`). Deep plan and master plan established with 25 prioritized tasks.
- **Next 5 Tasks**: (1) `AI-101`: Core FastAPI sovereign daemon on port 8900 with Tailscale auth. (2) `AI-102`: Telegram executive bot gateway integration. (3) `AI-103`: Local Ollama & `AI_Models_Hub` streaming provider bridge. (4) `AI-104`: Dynamic Island morphing voice waveform visualizer. (5) `AI-105`: On-device Whisper voice transcription pipeline.
- **Risks**: GPU VRAM contention with 3D games (mitigated by Game Mode pause coordinator); API quota exhaustion on external fallback models.
- **Plan Links**: [Deep Plan](file:///D:/Projects/_SIR/plans/sir-ai-DEEP.md) · [Master Plan](file:///D:/Projects/SIR%20AI/.sir/MASTER_PLAN.md)

### 2.7 SIR Negm Furniture | `SIR Negm Furniture`
- **Status (FROZEN BY OWNER ORDER 2026-11-09)**: Ahmed's friend's commercial furniture brand. Strictly **PLAN ONLY**. No SIR agent writes code, configures CI, or deploys instances. Turn-key Handoff Pack blueprint authored in `_SIR/plans/sir-negm-furniture-DEEP.md` containing complete specifications for the friend's own AI agent.
- **Next 5 Tasks**: (1) `NF-101`: Author master `HANDOFF.md` and friend's agent kickoff prompt. (2) `NF-102`: Extract normalized product catalog JSON schema. (3) `NF-103`: Document 3D Draco GLTF asset compression under 2MB. (4) `NF-104`: Document 2D/3D floor plan canvas coordinate math. (5) `NF-105`: Design formatted WhatsApp checkout payload generator.
- **Risks**: Violation of workspace law if agents accidentally touch product code or provision cloud resources (strictly prohibited).
- **Plan Links**: [Deep Plan](file:///D:/Projects/_SIR/plans/sir-negm-furniture-DEEP.md) · [Master Plan](file:///D:/Projects/SIR%20Negm%20Furniture/.sir/MASTER_PLAN.md)

### 2.8 SIR Obour Hub | `SIR Obour Hub`
- **Status (M0 Ready, Plan Completed 2026-11-09)**: Sovereign academic portal and timetable hub for Obour Higher Institutes (CS, Engineering, Business). Rebuilding from `legacy/Obour Academic Hub` with all non-compliant quiz automation permanently quarantined. Edge serverless architecture with Cloudflare D1 / Turso SQLite database.
- **Next 5 Tasks**: (1) `OH-101`: Academic timetable D1 schema & CS Year 2 seed data. (2) `OH-102`: Interactive semester schedule calendar with active lecture pulse. (3) `OH-103`: Egyptian 4.0 credit-hour GPA simulator. (4) `OH-104`: Lecture hall & campus building interactive locator (Hall 533). (5) `OH-105`: Official professor office hours & academic contact directory.
- **Risks**: Academic policy compliance (strictly learning support only; zero quiz auto-solving); sudden timetable revisions by institute administration.
- **Plan Links**: [Deep Plan](file:///D:/Projects/_SIR/plans/sir-obour-hub-DEEP.md) · [Master Plan](file:///D:/Projects/SIR%20Obour%20Hub/.sir/MASTER_PLAN.md)

### 2.9 SIR Hagoozat | `SIR Hagoozat`
- **Status (M0 Ready, Plan Completed 2026-11-09)**: Football pitch reservation and tournament platform consolidating `Hagoozat Elite`, `11Players`, and `EGFootball5`. Edge serverless with PostgreSQL/D1 ACID row-level locking to eliminate double-booking race conditions during peak hours. Wave 0 security PR patched legacy unsigned webhook vulnerabilities.
- **Next 5 Tasks**: (1) `HZ-101`: Unified PostgreSQL pitch and reservation schema. (2) `HZ-102`: Atomic slot reservation state machine with 5-minute checkout hold. (3) `HZ-103`: Interactive Cairo/Giza pitch map and filter. (4) `HZ-104`: Dynamic Island active-only tab bar. (5) `HZ-105`: "Missing Player" 5v5 squad matchmaking lobby.
- **Risks**: Concurrent slot contention on prime Thursday/Friday evening slots; pitch managers manually double-booking walk-in clients.
- **Plan Links**: [Deep Plan](file:///D:/Projects/_SIR/plans/sir-hagoozat-DEEP.md) · [Master Plan](file:///D:/Projects/SIR%20Hagoozat/.sir/MASTER_PLAN.md)

### 2.10 SIR Business | `SIR Business`
- **Status (M0 Ready, Plan Completed 2026-11-09)**: Multi-vertical retail POS and inventory OS consolidating `SIR Market`, `SIR Restaurant`, `SIR Pharmacy`, and `SIR Library`. 100% offline-first architecture with local SQLite storage, sub-50ms barcode checkout, raw ESC/POS binary thermal printing, and pharmacy active ingredient generic drug substitution.
- **Next 5 Tasks**: (1) `BZ-101`: Unified multi-vertical SQLite schema with JSON extensions. (2) `BZ-102`: Sub-50ms offline barcode checkout engine. (3) `BZ-103`: Raw ESC/POS thermal receipt binary generator. (4) `BZ-104`: Dynamic Island active-only tab bar. (5) `BZ-105`: Pharmacy generic drug chemical substitution engine.
- **Risks**: Network dropouts during busy checkout shifts (mitigated by offline-first SQLite transaction queues); thermal printer ESC/POS driver variations.
- **Plan Links**: [Deep Plan](file:///D:/Projects/_SIR/plans/sir-business-DEEP.md) · [Master Plan](file:///D:/Projects/SIR%20Business/.sir/MASTER_PLAN.md)

### 2.11 SIR Content Creation Studio | `SIR Content Creation Studio`
- **Status (M0 Ready, Plan Completed 2026-11-09)**: Autonomous video generation and social syndication engine powering ByteVibeHQ (TikTok, Reels, Shorts, Reddit, Facebook, X). Local hardware-accelerated FFmpeg rendering using Nvidia NVENC (`h264_nvenc`) with auto-fallback. Neural voiceover via `AI_Models_Hub` with word-level kinetic subtitle highlighting. Compliant with Tier 3 rules (official APIs only; zero scraping of X).
- **Next 5 Tasks**: (1) `CS-101`: Hardware-accelerated FFmpeg 9:16 vertical render engine. (2) `CS-102`: Kinetic typography subtitle generator with word-level highlights. (3) `CS-103`: Background audio normalization & voice ducking engine (-14 LUFS). (4) `CS-104`: Dynamic Island active-only tab bar. (5) `CS-105`: Interactive in-browser canvas timeline scrubber.
- **Risks**: Social media account shadow-bans from excessive posting (mitigated by mandatory Telegram 1-tap review before publishing); NVENC GPU load during gaming.
- **Plan Links**: [Deep Plan](file:///D:/Projects/_SIR/plans/sir-content-creation-studio-DEEP.md) · [Master Plan](file:///D:/Projects/SIR%20Content%20Creation%20Studio/.sir/MASTER_PLAN.md)

### 2.12 SIR Controller | `SIR Controller`
- **Status (M0 Ready, Plan Completed 2026-11-09)**: Game controller remapper and PC gaming optimizer unifying `SIR Controller (v1)` and `SIR Optimizer`. Modernized user-space ViGEmBus virtual Xbox 360 controller driver (zero anti-cheat risk). Safe Win32 `timeBeginPeriod(1)` driver maintaining 0.5ms timer resolution. Interactive 3D controller visualizer in Three.js.
- **Next 5 Tasks**: (1) `CT-101`: Clean ViGEmBus virtual Xbox 360 controller driver bridge. (2) `CT-102`: Interactive 3D real-time controller diagnostic visualizer. (3) `CT-103`: Sub-millisecond Windows 0.5ms timer resolution engine. (4) `CT-104`: Dynamic Island active-only tab bar. (5) `CT-105`: Precision radial deadzone & anti-deadzone calibrator.
- **Risks**: Anti-cheat false positives if virtual driver touches game memory (mitigated by 100% clean user-space virtual gamepad architecture); Bluetooth wireless packet drops.
- **Plan Links**: [Deep Plan](file:///D:/Projects/_SIR/plans/sir-controller-DEEP.md) · [Master Plan](file:///D:/Projects/SIR%20Controller/.sir/MASTER_PLAN.md)

### 2.13 SIR ModPack | `SIR ModPack`
- **Status (M0 Ready, Plan Completed 2026-11-09)**: Curated performance Minecraft modpack and sovereign launcher. Tauri / Rust desktop shell with official Microsoft Xbox Live OAuth2 device flow (tokens in Windows Credential Manager). Conflict-free Fabric mod matrix (Sodium, Lithium, Iris) with automated ZGenerational ZGC heap tuning for stable 120+ FPS on laptop GPUs.
- **Next 5 Tasks**: (1) `MP-101`: Tauri desktop launcher shell with Microsoft OAuth2. (2) `MP-102`: Conflict-free Fabric optimization mod matrix. (3) `MP-103`: Sub-8ms JVM ZGC memory tuning & argument compiler. (4) `MP-104`: Dynamic Island active-only tab bar. (5) `MP-105`: Fast delta auto-updater with SHA-1 manifest hash verification.
- **Risks**: Upstream Fabric/Minecraft updates breaking mod mixins; allocating >75% of physical RAM causing Windows paging file thrashing.
- **Plan Links**: [Deep Plan](file:///D:/Projects/_SIR/plans/sir-modpack-DEEP.md) · [Master Plan](file:///D:/Projects/SIR%20ModPack/.sir/MASTER_PLAN.md)

### 2.14 SIR Mods for GTA V | `SIR Mods for GTA V`
- **Status (M0 Ready, Plan Completed 2026-11-09)**: Mod manager, vehicle physics overhaul, and graphics preset suite for Grand Theft Auto V single-player. Non-destructive isolated `mods\` folder architecture preserving original RPF archives. Hard air-gap safety interlock (`dinput8.dll` disabler) permanently preventing players from entering GTA Online with active mods.
- **Next 5 Tasks**: (1) `GT-101`: GTA Online safety air-gap interlock (`dinput8.dll` disabler). (2) `GT-102`: Non-destructive isolated `mods\` folder engine. (3) `GT-103`: Interactive 3D vehicle handling (`handling.meta`) tuner lab. (4) `GT-104`: Dynamic Island active-only tab bar. (5) `GT-105`: Fast 1-click OpenIV `.oiv` package installer.
- **Risks**: Rockstar executable updates invalidating ScriptHookV offsets; archive corruption if edits occur outside `mods\` folder.
- **Plan Links**: [Deep Plan](file:///D:/Projects/_SIR/plans/sir-mods-for-gta-v-DEEP.md) · [Master Plan](file:///D:/Projects/SIR%20Mods%20for%20GTA%20V/.sir/MASTER_PLAN.md)

### 2.15 SIR Odysseus | `old projects/`
- **Status (RETIRED & ARCHIVED 2026-11-01)**: Upstream autonomous browser research tool permanently retired by owner order. Code preserved as read-only reference in `D:\Projects\old projects\SIR Odysseus (removed 2026-11-01)` and `D:\Projects\SIR AI\legacy\Odysseus app`. GitHub repo archived. DOM extraction heuristics harvested into `SIR AI`.
- **Next Tasks**: None. Zero active services, zero open ports. Maintain read-only archival preservation.
- **Plan Links**: [Retirement Spec](file:///D:/Projects/_SIR/plans/sir-odysseus-DEEP.md)

### 2.16 SIR Life | `SIR Life`
- **Status (M0 Ready, Plan Completed 2026-11-09)**: Personal lifestyle operating system, habit tracker, and spiritual sentinel for Ahmed. Strictly personal (completely distinct from AHome; zero couple data). Offline-first astronomical prayer calculator for Cairo (Egyptian General Survey method) with gentle acoustic chimes. Compassionate habit streak engine with rest-day protection.
- **Next 5 Tasks**: (1) `LF-101`: Offline Cairo astronomical prayer calculation engine. (2) `LF-102`: Dynamic Island next-prayer countdown & Adhan chime pill. (3) `LF-103`: Compassionate habit tracker with rest-day freeze. (4) `LF-104`: Dynamic Island active-only tab bar. (5) `LF-105`: 2-minute morning focus & evening gratitude journal.
- **Risks**: Habit tracker anxiety if streak penalties are punitive; prayer calculation drift if solar angles lack Cairo survey correction.
- **Plan Links**: [Deep Plan](file:///D:/Projects/_SIR/plans/sir-life-DEEP.md) · [Master Plan](file:///D:/Projects/SIR%20Life/.sir/MASTER_PLAN.md)

### 2.17 SIR Platform | `SIR Platform`
- **Status (Wave 7 Shared Kit, Plan Completed 2026-11-09)**: The architectural keystone extracted last from verified implementations across all products. Monorepo hosting 7 packages: `@sir/owner-auth`, `@sir/signed-webhook`, `@sir/ai-proxy`, `@sir/tokens-and-ui`, `@sir/i18n`, `@sir/legal-pack`, and `sir-kit` CLI. Built once products prove their patterns in production.
- **Next 5 Tasks**: (1) `PL-101`: Package `@sir/owner-auth` Tailnet WireGuard & loopback library. (2) `PL-102`: Package `@sir/signed-webhook` timing-safe HMAC verifier. (3) `PL-103`: Package `@sir/ai-proxy` privacy-preserving router. (4) `PL-104`: Package `@sir/tokens-and-ui` Dynamic Island spring engine. (5) `PL-105`: Package `@sir/i18n` bilingual Cairo/Inter dictionary resolver.
- **Risks**: Premature abstraction locking project chats into rigid patterns; circular package dependencies.
- **Plan Links**: [Deep Plan](file:///D:/Projects/_SIR/plans/sir-platform-DEEP.md) · [Master Plan](file:///D:/Projects/SIR%20Platform/.sir/MASTER_PLAN.md) · [Portfolio Links](file:///D:/Projects/_SIR/plans/PORTFOLIO_LINKS.md)

### 2.18 SIR Portfolio | `SIR Portfolio`
- **Status (Wave 7 Public Wall, Plan Completed 2026-11-09)**: Ahmed Alaa's public developer showcase and sovereign product wall. Strictly adheres to the Truth Rule: reads physical verification states directly from `_SIR/ops/` and `_SIR/plans/` with zero inflated claims. Static export for Cloudflare Pages with live GitHub commit tickers and verified A4 CV download bridge.
- **Next 5 Tasks**: (1) `PF-101`: Single-source portfolio data pipeline from `_SIR`. (2) `PF-102`: Interactive live project terminal and showcase cards. (3) `PF-103`: Dynamic Island active-only navigation bar. (4) `PF-104`: Downloadable agency-grade A4 CV bridge (`SIR Jobs`). (5) `PF-105`: Interactive real-time GitHub commit activity stream.
- **Risks**: Stale project statuses displayed if static build does not recompile upon product releases.
- **Plan Links**: [Deep Plan](file:///D:/Projects/_SIR/plans/sir-portfolio-DEEP.md) · [Master Plan](file:///D:/Projects/SIR%20Portfolio/.sir/MASTER_PLAN.md)

---

## 3. Command & Script Fast Reference
- **Local AI Worker**: `powershell -File D:\Projects\_SIR\scripts\ai\ask.ps1 -Prompt "<text>" -LocalOnly`
- **Send Telegram Brief**: `node D:\Projects\_SIR\scripts\deliver\send-owner-brief.mjs "Brief message"`
- **Refresh Dashboard**: `python D:\Projects\_SIR\plans\generate_dashboard.py`
- **Hidden Refresh Runner**: `wscript.exe //B //Nologo D:\Projects\_SIR\scripts\run-refresh-hidden.vbs`
- **Signal Done**: `python D:\Projects\_SIR\scripts\agy-done.py <task-name> <ok|fail|blocked> "<result>"`
