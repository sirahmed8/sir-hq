# r66 verification: Telegram bot profile photo replaced with high-quality image

Date: 2026-11-12. Bot: @PersonalAI_1Bot (id 8704748172, "SIR AI", the SIR backup manager bot).
Token read from env `SIR_TELEGRAM_BOT_TOKEN` (same bot as `D:/Projects/SIR AI/legacy/SIR Tele Gateway/config/gateway_config.json` -> `bot_token`; verified both resolve to id 8704748172). Token never printed or committed.

## What changed

- New image built from the canonical brand master `D:/Projects/SIR AI/assets/brand/source.png` (1024x1024, the same source `scripts/make-icons-and-desktop.ps1` uses for `icon.png`):
  - `ops/telegram-media/bot-profile-r66.png` — PNG 1024x1024, 876,015 bytes
  - `ops/telegram-media/bot-profile-r66.jpg` — JPEG 1024x1024 q95, 148,458 bytes (required: Bot API `InputProfilePhotoStatic` only accepts .JPG)
- Command: `magick "D:/Projects/SIR AI/assets/brand/source.png" -resize 1024x1024 -strip -quality 95 ops/telegram-media/bot-profile-r66.jpg`
- `magick identify` -> `JPEG 1024x1024 1024x1024+0+0 8-bit sRGB`

## API evidence

`setMyProfilePhoto` required the new Bot API shape (photo is `InputProfilePhoto`, not a bare InputFile). Working call:

```
curl -X POST "https://api.telegram.org/bot<token>/setMyProfilePhoto" \
  -F 'photo={"type":"static","photo":"attach://botimg"};type=application/json' \
  -F 'botimg=@D:/Projects/_SIR/ops/telegram-media/bot-profile-r66.jpg;type=image/jpeg'
```

Response: `{"ok":true,"result":true}`

Note for future rounds: bare multipart `photo=@file` returns `400 photo isn't specified`, and `photo` as a plain string/file_id/URL returns `400 can't parse photo JSON object`. The JSON `{"type":"static","photo":"attach://<name>"}` wrapper plus a JPEG file is required.

## Before / after (getUserProfilePhotos, user_id=8704748172)

Before (total_count 1): sizes 160x160/9491B, 320x320/27263B, 640x640/70080B.
After (total_count 1): sizes 160x160/6095B, 320x320/15352B, 640x640/42451B — new file_ids
(`AgACAgQAAxUAAWr2GCQ5VZ_Wq1og4-K_yPXtlTS0AAJFD2sb6d6xU5OY2Buy0Y-xAQADAgADYQADPQQ` etc.).
Telegram recompresses profile photos to max 640px on its side; the uploaded source was 1024x1024 so the stored image is as crisp as the platform allows.

Bot username and name untouched (verified via getMe: `PersonalAI_1Bot` / "SIR AI").
