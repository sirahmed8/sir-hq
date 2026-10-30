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
platform-kit (SIR Platform) · web-saas (Obour Hub, Hagoozat) · pos-desktop (Business) · desktop-engine (Content Creation Studio, SIR AI) · windows-tool (Controller) · internal-ops (Laptop Manager) · private-local (AHome, Jobs, Study) · static-site (Portfolio, Negm Furniture) · game-mod (ModPack, GTA mods) · selfhost-oss (Odysseus) · life-app (Life).

## Regenerate
`python plans/generate_plans.py` then `python plans/generate_kit.py`. The kit writer never touches `legacy/`, never overwrites a CHECKPOINT that a project chat has started, keeps existing README/SECURITY/.editorconfig, and replaces only the marked kit block in AGENTS.md. Edit the data files, not the generated output.

## Decisions made by HQ on 2026-10-30 (reversible)
- Odysseus: upstream-derived (AGPL-3.0), not Ahmed's main project. Source is copied in `SIR Odysseus/legacy/Odysseus app`; its repo `sirahmed8/odysseus` is left alone (no PRs reviewed or merged, not archived). SIR Odysseus stays separate from SIR AI because mixing AGPL code into proprietary SIR AI is a licence problem; they share ideas through documented APIs only (ADR in its ARCHITECTURE.md).
- Old repos: 18 renamed `sir-legacy-*` and archived (private); every new product has a new private repo. The public release repos (`SIR-*-Public`, `SIR-ModPack`) and the profile repo `sirahmed8` stay as they are because they hold download links. The ModPack private source repo is `sir-modpack-source` (the name `sir-modpack` is the public release repo).
- AHome keeps its own private repo and is never pushed from HQ.
