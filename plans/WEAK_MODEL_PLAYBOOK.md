# QUALITY PLAYBOOK FOR ANY AI AGENT (written so a smaller model still produces premium work)

Use this when the agent is not a top model (for example Gemini high in Antigravity, OpenCode, Kilo, Codex). The goal is the same quality as the best models: correct, secure, tested, accessible, beautiful, and boring to maintain.

## How to work (always, in this order)
1. **Read before writing.** Read the README, `AGENTS.md`, the plan and the task list of the project. Open the files you will change and one finished file of the same kind. Never guess a file name, function or command: search for it.
2. **Write the plan in 5 lines** in the checkpoint file: goal, approach, files to change, how to prove it works, risks.
3. **One small task at a time.** Finish it completely (code, tests, docs, check on screen) before starting the next. If a task needs more than about 150 lines of change, split it.
4. **Prove it.** Run the project's verify command (typecheck, lint, tests, build) after every task. Fix every error. Never mark a task done while anything is red. Show the command output.
5. **Look at it.** For anything visual, open the page in a browser or the app, take a screenshot at phone width (390 px) and desktop width (1280 px), in light and dark, left-to-right and right-to-left. Fix what looks wrong.
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

## Definition of done for any task
Code written, tests added and passing, verify command green, checked on screen, no console errors, docs and checkpoint updated, committed.
