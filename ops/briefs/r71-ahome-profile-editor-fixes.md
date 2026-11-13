# r71: AHome profile editor and input fixes (owner mobile report, 2026-11-13)

Owner sent 3 mobile screenshots of the AHome web app (dark mode, phone width). Read them first:
- D:/Projects/_SIR/ops/telegram-media/photo-1794529170535-0-739920742.jpg (avatar crop sheet)
- D:/Projects/_SIR/ops/telegram-media/photo-1794529170535-1-739920743.jpg (profile form with keyboard open)
- D:/Projects/_SIR/ops/telegram-media/photo-1794529170535-2-739920744.jpg (notification settings sheet)

Project: D:/Projects/AHome (work only under apps/ and tests; never open private data).
Read D:/Projects/AHome/AGENTS.md and .sir/CHECKPOINT.md first. Version stays 1.0.0. RTL-first, dark tokens, 44px touch targets, transform/opacity animation only. No mock data, no placeholders, no emoji in UI.

## What the owner reported (fix all of it)

1. The zoom slider under the avatar photo is broken and misplaced. In apps/web/src/components/profile/AvatarEditor.tsx the raw `<input type="range">` renders browser-default on mobile (screenshot shows a tiny red dot inside a flat grey pill, no visible track). Style it fully cross-browser (webkit/moz thumb and track) with the project tokens: clean rounded track, solid round thumb (no white overflow dot), correct direction in RTL, and keep the 44px row height. Test at 320 and 390 px.

2. The crop and zoom method needs fixing.
   - clampState in apps/web/src/lib/profile/avatarEditor.ts clamps offsetX/offsetY after rotation but does not remap the pan across rotation axes: pan to an edge, press rotate, and the photo jumps or empty space shows. Remap offsets when rotation changes (swap/negate axes correctly) inside the rotate action so the crop stays continuous.
   - Add pinch-to-zoom and two-finger pan on the round frame (currently only one-pointer drag). Keep the existing slider and zoom buttons working; all three must share one state.

3. Every text input must stay visible above the mobile keyboard (owner: "any type box must rise above the keyboard so the user sees what they type"). The bio field in apps/web/src/components/profile/ProfileForm.tsx is covered by the keyboard (screenshot 2). The app already has the right kit: apps/web/src/hooks/useKeyboardViewport.ts and apps/web/src/lib/chat/viewportMath.ts (used by chat). Apply the same mechanism to the profile form sheet, the search bar, and any other sheet or screen with a text input (grep for input/textarea in apps/web/src/components and apps/web/src/app). On focus, the focused field must scroll into the visible area and the action buttons must not be hidden under the keyboard.

4. Buttons on the crop sheet: audit every button (rotate, reset, save, cancel, the top toolbar row and the bottom nav) for dead clicks, wrong handlers, and RTL layout order. The owner says "the buttons are still broken": verify each one actually does what its label says, fix what is wrong, and add pointer feedback (active:scale) where missing.

5. Notification settings sheet (screenshot 3): the toggle knobs are white circles overflowing their red track (apps/web/src/components, the notification settings sheet). Fix the toggle so the knob stays fully inside the track in both states, and check the ringtone dropdown row renders correctly in RTL.

## Checks (all must pass before commit)
- cd apps/web: tsc --noEmit, eslint on touched files, npm test, npm run build.
- Screenshots at 320 and 390 px of: the crop sheet, the profile form with a keyboard-open emulation (visualViewport resize), and the notification settings sheet. Save under ops/reports or the project's screenshots folder and reference them in the report.
- Commit straight to main (no PR), push. If the runner had uncommitted AHome changes from a previous task, review the diff first, never revert it, build on it.

## Root causes HQ found in the source (use these, do not spend a round re-diagnosing)

1. Slider height bug, exact cause. `AvatarEditor.tsx` line 98 gives the range input the class `min-h-[44px]`, while `apps/web/src/app/globals.css` line 1057 makes every `input[type="range"]` `height: 4px` with `background: rgba(255,255,255,0.2)` and `appearance: none`. The 44px minimum wins, so the whole 44px box is painted light grey: that flat pill with a small red dot in the owner's screenshot. Fix: no min-height on the input itself. Wrap it in a 44px tall label or div that carries the touch height, and give the input an explicit component class (for example `ui-range`) with a 4 to 6px visible track, a filled part up to the thumb, and a 20px round thumb with no white ring that overflows. Keep `accent-color` off that class so the white border from the global rule cannot come back.

2. The crop editor is not a sheet. `ProfileForm.tsx` line 88 renders `<AvatarEditor />` inline inside the settings card, so on a phone the settings tab strip, the tab bar and the page behind stay in place and the editor is squeezed between them. Make it a real modal: fixed inset overlay, z-index above the tab bar, own scroll area, safe-area padding at the bottom, and the tab bar not reachable while it is open. `PersonProfileSheet.tsx` is the existing pattern to copy.

3. The keyboard kit exists but only the chat uses it. `apps/web/src/hooks/useKeyboardViewport.ts` is only mounted in `apps/web/src/app/page.tsx`. `SettingsTab.tsx` (line 61, `pb-40`) and every settings or profile card do nothing when the keyboard opens, so the bio field sits under it. Mount the hook once in the screen that owns the tab content (or in the settings tab), then: when `html[data-keyboard-open]` is set, the scroll container gets bottom padding of `var(--kb)` and the focused field scrolls into view with `scrollIntoView({ block: "center" })` on `focusin`. Do it for the name field, the bio, the search bar and every other sheet with a text input. Proven by the existing harness page `apps/web/src/app/dev/chat-keyboard/page.tsx`: add a profile-form case there and take a screenshot with the emulated keyboard open.

4. Toggle: no maths error in the track (51 track, 27 knob, 2 inset, 20 travel). What is suspect is (a) the duplicate dead rule `.ui-switch__thumb { background: #ffffff !important }` at `ui-controls.css` line 251, and (b) the pointer drag leaving the knob scaled and shifted when the gesture ends outside the control (inline transform set in `handlePointerDown` and only cleared in `finishDrag`). Reproduce at 390px: tap, drag and cancel in both RTL and LTR, on and off; the knob must end fully inside the track every time and no inline transform may stay behind.

5. "الزراير مضروبة": the crop sheet is the place to look, because it is the screen where every control sits in a 280px column (rotate, reset, cancel, save, zoom out, zoom in). At 320px with `whitespace-nowrap` and `px-3` those labels can clip. Every button must be at least 44px, show `active:scale`, have a visible focus ring, and never clip its label at 320px.

6. The pill "الملف الشخصي" at the top right in screenshot 1 is the settings sub-tab strip (`LiquidTabs` in `SettingsTab.tsx`), not a duplicate button. Leave the strip as it is; do not remove it.

## Report
Write D:/Projects/_SIR/ops/agy-runs/reports/r71-ahome-profile-editor-fixes.md: what changed per item, commands run with real output tail, screenshot paths, what is open.
