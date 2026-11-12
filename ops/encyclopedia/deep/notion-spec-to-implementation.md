# notion-spec-to-implementation

Tools: gemini-plugin (Notion plugin). Source: C:\Users\a7med\.gemini\config\plugins\notion\skills\notion-spec-to-implementation\SKILL.md (+ reference/spec-parsing.md, plan/task/progress templates, examples/)

## Summary
Converts Notion product or technical specs into implementation plans, linked task records, and evidence-based progress updates — preserving requirements, acceptance criteria, dependencies, and traceability back to the spec. It distinguishes plan-only, task-creation, implementation, and progress-update requests and completes the requested combination.

## When to use / not use
Use for planning or implementing a spec, creating tasks from requirements, or reconciling implementation with spec changes. Not for general project setup (that's `notion-set-up-my-project`) or standalone status digests.

## Inputs, outputs, dependencies
Input: a spec page/URL plus optional task database and code access. Output: implementation plan, task records with acceptance criteria and dependencies, status/progress updates linked to the spec. Needs Notion MCP tools; code tools if actual implementation is requested.

## Key rules
1. Extract functional/non-functional requirements, acceptance criteria, constraints, dependencies, explicit out-of-scope items; label assumptions and estimates — never invent commitments.
2. Plan at independently verifiable granularity; no forced task count, phase count, or 1–2-day durations; reuse an existing plan on updates.
3. Tasks need objective, source requirements, testable acceptance criteria, dependencies; check for existing coverage before creating duplicates; never guess assignees, dates, or relation values.
4. Implementation claim discipline: a created plan/task is not evidence of completed work; progress is computed from observed coverage with an explained denominator; statuses change only when work actually starts or meets completion criteria.
5. Spec changes → diff requirements against existing plan/tasks, update affected work, preserve completed work and history, record impact; notify others only when requested.

## Risks / owner items
- When implementation is requested and code tools exist, the skill expects the agent to continue through implementation and validation — not stop at planning.
- Partial batch writes: retain successful IDs, inspect uncertain outcomes, retry only missing work.

## Category and tags
build, ops — notion, spec, implementation, tasks, traceability, mcp.

## Revision note
Single plugin revision; the bridge skill between Notion specs and actual code work.
