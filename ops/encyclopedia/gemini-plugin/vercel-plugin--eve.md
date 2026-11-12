# eve

## Summary
A pointer skill for eve, Vercel's filesystem-first framework for durable backend AI agents: an agent is a directory on disk (instructions, skills, tools, connections, channels, subagents, schedules) that eve compiles and runs. The SKILL.md itself contains almost no guidance; it exists to route the agent to the real documentation bundled inside the installed `eve` npm package.

## When to use / when NOT
Use when creating, editing, debugging, or scaffolding an eve project (`.eve/` dirs, `agent/channels/eve.ts`, `npx eve init`, `eve dev/build/start/evals`), or when the overlay's retrieval patterns match (durable sessions, channels, sandboxes, subagents, schedules, Agent Runs observability). Do NOT use for generic agent-building prompts, incidental mentions of "eve", or established non-eve stacks unless the user asks for comparison or migration. The overlay.yaml metadata explicitly excludes "eve online" and "user-agent" false positives.

## Inputs, outputs, tools
- Inputs: an eve project directory or a request to scaffold one (`npx eve init <name>` / `npm install eve`).
- Outputs: none directly; it directs the agent to `node_modules/eve/docs/README.md` for the version-matched index and reading order.
- Tools: filesystem reads of bundled docs; npm/bunx for install and scaffold; Vercel MCP/CLI `vercel agent-runs` for production run traces (per overlay docs links).

## 5 most important rules
1. Never rely on the SKILL.md body for eve guidance — always read `node_modules/eve/docs/` first because it matches the installed version exactly.
2. Start at `node_modules/eve/docs/README.md`; it holds the full index and recommended reading order.
3. If eve is not installed, install it (`npm install eve`) or scaffold with `npx eve init <agent-name>` before reading docs.
4. Treat the agent as files on disk: instructions, skills, tools, connections, channels, subagents and schedules are all files eve compiles.
5. The skill chains to `vercel-connect` when `@vercel/connect/eve` imports appear (managed OAuth for channels/credentials).

## Risks / owner needs
Low risk: it is documentation routing only. Owner-relevant only if a project adopts eve — then Vercel account/MCP access may be needed for Agent Runs observability.

## Category and tags
Category: ai. Tags: agents, vercel, durable-agents, framework-docs, filesystem-first.

## Revisions
Only the gemini-plugin (vercel-plugin) copy exists in this slice's tool set; no competing revisions.
