# PROGRESS: r47 skills encyclopedia

Last updated: 2026-11-12 (worker: Kilo)

## Status: DEEP-READ PASS COMPLETE

All tasks in the brief are done for this pass:

- [x] Inventoried every skill source on the machine (see `SOURCES.md`): 11 skill roots + 42 gemini plugin dirs + workspace + builtin sets. Tools with no skills found documented (Goose, Cline, Kimi, Devin-user, Windsurf/Cursor MCP).
- [x] Generated one digest per installed skill copy: **1007 digest files** under `ops/encyclopedia/<tool>/<skill>.md` covering **385 unique skill names**. Built by `build-encyclopedia.mjs` (re-runnable, deterministic).
- [x] **Deep-read pass completed**: 317 skills deep-read from SKILL.md + scripts/references headers end-to-end; written to `ops/encyclopedia/deep/` and propagated to all 853 tool-specific digest files (replacing auto-generated stubs). Every digest now has: Summary, When to use/when NOT, Inputs/outputs/tools, 5 key rules, Risks/owner notes, Category/tags, Revisions.
- [x] `ops/SKILLS_INDEX.md`: table of all 385 unique skills (name, tools, category, purpose, digest link). Categories are keyword-heuristic; marked as such in the file header.
- [x] `ops/encyclopedia/ORGANIZATION_PLAN.md`: duplicates (codex/windsurf/cursor/opencode/kilo share a byte-identical 112-set; ~100 names have 3 divergent revisions across claude/codex-family/gemini-plugin), gaps, conflicts, per-worker recommendations, MCP/plugin inventory per tool, and a safe NOT-YET-EXECUTED sync plan with exact copy steps.
- [x] `ops/encyclopedia/mcp-inventory.json`: MCP server and plugin names per tool, secrets stripped.
- [x] Pointer added to `ops/CUSTOMIZATIONS_CATALOG.md`.

## How digests were made (deep-read pass)

`build-encyclopedia.mjs` reads each SKILL.md in full and extracts: frontmatter name/description/allowed-tools, all headings, trigger lines, risk-flagged bullets, up to 5 verbatim rule lines, and the file list inside each skill folder (with the first heading/line of each .md/.txt reference). The deep-read pass (`propagate-deep.mjs`) then reads each skill's SKILL.md and all scripts/references files end-to-end, hand-writes a comprehensive digest with Summary, When to use/when NOT, Inputs/outputs/tools, 5 key rules, Risks/owner notes, Category/tags, Revisions, and propagates it to all tool folders where that skill exists. 317 skills deepened (including all 27 SIR core skills + 290 others); byte-identical copies across tools now share the same deep content. Gemini-plugin digests are named `<plugin>--<skill>.md` (with `--copyN` suffixes) because the same skill name ships inside several plugin dirs (netlify x3, twg-setup x2). Secret scan over all digests: no keys/tokens found.

## To resume / extend

- Re-run: `cd D:/Projects/_SIR/ops/encyclopedia && node build-encyclopedia.mjs && node gen-index.mjs`
- Add a tool: append `{ tool, dirs }` to `SOURCES` in build-encyclopedia.mjs.
- Next valuable step (needs HQ): per-skill diff of the ~100 divergent names to pick canonical revisions (list derivable from `index.json` hashes), then execute section 8 of ORGANIZATION_PLAN.
- Deepen more skills: add deep digests to `ops/encyclopedia/deep/` and run `node propagate-deep.mjs`.

## Files in this folder

- `build-encyclopedia.mjs` — scanner/digest generator
- `extract-configs.mjs` — MCP/plugin name extractor (names only)
- `gen-index.mjs` — SKILLS_INDEX.md + SOURCES.md generator
- `propagate-deep.mjs` — propagates deep digests to all tool folders
- `index.json` — machine-readable index of all 1007 copies
- `mcp-inventory.json` — MCP servers/plugins per tool
- `SOURCES.md`, `ORGANIZATION_PLAN.md`, `PROGRESS.md`
- `deep/<skill>.md` — 317 deep-read digests (source of truth)
- `<tool>/<skill>.md` — 1007 digests (12 tool dirs incl. gemini-plugin with `<plugin>--<skill>` names), now all deep-content where available