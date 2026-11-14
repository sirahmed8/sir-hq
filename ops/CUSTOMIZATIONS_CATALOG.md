# SIR Customizations Catalog: Skills, Plugins & MCP Servers Across All AI Tools

> **Status**: SYNCED & REFRESHED across `D:\Projects` (verified 2026-11-14).
> **Machine-Wide Inventory**: **421 unique skill names** across **1,223 installed copies** (13 sources) indexed in [`SKILLS_INDEX.md`](SKILLS_INDEX.md), with per-skill digests in [`encyclopedia/`](encyclopedia/PROGRESS.md), canonical SIR core staging in [`encyclopedia/canonical/`](encyclopedia/canonical/), and cross-tool MCP/plugin names in [`encyclopedia/mcp-inventory.json`](encyclopedia/mcp-inventory.json).
> **Context Budget Reality**: Antigravity loads workspace, `~/.gemini/config/skills/`, builtin, and plugin skills under a strict prompt context budget; excess lower-priority plugin skills are excluded dynamically when the budget is reached. Always read `SKILLS_INDEX.md` or search `ops/encyclopedia/` when looking up an excluded plugin skill.

---

## 1. Core Autonomy & Computer Use Layer

| System | Path / Identifier | Description | Mode |
| :--- | :--- | :--- | :--- |
| **SIR Autonomy MCP** | `D:\Projects\_SIR\tools\sir-autonomy\mcp_server.py` | Native JSON-RPC stdio MCP exposing 22 tools for Chrome & Windows desktop | Auto-spawn daemon |
| **SIR Browser Extension** | `D:\Projects\_SIR\tools\sir-autonomy\chrome-extension\` | Manifest V3 Chrome extension with offscreen keepalive and 0-approval control | Real signed-in Chrome |
| **SIR Bridge Server** | `http://127.0.0.1:18991` | WebSocket (`/ws`) and REST (`/browser`, `/computer`) loopback bridge (`sir_bridge` in Codex) | Local background daemon |
| **SIR Autonomy CLI** | `D:\Projects\_SIR\tools\sir-autonomy\sir_ctl.py` | Unified CLI for PowerShell/bash scripts to drive Chrome and Windows desktop | Scriptable CLI |
| **Browse CLI** | `browse` (global npm) | Browserbase headless browser automation & scraping | Cloud/Local automation |

### Autonomous Browser Tools (`sir-browser`)
- `sir_browser_tabs`: Enumerate all open Chrome tabs (IDs, URLs, titles).
- `sir_browser_open(url)`: Open a new tab or URL in Chrome.
- `sir_browser_navigate(url, tabId)`: Navigate active or target tab.
- `sir_browser_snapshot(tabId, maxChars)`: Capture accessibility DOM tree with interactive `[ref_1]`, `[ref_2]` references.
- `sir_browser_click(target, tabId)`: Click interactive element by `ref_N` or CSS selector.
- `sir_browser_fill(target, value, tabId)`: Fill inputs and textareas.
- `sir_browser_scroll(target, dx, dy)`: Smoothly scroll page or element.
- `sir_browser_eval(expression, tabId)`: Run JavaScript in real page context.
- `sir_browser_screenshot(tabId)`: Capture visible tab screenshot.
- `sir_browser_close(tabId)`: Close a tab.

### Autonomous Computer Use Tools (`sir-computer-use`)
- `sir_computer_screenshot(save_path)`: Full screen capture (attaches to `WinSta0\Default`).
- `sir_computer_click(x, y, button, clicks)`: Native mouse click, double-click, or right-click.
- `sir_computer_move(x, y)`: Move cursor to coordinates.
- `sir_computer_drag(x1, y1, x2, y2)`: Click and drag across screen.
- `sir_computer_scroll(dy, dx, x, y)`: Scroll mouse wheel.
- `sir_computer_type(text)`: Type text with Unicode & Arabic support via `SendInput`.
- `sir_computer_key(key)`: Press special key (Enter, Tab, Esc, Win, etc.).
- `sir_computer_hotkey(keys)`: Press key combinations (Ctrl+C, Alt+Tab, Win+R).
- `sir_computer_windows()`: List all open desktop windows with titles and bounds.
- `sir_computer_focus_window(title_or_hwnd)`: Bring any app window to foreground.
- `sir_computer_open_app(target)`: Launch desktop application or command.
- `sir_computer_batch(actions)`: Execute atomic sequence of actions.

---

## 2. Unified Cross-Tool Matrix (Skills, Plugins & MCP Servers)

Truthful snapshot verified against disk and [`encyclopedia/mcp-inventory.json`](encyclopedia/mcp-inventory.json) on 2026-11-14:

| Agent / Runtime | Skill Roots (Verified Count) | Configured MCP Servers (User / Workspace) | Plugins |
| :--- | :--- | :--- | :--- |
| **Antigravity & Gemini CLI** | `~/.gemini/config/skills` (**69**)<br>`~/.gemini/skills` (**58**)<br>`~/.gemini/antigravity/builtin/skills` (**14**)<br>`~/.gemini/antigravity/scratch/skills` (**1**)<br>`~/.gemini/config/plugins/*/skills` (**405**)<br>`D:\Projects\.agents\skills` (**2**) | `~/.gemini/config/mcp_config.json` & `~/.gemini/antigravity/mcp_config.json` (**14**): `GitKraken`, `chrome-devtools-mcp`, `dart-mcp-server`, `datacloud_bigquery_remote`, `datacloud_cloud-sql_remote`, `datacloud_knowledge_catalog_remote`, `datacloud_spanner_remote`, `firebase-mcp-server`, `github-mcp-server`, `gmp-code-assist`, `nvidia-app`, `sequential-thinking`, `sir-autonomy`, `ticktick`<br>`~/.gemini/settings.json` adds: `MCP_DOCKER` | **44** plugin dirs on disk (**43** manifests in `mcp-inventory.json`, **16** exposing plugin-scoped MCP servers; `agent-reach` dir has no manifest) |
| **Claude Code** | `~/.claude/skills` (**79**)<br>Canonical source for 26/27 SIR core skills + 9 synced Claude-only skills | `~/.claude.json` (**2**): `GitKraken`, `nvidia-app`<br>Enabled plugin MCPs (**6** plugins): `canva`, `chrome-devtools`, `cloudflare`, `figma`, `firebase`, `firecrawl` | **85** installed in `~/.claude/plugins/installed_plugins.json` (**14 enabled**, **71 disabled** in `~/.claude/settings.json`, incl. `sir-context@sir-mods`, `sir-guards@sir-mods`; **37 installed** total expose MCP definitions) |
| **Codex** | `~/.codex/skills` (**119**) | `~/.codex/config.toml` (**3**): `GitKraken`, `node_repl`, `sir_bridge` | **12** configured (**11 enabled**, **1 disabled**: `code-review@openai-bundled`): `7` `@openai-bundled` (`browser`, `chrome`, `code-review`, `codex-app-tools`, `computer-use`, `unified-computer-use`, `visualize`) + `5` `@openai-primary-runtime` (`documents`, `pdf`, `presentations`, `spreadsheets`, `template-creator`) |
| **OpenCode** | `~/.config/opencode/skills` (**124**)<br>(includes 9 Claude-only + 27 canonical SIR core) | `~/.config/opencode/opencode.jsonc` (**3** connected): `nvidia-app`, `sir-autonomy` (top-level under `mcp`), `GitKraken` (nested under `mcp.servers`)<br>Instructions: `WORKER_PREAMBLE.md`, `CLI_AGENT_INSTRUCTIONS.md`, `AGENTS.md`, `23-premium-code-bar.md`, `USAGE_POLICY.md` | None (uses skills + shared instructions) |
| **Kilo** | `~/.config/kilo/skills` (**119**)<br>(includes 9 Claude-only + 27 canonical SIR core; `kilo debug skill` loads **129** incl. builtin, `~/.agents/skills`, `D:\Projects\.agents\skills\sir-worker-preamble`, and `~/.claude/skills` fallbacks) | `~/.config/kilo/kilo.jsonc` (**2** connected): `nvidia-app`, `sir-autonomy`<br>Instructions: `WORKER_PREAMBLE.md`, `CLI_AGENT_INSTRUCTIONS.md`, `AGENTS.md`, `23-premium-code-bar.md`, `USAGE_POLICY.md` | None (uses skills + shared instructions) |
| **Devin CLI** | Builtin (**2**): `declarative-repo-setup`, `upload-secrets`<br>Workspace `D:\Projects\.agents\skills` (**2**): `sir-session-end`, `sir-worker-preamble`<br>Shared `~/.agents/skills` (**2**): `agent-reach`, `sir-skill-library`<br>Auto-imported (`devin skills list`): `~/.claude/skills`, `~/.codeium/windsurf/skills`, `~/.cursor/skills` | `%APPDATA%\devin\config.json` omits `mcpServers` (`hasMcpServersKey: false`); `devin mcp list` auto-imports `~/.claude.json` user MCPs (**2**): `GitKraken`, `nvidia-app`<br>`AppData\Local\devin\cli\mcp\descriptions.json`: 2 cached MCP hashes (incl. NVIDIA App diagnostics) | None |
| **Secondary IDEs (Windsurf / Cursor / Cline / Kimi / Goose)** | Windsurf (`~/.codeium/windsurf/skills`: **113**)<br>Cursor (`~/.cursor/skills`: **118**)<br>Cline, Kimi Code, Goose: **0** skill dirs | Workspace `.mcp.json` (`{}`) and `.agents\mcp_config.json` (`0bridge`, `100hires`, `everything-app`). No user MCP files for Windsurf, Cursor, Cline, Kimi, or Goose | None |

### Retired `AgentsRoom` Cleanup (2026-11-14)
- `D:\Projects\.mcp.json`: Removed 5 retired `AgentsRoom-*` entries; now `{ "mcpServers": {} }`.
- `D:\Projects\.agents\mcp_config.json`: Removed 4 retired `AgentsRoom-*` entries; preserved `everything-app`, `100hires`, `0bridge`.
- `D:\Projects\.agentsroom`: Inspected 270 retired runtime/cache/message files (all dated 2026-11-08 08:37 or earlier; 265/270 byte-identical to `SIR AI\legacy\agentsroom\project-state\`, plus 5 retirement-day runtime cache files) and deleted the folder.

---

## 3. MCP Servers Detail

### A. User-Level MCP Servers (Antigravity / Gemini / CLI Tools)

| MCP Server Name | Active In | Purpose & Capabilities |
| :--- | :--- | :--- |
| `sir-autonomy` | Antigravity, Gemini CLI, OpenCode, Kilo, (`sir_bridge` in Codex) | Zero-prompt Chrome browser bridge & Windows desktop computer use |
| `nvidia-app` | Antigravity, Gemini CLI, Claude, OpenCode, Kilo, Devin (auto-imported from `~/.claude.json`) | NVIDIA GPU telemetry, driver status, game filters, overlay capture |
| `GitKraken` | Antigravity, Gemini CLI, Claude, Codex, OpenCode, Devin (auto-imported from `~/.claude.json`) | Git workflows, branch inspection, PRs, repo history |
| `chrome-devtools-mcp` | Antigravity, Gemini CLI | Chrome DevTools Protocol automation, network, console, CSS inspection |
| `github-mcp-server` | Antigravity, Gemini CLI | GitHub repos, issues, pull requests, reviews, commits |
| `firebase-mcp-server` | Antigravity, Gemini CLI | Cloud Firestore, Auth, Storage, Data Connect, Rules validation |
| `dart-mcp-server` | Antigravity, Gemini CLI (also `flutter` plugin) | Dart & Flutter analysis, widget tree, pub tools, hot reload |
| `datacloud_bigquery_remote` | Antigravity, Gemini CLI | Google Cloud BigQuery datasets and queries |
| `datacloud_cloud-sql_remote` | Antigravity, Gemini CLI | Google Cloud SQL instances and schemas |
| `datacloud_knowledge_catalog_remote` | Antigravity, Gemini CLI | Google Cloud Dataplex Knowledge Catalog |
| `datacloud_spanner_remote` | Antigravity, Gemini CLI | Google Cloud Spanner databases |
| `gmp-code-assist` | Antigravity, Gemini CLI | Google Maps Platform code and API assistance |
| `sequential-thinking` | Antigravity, Gemini CLI | Structured multi-step algorithmic reasoning |
| `ticktick` | Antigravity, Gemini CLI | Task management, deadlines, and project lists in TickTick |
| `MCP_DOCKER` | Gemini CLI (`~/.gemini/settings.json`) | Docker MCP gateway |
| `node_repl` | Codex (`~/.codex/config.toml`) | Stateful Node.js REPL execution |

### B. Workspace Shared MCP Servers (`D:\Projects\.agents\mcp_config.json`)

| MCP Server Name | Purpose & Notes |
| :--- | :--- |
| `everything-app` | Remote Alpic staging HTTP MCP endpoint (`https://everything-app-7f22928f.staging.alpic.live` in `D:\Projects\.agents\mcp_config.json`; monitor remote quota limits) |
| `100hires` | Remote 100hires HTTP MCP endpoint (`https://mcp.100hires.com/mcp`; hiring & candidate workflow connector) |
| `0bridge` | Remote 0bridge MCP (`https://0bridge.dev/mcp` via `mcp-remote@0.15.2`; `MCP_REMOTE_CONFIG_DIR` still references `~\.agentsroom\mcp-oauth\e649caaf5f6077dc`: re-point or re-auth if used) |

### C. Antigravity Plugin-Scoped MCP Servers (16 Plugins in `C:\Users\a7med\.gemini\config\plugins\`)

| Plugin Name | Exposed MCP Server Name(s) | Skills Indexed in Plugin |
| :--- | :--- | :--- |
| `canva` | `canva` | 12 |
| `context7` | `context7` | 1 |
| `data-agent-kit-plugin` | `dak-bigquery`, `dak-cloudsql`, `dak-data-agent-kit`, `dak-kc`, `dak-notebook`, `dak-spanner` | 70 (40 unique) |
| `figma` | `figma` | 35 (19 unique) |
| `flutter` | `dart-mcp-server` | 25 |
| `gemini-api` | `gemini-api-docs` | 4 |
| `google-developer-knowledge` | `google-developer-knowledge` | 1 |
| `linear` | `linear` | 0 |
| `mobbin` | `mobbin` | 4 |
| `netlify` | `netlify` | 48 (16 unique) |
| `notion` | `notion` | 12 |
| `postman` | `postman` | 19 |
| `sir-autonomy` | `sir-autonomy` | 2 |
| `stripe` | `stripe` | 0 |
| `supabase` | `mcp` | 2 |
| `vercel-plugin` | `vercel` | 48 (39 unique) |

All remaining plugin directories in `~/.gemini/config/plugins/` (`advanced-engineering`, `android-cli-plugin`, `atlassian-twg-cli`, `auth0`, `base44`, `browse`, `chrome-devtools-plugin`, `creator-studio`, `firebase`, `gcalendar`, `gdocs`, `gdrive`, `gmail`, `google-antigravity-sdk`, `google_maps_platform`, `googlecloudtools.datacloud_telemetry`, `gsheets`, `gslides`, `invideo`, `modern-web-guidance-plugin`, `multi-agent-orchestrator`, `qodo`, `reverse-engineering`, `sir-ecosystem`, `sir-ecosystem-suite`, `superpowers`, `unity`, plus manifest-less `agent-reach`) provide skills/hooks without extra MCP servers. Total across `~/.gemini/config/plugins/*/skills`: **405 skills** across **44 plugin directories** (**43** plugin manifests).

---

## 4. Safe Canonical Skill Sync (Executed 2026-11-14)

### A. Canonical Staging: 27 SIR Core Skills (`ops/encyclopedia/canonical/`)

All 27 core skills listed in [`encyclopedia/ORGANIZATION_PLAN.md`](encyclopedia/ORGANIZATION_PLAN.md) were canonicalized into `D:\Projects\_SIR\ops\encyclopedia\canonical\` and verified byte-identical across `~/.gemini/config/skills/`, `~/.config/opencode/skills/`, and `~/.config/kilo/skills/`:

- **26 canonicalized from `~/.claude/skills/`** (retained full trigger `"Use when ..."` frontmatter descriptions lost in earlier truncated copies):
  `accidental-data-loss-prevention`, `agent-supercharged-os`, `anti-vibecoded-design-system`, `claude-council`, `cognitive-product-intuition`, `customization-architect`, `database-reliability-transactions`, `direct-action-shield`, `emil-motion-impeccable`, `high-conversion-copywriting`, `karpathy-skills`, `legal-compliance-shield`, `master-production-directive`, `modern-ui-ux-design-system`, `omniroute-resilience-gateway`, `paperclip-orchestrator`, `ponytail-yagni-optimizer`, `production-engineering-standards`, `repomix-token-optimizer`, `review-agent`, `sir-ecosystem-orchestrator`, `skill-creator`, `taste-design-engine`, `vibe-auth-hardening`, `zero-trust-security-hardening`, `sir-session-end`
- **1 canonicalized from `modern-web-guidance-plugin`** (2026-11-13 revision adding `legacy-scan` workflow, superseding older 2026-10-21 copies):
  `modern-web-guidance`

### B. Claude-Only Sync to Antigravity, OpenCode & Kilo

Of the 12 Claude-only skill candidates from `ORGANIZATION_PLAN.md`, **9** existed in `~/.claude/skills/` and were synced identically into `~/.gemini/config/skills/`, `~/.config/opencode/skills/`, and `~/.config/kilo/skills/`:

- `accidental-data-loss-prevention` (also in canonical core)
- `firestore-data`
- `imagegen`
- `nextjs`
- `review-agent` (also in canonical core)
- `shadcn`
- `skill-installer`
- `social-creator-studio`
- `video-digest`

The remaining 3 candidates (`next-forge`, `next-upgrade`, `turbopack`) did not exist in `~/.claude/skills/` (already present in Codex, OpenCode, and Kilo) and were skipped cleanly.

### C. New Cross-Tool `sir-worker-preamble` Skill

Created a dedicated `sir-worker-preamble` skill packaging `D:\Projects\_SIR\ops\WORKER_PREAMBLE.md` and `D:\Projects\_SIR\standard\23-premium-code-bar.md` in:
- [`C:\Users\a7med\.gemini\config\skills\sir-worker-preamble\SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/sir-worker-preamble/SKILL.md) (Antigravity)
- [`D:\Projects\.agents\skills\sir-worker-preamble\SKILL.md`](file:///D:/Projects/.agents/skills/sir-worker-preamble/SKILL.md) (Workspace `.agents` for Devin CLI & workspace-aware agents)
- Deep digest archived at [`ops/encyclopedia/deep/sir-worker-preamble.md`](encyclopedia/deep/sir-worker-preamble.md)

---

## 5. High-Signal Skills Quick Reference (Full 421-Skill Table in `SKILLS_INDEX.md`)

Rather than duplicating 421 rows here, this table highlights the primary entry-point skills synced across tools. Use [`SKILLS_INDEX.md`](SKILLS_INDEX.md) for the complete 421-row searchable index and [`encyclopedia/SOURCES.md`](encyclopedia/SOURCES.md) for every root path.

| Domain | Key Unified / Canonical Skills | Complete Scope |
| :--- | :--- | :--- |
| **SIR Core Governance & Session** | `sir-worker-preamble`, `sir-session-end`, `sir-ecosystem-orchestrator`, `sir-skill-library`, `master-production-directive`, `direct-action-shield`, `karpathy-skills`, `ponytail-yagni-optimizer`, `production-engineering-standards` | Canonical in `ops/encyclopedia/canonical/` & `.agents/skills/` |
| **Autonomy, Planning & Review** | `sir-browser`, `sir-computer-use`, `agent-supercharged-os`, `claude-council`, `paperclip-orchestrator`, `review-agent`, `accidental-data-loss-prevention`, `using-superpowers`, `systematic-debugging`, `test-driven-development`, `verification-before-completion` | Synced across Claude, Antigravity, OpenCode, Kilo + `superpowers` plugin |
| **Design, UI/UX & Copy** | `anti-vibecoded-design-system`, `cognitive-product-intuition`, `modern-ui-ux-design-system`, `taste-design-engine`, `emil-motion-impeccable`, `high-conversion-copywriting`, `shadcn`, `mobile-ergonomics-polish` | Plus `figma` (35 indexed / 19 unique), `canva` (12), `mobbin` (4), `creator-studio` (2) |
| **Web, Next.js & Mobile** | `modern-web-guidance`, `nextjs`, `ai-sdk`, `react-best-practices`, `android-cli`, `compose-preview`, `flutter-*`, `dart-*` | Plus `vercel-plugin` (48 / 39 unique), `netlify` (48 / 16 unique), `android-cli-plugin` (3), `flutter` (25) |
| **Data, Cloud & Security** | `database-reliability-transactions`, `firestore-data`, `zero-trust-security-hardening`, `vibe-auth-hardening`, `legal-compliance-shield`, `owasp-vulnerability-shield`, `omniroute-resilience-gateway` | Plus `firebase` (13), `supabase` (2), `data-agent-kit-plugin` (70 / 40 unique), `auth0` (1) |
| **Media, Docs & Tooling** | `imagegen`, `video-digest`, `social-creator-studio`, `skill-creator`, `skill-installer`, `customization-architect`, `repomix-token-optimizer`, `typst-pdf-maker`, `excel-generator` | Plus `invideo` (11), `postman` (19), `qodo` (5), `unity` (33), `notion` (12), `google-*` |
