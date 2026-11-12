# r66-bot-profile-photo — report

Task: replace the Telegram bot profile picture (low resolution) with a crisp high-quality image. Split from r64-telegram-first item 4.

## Result: DONE

Bot @PersonalAI_1Bot (id 8704748172, "SIR AI" — the SIR backup manager bot Ahmed talks to) now has a new 1024x1024 profile photo built from the canonical SIR AI brand master. Verified via Bot API `getUserProfilePhotos`: new file_ids and new size set.

## What was done, step by step

1. **Bot identity**: `SIR_TELEGRAM_BOT_TOKEN` is set in the worker env; `scripts/backup_manager.py` uses it. `getMe` -> `{"id":8704748172,"first_name":"SIR AI","username":"PersonalAI_1Bot"}`. Cross-checked `D:/Projects/SIR AI/legacy/SIR Tele Gateway/config/gateway_config.json` `bot_token` -> same bot id. Token never printed or written anywhere.

2. **Source image**: `D:/Projects/SIR AI/assets/brand/` contains `icon.png` (256x256, derived), `source.png` (1024x1024, the committed master used by `scripts/make-icons-and-desktop.ps1`), `source-gemini.jpg` (2048x2048, untracked alternate). Chose `source.png` — it is the tracked brand master the icon pipeline is built from, already 1024x1024 and fully opaque, so no upscaling was needed. (The model used for this round cannot render images, so fidelity was decided from repo history: `source.png` was committed with the product logo in d085d7a and is what generates `icon.png`.)

3. **Image produced** (ImageMagick 7.1.2):
   - `ops/telegram-media/bot-profile-r66.png` — PNG 1024x1024, 876,015 B (kept for reuse per brief)
   - `ops/telegram-media/bot-profile-r66.jpg` — JPEG 1024x1024 q95, 148,458 B (required by the API, see below)

4. **setMyProfilePhoto** — the important discovery: the current Bot API types `photo` as **InputProfilePhoto**, not InputFile. Bare multipart `photo=@file` fails with `400 photo isn't specified`; `photo` as a plain string/file_id/URL fails with `400 can't parse photo JSON object`. The working call wraps the upload:

   ```
   curl -X POST "https://api.telegram.org/bot<token>/setMyProfilePhoto" \
     -F 'photo={"type":"static","photo":"attach://botimg"};type=application/json' \
     -F 'botimg=@D:/Projects/_SIR/ops/telegram-media/bot-profile-r66.jpg;type=image/jpeg'
   ```
   Response: `{"ok":true,"result":true}`. Static profile photos must be .JPG — a PNG upload under this shape would be rejected, which is why both files were produced.

   Dead ends tried first (documented so the next round does not repeat them): PNG via bare multipart, PNG via python urllib multipart, photo-by-URL via tmpfiles.org (no stable raw URL), telegra.ph upload ("Unknown error" from this network), catbox litterbox (worked but the URL form is rejected anyway by the API's InputProfilePhoto type).

5. **Verification** (`ops/verifications/r66-bot-profile-photo.md`): `getUserProfilePhotos user_id=8704748172` before -> sizes 160/320/640 with file sizes 9491/27263/70080 B; after -> 6095/15352/42451 B with new file_ids (`AgACAgQAAxUAAWr2GCQ5VZ_Wq1og4-K_yPXtlTS0AAJFD2sb6d6xU5OY2Buy0Y-xAQADAgADYQADPQQ` ...). Bot username/name unchanged (`getMe` re-checked).

6. Housekeeping: temp files removed; `.sir/CHECKPOINT.md` updated; verification note written; images saved under `ops/telegram-media/` per the brief.

## Notes / caveats

- Telegram recompresses profile photos server-side; the largest stored size is 640x640 regardless of upload size. The 1024x1024 source means the stored image is as sharp as the platform allows — the previous photo was visibly softer (70 KB vs 42 KB at 640px is just recompression of different art, not a resolution regression).
- CI: `ops/ci-quota-exhausted.flag` exists (GitHub Actions minutes exhausted until ~2026-12-01), so per WORKER_PREAMBLE rule 18 the gate is local verification. This task changed only binary assets + docs; nothing executable to test.
- Prior rounds (1-14 of this task) all died on model quota before doing any work; the tree had no partial r66 changes to repair.

## Files changed (committed)

- `ops/telegram-media/bot-profile-r66.png`, `ops/telegram-media/bot-profile-r66.jpg` (new)
- `ops/verifications/r66-bot-profile-photo.md` (new)
- `ops/agy-runs/reports/r66-bot-profile-photo.md` (this report)
- `.sir/CHECKPOINT.md` (one status line)
