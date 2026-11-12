# run-workflow

Tools: gemini-antigravity-builtin. Source: C:\Users\a7med\.gemini\antigravity\builtin\skills\run-workflow\SKILL.md (198 lines, read in full)

## Summary
How to write dynamic workflow scripts for Antigravity's `run_workflow` tool: a Python script orchestrating many agents via `agent()`, `parallel()`, `pipeline()`, `phase()` — for fan-out-over-lists, staged pipelines, and aggregate-then-report patterns. Agents return schema-validated results via a `finish` tool; workflows run in background with UI cards per agent.

## When to use / not use
Use when a task splits into many independent or staged agent-work pieces (per-file review, per-module implementation, multi-angle analysis). NOT for a single delegated task (use a plain subagent) or legacy workflow files (see migrate-workflows).

## Inputs, outputs, dependencies
Input: inline `Script` or `ScriptPath` file + `Args` JSON + `Description`. Output: tool result with `Logs:`/`Output:` (script prints), per-agent conversation links. Needs: python3 (3.8+) on PATH, `run_workflow` tool, agent types/schemas; primitives include `call_tool`, `trajectory()` for reading prior conversation steps.

## Key rules
1. Orchestration is code: loops, fan-out+aggregate, pipelines — reach for it when the SHAPE of delegation is programmatic, not for one task.
2. Every agent needs a JSON `schema` for its `finish` result — an agent ending without `finish` fails the workflow; `{"type":"string"}` for free-form.
3. `parallel` = concurrent fan-out (one failure cancels all); `pipeline` = sequential; awaiting same agent twice runs once; un-awaited agents never run.
4. Context isolation: agents see neither script nor each other — put ALL needed context in each prompt; use `trajectory()` to feed prior step outputs into child prompts.
5. Workspace modes matter for parallel edits: `"inherit"` shared, `"branch"` isolated clone (for code-editing agents), `"share"` shared repo — wrong choice = merge collisions.

## Risks / owner items
- Workflow agents are MAIN agents (hidden from conversation list) — cost scales with fan-out; use lighter `model` tiers (flash_lite/flash) for simple high-volume work.
- No user questions from inside a workflow — calls needing ungranted approval are denied; design scripts to not block on humans.
- `parallel` all-or-nothing failure semantics: one agent failure cancels siblings — for resilient fan-out, wrap per-item errors in the fn.
- Tool outputs aren't visible unless script logs them; `trajectory()` output truncated at 200k chars; cleared steps need transcript.jsonl.

## Category and tags
ai, automation, build — antigravity, workflows, multi-agent, orchestration, python.

## Revision note
Single builtin revision; the runtime contract for Antigravity dynamic workflows.
