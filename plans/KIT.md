# PROJECT KIT (what HQ prepares so each project chat can start building at once)

HQ is the manager: it prepares, it does not build. Ahmed opens one chat per project folder; that chat reads the kit and builds.

## What every project folder contains (generated 2026-10-30 by `plans/generate_kit.py`)
- `.sir/PLAN.md` the contract (mission, names, why rebuild, port list, screens, security, milestones M0-M6). `.sir/TASKS.md` the ordered T-NNN list built from the plan plus per-product kit tasks, each with an owner agent. `.sir/BOARD.md` the live board.
- `.sir/ARCHITECTURE.md` modules in build order, entity drafts, ADRs to write first. `DESIGN.md` seed colour, personality, signature interaction, motion and RTL rules. `PLATFORMS.md` state, reason and build/test tool for 17 platforms. `PRODUCTION.md` hosting, backups, monitoring, releases, production checklist. `QUALITY.md` definition of done. `BENCHMARK.md` research targets.
- `.sir/TEAM.md` the sub-agent roster with model and effort, spawn rules, delegation brief. `TOOLKIT.md` MCPs available now, skills to load, how to discover and vet more, CLIs to install.
- `.sir/project.yml`, `status.json`, `CHECKPOINT.md` (next step named exactly), `decisions/`, `evidence/`, `reports/`, `inbox/`.
- `.claude/agents/<slug>-pm.md` the Project Manager role; `.claude/commands/continue.md` and `end.md`.
- `AGENTS.md` (kit block), `CLAUDE.md` -> AGENTS.md, `GEMINI.md`, `README.md`, `SECURITY.md`, `.editorconfig`, hardened `.gitignore` (legacy/, materials/, secrets, keys).
- A private GitHub repo `sirahmed8/<repo>` with `origin` set and the kit pushed to `main`. No pull requests.

## Archetypes (data in `plans/kit_archetypes.py`, `kit_platforms.py`; per-product data in `kit_products_a.py`, `kit_products_b.py`)
platform-kit (the shared kit) · web-saas (Education Hub, Hagoozat) · pos-desktop (Business) · desktop-engine (Content Creation Studio, SIR AI) · windows-tool (Controller) · internal-ops (Laptop Manager) · private-local (AHome, Jobs, Study) · static-site (Portfolio, Negm Furniture) · game-mod (ModPack, GTA mods) · selfhost-oss (Odysseus) · life-app (Life).

## Regenerate
`python plans/generate_plans.py` then `python plans/generate_kit.py`. The kit writer never touches `legacy/`, never overwrites a CHECKPOINT that a project chat has started, keeps existing README/SECURITY/.editorconfig, and replaces only the marked kit block in AGENTS.md. Edit the data files, not the generated output.

## Decisions made by HQ on 2026-10-30 (reversible)
- Odysseus: upstream-derived (AGPL-3.0), not Ahmed's main project. Source is copied in `SIR Odysseus/legacy/Odysseus app`; its repo `sirahmed8/odysseus` is left alone (no PRs reviewed or merged, not archived). SIR Odysseus stays separate from SIR AI because mixing AGPL code into proprietary SIR AI is a licence problem; they share ideas through documented APIs only (ADR in its ARCHITECTURE.md).
- Old repos (updated later the same day on Ahmed's order): 18 renamed `sir-legacy-*` and archived, then the public release repos (`SIR-*-Public`, `SIR-ModPack`), `odysseus` and `laptop-manager` archived too: 30 archived. Archived public repos stay readable, so old download links keep working. Kept active: the 16 new private repos, `ahmed-and-habiba-sanctuary` (AHome), `sir-hq`, `sir-backups` and the profile repo `sirahmed8`. The ModPack private source repo is `sir-modpack-source`.
- AHome keeps its own private repo and is never pushed from HQ.

## Mods installed for every chat (user scope, source in `_SIR/mods/`, marketplace `sir-mods`)
- **sir-control-room**: pane beside the chat with every project's wave, task bar and next task; reads each `.sir/TASKS.md` every 30 seconds, so it updates by itself as project chats tick tasks. `/sir` opens it. AHome shows counts only.
- **sir-guards**: stops `gh pr create`, stops deleting any `legacy` folder, and keeps AHome's files out of every chat not opened in the AHome folder. Tested (`claude plugin test`).
- **sir-context**: adds a short section to every chat's system prompt (main plan path, this project's wave, task count, next task, unread inbox count, Ahmed's rules), so every chat knows the plan without being told.
- Inbox: `ops/bus/<slug>.md` per project plus `ops/bus/all.md`; the Control Room pane and status line show unread counts. Live chat-to-chat talk uses ListAgents and SendMessage.
- Update a mod: edit the folder, then `/reload-plugins`. Add one: put it under `_SIR/mods/`, list it in `.claude-plugin/marketplace.json`, `claude plugin marketplace update sir-mods`, `claude plugin install <name>@sir-mods`.
- Already covered elsewhere, so not built as mods: the checkpoint reminder on Stop (existing `scripts/memory/stop-guard.mjs` hook), the per-project status line (inside sir-control-room), the plan digest (sir-context). Next ideas: a per-project pane mod made by the project chat that needs one (for example a booking calendar view for Hagoozat).

## Studied wave order and deep scan
`plans/WAVE_STUDY.md` ranks projects (AHome first, then quick cash, then paying products, then internal tools). Every project's first M0 task is a deep scan of `legacy/` (never deleted before M6) and of the plan, written to `.sir/reports/deep-scan.md`, followed by a plan upgrade.
