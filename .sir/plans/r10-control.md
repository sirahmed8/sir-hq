# Task Plan: Round 10 Quality Charter & Operational Independence (Control Room)

Goal: Eliminate console flashing for scheduled tasks, build a visible Gemini Handover panel with per-project master plans & next 10 tasks, implement bespoke brand logo assets, and enforce the Gemini Quality Charter across tab bars and UI motion.

## Files Touched
- `D:\Projects\_SIR\scripts\run-refresh-hidden.vbs`: New silent VBS launcher for Control Room telemetry refresh.
- `D:\Projects\_SIR\scripts\refresh-control-room.py`: Add headless logging, `CREATE_NO_WINDOW` flags, and graceful quiet mode.
- `D:\Projects\_SIR\plans\generate_dashboard.py`: Parse per-project `.sir/MASTER_PLAN.md` (or `.sir/TASKS.md` / `plans/<slug>.md`), extract next 10 tasks, and inject Gemini Handover data and brand assets into dashboard context.
- `D:\Projects\_SIR\plans\dashboard_template.html`: Add Gemini Autonomous Handover panel, tab bar active-label styling, bespoke SVG/PNG logo in top bar, and favicon/apple-touch-icon links.
- `D:\Projects\_SIR\ops\assets\logo.svg`: New bespoke vector logo for SIR Control Room.
- `D:\Projects\_SIR\ops\assets\favicon.svg`: Vector favicon.
- `D:\Projects\_SIR\ops\assets\manifest.json`: Web app manifest pointing to bespoke 192/512 icons.
- `D:\Projects\_SIR\ops\assets\icon-192.png`: 192x192 app icon.
- `D:\Projects\_SIR\ops\assets\icon-512.png`: 512x512 app icon.
- `D:\Projects\_SIR\ops\assets\apple-touch-icon.png`: Apple touch icon.
- `D:\Projects\_SIR\.sir\MASTER_PLAN.md`: Per-project master plan for Control Room / HQ.
- `D:\Projects\_SIR\ops\agy-runs\reports\r10-control.md`: Final Round 10 engineering report.

## Steps in Order
1. Silence Scheduled Tasks & Daemons:
   - Create `run-refresh-hidden.vbs`.
   - Update `refresh-control-room.py` with `CREATE_NO_WINDOW` and file logging.
   - Update Windows Task Scheduler task `SIR_ControlRoom_Refresh` to execute `wscript.exe //B //Nologo "D:\Projects\_SIR\scripts\run-refresh-hidden.vbs"`.
   - Test task trigger silently without console flash.
2. Bespoke Brand Identity & Logo Assets:
   - Create bespoke SVG logo for SIR Control Room (radar/command geometric aperture with indigo/cyan aesthetic, zero emojis).
   - Render SVG to high-resolution PNGs (192x192, 512x512, apple-touch-icon) and vector favicon.
   - Update `manifest.json` and top navigation bar in `dashboard_template.html`.
   - Update Desktop folder icon for Control Room (`Desktop\SIR Projects\SIR Control Room`).
3. Tab Bar & Dynamic Island Motion Overhaul:
   - Apply charter tab bar rules: only active tab displays text label; inactive tabs show crisp SVG icons with fluid spring physics (`cubic-bezier(0.16, 1, 0.3, 1)`).
   - Eliminate any white focus outline flashes or jumping layouts.
4. Gemini Handover Panel:
   - In `generate_dashboard.py`, scan all 16 projects for `.sir/MASTER_PLAN.md`, `.sir/TASKS.md`, or `plans/<slug>.md`.
   - Parse project master plan path, top 10 actionable next tasks with status, and readiness audit for autonomous Gemini operation.
   - Build responsive, bilingual (EN/AR) Gemini Handover section in `dashboard_template.html`.
5. Verification & Evidence:
   - Regenerate dashboard and artifact (`python plans/generate_dashboard.py`).
   - Run compilation and privacy leak checks.
   - Capture desktop and mobile screenshots (390px, 1440px).
   - Push to `main`, verify GitHub Actions green.
   - Signal completion via `agy-done.py`.

## Acceptance Checks (What will be seen on screen)
- No console window or terminal flash when `SIR_ControlRoom_Refresh` triggers (tested manually and scheduled).
- Dedicated "Gemini Autonomous Handover" section in Control Room dashboard showing all 16 projects, master plan file links, next 10 tasks, and honest readiness checklist.
- Top navigation bar displays the bespoke SIR Control Room logo (clean vector geometry, not generic/broken).
- Browser tab displays bespoke favicon; PWA manifest references 192/512 icons.
- Tab bars show label only on the active tab, smoothly expanding with spring animation on selection.

## Risks & Mitigations
- *Task Scheduler permission error*: Updating task via `schtasks` or PowerShell `Set-ScheduledTask` may need appropriate user context. Mitigation: Test task with current user token or recreate with `schtasks /create /f`.
- *Missing master plan files in other projects*: Some projects may not have `.sir/MASTER_PLAN.md` yet. Mitigation: Fallback gracefully to `.sir/TASKS.md` or `_SIR/plans/<slug>.md` while noting file presence honestly in the handover panel.
- *Privacy leak in parsed task names*: Mitigation: Filter out any sensitive names or private repos using the assertive privacy guard in `generate_dashboard.py`.
