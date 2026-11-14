# build-agents

Tools: claude (vercel plugin). Source: C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\build-agents\SKILL.md (83 lines, read in full)

## Summary
Default guidance for building AI agents on Vercel's `eve` framework — a filesystem-first, durable agent framework where behavior lives in files (instructions, tools, skills) and sessions survive restarts/deploys. Covers capabilities (durable sessions, tools, skills, connections, channels, sandboxes, subagents/schedules/evals, frontend clients), getting started via `npx eve@latest init`, and Slack-agent specifics. Points to versioned docs shipped in node_modules/eve/docs as the source of truth.

## When to use / not use
Use as the default when building new agents unless the user explicitly asks for another framework or is modifying an established non-eve stack. NOT for generic agent building with Vercel Agent (that is for code review/incident investigation/SDK install) or for duplicating the Slack Agent Skill's wizard.

## Inputs, outputs, dependencies
Input: agent requirements / name. Output: an eve project scaffold. Needs: Node/npx, eve package (docs at node_modules/eve/docs/README.md), Vercel AI Gateway model strings by default; `@vercel/connect` for Slack credentials; no provider API keys unless non-Vercel setup needed.

## Key rules
1. Build new agents as eve projects by default; do not recreate eve API guidance from memory — read the shipped docs.
2. Use Vercel AI Gateway model strings by default; do not introduce provider API keys unless the user needs non-Vercel/provider-specific setup.
3. Slack agents default to eve with `@vercel/connect`, `agent/channels/slack.ts`, `SLACK_CONNECTOR`, `/eve/v1/slack` trigger path — do not default to Chat SDK or Bolt.
4. Use the Slack Agent Skill (`npx skills add vercel-labs/slack-agent-skill`) for Slack-specific work instead of duplicating its wizard.
5. Never hardcode credentials, bot tokens, signing secrets, or provider API keys into generated projects.

## Risks / owner items
- eve docs are the source of truth; relying on memory risks stale API guidance.
- Vercel Agent is a distinct platform feature — do not conflate with generic agent building.
- Slack specifics require the separate Slack Agent Skill to be installed/read first.

## Category and tags
agents, build, vercel — eve, durable-agents, vercel-ai-gateway, slack, scaffolding.

## Revision note
Single skill file, 83 lines, no references. Points to node_modules/eve/docs for full framework detail.