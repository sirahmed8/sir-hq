# IMPROVEMENT DOCTRINE: real, visible, daily improvement (Ahmed, 2026-11-09)

"Tests are green" is not an achievement: if nothing changed, nothing can fail. A cycle counts only if the product got better in a way the owner can SEE or FEEL. Every day, every project gets new improvement missions; when they are finished the agents review them, understand the code they wrote, look at it in the running app (browser, phone viewport, computer use), and only then move on.

## Rules for every cycle
1. **Plan first (5 minutes):** study the product as a user and as an engineer, then write the cycle plan in `.sir/cycles/<date>-<n>.md`: at least 10 concrete improvements, each with the user-visible benefit and how it will be checked. Prefer big wins first (logic, backend, UX flows, motion, design system) before small polish.
2. **Build them for real:** new features, better flows, better logic, a better backend, a better frontend, better local services and automations, more animation, better design, fewer clicks, fewer errors, fewer glitches. Replace weak designs, do not just patch them. Remove what is not needed.
3. **Evidence is a before/after, not a test count:** screenshots or a short recording of the old and new behaviour, numbers (clicks, milliseconds, bytes, errors) and a one-line "why it is better". A report that says only "tests pass" is rejected and the cycle is redone.
4. **Understand and review:** reread your diff as if someone else wrote it, explain what each change does and why it is correct, run it in the real app, try to break it (bad input, offline, slow, rotate, repeat taps), fix what breaks. Use computer use and the browser to look at it like a user.
5. **Ship:** commit small, push when verify is green (tests, lint, types, secrets, privacy) and the GitHub check is green, update the checkpoint and TASKS.md, send the Arabic team brief to Ahmed.
6. **Next cycle:** pick a new lens and a new set of improvements from the backlog below and from what you learned. Never say "nothing left".
7. Each project keeps its own rules, plan, structure and order (its AGENTS.md and .sir plan). Chats work only on their own project; never on another project and never on SIR Negm Furniture (frozen, see below).

## Frozen project: SIR Negm Furniture
It is Ahmed's friend's project. No chat works on it, builds it, adds CI to it or deploys it (no Firebase, no hosting). It only exists as a private repo; later Ahmed gives it to the friend, who clones it. Until Ahmed says otherwise: do not touch it.

## Improvement backlogs (start here; add more yourself)
### AHome (Antigravity chat; the AHome Claude chat owns backend, relay, deploys)
Page merge 7 to 3-4; every sheet and menu with spring motion; gender-aware copy; island and keyboard fixes; Habiba's private corner; health, duaa, fitness, sounds rebuilt; apps connections to Settings with a sync backend; swipe actions; bot rewrite; offline-first with visible sync state; global search; widgets; notification centre; theming; onboarding; empty states with a clear first action; performance budget on a mid-range phone; accessibility; backup/restore UI; screen-by-screen design audit against the best apps (Telegram, Apple Health, Notion Calendar).
### SIR Study
Real exam simulator (timer, sections, review, score, weak-topic report); spaced repetition from the exam dates; flashcards with progress; per-subject mastery map; search across all subjects; offline PWA with install prompt; print-ready cram sheets; Arabic/English toggle per section; voice read-aloud for lectures; formula sheets; past-paper pattern analysis (patterns only); study planner with daily goals and reminders on Telegram; keyboard and touch gestures; dark/light that follows the phone; fast first paint; accessibility.
### SIR Jobs
Honest fit scoring with explanations; scam detector with reasons; duplicate and expired listing detection; saved searches and alerts; pipeline board with drag and drop; proposal builder with verified claims only and tone variants (Arabic/English); follow-up reminders; rate and target calculator with sourced assumptions; weekly report; calendar of interviews; profile completeness checks; export; offline PWA; one-tap open of the listing; analytics of what works (real, not invented).
### SIR Laptop Manager
Disk report and safe cleanup with undo; startup manager with reversible disable; process and memory advisor; health score; thermals and battery history; scheduled tasks overview; shortcut doctor; Windhawk mods manager and improved mods in a copy; macOS look pack with one-click restore; driver and update advisor; backup status; local RAG over the owner's files; agent config sync across CLIs; notifications; a clean installer and a tray app; Android/iOS companion later.
### SIR Control Room
Live status of every project from git, CI and reports; attention queue that is always true; portfolio health score; per-project timelines; GitHub status; usage and quota panel (Claude, Antigravity); phone-friendly layout; Arabic brief generator; search; weekly health report; SIR AI plan (docs): Telegram bot, mobile apps, laptop control, CLI agents, subscriptions.
