# Tools survey (operator15, 2026-11-09)

Read-only survey. No purchases, no sign-ups, no passwords typed, no tasks started.

## 1. OpenCode (CLI) - WORKS
- Version: opencode v2.2.6. Auth: GitHub Copilot (OAuth), Google (API key), OpenRouter (API key), all stored.
- Start non-interactively in a project folder: `opencode run -m opencode/big-pickle "your task"`
- Start interactive TUI: `opencode -m opencode/big-pickle`
- Free models (labelled free or `-free` by OpenCode): opencode/big-pickle (unnamed), opencode/beam-free, opencode/crouton-alpha-free (stealth), opencode/flint-40b-free, opencode/iceman-free, opencode/inkling-2-small-free, opencode/glm-5.3-flash-free, opencode/deepseek-v4.1-flash-free, opencode/mimo-v2.6-flash-free, opencode/nemotron-3.5-lightning-free, opencode/nemotron-3.5-super-vl-free, opencode/longcat-2.5-free.
- Also on OpenRouter free: openrouter/google/gemma-4-31b-it:free, openrouter/openrouter/free, openrouter/recursive/flint-v1.0:free.
- Strength: not benchmarked here. Named models with the strongest families and free access are the GLM-5.3 Flash, DeepSeek v4.1 Flash, MiMo v2.6 Flash, and the unnamed big-pickle. Verify with one small task before relying on any of them.

## 2. Kilo (CLI, v7.8.27) - WORKS
- Auth: Kilo Gateway (OAuth), 1 credential. Profile: Personal team, balance $0.00. So only free-labelled models are usable without paying.
- Start non-interactively: `kilo run -m kilo/kilo-auto/free "your task"` (run from the project folder, or pass the folder as the `project` positional to `kilo`).
- Interactive TUI: `kilo [project-folder]`.
- Free / unnamed models in the list: kilo/kilo-auto/free (router), kilo/openrouter/free, kilo/stealth/glyph-cluster (stealth), kilo/stealth/crouton-alpha (stealth), kilo/meta/muse-spark-1.3 and other muse-* (Meta, check if free), kilo/nvidia/nemotron-3.5-lightning:free, kilo/nvidia/nemotron-3-ultra-550b-a55b:free, kilo/elorian/glimpse, kilo/fireworks/ember-1, kilo/google/gemini-4-argon (shown only if the account allows it).
- The model list has 319 entries. Only the `:free`, `kilo-auto/free` and stealth ones are safe to assume free. Other entries may bill against the $0.00 balance and fail.

## 3. Codex (OpenAI) - NOT READY
- The `codex` command is not installed on the PATH. The npm shim at `C:\Users\a7med\AppData\Roaming\npm\codex.cmd` actually launches GitHub Copilot CLI, so it is not Codex.
- The Codex desktop app is set up: `C:\Users\a7med\.codex\config.toml` uses model gpt-6-luna. `C:\Users\a7med\.codex\auth.json` has auth_mode "chatgpt", so a ChatGPT login exists. The token values were not read.
- Usage left and reset time: NOT checked (the Codex desktop window was not opened).
- Owner one-step: open the Codex app, look at the usage panel, and tell HQ the weekly or monthly reset time.

## 4. Devin (desktop) - NOT INSTALLED
- Owner confirmed: not installed. No Devin desktop app (devin.exe) found. Only leftover files exist: C:\Users\a7med\AppData\Local\Devin\cli and telemetry_state.json. The desktop app was not opened, no task started, nothing accepted, nothing installed.
- Free tier: web search only, not checked in this pass.

## 5. Cursor - NOT INSTALLED
- No Cursor folder found in Programs, Local, Roaming or on the PATH. Nothing to check.

## 6. Windsurf - NOT INSTALLED
- Owner confirmed: not installed. Nothing found in Programs, Local or Roaming. Nothing installed.
- Free tier (web search only): Devin's own pricing post says the Free plan is $0 with a daily and weekly quota and no credits, and that the free model SWE-1.5 stays usable after the quota runs out. A July 2026 guide lists 25 credits per month instead (may be older). Check windsurf.com/pricing for current numbers.
- CLI or API for terminal use: none found in search results. Treat it as an IDE only.

## 7. GLM (Z.ai) (web search only)
- Free API models (per a Z.ai pricing summary dated 2026-10-07): GLM-4.7-Flash, GLM-4.5-Flash, GLM-4.6V-Flash at $0. Older generations, and Z.ai does not promise they stay free.
- GLM Coding Plan (paid subscription): Lite, Pro, Max; limits per 5 hours and per week. Max is listed at $117.6/month (promo) vs $168 list. Not free.
- Terminal use: the GLM models are also reachable through OpenCode and Kilo (opencode/glm-5.3-flash-free above), so no separate install is needed for a free try.

## Ranked recommendation after Antigravity (strongest and cheapest first)
1. OpenCode free models, `opencode run -m opencode/big-pickle "<task>"` (or glm-5.3-flash-free / deepseek-v4.1-flash-free for a second opinion). Free, already signed in, runs in the terminal.
2. Kilo free router, `kilo run -m kilo/kilo-auto/free "<task>"`, and the stealth models kilo/stealth/crouton-alpha or kilo/stealth/glyph-cluster when the router is busy. Free, signed in, $0 balance so paid models will fail.
3. Codex (ChatGPT login) only after the owner has checked its reset time, `codex` is not on PATH yet, so the desktop app is the route until it is installed.

Not ranked: Devin, Cursor (not installed), Windsurf and GLM Coding Plan (no free terminal path confirmed).

## Update 2026-11-10 (HQ installs, owner authorised)
- Gemini CLI 0.67.0 installed (npm @google/gemini-cli): the free Google-account tier for it is DISCONTINUED ('migrate to Antigravity'), and its API-key tier needs a valid key (the stored one is invalid): not usable for now.
- OpenRouter free models work through OpenCode with the stored OpenRouter key: `opencode run -m openrouter/openrouter/free "..."` (router, tested OK), also openrouter/nvidia/nemotron-3-ultra-550b-a55b:free, openrouter/cohere/north-mini-code:free, openrouter/google/gemma-4-31b-it:free. Free tier has daily limits.
- Kilo auto-free works: `kilo run --auto -m kilo/kilo-auto/free "..."` (used by scripts/cli-run.sh).
- Devin CLI 3000.12.32 installed in %LOCALAPPDATA%\devin\cli\bin\devin.exe (setup wizard needs the owner's login: option 1 'Log in with browser', recommended). Free plan has daily/weekly quota; model SWE-1.5 stays usable.
- ZCode (Z.ai, free desktop app with GLM-5.3, an Antigravity-like agent app) 3.17.2 installed silently under %LOCALAPPDATA%\Programs\ZCode; first launch needs Connect Z.ai (owner login) or an API key.
- Disk: C: 17 GB free, D: 7.4 GB free at install time.
