# ORGANIZATION_PLAN: skills, plugins and MCP servers across the SIR machine (r47, 2026-11-12)

Read-only analysis. Nothing here has been synced or changed. Data: `ops/encyclopedia/index.json`, `mcp-inventory.json`, `SOURCES.md`, `../SKILLS_INDEX.md`.

## 1. What exists, in one picture

| Tool | Skills | Where | MCP servers | Plugins |
|---|---|---|---|---|
| Claude Code (HQ) | 71 | `~/.claude/skills` | none in `~/.claude.json` | 84 installed (`~/.claude/plugins`) |
| Codex | 112 | `~/.codex/skills` | not checked deeply (CLI-managed) | none found |
| Windsurf | 112 | `~/.codeium/windsurf/skills` | none found (settings in protobuf) | none |
| Cursor | 112 | `~/.cursor/skills` | none (`~/.cursor` has no mcp.json) | none |
| OpenCode | 112 | `~/.config/opencode/skills` | `nvidia-app` only | none |
| Kilo | 112 | `~/.config/kilo/skills` | `nvidia-app` only | none |
| Shared `.agents` | 1 (`agent-reach`) | `~/.agents/skills` | n/a | n/a |
| Gemini CLI | 56 (mostly GCP/data) | `~/.gemini/skills` | Google stack + dev tools (see inventory) | shares `config/plugins` |
| Antigravity builtin | 13 | `~/.gemini/antigravity/builtin/skills` | same Google stack (`antigravity/mcp_config.json`) | n/a |
| Gemini plugins | 269 unique skill names inside 42 plugin dirs | `~/.gemini/config/plugins/*/skills` | per-plugin MCPs (figma, canva, linear, stripe, supabase, vercel, notion, postman, qodo, unity, invideo, netlify, atlassian, auth0, base44, context7, chrome-devtools, browse, firebase, flutter, gemini-api, google-developer-knowledge, google_maps_platform, gcalendar/gdocs/gdrive/gsheets/gslides/gmail via Google plugins, modern-web-guidance-plugin, multi-agent-orchestrator, reverse-engineering, sir-autonomy, sir-ecosystem, sir-ecosystem-suite, superpowers, advanced-engineering, creator-studio, android-cli-plugin, agent-reach) | the 42 plugins themselves |
| Workspace | 1 (`sir-session-end`) | `D:/Projects/.agents/skills` | workspace `.mcp.json` has stale AgentsRoom servers | n/a |
| Devin CLI | 2 builtin (`declarative-repo-setup`, `upload-secrets`) | built into binary | `descriptions.json` empty | none |
| Kimi Code | 0 | none | none (providers/models only in config.toml) | none |
| Cline | 0 | none | none found | none |
| Goose | 0 | none (binary installed, no config dir) | none | none |

384 unique skill names, 1004 installed copies (`index.json`).

## 2. Duplicates

- **The big replicated set**: codex, windsurf, cursor, opencode and kilo hold the SAME 112 skills, byte-identical inside the group (verified by content hash). One edit must be made 5 times or synced.
- **Claude vs the 112-set**: 71 of Claude's skills overlap by name with the shared set but with DIFFERENT content in ~100 cases (e.g. `karpathy-skills`, `modern-web-guidance`, all `firebase_*`, `gdrive`, `laptop-admin`). Claude's copies look like an older/different revision. This is the main divergence risk: two "versions" of the same skill with different rules.
- **Gemini plugin variants**: many shared-set names also exist inside gemini plugins with different content (e.g. `binary-reverse-engineer`, `direct-action-shield`, `emil-motion-impeccable`, `firebase_*`, `mimic-api-extractor`). Third variant of the same skill.
- Only 16 multi-tool names are byte-identical everywhere (`gcalendar`, `gdrive`, `meta-social-sidecar`, `modern-web-guidance` across claude+codex-family+gemini-plugin, etc.).

## 3. Gaps (skills one tool has that others lack)

- **Claude-only (not in the 112-set)**: `accidental-data-loss-prevention`, `agent-reach`(also in .agents), `firestore-data`, `github-gem-seeker`(actually shared), `imagegen`, `managing-python-dependencies`(also gemini), `master-production-directive`(also antigravity-scratch), `nextjs`, `open-seo-auditor`, `owasp-vulnerability-shield`, `production-engineering-standards`, `pulse-engineering`, `react-best-practices`, `repomix-token-optimizer`, `review-agent`, `shadcn`, `sir-ahmed-career-autopilot`, `sir-ecosystem-orchestrator`, `skill-installer`, `skills-discovery-engine`, `social-creator-studio`, `system-design-architect`, `taste-design-engine`, `vibe-auth-hardening`, `website-traffic-analytics`, `youtube-video-research`, `zero-trust-security-hardening`, `video-digest`, `gdocs`(windsurf-family has it? check index), `gsheets`, `gslides`, `google_maps_platform`, `gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`, `google-preferred-sources`, `knowledge-update`, `marketplace`, `memory-leak-debugging`, `music-prompter`, `next-forge`, `next-upgrade`, `retrieving-developer-knowledge`, `stock-analysis`, `troubleshooting`, `turbopack`, `typst-pdf-maker`, `verification`, `xcode_project_setup`, `debug-optimize-lcp`, `compose-preview`, `device-hub`, `env-vars`, `excel-generator`, `extension_to_functions_codebase`, `financial-analysis`, `chrome-extensions`, `chat-sdk`, `ai-gateway`, `ai-sdk`, `all-skills`, `auth`, `bootstrap`, `cookie-debugging`, `debug-optimize-lcp`, `deployments-cicd`, `knowledge-update` — i.e. the entire Vercel/Google-plugin skill family exists ONLY in the codex-family 112-set and gemini plugins, NOT in Claude's 71.
- **Gemini-only**: 56 GCP/data skills (alloydb, bigquery, cloud-sql, spanner, dataform, dbt, dataproc, composer, dataflow, etc.) and 269 plugin skills (unity, flutter, figma, canva, invideo, postman, qodo, atlassian, auth0, base44, stripe, supabase, netlify, shopify-ish, unreal, ui5...).
- **Antigravity builtin only**: `agy-customizations`, `antigravity_guide`, `automation`, `generative_ui`, `migrate-agent-settings`, `migrate-workflows`, `native_swarm`, `permissioned-github`, `plugin`, `run-workflow`, `scheduled-tasks`(?), `browser` subskills — 13 total.
- **Workspace only**: `sir-session-end`.
- **Missing everywhere useful**: no dedicated "SIR worker preamble" skill exists; workers get rules via `instructions` arrays in opencode.jsonc/kilo.jsonc and AGENTS.md, not via skills.

## 4. Conflicts

- Three divergent revisions of ~100 shared skills (claude / codex-family / gemini-plugin). Rule drift example: `firebase_*` skills exist in all three with different hashes; whichever an agent reads depends on the tool. Recommend picking ONE canonical revision per skill (see sync plan).
- `master-production-directive` exists in claude, codex-family AND `antigravity/scratch/skills` with 3 different hashes.
- Stale MCP entries: `D:/Projects/.mcp.json` and `.agents/mcp_config.json` still list `AgentsRoom-*` servers though AgentsRoom was retired 2026-11-08.
- `CUSTOMIZATIONS_CATALOG.md` claims "0 excluded skills, <65% token budget" but lists only the Gemini plugin set; it does not reflect the 112-skill codex-family set or Claude's 71.

## 5. Recommended skill set per worker

Free/cheap workers (from WORKFORCE.md + CLI_AGENT_INSTRUCTIONS.md):

| Worker | Should get | Why |
|---|---|---|
| Antigravity / Gemini (main builder) | Everything it already has: 56 gemini skills + 42 plugins + builtin 13. Add the SIR core set (below). | It is the primary builder; needs Google stack + design + security skills. |
| Kilo (`kilo-auto/free`) | The shared 112-set it already has is fine, BUT replace divergent copies with canonical ones; add SIR core set. | Free builder; needs build/design/security, not GCP plugin skills. |
| OpenCode (big-pickle, glm-flash, deepseek, openrouter free) | Same as Kilo: canonical 112-set + SIR core. | Same role. |
| Devin CLI (swe-2-flash-medium, free) | Currently NO user skills dir found — Devin reads `.devin/` project config and builtin skills only. Add a project-level or user-level skills dir if Devin supports `~/.config/devin/skills` (verify); minimum: AGENTS.md instructions already wired. | Free builder; needs the same core set. |
| ZCode (GLM-5.3 free, driven by Haiku computer-use) | Rules via its own config; give it the SIR core skill files to read on demand. | Free builder. |
| Local Ollama models | None (too weak for skill instructions; they get `scripts/ai/ask.ps1` prompts). | Privacy lane. |
| Claude Haiku subagents (review/audit/plan) | Claude's own 71 skills already; ensure canonical revisions win over stale copies. Haiku agents should get: review-agent, owasp-vulnerability-shield, zero-trust-security-hardening, accidental-data-loss-prevention, customization-architect, direct-action-shield, karpathy-skills, premium-code-bar-adjacent design skills. | Review lane; needs judgment skills, not bulk builders. |
| HQ manager (Claude) | All 71 + read access to this encyclopedia. | Orchestration. |

**SIR core set** (recommend syncing everywhere, ~25 skills): accidental-data-loss-prevention, agent-supercharged-os, anti-vibecoded-design-system, claude-council, cognitive-product-intuition, customization-architect, database-reliability-transactions, direct-action-shield, emil-motion-impeccable, high-conversion-copywriting, karpathy-skills, legal-compliance-shield, master-production-directive, modern-ui-ux-design-system, modern-web-guidance, omniroute-resilience-gateway, paperclip-orchestrator, ponytail-yagni-optimizer, production-engineering-standards, repomix-token-optimizer, review-agent, sir-ecosystem-orchestrator, skill-creator, taste-design-engine, vibe-auth-hardening, zero-trust-security-hardening, plus workspace `sir-session-end`.

## 6. MCP servers and connectors per tool (names only; full list in mcp-inventory.json)

- **Claude**: no user/project `mcpServers` in `~/.claude.json`; MCP comes via the 84 installed plugins (firebase, figma, canva, notion, linear, stripe, vercel, posthog, cloudflare, supabase, telegram, firecrawl, github-ish, etc.).
- **OpenCode / Kilo**: `nvidia-app` only, identical jsonc.
- **Gemini CLI + Antigravity**: shared Google stack — chrome-devtools-mcp, dart-mcp-server, datacloud_* (bigquery, cloud-sql, knowledge-catalog, spanner), firebase-*, github, gmail, gdrive, gdocs, gsheets, gslides, gcalendar, linear, notion, stripe, supabase, vercel, postman, context7, etc. (full names in JSON).
- **Workspace `.mcp.json` / `.agents/mcp_config.json`**: stale `AgentsRoom-*` + `everything-app`, `100hires`, `0bridge`.
- **Devin**: empty descriptions; builtin skills only.
- **Kimi / Cline / Goose / Windsurf / Cursor**: no MCP config found.

## 7. Plugins per tool

- **Gemini/Antigravity**: 42 plugin dirs under `~/.gemini/config/plugins` (see SOURCES.md for the list).
- **Claude**: 84 installed plugins under `~/.claude/plugins` (official marketplace + `sir-guards@sir-mods`, `sir-context@sir-mods`).
- **All other tools**: no plugin system found.

## 8. Safe sync plan (DO NOT EXECUTE yet — exact steps only)

Goal: one canonical copy of each shared skill, propagated to the tools that need it, without touching private data or breaking tool-specific loaders.

1. **Pick canonical source per skill.** For the ~100 divergent names, diff `~/.claude/skills/<n>/SKILL.md` vs `~/.codex/skills/<n>/SKILL.md` vs the gemini-plugin copy; keep the newest/most complete as canonical in a new staging dir `D:/Projects/_SIR/ops/encyclopedia/canonical/<name>/`. (HQ decision per skill; default: Claude copy for SIR-custom skills, codex-family copy for Vercel/Google skills, gemini-plugin copy only when it is clearly newer.)
2. **Stage, don't sync blind.** Copy canonical dirs to `D:/Projects/_SIR/ops/encyclopedia/canonical/` first; run `build-encyclopedia.mjs` against it; HQ reviews the digest diff before any propagation.
3. **Propagate to CLI workers** (they read plain skill folders):
   - `robocopy "D:\Projects\_SIR\ops\encyclopedia\canonical\<name>" "C:\Users\a7med\.config\opencode\skills\<name>" /E`
   - same for `C:\Users\a7med\.config\kilo\skills\<name>` and `C:\Users\a7med\.codex\skills\<name>` (codex is already the donor for most, so only divergent ones need overwrite — back up first: `ren <dir> <dir>.bak-20261112`).
   - Windsurf/Cursor share the same 112-set; sync only if those tools are still used (they duplicate opencode/kilo).
4. **Claude**: do NOT bulk-overwrite `~/.claude/skills`; Claude's copies are the SIR-customized ones. Only port missing skills FROM the canonical set INTO `~/.claude/skills` (the Vercel/Google family Claude lacks), one batch at a time, verifying `skill` still lists them.
5. **Gemini plugins**: never copy into `config/plugins` manually — plugins are managed by Gemini's plugin installer; use `gemini` plugin commands or leave as-is.
6. **Devin**: verify whether `~/.config/devin/skills` or project `.devin/skills` is read (check `devin --help` / docs in `AppData/Local/devin/cli/_versions/*/share/devin/docs/extensibility`); if yes, symlink or copy the SIR core set there.
7. **After every batch**: re-run `node build-encyclopedia.mjs`, regenerate `SKILLS_INDEX.md`, update `PROGRESS.md`, commit.
8. **Housekeeping (separate, owner-visible)**: the stale `AgentsRoom-*` MCP entries in `D:/Projects/.mcp.json` and `.agents/mcp_config.json` should be removed by HQ (AgentsRoom retired); flagged here, not changed.

## 9. Open questions for HQ

- Which revision is canonical for the ~100 divergent skills? Needs a per-skill diff review (suggest haiku subagent batch).
- Does Devin CLI read a user skills dir? (check docs/extensibility.)
- Are Windsurf and Cursor still used enough to keep their 112-copy in sync, or should they be frozen?
- `CUSTOMIZATIONS_CATALOG.md` needs a rewrite to reflect all tools, not just Gemini plugins (pointer added in this round).
