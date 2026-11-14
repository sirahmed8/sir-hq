# SOURCES: where every skill/plugin/MCP definition was found (r47, verified 2026-11-14)

| Source | Path | Exists | Skill dirs found | Notes |
|---|---|---|---|---|
| Claude skills | `C:/Users/a7med/.claude/skills` | yes | 79 | |
| Codex skills | `C:/Users/a7med/.codex/skills` | yes | 119 | |
| Windsurf skills | `C:/Users/a7med/.codeium/windsurf/skills` | yes | 113 | |
| Cursor skills | `C:/Users/a7med/.cursor/skills` | yes | 118 | |
| OpenCode skills | `C:/Users/a7med/.config/opencode/skills` | yes | 124 | |
| Kilo skills | `C:/Users/a7med/.config/kilo/skills` | yes | 119 | |
| Shared .agents skills | `C:/Users/a7med/.agents/skills` | yes | 2 | |
| Gemini CLI skills | `C:/Users/a7med/.gemini/skills` | yes | 58 | |
| Gemini config skills (Antigravity) | `C:/Users/a7med/.gemini/config/skills` | yes | 69 | |
| Antigravity builtin skills | `C:/Users/a7med/.gemini/antigravity/builtin/skills` | yes | 14 | |
| Antigravity scratch skills | `C:/Users/a7med/.gemini/antigravity/scratch/skills` | yes | 1 | |
| Gemini plugins (skills inside) | `C:/Users/a7med/.gemini/config/plugins/*/skills` | yes | 405 | |
| Workspace skills | `D:/Projects/.agents/skills` | yes | 2 | |

## Tools checked with no skill store found

- **Goose**: `goose.exe` on PATH (WinGet Links) but no `~/.config/goose`, no AppData config, no skills.
- **Cline**: `~/.cline` has data/tasks/cron only; no skills dir, no mcp settings file found.
- **Kimi Code**: `~/.kimi-code` has config.toml (providers/models), sessions, telemetry; no skills or MCP tables.
- **Devin CLI**: `~/AppData/Local/devin/cli` binary + docs; no standalone `%APPDATA%/devin/skills` populated on disk, has 2 builtin skills (`declarative-repo-setup`, `upload-secrets`), loads `~/.agents/skills/` and `D:/Projects/.agents/skills/`, and auto-imports `~/.claude/skills/`, `~/.codeium/windsurf/skills/`, and `~/.cursor/skills/`.
- **Windsurf / Cursor MCP**: no `mcp_config.json` / `mcp.json` found; Cursor `~/.cursor` holds only AGENTS.md and skills/.
- **Project skill folders**: `D:/Projects/*/.claude`, `.agents`, `.sir` contain `agents/` subagent definitions (one per project), not SKILL.md skills, except `D:/Projects/.agents/skills/` (`sir-session-end`, `sir-worker-preamble`). `D:/Projects/AHome` was NOT opened (private project). Legacy bundled SKILL.md files under `SIR AI/legacy/**` are research artifacts, excluded from the index.
- **Claude plugins**: installed vs enabled/disabled plugins catalogued in `mcp-inventory.json` (`claude.plugins`, `claude.enabledPlugins`, `claude.disabledPlugins`); their skills live in the plugin cache, not user skill dirs.
- **Canonical staging**: `D:/Projects/_SIR/ops/encyclopedia/canonical/` holds the 27 canonical SIR core skills synced across `gemini-config`, `opencode`, and `kilo`.

## MCP / connector definitions per tool

Names only (secrets stripped): see `ops/encyclopedia/mcp-inventory.json`. Summary:
- Claude (`~/.claude.json`, `~/.claude/settings.json`): `GitKraken`, `nvidia-app`, plus 85 installed plugins (14 enabled, 71 disabled; 6 enabled / 37 installed expose MCP servers).
- Codex (`~/.codex/config.toml`): `GitKraken`, `node_repl`, `sir_bridge`, plus 12 plugins (11 enabled, 1 disabled: `code-review@openai-bundled`).
- OpenCode (`~/.config/opencode/opencode.jsonc`): `GitKraken`, `nvidia-app`, `sir-autonomy` (top-level: `nvidia-app`, `sir-autonomy`; nested under `mcp.servers`: `GitKraken`).
- Kilo (`~/.config/kilo/kilo.jsonc`): `nvidia-app`, `sir-autonomy`.
- Gemini CLI & Antigravity (`~/.gemini/settings.json`, `~/.gemini/config/mcp_config.json`, `~/.gemini/antigravity/mcp_config.json`): `GitKraken`, `MCP_DOCKER`, `chrome-devtools-mcp`, `dart-mcp-server`, `datacloud_bigquery_remote`, `datacloud_cloud-sql_remote`, `datacloud_knowledge_catalog_remote`, `datacloud_spanner_remote`, `firebase-mcp-server`, `github-mcp-server`, `gmp-code-assist`, `nvidia-app`, `sequential-thinking`, `sir-autonomy`, `ticktick`, plus 16 plugin-scoped MCP providers (`canva`, `context7`, `data-agent-kit-plugin`, `figma`, `flutter`, `gemini-api`, `google-developer-knowledge`, `linear`, `mobbin`, `netlify`, `notion`, `postman`, `sir-autonomy`, `stripe`, `supabase`, `vercel-plugin`).
- Workspace `D:/Projects/.mcp.json` (`{}`) and `D:/Projects/.agents/mcp_config.json`: `0bridge`, `100hires`, `everything-app` (retired `AgentsRoom-*` entries removed 2026-11-14).
- Devin: `%APPDATA%/devin/config.json` has `hasMcpServersKey: false`; `devin mcp list` auto-imports `~/.claude.json` MCPs (`GitKraken`, `nvidia-app`); `cli/mcp/descriptions.json` caches 2 entries; loads builtin (`declarative-repo-setup`, `upload-secrets`), `~/.agents/skills`, `D:/Projects/.agents/skills`, plus auto-imported Claude/Windsurf/Cursor skills.
- Kimi: no MCP; config.toml defines providers/models only.
- Cline, Goose: no MCP config found.