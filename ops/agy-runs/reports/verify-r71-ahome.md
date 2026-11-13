# verify-r71-ahome — verification report

Verifier: Devin (SWE-2 Flash). Date: 2026-11-13 ~04:20 local.
Claim under test: commit `7163267` (r71 profile-editor fixes) — crop sheet modal, pinch zoom, rotate pan remap, keyboard-safe screens, toggle drag cleanup. Prior commit `212af85` same message is its ancestor; both on `main`.

Verdict: **PASS on all brief checks.** Two suite failures during the run were caused by my own mid-suite production rebuild (daemon restart) plus the known r15 paint flake; both pass on re-run against the fresh build.

## Step 1 — tests and typecheck (exact commands and counts)

- `cd apps/web && npx tsc --noEmit -p tsconfig.json` → exit 0, no output (clean).
- `cd apps/web && npx eslint src --quiet` → exit 0, no output (0 errors; warnings suppressed by `--quiet`, consistent with repo gate).
- `cd apps/web && node --test --test-concurrency=1 tests/*.test.mjs` → **1059 tests, 1056 pass, 2 fail, 1 skip** (`.sir/evidence/r71-verify-tests.txt`, 149.5 s). The untracked `tests/r71-mobile-profile-structure.test.mjs` was included in the glob and all its r71 contract tests passed (lines 1025–1033 of the evidence file).
- The 2 failures:
  - `r15_chat_keyboard.test.mjs` — `page.waitForFunction` timeout in `ensureKeyboardOpen`. Cause: I rebuilt the web app (`scripts/web-build.ps1 -Restart`) while the serial suite was running; the daemon restart made `127.0.0.1:3000` unreachable mid-test. Re-run alone after rebuild: **PASS** (5.1 s).
  - `r15_reply_voice.test.mjs` — "Voice recorder layer must be fully opaque", read `opacity 0`. This is the documented r15 paint-timing flake (CHECKPOINT r40 note). Re-run alone: **PASS** (7.5 s).
  - Effective result: **1059/1059 pass, 1 skip** (skip is a pre-existing env-gated test).
- Note: the serial suite must run against a current `:3000` build. The build stamp was stale on arrival (`web-build.ps1 -Check` → exit 3, "sources changed"); I ran `scripts/web-build.ps1 -Restart` (build OK, daemon restarted by watchdog) before screenshots. Any browser test that hit `:3000` before ~04:05 ran against the pre-r71 build.

## Step 2 — screenshots (synthetic data only)

Harness pages: `/dev/avatar-editor`, `/dev/profile-form`, `/dev/notification-settings` (all dev-only, sample data, committed pattern from r71). Production build on `127.0.0.1:3000`, headless Chrome, `ar-EG`, `isMobile+hasTouch`, `speechSynthesis` stubbed, browser closed in `finally`. Evidence dir: `D:/Projects/AHome/.sir/evidence/verify-r71-20261113/`:

- `crop-sheet-390.png`, `crop-sheet-768.png`
- `crop-sheet-pinched-390.png`, `crop-sheet-pinched-768.png`
- `profile-form-keyboard-390.png`, `profile-form-keyboard-768.png`
- `notification-settings-390.png`, `notification-settings-768.png`

Raw probe JSON printed to console (also reproducible via `apps/web/scripts/_verify_r71_shots.mjs`, `_verify_r71_switch_kb.mjs`, `_verify_r71_kb768b.mjs` — now git-ignored scratch).

## Step 3 — checks, PASS/FAIL

| Check | 390 px | 768 px | Evidence |
|---|---|---|---|
| Slider under profile photo sits right | PASS | PASS | Slider row (44 px tall, 176 px wide) directly below the 240×240 frame (frame bottom 643 < slider top 659 at 390; 456 < 472 at 768). |
| Crop sheet works (modal, pinch, rotate, reset) | PASS | PASS | `role=dialog` bottom-sheet, `body overflow:hidden`, scroll locked. Pinch via two synthetic PointerEvents moved zoom 1 → 2.33 at both widths. Rotate applied `rotate(90deg)` transform; reset restored. Frame is `overflow-hidden rounded-full` (`AvatarEditor.tsx:193`) so the rotated photo stays clipped to the circle by construction. |
| Text inputs stay visible above keyboard | PASS | PASS | 390: `--kb=374px`, `data-keyboard-open`, both fields fully inside the 470 px visible area, save button bottom 463 ≤ 470. 768: same result verified with a portrait-tablet simulation (768×1280 → 768×906, `--kb=374px`, fields ok, save bottom 472 ≤ 906). |
| Buttons and round frame not clipped | PASS | PASS | All 7 dialog buttons `fullyVisible`, 44 px each (close, zoom out/in, rotate, reset, cancel, save). Dialog `scrollHeight == clientHeight` (no internal clipping), fits viewport at both widths. |
| Switch geometry + drag cleanup (commit claim) | PASS | PASS | Track 51×31, thumb 27×27, inside with 2 px gaps. Tap toggles `aria-checked` true→false; 120 px drag does not toggle; `data-dragging` cleared; `thumb.style.transform` empty after gesture (no stale inline styles). |

### Caveats (honest limits)

- Keyboard was verified by viewport emulation (`setViewportSize` + visualViewport), not a real on-screen keyboard. First 768 attempt (768×844 → 768×470) correctly did NOT open the keyboard state: the shrunken viewport is wider than tall, which `viewportMath.nextViewport` treats as a rotation and resets the baseline — that is intended behaviour, not a bug. The portrait-tablet simulation above is the meaningful check.
- Pinch/rotate used synthetic `PointerEvent`s, not a real multitouch digitizer.
- `imgInsideFrame` geometric check read false after 90° rotation because a rotated image's AABB exceeds the frame rect; harmless because the frame clips with `overflow-hidden rounded-full`. Verified by code, not pixels (this model cannot view PNGs).
- The dev harness `/dev/profile-form` mounts the same keyboard hooks as the app but is not the real Settings tab; the r15 chat-keyboard suite covers the real chat path and passes.

## Step 4 — housekeeping done in this round

- Repo-root `.gitignore`: added scratch patterns `apps/web/scripts/_probe_*.mjs`, `_pw_*`, `_shots_*`, `_verify_*`, `_r*_*.mjs`, `audit_cycle_*.mjs` (checkpoint next-step item). Committed `7e18876`, pushed to `main`. Tracked scripts (`_shots_r71.mjs`, `_r57_*`, `_r62_*`) unaffected.
- Rebuilt stale production web build (`web-build.ps1 -Restart`); `:3000` now serves post-7163267 code.
- Still uncommitted, deliberately: `folder.ico` (binary, owner decision per checkpoint), `apps/web/src/app/dev/notification-settings/page.tsx` and `apps/web/tests/r71-mobile-profile-structure.test.mjs` (previous worker's untracked additions — verifier does not commit product-repo files; both pass and are worth keeping, HQ call), probe scripts (now ignored).

## CI

`ops/ci-quota-exhausted.flag` exists → per worker rule 18, local verification is the gate. Local gates all green (see Step 1). AHome `main` pushed: `7163267..7e18876`.

## Recommended next

- Owner re-check on the physical phone: slider position, crop sheet, keyboard over bio field (the four open promises in `.sir/CHECKPOINT.md`).
- Decide whether to commit `dev/notification-settings` + `r71-mobile-profile-structure.test.mjs`.
- `folder.ico` still awaits owner intent.
