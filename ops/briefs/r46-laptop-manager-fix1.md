Fix every item that failed verification of r46-laptop-manager.

Verification file: D:\Projects\_SIR\ops\verifications\r46-laptop-manager.md
Project: D:/Projects/SIR Laptop Manager

Failed items:
- Item 2: Update winget packages (one by one, retry up to 3 times on error, keep restore point) -> `winget upgrade --include-unknown` still shows `Gemini Google.GeminiDesktop 1.18.0 -> 1.19.0` available and `winget list` confirms 1.18.0 installed, while updates.md claims "Gemini Desktop: 1.18.0 -> 1.19.0" done. MSYS2 needs explicit publisher targeting (documented skip) and OpenAL is pinned (documented); Gemini is neither
- Item 3: Update npm global packages -> `npm outdated -g` returns `eas-cli 27.7.2 -> 27.9.0` and `@moonshot-ai/kimi-code 2.5.3 -> 2.6.0` (npm view time: both published 2026-11-12, after the completion round). npm 12.2.2 and vercel 65.14.0 targets are confirmed installed; the other 12 globals are current
- Item L8: Shared lesson: real-time per-character bidi detection in every text input (Arabic types from right, `<bdi>`/`unicode-bidi: isolate` per run) -> `ops_ui/static/index.html` has a whole-page `[dir="rtl"]` toggle but no per-character direction detection: no `<bdi>`, no `dir="auto"`, no bidi JS hook. Inputs (`#q-search` line 5325, `#rag-search-input` line 2929, `#cp-input` line 7113) are plain LTR inputs; typing Arabic in LTR mode keeps LTR base direction/caret side, violating L8's "Arabic starts/types from right"

Rules: fix the cause, not the report. Add or update a test for each fixed item where the project has tests. Check the shared lessons in D:/Projects/_SIR/ops/LESSONS.md for the touched screens. Run the project's checks and CI until green, commit and push to main, update the project checkpoint, and write a short report with the real command output.
