# automation

Source read: `C:\Users\a7med\.gemini\antigravity\builtin\skills\automation\SKILL.md` (antigravity-builtin revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A workflow automation skill that defines and executes multi-step agent tasks with conditional branching, error handling, and cross-tool integration. It reads YAML or JSON workflow definitions, executes each step in sequence, and supports retry logic, fallback actions, and checkpoint persistence. The skill is used by the SIR autopilot to orchestrate complex operations across multiple agents and tool ecosystems.

## When to use / when NOT
Use when you need to orchestrate complex, multi-step operations that span different tools or agents — the skill ensures each step completes before the next begins, handles failures gracefully, and persists state so the workflow can be resumed after an interruption. Do NOT use for simple one-command tasks — the skill adds overhead that isn't justified for single-operation tasks. Do NOT modify workflow definitions while a run is in progress — the skill will lock the definition file and reject changes; any edits must wait for the current run to complete or be aborted.

## Inputs, outputs, tools
- Inputs: workflow definition file (YAML/JSON), step list, retry counts, fallback actions, checkpoint directory.
- Outputs: step execution results, success/failure status per step, checkpoint file for resume, logs of all step outputs.
- Tools: filesystem read/write, YAML/JSON parsers, git for checkpoint persistence, node.js for step execution. MCP: antigravity-builtin connector.

## 5 most important rules
1. **Always define a checkpoint directory** — the skill writes a checkpoint file after each step; without this, the workflow cannot be resumed after an interruption or model restart.
2. **Use retry logic sparingly** — the skill retries a step up to 3 times before moving to the fallback; excessive retries can mask underlying issues that should be fixed directly.
3. **Specify fallback actions for critical steps** — if a step fails after retries, the skill executes the fallback; never leave a critical step without a fallback defined.
4. **Persist workflow definitions in version control** — the skill reads from the git repo; if the definition file is lost, the workflow history is lost too.
5. **Review workflow logs after each run** — the skill generates detailed logs; the owner should review them to identify bottlenecks or recurring failures.

## Risks / owner notes
The most common failure is forgetting the checkpoint directory — the next worker cannot resume the workflow and must start from the beginning. The owner should always include a checkpoint path when defining a new workflow. Workflow definitions that are edited mid-run can cause unpredictable behavior; the skill's lock mechanism prevents this, but the owner should be aware that concurrent edits are rejected.

## Category / tags
ops · workflow, automation, orchestration, checkpoint, yaml, error-handling, cross-tool

## Revisions
The antigravity-builtin copy is the only revision; it is not available in claude, codex, cursor, or kilo skill stores. This is the canonical source, and all tool folders should have this deep digest propagated to them via propagate-deep.mjs.