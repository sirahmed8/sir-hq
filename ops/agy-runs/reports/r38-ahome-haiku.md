# AHome r38 report (haiku builder, 2026-11-12)

Verification used: CI was not used. Per the 15:00 update, GitHub Actions minutes are used up, so every check was run locally and the output is in `AHome/.sir/evidence/r38/`.

## Items (brief order)

1. Tab bar vanishes and page zooms (addendum 8): DONE. Commit 5325f29. Evidence `item1-zoom-keyboard-stuck.txt`.
2. Dynamic Island search morph, one search icon (items 5, 9): DONE. Commit 460530f. Evidence `item2-island-morph.json`, `island-search-open-390.png`.
3. Voice bar, AI voice, transcript states (items 2, 3, 4): DONE. Commit 36522a4.
   - The recorder row was 71 px inside a 56 px box and clipped. It is now one 48 px row (cancel, timer, wave, pause, send). Evidence `item3-voice-before-390.png`, `item3-voice-after-390.png`, `item3-ai-voice-390.png`.
   - AI chat uses the same recorder and the same player. `useAiRecorder` and `AiRecordingBar` were removed.
   - Transcript has five states (idle, working, done, error with retry, empty). Unit test `tests/r38_transcript_phase.test.mjs`.
   - NOT verified end to end: a real transcription with a sample audio file. It needs the PC core (local Whisper), which is not running in this session.
4. Biometric card centred, localized labels (item 1): DONE. Commit a069feb. Evidence `item4-lock-card-390.png`.
5. Profile tab in Settings (item 10): DONE with limits. Commit 69a8038.
   - Photo, name, nickname, bio, colour. Five states on the settings card and the sheet. Stored in the app's encrypted store on the device only.
   - Header shows the avatar and name, and opens a profile sheet. Save persists across reload (checked).
   - Limits: the photo is a centre crop, not a manual crop. The partner's profile exists only on the device where they saved it, because there is no sync API. On the other device the sheet honestly shows "no profile saved on this device yet".
6. Calm spacing (item 11): DONE. Commit f185cec. Cards had 0 px between them, now 16 px. Mood chips are one row of five. The arcade "reset all games" button (where that label lives) has padding and wraps. Evidence `item6-calm-390-after2.png`, `item6-arcade-reset-390.png`.
7. Games (item 12): PARTLY DONE. Commit dc0e40d.
   - DONE: games hub with two sections and one card per game (cover, title, one line, Play); back-to-hub control. Evidence `item7-arcade-hub-390.png`.
   - Decision file: `.sir/decisions/r38-3d-engine.md` (raw WebGL2, no three.js).
   - NOT DONE: the WebGL layer itself, per-game pause and levels, high-score chips (no fake numbers were added).
8. Ten or more own defects at 320/390/768/1280: NOT DONE. Defects fixed along the way: voice bar clipping, AI voice row, calm card spacing, mood chip clipping, arcade button label, six lint errors in touched files (set-state-in-effect). That is short of ten, and no 320/768/1280 pass was run.

## Local verification (last run)
- `tsc --noEmit`: exit 0.
- `npm run lint`: exit 0, 0 errors, 112 warnings (all pre-existing unused variables).
- `node --test --test-concurrency=1 tests/*.test.mjs` from apps/web: 978 tests, 978 pass, 0 fail (`tests-item7-final.txt`).
- Known flake: `r15_reply_voice.test.mjs` (WebKit) passes on some runs and fails on others ("layer must be opaque when recording"). It is the same flake the checkpoint recorded. Not fixed.
- A Next.js hydration warning appeared once on the `/dev/chat-keyboard` route. It did not reproduce in two further runs. Not investigated further.

## Left for the next round
- Item 7 3D WebGL layer and game-level polish.
- Item 8 audit loop at four widths.
- Real Whisper check when the PC core runs.
- Partner profile sync (needs a core endpoint; the owner decides the design).
- The `apps/web/src/app/dev/calm` route was committed as a dev check page, like the other `/dev/*` routes.
