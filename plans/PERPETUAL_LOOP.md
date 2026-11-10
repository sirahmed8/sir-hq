# PERPETUAL LOOP: agents do not stop, usage stops them (Ahmed, 2026-11-08)

Ahmed wants a real engineering team, not instruction followers: the agents keep finding and fixing problems nobody told them about (UI, UX, animation, code, security, speed, copy), project by project, until each project is perfect. Only usage limits stop the work. He wants to say "wow, how did you find that bug" and "finally, you fixed it without me telling you".

> Status 2026-11-10: low-usage mode (`LOW_USAGE_MODE.md`) limits this loop to one cycle per day per project and at most 2 chats at once until the owner or HQ ends it. When Antigravity quota is out, the same cycle runs on the free CLI agents (`CLI_AGENT_INSTRUCTIONS.md`). Screenshots at 320, 390, 768, 1280 and 1920 px as in `D:/Projects/GEMINI.md`.

## The cycle (one Antigravity chat runs up to 3 cycles, then hands over with a fresh chat)
1. **Read state:** the project's AGENTS.md, `.sir/CHECKPOINT.md`, TASKS.md, last 20 commits, the previous cycle's report in `ops/agy-runs/reports/`.
2. **Run it for real:** start the app, open it in the browser (SIR Autonomy / browser tools), click through every screen and flow at 390 px and desktop, light, dark, high contrast, RTL, offline, slow network, with an empty account and a full one. Use dummy data for private projects.
3. **Audit through a different lens each cycle** (never repeat the same lens twice in a row): pixel-level polish (alignment, spacing grid, colour mismatches, cropped or clipped parts) · motion (timing, jank, double toggles, flicker, backdrop and sheet behaviour, spring physics) · UX friction (dead clicks, duplicated controls, unclear states, anxiety, too many steps) · all five UI states per view (idle, loading skeleton, empty, error with retry, overflow) · accessibility (keyboard, focus rings, labels, contrast, reduced motion) · responsiveness 320 px to 4K and zoom 80 to 200 percent · copy (plain words, no hype, no em dashes, bilingual correctness) · security (auth, rules, injection, secrets, privacy) · performance (Lighthouse, bundle, memory, battery) · code quality (duplication, dead code, types, file size, tests, flaky tests) · data integrity and offline behaviour · comparison with the best apps in the category and the plan's benchmark: add what is missing.
4. **Pick the top five by impact,** fix each at the root (not a patch), with a test where possible and a before and after screenshot. Commit locally in small commits with clear messages.
5. **Adversarial pass:** try to break your own fixes (rapid taps, rotate, resize, kill network, bad input, back button) and fix what breaks.
6. **Report** to `ops/agy-runs/reports/<name>.md`: what was fixed, evidence, a section "Found without being told" (bugs the owner never mentioned), what is still weak, the next lens. Update the project checkpoint and TASKS.md with the real state.
7. **Never conclude "nothing left".** If a lens finds nothing, widen the benchmark, test on another device size, break it with hostile input, read the code for the next refactor. A cycle may end only by: usage limit reached, 3 cycles completed, or a true blocker (sign-in, 2FA, CAPTCHA, payment). Then write the handoff and signal.

## Manager loop (Claude, Sonnet high, reviewer)
- Start a batch of loop chats (one per active project, at most 5 at once; 2 while low-usage mode is on) with `scripts/agy-task.py` and the queued "continue" line. The batch watcher wakes me once.
- Review every report completely: diff, tests, on-screen check of the riskiest change. Approve and push to main, or write a fix brief. Look for the "Found without being told" section: ask for more of that.
- Immediately queue the next cycle for the same project with the next lens (copy `ops/briefs/loop-<project>.md`, change the lens line), plus new projects when a project meets the definition of done.
- Keep my own turns few: one review turn per batch. Delegate screen work to Haiku (low effort). Check Antigravity usage at batch boundaries; below 15 percent of the 5-hour window, stop starting chats until the reset time, then resume.

## A project is done only when
Verified (tests, lint, types, e2e on screen), deployed and checked live, built for every platform its plan lists, legal and security checks green, accessible, fast, bilingual, nothing in its task list, three consecutive audit cycles found nothing worth fixing, and a fresh reviewer agrees. Then the next project in the wave order starts and the finished one gets a maintenance cycle once a week.

## Order of projects
AHome, SIR Study (coaching only, exam weeks first), SIR Jobs, SIR Laptop Manager, then SIR AI (Ahmed, 2026-11-08: Jarvis for his laptop: Telegram bot, iOS and Android apps, manage the laptop and every CLI agent, subscriptions for users; important, starts right after the current projects), then SIR Life, SIR Content Creation Studio, SIR Business, SIR Hagoozat, SIR Obour Hub, SIR ModPack, SIR Mods for GTA V, SIR Platform, SIR Portfolio, SIR Controller (optional, last). SIR Negm Furniture is plans only. Source of truth for the order: `plans/WAVE_STUDY.md`.
