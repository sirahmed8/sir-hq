import subprocess, sys

COMMON = (
    "ROUND 10 FROM THE MANAGER (2026-11-09, from the owner's own testing on laptop and phone). "
    "Read D:/Projects/_SIR/plans/GEMINI_QUALITY_CHARTER.md first and follow it for every task (plan first, one design system, "
    "motion like the Dynamic Island everywhere, computed layouts, tab bars with the active label only, own logo everywhere, "
    "no yellow buttons, self-review). Rules unchanged: version 1.0.0, no emoji, truth rule, verify green, push to main, Haiku does "
    "computer control, AHome private data never leaves. FIRST re-check that EVERYTHING from your old prompts and your ledger is "
    "finished (list it in the report); then do the items below with before/after screenshots; then keep your perpetual loop. "
    "Report to ops/agy-runs/reports/r10-SLUG.md and run agy-done.py r10-SLUG. "
)
ICON = (
    "ICON ORDER (all projects): your project needs its OWN logo image (draw a clean SVG/PNG): use it as the browser favicon, "
    "as the installable app/PWA icon (manifest icons 192/512, apple-touch-icon, Android launcher icon where there is an app), and "
    "as the image in the top navigation bar instead of whatever generic or broken icon is there now. Also set the project's Desktop "
    "folder icon if not done. "
)

ITEMS = {
    "laptop": ("D:/Projects/SIR Laptop Manager",
        "ALSO: the owner says this chat has not finished its older tasks: list every task in all your earlier prompts (standing, "
        "r3 to r9, finish-all, xreview findings, ledger) with its state and finish all of them first. NEW ITEMS: "
        "(1) CMD WINDOWS: every time the owner opens the Laptop Manager site or something runs in the background, black CMD/console "
        "windows flash with many commands. Find every cause (subprocess calls without CREATE_NO_WINDOW, python.exe instead of "
        "pythonw.exe, PowerShell without -WindowStyle Hidden, scheduled tasks and start scripts, vbs wrappers) and make everything run "
        "hidden, in this project and also in the scheduled tasks SIR-*, SIR_ControlRoom_Refresh and SIR_Laptop_Manager (their action "
        "must use pythonw or hidden launchers; check with Get-ScheduledTask). The owner is gaming and gets interrupted. "
        "(2) GAME MODE AUTOMATION: find the owner's installed games (Steam, Epic, Rockstar, Minecraft, Prism, Lunar Client, any exe in "
        "game folders: build the list from the launchers and let him edit it), watch for a game process starting, then automatically "
        "close or pause everything heavy that the game does not need: Claude desktop, Antigravity, Google Chrome, background syncs, "
        "indexers. Ask apps to close gracefully, never kill unsaved work; when the game exits, reopen them. Never change security or "
        "system settings. Dry-run and undo, a log of what it closed, a visible switch to turn it off, tests. "
        "(3) STARTUP AUTOMATION: at logon open Claude desktop, Antigravity and Google Chrome (with the SIR Autonomy extension), and "
        "start every local server the projects need (Jobs 3456, Study 3300, Laptop 8765, Control Room 8899, Tailscale serve, the "
        "Telegram listener, AHome private services, Ollama), all hidden; skip while a game is running; show the result in the "
        "dashboard. Register-ScheduledTask gave Access is denied from some shells: copy the working method of your "
        "install-autostart.ps1. "),
    "jobs": ("D:/Projects/SIR Jobs",
        "NEW ITEMS: (1) The UI is broken: buttons spill outside their cards (Approve, Reject, Quick Apply sit outside the card in the "
        "Pipeline Board), cards are disorganised, colours are odd, and the owner does NOT want yellow buttons anywhere on the site. "
        "Rebuild the card layout, the button system and the palette (neutral, primary, danger, success) with computed flex/grid so "
        "nothing overlaps at 320 px to 4K, and make the whole site simpler and easier: fewer controls per card, one clear primary "
        "action, a clear next step. "
        "(2) THE MONEY GOAL (owner, this month): he wants to finish this month with real money made through AI. Make Jobs find, every "
        "day, real paid work that suits Ahmed (second-year CS student, Egypt, remote, AI/automation/web/data skills, his CV) and that "
        "AI can do: freelance gigs, small automation, content, data entry, Arabic/English translation, web and app fixes, prompt and AI "
        "services, micro-tasks. Rank by pay, speed to first payment and win probability, show a simple 'today's best 5' with exact "
        "steps, stage honest proposals (never claim what is not verified, never submit anything in his name without his approval, no "
        "spam), and for tasks the AI can do itself prepare the finished deliverable inside the project for his review and delivery. "
        "Add a plain Arabic Telegram brief once a day with the top picks and what he must tap. Also design one or two simple AI service "
        "offers he can sell (price in EGP, an example made by the AI, a short landing text) and log every real outcome honestly. "),
    "control": ("D:/Projects/_SIR",
        "NEW ITEMS: (1) The scheduled task SIR_ControlRoom_Refresh shows a console window ('Starting SIR Control Room telemetry "
        "refresh...') on every refresh and disturbs the owner while gaming: make it run hidden (pythonw.exe or a hidden launcher, no "
        "console flash) and check every other scheduled task and daemon you own the same way. (2) Claude's subscription ends in about "
        "two weeks and Gemini in Antigravity will work alone: add a visible 'Gemini handover' panel to the dashboard listing, per "
        "project, the master plan file and the next 10 detailed tasks (from .sir/MASTER_PLAN.md that each chat now writes), and an "
        "honest checklist of what Gemini still needs to work well alone. (3) Check the dashboard tab bars and project logos (the "
        "project's own logo image, not a generic icon). "),
    "study": ("D:/Projects/SIR Study",
        "NEW ITEMS: (1) Verify Study's server autostart at logon with Get-ScheduledTask and that it runs hidden with no console flash. "
        "(2) Apply the charter to every guide and the PWA: one component set for tabs, selects, cards and buttons; active-tab-only "
        "labels with icon-only others; motion; layouts at 320 px to 4K; no white outline glitches on tab switches. (3) Exams: check "
        "the schedule file against the portal calendar, then prepare the next exams equally and send one simple Arabic brief. "),
    "ahome": ("D:/Projects/AHome",
        "NEW ITEMS from the owner's phone and laptop testing (verify each at 390 px and on the phone over ADB, and fix the cause for ALL "
        "platforms): (1) AI chat on mobile: the type box still does NOT sit above the keyboard like in the normal chat. Fix it with "
        "the visualViewport technique used for the normal chat and prove it with a keyboard-open screenshot or ADB test. "
        "(2) In friends mode remove the words for 'couples space' from the top header pill and anywhere else (audit every string for "
        "couple wording in friends mode). Keep the chat title 'الشريك' exactly as it is. "
        "(3) The upload/attach sheet shows a useless vertical scrollbar: remove it (overflow rules, make the content fit). "
        "(4) White outline flashes and glitches when switching tabs on several pages: find the cause (focus ring on programmatic "
        "focus, outline transition, repaint) and fix it on every tab bar, all platforms. "
        "(5) Overlapping buttons in the game screen (XO game, invite to play, solo, sync chips overlap): rebuild with computed "
        "flex/grid wrap so nothing overlaps; audit every screen for overlapping controls at 320 to 1440 px. "
        "(6) Tab bars including Settings tabs: only the selected tab shows its label, the others show the icon only. "
        "(7) Voice record button in the normal chat: pressing it must grow the type box smoothly into the recorder like the Dynamic "
        "Island growth, and shrink back smoothly. Make that smoothness (spring, shared-element growth) the standard for every sheet, "
        "menu, card and control in the app. "
        "(8) Pages: Today, Us, Notes, Calendar, Events and Memories are still too many separate pages: confirm what shipped from the "
        "earlier merge (ADR-005) and take it further to 3 or 4 clean top-level pages with similar things together, redirects and "
        "state migration, nothing lost. "
        "(9) Apps and two-way sync: tapping link Google Tasks says synced and saved locally while the status stays not linked. Never "
        "claim success without a real result: implement the real linking flow (OAuth through the local core, no cloud AI), show true "
        "states (not linked, linking, linked, error with retry) and test it. Same for TickTick and the others. "
        "(10) The default advance notice dropdown looks different from other dropdowns and lists: replace every native select with ONE "
        "shared custom select/list component in the app's style. "
        "(11) Keep the notification channels and always-on permissions you built; add nothing the owner did not ask for. "),
}

for slug, (cwd, text) in ITEMS.items():
    path = f"D:/Projects/_SIR/ops/briefs/r10-{slug}.md"
    body = f"You are the {slug} chat. " + COMMON.replace("SLUG", slug) + text + ICON
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)
    subprocess.run([sys.executable, "D:/Projects/_SIR/scripts/agy-task.py", f"r10-{slug}", path, cwd], check=True)
