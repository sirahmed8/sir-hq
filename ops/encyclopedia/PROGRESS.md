# PROGRESS: r47 skills encyclopedia

Last updated: 2026-11-12 (worker: Devin CLI swe-2-flash-medium)

## Status: SCAN COMPLETE, INDEX + PLAN WRITTEN

All tasks in the brief are done for this pass:

- [x] Inventoried every skill source on the machine (see `SOURCES.md`): 11 skill roots + 42 gemini plugin dirs + workspace + builtin sets. Tools with no skills found documented (Goose, Cline, Kimi, Devin-user, Windsurf/Cursor MCP).
- [x] Generated one digest per installed skill copy: **1007 digest files** under `ops/encyclopedia/<tool>/<skill>.md` covering **385 unique skill names** (counts drifted +1/+1 during the run because `video-digest` was added to `~/.claude/skills` mid-session; re-running the scripts picks it up). Built by `build-encyclopedia.mjs` (re-runnable, deterministic).
- [x] `ops/SKILLS_INDEX.md`: table of all 385 unique skills (name, tools, category, purpose, digest link). Categories are keyword-heuristic; marked as such in the file header.
- [x] `ops/encyclopedia/ORGANIZATION_PLAN.md`: duplicates (codex/windsurf/cursor/opencode/kilo share a byte-identical 112-set; ~100 names have 3 divergent revisions across claude/codex-family/gemini-plugin), gaps, conflicts, per-worker recommendations, MCP/plugin inventory per tool, and a safe NOT-YET-EXECUTED sync plan with exact copy steps.
- [x] `ops/encyclopedia/mcp-inventory.json`: MCP server and plugin names per tool, secrets stripped.
- [x] Pointer added to `ops/CUSTOMIZATIONS_CATALOG.md`.

## How digests were made (and their limit)

`build-encyclopedia.mjs` reads each SKILL.md in full and extracts: frontmatter name/description/allowed-tools, all headings, trigger lines, risk-flagged bullets, up to 5 verbatim rule lines, and the file list inside each skill folder (with the first heading/line of each .md/.txt reference). It does NOT yet deep-read every script's full header or every reference file end-to-end; for the ~385 unique skills a human/agent pass can deepen any single digest on demand. Byte-identical copies across tools are written as short stubs pointing to the canonical digest. Gemini-plugin digests are named `<plugin>--<skill>.md` (with `--copyN` suffixes) because the same skill name ships inside several plugin dirs (netlify x3, twg-setup x2). Secret scan over all digests: no keys/tokens found.

## To resume / extend

- Re-run: `cd D:/Projects/_SIR/ops/encyclopedia && node build-encyclopedia.mjs && node gen-index.mjs`
- Add a tool: append `{ tool, dirs }` to `SOURCES` in build-encyclopedia.mjs.
- Next valuable step (needs HQ): per-skill diff of the ~100 divergent names to pick canonical revisions (list derivable from `index.json` hashes), then execute section 8 of ORGANIZATION_PLAN.
- Optional deepen pass: for the ~25 "SIR core" skills, hand-write richer digests replacing the auto ones.

## Files in this folder

- `build-encyclopedia.mjs` — scanner/digest generator
- `extract-configs.mjs` — MCP/plugin name extractor (names only)
- `gen-index.mjs` — SKILLS_INDEX.md + SOURCES.md generator
- `index.json` — machine-readable index of all 1007 copies
- `mcp-inventory.json` — MCP servers/plugins per tool
- `SOURCES.md`, `ORGANIZATION_PLAN.md`, `PROGRESS.md`
- `<tool>/<skill>.md` — 1007 digests (12 tool dirs incl. gemini-plugin with `<plugin>--<skill>` names)
