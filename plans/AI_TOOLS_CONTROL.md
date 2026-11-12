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
| Antigravity (Gemini) | quota out until 2026-11-11 00:04 (free accounts), 19 accounts in two Chrome profiles; CLI `agy` works headless | rotation in `ops/ACCOUNT_ROTATION.md`; operator `scripts/agy-chooser.py`; `agy` models in `cli_pool.py` |
| Gemini CLI (`@google/gemini-cli` 0.68.0) | installed, **not usable in this round** | `gemini -p ... --yolo --skip-trust` failed with `IneligibleTierError: This client is no longer supported for Gemini Code Assist for individuals... migrate to the Antigravity suite`; no working free tier path verified; pool entry added but will cool down on auth/setup failure |
| Qwen CLI | WORKS via local Ollama (no sign-in): `OPENAI_BASE_URL=http://localhost:11434/v1 OPENAI_API_KEY=ollama OPENAI_MODEL=<ollama-tag> qwen -p "<prompt>" --auth-type openai`; smoke OK on qwen3:4b (`QWEN_OK`) | in `cli_pool.py` as `qwen|qwen3:8b` / `qwen|qwen3:4b`; tiny real task recorded in `_quarantine-safe` scratch: wrote/read `ops/agy-runs/scratch/r36/qwen-smoke.txt` |
| Codex CLI | installed (0.167.1), **quota-limited** | `codex exec --skip-git-repo-check --ephemeral ...` runs mechanically but returned `You’ve hit your usage limit ... try again at Nov 27th, 2026 9:08 AM` (matches `ops/ACCOUNT_LEDGER.md`); added to pool/runner/manager with cooldown on limit |
| Cline CLI | installed (3.0.74), **needs owner re-auth** | `cline -p --yolo ...` returned Unauthorized / re-authenticate; smoke failed; added to pool/runner/manager but will cool down until re-authed |
| Goose | WORKS with local Ollama: `GOOSE_PROVIDER=ollama GOOSE_MODEL=<tag> goose run -t "<prompt>"`; smoke OK on qwen3:4b | in `cli_pool.py` as `goose|qwen3:8b` / `goose|qwen3:4b`; tiny real task recorded in scratch: created/read `ops/agy-runs/scratch/r36/goose-real.txt` |
| Crush | WORKS as runner via Ollama model flag | `crush run -m ollama/qwen3:4b ...` supported; provider config may be needed for some modes, but runner branch added (`crush run -m "$model" "$msg"`); smoke recorded in report (non-interactive run attempted) |
| Aider | **not installed** | `pip install aider-chat` failed building aiohttp on Store Python 3.13; `uv tool install aider-chat` not completed/available in this round; runner/pool entries added for `aider|ollama/qwen3:8b` (will fast-fail/cooldown until installed) |
| Kimi Code CLI | installed (`kimi` 2.5.3), **not usable without auth** | `kimi -p ...` returned `No model configured. Run kimi and use /login...`; runner/pool entry added, will cool down on setup/auth failure |
| Windsurf / Cascade CLI | not installed on this machine | no free headless mode; skip |

Round r36 (2026-11-12, infra): widened pool and manager coverage. Smoke scratch: `ops/agy-runs/scratch/r36/` (qwen/goose pass files created+read; codex/gemini/cline/kimi/aider/crush outcomes recorded in report). Gemini CLI free tier for individuals not verified (ineligible/migrate); Aider install blocked by environment this round. Rule: one writer per project at a time (CLI runner OR ZCode OR Antigravity). The autopilot treats any commit or edit in the last 25 minutes as "someone is working" and starts nothing.

## 8. Owner rules added 2026-11-10 night
- ZCode (and any app-based agent): the workspace is the whole `D:\Projects` folder, never one project, so every agent sees every project and reads the file it is told to read. The owner already set this up in ZCode. The brief names the project folder to work in.
- Permissions: agents get full access (ZCode "Full access", Devin `--permission-mode dangerous`, Kilo `--auto`) so they never stop to ask for approval. The owner decided this; the limits that remain are the laws in `D:/Projects/AGENTS.md` (private data, no secrets in git, no payments, no sign-in tricks).
- One writer per project at a time still applies (two agents editing one folder overwrite each other).

## 9. Watchdog (added 2026-11-11 night)
`scripts/hq_watchdog.py`, scheduled task `SIR_HQ_Watchdog` every 10 minutes, state `ops/watchdog_state.json`, log `ops/watchdog.log`. It restarts the autopilot when its heartbeat is older than 12 minutes, queues a "fix CI" task for any project whose last main run is red and that has no open task, queues audit-loop tasks when the queue is empty, clears regenerable caches when C: is under 3 GB, and tells the owner on Telegram when every free model is cooling for hours. It reads only git and gh output for AHome. ZCode (screen-driven) is outside the watchdog: the HQ manager checks it hourly and sends a Haiku operator when its quota message appears (switch model first, then account from the approved list, Full access, send "continue"). The owner's observation: ZCode Start plan quota does not seem to come back daily on his main account; treat each account as one-time and rotate.

## 10. When Claude is gone (succession, about 2026-11-23)
Nothing depends on Claude except two things: screen operation of ZCode and the hourly Claude cron (session only). Everything else is OS tasks: `SIR_HQ_Autopilot` (starts workers), `SIR_HQ_Watchdog` (repairs, queues CI fixes and audits, cleans disk), `SIR_HQ_ManagerTick` (hourly; when no manager note was written for 50 minutes it runs `ops/MANAGER_PROMPT.md` through a free model from the pool, so a free AI is the manager automatically). A new human or AI manager: read section 6 of this file, run `python scripts/ai-status.py`, and keep appending notes to `ops/HQ_CHECKPOINT.md`; as long as notes are fresh the free manager stays idle. To change what the free manager does edit `ops/MANAGER_PROMPT.md`. To pause everything: `Stop-ScheduledTask` on the three tasks and delete nothing.

## 10. Round r43 (2026-11-12, Haiku pool keeper): free-model additions and proofs
Tiny real task in each scratch folder: create `proof.txt` containing exactly `TINY_OK`, read it back. Scratch: `ops/agy-runs/scratch/r43/`.
| Entry | Result | Note |
|---|---|---|
| `opencode|opencode/nemotron-3.5-lightning-free` | PASS | file written and read back; in POOL |
| `opencode|opencode/beam-free` | PASS | file written and read back; in POOL; keeps data 30 days, never for private work |
| `opencode|opencode/nemotron-3-ultra-free` | FAIL | "Model unavailable" (not in `opencode models`); removed from POOL. The OpenRouter NVIDIA ultra model stays in POOL via kilo/opencode |
| `qwen|qwen2.5-coder:1.5b` (local) | FAIL | replied DONE but wrote no file (tool use too weak); removed from POOL |
Runner and pool changes: `scripts/cli-run2.sh` now sends AHome tasks only to local models (`cli_pool.py pick local`); `scripts/cli_pool.py` now reads only error lines for limits, puts all `openrouter/` entries on cooldown to 00:00 UTC on the OpenRouter daily cap, and lists new OpenCode free models. Both checked with `py_compile`, `bash -n`, and unit tests against a scratch state file.
No new CLI was installed. Installed tools (kilo, opencode, devin, gemini, qwen, goose, crush, cline, kimi, ollama, agy) already had runner branches.
Vendor limits and which free services need the owner: `ops/USAGE_LIMITS.md`, `ops/research/free-tools-2026-11-12.md`.
