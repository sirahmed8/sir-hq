# DEEP PLAN & MASTER SPEC: SIR ModPack
**Project**: SIR ModPack (`D:/Projects/SIR ModPack`)  
**Mission**: Sovereign Performance Minecraft Modpack, Custom Launcher & 120 FPS Laptop Optimization Suite  
**Security Invariant**: Strictly zero plaintext account credentials in git; Microsoft OAuth2 token authentication only  
**Version**: 1.0.0 (Strictly enforced)  
**Standard**: `_SIR/standard/23-premium-code-bar.md` & `_SIR/plans/GEMINI_QUALITY_CHARTER.md`

---

## 1. Executive Summary & Product Purpose
SIR ModPack is a curated, high-performance Minecraft modding suite and sovereign launcher engineered specifically for laptop hardware. It combines a Conflict-Free Fabric Optimization Matrix (Sodium, Lithium, FerriteCore, Iris Shaders, Entity Culling) with fine-tuned JVM garbage collection flags (ZGC / Shenandoah), delivering a rock-solid 120+ FPS experience with sub-8ms frame times on mid-range discrete GPUs. It features an integrated auto-updater, shader preset manager, and native game controller remapping.

---

## 2. Legacy Forensic Audit & Porting Analysis

### 2.1 Existing Legacy Assets (`SIR ModPack/legacy/`)
- **`SIR ModPack (v1)`**: Historical launcher scripts, Fabric mod directories, shader presets, and JVM tuning configurations.
- **Security Incident Note**: Account files (`accounts.json`, `ias_accounts.json`) were permanently scrubbed from git history via `git-filter-repo` in Phase 0; account files are now strictly excluded via `.gitignore`.

### 2.2 What is Valuable to Port
- **Curated Fabric Mod Compatibility List**: Extensively tested mod roster guaranteeing zero mixin crashes and zero chunk rendering stalls.
- **Low-Overhead JVM Flags**: Tested arguments (`-XX:+UseZGC`, `-XX:+ZGenerational`, memory paging tweaks) eliminating micro-stutters.
- **Curated Shader Profiles**: Balanced Iris shader configuration (Complementary Reimagined tuned for GTX/RTX laptop mobile chips).

### 2.3 What Must Be Discarded
- Legacy insecure accounts file formats and plaintext session caches.
- Bloated 1GB+ redundant Minecraft runtime binaries (rely on official Mojang launcher runtime or clean Microsoft OAuth downloads).

---

## 3. Architecture & Design Identity

### 3.1 Technical Architecture
- **Launcher Client**: Tauri / Rust lightweight desktop shell with native Windows APIs and zero Electron RAM bloat.
- **Authentication**: Official Microsoft Xbox Live / Mojang OAuth2 device code flow; tokens stored in encrypted Windows Credential Manager.
- **Asset Ingestion & Hash Verifier**: Multi-threaded downloader verifying SHA-1 hashes of game assets and mod JARs against remote manifest.
- **Controller Bridge**: Pre-integrated controller mod (`MidnightControls` / `Controllable`) mapped to `SIR Controller` virtual gamepad profile.

### 3.2 Design Identity
- **Brand Aesthetic**: Emerald Pixel Vanguard & Obsidian Bedrock. Tactile, atmospheric, high-framerate, and immersive.
- **Palette**:
  - Primary Emerald Matrix: `#10B981` (Emerald 500) / `#059669` (Emerald 600)
  - Secondary Bedrock Obsidian: `#0B0F14` / `#111822`
  - Accent Redstone Ruby: `#EF4444` (Red 500)
  - Surface Glass: Translucent Emerald Slate (`rgba(17, 24, 34, 0.75)` with `backdrop-filter: blur(14px)`)
  - **Zero Yellow Buttons**: Clean emerald, ruby, and slate semantic tokens.
- **Typography**: Precision gaming typography (`Inter`, `Cairo`, `Minecraftia` / pixel accents for titles).
- **Motion**: Dynamic Island spring transitions (`cubic-bezier(0.16, 1, 0.3, 1)`), live FPS gauge animation, active-only tab labels.
- **Emblem**: Vector SVG faceted emerald crystal cube with pulsing runic apex core.

---

## 4. Dependencies, Cross-Project Links & Risks
- **Provides**: Gaming performance and controller testing bed to `SIR Controller`.
- **Consumes**: Game Mode process suspension from `SIR Laptop Manager`; controller driver from `SIR Controller`.
- **Risks**: Mojang authentication API changes; upstream Fabric API breaking changes on minor game updates.

---

## 5. The First 25 Prioritized Tasks

### MP-101 | Tauri Desktop Launcher Shell with Microsoft OAuth2 Device Flow
- **Files**: `src-tauri/src/main.rs`, `src-tauri/src/auth.rs`
- **Steps**: Implement official Microsoft Xbox Live OAuth2 device flow; store refresh tokens in Windows Credential Manager.
- **Acceptance**: User signs in via official `microsoft.com/link` code; profile skin and Gamertag render in launcher.

### MP-102 | Conflict-Free Fabric Optimization Mod Matrix (1.20.4+ / 1.21)
- **Files**: `manifest/modlist.json`, `scripts/validate_mods.py`
- **Steps**: Curate compatible Fabric mod matrix: Sodium, Lithium, FerriteCore, MemoryLeakFix, ImmediatelyFast, EntityCulling, Iris.
- **Acceptance**: Game launches cleanly with 0 mixin conflicts and 0 crash logs in under 10 seconds.

### MP-103 | Sub-8ms JVM ZGC Memory Tuning & Argument Compiler
- **Files**: `src/lib/jvmArguments.ts`, `src/lib/memoryProfiler.ts`
- **Steps**: Auto-detect physical system RAM; generate optimal JVM heap flags (`-Xms`, `-Xmx`, `-XX:+UseZGC`, `-XX:+ZGenerational`).
- **Acceptance**: Game runs with 120+ FPS and 0 garbage collection freeze frames during rapid elytra flight.

### MP-104 | Dynamic Island Active-Only Tab Navigation
- **Files**: `src/components/nav/TabBar.tsx`, `src/app/globals.css`
- **Steps**: Unified navigation bar (Play, Mods, Shaders, Performance, Settings) displaying text label only on active tab.
- **Acceptance**: Inactive tabs collapse to monochrome SVG icons; active tab smoothly reveals text label.

### MP-105 | Fast Delta Auto-Updater & SHA-1 Manifest Hash Verifier
- **Files**: `src/updater/manifest_verifier.py`, `src-tauri/src/downloader.rs`
- **Steps**: Compare local mod files against remote manifest; download only modified or missing JARs with parallel HTTP chunking.
- **Acceptance**: Updates modpack delta (e.g. 3 new mods) in under 4 seconds with 100% hash verification.

### MP-106 | Balanced Iris Shader Preset (Complementary Reimagined)
- **Files**: `presets/shaders/complementary_reimagined_laptop.txt`
- **Steps**: Tune shader settings: optimized shadow distance (8 chunks), real-time godrays, dynamic water reflections, FXAA.
- **Acceptance**: Maintains 90+ FPS at 1080p on laptop RTX GPU with stunning cinematic lighting.

### MP-107 | Integrated Gamepad Remapping & Hotkey Accelerator
- **Files**: `config/midnightcontrols.json`, `src/lib/controllerBridge.ts`
- **Steps**: Pre-configure controller bindings matching `SIR Controller` virtual Xbox 360 profile; add quick-loot and inventory triggers.
- **Acceptance**: Gamepad navigates inventory and controls character movement flawlessly without mouse touch.

### MP-108 | One-Click World Backup & Automated Snapshot Retention
- **Files**: `src/backup/world_backup.py`, `src/components/worlds/WorldCard.tsx`
- **Steps**: Automated ZIP snapshot of single-player saves before game launch; maintain 7-day rolling retention with 1-click restore.
- **Acceptance**: Tapping "Restore Backup" reverts corrupted world save in under 2 seconds.

### MP-109 | Bespoke Vector SVG ModPack Brand Assets
- **Files**: `public/logo.svg`, `public/favicon.svg`
- **Steps**: Design faceted emerald crystal cube with runic core; render multi-size favicons, desktop folder icon, and taskbar icons.
- **Acceptance**: Crisp vector rendering across desktop launcher and Windows shortcut.

### MP-110 | Dynamic RAM Allocation Auto-Sizer Lab
- **Files**: `src/components/settings/RamSlider.tsx`
- **Steps**: Interactive slider querying free system RAM; dynamically recommends safe allocation (e.g. 6GB on 16GB PC, leaving 10GB for OS).
- **Acceptance**: Slider warns in amber if user allocates >75% of physical memory to prevent paging lockups.

### MP-111 | Resource Pack High-Resolution Texture Manager
- **Files**: `src/components/resourcepacks/PackManager.tsx`
- **Steps**: Ingest and reorder faithful high-resolution texture packs (32x / 64x) with drag-and-drop priority sorting.
- **Acceptance**: Changing texture priority updates `options.txt` pack order immediately.

### MP-112 | In-Game Performance Telemetry & Frame Time Overlay
- **Files**: `config/spark.json`, `src/components/performance/FpsBenchmark.tsx`
- **Steps**: Integrate Spark performance profiler; render clean, non-obtrusive 99th percentile frametime graph.
- **Acceptance**: F3 screen or custom overlay displays clean 120 FPS graph with zero screen clutter.

### MP-113 | Offline Mode Single-Player Game Launcher
- **Files**: `src-tauri/src/offline_launcher.rs`
- **Steps**: Allow booting single-player worlds without internet connectivity using cached Mojang assets and verified offline profile.
- **Acceptance**: Disconnecting Wi-Fi allows launching game and playing local single-player worlds instantly.

### MP-114 | Chunk Loading Distance & Entity Distance Auto-Scaler
- **Files**: `src/lib/renderScaler.ts`
- **Steps**: Dynamically calibrate render distance (12 chunks) and simulation distance (8 chunks) based on detected battery state (AC vs Battery).
- **Acceptance**: Unplugging laptop AC power automatically drops render distance to 8 chunks to preserve battery.

### MP-115 | Multi-Instance Isolated Installation Manager
- **Files**: `src/instances/instance_manager.py`
- **Steps**: Support separate isolated mod instances (e.g., Performance Vanilla, Creative Lab, Tech Modpack) with distinct config folders.
- **Acceptance**: Launching different instances uses isolated `.minecraft` subdirectories without config pollution.

### MP-116 | Clean Crash Log Forensics & Mixin Dissector
- **Files**: `src/diagnostics/crash_parser.py`, `src/components/diagnostics/CrashModal.tsx`
- **Steps**: Automatically intercept JVM crashes; parse `hs_err_pid` and `crash-reports`; identify exact offending mod name in plain English.
- **Acceptance**: Displays human-readable error modal ("Crash caused by conflicting mod X; disable to resume").

### MP-117 | Crosshair & HUD Minimalist Cleaner Suite
- **Files**: `config/hud_cleaner.json`
- **Steps**: Minimalist HUD configuration removing visual clutter, adding subtle health indicators, and modern sleek crosshair.
- **Acceptance**: HUD presents clean executive aesthetic matching SIR design standards.

### MP-118 | Server Ping & Regional Low-Latency Ping Explorer
- **Files**: `src/components/servers/ServerList.tsx`
- **Steps**: Ping favorite multiplayer servers (Cairo, European, Middle East nodes); display live latency ms with packet loss indicator.
- **Acceptance**: Server cards display real-time ping gauge updating every 10 seconds.

### MP-119 | Multi-Screen Responsive Launcher Verification (320px to 4K)
- **Files**: `tests/responsive_modpack.test.mjs`
- **Steps**: Playwright tests verifying launcher tabs, mod lists, and world cards across 320px to 4K desktop viewports.
- **Acceptance**: Zero horizontal overflow and zero button clipping across all test viewports.

### MP-120 | Background Memory De-allocation on Game Exit
- **Files**: `src-tauri/src/game_watcher.rs`
- **Steps**: Monitor `javaw.exe` lifecycle; cleanly purge launcher memory caches upon game exit and trigger garbage collection.
- **Acceptance**: Closing Minecraft returns system RAM usage to baseline within 3 seconds.

### MP-121 | Custom Soundpack & Ambient Sound Enhancer
- **Files**: `config/sound_enhancer.json`
- **Steps**: Integrate ambient sound physics mod (Presence Footsteps, Sound Physics Remastered) for realistic cave reverb.
- **Acceptance**: Footsteps and environmental audio render spatial acoustic reverb without audio clipping.

### MP-122 | Dark Obsidian & Daylight Emerald Theme Engine
- **Files**: `src/hooks/useModpackTheme.ts`
- **Steps**: Flawless zero-flash theme engine; deep bedrock obsidian theme tuned for gaming environments.
- **Acceptance**: Switching theme updates all CSS custom properties instantly with zero white flash.

### MP-123 | Clean Mod Removal & Config Quarantine Janitor
- **Files**: `src/care/mod_janitor.py`
- **Steps**: When a mod is removed, safely isolate its orphaned configuration files to a quarantine folder with 1-click restore.
- **Acceptance**: Removing a mod cleans its orphaned JSON/TOML configs without manual file browsing.

### MP-124 | Silent Windows Logon Launcher Integration
- **Files**: `scripts/install-autostart.ps1`
- **Steps**: Provide optional silent startup entry minimized to system tray for instant game launching.
- **Acceptance**: Launcher launches silently to tray on Windows boot with zero console flash.

### MP-125 | End-to-End Automated ModPack Verification Suite
- **Files**: `scripts/verify.ps1`, `tests/test_modpack_integrity.py`
- **Steps**: Validate modlist hashes, JVM flag syntax, launcher compilation, and verify gates.
- **Acceptance**: `verify.ps1` runs in under 3 seconds with 100% green gates.


---

## 5. Mandatory Standards 24 to 27 Architecture

### 5.1 Launch Package (Standard 24)
- **Identity & Domain**: Fresh dedicated repository (`sirahmed8/sir-modpack`), clean desktop distribution pipeline, target domain `sirmodpack.app` (~$12.00 / ~550 EGP/yr).
- **Supported Platforms & Build Commands**:
  - Windows Desktop (Primary): `npm run tauri build` (Produces lightweight native `.msi` and `.exe` installer).
  - macOS / Linux: `cargo tauri build --target x86_64-unknown-linux-gnu`.
- **Security & Integrity Tasks**:
  - Official Microsoft / Mojang OAuth2 authentication; zero storage of user Minecraft passwords.
  - Cryptographic verification: All downloaded mod files validated against remote SHA-1 / SHA-256 hashes.
  - Silent background updates via `CREATE_NO_WINDOW = 0x08000000`.
- **Fair EGP Commercial Model**:
  - 100% Free Core Modpack & Launcher: Zero ads, zero Overwolf bloat.
  - Optional Curated Server Hosting: 89 EGP / month (Paymob test checkout integrated with "Launching Soon" fallback).
- **Owner Activation Checklist (Plain Arabic & English for Ahmed)**:
  1. Buy domain `sirmodpack.app` on Namecheap (~$12.00 / 550 EGP) and deploy static landing page.
  2. Register Azure AD Application for Microsoft OAuth2 authentication.
  3. Verify: Click "Sign in with Microsoft", authenticate via browser, verify modpack launches into title screen at 120 FPS.

### 5.2 Market-Grade Compliance (Standard 25)
- **Competitor Study**: Documented in `_SIR/plans/competitors/sir-modpack.md` with cited sources comparing against CurseForge, Modrinth App, Prism Launcher, and ATLauncher.
- **Commercial Usage & Gaming EULA Compliance**:
  - Adheres strictly to the official Microsoft / Mojang Commercial Usage Guidelines.
  - COPPA Compliance: Age gate (13+) for online multiplayer and Discord integration.
- **Privacy-First Analytics**: Opt-in anonymized telemetry measuring launch crash frequency and average FPS; zero username or chat telemetry captured.
- **Legal Pack with Lawyer Disclaimer**: Pre-drafted Terms of Service, EULA Disclaimer, and Privacy Policy, marked: *"AI-drafted for technical clarity; to be reviewed by a qualified Egyptian attorney before commercial launch."*

### 5.3 Autonomous Operations (Standard 26)
- **In-Product Assistant**: "مرشد المودباك" - embedded support assistant grounded in Fabric mod compatibility lists, Java runtime troubleshooting, and shader optimization.
- **Operations Runbook**: Nightly mod manifest verification, broken download mirror auto-failover, error log digests, and health check route (`/api/health`).
- **12-Week Marketing Launch Calendar**: Reddit r/Minecraft teaser (Weeks -2 to 0), YouTube performance benchmark comparison vs CurseForge (Weeks 1 to 4), Arab gaming Discord server partnerships (Weeks 5 to 8), community building contest (Weeks 9 to 12).
- **Escalation & Guard Rails**: Maximum daily external AI spend capped at $2.00/day. Chairman notified via Telegram bot ONLY for Mojang OAuth2 authentication deprecations or download CDN failures.

### 5.4 Visibility & Discovery (Standard 27)
- **High-Intent Search Queries**:
  - Arabic: *"مودباك ماين كرافت لتسريع اللعبة", "تشغيل ماين كرافت 120 فريم على اللابتوب", "أفضل لانشر ماين كرافت بدون إعلانات"*
  - Egyptian Slang: *"إزاي أزود فريمات ماين كرافت بدون لاج", "أحسن لانشر ماين كرافت خفيف"*
  - English: *"performance Minecraft modpack Fabric 1.21", "lightweight Minecraft launcher Windows", "120 FPS laptop Minecraft setup"*
- **Generative Engine Optimization (GEO)**: Publishes validated `llms.txt` and `/facts` page with structured benchmark tables, mod lists, and entity definitions.
- **Technical SEO & Structured Data**: Pre-rendered Next.js metadata, valid `SoftwareApplication` JSON-LD schema, and automated weekly AI visibility testing script (`scripts/check_ai_visibility.py`).
