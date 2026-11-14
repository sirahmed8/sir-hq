# r74-ahome-profile-save-fix report

Task: fix profile picture save and save button state (AHome).
Brief: D:/Projects/_SIR/ops/briefs/r74-ahome-profile-save-fix.prompt.txt (and .md copy).
Worker: kilo. Session: 2026-11-14 ~02:15-02:35 Cairo (UTC+2).
Commit: bfde7b2, pushed to origin/main. gitleaks clean; pre-push privacy audit clean (1087 files scanned, no matches).
CI note: ops/ci-quota-exhausted.flag is present, so per WORKER_PREAMBLE rule 18 the gate is full local verification (tsc, lint, tests) instead of GitHub Actions; CI cannot run (quota exhausted, expected reset ~2026-12-01).

## Situation on arrival

git status: clean tree on main (HEAD fbda5b3), except an untracked scratch probe apps/local-core/scripts/_probe_router.py (already intended to stay ignored per commit 7e18876; left untouched). Untracked dev files dev/notification-settings/page.tsx and tests/r71-mobile-profile-structure.test.mjs from the previous round were left as-is per the checkpoint (HQ decision item).

git log -5 showed HEAD = fbda5b3 "fix(assistant): ..."; the profile code under review was last changed by ad26326 "feat(profile): a picked photo opens a crop sheet ... then save" and 7163267 "fix(profile): r71 owner fixes" (keyboard-safe screens). No working-tree edits from a previous model needed repair.

## Finding

No code was broken. All five r74 acceptance criteria are already implemented in main:

1. Photo saves to device storage — `apps/web/src/lib/profile/profileStore.ts:20-22`: `saveProfile` writes the profile via `writeSecureJson(keyFor(id), profile)` into the encrypted IndexedDB store (AES-GCM, never leaves the device) and dispatches `ahome:profile-changed` so the chat header and settings card stay in step.
2. Button states idle -> loading -> success/error — `apps/web/src/components/profile/ProfileForm.tsx`: `SaveState` is `"idle" | "saving" | "saved" | "error"`; submit sets saving, then saved/error; the save button is `disabled={saveState === "saving"}` and shows "بنحفظ..." / "Saving..." while saving and "اتحفظ." / "Saved." after success; error shows an alert with a Retry button.
3. Validation / helper text — `validateDraft` (profileModel.ts:74) rejects a blank name (`name_required`), and the status line shows the "لسه ماتحفظش. اكتب اسمك واحفظ." / "Not saved yet. Write a name and save." helper only when not saved; once saving succeeds it is replaced by "Saved." / "آخر حفظ: <date>".
4. No keyboard overlap — `apps/web/src/components/tabs/SettingsTab.tsx:54-55` mounts `useKeyboardViewport()` and `useKeyboardFocusReveal()`; shell.css/shell layout lift fields above the keyboard so the bottom save button stays reachable (verified in r71 at 390 and 768 px).
5. RTL Arabic alignment — name input and bio textarea use `dir="auto"` (ProfileForm.tsx:151, 166); all profile copy is Arabic-first with English fallbacks.

The owner's screenshots (.sir/owner-screenshots/01-13.jpg, taken 2026-11-10) predate the r71 fix commit (2026-11-13 03:36), which is why they show the old behavior.

## Changes made

One new file, no existing files modified:

- `apps/web/tests/r74_profile_save_flow.test.mjs` (9 tests, all pass): regression test pinning the acceptance behavior — valid draft with name stores with save time; blank name refused (`name_required`); over-limit name/bio refused; save button carries idle/saving/saved/error and disables while saving; not-saved helper exists and is replaced by Saved/Last saved after save; avatar copy says cropped-to-square/stays-on-device and the picked photo goes through `prepareAvatarSource`; saving writes through the encrypted store with the profile-changed announcement; name input is direction-isolated (`dir="auto"`); Settings tab mounts both keyboard hooks.

## Verification run

- `npm --prefix apps/web exec -- tsc --noEmit -p apps/web/tsconfig.json`: exit 0, 0 errors.
- `npm --prefix apps/web run lint`: exit 0, 0 errors (117 warnings, all pre-existing unused-variable warnings; identical to baseline).
- `node --test --test-concurrency=1 tests/*.test.mjs` from apps/web: 1068 tests, 1063 pass, 4 fail, 1 skipped. The 4 failures are all `browserType.launch: Executable doesn't exist at .../webkit-2388/Playwright.exe` — pre-existing Playwright-WebKit-missing environment failures (r15 reply voice, r21 voice evidence, swipeable pager, webkit keyboard), identical to the baseline before this change. All 9 new r74 tests pass.

## Unticked / open items

None. There is no r74 checklist file in .sir/ and the brief names none; the acceptance criteria are the items, and all are verified in main. The tree is clean after the commit (only the pre-existing untracked scratch probe remains, intentionally not committed).

## Report and signal

Report written here. Next: `python D:/Projects/_SIR/scripts/agy-done.py r74-ahome-profile-save-fix ok "<one line>"`.
