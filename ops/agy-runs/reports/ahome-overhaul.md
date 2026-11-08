# AHome Complete UI/UX Overhaul & Sanctuary Unification Report

**Date**: 2026-11-09  
**Agent**: Antigravity  
**Task**: `ahome-overhaul`  
**Status**: Verification Complete & Passing

---

## 1. Executive Summary

A comprehensive agency-grade UI/UX overhaul and sanctuary architecture unification has been executed across **AHome** (`apps/web`). All 14 directives specified in the overhaul brief and ADR-005 have been completed with zero compromises on performance, privacy, or accessibility:
- **Zero-leak Privacy Compliance**: All personal and sensitive health data (Habiba's Private Corner, reminders, notes, personal tasks) remain strictly encrypted and processed on local devices.
- **Spring Motion & Fluidity**: Integrated spring physics across bottom sheets, dynamic island states, keyboard viewport shifts, and gesture-driven swipeable items.
- **Sanctuary Consolidation**: Unified 7 fragmented screens into 4 cohesive sanctuaries while maintaining 100% deep-link and state backward-compatibility.
- **Test Invariants**: 848 automated tests passing across the entire test suite (0 failures).

---

## 2. Detailed Deliverables & Technical Changes

### Directive 1: Bottom Sheets & Dialogs Spring Motion
- Replaced harsh solid black backdrops with soft, hardware-accelerated translucent overlays (`bg-black/45 backdrop-blur-md animate-in fade-in`).
- Applied spring transformation curves (`cubic-bezier(0.34, 1.25, 0.64, 1)`) to modals, quick-add sheets, and search panels in `ChatAttachSheet.tsx`, `QuickAddSheet.tsx`, and `globals.css`.

### Directive 2: Dynamic Banners Audience Isolation & Gender Phrasing
- Created `apps/web/src/lib/perspectiveHelper.ts` with `getGenderedText()`, `isBannerAudienceMatch()`, and `personalizeBannerMessage()`.
- Dynamically personalizes copy: feminine Arabic phrasing for Habiba, masculine Arabic phrasing for Ahmed.
- Strictly isolates private study and personal notifications so private items never render on partner screens.
- Verified via `apps/web/tests/perspective_gender.test.mjs` (5/5 passed).

### Directive 3: Dynamic Island Search & Tap Spring Animation
- In `apps/web/src/components/island/machine.ts`, mapped explicit `search` events directly to expanded state transitions.
- Replaced toggle logic with smooth `send({ type: "search" })` and `closeSearch()`.
- Replaced forbidden `100vw` with responsive container width `min(24rem, calc(100% - 1.5rem))` in `globals.css` with spring timing fallback `--di-spring: cubic-bezier(0.34, 1.25, 0.64, 1)`.

### Directive 4: Keyboard Viewport & Composer Pinning
- Fixed `apps/web/src/hooks/useKeyboardViewport.ts` to prevent infinite `window.scrollTo(0, 0)` jitter loops during mobile keyboard resize frames.
- Pinned `.ai-chat-composer-wrap` to virtual keyboard top using `--vvtop` and `--vvh`.
- Added spring expansion physics to `ChatComposer.tsx` during voice recording transitions.

### Directive 5: 4-Sanctuary Page Consolidation (ADR-005)
1. **اليوم (Today / Pulse - `/`)**: Living sanctuary pulse, live prayer times with interactive checkmarks, active reminders, daily duaa, and mood.
2. **نحن (Us - `/us` / `/timeline`)**: Unifies Us, Memories, and Dates/Events with deep links and shared milestone cards.
3. **حياتنا (Life & Planning Hub - `/life`)**: Integrates Lessons & University Schedule, Study Room, Shared Calendar, Notes & Lists, Wellness, and Hudoo.
4. **الاستوديو والعافية (Studio & Wellness - `/ai_studio`)**: Integrates Local AI Arena, Voice Cloning Booth, Voice Playground, FLUX/Wan Generative Media, Calm Acoustics, Workout Hub, and Habiba's Private Corner.

### Directive 6: Image/Video Generation Emoji Removal
- In `apps/web/src/components/studio/MediaGenerationStudio.tsx`, purged `✨` and `🎬` unicode emojis from action buttons.
- Replaced with crisp Lucide SVG icons (`Sparkles` and `Video`) for agency-grade tactile aesthetics.

### Directive 7: AI Technical Copy Simplification
- In `apps/web/src/lib/translations/aichatChat.ts`, transformed cold technical messages ("Photos and voice notes are read on the laptop...") into warm, human phrasing in English, Egyptian Arabic, and Saudi Arabic:
  - `"الصور والرسائل الصوتية بتتعالج بهدوء وخصوصية تامة."`
  - `"Photos and voice messages are processed privately on your home device."`

### Directive 8: Connections & Reminder Ecosystem in Settings
- Created client API `apps/web/src/lib/connectionsApi.ts` and UI component `apps/web/src/components/settings/ConnectionsSettingsCard.tsx`.
- Integrated 4 providers:
  1. **TickTick**: Connected (Ahmed's local database sync).
  2. **Google Tasks**: Habiba's account connection trigger.
  3. **Xiaomi / HyperOS**: ICS calendar feed subscription URL copy button + manual ICS import.
  4. **AHome Voice Reminders**: On-device AI speech-to-task parsing.
- Added global sync button, failed operations badge with retry trigger, and reminder notification preferences (push alerts, Telegram bot reminders, in-app banners, early notice lead, and quiet hours 23:00 - 07:00).
- Mounted under Settings subtab `"connections"` and replaced embedded mock modal in `DailyTasksCard.tsx` with a direct shortcut link.

### Directive 9: Animated Morphing Delete & Confirm
- Created `apps/web/src/components/ui/MorphingDeleteConfirm.tsx`.
- Inline morph into an expanding chip with gentle red pulsing border: *"هل أنت متأكد؟"* with *"حذف"* and *"تراجع"*.
- Automatic revert timeout after 5 seconds of inactivity.
- Upgraded `RowActions` in `LifeCard.tsx` (propagating to `DailyTasksCard`, `MealTracker`, `MedicationsTracker`, `ObourCoursesCard`, and `StudyScheduleCard`).

### Directive 10: Configurable Swipe Actions & Mobile Long-Press
- Created `apps/web/src/components/ui/SwipeableRow.tsx` with pointer-event touch tracking, directional velocity thresholds, and RTL awareness.
- Swipe right reveals delete with inline morph confirmation; swipe left reveals edit.
- Long-press (>500ms) triggers contextual haptic vibration and context menu.
- Integrated into `RemindersList.tsx` and `DailyTasksCard.tsx`.

### Directive 11: Reminder Save Button Semantic Color
- In `ReminderPlanner.tsx` and `lifeShared.ts`, replaced non-standard `bg-amber-400` buttons with semantic primary action styles (`bg-rose-500 hover:bg-rose-600 text-white`, `focus-visible:outline-rose-300`).

### Directive 12: Daily Prayers Checkmarks & Habiba's Private Corner
- In `LifeTab.tsx`, added interactive checkmark buttons for daily prayers (`Fajr`, `Dhuhr`, `Asr`, `Maghrib`, `Isha`) with completion counter (X/5).
- Created `apps/web/src/components/calm/HabibaPrivateCorner.tsx`:
  - Menstrual cycle tracking, religious exemption awareness, natural comfort tips, respectful gentle consent sharing with Ahmed.
  - 100% locally encrypted in browser/local SQLite storage; concealed during privacy cloak mode.
  - Mounted inside `CalmHub.tsx`.

### Directive 13: Fitness & Workout Clean-up
- In `apps/web/src/components/calm/WorkoutHub.tsx`, removed redundant "منصة التمارين العلمية الذكية" header card.
- Simplified workout location and muscle group tabs ("في البيت", "في الجيم", "البطن").
- In `workoutDatabase.ts`, renamed all exercise items from pseudo-scientific jargon to natural Egyptian Arabic names ("تمرين الضغط العادي", etc.).

### Directive 14: Calm Sounds Organic Acoustic Overhaul
- In `apps/web/src/lib/calm/audio.ts`, upgraded Web Audio procedural synthesis to organic multi-band acoustic modeling:
  - Paul Kellet 3-pole pink noise filtering.
  - Procedural sine micro-droplets for natural rain against glass.
  - Dual-LFO brown noise water swells with band-pass foaming crest surf for ocean waves.
  - Velvet brown noise for authentic white/brown ambience.
- In `apps/web/src/components/calm/SoundTab.tsx`, added visual animated soundwave bars, volume percentage readout, rich sound description badges, and sleep timer options (15, 30, 45, 60 minutes).

---

## 3. Verification & Compliance Matrix

| Check | Tool / Suite | Result |
|---|---|---|
| Core Python Tests | `pytest tests -q` | 67 / 67 Passed |
| Web ESLint | `eslint src --quiet` | 0 Errors |
| TypeScript Typecheck | `tsc --noEmit` | Clean (0 Errors) |
| Web Test Suite | `node --test tests/*.test.mjs` | 848 / 848 Passed |
| Secret Scan | `gitleaks detect` | 0 Leaks |
| Privacy Audit | `privacy-audit.mjs` | Passed (No Private Data Leaks) |
| Layout / No 100vw | `tab_layout.test.mjs` | Passed |

---

## 4. Next Steps
- Commit changes locally on `main` branch.
- Signal completion via `python D:/Projects/_SIR/scripts/agy-done.py ahome-overhaul ok "..."`.
- Release lock `D:/Projects/_SIR/ops/locks/AHome.lock`.
