# SIR Customizations Catalog: Plugins, Skills, MCP Servers & Subagents

> **Status**: ACTIVE & OPTIMIZED across all workspaces (`D:\Projects`).
> **Token Budget Health**: Fully compliant (< 65% of 20,000 cap, **0 excluded skills**, **0 excluded MCP tools**).
> **Canonical Reference**: Read by all agents and future sessions at startup.
>
> **2026-11-12 (r47)**: the full machine-wide inventory now lives in [`SKILLS_INDEX.md`](SKILLS_INDEX.md) (384 unique skills, 1004 installed copies across Claude, Codex, Windsurf, Cursor, OpenCode, Kilo, Gemini, Antigravity, plugins, workspace) with per-skill digests in [`encyclopedia/`](encyclopedia/PROGRESS.md), MCP/plugin names per tool in [`encyclopedia/mcp-inventory.json`](encyclopedia/mcp-inventory.json), and the sync plan in [`encyclopedia/ORGANIZATION_PLAN.md`](encyclopedia/ORGANIZATION_PLAN.md). This catalog remains the curated narrative; the index is the complete list.

---

## 1. Core Autonomy & Computer Use Layer

| System | Path / Identifier | Description | Mode |
| :--- | :--- | :--- | :--- |
| **SIR Autonomy MCP** | `D:\Projects\_SIR\tools\sir-autonomy\mcp_server.py` | Native JSON-RPC stdio MCP exposing 22 tools for Chrome & Windows desktop | Auto-spawn daemon |
| **SIR Browser Extension** | `D:\Projects\_SIR\tools\sir-autonomy\chrome-extension\` | Manifest V3 Chrome extension with offscreen keepalive and 0-approval control | Real signed-in Chrome |
| **SIR Bridge Server** | `http://127.0.0.1:18991` | High-speed WebSocket (`/ws`) & REST (`/browser`, `/computer`) loopback bridge | Local background daemon |
| **SIR Autonomy CLI** | `D:\Projects\_SIR\tools\sir-autonomy\sir_ctl.py` | Unified CLI for pwsh/bash scripts to drive Chrome and Windows desktop | Scriptable CLI |
| **Browse CLI** | `browse` (global npm) | Browserbase headless browser automation & scraping | Cloud/Local automation |

### Autonomous Browser Tools (`sir-browser`):
- `sir_browser_tabs`: Enumerate all open Chrome tabs (IDs, URLs, titles).
- `sir_browser_open(url)`: Open a new tab or URL in Ahmed's Chrome.
- `sir_browser_navigate(url, tabId)`: Navigate active or target tab.
- `sir_browser_snapshot(tabId, maxChars)`: Capture accessibility DOM tree with interactive `[ref_1]`, `[ref_2]` references.
- `sir_browser_click(target, tabId)`: Click interactive element by `ref_N` or CSS selector.
- `sir_browser_fill(target, value, tabId)`: Fill inputs and textareas.
- `sir_browser_scroll(target, dx, dy)`: Smoothly scroll page or element.
- `sir_browser_eval(expression, tabId)`: Run JavaScript in real page context.
- `sir_browser_screenshot(tabId)`: Capture visible tab screenshot.
- `sir_browser_close(tabId)`: Close a tab.

### Autonomous Computer Use Tools (`sir-computer-use`):
- `sir_computer_screenshot(save_path)`: High-res full screen grab (attaches to `WinSta0\Default`).
- `sir_computer_click(x, y, button, clicks)`: Native mouse click/double-click/right-click.
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

## 2. Installed MCP Servers (Registered in `mcp_config.json`)

| MCP Server Name | Transport | Purpose & Capabilities |
| :--- | :--- | :--- |
| `sir-autonomy` | stdio (Python) | Zero-prompt Chrome bridge & Windows desktop computer use |
| `chrome-devtools-mcp` | stdio (npx) | Chrome DevTools Protocol automation, network requests, console, CSS inspection |
| `github-mcp-server` | stdio (gh) | GitHub repos, issues, pull requests, reviews, and commits |
| `firebase-mcp-server` | stdio (npx) | Cloud Firestore, Auth, Storage, Data Connect, and Rules validation |
| `datacloud_*` | remote | Google Cloud BigQuery, Cloud SQL, Knowledge Catalog, Spanner |
| `nvidia-app` | stdio | NVIDIA GPU telemetry, driver status, game filters, overlay capture |
| `sequential-thinking` | stdio (npx) | Structured multi-step algorithmic reasoning and stateful hypotheses |
| `ticktick` | stdio (npx) | Task management, deadlines, and project lists in TickTick |
| `postman-mcp-server` | stdio (npx) | API collections, workspaces, environments, and mock runs |
| `supabase_mcp` | stdio (npx) | Supabase databases, RLS policies, migrations, edge functions |
| `figma_figma` | stdio (npx) | Figma design frames, components, design tokens, FigJam diagrams |
| `canva_canva` | stdio (npx) | Canva design generation, templates, image asset management |
| `notion_notion` | stdio (npx) | Notion databases, pages, blocks, comments, and workspace search |
| `linear_linear` | stdio (npx) | Linear issues, cycles, projects, and milestones |
| `stripe_stripe` | stdio (npx) | Stripe billing, products, invoices, customers, and checkout |
| `vercel-plugin_vercel` | stdio (npx) | Vercel projects, deployments, env vars, domains, sandboxes, logs |

---

## 3. Installed Plugins (37 Plugins in `C:\Users\a7med\.gemini\config\plugins\`)

| Plugin | Skills Count | Primary Domain |
| :--- | :--- | :--- |
| `advanced-engineering` | 8 | Advanced senior engineering suite: Agent Supercharged OS, System Design Arc |
| `agent-reach` | 0 |  |
| `android-cli-plugin` | 3 | Core tools and knowledge required to develop for Android. |
| `atlassian-twg-cli` | 1 | Teamwork Graph CLI is Atlassian's agent-first interface to your entire work |
| `auth0` | 1 | Add Auth0 authentication to any app: login, MFA, SSO, Organizations, RBAC,  |
| `base44` | 3 | Build and deploy Base44 full-stack apps: CLI project management, JavaScript |
| `browse` | 1 | Give your agent a real browser: navigate, click, type, screenshot, and extr |
| `canva` | 6 | Create, edit, review, resize, and brand-check Canva designs with the Canva  |
| `chrome-devtools-plugin` | 6 | Reliable automation, in-depth debugging, and performance analysis in Chrome |
| `context7` | 1 | Up-to-date documentation lookup. Pull version-specific documentation and co |
| `creator-studio` | 2 | High-conversion viral social creator studio: Reels scripts, 10-slide viral  |
| `figma` | 16 | Turn Figma designs into production code, map components with Code Connect,  |
| `firebase` | 13 | Prototype, build & run modern apps that users love with Firebase's backend, |
| `gcalendar` | 1 | Check availability, schedule events, and RSVP. |
| `gdocs` | 1 | Read, draft, and edit docs. |
| `gdrive` | 1 | Search, upload, download, and share files. |
| `gemini-api` | 3 | Build applications with the Gemini Interactions API and Live API, including |
| `google-antigravity-sdk` | 1 | Using the Google Antigravity Python SDK to build AI agents |
| `google-developer-knowledge` | 1 | Search and retrieve official documentation across Google Cloud, Gemini, And |
| `google_maps_platform` | 1 | Integration skill and tools for Google Maps Platform APIs |
| `gsheets` | 1 | Read, write, and format spreadsheets. |
| `gslides` | 1 | Read, edit, and export presentations. |
| `linear` | 0 | The product development system for teams and agents. Manage issues, project |
| `mobbin` | 4 | Give your AI agent 600,000+ real app screens, and the skills to use them. I |
| `modern-web-guidance-plugin` | 2 | Keep your coding agent up to date with the latest web best practices. |
| `multi-agent-orchestrator` | 2 | Enterprise multi-agent organization and governance: Paperclip company org c |
| `netlify` | 15 | Build and deploy on Netlify: functions, edge functions, blobs, database, id |
| `notion` | 7 | Connect Antigravity to your Notion workspace with the Notion MCP server, pl |
| `postman` | 17 | Equip Antigravity with specialized Postman skills for the complete API life |
| `qodo` | 5 | Set up Qodo, explore code and repository history, review local changes, and |
| `reverse-engineering` | 2 | Reverse engineering and binary deconstruction suite: Mimic API extractor (t |
| `sir-autonomy` | 2 | Zero-approval autonomous browser bridge and Windows computer use for Antigr |
| `sir-ecosystem` | 3 | Unified orchestration plugin for Sir Ahmed's 23 enterprise workspaces, 10 A |
| `sir-ecosystem-suite` | 1 | Sir Ahmed Official AI Operator & Laptop Management Suite: multi-platform en |
| `stripe` | 0 | Accept payments and grow your business. Stripe's official MCP server enable |
| `supabase` | 2 | Official Supabase plugin for Antigravity with Supabase skills and MCP acces |
| `superpowers` | 15 | Make your coding agent a better engineer |
| `unity` | 32 | Unity's official plugin for Antigravity, with curated skills for game devel |
| `vercel-plugin` | 37 | Build and deploy web apps and AI agents on Vercel with skills for Next.js,  |

---

## 4. Master Skills Directory (253 Skills Grouped by Domain)

### Autonomy, Browser & Computer Use (9 skills)

| Skill Name | Trigger / High-Level Purpose | File Link |
| :--- | :--- | :--- |
| `agent-supercharged-os` | Engineering OS: 4-phase discipline (Plan, Test, Implement, Review). | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/advanced-engineering/skills/agent-supercharged-os/SKILL.md) |
| `browse` | Browserbase browser automation CLI for remote browsing, navigation, clicking. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/browse/skills/browse/SKILL.md) |
| `sir-browser` | Zero-prompt autonomous Chrome browser bridge and automation. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/sir-autonomy/skills/sir-browser/SKILL.md) |
| `sir-computer-use` | Autonomous Windows desktop control: mouse, keyboard, and screen. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/sir-autonomy/skills/sir-computer-use/SKILL.md) |
| `diagnosing-superpowers` | Diagnose superpowers session issues, audit execution transcripts. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/superpowers/skills/diagnosing-superpowers/SKILL.md) |
| `dispatching-parallel-agents` | Use when facing 2+ independent tasks that can be worked on without shared. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/superpowers/skills/dispatching-parallel-agents/SKILL.md) |
| `executing-plans` | Execute implementation plans step-by-step with verified milestones. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/superpowers/skills/executing-plans/SKILL.md) |
| `using-superpowers` | Use when starting any conversation, establishes how to find and use skills. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/superpowers/skills/using-superpowers/SKILL.md) |
| `writing-plans` | Use when you have a spec or requirements for a multi-step task. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/superpowers/skills/writing-plans/SKILL.md) |

### Engineering Standards, Quality & TDD (95 skills)

| Skill Name | Trigger / High-Level Purpose | File Link |
| :--- | :--- | :--- |
| `ponytail-yagni-optimizer` | YAGNI minimalist engineering to cut code bloat and dependencies. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/advanced-engineering/skills/ponytail-yagni-optimizer/SKILL.md) |
| `skills-discovery-engine` | Search, evaluate, and install skills from skills.sh and GitHub registries. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/advanced-engineering/skills/skills-discovery-engine/SKILL.md) |
| `twg-setup` | Install, upgrade, authenticate, or repair `twg` for your coding agent. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/atlassian-twg-cli/skills/twg-setup/SKILL.md) |
| `base44-cli` | The base44 CLI is used for EVERYTHING related to base44 projects. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/base44/skills/base44-cli/SKILL.md) |
| `base44-sdk` | The base44 SDK is the library to communicate with base44 services. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/base44/skills/base44-sdk/SKILL.md) |
| `base44-troubleshooter` | Troubleshoot production issues using backend function logs and workflow. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/base44/skills/base44-troubleshooter/SKILL.md) |
| `chrome-devtools` | Automate browsers, inspect network requests, debug DOM/CSS. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/chrome-devtools-plugin/skills/chrome-devtools/SKILL.md) |
| `cookie-debugging` | Inspect, test, and debug cookies, sessions, authentication headers. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/chrome-devtools-plugin/skills/cookie-debugging/SKILL.md) |
| `debug-optimize-lcp` | Debug and optimize Largest Contentful Paint (LCP) and Core Web Vitals. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/chrome-devtools-plugin/skills/debug-optimize-lcp/SKILL.md) |
| `memory-leak-debugging` | Diagnoses and resolves memory leaks in JavaScript/Node.js applications. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/chrome-devtools-plugin/skills/memory-leak-debugging/SKILL.md) |
| `troubleshooting` | Troubleshoot Chrome DevTools MCP connection and target issues. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/chrome-devtools-plugin/skills/troubleshooting/SKILL.md) |
| `context7-mcp` | This skill should be used when the user asks about libraries, frameworks. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/context7/skills/context7-mcp/SKILL.md) |
| `extension-to-functions-codebase` | Convert Firebase Extensions into standalone Cloud Functions codebases or. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/firebase/skills/extension_to_functions_codebase/SKILL.md) |
| `xcode-project-setup` | Modify Xcode projects (.pbxproj) safely to add Swift Packages and link. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/firebase/skills/xcode_project_setup/SKILL.md) |
| `google-antigravity-sdk` | Design, build, and debug autonomous AI agents with Google Antigravity SDK. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/google-antigravity-sdk/skills/google-antigravity-sdk/SKILL.md) |
| `google-maps-platform` | Manage Android SDK components, build projects. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/google_maps_platform/skills/SKILL.md) |
| `best-practices` | Tells your agent what Mobbin can and can't do and how the Mobbin skills. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/mobbin/skills/best-practices/SKILL.md) |
| `plain-writing` | Makes every report a Mobbin skill writes read like a person wrote it. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/mobbin/skills/plain-writing/SKILL.md) |
| `search` | Gets better results from every Mobbin search. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/mobbin/skills/search/SKILL.md) |
| `chrome-extensions` | Build, debug, and publish Manifest V3 Chrome extensions, content scripts. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/modern-web-guidance-plugin/skills/chrome-extensions/SKILL.md) |
| `claude-council` | 4-seat advisory council (Visionary, Skeptic, Investor, Justice) to vet architecture. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/multi-agent-orchestrator/skills/claude-council/SKILL.md) |
| `paperclip-orchestrator` | Coordinates multi-agent hierarchies as a virtual company. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/multi-agent-orchestrator/skills/paperclip-orchestrator/SKILL.md) |
| `ai-readiness` | Use when assessing or improving how well AI agents can discover, call. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/postman/skills/ai-readiness/SKILL.md) |
| `bootstrap` | Bootstrap and repair repositories with Vercel databases, environment pulling. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/postman/skills/bootstrap/SKILL.md) |
| `ci-integration` | Use when adding API tests, structural or governance lint. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/postman/skills/ci-integration/SKILL.md) |
| `collection-schema-v3` | Use when writing or debugging local Postman v3 collection and environment. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/postman/skills/collection-schema-v3/SKILL.md) |
| `datasets` | Use when a collection needs queried or joined test inputs. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/postman/skills/datasets/SKILL.md) |
| `flows` | Use when running, deploying, or debugging an existing Postman Flow. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/postman/skills/flows/SKILL.md) |
| `performance-testing` | Use when load-testing or benchmarking an API with concurrent virtual users. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/postman/skills/performance-testing/SKILL.md) |
| `variables` | Use when parameterizing requests across environments. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/postman/skills/variables/SKILL.md) |
| `webhook-testing` | Capture, forward to localhost, replay. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/postman/skills/webhook-testing/SKILL.md) |
| `qodo-codebase-wisdom` | Understand how code works, how a change was done before. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/qodo/skills/qodo-codebase-wisdom/SKILL.md) |
| `qodo-review-notes` | Review local changes and pull requests with Qodo during coding milestones. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/qodo/skills/qodo-review-notes/SKILL.md) |
| `qodo-review-resolver` | Review local changes and pull requests with Qodo during coding milestones. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/qodo/skills/qodo-review-resolver/SKILL.md) |
| `qodo-review` | Review local changes and pull requests with Qodo during coding milestones. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/qodo/skills/qodo-review/SKILL.md) |
| `qodo-setup` | Set up Qodo in a coding agent — install the CLI, sign in, and verify tools. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/qodo/skills/qodo-setup/SKILL.md) |
| `sir-ecosystem-orchestrator` | Orchestrator for Sir Ahmed's 23 enterprise workspaces. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/sir-ecosystem/skills/sir-ecosystem-orchestrator/SKILL.md) |
| `brainstorming` | You MUST use this before any creative work, creating features. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/superpowers/skills/brainstorming/SKILL.md) |
| `finishing-a-development-branch` | Use when implementation is complete, all tests pass. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/superpowers/skills/finishing-a-development-branch/SKILL.md) |
| `receiving-code-review` | Use when receiving code review feedback, before implementing suggestions. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/superpowers/skills/receiving-code-review/SKILL.md) |
| `requesting-code-review` | Use when completing tasks, implementing major features. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/superpowers/skills/requesting-code-review/SKILL.md) |
| `subagent-driven-development` | Execute implementation plans using parallel subagents for independent tasks. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/superpowers/skills/subagent-driven-development/SKILL.md) |
| `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/superpowers/skills/systematic-debugging/SKILL.md) |
| `test-driven-development` | Use when implementing any feature or bugfix, before writing implementation code | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/superpowers/skills/test-driven-development/SKILL.md) |
| `using-git-worktrees` | Use when starting feature work that needs isolation from current workspace. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/superpowers/skills/using-git-worktrees/SKILL.md) |
| `verification-before-completion` | Use when about to claim work is complete, fixed, or passing. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/superpowers/skills/verification-before-completion/SKILL.md) |
| `writing-skills` | Use when creating new skills, editing existing skills. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/superpowers/skills/writing-skills/SKILL.md) |
| `asset-transformer-toolkit` | Imports 3D models and point clouds with Asset Transformer Toolkit. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/asset-transformer-toolkit/SKILL.md) |
| `create-2d-physics` | Creates and fixes Unity 2D physics in both systems. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/create-2d-physics/SKILL.md) |
| `generate-editor-search-query` | Generates Unity Search queries and opens the Search window to find assets. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/generate-editor-search-query/SKILL.md) |
| `implement-in-app-purchases` | Implements, configures, and debugs Unity In-App Purchases. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/implement-in-app-purchases/SKILL.md) |
| `initialize-ai-navigation` | Sets up and configures Unity AI Navigation, including NavMesh surfaces. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/initialize-ai-navigation/SKILL.md) |
| `localization` | Sets up and configures Unity Localization, including locales. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/localization/SKILL.md) |
| `optimize-text-mesh-pro` | Optimizes TextMeshPro rendering, memory, and font setup. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/optimize-text-mesh-pro/SKILL.md) |
| `optimize-web` | Optimizes Unity WebGL and WebGPU builds for smaller downloads. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/optimize-web/SKILL.md) |
| `physics-3d-collision` | Diagnoses 3D PhysX collision and trigger problems. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/physics-3d-collision/SKILL.md) |
| `setup-multiplayer-services` | Guides real-time online multiplayer with Unity Multiplayer Services. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/setup-multiplayer-services/SKILL.md) |
| `setup-vivox-voice-chat` | Adds and configures in-game voice and text chat with Unity Vivox. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/setup-vivox-voice-chat/SKILL.md) |
| `shader-graph-create-custom-node` | Generates custom Shader Graph nodes from HLSL code. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/shader-graph-create-custom-node/SKILL.md) |
| `ai-sdk` | Build AI features, streaming chat, and tool calling with Vercel AI SDK. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/ai-sdk/SKILL.md) |
| `bootstrap` | Bootstrap and repair repositories with Vercel databases, environment pulling. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/bootstrap/SKILL.md) |
| `chat-sdk` | Build multi-platform chat bots for Slack, Teams, Discord. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/chat-sdk/SKILL.md) |
| `create-a-backend` | Architect and implement scalable serverless backends and database schemas. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/create-a-backend/SKILL.md) |
| `custom-metrics` | Emit and query Vercel Custom Metrics. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/custom-metrics/SKILL.md) |
| `domains` | Search, register, connect, transfer. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/domains/SKILL.md) |
| `env-vars` | Vercel environment variable expert guidance. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/env-vars/SKILL.md) |
| `eve` | Guidance for the eve durable AI agent framework, tools, sandboxes, subagents. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/eve/SKILL.md) |
| `flags-sdk` | Implement feature flags in Next.js and SvelteKit using the Flags SDK. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/flags-sdk/SKILL.md) |
| `is-agentic` | Audit and score web applications and MCP endpoints for AI agent readiness. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/is-agentic/SKILL.md) |
| `marketplace` | Discover, install, and configure third-party database, auth. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/marketplace/SKILL.md) |
| `microfrontends` | Architect, configure, and route multi-zone microfrontends on Vercel. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/microfrontends/SKILL.md) |
| `offload-to-sandbox` | Offload resource-heavy builds, test suites. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/offload-to-sandbox/SKILL.md) |
| `react-best-practices` | React and Next.js performance rules, eliminating waterfalls. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/react-best-practices/SKILL.md) |
| `routing-middleware` | Vercel Routing Middleware guidance, request interception before cache. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/routing-middleware/SKILL.md) |
| `runtime-cache` | Configure Vercel Runtime Cache API for ephemeral edge and function caching. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/runtime-cache/SKILL.md) |
| `verification` | Full-story verification, infers what the user is building. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/verification/SKILL.md) |
| `workflow` | Vercel Workflow SDK expert guidance. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/workflow/SKILL.md) |
| `all-skills` | Master meta-skill unifying all Antigravity design, engineering, mobile UX. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/all-skills/SKILL.md) |
| `customization-architect` | Master engine for auditing, token-optimizing. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/customization-architect/SKILL.md) |
| `database-reliability-transactions` | Atomic transactions with rollback, client idempotency keys, query indexing. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/database-reliability-transactions/SKILL.md) |
| `excel-generator` | Generate styled Excel workbooks with openpyxl, native formulas, and charts. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/excel-generator/SKILL.md) |
| `github-gem-seeker` | Discovery, scraping, and evaluation of high-potential open-source. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/github-gem-seeker/SKILL.md) |
| `google-preferred-sources` | Implements Google Preferred Sources badges, Google Follow RSS tags. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/google-preferred-sources/SKILL.md) |
| `graphify-ast-memory` | Transform codebases into deterministic AST knowledge graphs. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/graphify-ast-memory/SKILL.md) |
| `internet-skill-finder` | Internet research engine for discovering, vetting, benchmarking. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/internet-skill-finder/SKILL.md) |
| `karpathy-skills` | Codifies Andrej Karpathy's 4 core rules for AI software engineering. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/karpathy-skills/SKILL.md) |
| `master-production-directive` | Master directive, full-stack engineering, zero-mock persistence, AST graphs. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/master-production-directive/SKILL.md) |
| `modern-app-engineering` | Senior architecture guidelines for production desktop (WinUI/Tauri). | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/modern-app-engineering/SKILL.md) |
| `production-engineering-standards` | Production-grade engineering standards, zero-mock persistence. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/production-engineering-standards/SKILL.md) |
| `pulse-engineering` | Expert guidelines for engineering lightweight. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/pulse-engineering/SKILL.md) |
| `repomix-token-optimizer` | Compress and pack codebases using Tree-sitter AST signature extraction. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/repomix-token-optimizer/SKILL.md) |
| `skill-creator` | Meta-skill architect that analyzes incoming user capabilities, workflows. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/skill-creator/SKILL.md) |
| `skill-repair` | Fix and re-install agent skills that failed installation and surgically. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/skill-repair/SKILL.md) |
| `typst-pdf-maker` | Typeset and compile agency-grade, publication-quality PDF documents. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/typst-pdf-maker/SKILL.md) |
| `sir-session-end` | End-of-session ritual for SIR work, update the checkpoint. | [`SKILL.md`](file:///D:/Projects/.agents/skills/sir-session-end/SKILL.md) |

### Design, UI/UX, Motion & Taste (40 skills)

| Skill Name | Trigger / High-Level Purpose | File Link |
| :--- | :--- | :--- |
| `emil-motion-impeccable` | Agency-grade spring physics, fluid micro-interactions, layout morphing. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/advanced-engineering/skills/emil-motion-impeccable/SKILL.md) |
| `system-design-architect` | Large-scale system design patterns, distributed caching, rate limiters. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/advanced-engineering/skills/system-design-architect/SKILL.md) |
| `canva-brand-check` | Check a Canva design against a brand kit and report where it diverges. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/canva/skills/brand-check/SKILL.md) |
| `canva-bulk-create` | Bulk-create Canva designs from tabular data using a brand template with. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/canva/skills/bulk-create/SKILL.md) |
| `canva-edit-design` | Make edits to an existing Canva design, change or fix text. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/canva/skills/edit-design/SKILL.md) |
| `canva-design-feedback` | Read a Canva design and return structured, actionable design feedback. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/canva/skills/get-design-feedback/SKILL.md) |
| `canva-implement-feedback` | Implement reviewer feedback on a Canva design. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/canva/skills/implement-feedback/SKILL.md) |
| `canva-resize-for-social-media` | Resize a Canva design into multiple social media formats. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/canva/skills/resize-for-social-media/SKILL.md) |
| `a11y-debugging` | Uses Chrome DevTools MCP for accessibility (a11y) debugging and auditing. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/chrome-devtools-plugin/skills/a11y-debugging/SKILL.md) |
| `motion-graphics-engine` | Programmatic motion graphics, kinetic typography. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/creator-studio/skills/motion-graphics-engine/SKILL.md) |
| `figma-code-connect` | Create and maintain Figma Code Connect (.figma.ts) files mapping Figma. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/figma/skills/figma-code-connect/SKILL.md) |
| `figma-code-workflows` | Import local HTML, code layers, and web projects into Figma design frames. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/figma/skills/figma-code-workflows/SKILL.md) |
| `figma-create-new-file` | Always use this skill when the user wants to create a new Figma Design. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/figma/skills/figma-create-new-file/SKILL.md) |
| `figma-design-to-code` | Implement and translate Figma frames, screens. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/figma/skills/figma-design-to-code/SKILL.md) |
| `figma-generate-design` | Translate application pages, views, modals, forms. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/figma/skills/figma-generate-design/SKILL.md) |
| `figma-generate-diagram` | Generate diagrams, flowcharts, ERDs, sequence diagrams. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/figma/skills/figma-generate-diagram/SKILL.md) |
| `figma-generate-library` | Build and update Figma design system libraries, tokens, variables. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/figma/skills/figma-generate-library/SKILL.md) |
| `figma-generative-plugins` | Create, author, and extend reusable generative Figma plugins. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/figma/skills/figma-generative-plugins/SKILL.md) |
| `figma-implement-motion` | Translate Figma motion, keyframes, transitions. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/figma/skills/figma-implement-motion/SKILL.md) |
| `figma-shaders` | Author, edit, and iterate on custom procedural shader fills and effects in. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/figma/skills/figma-shaders/SKILL.md) |
| `figma-spec` | Read, create, review, and comment on technical specs in Figma. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/figma/skills/figma-spec/SKILL.md) |
| `figma-swiftui` | Bi-directional translation between SwiftUI code and Figma designs, screens. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/figma/skills/figma-swiftui/SKILL.md) |
| `figma-use-figjam` | Use Figma's use_figma MCP tool in the FigJam context. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/figma/skills/figma-use-figjam/SKILL.md) |
| `figma-use-motion` | Add, inspect, and edit animations, easing. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/figma/skills/figma-use-motion/SKILL.md) |
| `figma-use-slides` | Use Figma's use_figma MCP tool in the Slides context. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/figma/skills/figma-use-slides/SKILL.md) |
| `figma-use` | Core protocol for running JavaScript in the Figma Plugin API context. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/figma/skills/figma-use/SKILL.md) |
| `redesign-screen` | Redesign any screen from patterns real apps ship. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/mobbin/skills/redesign-screen/SKILL.md) |
| `modern-web-guidance` | Up-to-date modern web platform best practices for HTML, CSS, client JS. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/modern-web-guidance-plugin/skills/modern-web-guidance/SKILL.md) |
| `notion-database-designer` | Turns scattered notes and recurring work into useful Notion trackers for. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/notion/skills/notion-database-designer/SKILL.md) |
| `build-gtk` | Builds node-based Editor tools with Unity Graph Toolkit (GTK) on Unity 6.6+. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/build-gtk/SKILL.md) |
| `build-live-game` | Builds and operates a live game's backend with Unity Gaming Services. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/build-live-game/SKILL.md) |
| `ui-imgui` | Generates and modifies Unity IMGUI editor code such as EditorWindows. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/ui-imgui/SKILL.md) |
| `ui-ugui` | Understands, edits, and generates Unity uGUI Canvas hierarchies. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/ui-ugui/SKILL.md) |
| `ui-uitk` | Understands, edits, and generates Unity UI Toolkit UXML and USS with flex. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/ui-uitk/SKILL.md) |
| `ui` | Routes Unity UI requests to the right framework skill. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/ui/SKILL.md) |
| `build-agents` | Default guidance for building AI agents. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/build-agents/SKILL.md) |
| `anti-vibecoded-design-system` | Bespoke, high-contrast, tactile UI eliminating AI design clichés. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/anti-vibecoded-design-system/SKILL.md) |
| `cognitive-product-intuition` | Human intuition and product logic, eliminates UI clone syndrome. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/cognitive-product-intuition/SKILL.md) |
| `modern-ui-ux-design-system` | Design and implement modern, scientific UI/UX design systems, tokens. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/modern-ui-ux-design-system/SKILL.md) |
| `taste-design-engine` | Premium design taste, self-auditing, image-to-code replication. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/taste-design-engine/SKILL.md) |

### Cloud, Hosting & Backend (Vercel, Supabase, Firebase, Netlify) (48 skills)

| Skill Name | Trigger / High-Level Purpose | File Link |
| :--- | :--- | :--- |
| `omniroute-resilience-gateway` | AI model routing gateway with automated multi-provider failover. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/advanced-engineering/skills/omniroute-resilience-gateway/SKILL.md) |
| `firebase-ai-logic-basics` | Integrate Firebase AI Logic (Gemini API) into web apps. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/firebase/skills/firebase_ai_logic_basics/SKILL.md) |
| `firebase-app-hosting-basics` | Deploy and manage full-stack SSR web applications. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/firebase/skills/firebase_app_hosting_basics/SKILL.md) |
| `firebase-auth-basics` | Set up and configure Firebase Authentication for user sign-in. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/firebase/skills/firebase_auth_basics/SKILL.md) |
| `firebase-basics` | Foundational Firebase CLI setup, CLI login, project creation. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/firebase/skills/firebase_basics/SKILL.md) |
| `firebase-crashlytics` | Set up, provision, and integrate Firebase Crashlytics SDKs for real-time. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/firebase/skills/firebase_crashlytics/SKILL.md) |
| `firebase-data-connect` | Build and deploy Firebase SQL Connect backends with PostgreSQL. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/firebase/skills/firebase_data_connect_basics/SKILL.md) |
| `firebase-firestore` | Set up, query, and configure Cloud Firestore databases, data models. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/firebase/skills/firebase_firestore/SKILL.md) |
| `firebase-hosting-basics` | Deploy and configure classic Firebase Hosting for static websites, SPAs. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/firebase/skills/firebase_hosting_basics/SKILL.md) |
| `firebase-remote-config-basics` | Manage Firebase Remote Config templates, feature flags, loading strategies. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/firebase/skills/firebase_remote_config_basics/SKILL.md) |
| `firebase-security-rules-auditor` | Audit Firebase Firestore and Cloud Storage security rules for. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/firebase/skills/firebase_security_rules_auditor/SKILL.md) |
| `firestore-rules-creation` | Author and harden production Cloud Firestore Security Rules. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/firebase/skills/firestore_rules_creation/SKILL.md) |
| `retrieving-developer-knowledge` | Search and retrieve official Google developer documentation across Google. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/google-developer-knowledge/skills/retrieving-developer-knowledge/SKILL.md) |
| `netlify-access-control` | Picks the right Netlify site-protection layer and disambiguates the three. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/netlify/skills/netlify-access-control/SKILL.md) |
| `netlify-agent-runner` | Run AI agent tasks remotely on Netlify using Claude, Codex, or Gemini. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/netlify/skills/netlify-agent-runner/SKILL.md) |
| `netlify-ai-gateway` | Use Netlify AI Gateway to call OpenAI, Anthropic Claude, Google Gemini. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/netlify/skills/netlify-ai-gateway/SKILL.md) |
| `netlify-blobs` | Store and retrieve unstructured objects, files. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/netlify/skills/netlify-blobs/SKILL.md) |
| `netlify-caching` | Cache dynamic and static responses on Netlify's CDN from Functions. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/netlify/skills/netlify-caching/SKILL.md) |
| `netlify-config` | Configure Netlify builds and routing via netlify.toml, _redirects, and _headers. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/netlify/skills/netlify-config/SKILL.md) |
| `netlify-database` | Zero-config Postgres for Netlify apps via @netlify/database. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/netlify/skills/netlify-database/SKILL.md) |
| `netlify-deploy` | Create, configure, and manage Netlify deploys from code. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/netlify/skills/netlify-deploy/SKILL.md) |
| `netlify-edge-functions` | Write, route, cache, and debug Netlify Edge Functions. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/netlify/skills/netlify-edge-functions/SKILL.md) |
| `netlify-forms` | Serverless form handling on Netlify-hosted sites. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/netlify/skills/netlify-forms/SKILL.md) |
| `netlify-frameworks` | Deploy and configure web frameworks on Netlify. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/netlify/skills/netlify-frameworks/SKILL.md) |
| `netlify-functions` | Write, configure, and deploy Netlify serverless functions in TypeScript. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/netlify/skills/netlify-functions/SKILL.md) |
| `netlify-identity` | Add user authentication to a Netlify site with @netlify/identity. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/netlify/skills/netlify-identity/SKILL.md) |
| `netlify-image-cdn` | Transforms images on demand via Netlify Image CDN's /.netlify/images. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/netlify/skills/netlify-image-cdn/SKILL.md) |
| `netlify-mcp-servers` | Build, deploy, and secure Model Context Protocol (MCP) servers on Netlify. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/netlify/skills/netlify-mcp-servers/SKILL.md) |
| `notion-knowledge-capture` | Captures conversations and supplied notes as Notion wiki pages. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/notion/skills/notion-knowledge-capture/SKILL.md) |
| `supabase-postgres-best-practices` | Postgres performance and schema design best practices, query optimization. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/supabase/skills/supabase-postgres-best-practices/SKILL.md) |
| `supabase` | Manage Supabase projects, databases, auth, Edge Functions, Realtime, storage. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/supabase/skills/supabase/SKILL.md) |
| `access-protected-vercel-deployment` | Access and test protected Vercel preview or production deployments using. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/access-protected-vercel-deployment/SKILL.md) |
| `ai-gateway` | Configure Vercel AI Gateway for multi-provider LLM routing, failover. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/ai-gateway/SKILL.md) |
| `cdn-caching` | Debug Vercel CDN caching, cache hit rate, stale content. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/cdn-caching/SKILL.md) |
| `daemons` | Configure and deploy long-running background workers, queue consumers. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/daemons/SKILL.md) |
| `deployments-cicd` | Vercel deployment and CI/CD expert guidance. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/deployments-cicd/SKILL.md) |
| `knowledge-update` | Corrects outdated LLM knowledge about the Vercel platform and introduces. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/knowledge-update/SKILL.md) |
| `queues` | Buffer asynchronous traffic and background tasks with durable. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/queues/SKILL.md) |
| `vercel-agent` | Vercel Agent guidance, dashboard and Slack chat, code review. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/vercel-agent/SKILL.md) |
| `vercel-cli` | Deploy, inspect logs, pull environment variables, manage domains. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/vercel-cli/SKILL.md) |
| `vercel-connect` | Securely obtain and manage scoped credentials, OAuth tokens. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/vercel-connect/SKILL.md) |
| `vercel-firewall` | Configure DDoS protection, WAF rules, IP blocking, rate limiting. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/vercel-firewall/SKILL.md) |
| `vercel-flags` | Plan, configure, and evaluate feature flags, A/B tests. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/vercel-flags/SKILL.md) |
| `vercel-functions` | Configure and optimize serverless Vercel Functions, Fluid Compute. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/vercel-functions/SKILL.md) |
| `vercel-sandbox` | Run untrusted code safely in ephemeral Firecracker microVM sandboxes. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/vercel-sandbox/SKILL.md) |
| `vercel-services` | Configure multi-service architectures, backend services. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/vercel-services/SKILL.md) |
| `vercel-storage` | Vercel storage expert guidance, Blob, Global Config (formerly Edge Config). | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/vercel-storage/SKILL.md) |
| `vercel-tracing` | Configure OpenTelemetry tracing for Vercel functions. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/vercel-tracing/SKILL.md) |

### Game Development & Real-Time (Unity, Graphics, Audio) (14 skills)

| Skill Name | Trigger / High-Level Purpose | File Link |
| :--- | :--- | :--- |
| `2d-pixel-perfect` | Sets up, diagnoses, and fixes pixel perfect 2D rendering with. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/2d-pixel-perfect/SKILL.md) |
| `audio-setup-mixers` | Routes Audio Sources into existing Audio Mixer Groups. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/audio-setup-mixers/SKILL.md) |
| `create-tile-palette-or-rule-tiles` | Create a 2D tile palette from sprites or textures. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/create-tile-palette-or-rule-tiles/SKILL.md) |
| `levelplay-unity-integration` | Integrates the LevelPlay ad mediation SDK via the Ads Mediation package. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/levelplay-unity-integration/SKILL.md) |
| `manage-sprite-atlas` | Manages SpriteAtlas assets through a prebuild pipeline. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/manage-sprite-atlas/SKILL.md) |
| `migrate-birp-to-urp` | Plans, executes, and troubleshoots migration from the Built-in Render. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/migrate-birp-to-urp/SKILL.md) |
| `new-unity-project` | Guides creating a new Unity project, gathering concept, platforms. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/new-unity-project/SKILL.md) |
| `optimize-audio` | Optimize audio memory, CPU cost, and playback quality in Unity. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/optimize-audio/SKILL.md) |
| `sprite-editor` | Edits Unity sprite rectangles, borders, pivots, outlines. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/sprite-editor/SKILL.md) |
| `sprite-segment-3x3grid` | Segments a Sprite texture into a 3x3 grid and outputs a pattern of cells. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/sprite-segment-3x3grid/SKILL.md) |
| `unity-cli` | Controls the Unity Editor and projects from the command line. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/unity-cli/SKILL.md) |
| `unity-package-management` | Add, remove, upgrade, and resolve Unity package dependencies. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/unity-package-management/SKILL.md) |
| `urp-postprocessing` | Sets up, configures, and debugs URP post-processing with the Volume framework. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/urp-postprocessing/SKILL.md) |
| `validate-urp-render-graph-renderer-feature` | Reviews a Unity 6 URP ScriptableRendererFeature that uses the Render Graph. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/unity/skills/validate-urp-render-graph-renderer-feature/SKILL.md) |

### Mobile & Cross-Platform (Android, Compose, Flutter) (4 skills)

| Skill Name | Trigger / High-Level Purpose | File Link |
| :--- | :--- | :--- |
| `android-cli` | Manage Android SDK components, build projects, and run adb commands. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/android-cli-plugin/skills/SKILL.md) |
| `compose-preview` | Render and review Jetpack Compose @Preview functions interactively. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/android-cli-plugin/skills/compose-preview/SKILL.md) |
| `android-device-hub` | Manage, start, stop, and mirror Android Virtual Devices (AVDs). | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/android-cli-plugin/skills/device-hub/SKILL.md) |
| `mobile-ergonomics-polish` | Mobile UX polish, eliminates horizontal scroll, adds fluid drawer menus. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/mobile-ergonomics-polish/SKILL.md) |

### Security, Auth & Compliance (OWASP, Zero-Trust, Rules) (7 skills)

| Skill Name | Trigger / High-Level Purpose | File Link |
| :--- | :--- | :--- |
| `direct-action-shield` | Suppress conversational filler and deliver surgical, immediate action steps. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/advanced-engineering/skills/direct-action-shield/SKILL.md) |
| `vibe-auth-hardening` | Harden web auth: secure cookies, server-side RBAC, 2FA, and rate limiting. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/advanced-engineering/skills/vibe-auth-hardening/SKILL.md) |
| `auth0` | Authenticate users and protect Next.js routes with Auth0. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/auth0/skills/auth0/SKILL.md) |
| `auth` | Integrate user authentication in Next.js, Clerk, Better Auth, Auth0. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/vercel-plugin/skills/auth/SKILL.md) |
| `legal-compliance-shield` | Ironclad legal compliance, privacy policies matching collection. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/legal-compliance-shield/SKILL.md) |
| `owasp-vulnerability-shield` | Audit and eliminate OWASP Top 10 vulnerabilities, injection, SSRF. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/owasp-vulnerability-shield/SKILL.md) |
| `zero-trust-security-hardening` | Zero-trust security, RLS tenant isolation, parameterized queries. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/zero-trust-security-hardening/SKILL.md) |

### API Engineering & Reverse Engineering (Postman, Traffic, Decompilation) (14 skills)

| Skill Name | Trigger / High-Level Purpose | File Link |
| :--- | :--- | :--- |
| `gemini-api-dev` | Build applications with the Google GenAI SDK, text generation. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/gemini-api/skills/gemini-api-dev/SKILL.md) |
| `gemini-live-api-dev` | Build real-time bidirectional streaming audio, video. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/gemini-api/skills/gemini-live-api-dev/SKILL.md) |
| `gemini-omni-flash-api` | Generative video editing, text-to-video, image-to-video. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/gemini-api/skills/gemini-omni-flash-api/SKILL.md) |
| `api-discovery` | Use when finding an API or owner, integrating a public provider. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/postman/skills/api-discovery/SKILL.md) |
| `api-documentation` | Use when defining or improving an API contract. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/postman/skills/api-documentation/SKILL.md) |
| `api-engineer` | Use when designing, implementing, mocking, testing, monitoring, documenting. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/postman/skills/api-engineer/SKILL.md) |
| `api-mocking` | Finds, builds, runs and publishes a stand-in for one API. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/postman/skills/api-mocking/SKILL.md) |
| `api-monitoring` | Use when setting up recurring API checks. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/postman/skills/api-monitoring/SKILL.md) |
| `api-simulation` | Runs your code for real against stand-ins for the HTTP services it calls. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/postman/skills/api-simulation/SKILL.md) |
| `api-testing` | Use when testing an endpoint, running collection assertions. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/postman/skills/api-testing/SKILL.md) |
| `postman-mcp-server` | Use when working through Postman MCP tools to inspect or change workspace. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/postman/skills/postman-mcp-server/SKILL.md) |
| `binary-reverse-engineer` | Decompile native binaries and APKs, trace execution. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/reverse-engineering/skills/binary-reverse-engineer/SKILL.md) |
| `mimic-api-extractor` | Reverse-engineers network traffic into typed Python and TypeScript client. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/reverse-engineering/skills/mimic-api-extractor/SKILL.md) |
| `website-traffic-analytics` | Audit web traffic, visitor telemetry, bounce rates, SEO keyword acquisition. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/website-traffic-analytics/SKILL.md) |

### Productivity, Workspace & Management (Notion, Google Workspace, Linear) (12 skills)

| Skill Name | Trigger / High-Level Purpose | File Link |
| :--- | :--- | :--- |
| `gcalendar` | Read, create, update, and manage Google Calendar events, meeting invites. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/gcalendar/skills/gcalendar/SKILL.md) |
| `gdocs` | Read, create, edit, format, and manage Google Docs documents, tables. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/gdocs/skills/gdocs/SKILL.md) |
| `gdrive` | Browse, search, upload, download, and manage Google Drive files. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/gdrive/skills/gdrive/SKILL.md) |
| `gsheets` | Read, write, format, sort, and manage Google Sheets spreadsheets, ranges. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/gsheets/skills/gsheets/SKILL.md) |
| `gslides` | Read, create, edit, and export Google Slides presentations, slides. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/gslides/skills/gslides/SKILL.md) |
| `notion-meeting-intelligence` | Prepares meeting agendas, internal pre-reads. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/notion/skills/notion-meeting-intelligence/SKILL.md) |
| `notion-research-documentation` | Researches questions across Notion sources and synthesizes cited briefs. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/notion/skills/notion-research-documentation/SKILL.md) |
| `notion-setup` | A guided setup flow to get the most out of Notion that is recommended for. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/notion/skills/notion-setup/SKILL.md) |
| `notion-spec-to-implementation` | Converts Notion product or technical specs into implementation plans. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/notion/skills/notion-spec-to-implementation/SKILL.md) |
| `notion-weekly-project-digest` | Produces evidence-based weekly project or team updates by comparing. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/notion/skills/notion-weekly-project-digest/SKILL.md) |
| `laptop-admin` | Official executive laptop management and autonomous ecosystem operator for. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/sir-ecosystem-suite/skills/laptop-admin/SKILL.md) |
| `pc-storage-guardian` | Storage capacity telemetry, safe temp & cache pruning. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/sir-ecosystem/skills/pc-storage-guardian/SKILL.md) |

### Media, Content & Social (Video, Graphics, Copywriting) (5 skills)

| Skill Name | Trigger / High-Level Purpose | File Link |
| :--- | :--- | :--- |
| `social-creator-studio` | High-conversion social content, Reels scripts, viral carousels. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/creator-studio/skills/social-creator-studio/SKILL.md) |
| `meta-social-sidecar` | Meta Facebook Page publishing automation, Remotion video render triggers. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/plugins/sir-ecosystem/skills/meta-social-sidecar/SKILL.md) |
| `high-conversion-copywriting` | Direct-response product copywriting, eliminates AI buzzwords. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/high-conversion-copywriting/SKILL.md) |
| `music-prompter` | Professional music prompt engineering for Suno v3.5/v4, Udio. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/music-prompter/SKILL.md) |
| `youtube-video-research` | YouTube competitive research, video transcript extraction. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/youtube-video-research/SKILL.md) |

### Business, Finance & Market Analysis (5 skills)

| Skill Name | Trigger / High-Level Purpose | File Link |
| :--- | :--- | :--- |
| `commercial-app-blueprint` | Commercial architecture blueprints, llms.txt, service silos, case studies. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/commercial-app-blueprint/SKILL.md) |
| `financial-analysis` | Corporate and project financial analysis, income statement (P&L). | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/financial-analysis/SKILL.md) |
| `open-seo-auditor` | SEO and GEO, keyword optimization, JSON-LD schemas. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/open-seo-auditor/SKILL.md) |
| `sir-ahmed-career-autopilot` | Job application, live multi-board scraper, ATS CV generation. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/sir-ahmed-career-autopilot/SKILL.md) |
| `stock-analysis` | Equity market research, technical analysis. | [`SKILL.md`](file:///C:/Users/a7med/.gemini/config/skills/stock-analysis/SKILL.md) |
