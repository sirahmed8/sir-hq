# netlify-agent-runner (netlify plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-agent-runner\SKILL.md`. Runs AI coding agents (Claude, Codex, Gemini) remotely on Netlify infra.

## Summary
Remote agent-task runner via `netlify agents:*` CLI only. Prerequisites: site linked to a Netlify project (`netlify link`/`init`) OR pass `--project <name>` directly; CLI authenticated; runs consume plan credits — no credits/agent-limit = blocked, surface to user, don't work around. Strict surface rule: ONLY documented `netlify agents:*` commands + `--help` + public CLI reference — never curl api.netlify.com, never `netlify api` as recovery, never read auth tokens from `~/Library/Preferences/netlify/config.json`. Behavior differences vs local agents: tasks run REMOTELY on the connected repo (uncommitted/unpushed local changes invisible); branch-based — `-b` sets the BASE branch (must be pushed first) but output lands on a NEW branch + Deploy Preview, never overwrites base; asynchronous — `agents:create` returns when queued; NO webhooks/callbacks — must poll `agents:show <id>`/`agents:list`; statuses `new`→`running`→terminal `done|error|cancelled` — only act on results at terminal states. Workflow: create (`--json` for task ID) → poll until terminal → review results on the new branch/Deploy Preview. Options: `-a claude|codex|gemini`, `-p prompt`, `-b branch`, `-m model`, `--project`.

## When to use / when NOT
Use for delegating dev tasks to a remote agent against the site's repo, second opinions from another model, or remote automation. NOT for local code edits (agent can't see unpushed work) or for reaching undocumented API endpoints.

## Inputs, outputs, tools
- Inputs: prompt, agent choice, optional base branch/model/project.
- Outputs: queued task → new branch + Deploy Preview with agent's changes.
- Tools: `netlify agents:create|show|list` CLI; Netlify plan credits; connected git repo.

## 5 most important rules
1. Documented CLI commands ONLY — no curl, no `netlify api` fallback, no token reading.
2. Remote agents see only PUSHED code — warn before tasks that depend on local changes.
3. `-b` sets the base branch, NOT where output lands — results always come on a new branch/Deploy Preview.
4. No completion notifications — poll `agents:show` until `done`/`error`/`cancelled`.
5. Credit exhaustion blocks task creation — report it; don't retry-loop or bypass.

## Risks / owner notes
Consumes real plan credits per run. Agent output needs human review on the Deploy Preview — it's a proposal, not a merge. Pushed-branch visibility means stale remote = wrong results.

## Category and tags
Category: cloud. Tags: netlify, ai-agents, remote-execution, cli, credits, deploy-preview.
