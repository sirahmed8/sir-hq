# QUALITY PLAYBOOK FOR ANY AI AGENT (written so a smaller model still produces premium work; updated 2026-11-10)

Use this when the agent is not a top model (for example Gemini in Antigravity, OpenCode, Kilo, Devin CLI, ZCode, Codex). After 2026-11-23 that is every agent. The short checklist for chats is `D:/Projects/GEMINI.md`; the design contract is `GEMINI_QUALITY_CHARTER.md`. The goal is the same quality as the best models: correct, secure, tested, accessible, beautiful, and boring to maintain.

## How to work (always, in this order)
1. **Read before writing.** Read the README, `AGENTS.md`, the plan and the task list of the project. Open the files you will change and one finished file of the same kind. Never guess a file name, function or command: search for it.
2. **Write the plan in 5 lines** in the checkpoint file: goal, approach, files to change, how to prove it works, risks.
3. **One small task at a time.** Finish it completely (code, tests, docs, check on screen) before starting the next. If a task needs more than about 150 lines of change, split it.
4. **Prove it.** Run the project's verify command (typecheck, lint, tests, build) after every task. Fix every error. Never mark a task done while anything is red. Show the command output.
5. **Look at it.** For anything visual, open the page in a browser or the app and take a screenshot at 320, 390, 768, 1280 and 1920 px, in light and dark, left-to-right and right-to-left (at most 6 screenshots per check: pick the riskiest screens). Check there is no horizontal scrollbar. Fix what looks wrong.
6. **Review yourself as a stranger.** Before finishing, re-read your diff and ask: what breaks with empty data, a slow network, a very long text, a wrong input, two clicks at once, a screen reader, Arabic?
7. **Commit small, clear commits** (type: what). Update the checkpoint file with what is done and the exact next step.

## Code rules
- Strict TypeScript (no `any`), validate every input at the boundary (zod), small files (under 300 lines), one job per file, clear names, no copy-paste, no dead code, no TODO left behind.
- Never invent data: no fake reviews, users, numbers, testimonials or placeholder text. If real content is missing, show an honest empty state and list what is needed.
- Secrets never go in git or in the browser bundle; use environment variables and keep an `.env.example` with names only. Admin and owner checks happen on the server.
- Every screen has five states: first use, loading (skeleton), empty (with one clear action), error (human message plus Retry), and populated (works with 1 and with 10,000 items).
- Accessibility: keyboard works everywhere, visible focus, labels on every control, contrast at least WCAG AA, touch targets at least 44 px, respect reduced motion.
- Internationalisation: every string goes through the translation layer; Arabic uses right-to-left with CSS logical properties; dates and numbers use `Intl`.
- Performance: images in modern formats with sizes, no layout shift, lazy load below the fold, Lighthouse 95 or more on mobile for public pages.
- Design: one accent colour used sparingly, a real type pairing, spacing on a 4/8 grid, motion that is short and meaningful, no gradients as decoration, no emoji as icons, no stock-photo filler.
- Copy: plain, specific and honest. No hype words (revolutionary, seamless, cutting-edge), no em-dashes.

## When stuck
- Do not say "I can't". Try another route: search the docs, read the error fully, check the tools and connectors you have, try the browser, try a smaller version of the task, try a different library only if the current one is truly the problem.
- If something needs a person (sign-in, payment, a code sent to a phone), do everything around it, write the single remaining step in the checkpoint, and continue with the next task.

## Definition of done for any task (with evidence)
Every line needs proof saved in `.sir/evidence/` or pasted in the report. No proof means not done.
1. Code written, tests added and passing. Proof: the verify command and the last lines of its output.
2. Checked on screen at five widths in light, dark, LTR and RTL. Proof: file names of the screenshots.
3. No console errors. Proof: the console log is empty after using the feature.
4. Five states handled (first use, loading, empty, error with Retry, populated).
5. Docs and checkpoint updated, committed, pushed to `main` (no pull requests), GitHub check green.
6. The report lists what you did NOT verify. Writing "not verified" is allowed; claiming without proof is not.

## Examples of vague versus concrete (read these twice)
- Vague: "make it responsive". Concrete: "at 320 px the two action buttons wrap under the title with a 12 px gap and no horizontal scroll".
- Vague: "add tests". Concrete: "add tests for empty list, one item, 10,000 items, and a failed fetch with Retry".
- Vague: "fix the UI". Concrete: "the tab bar flashes a white outline on switch; remove the focus ring flash by using `:focus-visible` and a 2 px token-colour ring".
- Vague: "it works". Concrete: "I opened /jobs at 390 px, added a job, reloaded, and it was still there (screenshot jobs-390.png)".

## Hand over when quota ends
Do this at the first quota warning, not after the cut. Clean tree, run verify, commit, push, update `.sir/CHECKPOINT.md` (Now, exact Next step, Open promises, which tool and account), append one line to `_SIR/ops/MISSION_LOG.md`, write the report, run `python D:/Projects/_SIR/scripts/agy-done.py <task> ok "<line>"`, stop. Steps in full: `D:/Projects/GEMINI.md` section 6.
