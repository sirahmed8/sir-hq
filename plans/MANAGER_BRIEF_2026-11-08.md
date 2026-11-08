# Manager brief, 2026-11-08 (from Ahmed, the CEO). Read after START_ANY_AI.md. It outranks older priority lists.

## 0. Priorities this week (order)
1. SIR Study, now. Ahmed has midterms this week and has not studied. Start workers on Study immediately (details in section 1). This pauses nothing else: AHome keeps running with its own workers.
2. SIR Jobs: start earning money (section 2).
3. SIR AI plus the AgentsRoom study (section 4) and account switching (section 5).
4. AHome continues with its workers (TASKS.md top-down). Other automation projects get workers too: Laptop Manager (machine health), Negm Furniture, Portfolio, in wave order.
Run up to 3 agents at once and keep the queue full across projects, not only AHome.

## 1. SIR Study: midterms
- Goal: Ahmed passes by studying efficiently. Rules stay: help him learn, never take graded work, never submit or complete graded assignments or exams for him, never help during an exam. Midterm preparation is allowed and wanted.
- Today: inventory the materials (`SIR Study/materials`, the e-learning portal he is already signed in to in the main browser, deadlines/exam dates from iCal or the portal pages) and build a countdown of every midterm with date, scope and weight.
- For each subject, in order of exam date: a one-page cram sheet, a per-lecture summary (start to the exam scope), key terms and formulas, worked examples with different numbers, 30 to 60 flashcards, practice questions in the real exam format with answers explained, a 3-day plan sized to the time left (daily blocks of 15, 30 or 60 minutes plus what to do the night before). Arabic and English as the material needs. Private files stay local (local models for bulk drafting through `_SIR/scripts/ai/ask.ps1`; Claude reviews accuracy against the source).
- Deliver in a simple way he can use on his phone today: one `START_HERE` page (what to study now), a Telegram or web push reminder schedule from the existing AHome-style reminders only if it does not expose private data, and quiz mode (ask question, he answers, explain). Track weak topics and repeat them.
- Keep Study's PLAN/TASKS true; report only what is ready to study.

## 2. SIR Jobs: earn money
- Use the main browser (Ahmed is signed in almost everywhere) and computer use to find real, paid, legitimate work: freelance platforms and remote job boards that fit his skills (web and app development, AI automation, Arabic/English content, design systems), plus local Egyptian options. Shortlist with an honest fit score, draft tailored proposals and applications from his real CV/portfolio, never invent experience, never apply or message as him without his rule allowing it: preparing and submitting through the platforms he is already signed in to is allowed; anything that speaks to a person live or involves payment or identity checks goes to OWNER_ACTIONS.md.
- Also create products that earn: the manager picks the fastest legal route (sell a service package, templates, a small SaaS from SIR Platform with Launching Soon billing) and plans it with the Company blueprint (`plans/SIR_COMPANY_BLUEPRINT.md`).
- Track outcomes (applications sent, replies, income in EGP) in Jobs' own checkpoint; honest numbers only.

## 3. Browser and computer use (cheap way)
- Main browser first: Ahmed's Chrome profile is signed in to almost everything. Agents use it through the Chrome extension tools or the computer-use plugin instead of asking for logins. Never type or store passwords; if a page asks for a sign-in, 2FA or CAPTCHA, stop that step and log the single owner action.
- Save usage: when a CLI (Antigravity, OpenCode, Kilo) cannot use the browser or computer-use plugins, the manager starts a Haiku agent (Claude, cheapest) to do the browsing or the screen work, and that agent reports a short result back to the manager (facts, URLs, file paths, 15 lines max). Claude itself may also use the browser and computer directly when that is faster.
- Batch actions, few screenshots, read page text instead of screenshots when possible.

## 4. SIR AI and the AgentsRoom study
- SIR AI (`SIR AI`) has in `legacy/` an extension intended to let Antigravity use the browser. Test it for real (install it, run a browsing task from Antigravity, measure, fix or rebuild properly).
- SIR AI is almost the same idea as AgentsRoom with features AgentsRoom lacks, and lacks features AgentsRoom has. Goal: SIR AI gets every AgentsRoom feature plus its own extras.
- Reverse-engineer AgentsRoom as a clean-room study: observe the installed app (screens, behaviour, settings, config and data formats on this PC, its public docs and changelog), check its terms of use first, and write a feature specification per feature (what it does, UI, data model, protocol, edge cases) into `D:\Projects\SIR AI\legacy\agents-room\` (specs, screenshots, flow diagrams, config schemas; no copied proprietary code or assets). Then start workers on SIR AI from the start of its plan: they build from those specs and the other legacy projects, so the project is faster than a blank start. The same legacy-first rule applies to every project: scan `legacy/` first and port value.
- Compare feature lists side by side (AgentsRoom, SIR AI legacy, Odysseus reference) into a table in SIR AI's BENCHMARK.md, then plan the merge.

## 5. Antigravity accounts: switching without hitting limits
- Accounts (Google): `a7medorabe7@gmail.com` (Pro), `ahmedalaa2006.7.6@gmail.com`, `1sir1ahmed1@gmail.com`, `a01083835229@gmail.com`. Ahmed has 4 Pro and about 15 free accounts; every other account in the Antigravity account picker is free. The `a01083835229` account is a PAID account and has the Claude models (Sonnet, Opus) and Argon in the agy CLI; the others are promotional Pro and do not. Use `a01083835229` only for work that needs those models (design, review, security, hard debugging); give routine coding to the promo Pro accounts.
- Track usage per account: Antigravity shows it in Settings, Models tab (5-hour and weekly limits). Keep `D:\Projects\_SIR\ops\agy-accounts-usage.md` with, per account label (never passwords or tokens): date/time read, 5-hour meter, weekly meter, reset times, plan type, models available, last used. A Haiku computer-use agent reads the Models tab on a schedule (every 2 hours while work runs, and before any switch) and updates the manager with a short line per account.
- Switching procedure (Haiku agent with computer use, only when the current account is at its limit or below the safe margin): open the Antigravity app, Settings, Accounts, sign out, sign in, choose the account from the Google account chooser already signed in on this PC (never type a password; if the chooser needs a password, 2FA or CAPTCHA, stop and log one owner action). Before choosing, read the usage table and pick the account with the most headroom for what the next tasks need; never switch blindly into an account that is nearly exhausted. After the switch, verify the signed-in email in the app and update the usage file.
- Margins: leave an account at 85% of the 5-hour meter and at 90% of the weekly meter; workers finish their step, commit and report before the switch.
- When the free accounts help (small, cheap tasks, local-ready reviews), use them last after the Pro accounts.

## 6. Housekeeping for the manager
- Add the new roles from the Company blueprint (Compliance, CFO, SRE, Support) if missing, and any role this brief needs (study coach, jobs scout, browser/computer-use operator on Haiku, account-switch operator on Haiku). Remove unused or duplicate agents.
- Log changes in `_SIR/ops/AGENTSROOM_CHANGELOG.md`; update AGENT_QUEUE.md and the Control Room after each real milestone.
- Report to Ahmed only what is done or a true owner action.

## 7. Succession: you may be cut off at any moment (Claude limit, crash, account switch)
Ahmed can replace the manager with Antigravity, Codex, OpenCode, Kilo or any model at any time, so the manager keeps the seat ready for the next one:
- Keep `D:\Projects\_SIR\ops\HQ_CHECKPOINT.md` and each project checkpoint true after every step (Now, exact Next step with commands or files, Open promises, Re-read list). Never keep state only in the chat.
- Keep `D:\Projects\_SIR\ops\MANAGER_STATE.md`: active projects and order, which agents are running (id, role, task, files, what each still owes), the queue, pending reviews, accounts in use and their usage (`ops/agy-accounts-usage.md`), scheduled jobs, open owner actions, decisions made this week and why, and the first three things the next manager should do.
- Work in small committed steps; push only verified work; never leave main broken; record half-done work as marked tasks. Before any known limit (80 percent) write the state files and hand off cleanly.
- Keep the roles, prompts and START_ANY_AI.md written for any model, not Claude-specific; avoid tool names only Claude has unless a fallback is written next to them.
- Anyone starting as manager pastes the START_ANY_AI.md block, reads MANAGER_STATE.md and the latest MANAGER_BRIEF, checks `git log` and the Control Room against reality, and continues; the previous manager is not needed.

## 8. Think and act like Ahmed (creative, connected, remembers)
- Study details now live in SIR Study itself (`SIR Study/.sir/PLAN.md`, `TASKS.md` T-100 to T-106, `SCHEDULE.md`): do not wait for instructions, read them and run workers. Academic integrity is a company hard line: prepare Ahmed to do his own graded work and exams, never solve graded assignments or quizzes for him to submit.
- Think like a human owner, not a task runner: for every goal list several routes (direct, indirect, from the opposite side, reuse what exists, buy time, ask what the real outcome is) and pick by cost, risk, speed and what compounds. Question the task itself ("what does Ahmed actually need by when?"), look for the cheaper or bigger move, calculate the numbers (time left, quota left, money, risk) and decide; only then brief workers.
- Decide once, apply everywhere: when you make a decision that fits every project (a design rule, a tool, a naming, a safety check, a prompt improvement), write it in the global rule files (`_SIR/standard`, `AGENTS.md`, the global design system) and propagate it to all projects through the kit generator or a script, so Ahmed never repeats himself per project.
- Build memory: keep `_SIR/ops/MANAGER_MEMORY.md` (what you learned about Ahmed preferences, each project, tools, accounts, quotas, mistakes and fixes, shortcuts that worked) and a `_SIR/knowledge/` note per project and per tool; link projects to each other (shared packages, shared data, shared design system, shared accounts); update after each lesson; prune what is stale. Anyone who replaces you reads it first.
- Anticipate: look at the calendar, exams, deadlines, renewals, quotas and weekends and prepare ahead; fix problems before Ahmed sees them; make every part connected (study to calendar, jobs to income tracking, machine health to every service, usage to scheduling).

## 9. One memory for every AI, and the life organiser (2026-11-08)
- Read `_SIR/plans/MEMORY_AND_SYNC_SYSTEM.md` and make it real in the first days: canonical AGENTS.md with thin CLAUDE.md/GEMINI.md/other-CLI pointers generated by script, a READ_LOG.md line at every session start, per-agent files in ops/agents/, MANAGER_STATE.md and MANAGER_MEMORY.md, a nightly structure check that writes ops/HEALTH_REPORT.md, and the Control Room showing freshness and read status. Fix any empty or stale project file (some .sir files were found at zero bytes).
- Put automation projects to work next to the active one: SIR Study (midterm week, T-100 to T-109), SIR Life (calendar, Tasks, Gmail triage, Telegram reminders on the SIR AI bot, T-100 to T-104), SIR Jobs, Laptop Manager, with AHome continuing. The bot reminds Ahmed, talks to him, and the manager feeds it from real task and calendar state. Study content is mirrored to Google Drive; the copy shared with friends is sanitised and contains nothing about Ahmed.
