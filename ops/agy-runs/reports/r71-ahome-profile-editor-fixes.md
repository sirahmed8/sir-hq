# r71-ahome-profile-editor-fixes — report (2026-11-13)

Implemented by backup-manager session (opencode/free). Owner report: 3 mobile screenshots of the AHome app
(ops/telegram-media/photo-1794529170535-0-739920742.jpg crop sheet, ...-1- profile form with keyboard,
...-2- notification settings sheet). Brief: ops/briefs/r71-ahome-profile-editor-fixes.md.

AHome main now carries the fixes: commit 212af85 (pushed; origin/main confirmed at 212af85 via ls-remote).
Version stays 1.0.0. No PR (straight to main per owner rule).

## What changed per brief item

1. Zoom slider (done). AvatarEditor no longer puts min-h-[44px] on the raw range input; the input sits in a
   44px-tall wrapper and carries class `avatar-zoom-track` only. ui-controls.css gives that class: 6px rounded
   track, 20px solid accent thumb, no border, no accent-color (the global sheet's white thumb ring cannot come
   back), background transparent. RTL-safe (logical properties; the widget itself is symmetric).
2. Crop and zoom method (done).
   - Rotate/pan remap: new `rotateState` in src/lib/profile/avatarEditor.ts maps (ox, oy) -> (-oy, ox),
     advances one quarter turn and clamps, so the photo no longer jumps and no empty frame edge can appear.
     AvatarEditor's Rotate button uses it. -0 offsets normalized to 0.
   - Pinch-to-zoom and two-finger pan: the crop frame tracks active pointers in a Map; with two pointers down it
     latches a pinch state (start distance, start zoom, start midpoint, start offsets) and scales zoom by
     dist/startDist and pans by the midpoint delta. With one pointer it drags as before. Slider and zoom buttons
     share the same clampState state.
3. Inputs above the keyboard (done in source; on-phone check open).
   - Global `html[data-keyboard-open], body { overflow: hidden !important }` (shell.css and chatLayout.css) is now
     scoped to chat screens only (`:has(main.chat-shell)` inside @supports). Non-chat screens (settings, profile,
     search) keep scrolling while the keyboard is up.
   - Non-chat `main:not(.chat-shell)` gains `padding-bottom: var(--kb)` while the keyboard is open.
   - New hook src/hooks/useKeyboardFocusReveal.ts scrolls the focused text field to block:center on focusin
     (350 ms settle); mounted in src/app/page.tsx next to useKeyboardViewport. Covers every input/textarea
     app-wide, condensed by the shell.css change above.
   - Dev harness src/app/dev/profile-form/page.tsx mounts the form with both keyboard hooks; 320 and 390 px
     screenshots taken (see Evidence). On real keyboards only a phone can prove it (see Open).
4. Buttons (done). Crop sheet buttons all >= 44 px (min-h/min-w), active:scale on every button, focus-visible
   rose ring on all crop-sheet buttons (rotate, reset, zoom in/out, cancel, save, backdrop/close X), labels
   whitespace-nowrap so nothing clips at 320 px, backdrop/Escape/X all close. The top "الملف الشخصي" pill is the
   settings sub-tab strip (LiquidTabs) and was left as it is per the brief. The app bottom nav hides itself while
   the keyboard is open (existing shell.css rule) and is unreachable under the crop modal.
5. Toggle knob (source hardened; on-phone check open). Removed the duplicate dead `.ui-switch__thumb { background: #ffffff !important }`
   at the end of ui-controls.css (the component rule above keeps the knob white with !important). Switch drag can
   no longer strand a scaled/shifted white knob: inline styles are cleared on lost-pointer-capture (in addition to
   pointer-up/cancel in finishDrag) and on unmount; the gesture resets drag state on lost capture so a stray
   capture loss cannot toggle twice. Track/knob maths (51/31/27/2, travel 20) were verified correct and left alone.
   Whether the owner's "white circle overflowing its red track" is fixed can only be confirmed by seeing the
   notification sheet on his phone; the APK on his phone is stale (see Open).
6. Crop sheet is now a real modal (HQ root-cause 2, done): fixed inset-0 z-[80], backdrop button, centered panel
   (bottom sheet on phones, centered card on >=sm), max-h 100dvh, overflow-y-auto, safe-area bottom padding,
   close X top (end side), Escape and backdrop close. Tab bar is below the backdrop.

Also committed with this round (r64 slice, verified locally): infra-daemons telegram_lib.py, telegram_api.py,
telegram_dispatch.py, send-update.py and apps/local-core/tests/test_bot_gateway.py (14/14 green under the project
venv). Unrelated worker files (.gitignore, next-env.d.ts, folder.ico, probe scripts in apps/web/scripts/) were
NOT committed.

## Commands and results (local, 2026-11-13)

- cd apps/web; npm exec -- tsc --noEmit — clean (no output).
- npx eslint on AvatarEditor.tsx, Toggles.tsx, avatarEditor.ts, useKeyboardFocusReveal.ts — 0 errors (1 ref warning fixed).
- node --test tests/r71-avatar-editor.test.mjs — 9 pass, 0 fail.
- npm run build — ✓ Compiled, 34/34 static pages generated (includes /dev/profile-form).
- apps/local-core venv: pytest tests/test_bot_gateway.py -q — 14 passed.
- gh run list --limit 3 — verify run 43340625887 "failure" in 4s with zero steps: the GitHub Actions quota flag
  (ops/ci-quota-exhausted.flag present; expected reset ~2026-12-01). Local gates above are the evidence.
- Screenshots: apps/web/scripts/_shots_r71.mjs (channel chrome) wrote 320 and 390 px
  crop-sheet, profile-form and profile-form-keyboard to AHome .sir/evidence/r71-20261113/ (gitignored, like all
  evidence). Direct view of crop-sheet-390.png: modal renders, circle crop, track+thumb slider clean, rotate/reset
  and save/cancel rows fit, Arabic RTL labels intact. profile-form shots: form fits at 320/390, focused textarea
  shows its focus ring.

## What is open

- On-phone verification (owner, phone was dozing/locked): INSTALL_FAILED_USER_RESTRICTED earlier blocks APK updates;
  the installed APK is stale and does not carry ANY of the 2026-11-13 fixes. Needs: unlock the phone and allow
  installing the new build (or run from the dev server), then one pass over the three screens.
- The "white circle overflowing the red track" could not be reproduced from source geometry; suspected stale APK.
  If it still overflows after the new build, that means a second stylesheet rule wins in the WebView — needs one
  on-phone screenshot to pin down.
- The keyboard-open capture could not emulate a real IME in desktop Chrome (visualViewport does not shrink
  independently here); the global keyboard CSS was verified not to pin non-chat screens and the focus-reveal hook
  runs, but the end-to-end "bio above keyboard" moment needs the phone.
- The notification sheet and settings area were checked in source only, not on a live instance.
- AUTOPILOT_QUEUE.json still lists r71-ahome-profile-editor-fixes with done:false on purpose: HQ closes it after
  the owner/phone check. CI stays red until the Actions quota resets or the flag is cleared.

## Files touched

AvatarEditor.tsx, profile/avatarEditor.ts, profile/profileModel.ts (repaired another worker's half-finished 8-accent
refactor to a superset all importers accept), ui/Toggles.tsx, app/page.tsx, app/shell.css, app/ui-controls.css,
components/chat/chatLayout.css, hooks/useKeyboardFocusReveal.ts, app/dev/profile-form/page.tsx,
tests/r71-avatar-editor.test.mjs, scripts/_shots_r71.mjs, plus the five r64 bot-kit files above.
