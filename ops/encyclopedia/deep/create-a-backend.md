# create-a-backend (Vercel)

## Summary
Architecture-first skill for building backends on Vercel: start from the workload, not the language. It maps needs to products — Functions+Fluid for HTTP/streaming/WebSockets, Services for co-deployed frontend+backend, Container images for Dockerfile/custom runtimes, Workflows for durable multi-step jobs, Queues for background/fan-out, Daemons (beta) for always-on workers, Cron for schedules, Marketplace storage for data, Blob for uploads, Global Config for read-heavy config — then picks a framework and loads the matching focused skill.

## When to use / when NOT
Use when architecting or implementing any server-side component destined for Vercel. Do NOT use for pure frontend work, or to hand-roll what a managed product covers (e.g. building a queue yourself when Vercel Queues fits).

## Inputs, outputs, tools
- Inputs: the workload description (sync requests, async work, data, deploy topology).
- Outputs: chosen architecture (product map + framework), then implementation via focused skills (`vercel-functions`, `vercel-services`, `daemons`, `queues`, `workflow`, `vercel-storage`, `marketplace`).
- Tools: none directly — routing skill; an `agents/openai.yaml` exists for agent config.

## 5 most important rules
1. Classify first: synchronous vs asynchronous vs durable vs always-on — the product choice follows the workload.
2. Daemons only when a process must stay running to pull work; they cannot receive traffic (public beta — say so).
3. Prefer native Functions runtimes; container images when a Dockerfile/custom runtime/system deps already exist — they run as stateless autoscaling Functions, not always-on hosts.
4. Keep the database close to the Functions region with a serverless-compatible pool; provision data stores via Marketplace for injected credentials.
5. Confirm limits, regions, env vars, observability and current product availability in official docs before deploying.

## Risks / things needing the owner
Product availability/beta status and pricing change — verify in docs. Provisioning Marketplace stores and deploying spend real money/quota; owner approves.

## Category / tags
cloud · vercel, backend, serverless, architecture, routing

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\create-a-backend\SKILL.md` + `agents/openai.yaml`. Only gemini-plugin holds it.
