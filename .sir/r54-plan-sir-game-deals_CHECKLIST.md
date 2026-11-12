# Round checklist: r54-plan-sir-game-deals

Task: write the premium plan for SIR Game Deals (slug `sir-game-deals`) as its own small independent product. Brief: `D:/Projects/_SIR/ops/briefs/r54-plan-sir-game-deals.md`. Output only under `D:/Projects/_SIR` (plans and ops folders).

- [x] Read the manual, the brief, the workspace laws, `standard/OWNER_DEFAULTS.md`, `plans/PRODUCT_DIRECTION_2026-11-12.md` (sections 6 and 8), `ops/briefs/r52-product-premium-plan.md`, `plans/SHARED_PLATFORM_KIT.md` and `ops/SKILLS_INDEX.md`
- [x] Rescan rule: read every existing note about the idea (`plans/sir-deals.md`, `plans/PRODUCT_DIRECTION_2026-11-12.md` section 8, `ops/TICKTICK_MAP.md` row "price and game-deal finder", `ops/IDEAS_INBOX.md`, the r51 and r52 briefs, `ops/briefs/r51-backlog-projects.md`) and check for any other mention under `plans/` and `ops/`
- [x] Market research on the web: 10 competitors with strengths, flaws and our edge, Egypt and the Arab market first, then global, every row with a dated source and a "(unsourced, verify)" tag where the page could not be opened
- [x] Own probes recorded (2026-11-12): Steam `appdetails` with `cc=EG` returns `$39.99 USD` while `cc=SA` returns `249.00 SR` and `cc=AE` returns `249.00 AED` (Steam has no Egyptian pound price); Steam app-list method not found; GG.deals and SteamDB answer a bot challenge (403); the FreeToGame API answers JSON
- [x] `plans/sir-game-deals.md` written: promise and end state, the ten competitors and our edge, features with the owner's own ideas and what is out of scope, platform matrix, architecture on the shared kit, the data model, the owner-only analytics page, AI with the fallback chain, the premium quality bar, free tier and fair EGP and USD pricing, M0 to M6 with acceptance tests, the first ten tasks, skills, risks, owner-only steps and sources
- [x] `plans/sir-game-deals.md` includes M0 = create `D:/Projects/SIR Game Deals` with `.sir/`, `AGENTS.md`, the repo `sirahmed8/sir-game-deals` and the Desktop folder kit (OWNER_DEFAULTS item 19)
- [x] `ops/competitors/sir-game-deals.md` written: the ten that matter with sources and dates, the second ring, what the market looks like, our edge as five promises, the sourcing tasks still open
- [x] `ops/briefs/sir-game-deals-tasks.md` written: the first ten tasks, each a title plus one paragraph brief, with the queue order, the dependencies and the file ownership
- [x] The project folder, the GitHub repo and the Firebase project were NOT created in this round (the brief forbids it)
- [x] No emoji, no em dashes in copy, version stated as 1.0.0, no fake users, prices, deals or countdowns
- [x] One line appended to `ops/bus/sir-hq.md`
- [x] `.sir/CHECKPOINT.md` updated with the worker note
- [x] The three explicit paths plus the round checklist committed and pushed to `main`
- [x] Report written to `ops/agy-runs/reports/r54-plan-sir-game-deals.md`
- [x] Done signal sent with `python D:/Projects/_SIR/scripts/agy-done.py r54-plan-sir-game-deals ok "<one line>"`
