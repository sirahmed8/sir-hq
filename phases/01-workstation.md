# Phase 1 — Workstation, Claude Code and tools

> **Read first:** `START_HERE.md`, then `core/03-team.md` (roster, external workforce, usage) and `core/05-verify-first.md`. **When this phase is done:** add an entry to `ops/MISSION_LOG.md`, update `ops/HQ_CHECKPOINT.md` and `REQUIREMENTS.md`, send the short report (`core/07-reporting.md`), and continue with `phases/02-ahome-and-pc.md`.

**1.1 Update and diagnose.** Update Claude Code, run `claude doctor`, fix what it reports.

**1.2 Fix the Remote Control error** `CCR v2 worker registration failed for session cse_…: Request failed with status code 404`.

- Cause (a known Claude Code bug): a stale `bridge-pointer.json` makes `claude remote-control` re-adopt a session the server already deleted. It recovers (you see "Connected · Capacity 0/32") but repeats on every launch, forever.
- Fix:
  1. Stop all `claude remote-control` processes.
  2. In `%USERPROFILE%\.claude\projects\`, find the folders for the affected directories (AHome, AhmedAndHabiba, `D:\Projects`, any other that shows the error). Move only their `bridge-pointer.json` files into a backup folder.
  3. In each affected git repo, run `git worktree list`. For stale `.claude/worktrees/bridge-cse_*` worktrees whose owner process is dead: `git worktree remove --force <path>`, then `git worktree prune`.
  4. Restart `claude remote-control` and confirm the log shows a freshly registered worker with no 404.
- If it persists: update Claude Code again; re-login (`claude auth logout`, then `claude auth login`, choosing the claude.ai account); make sure `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN` and `ANTHROPIC_BASE_URL` are not set anywhere (Remote Control requires claude.ai subscription login); run with `--verbose --debug-file <path>` and read the log.
- Spawn modes: `same-dir` means all remote sessions share one working directory and can collide on the same files; `worktree` gives each session its own git worktree (git repos only). Press `w` to switch; the choice is saved per folder. Use `worktree` for single-repo servers and `same-dir` for the HQ server in `D:\Projects` (not a git repo), and rely on the locks protocol there.

**1.3 Every session reachable from the iPhone.**

- Set `"remoteControlAtStartup": true` in **user** settings (`%USERPROFILE%\.claude\settings.json`; project settings can't turn it on). Every interactive Claude Code session then auto-connects and appears in the Claude iOS app under **Code**.
- Claude Desktop app: Settings → Claude Code → "Connect new sessions to Remote Control": on.
- In `/config`, enable "Push when actions required" and "Push when Claude decides".
- **HQ server:** a small script `_SIR/scripts/rc-hq.ps1` runs `claude remote-control --name "SIR HQ" --spawn same-dir --capacity 8 --chrome` in `D:\Projects` inside a relaunch loop (server mode exits after about 10 minutes without network). A Task Scheduler task starts it at logon in Windows Terminal. `D:\Projects` is already trusted because this session runs there; any other folder becomes trusted by opening Claude Code in it once. New sessions started from the phone then begin in `D:\Projects` and can work on any project through the HQ `AGENTS.md`.
- Sessions live on this laptop: it must be on, awake, online, and running the Claude process. Apply a power plan: no sleep on AC power, lid close does nothing on AC, normal behavior on battery. Log the previous settings so they can be restored.
- Limitation to explain to Ahmed: the phone shows live Remote Control sessions. Old local conversations are resumed on the laptop with `claude --resume`; they don't all appear on the phone.
- Verify: send a test push and open a test session. Ahmed confirms from his iPhone whenever he sees it; don't wait for him.

**1.4 Permissions: "full permission", done safely.**

- Set `"permissions": { "defaultMode": "auto" }` in **user** settings (project settings ignore `auto`). Auto mode runs without routine prompts while a safety classifier blocks destructive or data-leaking actions. Do **not** use `bypassPermissions` on this laptop: it holds Ahmed's real accounts, money and social media, and bypass mode removes the safety net. It's meant for disposable containers.
- `permissions.additionalDirectories` (user settings): `D:\Projects`, `C:\Users\a7med\Desktop`, `D:\Projects\Backups`.
- Deny rules (enforced in every mode) for the Tier 3 cases you can express as tool patterns, for example force pushes. Test that each rule matches what you intend.
- Write the Tier 2 and Tier 3 boundaries into the global `CLAUDE.md` (1.9); the classifier reads them.
- **Standing permissions for the classifier:** auto mode blocks some actions by default, including merging a PR no human approved and production deploys. Ahmed's standing instruction is to work without asking him, so add precise natural-language rules to `autoMode.allow` in **user** settings (project settings can't set them). Examples: merging PRs in Ahmed's own repositories once required CI checks pass and the `reviewer` agent approved; deploying to production for products marked pre-launch in `.sir/project.yml`. Describe his GitHub account, Vercel and Firebase projects in `autoMode.environment` as trusted infrastructure. Keep the built-in safety defaults. Check the result with `claude auto-mode config`.
- Browser control: enable Claude in Chrome for sessions (`/chrome` or `--chrome`), and install Playwright MCP and Chrome DevTools MCP for testing. Use computer use for native apps where the session offers it.

**1.5 Agent teams.** Enable them per the current docs (currently the `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` environment setting in user settings `env`) and run a 2-teammate smoke test.

**1.6 Agent roster, hooks and skills.** Create the roster from A2 and the first skills from A1 rule 9, and add the `SubagentStop` hook next to the memory hooks from Phase 0. Test each.

**1.7 MCP servers, connectors, plugins and skills: a clean slate.**

- Inventory everything: `/mcp`, `claude mcp list`, `/plugin`, the skills list, and the claude.ai connectors available to Claude Code. For each, record status: connected, needs auth, failed, duplicate, or unused.
- Re-authenticate broken claude.ai connectors (`claude mcp login "claude.ai <Name>" --no-browser` prints a link), reconnect (`/mcp reconnect`), and remove dead or duplicate entries.
- Keep the always-on set lean (every enabled server costs context in every session). Use user scope for tools needed everywhere and project `.mcp.json` for project-specific ones. "Re-enable everything everywhere" would make every session slower and more expensive.
- Install missing essentials from official sources only (verify each exists and its current install command): GitHub (official server or the `gh` CLI), Firebase (the Firebase CLI's MCP server), Playwright, Chrome DevTools, Context7 (live library docs), Expo/EAS (if an official server exists), an Android emulator/device control server, Sentry, Cloudinary. Already connected and useful: Vercel, Figma, TickTick, Gmail, Google Calendar and Drive, Notion, Firecrawl, Supabase, Canva, Adobe, ElevenLabs, OpusClip, vidIQ, Indeed, PostHog, Microsoft Learn, Tarteel and UmmahAPI (verified Islamic content for SIR Deen). Plugins worth keeping enabled: engineering, design, data (`/data:build-dashboard`), SEO, social media / Postiz, small-business, marketing, legal (privacy, product).
- Mirror the essential MCP servers into Antigravity's MCP config (per its docs) so Gemini sessions get the same tools later.
- Record everything in `TOOLS.md`: what, why, scope, status, how to re-authenticate.

**1.8 Dev toolchain.** Install with winget or official installers, verify each, and log versions in `TOOLS.md`:

- Git (with `core.longpaths true`) and Windows long-path support; GitHub CLI; Node LTS with Corepack/pnpm; Python 3.12+; JDK 17 (Temurin).
- Android Studio and the SDK: platform-tools, cmdline-tools, build-tools, emulator, the latest platform (API 37), API 36, and the minSdk platform; system images. Set `ANDROID_HOME`, `JAVA_HOME` and `PATH`.
- Emulators, disk-aware: install only three system images (latest API, minSdk API, Wear OS). Make the minSdk one a plain AOSP image without Google Play, so it also covers phones without Google services. The latest-API phone, small phone, tablet and foldable (Pixel Fold profile) are device profiles sharing one image; add a minSdk phone and a round Wear OS watch. Delete images you stop using.
- Firebase CLI, Cloudflare's Wrangler CLI, Vercel CLI (non-commercial projects only), EAS CLI, Maestro (mobile e2e), Playwright browsers, gitleaks, ImageMagick (icon pipeline), ffmpeg (video), Visual Studio Build Tools (C++ workload) with the Windows SDK (signtool, the Windows App Certification Kit and the MSIX tools for Microsoft Store packages), 7-Zip.
- Ollama for local models. First check whether `AI_Models_Hub` already holds models, and point Ollama's model folder at it instead of downloading duplicates.
- n8n (1.11), the Antigravity CLI `agy` and the OpenCode CLI (1.10). Rust only if an ADR chooses Tauri.
- Add the Android Auto Desktop Head Unit (SDK extras) and an Android TV system image only when a product with a car or TV target reaches its wave (disk).
- Ahmed's Android phone: turn on developer options and USB/wireless debugging so `adb install` can put builds on it directly.
- Smoke test: create a throwaway Expo app, run it on the Android emulator, then delete it.
- **iOS and macOS reality:** Apple builds require macOS and Xcode, and this laptop runs Windows. iOS, iPadOS, watchOS and macOS builds go through cloud macOS: EAS Build for mobile, GitHub Actions macOS runners for the Electron mac build, with Codemagic's free macOS minutes as a second source (module 22). On-device testing uses a development build on Ahmed's iPhone 14; device builds and TestFlight need the Apple Developer account. Prepare everything else and list Apple-dependent steps in `OWNER_ACTIONS.md`.

**1.9 Global instruction files.**

- `%USERPROFILE%\.claude\CLAUDE.md`: owner profile (short), the autonomy tiers, a pointer to the SIR Standard in `D:\Projects\_SIR\standard\`, and an Orchestra Protocol summary.
- `%USERPROFILE%\.gemini\GEMINI.md` (and/or `~/.gemini/AGENTS.md`): the same core for Antigravity, under 20 KB.
- HQ files in `D:\Projects\`: `AGENTS.md` (portfolio map, how to pick up work, locks), `CLAUDE.md` (first line `@AGENTS.md`), and `GEMINI.md`.
- **Laptop Manager becomes Ahmed's "Personal OS".** It's the home for everything not tied to one product: PC care and cleanup, personal automations, the autopilot routines, cross-tool agent configs (1.13), local AI (1.14), and the personal knowledge base. Extract every non-project instruction from this mission folder into `D:\Projects\Laptop Manager\AGENTS.md` (a short charter) plus `docs/PERSONAL_OPS.md` (the details). A session opened in Laptop Manager then knows the whole personal domain. `_SIR` keeps the portfolio-level concerns: standard, platform, ops, dashboard, knowledge, the AI router.

**1.10 External workforce.**

- `agy`: confirm it's installed and signed in with Ahmed's primary account; run `agy models`; test `agy -p "hi" --output-format json`; set `useG1Credits: false` and confirm "AI Credit Overages" is "Never".
- `opencode`: confirm it's installed; run `opencode models`; test `opencode run --format json "hi"` with Muse Spark 1.3; read the model's data terms and record what it may be used for.
- `kilo`: install it if it's missing (`npm install -g @kilocode/cli`), connect a provider, test `kilo run --auto --format json "hi"`, and record its limits and data terms.
- Ollama: pick 1–2 small models (one general instruct model with solid Arabic, plus an embedding model only if a workflow needs it); test them.
- Build `_SIR/scripts/ai/ask.ps1` and the usage ledger (A2). Test the fallback chain by forcing a failure.
- Record everything in `TOOLS.md`.

**1.11 n8n: the automation engine.**

- Install the current n8n with its officially supported method (npm is lighter than Docker on a tight disk; check the required Node version). Bind it to localhost only. Create the owner account with a generated strong password stored in Windows Credential Manager (tell Ahmed where it is), and back up the encryption key and data folder.
- Enable the Execute Command node deliberately (n8n 2.x disables it by default; verify the current way, community-reported as `NODES_EXCLUDE="[]"`), because AI automations call `claude -p`, `agy -p`, `opencode run` and Ollama. Document the risk: local only; no public webhooks without auth.
- If the current n8n supports MCP, connect it with Claude Code so Claude can run workflows as tools.
- Start n8n at logon with low priority. If you measure real RAM pressure, switch it to on-demand starts.
- Note: a Claude Pro subscription doesn't include API keys, and n8n's Anthropic node needs a separately paid API key. Use `claude -p` instead (it uses subscription usage, so reserve it for high-value steps), or local models and Gemini.

**1.12 Personal-AI autopilot (works without prompts).**

- **Desktop scheduled tasks** (local; they run only while the Claude app is open and the laptop is awake: turn on "Keep computer awake"; auto permission mode per task; click "Run now" once after creating each one and approve what it needs). Use odd minutes, because the scheduler adds jitter.
  - **Morning brief (~08:47):** today's calendar; Gmail triage with draft replies (not sent); TickTick items due; Obour deadlines; job and freelance leads; project blockers; usage left. One push notification.
  - **Midday (~13:17):** content drafts for the approved calendar; proposals for new leads.
  - **Nightly (~23:13):** incremental verify of active projects (Haiku); security and dependency scan; Command Center refresh; TickTick sync; MISSION_LOG; usage-ledger summary; disk report.
  - **Weekly (Friday ~18:07):** business report; next week's content calendar for approval; standard-improvement proposals; Ideas Inbox triage.
  - A run missed while the laptop slept gets one catch-up run later, so each prompt checks the current time and skips stale work.
- **Cloud scheduled tasks** for work that needs no local files (GitHub PR reviews, CI watching). They run even when the laptop is off.
- **`/goal`** for long autonomous pushes inside a session, with a measurable condition and a turn cap, run in auto mode. Example: `/goal every Wave-1 web app passes pnpm verify and has a preview deployment, or stop after 40 turns`.
- **`~/.claude/loop.md`:** the default maintenance loop for `/loop` (continue unfinished BOARD work, tend PRs, run cleanup passes).
- Every routine has a usage budget and uses the cheapest capable model. Skip low-value runs when the week's usage is tight.

**1.13 Cross-tool parity: the same power in Antigravity, Codex and the other CLIs.** After the month, Ahmed should feel no difference working in Antigravity with Gemini, in Codex (ChatGPT's coding agent), in OpenCode, or in Kilo.

- **One canonical source:** `D:\Projects\Laptop Manager\agent-config\` holds the core rules, every skill (`SKILL.md` folders), the agent roster (role, model tier, tools, prompt), the MCP server list, hook intents and schedule definitions. A `sync-agent-config` script writes each tool's native format. Never hand-edit the generated copies.
- **Claude Code:** `~/.claude/CLAUDE.md`, `~/.claude/agents/`, `~/.claude/skills/`, hooks in settings, MCP through `claude mcp add`, plugins.
- **Antigravity:** package everything as one **SIR plugin** (`plugin.json` plus `skills/`, `agents/`, `rules/`, `mcp_config.json`, `hooks.json`) and install it globally (`~/.gemini/config/plugins/`, or `agy plugin install <path>`), so it works in the Antigravity app, IDE and CLI.
  - Map the roster: planner and reviewer roles → `model: pro`; builder roles → `model: flash`. Set `tools` and `commandExecutionPolicy` per agent; a misspelled tool name can hang a subagent.
  - Hooks: Antigravity supports `SessionStart`, `PreToolUse`, `PostToolUse`, `PreInvocation`, `PostInvocation` and `Stop` (camelCase JSON in and out). Point its `SessionStart` hook at the same memory reload script (adapt the input and output to its JSON format, then test it), so Antigravity sessions also start from the checkpoint.
  - Re-create the autopilot routines with Antigravity's `/schedule`, long runs with `/goal`, big jobs with `/teamwork-preview`, and use Antigravity's own Remote Control.
  - Check the Marketplace (`antigravity-plugins-official`) for official plugins matching the MCP servers and skills used here.
- **Codex:** global `~/.codex/AGENTS.md` (repos already have `AGENTS.md`); skills in `~/.agents/skills` (global) and `.agents/skills` (repo; the same folder Antigravity reads); MCP servers, subagents, hooks and plugins per the current Codex configuration reference.
- **OpenCode, Cursor, GitHub Copilot** read `AGENTS.md`; add MCP servers and agents per each tool's docs.
- **Kilo CLI** (`kilo`) works with `AGENTS.md` (its `/init` creates one, and its `instructions` setting can add more files). MCP servers go in `~/.config/kilo/kilo.jsonc` (global) or `kilo.json` / `.kilo/` (project); custom agents through `kilo agent`; skills per its docs. Headless runs: `kilo run --auto`.
- **Automations stay tool-agnostic:** n8n calls CLIs through `ask.ps1`. After the month, change its default provider from `claude` to `agy` or local in one config line.
- **Parity test:** run the same smoke task in every tool ("read AGENTS.md, list the project's next 3 steps, run `pnpm verify`") and confirm each one loads the rules, skills and MCP servers. Record the results in `TOOLS.md`.
- Re-run `sync-agent-config` whenever a skill, agent or MCP server changes, and once more before the month ends.

**1.14 Make the local AIs better** (they matter even more after the month). Work in this order, measuring each step on Ahmed's real tasks, Arabic included:

1. Pick the best small model for each job (chat, Arabic text, code, embeddings) by testing, not by reputation.
2. Write Ollama Modelfiles per role: system prompt, Ahmed's context, sensible parameters.
3. **Retrieval (RAG):** a local knowledge base (embeddings plus a vector index) over project docs and CHECKPOINTs, Obour materials, the CV and notes, refreshed nightly. This is the biggest gain for "it knows my stuff".
4. **Fine-tuning** only for narrow, repeated tasks, with a curated dataset and a before/after evaluation. On 6 GB of VRAM that means QLoRA on small models (roughly 1–4B parameters; 7–8B models generally need 8–12 GB). Run it overnight, export to GGUF for Ollama, and keep only adapters that beat the baseline (disk).

AHome's private data never leaves the laptop.

**Phase 1 deliverables:** Remote Control working from the iPhone, `TOOLS.md` complete, toolchain green, roster and hooks tested, external workforce and n8n working, autopilot routines created and each run once, the SIR plugin installed in Antigravity, and the parity test passed in every tool.
