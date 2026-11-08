Use your skills and tools as you see fit: plan first, use teamwork/sub-agents for independent parts, use the browser and computer-use tools to look at the real result on screen, keep going until the done-when checks pass. 

Task: SIR Laptop Manager deep scan and plan upgrade. Work in D:/Projects/SIR Laptop Manager (read its AGENTS.md, .sir/PLAN.md, TASKS.md, CHECKPOINT.md, legacy/README.md first; legacy/ is the source code to port from: never delete or edit it).
1. Scan the whole project and legacy/: what exists, what runs, what is dead, what each legacy app does. List it in .sir/reports/scan-2026-11-08.md.
2. Rewrite .sir/PLAN.md, ARCHITECTURE.md, TASKS.md, QUALITY.md, PRODUCTION.md so they match reality and are much better: clear milestones, owner-free tasks, best-in-category benchmark (a laptop manager: health, cleanup, updates, power, drivers, startup, Windhawk mods and a macOS look for Windows, agent config sync), safe defaults (never change system or security settings without a restore point; dry run first).
3. Inventory the owner's Windhawk mods and scripts (find where they are, read them, list what each does and what to improve) in .sir/reports/windhawk-inventory.md. Do not install, remove or change any mod or Windows setting now.
4. Run the project's tests or verify if any exist and record the result.
Done when: the scan report, inventory report and rewritten plan files exist, tests status recorded. Commit locally; do not push.
