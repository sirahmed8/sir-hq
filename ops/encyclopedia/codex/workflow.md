# workflow

- Tool: `codex`
- Category: design
- Source: `C:\Users\a7med\.codex\skills\workflow\SKILL.md`
- SKILL.md size: 18376 chars

## What it does

Vercel Workflow DevKit guidance: durable tasks, retries, step execution, and crash-safe orchestration.

## When to use (from skill text)

- async function triggerChild(data: string) {
- const childRunId = await triggerChild("some data");  // Fire-and-forget via step
- - `start()` — trigger a workflow

## Structure (headings inside SKILL.md)

- *CRITICAL*: Always Use Correct `workflow` Documentation
- Official Resources
- Quick Reference
- Prefer Step Functions to Avoid Sandbox Errors
- Workflow Sandbox Limitations
- DurableAgent — AI Agents in Workflows
- Starting Workflows & Child Workflows
- Hooks — Pause & Resume with External Events
- Single event
- Multiple events (iterable hooks)
- Resuming from API routes
- Error Handling
- Serialization
- Streaming
- Namespaced Streams
- Debugging
- Check workflow endpoints are reachable
- Visual dashboard for runs
- CLI inspection (use --json for machine-readable output, --help for full usage)
- For Vercel-deployed projects, specify backend and project
- Open Vercel dashboard in browser for a specific run
- Cancel a running workflow
- --env defaults to "production"; use --env preview for preview deployments
- Testing Workflows
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - `waitForHook(run, { token? })` / `waitForSleep(run)` — wait for workflow to reach a pause point
- - `resumeHook(token, data)` / `resumeWebhook(token, request)` — resume paused workflows
- - Use deterministic hook tokens based on test data for easier resumption

## Key rules (verbatim lines from SKILL.md)

1. 1. **Find docs**: `glob "node_modules/workflow/docs/**/*.mdx"`
2. 2. **Search content**: `grep "your query" node_modules/workflow/docs/`
3. - `getting-started/` - Framework setup (next.mdx, express.mdx, hono.mdx, etc.)

## Files inside the skill

- `overlay.yaml`
- `references/durable-agent-patterns.md` — "Workflow DevKit — DurableAgent Patterns"
