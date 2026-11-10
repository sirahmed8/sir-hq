# Control guide: every AI tool under SIR management (HQ, 2026-11-10)
For the owner, the HQ manager, and any manager appointed after Claude. Read this to see, steer or repair the whole AI workforce in 5 minutes.

## 1. Who does what
| Layer | What | Where it lives |
|---|---|---|
| Owner | Sign-ins, payments, decisions | `ops/OWNER_ACTIONS.md` |
| HQ manager (Claude now; any model/person later) | Reviews, writes briefs, verifies on screen and with `gh run list` | `_SIR/START_HERE.md`, `ops/HQ_CHECKPOINT.md` |
| Autopilot | Every 5 min: starts a worker for the first 2 open queue tasks (different projects) when nobody touched the project for 25 min | `scripts/hq_autopilot.py`, task `SIR_HQ_Autopilot`, queue `ops/AUTOPILOT_QUEUE.json`, state `ops/autopilot_state.json`, log `ops/autopilot.log` |
| Runner | Runs ONE task through the free models in turns (rounds up to 55 min) | `scripts/cli-run2.sh <task> <folder>`, log `ops/agy-runs/cli-<task>.log` |
| Model pool | Shared cooldown list: which free model is next, which is out of quota | `scripts/cli_pool.py`, state `ops/agy-runs/model-pool.json` |
| Workers | Kilo, OpenCode, Devin CLI (free models); Antigravity (Gemini) when it has quota; ZCode via the screen operator | configs below |
| Worker manual | Rules every worker gets in every round | `ops/WORKER_PREAMBLE.md` |
| Briefs | One task = `ops/briefs/<name>.md` (+ generated `.prompt.txt`) | add with `python scripts/queue-add.py <name> <brief.md> <folder> "<title>"` |

## 2. See everything in one screen
`python scripts/ai-status.py` (heartbeat, queue, pool cooldowns, running agent processes, last rounds per task).
Then: `gh run list --limit 3` inside each project. CI red = the task is not done, whatever the report says.

## 3. Worker configs (global)
- Kilo: `%USERPROFILE%\.config\kilo\kilo.jsonc` + `AGENTS.md`. OpenCode: `%USERPROFILE%\.config\opencode\opencode.jsonc` + `AGENTS.md`. Both load: workspace `AGENTS.md`, `standard/23-premium-code-bar.md`, `plans/USAGE_POLICY.md`, `ops/WORKER_PREAMBLE.md`, `plans/CLI_AGENT_INSTRUCTIONS.md`.
- Devin CLI: `%LOCALAPPDATA%\devin\cli\bin\devin.exe`, reads `AGENTS.md` of the folder; runner passes the manual in the prompt. Permission mode `dangerous` (auto-approve) is set only in `cli-run2.sh`, the same trust level as `kilo run --auto`; reason: in `smart` mode it rejected every shell/edit call in non-interactive runs and did nothing (found 2026-11-10).
- Free models and their order: the `POOL` list in `scripts/cli_pool.py`. List what exists: `opencode models | findstr free`, `kilo models | findstr free`. Add or remove one line there; no other file needs to change.
- Antigravity accounts and order: `ops/ACCOUNT_ROTATION.md` (CURRENT ORDER block).

## 4. What went wrong on 2026-11-10 and what changed
1. Kilo auto-free hit its limit after about 40 minutes of work, OpenCode big-pickle at once, and both tasks hit the same models together. Fix: one shared pool with cooldowns (60 min after a limit, 15 min after a fast failure, 6 h after refused tool calls); the runner picks the first available model and exits with "usage limit" lines when the pool is empty so the autopilot waits 60 min.
2. Devin ran in `smart` mode and refused every tool call (all those rounds were empty). Fix: permission mode and a 6 h cooldown rule when 3 refusals are seen.
3. Workers wrote PowerShell commands with `&&` and unquoted paths with spaces, left a refactor half done (broken import) and reported "all gates green" while CI was red. Fix: `ops/WORKER_PREAMBLE.md` (shell rules, never leave main broken, CI must be seen green, how to finish).
4. A runner restarted while another was alive writes the same log; two writers per project must never exist. Check `python scripts/ai-status.py` before starting a runner by hand.

## 5. Everyday commands
- Add work: `python scripts/queue-add.py r21-x ops/briefs/r21-x.md "D:/Projects/<Project>" "title"`.
- Worker stuck: look at the last 60 lines of `ops/agy-runs/cli-<task>.log`; if the pool is cooling, nothing to do; if a worker loops, kill it (`taskkill /PID <pid> /T /F`) and the runner moves on to the next model.
- Stop one task: write `ops/agy-runs/done/<task>.done` (use `scripts/agy-done.py <task> ok|fail|blocked "summary"`).
- Restart the autopilot after editing it: stop the python process of `hq_autopilot.py` (match on `hq_autopilot.py` AND the name `python`, not on text only), then `Start-ScheduledTask SIR_HQ_Autopilot`. It reads its state file once at start.
- Game running: autopilot pauses by itself (game-mode snapshot of the Laptop Manager).

## 6. Hand-over to a new manager
Read in this order: `_SIR/START_HERE.md`, this file, `ops/HQ_CHECKPOINT.md` (last note), `ops/OWNER_ACTIONS.md`, `ops/bus/sir-hq.md`. Then run section 2. Review rule: a task is done only when its report has pasted command output, CI on `main` is green (`gh run list`), and you saw the result yourself or through a second agent. Keep appending notes to `ops/HQ_CHECKPOINT.md`; never delete earlier ones.

## 7. Tool status (tested by HQ 2026-11-10 night) and the screen-operated workers
| Tool | State | Note |
|---|---|---|
| Kilo, OpenCode, Devin CLI | in the pool | free models, see `scripts/cli_pool.py` |
| ZCode (Z.ai, GLM-5.3 and flash) | usable by screen operator | no command line; a Haiku operator (lowest effort, computer use) opens the folder, picks the model and sends "read WORKER_PREAMBLE.md and the brief". Own it per project: never the same project as a CLI runner. Accounts: owner's own only, switched through the account chooser, never passwords. Plan ends about 2026-11-14 |
| Antigravity (Gemini) | quota out until 2026-11-11 00:04 (free accounts), 19 accounts in two Chrome profiles | rotation in `ops/ACCOUNT_ROTATION.md`; operator `scripts/agy-chooser.py` |
| Gemini CLI | dead: "no longer supported, migrate to Antigravity" | do not use |
| Qwen CLI | broken install (`cli.js` missing) | reinstall with npm and a browser login by the owner if wanted |
| Codex CLI | not callable from this shell (wrapper points at a missing file) | repair before use; reset date unknown |
Rule: one writer per project at any time (CLI runner OR ZCode OR Antigravity). The autopilot treats any commit or edit in the last 25 minutes as "someone is working" and starts nothing.

## 8. Owner rules added 2026-11-10 night
- ZCode (and any app-based agent): the workspace is the whole `D:\Projects` folder, never one project, so every agent sees every project and reads the file it is told to read. The owner already set this up in ZCode. The brief names the project folder to work in.
- Permissions: agents get full access (ZCode "Full access", Devin `--permission-mode dangerous`, Kilo `--auto`) so they never stop to ask for approval. The owner decided this; the limits that remain are the laws in `D:/Projects/AGENTS.md` (private data, no secrets in git, no payments, no sign-in tricks).
- One writer per project at a time still applies (two agents editing one folder overwrite each other).
