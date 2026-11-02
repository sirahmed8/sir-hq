# Premium code bar (every AI, every project, every CLI)
Older or weaker models write dated, template-looking code. This file is the floor. If your output looks like a plain HTML page from 2015, redo it.
- Stack: current stable versions (Next.js 15+ App Router, React 19, TypeScript strict, Tailwind v4 tokens, FastAPI + Pydantic v2, Tauri v2/Electron + Vite). Check the project's package.json first and match it; never downgrade or add a second framework.
- Structure: layered (presentation, domain, data, core), files under 300 lines, no god components, absolute imports, typed everything, no `any`.
- UI: design tokens, themes (light, dark, system, high contrast), spring motion, RTL-first with logical CSS properties, real icons, glass or tonal surfaces per the project's design engine, no emoji headers, no gradient hero text, no pill-everything, five states on every screen (idle, loading skeleton, empty with one action, error with retry, populated), 44 px touch targets, 120 Hz-safe animation (transform and opacity only).
- Content: nothing hard-coded that belongs to the user (names, memories, dates, photos): it comes from the data store; neutral empty states; no fake numbers, reviews or users.
- Security: no secrets in git, server-side checks, rate limits, input validation, privacy of the people first.
- Proof: tsc, eslint, tests and the project's verify command green before any 'done'; screenshots for UI; commit small and push straight to main (no pull requests).
- Continue: read `.sir/CHECKPOINT.md` of the project (or `_SIR/ops/HQ_CHECKPOINT.md` for HQ), then `.sir/PLAN.md`, `.sir/TASKS.md`, `.sir/PREMIUM.md` and `DESIGN.md` if present; continue from 'Next step'; update the checkpoint after every step.
