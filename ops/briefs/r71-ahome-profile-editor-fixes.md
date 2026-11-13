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

## Report
Write D:/Projects/_SIR/ops/agy-runs/reports/r71-ahome-profile-editor-fixes.md: what changed per item, commands run with real output tail, screenshot paths, what is open.
