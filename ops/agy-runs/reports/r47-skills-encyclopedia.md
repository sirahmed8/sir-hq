# Report: r47-skills-encyclopedia

Worker: Devin CLI (swe-2-flash-medium). Date: 2026-11-12. Repo: `D:/Projects/_SIR` (sir-hq). Commits: `a76c925` (encyclopedia), `0eb2acc` (checkpoint + bus). Both pushed to `main`.

## What was done

Built the complete skills encyclopedia the brief asked for, covering every skill/plugin/MCP definition found on the machine. Because the corpus is ~1000 installed copies, I wrote deterministic generator scripts (kept in `ops/encyclopedia/`, re-runnable by the next worker) instead of hand-writing 1000 files; every SKILL.md was read in full by the generator and digests carry verbatim rule lines, headings, file lists, risk flags, MCP mentions and frontmatter.

### Sources verified (details in `ops/encyclopedia/SOURCES.md`)

| Source | Found |
|---|---|
| `~/.claude/skills` | 72 skills (73 dirs; `video-digest` was added mid-run) |
| `~/.codex/skills` | 113 |
| `~/.codeium/windsurf/skills` | 112 |
| `~/.cursor/skills` | 112 |
| `~/.config/opencode/skills` | 112 |
| `~/.config/kilo/skills` | 112 |
| `~/.agents/skills` | 1 (`agent-reach`) |
| `~/.gemini/skills` | 57 (mostly GCP/data) |
| `~/.gemini/antigravity/builtin/skills` | 13 |
| `~/.gemini/antigravity/scratch/skills` | 1 |
| `~/.gemini/config/plugins/*/skills` | 301 SKILL.md inside 42 plugin dirs |
| `D:/Projects/.agents/skills` | 1 (`sir-session-end`) |
| Project `.claude/.agents/.sir` skill folders | none (they hold `agents/` subagent defs, not SKILL.md) |
| `D:/Projects/AHome` | NOT opened (private) |

Tools with no skill store found (documented): Goose (binary only, no config), Cline (data/tasks only), Kimi Code (config.toml providers/models only), Devin user dir (builtin skills only), Windsurf/Cursor MCP configs absent.

### Outputs

- `ops/encyclopedia/<tool>/<skill>.md` — **1007 digest files**, each with: what it does, when to use, structure/headings, tools/MCPs needed, risks, 3-5 verbatim key rules, files inside the skill. Byte-identical copies are stubs pointing to the canonical digest. Gemini-plugin digests use `<plugin>--<skill>.md` names.
- `ops/SKILLS_INDEX.md` — 385 unique skills, one table (name, tools, category, purpose, digest link). Categories are keyword-heuristic, flagged as such.
- `ops/encyclopedia/SOURCES.md` — per-source inventory + MCP summary.
- `ops/encyclopedia/ORGANIZATION_PLAN.md` — duplicates, gaps, conflicts, per-worker skill recommendations (free CLI workers + Haiku agents), MCP servers/connectors and plugins per tool, and a safe NOT-executed sync plan with exact copy steps.
- `ops/encyclopedia/mcp-inventory.json` — MCP server and plugin names per tool, secrets stripped.
- `ops/encyclopedia/index.json`, `PROGRESS.md` — machine index + resume notes.
- `ops/CUSTOMIZATIONS_CATALOG.md` — pointer to the new index added at top.
- Scripts: `build-encyclopedia.mjs`, `extract-configs.mjs`, `gen-index.mjs`.

## Key findings

- codex/windsurf/cursor/opencode/kilo hold a **byte-identical 112-skill set** (content-hash verified). Any sync must hit all five or none.
- **~100 skill names exist in 3 divergent revisions**: Claude's `~/.claude/skills`, the shared 112-set, and gemini-plugin copies (e.g. all `firebase_*`, `karpathy-skills`, `master-production-directive`). Canonical pick needed before syncing (proposed in ORGANIZATION_PLAN section 8).
- Claude lacks the entire Vercel/Google-plugin skill family that the other tools have; Gemini plugins hold 269 unique skill names nothing else has.
- MCP: only OpenCode/Kilo (`nvidia-app`) and the Google stack (Gemini CLI + Antigravity, ~30 servers) are configured; Claude gets MCP via its 84 installed plugins; Devin/Kimi/Cline/Goose/Windsurf/Cursor have none found.
- `D:/Projects/.mcp.json` and `.agents/mcp_config.json` still list `AgentsRoom-*` servers though AgentsRoom was retired 2026-11-08 — flagged as stale, not removed.
- `CUSTOMIZATIONS_CATALOG.md` previously catalogued only the Gemini plugin set; now points to the complete index.
- Secret scan over all 1007 digests (sk-, AIza, ghp_, JWT, PEM patterns): clean.

## Commands run (real output)

- `node build-encyclopedia.mjs` → `processed=1007 uniqueNames=385` (per-tool counts listed above; re-run after collision fix).
- `node extract-configs.mjs` → `written mcp-inventory.json`.
- `node gen-index.mjs` → `SKILLS_INDEX rows=385, digests=1007`.
- `grep -rInE "(sk-…|AIza…|ghp_…|BEGIN…)" ops/encyclopedia` → no matches.
- `git add ops/encyclopedia ops/SKILLS_INDEX.md ops/CUSTOMIZATIONS_CATALOG.md` → commit `a76c925`; `git push origin main` → `5aa127c..a76c925` then `a76c925..0eb2acc`.
- CI: not applicable — `_SIR` repo; GitHub Actions quota flag `ops/ci-quota-exhausted.flag` exists (rule 18), docs/data-only change, local verification = the generator runs above all green.

## What is unsure / open

- Digest depth: SKILL.md files are read in full, but scripts/references inside each skill are listed with first-line notes, not fully digested. `PROGRESS.md` documents how to deepen any single digest; a per-skill hand pass for the ~25 SIR core skills is the suggested next step.
- SKILLS_INDEX categories are heuristic; spot-check before relying on them for routing.
- Whether Devin CLI reads a user skills dir (`~/.config/devin/skills` or project `.devin/skills`) is unverified — flagged as an open question in the plan.
- The ~100 divergent skill revisions need a diff review to pick canonicals (suggested: haiku subagent batch).
- Windsurf and Cursor may be unused tools; their 112-copy sync need is an HQ decision.

## Recommended next

1. HQ picks canonical revisions for divergent skills (data already in `index.json` hashes).
2. Execute ORGANIZATION_PLAN section 8 in small batches, re-running the two generator scripts after each.
3. Hand-deepen digests for the SIR core set listed in the plan.
