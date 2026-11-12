# dispatching-parallel-agents (superpowers)

## Summary
Pattern for delegating independent work to parallel subagents: group failures/problems by independent domain, give each agent a focused self-contained prompt (specific scope, clear goal, constraints like "don't change other code", defined output), issue all dispatches in ONE response for true parallelism, then review summaries, check for conflicts, run the full suite, and integrate. Includes a when-to-use decision flow and prompt-structure example.

## When to use / when NOT
Use for 2+ independent tasks — e.g. 3+ test files failing with different root causes, independently broken subsystems, investigations needing no shared state. Do NOT use when failures are related (one fix may fix all), when full system state is needed, or when agents would interfere.

## Inputs, outputs, tools
- Inputs: a set of independent problems + context each agent needs.
- Outputs: per-agent summaries of findings/fixes; integrated result after conflict check + full test run.
- Tools: subagent dispatch (general-purpose agents); one dispatch call per domain in the same response.

## 5 most important rules
1. One agent per independent problem domain — never "fix all the tests" (too broad, agent gets lost).
2. Prompts must be self-contained: all context needed, no inherited session history.
3. Multiple dispatches in one response = parallel; one per response = sequential.
4. Constrain scope explicitly ("don't change other code") and demand a specific output format.
5. After they return: read each summary, verify fixes don't conflict, run the FULL suite before integrating.

## Risks / things needing the owner
Parallel agents editing the same files cause conflicts — the independence check exists to prevent that. Subagents burn tokens/quota; don't parallelize trivial work.

## Category / tags
ai · orchestration, subagents, parallelism, delegation

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\superpowers\skills\dispatching-parallel-agents\SKILL.md`. Only gemini-plugin holds it.
