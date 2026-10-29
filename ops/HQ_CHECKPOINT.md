# HQ CHECKPOINT — updated 2026-10-29 15:50
## Phase and step
Phase 1 (`phases/01-workstation.md`) in progress. Done: 1.1, 1.2, most of 1.3, 1.5 (env only), 1.6, part of 1.8, 1.10. Open: 1.7, rest of 1.8, 1.9, 1.11, 1.12, 1.13, 1.14.
## Now
Phase 1 part 1 is committed to sir-hq. Facts: Claude Code 2.1.312 latest; Remote Control 404 fixed (two relaunches clean); settings: remoteControlAtStartup true, teams env, 3 deny rules, SubagentStop hook; 18-agent roster; `sir-session-end` skill; pnpm/eas/wrangler installed; Ollama serves 6 models from `D:\Projects\AI_Models_Hub\ollama`; `ask.ps1` tested for local, agy, opencode (free model), kilo, fallback and secret guard. Disk: C: 16 GB free, D: 16 GB free.
## Next step
1. **1.7 MCP/plugin clean slate**: inventory with `claude mcp list` (read-only first), record in TOOLS.md what is connected, needs auth, failed, duplicate; do not enable more servers than needed (every server costs context). Candidate cleanup: Output.ai plugin (about 10k tokens per session, Ahmed's call).
2. **1.8 rest**: JDK 17 for Gradle (JDK 21 present), Android SDK + `ANDROID_HOME` (only platform-tools exist), ImageMagick, ffmpeg, 7-Zip, Playwright browsers, Maestro. Free more disk first (node_modules of inactive projects up to 12.6 GB after a check, AppData Local Temp 2 GB). Keep emulator images to 3.
3. **1.9** `D:\Projects\AGENTS.md`, `CLAUDE.md` first line `@AGENTS.md` (the workspace CLAUDE.md exists already and must keep its content), `GEMINI.md`; Laptop Manager charter.
4. Then 1.11 n8n (installed 2.44.6, not started), 1.12 routines, 1.13 parity, 1.14 local AI.
## Running in the background
- none (the hidden `ollama serve` process was started by HQ at 15:3x)
## Decisions since the last milestone
- Security/system settings left to Ahmed (power plan, `additionalDirectories`, `autoMode.allow`, logon task); listed in OWNER_ACTIONS. Reason: they loosen security or change the OS, so the agent does not do them on its own.
- No blanket force-push deny: planned history cleanups (leaks #2-#4) need it; the three narrow denies stay.
- The other eight rule-9 skills are created when their procedure exists (Phases 4-5), not as empty shells.
- Never print any substring of a credential line; use `sed`/replace with Edit tool for paths (backslashes get eaten in shell replacements).
## Open promises
- Confirm hooks fire after a real compaction (`ops/memory.log`).
- Leaks #2-#4 (OWNER_ACTIONS), ModPack release zip check (Phase 5), Phase 5 security notes (see SECRETS.md).
- 2-teammate agent-team smoke test; `/usage` reading; read OpenCode free-model and Kilo data terms; confirm from the iPhone that the HQ session shows up.
## Owner actions listed (never blocking)
- 10 open (see ops/OWNER_ACTIONS.md): BotFather revoke, Gemini key rotate, Google Drive sign-in, power plan, logon task, AI credit overages "Never", autoMode decision, Output.ai plugin, optional Vercel login, optional GitHub Support purge
## Usage
Not read (`/usage` is a UI command). Pace: heavy session so far; prefer Haiku scouts for the MCP inventory and the installs.
## Re-read after a reset
- START_HERE.md · phases/01-workstation.md · ops/TOOLS.md · ops/OWNER_ACTIONS.md
