# NEXT (read this first; updated 2026-10-29 late) 
The program: rebuild every product as a new SIR project (see `plans/MASTER_REBUILD_PLAN.md`). Agents run everything; only the last section needs Ahmed.

## Done
- AHome renamed, 5.9 GB freed, 3 routines registered, Moodle automation quarantined (75 files, task disabled), consolidation (Merged sites -> Hagoozat Elite, 11Players and EGFootball5 -> old projects).
- 16 inventories + scores + TickTick map; five security fixes pushed as PRs (all re-tested, reviewed once; merge script ready).
- Master rebuild plan, 15 detailed product plans (`plans/*.md`), 10 new folders with plan + agent files: SIR Platform, SIR Business, SIR Life, SIR Hagoozat, SIR Obour Hub, SIR Home, SIR Laptop Manager, SIR Jobs, SIR Negm Furniture, SIR Odysseus.

## Next, in this order
1. Protect live users (old repos): rotate keys (Google AI Studio, OpenRouter) in Ahmed's Chrome, fix failing GitHub Actions (SIR-Controller build, sir-content-creation-studio CI, odysseus CI + Container scan, antigravity-agent-suite CI), merge the 5 PRs (script) , leftovers listed below.
2. SIR Platform M0-M2: owner-auth, signed-webhook, ai-proxy, billing fallback, legal-pack, ui kit, project-kit (plan: `plans/sir-platform.md`).
3. SIR Obour Hub M0-M6 (first product; proves Cloudflare + new Firebase project + login brand check).
4. SIR Hagoozat, then SIR Business (Restaurant mode first).
5. SIR Content Creation Studio, SIR Controller (+Optimizer), SIR AI.
6. SIR Home (rename last, daemons stopped), SIR Laptop Manager, SIR Jobs.
7. SIR ModPack, SIR Mods for GTA V, SIR Odysseus, SIR Negm Furniture, SIR Life.
8. Not done yet and must not be forgotten: the benchmark against the best apps for each product (Phase 3.6, do it at each product's M0), parity test of the SIR setup in Antigravity/OpenCode/Kilo, test of the agent-config sync script on a temp workspace, Wave 0 leftovers (below), legal truthful-claims sweep on the OLD live sites, x360ce App (listed in TickTick, no folder found).

## Wave 0 leftovers (go into the rebuilds or old repos, whichever comes first)
- Webhooks: timestamp inside the signed payload; native Stripe/Paymob formats; idempotent activation.
- SIR AI: portal chat sends no bearer so the owner is metered; tokeninfo audience check; X-Forwarded-For on support quota; OwnerManager hard-coded list; untrack `.env.production` in GTA V; SIR Optimizer: firebase-admin + verifyIdToken, public /transactions and /metrics reads.

## Only Ahmed can do
- Run `pwsh -NoProfile -File D:\Projects\_SIR\scripts\merge-approved-prs.ps1` (5 merges; Optimizer and SIR AI deserve one quick second look).
- Move passwords out of the TickTick notes into a password manager; change the Moodle password.
- When asked: be logged in to Google AI Studio and OpenRouter in Chrome; create the Paymob/Fawry accounts when ready (billing stays "Launching Soon" until then).
