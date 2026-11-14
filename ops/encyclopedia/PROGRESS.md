# PROGRESS: r47 skills encyclopedia & canonical sync

Last updated: 2026-11-14 (Antigravity / Gemini worker)

## Status: CANONICAL SYNC & ENCYCLOPEDIA REFRESH COMPLETE

### Completed in 2026-11-12 deep-read pass (r47, Kilo)

- [x] Inventoried skill sources (see `SOURCES.md`), generated initial 1007 digest files across 385 unique skill names, deepened 317 skills in `ops/encyclopedia/deep/`, and published `ORGANIZATION_PLAN.md` + initial `mcp-inventory.json`.

### Completed in 2026-11-14 sync & refresh pass

- [x] **Claude-only sync**: Copied the 9 existing Claude-only skills (`accidental-data-loss-prevention`, `firestore-data`, `imagegen`, `nextjs`, `review-agent`, `shadcn`, `skill-installer`, `social-creator-studio`, `video-digest`) from `~/.claude/skills/` into `~/.gemini/config/skills/`, `~/.config/opencode/skills/`, and `~/.config/kilo/skills/`. Skipped 3 absent in Claude (`next-forge`, `next-upgrade`, `turbopack`, already present in Codex/OpenCode/Kilo).
- [x] **Canonical SIR core staging**: Populated `ops/encyclopedia/canonical/` with all **27 SIR core skills** (26 canonicalized from `~/.claude/skills/` for full trigger descriptions; `modern-web-guidance` canonicalized from `modern-web-guidance-plugin` 2026-11-13 revision) and synced them to `~/.gemini/config/skills/`, `~/.config/opencode/skills/`, and `~/.config/kilo/skills/`.
- [x] **`sir-worker-preamble` skill created**: Authored `SKILL.md` packaging `ops/WORKER_PREAMBLE.md` and `standard/23-premium-code-bar.md` in `~/.gemini/config/skills/sir-worker-preamble/` and `D:/Projects/.agents/skills/sir-worker-preamble/`, plus deep digest `ops/encyclopedia/deep/sir-worker-preamble.md`.
- [x] **Retired AgentsRoom MCP cleanup**: Removed 5 `AgentsRoom-*` entries from `D:/Projects/.mcp.json` and 4 from `D:/Projects/.agents/mcp_config.json` (preserving `everything-app`, `100hires`, `0bridge`); archived-verified and removed `D:/Projects/.agentsroom` (270 retired state files already backed up in `SIR AI/legacy/agentsroom/project-state/`).
- [x] **Encyclopedia & MCP inventory rebuilt**: Added `gemini-config` (`~/.gemini/config/skills`) to `build-encyclopedia.mjs`, fixed `gen-index.mjs` relative links, fixed `extract-configs.mjs` (JSONC comment stripping, `codex` TOML, `claude` v2 `installed_plugins.json`, `devin` MCP/skills, `workspaceMcp`), and refreshed `index.json` (**421 unique skill names**, **1219 installed copies**), `SKILLS_INDEX.md`, `SOURCES.md`, `mcp-inventory.json`, and `CUSTOMIZATIONS_CATALOG.md`.

## How digests work

`build-encyclopedia.mjs` reads each `SKILL.md` in full and extracts frontmatter (`name`, `description`, `allowed-tools`), headings, trigger lines, risk-flagged bullets, up to 5 rule lines, and internal file lists. `propagate-deep.mjs` then merges hand-reviewed deep digests from `ops/encyclopedia/deep/` across all tool folders (389 deep digests covering 1128 digest files; 3 pre-existing AlloyDB deep files remain unmatched because those skills do not exist on disk). Gemini-plugin digests use `<plugin>--<skill>.md` names because plugins share names (`netlify` x3, `twg-setup` x2).

## To resume / extend

- Re-run after any skill change: `cd D:/Projects/_SIR/ops/encyclopedia && node build-encyclopedia.mjs && node gen-index.mjs && node propagate-deep.mjs && node extract-configs.mjs`
- Add a tool root: append `{ tool, dirs }` to `SOURCES` in `build-encyclopedia.mjs` and add its row in `gen-index.mjs`.
- Deepen remaining skills (including the newly synced `sir-worker-preamble` neighbors or new plugin skills): add `ops/encyclopedia/deep/<skill>.md` and run `node propagate-deep.mjs`.

## Files in this folder

- `build-encyclopedia.mjs` - scanner and digest generator (13 sources incl. `gemini-config`)
- `extract-configs.mjs` - MCP and plugin name extractor (secrets stripped)
- `gen-index.mjs` - `SKILLS_INDEX.md` and `SOURCES.md` generator
- `propagate-deep.mjs` - propagates `deep/` digests to all tool digest folders
- `canonical/<skill>/` - 27 canonical SIR core skill directories
- `deep/<skill>.md` - 389 deep-read digests (source of truth for digest bodies)
- `index.json` - machine-readable index of all 1219 installed skill copies
- `mcp-inventory.json` - MCP servers and plugins per tool + workspace MCP
- `SOURCES.md`, `ORGANIZATION_PLAN.md`, `PROGRESS.md` - source map, sync plan, and status
- `<tool>/<skill>.md` - 1219 per-tool digests across 13 tool directories
