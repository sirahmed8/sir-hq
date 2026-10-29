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

## Phase 1 additions (2026-10-29)
- Installed (npm global): pnpm 12.16.1, eas-cli 27.1.0, wrangler 4.155.0. Removed the duplicate npm copy of Claude Code (native 2.1.312 at `~/.local/bin` is the one that runs). `git config --global core.longpaths true`.
- Claude Code: latest; `claude doctor` clean after the duplicate removal. `ANTHROPIC_BASE_URL` is set only inside the desktop-app process to the default `https://api.anthropic.com` (not user/machine/settings level): harmless. Auto-updates show "disabled (set by env: DISABLE_AUTOUPDATER)" in the app process; update manually (`claude update`) or via npm-free native updater.
- Remote Control: 27 stale `bridge-pointer.json` files moved to `D:\Backups\SIR-2026-10-29\bridge-pointers\`. HQ server script `_SIR/scripts/rc-hq.ps1` run twice: connected, "Capacity 0/8", worker registered on attempt 1 both times (second run reused the prior environment from the pointer), no HTTP 404. NOT registered as a logon task (owner action).
- User settings (`~/.claude/settings.json`, backups `settings.json.bak-pre-sir-2026-10-29` and `.bak-phase1-2026-10-29`): `remoteControlAtStartup: true`, env `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` (2-teammate smoke test still to run), deny rules added for `gh repo delete`, `git push --mirror`, `gh release delete`. Hooks now: SessionStart, PreCompact, Stop, SubagentStop. `defaultMode` stays `auto`; `bypassPermissions` not used.
- Roster: 18 agents in `~/.claude/agents/` (scout, architect, reviewer, builder, mobile-engineer, desktop-engineer, ui-craftsman, qa-breaker, security-auditor, release-manager, localizer, seo-specialist, automation-engineer, docs-keeper, ai-engineer, growth-operator, study-coach, pc-janitor); existing agents kept (architect-refactor, desktop-release-qa, explorer, legal-compliance-counsel, security-shield-auditor, ui-motion-director). Skill `sir-session-end` created; the other eight rule-9 skills are created when their procedure exists (Phases 4-5), not as empty shells.
- External workforce, all tested through `_SIR/scripts/ai/ask.ps1` (pwsh 7.6): local Ollama (qwen2.5:1.5b default) ok; `agy` (default model, ~50 s for one word) ok; `opencode` with `opencode/deepseek-v4.1-flash-free` ok; `kilo run --auto` ok. Forced failure (nonexistent OpenCode model) retried once then fell back to local. A prompt containing a credential-shaped string is forced to local-only. Ledger: `ops/usage-ledger.jsonl`; cooling marker: `ops/provider-cooling.json` (both git-ignored).
  - agy: `--model gemini-3.8-flash-low` returned INVALID_ARGUMENT, so the wrapper omits `--model` unless asked. Models listed: gemini-3.8-flash (high/medium/low), claude-sonnet-4-6, claude-opus-4-6-thinking, gpt-oss-120b.
  - `useG1Credits` was **true**; set to **false** (backup `settings.json.bak-pre-sir-2026-10-29` next to it). The app-level "AI Credit Overages" switch still needs Ahmed to confirm "Never" (OWNER_ACTIONS).
  - OpenCode has no "Muse Spark" model in its list; use the `opencode/*-free` models.
  - Data terms (read 2026-10-29 from opencode.ai/docs/zen and kilo.ai/privacy): OpenCode `deepseek-v4.1-flash-free` and `glm-5.3-flash-free`: zero retention, not used for training (the only two allowed for workspace text). `beam-free`: no training, 30-day retention. `big-pickle`, `mimo-v2.6-flash-free`, `flint-40b-free`: data may be used to improve the model during the free period: public text only. NVIDIA Nemotron free endpoints: logged and used to improve NVIDIA products: public text only. Kilo: its privacy policy is silent on training and on free models, and prompts go to the chosen provider via OpenRouter under that provider's retention rules: treat Kilo as public text only. Secrets and private data (AHome, Habiba, credentials) stay local-only in every case (ask.ps1 already forces that for credential-shaped prompts).
- Ollama: `OLLAMA_MODELS` (user scope) corrected from `D:\AI_Models_Hub\ollama` to `D:\Projects\AI_Models_Hub\ollama`; server restarted as a hidden `ollama serve` process; all 6 models now listed (qwen3:8b, bge-m3, qwen2.5-coder:1.5b, deepseek-r1:1.5b, nomic-embed-text, qwen2.5:1.5b). Empty leftover folders at `D:\AI_Models_Hub` (0 files) for the janitor.
- Heads-up: the enabled plugin `outputai@claude-plugins-official` injects about 41,000 characters of Output.ai instructions into every session start. It read `false` in settings at the start of this session and `true` later (toggled by Ahmed or the app); if Output.ai is not used, disabling it saves roughly 10k tokens per session.
