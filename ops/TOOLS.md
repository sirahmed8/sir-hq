# TOOLS (checked 2026-10-29, Phase 0.2)

Windows 11 Pro 10.0.26300 x64 · Git Bash shell · Lenovo i7-13th, RTX 4050 6 GB, 24 GB RAM (per rule 6).

## CLIs present
| Tool | Version | Path / note |
|---|---|---|
| Claude Code | 2.1.312 | npm global. `claude doctor` not run (interactive); run it in Phase 1 |
| git | 2.56.0.windows.3 | msys2 ucrt64 |
| node / npm | v24.22.1 / 11.11.0 | `C:\Program Files\nodejs` |
| bun | 1.4.2 | `~/.bun/bin` |
| java | OpenJDK 21.0.13 (Microsoft) | `JAVA_HOME` set. Rules mention JDK 17 for Gradle: verify per project in Phase 1 |
| python | 3.14.7 (msys2) and `py` 3.14.2 | two Pythons; pick one per project |
| gh | 2.103.3 | logged in as `sirahmed8`, https |
| firebase | 15.12.0 | logged in as the Gmail account on file |
| vercel | 50.1.3 | **not logged in** (Hobby is non-commercial only anyway, rule 17) |
| agy (Antigravity CLI) | 1.4.9 | `~/AppData/Local/agy/bin` |
| opencode | v2.2.0 | npm global |
| kilo | 7.8.18 | npm global |
| ollama | 0.40.11 | server up on :11434 but `api/tags` is empty: models live in `D:\Projects\AI_Models_Hub\ollama`, so `OLLAMA_MODELS` needs to point there (rule 11, Phase 1) |
| n8n | 2.44.6 | npm global, not started |
| adb | 36.0.0 | `C:\Users\a7med\platform-tools` (standalone; `ANDROID_HOME` unset) |
| winget | 1.29.380 | used for installs |
| gitleaks | 8.30.1 | installed this session via winget `Gitleaks.Gitleaks` |
| git-filter-repo | a40bce548d2c | pip from PyPI (`py -m pip install git-filter-repo`), run as `py -m git_filter_repo`; used once on SIR ModPack |
| pm2, localtunnel, cline, crush, droid, copilot, pi-coding-agent, ticktick-cli | see `npm ls -g` | other agents/tools already present |

## Missing (install in Phase 1 from official sources, project scope first)
pnpm · eas-cli · wrangler (Cloudflare) · Android SDK + `ANDROID_HOME` (only platform-tools exist) · docker (not needed yet) · cargo · flutter (not needed unless a project requires it).

## Local Ollama models (files present, not yet served)
bge-m3, deepseek-r1:1.5b, nomic-embed-text, qwen2.5:1.5b, qwen2.5-coder:1.5b, qwen3:8b. Total about 9.2 GB. Manifest: `D:\Backups\SIR-2026-10-29\AI_Models_Hub-manifest.txt`.

## Hooks (SIR memory)
`C:\Users\a7med\.claude\settings.json` → SessionStart, PreCompact, Stop → `D:/Projects/_SIR/scripts/memory/*.mjs`. Backup of the previous settings: `settings.json.bak-pre-sir-2026-10-29` in the same folder. Re-authenticate: nothing to do.

## MCP / connectors needing authorization (user action via `/mcp`, never blocking)
Many plugin servers show "needs authentication" (GitHub connector, Exa, Firecrawl plugin, HubSpot, Atlassian, etc.). Failed to connect this session: firebase (timeout), discord, fakechat, firestore-native (closed), zoom (401). The mission does not depend on them yet; revisit per phase.
