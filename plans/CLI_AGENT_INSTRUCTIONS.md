# Instructions for the free coding agents (Kilo, OpenCode, Devin CLI, ZCode) - 2026-11-10
nSee also plans/AI_TOOLS_CONTROL.md (how the workers, pool and autopilot fit together) and ops/WORKER_PREAMBLE.md (the manual every worker gets each round).

These tools do the building when Antigravity quota is out. Every one of them follows D:/Projects/AGENTS.md, plans/GEMINI_QUALITY_CHARTER.md and the project's .sir files. Rules for all of them:
1. Read first: D:/Projects/AGENTS.md and D:/Projects/GEMINI.md, the project's AGENTS.md, .sir/CHECKPOINT.md, the checklist file, the brief; then `git status` and the last commits (another tool may have edited before you; never revert its edits).
2. Work in small steps. After EVERY finished item: run the checks (tsc, tests, lint), commit with a clear message, push to main, tick the checklist, update .sir/CHECKPOINT.md. A quota cut can happen at any moment and the next tool starts from those files.
3. Web research is ALLOWED (owner, 2026-11-10): search and read the web freely for docs, examples and fixes. In non-interactive runs the built-in 'web search' tool may ask for permission and crash the run: if that happens use curl, a fetch/webfetch tool or the Firecrawl search tool instead. Never put private data (AHome vault, messages, notes, photos, secrets) into a web query.
4. Never open private data folders (AHome vault, messages, notes, photos). Work on source code only.
5. Do not ask the owner anything; decide, log and continue. When blocked by a quota message, write the state to the checkpoint and stop cleanly: the runner switches tool.
6. Premium quality: follow the charter (one design system, springs, computed layouts, swipe tabs, shared pickers), no placeholders, no invented data, no emoji, version 1.0.0. Done means the definition of done in D:/Projects/GEMINI.md section 3 (verify output, screenshots at 320, 390, 768, 1280 and 1920 px, five states, honest report).
7. No pull requests: push straight to main after the checks pass. Free tiers only: never buy credits or enable overages. Private data of AHome and Habiba never goes to any outside model, including these tools (AHome work is done only with local models).

## Which tool and model (chosen after tests on 2026-11-10)
- Kilo: `kilo run --auto -m kilo/kilo-auto/free "<task>"` (router picks a free model, works non-interactively; Muse Spark does not work there).
- OpenCode: `opencode run -m opencode/big-pickle "<task>"` is the most thorough free model (more tests written); `opencode/glm-5.3-flash-free` is the fastest; `opencode/deepseek-v4.1-flash-free` for a second opinion; OpenRouter free: `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free`, `openrouter/openrouter/free`, `openrouter/cohere/north-mini-code:free`. Daily free limit exists ('Free usage limit reached').
- Devin CLI: `devin -p --model swe-2-flash-medium --permission-mode smart --respect-workspace-trust false -- "<task>"`. Only SWE-2 Flash Medium is free (262K context); the other models cost credits (do not use them). Start in the project folder. Interactive: `devin`.
- ZCode (desktop app, GLM-5.3 on the free Start plan): use GLM-5.3 with Effort High for coding tasks, GLM-5.3-Flash for small ones; open the project folder, paste the brief pointer ('Read <brief file> completely and do exactly what it says'). Driven by the Haiku operator (computer use).
- Thinking levels: use High for design and logic tasks, Medium for routine edits, only where the model offers it for free.

## Handover between tools
Use the continue template (`plans/CHAT_PROMPT_TEMPLATES.md`, Template 6) as the first message to a tool that takes over. Order of tools and accounts: `ops/ACCOUNT_ROTATION.md`, CURRENT ORDER.
The runner (scripts/cli-run2.sh) rotates tools; each round reads the checkpoint, so partial work is never lost. The done marker is written by `python D:/Projects/_SIR/scripts/agy-done.py <task> ok "<line>"` at the very end.
