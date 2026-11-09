# DEEP PLAN & MASTER SPEC: SIR Mods for GTA V
**Project**: SIR Mods for GTA V (`D:/Projects/SIR Mods for GTA V`)  
**Mission**: Sovereign Grand Theft Auto V Mod Manager, Vehicle Physics Suite & Graphics Optimization Engine  
**GTA Online Safety Invariant**: Strict single-player isolation; automatically disables all mods before GTA Online boots  
**Version**: 1.0.0 (Strictly enforced)  
**Standard**: `_SIR/standard/23-premium-code-bar.md` & `_SIR/plans/GEMINI_QUALITY_CHARTER.md`

---

## 1. Executive Summary & Product Purpose
SIR Mods for GTA V is an executive mod manager, vehicle physics overhaul, and visual enhancement suite engineered for Grand Theft Auto V single-player. It provides non-destructive mod installations using an isolated `mods\` folder architecture, realistic vehicle handling physics (`handling.meta`), curated photorealistic graphics presets (ENB / Reshade tuned for 60+ FPS on laptop GPUs), and an ironclad safety interlock that prevents players from accidentally booting GTA Online with active mods.

---

## 2. Legacy Forensic Audit & Porting Analysis

### 2.1 Existing Legacy Assets (`SIR Mods for GTA V/legacy/`)
- **`SIR Mods for GTA V (v1)`**: OpenIV `.oiv` package archives, custom vehicle models, ScriptHookV script plugins, handling meta files, and earlier web configuration prototypes.
- **Wave 0 Security Fix**: Addressed a forgeable admin credential vulnerability in the legacy web interface; all owner operations now strictly validate server-side tokens.

### 2.2 What is Valuable to Port
- **Realistic Vehicle Handling Formulas**: Fine-tuned physical constants (suspension damping, center of mass, braking bias, transmission gear ratios) transforming arcade physics into responsive driving.
- **Non-Destructive `.oiv` Package Installer**: Package script that installs mods exclusively into the `mods\` directory, preserving original game archives (`x64*.rpf`) untouched.
- **GTA Online Hard Air-Gap Switch**: Automated rename of `dinput8.dll` -> `dinput8.dll.disabled` whenever online connectivity is requested.

### 2.3 What Must Be Discarded
- Insecure forgeable admin endpoints and client-side access gates.
- Brittle manual copy-paste instructions that risk corrupting core game files.

---

## 3. Architecture & Design Identity

### 3.1 Technical Architecture
- **Desktop Shell**: Tauri / Rust lightweight desktop manager with native Win32 file manipulation and process monitoring.
- **Archive Ingestion Subsystem**: Pure Rust / C# parser for OpenIV `.oiv` packages and XML `.meta` file transformers.
- **Safety Interlock**: Win32 process hook monitoring `GTA5.exe` launch arguments; terminates or disables ASI loaders if `-playGo` or online tokens are detected.
- **Web Companion**: Responsive PWA interface for inspecting installed mods and tuning handling parameters from a secondary screen.

### 3.2 Design Identity
- **Brand Aesthetic**: Vinewood Sunset & Neon Noir. Cinematic, aggressive, polished, and tactical.
- **Palette**:
  - Primary Sunset Amber: `#F59E0B` (Amber 500) / `#D97706` (Amber 600)
  - Secondary Neon Cyan: `#06B6D4` (Cyan 500)
  - Accent Vice Pink: `#EC4899` (Pink 500)
  - Dark Surface Base: Deep Vinewood Obsidian (`#080A10` / `#0E121D`)
  - Elevated Glass: Translucent Sunset Glass (`rgba(14, 18, 29, 0.75)` with `backdrop-filter: blur(14px)`)
  - **Zero Yellow Buttons**: Enforced amber, cyan, and slate tokens.
- **Typography**: Cinematic bold typography (`Inter`, `Cairo`, `Pricedown` accents for titles).
- **Motion Personality**: Dynamic Island spring transitions (`cubic-bezier(0.16, 1, 0.3, 1)`), tachometer gauge animations, active-only tab labels.
- **Bespoke Emblem**: Vector SVG tachometer gauge with needle pinned at redline and golden palm silhouette.

---

## 4. Dependencies, Cross-Project Links & Risks
- **Provides**: Custom vehicle test environment and telemetry to `SIR Controller`.
- **Consumes**: Game controller profiles from `SIR Controller`; game mode relief from `SIR Laptop Manager`.
- **Risks**: Rockstar Games software updates invalidating `ScriptHookV.dll` offsets; game integrity verification re-downloading large archive files if modified outside `mods\`.

---

## 5. The First 25 Prioritized Tasks

### GT-101 | GTA Online Safety Air-Gap Interlock (`dinput8` Disabler)
- **Files**: `src-tauri/src/safety_guard.rs`, `scripts/toggle_online_safe.ps1`
- **Steps**: Monitor game launch intent; if GTA Online is selected, automatically rename `dinput8.dll` to `dinput8.dll.disabled` and block ScriptHookV.
- **Acceptance**: Guarantees zero mod DLLs load when connecting to GTA Online, completely preventing anti-cheat bans.

### GT-102 | Non-Destructive Isolated `mods\` Folder Architecture Engine
- **Files**: `src-tauri/src/openiv_engine.rs`, `src/lib/modsFolder.ts`
- **Steps**: Ensure all vehicle, texture, and script modifications write strictly to `Grand Theft Auto V/mods/`; original game archives remain 100% read-only.
- **Acceptance**: Disabling the `mods\` directory restores vanilla game state with zero file re-downloads required.

### GT-103 | Interactive 3D Vehicle Handling (`handling.meta`) Tuner Lab
- **Files**: `src/components/handling/HandlingTuner.tsx`, `src/lib/handlingMath.ts`
- **Steps**: Visual sliders for `fMass`, `fInitialDriveForce`, `fBrakeForce`, and `vecCentreOfMassOffset`; live 3D chassis physics preview.
- **Acceptance**: Adjusting center of mass dynamically displays simulated vehicle rollover stability angle.

### GT-104 | Dynamic Island Active-Only Tab Navigation
- **Files**: `src/components/nav/TabBar.tsx`, `src/app/globals.css`
- **Steps**: Unified navigation bar (Garage, Handling, Graphics, Scripts, Safety) displaying text label only on active tab.
- **Acceptance**: Inactive tabs collapse to monochrome SVG icons; active tab smoothly reveals text label.

### GT-105 | Fast 1-Click OpenIV Package (`.oiv`) Installer & Extractor
- **Files**: `src-tauri/src/oiv_installer.rs`
- **Steps**: Parse OpenIV `assembly.xml` package files; extract models and textures; patch target RPF archives inside `mods\` folder.
- **Acceptance**: Dragging an `.oiv` package into launcher installs all assets in under 3 seconds with rollback backup.

### GT-106 | Balanced Laptop RTX Graphics Preset (ENB / Reshade)
- **Files**: `presets/graphics/vinewood_cinematic_laptop.ini`
- **Steps**: Calibrated ENB preset: soft ambient occlusion, temporal anti-aliasing, realistic vehicle paint reflections, 60+ FPS lock.
- **Acceptance**: Delivers photorealistic daylight and rain visuals with sub-14ms frametime on laptop GPU.

### GT-107 | Rockstar Game Version & ScriptHookV Compatibility Checker
- **Files**: `src/diagnostics/version_checker.py`
- **Steps**: Inspect `GTA5.exe` PE header version; compare against installed `ScriptHookV.dll` build; warn user before launching if update broke compatibility.
- **Acceptance**: Emits clear warning modal if game executable version is newer than installed ScriptHookV.

### GT-108 | Bespoke Vector SVG GTA Mods Brand Assets
- **Files**: `public/logo.svg`, `public/favicon.svg`
- **Steps**: Design tachometer gauge with needle at redline and golden palm silhouette; render multi-size favicons and desktop icons.
- **Acceptance**: Crisp vector rendering across desktop launcher and Windows shortcut.

### GT-109 | Vehicle Sound Overhaul & Custom Exhaust Audio Switcher
- **Files**: `src/components/garage/SoundSwitcher.tsx`, `src/lib/audioReloader.ts`
- **Steps**: Map high-fidelity engine audio samples (V8 rumble, twin-turbo spool, crackle overrun) to specific vehicle model slots.
- **Acceptance**: 1-tap sound swap updates game audio banks without crashing game sound engine.

### GT-110 | Real-Time In-Game Telemetry & Speedometer Overlay
- **Files**: `plugins/sir_telemetry.asi`, `src/components/telemetry/LiveTelemetry.tsx`
- **Steps**: Lightweight ASI plugin broadcasting speed (km/h), RPM, gear, and G-forces over local UDP port 8905 to secondary screen.
- **Acceptance**: Secondary mobile screen displays live sports car gauge cluster synchronized to in-game driving.

### GT-111 | Automatic Game Archive Backup & Rollback Sentinel
- **Files**: `src-tauri/src/backup_sentinel.rs`
- **Steps**: Create SHA-256 backup snapshot of any RPF archive before performing manual patch operations.
- **Acceptance**: Tapping "Undo Mod" restores original RPF archive from snapshot in under 1 second.

### GT-112 | Custom License Plate Text & Egyptian Plate Generator
- **Files**: `src/components/garage/LicensePlateGenerator.tsx`
- **Steps**: Generate custom vehicle license plate textures supporting Egyptian alphanumeric plates (Arabic letters & numbers).
- **Acceptance**: Generates 512x256 DDS texture injected into `vehshare.rpf`.

### GT-113 | Realistic Weapon Recoil & Ballistics Handling Overhaul
- **Files**: `presets/weapons/realistic_weapons.meta`
- **Steps**: Tune weapon accuracy cones, bullet velocity, damage drop-off curves, and realistic camera recoil impulse.
- **Acceptance**: Weapon firing feels punchy and tactical matching modern action shooters.

### GT-114 | Traffic Density & Pedestrian Spawn Multiplier Lab
- **Files**: `src/components/world/TrafficDensityLab.tsx`
- **Steps**: Sliders adjusting `popcycle.dat` values for ambient traffic density, supercar spawn frequency, and pedestrian crowds.
- **Acceptance**: Adjusting traffic multiplier updates spawn rates without causing texture pop-in or memory pooling crashes.

### GT-115 | Multi-Screen Responsive Launcher Verification (320px to 4K)
- **Files**: `tests/responsive_gtav.test.mjs`
- **Steps**: Playwright tests verifying mod library, garage car viewer, and handling sliders across 5 viewports.
- **Acceptance**: Zero horizontal overflow and zero button clipping across all test viewports.

### GT-116 | Clean Mod Uninstaller & Orphaned File Vacuum
- **Files**: `src-tauri/src/uninstaller.rs`
- **Steps**: Track every file written per installed mod in a local ledger; uninstalling mod cleanly deletes exactly those files.
- **Acceptance**: Cleanly removes all vehicle textures and scripts without leaving dangling orphaned files.

### GT-117 | Controller Deadzone & Vibration Tuning Bridge
- **Files**: `config/sir_controller_mapping.json`
- **Steps**: Connect directly to `SIR Controller` virtual gamepad profile; calibrate throttle and brake triggers for analog precision.
- **Acceptance**: Analog triggers provide progressive acceleration and threshold braking without lockup.

### GT-118 | Offline First Desktop PWA Service Worker Engine
- **Files**: `public/sw.js`, `public/manifest.json`
- **Steps**: Cache handling calculators and car specs offline for zero-latency tuning while gaming offline.
- **Acceptance**: Disconnecting network allows full handling configuration and calculation.

### GT-119 | Vinewood Sunset & Daylight High-Contrast Theme Engine
- **Files**: `src/hooks/useVinewoodTheme.ts`
- **Steps**: Zero-flash theme switcher; sunset noir theme tuned for evening gaming sessions.
- **Acceptance**: Theme switch triggers with zero white flash and updates all CSS variables.

### GT-120 | Clean Game Launch Shortcut with Game Mode Integration
- **Files**: `scripts/launch_gta_optimized.ps1`
- **Steps**: 1-click launcher: engages `SIR Laptop Manager` Game Mode, sets 0.5ms timer via `SIR Controller`, and boots GTA V single-player.
- **Acceptance**: Boots game into high-performance state with zero background worker interference.

### GT-121 | Texture Memory Allocation & VRAM Budget Calculator
- **Files**: `src/lib/vramBudget.ts`, `src/components/graphics/VramBudgetBar.tsx`
- **Steps**: Calculate cumulative texture memory footprint of all installed vehicle mods; warn if total exceeds GPU VRAM capacity.
- **Acceptance**: Progress bar displays estimated VRAM usage and alerts if texture streaming pool is at risk of crash.

### GT-122 | Automated Script Hook Error Logger & Crash Catcher
- **Files**: `src/diagnostics/scripthook_log_parser.py`
- **Steps**: Watch `ScriptHookV.log` and `asiloader.log`; parse fatal exceptions and display exact failing script name.
- **Acceptance**: Detects script crash and presents 1-tap "Disable Offending Script" option.

### GT-123 | Weather & Time of Day Dynamic Command Console
- **Files**: `plugins/sir_trainer_bridge.asi`, `src/components/world/WeatherConsole.tsx`
- **Steps**: Send instant hotkey commands to game: toggle weather (Thunder, Clear, Fog, Sunset) and freeze in-game clock.
- **Acceptance**: Clicking "Sunset" in web companion instantly changes in-game weather to golden sunset.

### GT-124 | Silent Windows Logon Scheduled Task Installer
- **Files**: `scripts/install-autostart.ps1`
- **Steps**: Provide optional silent startup entry for mod companion service.
- **Acceptance**: Companion service launches headlessly on boot with zero console windows.

### GT-125 | End-to-End Automated GTA Mods Verification Suite
- **Files**: `scripts/verify.ps1`, `tests/test_gtav_integrity.py`
- **Steps**: Validate safety interlock logic, handling math syntax, package installer, and verify gates.
- **Acceptance**: `verify.ps1` runs in under 3 seconds with 100% green gates.


---

## 5. Mandatory Standards 24 to 27 Architecture

### 5.1 Launch Package (Standard 24)
- **Identity & Domain**: Fresh dedicated repository (`sirahmed8/sir-mods-for-gta-v`), clean desktop build pipeline, target domain `sirgtamods.app` (~$12.00 / ~550 EGP/yr).
- **Supported Platforms & Build Commands**:
  - Windows Desktop (Primary): `npm run tauri build` (Produces signed `.msi` and `.exe` installer).
  - Web Companion: `npm run build` (Next.js 15 web handling configurator).
- **Security & Integrity Tasks**:
  - Zero Anti-Cheat Ban Guarantee: Air-gap interlock automatically quarantines all mod files into `_quarantine\` before GTA Online launches.
  - Non-destructive symlink architecture: original game archives are never permanently overwritten.
  - Silent background monitoring via `CREATE_NO_WINDOW = 0x08000000`.
- **Fair EGP Commercial Model**:
  - 100% Free Core Mod Manager: Full safe-mode switcher, `.oiv` package installer, and handling editor.
  - Optional Curated Audio & Vehicle Packs: 49 EGP one-time pack fee (Paymob test checkout integrated with "Launching Soon" fallback).
- **Owner Activation Checklist (Plain Arabic & English for Ahmed)**:
  1. Buy domain `sirgtamods.app` on Namecheap (~$12.00 / 550 EGP) and deploy static landing page.
  2. Paste Paymob keys into `D:\Projects\SIR Mods for GTA V\.env`.
  3. Verify: Click "Enable Safe Mode", launch GTA V, verify `dinput8.dll` is renamed and GTA Online loads with zero warning.

### 5.2 Market-Grade Compliance (Standard 25)
- **Competitor Study**: Documented in `_SIR/plans/competitors/sir-mods-for-gta-v.md` with cited sources comparing against OpenIV, GTA5-Mods manual installs, FiveM, and Vortex.
- **Publisher Policy Compliance**:
  - Complies strictly with Rockstar Games' official policy statement on single-player modding (offline single-player only; zero impact on GTA Online multiplayer).
  - Fair use DMCA safe harbor: Distributes zero proprietary Rockstar game code or copyrighted textures.
- **Privacy-First Analytics**: Opt-in anonymized telemetry measuring game launch success rates and mod load times; zero gaming hours or personal computer files scanned.
- **Legal Pack with Lawyer Disclaimer**: Pre-drafted Terms of Service, Single-Player EULA Disclaimer, and Privacy Policy, marked: *"AI-drafted for technical clarity; to be reviewed by a qualified Egyptian attorney before commercial launch."*

### 5.3 Autonomous Operations (Standard 26)
- **In-Product Assistant**: "مرشد تعديل GTA" - embedded support assistant grounded in ScriptHookV version tables, `.meta` XML syntax, and ENB shader tuning.
- **Operations Runbook**: Nightly game build version tracking, automated ScriptHookV update alerts, error log digests, and health check route (`/api/health`).
- **12-Week Marketing Launch Calendar**: GTA modding forum release (Weeks -2 to 0), YouTube handling showcase (Weeks 1 to 4), automotive modder Discord outreach (Weeks 5 to 8), realistic graphics demo release (Weeks 9 to 12).
- **Escalation & Guard Rails**: Maximum daily external AI spend capped at $2.00/day. Chairman notified via Telegram bot ONLY for game update breakages affecting all users.

### 5.4 Visibility & Discovery (Standard 27)
- **High-Intent Search Queries**:
  - Arabic: *"برنامج تركيب سيارات قراند 5 بدون باند", "تسريع لعبة GTA V للكمبيوتر", "مود القيادة الواقعية للسيارات قراند"*
  - Egyptian Slang: *"طريقة تشغيل مودات جاتا 5 من غير ما يجيلك باند", "تركيب عربيات في جاتا 5 بضغطة واحدة"*
  - English: *"safe GTA V mod manager single player", "anti-cheat safe GTA 5 mods", "realistic vehicle handling mod GTA V"*
- **Generative Engine Optimization (GEO)**: Publishes validated `llms.txt` and `/facts` page with structured handling parameters, safe-mode documentation, and entity definitions.
- **Technical SEO & Structured Data**: Pre-rendered Next.js metadata, valid `SoftwareApplication` JSON-LD schema, and automated weekly AI visibility testing script (`scripts/check_ai_visibility.py`).
