Fix every item that failed verification of r15-laptop.

Verification file: D:\Projects\_SIR\ops\verifications\r15-laptop.md
Project: D:/Projects/SIR Laptop Manager

Failed items:
- Item 2: Update winget packages (one by one, retry up to 3 times on error, keep restore point) -> `winget upgrade --include-unknown` still lists 13 upgrades available, including packages updates.md marked done: Lunar Client (still `3.7.28-ow` -> `3.7.28` available), OpenAL (still `Unknown` -> `1.1`), Google Cloud SDK (`585.0.0` -> `593.0.0` available; `gcloud --version` reports 588.0.0), plus Chrome, VC++ redists, PowerShell 7.7, Tailscale, Windows Terminal, Node.js LTS 26.13.1, Gemini, WSL. updates.md leaves gcloud as "جاري التحديث" (in progress) and never records final state
- Item 3: Update npm global packages -> `npm ls -g --depth=0` shows `vercel@50.1.3` (updates.md target was 65.14.0) and `npm -v` = `11.20.0` (target was 12.2.2). updates.md leaves both as "قيد التحديث" (in progress). Other packages did update (crush 0.100.0, copilot 1.0.109, cline 3.0.74, firebase-tools 15.35.0, droid 1.8.0, eas-cli 27.7.2) but the item is not fully done

Rules: fix the cause, not the report. Add or update a test for each fixed item where the project has tests. Check the shared lessons in D:/Projects/_SIR/ops/LESSONS.md for the touched screens. Run the project's checks and CI until green, commit and push to main, update the project checkpoint, and write a short report with the real command output.
