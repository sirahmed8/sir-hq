# AHome UI Bugs Audit & Remediation Report

**Date**: 2026-11-08  
**Scope**: `D:/Projects/AHome` (Web Application)  
**Status**: Completed & Verified All Green  
**Local Commit**: `21b5e66` (`main`)  

---

## 1. Executive Summary

A forensic audit and root-cause repair was conducted across the AHome web application following user bug reports and UI defects captured in `C:/Users/a7med/Pictures/Screenshots` (`Screenshot 2026-11-08 0534..0539`). All 4 reported defects plus universal mobile/desktop responsiveness issues were investigated, reproduced, surgically resolved, and verified through both automated testing suites and live browser automation (via Chrome DevTools MCP on emulated 390x844 mobile and desktop viewports in RTL/LTR and dark/light modes).

All 832 web tests and 941 core tests pass cleanly with 0 TypeScript errors, 0 ESLint warnings, 0 secret leaks, and a clean privacy audit. In adherence to AHome privacy guidelines, changes were committed strictly to local `main` with zero network push or deployment.

---

## 2. Forensic Screenshot Analysis & Bug Breakdown

| Screenshot | Affected View | Observed Defect | Root Cause |
|---|---|---|---|
| `Screenshot 2026-11-08 053856.png` | `ChatTab` (Attach Sheet) | Backdrop overlay was washed out (`bg-black/45`), text bled through, and the chat composer/message typebox was completely obscured / hidden under `ModalPortal`. | `ChatAttachSheet.tsx` wrapped the sheet in `ModalPortal`, portalling it to `document.body` and adding `inert` to `<main>`, completely hiding the composer. |
| `Screenshot 2026-11-08 053442.png`<br>`Screenshot 2026-11-08 053740.png`<br>`Screenshot 2026-11-08 053919.png` | Studio, Arcade, Settings (`DynamicBroadcastBanner`) | Banner displayed a vertical color mismatch strip on the edge and horizontal rasterization cut/clipping seams. | `DynamicBroadcastBanner.tsx` used `backdrop-blur-md` and `slide-in-from-top-2` inside an `overflow-hidden` container. Chromium's GPU rasterization divides backdrop filters into compositor tiles during CSS translations, creating visible seams and color discrepancies. |
| `Screenshot 2026-11-08 053814.png` | `DatesTab` (Empty State) | Screen had TWO add buttons: `[+ ضيف مناسبة]` in the top header AND `[ضيف مناسبة]` in the empty state card. | `DatesTab.tsx`, `CalendarTab.tsx`, and `TodayTab.tsx` rendered the header button unconditionally without checking if the list was empty, causing duplicate call-to-actions. |
| `Screenshot 2026-11-08 053849.png` | `ChatTopActionBar` (3-Dots Menu) | Tapping the 3-dots button triggered a rapid backdrop flash and open-close-reopen double toggle. | Redundant `window.addEventListener("pointerdown", onDown)` combined with `onClick` without `e.stopPropagation()` caused the pointerdown handler to close the menu immediately before `onClick` toggled it back open. |

---

## 3. Root Cause Analysis & Applied Fixes

### Bug 1: Attach & Upload Sheet Backdrop Contrast & Typebox Usability
- **Root Cause**: `ChatAttachSheet` used `<ModalPortal onDismiss={requestClose}>`. By default, `ModalPortal` portals into `document.body` and marks all other root siblings (including `<main>` and `ChatComposer`) as `inert=""`. This completely covered the chat input shell and typebox under a `fixed inset-0 z-[9999]` layer, preventing the user from seeing or typing messages while attaching media. Additionally, both `ChatAttachSheet` and `PhotoUploadModal` used a washed-out `bg-black/45 backdrop-blur-xs` backdrop.
- **Fix Applied**:
  1. In `apps/web/src/components/chat/ChatAttachSheet.tsx`:
     - Replaced `ModalPortal` with a localized React fragment.
     - Upgraded backdrop overlay to `fixed inset-0 z-40 min-h-screen min-w-full bg-black/85 backdrop-blur-md transition-opacity duration-200 cursor-default`.
     - Positioned the action sheet container at `absolute bottom-full z-50 mb-2 start-0 end-0 flex justify-center pointer-events-none px-1` directly floating above the composer.
  2. In `apps/web/src/components/chat/ChatComposer.tsx`:
     - Elevated `chat-composer` to `z-40` when sheet is open.
     - Elevated `chat-input-shell` to `z-50` when sheet is open (`${sheetOpen ? "z-50" : "z-10"}`).
     - Verified interactive text typing into `#chat-message-input` while the attach sheet is open.
  3. In `apps/web/src/components/photos/PhotoUploadModal.tsx`:
     - Upgraded backdrop overlay from `bg-black/45 backdrop-blur-xs` to deep `bg-black/85 backdrop-blur-md`.

### Bug 2: Dynamic Broadcast Banner Tile Glitch & Strip Color Mismatch
- **Root Cause**: `DynamicBroadcastBanner.tsx` used `backdrop-blur-md` and `slide-in-from-top-2` with `overflow-hidden` over transparent `bg-rose-500/10`. In Chromium on mobile/high-DPI screens, GPU rasterization creates tile boundary seams when translating elements with backdrop filters, producing mismatched color strips along the edges.
- **Fix Applied**:
  1. In `apps/web/src/components/ui/DynamicBroadcastBanner.tsx`:
     - Replaced semi-transparent blurred container with a solid, high-contrast dark surface: `relative flex items-center justify-between gap-3 rounded-2xl border border-rose-500/30 bg-zinc-900/95 p-3 sm:p-3.5 shadow-lg shadow-black/40 text-white animate-in fade-in duration-200`.
     - Removed `backdrop-blur-md` and `slide-in-from-top-2`, eliminating tile boundary rasterization seams and subpixel rendering cuts across all viewports and themes.

### Bug 3: Duplicate Add Buttons Elimination (Strictly 1 Add Button Per Screen)
- **Root Cause**: In `DatesTab.tsx`, `CalendarTab.tsx`, and `TodayTab.tsx`, the header bar rendered an add button regardless of whether items existed. When item lists were empty, the `EmptyState` card also rendered its primary action CTA, resulting in visual redundancy.
- **Fix Applied**:
  1. In `apps/web/src/components/tabs/DatesTab.tsx`:
     - Wrapped header add button with `{rows.length > 0 && (...)}`.
     - When `rows.length === 0`, only the `EmptyState` action button is shown.
  2. In `apps/web/src/components/tabs/CalendarTab.tsx`:
     - Wrapped header add button with `{!everythingEmpty && (...)}`.
  3. In `apps/web/src/components/tabs/TodayTab.tsx`:
     - Wrapped header add button with `{!showEmpty && (...)}`.
  4. Verified consistency with `NotesTab.tsx` which already followed this pattern.

### Bug 4: Three-Dots Menu Flicker & Double Toggle Eradication
- **Root Cause**: `ChatTopActionBar.tsx` registered a `window.addEventListener("pointerdown", onDown)` listener while also having `onClick` on the backdrop and the toggle button without `stopPropagation`. On mobile touch or click, `pointerdown` fired first outside the menu bounds (during transitions) triggering `setMenuOpen(false)`, immediately followed by `onClick` toggling it back to `true`, causing an open-close-reopen flicker. Furthermore, `transition-all` on the action bar container triggered layout recalculations upon z-index changes.
- **Fix Applied**:
  1. In `apps/web/src/components/chat/ChatTopActionBar.tsx`:
     - Removed redundant `window.addEventListener("pointerdown", onDown)` from `useEffect`, retaining only the `Escape` key listener.
     - Intercepted outside taps cleanly with a full-screen backdrop overlay (`z-[60]` with `bg-black/60 backdrop-blur-xs` and `onClick={(e) => { e.stopPropagation(); setMenuOpen(false); }}`).
     - Added `e.stopPropagation()` to the 3-dots button `onClick`.
     - Removed `transition-all` from the header bar and menu ref container.

### Bug 5: Multi-Tab Mobile & Desktop Visual Audit
- Tested across all tabs (Today, Chat, Dates, Calendar, Notes, Life, Memories, Arcade, Studio, Settings):
  - Emulated mobile 390px viewport (`390x844x3, mobile, touch`).
  - Executed automated DOM horizontal overflow checks (`scrollWidth > clientWidth`).
  - Result: `documentScrollWidth: 390`, `windowInnerWidth: 390`, `overflowsCount: 0` across all tabs.
  - Verified Light Mode and Dark Mode contrast compliance.

---

## 4. Verification & Testing Evidence

1. **Web Unit & Component Tests (`npm test` in `apps/web`)**:
   - `832 passed`, `0 failed`, `0 skipped`.
   - Duration: 3.3s.

2. **Turbopack Production Build (`npm run build` in `apps/web`)**:
   - Compiled successfully in 2.4s.
   - Finished TypeScript in 690ms with 0 errors.
   - Generated 17/17 static pages without errors.

3. **Master Verification Script (`powershell -NoProfile -File scripts/verify.ps1`)**:
   - `core tests`: 941 pytest tests passed in 53.4s.
   - `web lint`: 0 errors.
   - `web typecheck`: 0 errors.
   - `web tests`: 832 node tests passed.
   - `secret scan`: 296 commits scanned, 0 leaks.
   - `privacy audit`: 904 files scanned, 0 matches.
   - Final status: `verify: all green`.

4. **Live In-Browser Verification (`http://127.0.0.1:3000`)**:
   - Verified attach sheet backdrop contrast (`bg-black/85 backdrop-blur-md`).
   - Verified message typebox interactivity while sheet is open (`value: "سلام"` successfully typed into input).
   - Verified single add button in `DatesTab` empty state.
   - Verified clean opening and closing of 3-dots menu with zero flicker.
   - Verified banner background solidity and absence of tile seams.

---

## 5. Files Changed & Local Commit

```
apps/web/src/components/chat/ChatAttachSheet.tsx
apps/web/src/components/chat/ChatComposer.tsx
apps/web/src/components/chat/ChatTopActionBar.tsx
apps/web/src/components/photos/PhotoUploadModal.tsx
apps/web/src/components/tabs/CalendarTab.tsx
apps/web/src/components/tabs/DatesTab.tsx
apps/web/src/components/tabs/TodayTab.tsx
apps/web/src/components/ui/DynamicBroadcastBanner.tsx
```

- **Commit**: `21b5e66` on `main`
- **Subject**: `fix(ui): attach sheet typebox visibility, banner tile glitch, duplicate add buttons, and 3-dots menu flicker`
- **Network Deployment**: None (Strictly local commit adhering to AHome privacy directive).
