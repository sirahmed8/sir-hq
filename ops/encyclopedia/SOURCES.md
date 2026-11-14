# SOURCES: where every skill/plugin/MCP definition was found (r47, verified 2026-11-14)

| Source | Path | Exists | Skill dirs found | Notes |
|---|---|---|---|---|
| Claude skills | `C:/Users/a7med/.claude/skills` | yes | 78 | |
| Codex skills | `C:/Users/a7med/.codex/skills` | yes | 119 | |
| Windsurf skills | `C:/Users/a7med/.codeium/windsurf/skills` | yes | 112 | |
| Cursor skills | `C:/Users/a7med/.cursor/skills` | yes | 117 | |
| OpenCode skills | `C:/Users/a7med/.config/opencode/skills` | yes | 124 | |
| Kilo skills | `C:/Users/a7med/.config/kilo/skills` | yes | 119 | |
| Shared .agents skills | `C:/Users/a7med/.agents/skills` | yes | 2 | |
| Gemini CLI skills | `C:/Users/a7med/.gemini/skills` | yes | 57 | |
| Gemini config skills (Antigravity) | `C:/Users/a7med/.gemini/config/skills` | yes | 69 | |
| Antigravity builtin skills | `C:/Users/a7med/.gemini/antigravity/builtin/skills` | yes | 14 | |
| Antigravity scratch skills | `C:/Users/a7med/.gemini/antigravity/scratch/skills` | yes | 1 | |
| Gemini plugins (skills inside) | `C:/Users/a7med/.gemini/config/plugins/*/skills` | yes | 405 | |
| Workspace skills | `D:/Projects/.agents/skills` | yes | 2 | |

## Tools checked with no skill store found

- **Goose**: `goose.exe` on PATH (WinGet Links) but no `~/.config/goose`, no AppData config, no skills.
- **Cline**: `~/.cline` has data/tasks/cron only; no skills dir, no mcp settings file found.
- **Kimi Code**: `~/.kimi-code` has config.toml (providers/models), sessions, telemetry; no skills or MCP tables.
- **Devin CLI**: `~/AppData/Local/devin/cli` binary + docs; builtin skills (`declarative-repo-setup`, `upload-secrets`), plus reads workspace `.agents/skills/` (`D:/Projects/.agents/skills`) and `~/.agents/skills/`.
- **Windsurf / Cursor MCP**: no `mcp_config.json` / `mcp.json` found; Cursor `~/.cursor` holds only AGENTS.md and skills/.
- **Project skill folders**: `D:/Projects/*/.claude`, `.agents`, `.sir` contain `agents/` subagent definitions (one per project), not SKILL.md skills, except `D:/Projects/.agents/skills/` (`sir-session-end`, `sir-worker-preamble`). `D:/Projects/AHome` was NOT opened (private project). Legacy bundled SKILL.md files under `SIR AI/legacy/**` are research artifacts, excluded from the index.
- **Claude plugins**: installed plugins catalogued in `mcp-inventory.json` (`claude.plugins`); their skills live in the plugin cache, not user skill dirs.
- **Canonical staging**: `D:/Projects/_SIR/ops/encyclopedia/canonical/` holds the 27 canonical SIR core skills synced across `gemini-config`, `opencode`, and `kilo`.

## MCP / connector definitions per tool

Names only (secrets stripped): see `ops/encyclopedia/mcp-inventory.json`. Summary:
- Claude (`~/.claude.json`): `GitKraken`, `nvidia-app`, plus 85 installed plugins in `~/.claude/plugins/installed_plugins.json`.
- Codex (`~/.codex/config.toml`): `node_repl`, `sir_bridge`, `GitKraken`, plus 12 bundled/primary-runtime plugins.
- OpenCode (`~/.config/opencode/opencode.jsonc`): `sir-autonomy`, `nvidia-app`, `GitKraken` (under `mcp.servers`).
- Kilo (`~/.config/kilo/kilo.jsonc`): `sir-autonomy`, `nvidia-app`.
- Gemini CLI & Antigravity (`~/.gemini/settings.json`, `~/.gemini/config/mcp_config.json`, `~/.gemini/antigravity/mcp_config.json`): `MCP_DOCKER`, `GitKraken`, `chrome-devtools-mcp`, `dart-mcp-server`, `datacloud_*` (BigQuery, Cloud SQL, Knowledge Catalog, Spanner), `firebase-mcp-server`, `github-mcp-server`, `gmp-code-assist`, `nvidia-app`, `sequential-thinking`, `sir-autonomy`, `ticktick`, plus plugin-scoped MCPs (`canva`, `context7`, `data-agent-kit-plugin`, `figma`, `flutter`, `gemini-api`, `google-developer-knowledge`, `linear`, `mobbin`, `netlify`, `notion`, `postman`, `sir-autonomy`, `stripe`, `supabase`, `vercel-plugin`).
- Workspace `D:/Projects/.mcp.json` (`{}`) and `D:/Projects/.agents/mcp_config.json`: `everything-app`, `100hires`, `0bridge` (retired `AgentsRoom-*` entries removed 2026-11-14).
- Devin: `%APPDATA%/devin/config.json` has `mcpServers: {}` (`cli/mcp/descriptions.json` lists 2 cached MCP hashes incl. NVIDIA App); built-in skills (`declarative-repo-setup`, `upload-secrets`) + `.agents/skills` + `~/.agents/skills`.
- Kimi: no MCP; config.toml defines providers/models only.
- Cline, Goose: no MCP config found.