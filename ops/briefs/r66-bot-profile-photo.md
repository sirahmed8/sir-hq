# Telegram bot profile picture: crisp high-quality image

Owner request (voice, 2026-11-12): the Telegram bot profile picture is low resolution; replace it with a better quality one.

This is item 4 of the `r64-telegram-first` brief (`ops/briefs/r64-telegram-first.md`) split into its own fast task. Do ONLY this task here; do not touch the listener, menu or reply code.

## What to do

1. Find the bot identity first: look in `D:/Projects/_SIR/tools/` and `D:/Projects/_SIR/scripts/` for the Telegram bot code (grep for `api.telegram.org`, `bot`, `TELEGRAM`). Find the bot token location (env file, never print the token). The bot is the SIR backup manager bot Ahmed talks to.
2. Source image: use the SIR AI brand icon in `D:/Projects/SIR AI/assets/brand/` (`icon.png`, `source.png`, `source-gemini.jpg`). Check its size first. If it is small or ugly upscaled, regenerate a clean high-resolution square (at least 640x640, ideally 1024x1024) version. Tools available: ImageMagick `magick` if installed, Python PIL (`C:/Users/a7med/AppData/Local/Python/pythoncore-3.14-64/python.exe -c "import PIL"` to check), or the icon scripts in `D:/Projects/_SIR/scripts/` (see `make-icons-and-desktop.ps1` and related). Keep the design faithful to the existing icon: same colors, same shape, just crisp and square with transparent or clean background. Telegram crops to a circle, so keep the important art inside the center ~80%.
3. Set the photo via the Bot API: `setMyProfilePhoto` (needs multipart upload; curl or python `requests`/`urllib`). If `setMyProfilePhoto` is unavailable, use BotFather through Telegram Web via SIR Autonomy (playbook `plans/COMPUTER_USE.md`); never press Ctrl+P, close tabs after. Do not change the bot username or name.
4. Verify with evidence: call `getUserProfilePhotos` for the bot user (or `getMe` then getUserProfilePhotos on the id) and confirm a new photo file id exists, and/or take a screenshot of the bot profile page showing the new picture. Save the verification note in `ops/verifications/`.
5. Save the final image file under `D:/Projects/_SIR/ops/telegram-media/` or `D:/Projects/_SIR/assets/` as `bot-profile-<round>.png` so future rounds can reuse it.

## Rules
- Never print or commit the bot token.
- Commit and push straight to `main` if you changed repo files; update `.sir/CHECKPOINT.md` of the project folder you worked in.
- Nothing is done without evidence (command output or screenshot).
