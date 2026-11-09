# Round 11 Full Audit Report: AHome [التطبيق الخاص]
**Auditor**: Antigravity (Gemini 3.8 Flash High)
**Date**: 2026-11-09 19:33 (Cairo Time)
**Scope**: Mandated Round 11 Owner Directives (Top Settings Window, Side Menu Drawer/Rail, Full RTL/LTR Mirroring, Zero-Console Windows, Dynamic Island Update Notice with Build ID Detection)
**Target Device**: Xiaomi Redmi Note 12 Pro+ 5G (`ronf6d5hrkqsuoaa`) via ADB
**Repository**: `D:\Projects\AHome` (reporting to `_SIR`)
**Version**: 1.0.0 (Strictly enforced; hidden build ID used for updates)

---

## 1. Executive Summary & Verification Ledger

All directives from the Round 11 Addendum (`D:/Projects/_SIR/ops/briefs/r11-ahome.prompt.txt`) were executed with zero compromises:
1. **Top Settings Window (`TopSettingsWindow.tsx`)**: Replaced scattered top-bar controls with ONE unified settings button at the top trailing end of the Dynamic Island header. Tapping it opens a compact, tactile popover window growing smoothly with spring physics, housing all settings in 5 distinct groups: Appearance & Theme, Language & Direction, Privacy & Shield, Audio & Haptics, and Tools & Quick Diagnostics.
2. **Side Navigation Menu (`SideNavigationMenu.tsx`)**:
   - **Mobile (<768px)**: Sliding drawer from `inset-inline-start: 0` triggered via hamburger button in top header; displays user profile pill, online status, and complete tab navigation with icon + label + active badge. Bottom dock maintains at most 4–5 core items.
   - **Desktop/Tablet (>=768px)**: Collapsible rail on the screen's starting edge with smooth width transition (w-16 compact icon-only to w-60 expanded), state persisted in local storage.
3. **RTL and LTR Mirroring**: Fully mirrored drawer side, chevron indicators, animation origin (`origin-top-left` for RTL, `origin-top-right` for LTR), and strict logical CSS properties (`ps/pe`, `ms/me`, `inset-inline-start/end`).
4. **Zero Console Windows Prevention**: Root-caused black CMD/PowerShell window flashes to `subprocess.run` calls without `CREATE_NO_WINDOW`. Added `creationflags=0x08000000` across `vram_orchestrator.py`, `ocr_windows.py`, and `doctor.py`. Patched `ahome-service-supervisor.ps1` to run build checks with `-WindowStyle Hidden`.
5. **Dynamic Island App Update Notice (`appUpdate.tsx`)**:
   - Integrated update detection via hidden `buildId` (from `/downloads/version.json`) while keeping visible version strictly `1.0.0`.
   - Dismissal persistence stored by `buildId` in `localStorage` (`ahome_dismissed_update_build_id`); once dismissed or postponed with "Later", never shows again for that build.
   - Real, functional states: `available` -> `downloading` (with animated progress bar) -> `ready` -> `installing` -> `failed` (with retry button).
   - "تحديث الآن" triggers direct Android APK download and package install on Android, or cache purge + service worker unregister + reload on Web.
   - Spring animations (`--di-spring`), full Arabic/English bilingual strings, and testing support via `ahome:test-fake-update` and `?testUpdate=1`.

---

## 2. Detailed Implementation Breakdown

### 2.1 Top Settings Window
- **File**: `apps/web/src/components/navigation/TopSettingsWindow.tsx`
- **Trigger**: Rendered in `DynamicIsland.tsx` header trailing end. Rotating gear icon with tactile feedback and active glow.
- **Groups**:
  1. *Appearance & Display*: AMOLED Dark, Light, Cyberpunk theme selector; Cozy vs Compact density toggle.
  2. *Language & Direction*: One-tap switch between `العربية (RTL)` and `English (LTR)` via `setAppLocale`.
  3. *Privacy & Shield*: Active user display and one-tap toggle for Privacy Cloak ("وضع الأصدقاء").
  4. *Audio & Haptics*: Sound effects toggle (`ahome_sound_effects_enabled`) with haptic response.
  5. *Tools & Diagnostics*: Cache reload button and link to full advanced settings tab.
- **Design System Conformance**: 0 raw hex, 0 raw `rgba()`, 100% theme tokens, Escape/outside-click dismissal.

### 2.2 Side Navigation Menu (Drawer on Mobile, Rail on Desktop)
- **File**: `apps/web/src/components/navigation/SideNavigationMenu.tsx`
- **Mobile Drawer**:
  - Anchors to `right-0` in RTL, `left-0` in LTR with smooth slide transition `ease-[cubic-bezier(0.16,1,0.3,1)]`.
  - Triggered via top bar hamburger menu button (`data-side-menu-trigger="true"`).
  - Displays user avatar, partner online badge, privacy cloak badge, and all 9 navigation tabs.
- **Desktop Collapsible Rail**:
  - Mounted in `AppFrame as="main"` with `md:ps-16`.
  - Toggles between icon-only rail (w-16) and full expanded panel (w-60).
  - Toggle chevron mirrors direction based on `isRtl`.

### 2.3 Elimination of Console Windows
- **Root Cause**: On Windows, when background processes or services run detached from a console, any child process invocation of a CUI binary (`powershell.exe`, `nvidia-smi.exe`, `git.exe`, `manage-bde.exe`) without `CREATE_NO_WINDOW` (0x08000000) forces Windows to allocate a transient console window on the interactive desktop, causing visible black flashes.
- **Patches Applied**:
  - `apps/local-core/data/vram_orchestrator.py`: Added `creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0x08000000)` to `nvidia-smi` queries.
  - `apps/local-core/data/ocr_windows.py`: Added `creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0x08000000)` to `powershell.exe` helper invocations.
  - `scripts/doctor.py`: Added `creationflags=0x08000000` to all `powershell.exe`, `git`, and `manage-bde` checks.
  - `infra-daemons/ahome-service-supervisor.ps1`: Patched `Start-WebBuildIfStale` to run `web-build.ps1 -Check` via `Start-Process ... -WindowStyle Hidden -Wait`.

### 2.4 Dynamic Island App Update Activity
- **File**: `apps/web/src/components/island/activities/appUpdate.tsx`
- **Detection Logic**: Reads `/downloads/version.json`. Compares `info.sha256` or `builtAt` against local build stamp. Visible version string stays strictly `1.0.0`.
- **Dismissal Persistence**: `localStorage.setItem("ahome_dismissed_update_build_id", updateInfo.buildId)`. A dismissed or postponed build never appears again.
- **Interactive States**:
  - `available`: Clean summary card with "تحديث الآن" and "لاحقاً" buttons.
  - `downloading`: Real-time percentage indicator and animated progress bar.
  - `ready`: Checkmark badge with "تثبيت الآن".
  - `installing`: Spinning sync indicator with status text.
  - `failed`: Error badge with "إعادة المحاولة" button.
- **Platform Execution**: Triggers APK download/intent on Android, and cache purge/reload on Web.
- **Testing Interface**: Dispatches `ahome:test-fake-update` on demand and supports URL parameter `?testUpdate=1`.

---

## 3. Verification Commands & Real Test Output

### 3.1 Round 11 Refinements Test Suite
Command:
```powershell
node apps/web/tests/round11_refinements.test.mjs
```
Output:
```text
✔ R11-1: Top bar has unified Settings button and compact popover window (2.8452ms)
✔ R11-2: Side navigation menu has mobile drawer and desktop collapsible rail (1.3351ms)
✔ R11-3: RTL and LTR mirroring and logical properties (1.3739ms)
✔ R11-4: Console windows prevention across all scripts and daemons (1.5054ms)
✔ R11-5: Dynamic Island update notice with buildId detection and states (0.3075ms)
ℹ tests 5
ℹ suites 0
ℹ pass 5
ℹ fail 0
```

### 3.2 Design System Token Invariant (`no_raw_hex.test.mjs`)
Command:
```powershell
node apps/web/tests/no_raw_hex.test.mjs
```
Output:
```text
✔ no raw hex or rgb colours in the shell components (10.7853ms)
ℹ tests 1
ℹ suites 0
ℹ pass 1
ℹ fail 0
```

### 3.3 Full Repository Verification (`scripts/verify.ps1`)
Command:
```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File D:\Projects\AHome\scripts\verify.ps1
```
Output:
```text
== core tests
1007 passed in 70.40s (0:01:10)
== web lint (0 errors allowed)
== web typecheck
== web tests
ℹ tests 892
ℹ suites 0
ℹ pass 892
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 3272.368
== secret scan
7:31PM INF 320 commits scanned.
7:31PM INF scanned ~10279560 bytes (10.28 MB) in 2.33s
7:31PM INF no leaks found
== privacy audit
privacy-audit: 955 files scanned, no matches (3 deny-list entries).
verify: all green
```

---

## 4. Mobile Package & ADB Streaming

1. **Gradle Build Output**:
   - `apk`: `D:\Projects\AHome\dist\ahome-debug.apk`
   - `size`: 6,988,859 bytes
   - `sha256`: `af51ebdbc09857c4ebf9950ee8f55261088b018c2c0894f817997e305a987c90`
   - `versionCode`: 322 (`versionName`: 1.0.0)
2. **Publish & Sync**:
   - Published to `dist/AHome-v1.0.0.apk`
   - Published to `apps/web/public/downloads/AHome-v1.0.0.apk`
   - Updated `apps/web/public/downloads/version.json`
3. **Physical Device Installation**:
   - Command: `adb -s ronf6d5hrkqsuoaa install -r D:\Projects\AHome\dist\AHome-v1.0.0.apk`
   - Output: `Performing Streamed Install` -> `Success`
