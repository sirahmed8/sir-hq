# Gemini quality charter (Ahmed, 2026-11-09)
Claude's subscription ends in about two weeks; after that Gemini in Antigravity works alone. Every chat works like a senior engineer, not like a fast typist. This is the contract.

## Before you touch code (every task)
1. Write a short plan in `<project>/.sir/plans/<task>.md`: goal in one sentence, every file you will touch, the steps in order, the acceptance checks (what I will see on screen), the risks. Keep a per-project master plan `<project>/.sir/MASTER_PLAN.md` with every feature, its state, and the next 10 tasks in detail (files, steps, acceptance). Update it every cycle.
2. Read the existing component or style that already solves the same problem. Reuse it. Never invent a second version of a button, select, tab bar, card, sheet, toast or form.

## While coding
3. One design system per project: tokens for colour, radius, spacing, motion; ONE component per control. Every dropdown looks like every other dropdown; every list, card and button follows the same spacing grid. If you find two versions, merge them.
4. Motion everywhere, all of it in the Dynamic Island style: springs (stiffness 300-400, damping 28-30), shared-element growth from the trigger, staggered lists 30-50 ms, press scale 0.98, respects reduced motion. No hard cuts, no hard black backdrops, no focus outline flashes on tab switches (no white outline glitches).
5. Layout is computed, never hand-placed: flex/grid with wrap, gaps and min/max sizes so buttons never overlap or leave their card at any width 320 px to 4K. Test every screen at 320, 390, 768, 1024, 1440, light/dark, RTL/LTR.
6. Tab bars: only the active tab shows its label, the others show their icon only; icons are consistent (one icon set). Every project has its own logo image: favicon, PWA/app icon and the image in the top bar (never a broken or generic icon).
7. No yellow buttons anywhere unless the project's own brand colour is yellow; buttons use the semantic palette (primary, neutral, danger, success).
8. No emoji, no technical words for the owner, plain simple Arabic and English, version stays 1.0.0.

## After coding (self-review checklist, written in the report)
9. Run it and watch it: screenshots before/after at 390 px and desktop; click every control you touched; keyboard only; offline; console clean; tests and verify green; GitHub green after push.
10. Re-read your diff as a stranger: dead code, duplicates, magic numbers, copy-paste, missing states (loading, empty, error, retry, populated). Fix before reporting.
11. Honest status: only say working what you saw working today.
