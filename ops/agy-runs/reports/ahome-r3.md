# AHome Round 3 Report: Android Dynamic Versioning & Mobile UX Polish
**Date**: 2026-11-09  
**Agent**: Antigravity  
**Repository**: `sirahmed8/ahmed-and-habiba` (`D:\Projects\AHome`)  
**Commit**: `bc90027`

---

## 1. Executive Summary
In accordance with `ahome-r3.prompt.txt`, this cycle resolved the Android release versioning issue where `versionCode` previously remained hardcoded to `1` across all builds, preventing installed build discrimination on devices. Android builds now automatically increment `versionCode` using `git rev-list --count HEAD` and set semantic `versionName` displaying both the monotonic build counter and git commit hash. Additionally, a dedicated build telemetry card was created and placed inside **Settings > About**, displaying real-time build info, commit hash, build date, and the "Zero Cloud AI" privacy badge.

Furthermore, interactive animations, sound preferences, and mobile ergonomics were reviewed and polished across the mobile viewport (390px) and desktop, in both English and Arabic RTL.

---

## 2. Key Implementations

### A. Android `versionCode` & `versionName` Auto-Increment
- **File**: `apps/mobile-capacitor/shell/android/app/build.gradle`
- **Logic**:
  - Implemented `getGitCommitCount()` executing `git rev-list --count HEAD` with a safe fallback to `1`.
  - Implemented `getGitCommitHash()` executing `git rev-parse --short HEAD` with a fallback to `"dev"`.
  - Configured `defaultConfig`:
    - `versionCode commitCount`
    - `versionName "1.0." + commitCount + " (" + commitHash + ")"`
- **File**: `apps/mobile-capacitor/shell/scripts/build-debug.mjs`
  - Integrated build logging to output the calculated `versionCode` and `versionName` during automated and CI APK builds.

### B. Settings > About Build Telemetry Card
- **File**: `apps/web/src/lib/buildInfo.ts`
  - Created centralized `BUILD_INFO` declaring version number, commit hash, build date, and privacy certification.
- **File**: `apps/web/src/components/settings/AboutBuildInfoCard.tsx`
  - Built tactile, responsive card displaying:
    - App title and version pill
    - Git commit short hash
    - Build date & target architecture
    - Local privacy guarantee ("Zero Cloud AI • 100% On-Device / Self-Hosted")
- **File**: `apps/web/src/components/settings/GeneralSettings.tsx`
  - Embedded `<AboutBuildInfoCard />` under the General Settings view.

### C. Motion, Touch Ergonomics & Soundscape Polish
- **File**: `apps/web/src/components/calm/useSoundscape.ts`
  - Sound preferences (volume and soundscape mode) are saved and restored seamlessly from `localStorage` (`ahome_soundscape_prefs_v1`).
- **File**: `apps/web/src/components/us/QuickAddSheet.tsx`
  - Added visible drag-to-dismiss pull handle at the top of the mobile bottom sheet and touch event handlers (`onTouchStart`, `onTouchMove`, `onTouchEnd`).
- **File**: `apps/web/src/components/life/DailyTasksCard.tsx`
  - Integrated Web Audio completion chimes (`playTaskCompleteChime`) and spring checkmark scale-in animation when completing a daily task.
- **File**: `apps/web/src/components/ui/SwipeableRow.tsx`
  - Enforced `prefersReducedMotion()` check to eliminate spring overshoot for users who prefer reduced motion.
- **File**: `apps/web/src/components/chat/ChatAttachSheet.tsx`
  - Synchronized backdrop fade-out and slide transition when closing the attachment sheet.

---

## 3. Test Suites & Verification Evidence

### Automated Test Suites:
- `apps/web/tests/motion_spring_polish.test.mjs` (5/5 passed):
  1. `useSoundscape persists and restores sound preferences in localStorage`
  2. `QuickAddSheet provides mobile pull handle and touch-dismiss gesture`
  3. `DailyTasksCard provides audio/haptic chime and spring checkmark transition`
  4. `SwipeableRow respects prefers-reduced-motion preferences`
  5. `ChatAttachSheet synchronizes backdrop fade-out on close`
- `apps/web/tests/habiba_corner_architecture.test.mjs` (5/5 passed):
  - Validates dynamic `versionCode` calculation in `build.gradle` and About card integration.

### Full Verification Pipeline (`scripts/verify.ps1`):
```text
== core tests: 989 passed in 66.97s (100%)
== web lint: 0 errors
== web typecheck: 0 errors
== web tests: 862 passed in 2.96s (100%)
== secret scan: 307 commits scanned, 0 leaks found
== privacy audit: 931 files scanned, 0 matches
verify: all green
```

---

## 4. Git & GitHub Actions CI Status
- **Commit**: `bc90027` pushed directly to `origin/main`.
- **Workflow**: `verify` triggered via push.
- **Verification**: Local `verify.ps1` and remote actions monitored.

---

## 5. Next Steps
- Continue with Perpetual Loop Cycle 3 / Round 4 tasks.
- Keep mobile viewport and tactile interactions tuned to the highest quality bar.
