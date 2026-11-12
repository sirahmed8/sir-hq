# SOURCES: where every skill/plugin/MCP definition was found (r47, verified 2026-11-12)

| Source | Path | Exists | Skill dirs found | Notes |
|---|---|---|---|---|
| Claude skills | `C:/Users/a7med/.claude/skills` | yes | 72 | |
| Codex skills | `C:/Users/a7med/.codex/skills` | yes | 113 | |
| Windsurf skills | `C:/Users/a7med/.codeium/windsurf/skills` | yes | 112 | |
| Cursor skills | `C:/Users/a7med/.cursor/skills` | yes | 112 | |
| OpenCode skills | `C:/Users/a7med/.config/opencode/skills` | yes | 112 | |
| Kilo skills | `C:/Users/a7med/.config/kilo/skills` | yes | 112 | |
| Shared .agents skills | `C:/Users/a7med/.agents/skills` | yes | 1 | |
| Gemini CLI skills | `C:/Users/a7med/.gemini/skills` | yes | 57 | |
| Antigravity builtin skills | `C:/Users/a7med/.gemini/antigravity/builtin/skills` | yes | 13 | |
| Antigravity scratch skills | `C:/Users/a7med/.gemini/antigravity/scratch/skills` | yes | 1 | |
| Gemini plugins (skills inside) | `C:/Users/a7med/.gemini/config/plugins/*/skills` | yes | 301 | |
| Workspace skills | `D:/Projects/.agents/skills` | yes | 1 | |

## Tools checked with no skill store found

- **Goose**: `goose.exe` on PATH (WinGet Links) but no `~/.config/goose`, no AppData config, no skills.
- **Cline**: `~/.cline` has data/tasks/cron only; no skills dir, no mcp settings file found.
- **Kimi Code**: `~/.kimi-code` has config.toml (providers/models), sessions, telemetry; no skills or MCP tables.
- **Devin CLI**: `~/AppData/Local/devin/cli` binary + docs only; skills are builtin (declarative-repo-setup, upload-secrets). No user skill dir found.
- **Windsurf / Cursor MCP**: no `mcp_config.json` / `mcp.json` found; Cursor `~/.cursor` holds only AGENTS.md and skills/.
- **Project skill folders**: `D:/Projects/*/.claude`, `.agents`, `.sir` contain `agents/` subagent definitions (one per project), not SKILL.md skills, except `D:/Projects/.agents/skills/sir-session-end`. `D:/Projects/AHome` was NOT opened (private project). Legacy bundled SKILL.md files under `SIR AI/legacy/**` are research artifacts, excluded from the index.
- **Claude plugins**: 84 installed plugins catalogued in `mcp-inventory.json` (`claude.plugins`); their skills live in the plugin cache, not user skill dirs.

## MCP / connector definitions per tool

Names only (secrets stripped): see `ops/encyclopedia/mcp-inventory.json`. Summary:
- Claude (`~/.claude.json`): no `mcpServers` configured at user or project level.
- OpenCode & Kilo (`opencode.jsonc` / `kilo.jsonc`): only `nvidia-app` MCP.
- Gemini CLI (`~/.gemini/settings.json`, `~/.gemini/config/mcp_config.json`): chrome-devtools, dart, datacloud_* (BigQuery, Cloud SQL, Knowledge Catalog, Spanner), firebase, github, gmail, gdrive, gsheets, gslides, gdocs, gcalendar, linear, notion, stripe, supabase, verkle etc. (full list in JSON).
- Antigravity (`~/.gemini/antigravity/mcp_config.json`): same Google stack as Gemini CLI.
- Workspace `D:/Projects/.mcp.json` and `.agents/mcp_config.json`: AgentsRoom-* servers (AgentsRoom retired 2026-11-08, likely stale) plus everything-app, 100hires, 0bridge.
- Devin: `cli/mcp/descriptions.json` is empty `{}`; built-in skills only.
- Kimi: no MCP; config.toml defines providers/models only.
- Cline, Goose: no MCP config found.