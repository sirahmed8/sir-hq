# HQ CHECKPOINT — updated 2026-10-29 16:20 (local)
## Phase and step
Phase 1 (`phases/01-workstation.md`), about 60% done. Open: 1.8 rest, 1.9, 1.11, 1.12, 1.13, 1.14; then Phase 2.
## Now
**Usage is the constraint:** Pro plan, 5-hour limit 85% (resets about 18:20 local), weekly 72% (resets 2026-11-01). The first HQ session grew to 657K tokens (every turn re-sends it). All further work runs in FRESH sessions (start cost now 28K tokens, was 158K). Rule: pace on `get_usage`; above 90% finish the unit, checkpoint, wait for the reset (headless/background sessions continue automatically).
Done and verified this stretch: startup tokens 158,122 → 28,063 (headless "ok" test) after: 56 local plugins disabled (12 kept: firebase, cloudflare, canva, figma, firecrawl, chrome-devtools-mcp, commit-commands, frontend-design, modern-web-guidance, claude-security, skill-creator, typescript-lsp), 101 skills moved to `~/.claude/skills-disabled/` (73 kept), duplicate user `firebase` MCP removed, 22 claude.ai connectors disconnected (kept 20: OpusClip, AnythingMCP, Black SEO, Cloudflare, ElevenLabs, GitHub, Gmail, Calendar, Docs, Drive, Sheets, Harakah, HyperFrames, Indeed, Microsoft Learn, PostHog, Tarteel, TickTick, UmmahAPI, vidIQ), 77 of 78 account plugins removed (kept frontend-design). Android-MCP fixed (lazy device connect patched in the extension; handshake and tool list tested; Claude Desktop reloads it at next restart; originals in `D:\Backups\SIR-2026-10-29\android-mcp-original`). Off-laptop backup: private repo `sirahmed8/sir-backups`. HQ Remote Control launcher in the Startup folder. SessionStart hook verified in 2 real sessions.
## Next step (fresh session, in this order, cheap model for bulk)
1. **Verify the rest of "unverified"**: (a) run one `scout` agent and confirm `ops/subagent.log` gets a line (roster + SubagentStop); (b) read OpenCode free-model and Kilo data terms (WebFetch the vendors' pages) and write the finding into TOOLS.md; (c) start `pwsh -File D:/Projects/_SIR/scripts/rc-hq.ps1` hidden and confirm "SIR HQ" shows under claude.ai/code via Claude in Chrome (tabs_context_mcp, then close the tab); (d) compaction hook: self-announcing, check `ops/memory.log` whenever a compaction happens.
2. **1.8**: JDK 17 (winget `EclipseAdoptium.Temurin.17.JDK`), Android SDK to `D:\Android\Sdk` (cmdline-tools, platform-tools exists, build-tools, platform 36; no emulator images yet, they are 1.5 GB each: add one only when a build needs it), set `ANDROID_HOME`; ffmpeg, ImageMagick, 7-Zip, Playwright browsers. Disk first: C: and D: about 16 GB free; node_modules (12.6 GB) of inactive projects can go after Phase 2 decisions.
3. **1.9** `D:\Projects\AGENTS.md`, `GEMINI.md`; `D:\Projects\CLAUDE.md` already exists (18 lines): add `@AGENTS.md` as FIRST line without losing content; `~/.gemini/GEMINI.md`; Laptop Manager charter (`AGENTS.md` + `docs/PERSONAL_OPS.md`).
4. **1.11** n8n 2.44.6 is already running since 00:54 (not started by HQ): check it binds to localhost only, Execute Command node status, credentials in Credential Manager. **1.12** autopilot routines via the scheduled-tasks MCP (morning 08:47, nightly 23:13, weekly Fri 18:07), each run once. **1.13** parity (Antigravity plugin, Codex, OpenCode, Kilo configs from one canonical folder in Laptop Manager). **1.14** local AI (RAG first).
5. Then `phases/02-ahome-and-pc.md`.
## Running in the background
- hidden `ollama serve` (HQ started it 15:36). Nothing else of HQ's.
## Decisions since the last milestone
- Disabled/removed, not deleted: plugins are flags (re-enable in `~/.claude/settings.json` or "add back" in claude.ai), skills are in `~/.claude/skills-disabled/`, connectors reconnect from claude.ai/customize. Re-add when needed: Postiz and Social Media Skills (Phase 8.2), Study Desk (8.6), Cloudinary (Phase 4 if used), Canva/Figma connectors if the plugin MCPs are not enough.
- Owner list cut to 2 real items + 3 optional (ops/OWNER_ACTIONS.md). System/security settings stay off-limits to the agent even when asked.
- Never print any substring of a credential line; use the Edit tool for paths with backslashes (shell replacement eats them).
## Open promises
- Leaks #2, #3, #4 (see OWNER_ACTIONS and inventory/SECRETS.md); ModPack release asset zip check (Phase 5); Phase 5 security notes (Firebase key restrictions, ZATCA pseudo-key, hard-coded licence keys).
- 2-teammate agent-team smoke test (experimental env on; do after the scout check).
- Compaction hook confirmation (self-announcing).
## Owner actions listed (never blocking)
- 2 real, 3 optional
## Usage
Pro: 5-hour 85%, weekly 72% at about 16:20 local. First HQ session context 657K/1M.
## Re-read after a reset
- START_HERE.md · phases/01-workstation.md · ops/OWNER_ACTIONS.md
