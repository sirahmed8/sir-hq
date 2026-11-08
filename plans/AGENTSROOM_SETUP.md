# AGENTSROOM SETUP: Claude manages and reviews, Antigravity builds (Ahmed, 2026-11-07)

Why: Ahmed has 1 Claude Pro (weekly limit gone after one day of heavy work) and 4 Antigravity Pro accounts plus about 15 free ones. So Claude Code is the manager and reviewer and writes short, exact briefs; Antigravity CLI (`agy`, Gemini 3.8 flash, high effort) writes the code. AgentsRoom (`C:\Program Files\AgentsRoom`, data in `C:\Users\a7med\.agentsroom`) runs every CLI in one window and already has what this needs.

## What AgentsRoom gives us (read from its own docs in `C:\Program Files\AgentsRoom\resources\kb`)
- **Many CLIs, one room:** Claude Code, Codex, Antigravity, OpenCode, Kilo (via OpenCode family), Muse Code (Meta), Pi, oh-my-pi, Ollama and more; each agent picks its CLI and model (`multi-provider.md`).
- **Agent messaging and spawning:** saved agents write to each other whatever CLI they run on; `agents_spawn`, `agents_send`, `agents_read_inbox`, `agents_spawned_wait` on the AgentsRoom-MCP server (`agent-messaging.md`, `agentsroom-mcp.md`). This is how the Claude manager hands a ticket to an Antigravity worker and waits for the result.
- **Teams and QA delegation:** pipelines with steps, gates and reviewers (`teams.md`), and `run_qa_test` for browser checks on a cheaper model (`agent-delegation.md`).
- **Multi-account and auto-switch:** several Antigravity accounts in a pool; when one hits its limit the same conversation moves to the next (`multi-account.md`, `account-auto-switch.md`).
- **Quota rules:** per-gauge rules that block, redirect, change model, or rotate launches between providers (`quota-rules.md`); usage alerts at 90% are already on.
- **Roles and templates:** `.agentsroom\roles\*.md`, `agent-templates.json`, hooks, prompt and skill libraries, backlog board, mobile companion (the phone app replaces Remote Control inside AgentsRoom).

## What HQ found and fixed (2026-11-07)
1. **Connectors "AgentsRoom-Chrome / MCP / QA-Tester / Test-Runner: Reconnect" and HTTP 403:** a stale project file `D:\Projects\.mcp.json` (written 2026-11-03) held an old auth header for the AgentsRoom MCP host. Every Claude session under `D:\Projects` loaded it, including HQ. AgentsRoom now passes live, per-agent config itself (`.agentsroom\mcp\user-servers`). The stale file was removed (copy in `D:\Projects\Backups\agentsroom-2026-11-07\mcp.json.stale`).
2. **"Remote Control disconnected ... code 4090":** `remoteControlAtStartup` was true in `~/.claude/settings.json`, so every console registered a Remote Control session; when one is deleted from another device or app the console shows 4090. It is now false (copy of the old file in the same Backups folder). To use Remote Control on one console, type `/remote-control` there.
3. **Shared rules for every CLI:** `opencode.jsonc` and `kilo.jsonc` now load `D:\Projects\AGENTS.md`, the premium code bar and the usage policy; Codex, Gemini and Antigravity global files point to the same (agent-reset, 2026-11-02). AgentsRoom has `inheritUserCliConfig: false`, so inside it each CLI relies on the project's own `AGENTS.md` (opencode/kilo/codex/agy read it from the folder); the in-app chat must verify that each CLI quotes it (see the prompt).
4. **Not done by HQ (the app is running and rewrites its own `settings.json`):** accounts, roles, quota rules, tiers. The in-app chat applies them through AgentsRoom's own tools (`settings_set`, `quota_rules_save`, `agents_save`).
5. Not patched: the app itself (`app.asar`). An update would erase a patch, and settings, roles, hooks and templates already cover what we need.

## Current AgentsRoom state (read-only look)
Default provider and assistant: Antigravity, `gemini-3.8-flash-high`, effort max. Tiers fast/powerful already on Antigravity. Permission mode autonomous (Claude and Antigravity). Context meter cap 150k tokens (matches the usage policy). One project registered: `Projects` (`D:\Projects`), 29 role agents inactive, none of the 4 Antigravity accounts added as profiles yet (`antigravityProfiles: []`), no quota rules (`quotaRules: []`), `disabledProviders: []`. CLIs installed: claude 2.1.319, agy 1.5.3, opencode 2.2.6, kilo 7.8.27, pi, omp, crush, qwen, droid, ollama. Not installed: codex, muse, gemini, aider.

## Target setup (the in-app HQ chat builds this, no project work yet)
| Role | CLI and model | Effort | Job |
|---|---|---|---|
| Manager and reviewer (HQ) | Claude, sonnet-5.5 | medium (high for reviews and security only) | plans, writes briefs, reviews every diff, never bulk-codes |
| Workers (3 at once) | Antigravity, gemini-3.8-flash-high | max | write code and tests from a written brief, return 15 lines |
| Second reviewer | Antigravity on a different account or OpenCode | high | the author never grades its own work |
| Backup chain | OpenCode (Zen free models), Kilo (Auto Free), Muse Code, Pi, omp | high | when every Antigravity account is at its limit |
| Private work (AHome, Habiba, study material, credentials) | Ollama local models only | high | never any cloud provider |

Quota rules to create (names in the app): (1) Antigravity, any gauge reaches 95%: move running agents to the account with most quota left; (2) all Antigravity accounts near the limit: alternate-provider rotation to OpenCode then Kilo for new launches (not for AHome); (3) Claude week reaches 90%: block scheduled and webhook launches and keep only manual manager sessions.

## Free providers and gateways (verified by search 2026-11-07; limits change weekly, re-check before relying)
- OpenCode Zen free models (rotating; only inside the OpenCode CLI; some log prompts for training) and a no-key free tier: see the [OpenCode free tier tracker](https://mvalentsev.github.io/awesome-free-ai-coding/providers/opencode/) and [opencode-free-providers](https://github.com/mnk-works/opencode-free-providers) (46 models from 9 providers need no setup).
- Kilo Gateway Auto Free (`kilo-auto/free`), no card needed.
- OpenRouter `:free` models: 20 requests a minute, 50 a day (1,000 after a one-time $10 top-up, which we do not do: no budget).
- Google AI Studio Flash, NVIDIA trial endpoints, Groq developer tier, Gemini CLI free quota.
- Qwen's free OAuth tier ended on 2026-04-15, so the `qwen` CLI needs another backend.
- Gateways that combine many free providers behind one local endpoint: [OmniRoute](https://github.com/diegosouzapw/OmniRoute) (MIT, claims about 1.6B free tokens a month; unverified, the project's own estimate) and [9router](https://github.com/decolua/9router); a benchmark tool for free models is [free-coding-models](https://github.com/vava-nessa/free-coding-models). Rules before using any: local-only install, review the code first, free keys that Ahmed creates himself (account sign-up stays with him), never route AHome or secrets through them, never feed it a Claude or Antigravity subscription login (account-ban risk).
- Meta Muse Code: AgentsRoom lists it as a provider; no free-tier detail found. The in-app chat checks it through AgentsRoom's "Install a CLI".

## Update 2026-11-07 (later)
Antigravity thinking is max everywhere; Claude (manager, reviewer) is sonnet-5.5 high. Roles sir-manager, sir-reviewer, sir-worker, sir-private-worker, sir-qa are in D:/Projects/_SIR/standard/roles and C:/Users/a7med/.agentsroom/roles. The manager also creates new tasks and drives workers without being told; OWNER_ACTIONS.md is reduced to true blockers.
