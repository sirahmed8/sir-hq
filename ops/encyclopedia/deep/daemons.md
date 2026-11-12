# daemons (Vercel)

## Summary
Skill for Vercel Daemons (public beta): long-running container-image processes declared under top-level `daemons` in vercel.json — fixed instance counts per region, built from a Dockerfile, rolled out on production deploys, restarted on crash, logs to project Logs, Fluid compute. They pull work (queues, workflows, external APIs) and CANNOT receive inbound traffic. Covers config schema, lifecycle/scaling (including dashboard/CLI overrides that beat vercel.json), graceful SIGTERM shutdown, and consuming Vercel Queues poll mode via `PollingQueueClient`.

## When to use / when NOT
Use only when something must stay running to pull work: always-on queue consumers, Celery/Sidekiq/BullMQ workers, self-hosted runners. For request-driven work prefer Functions or Queues push; for durable steps use Workflows; for schedules use Cron; for untrusted code use Sandbox. Say "public beta" when recommending.

## Inputs, outputs, tools
- Inputs: worker source dir with Dockerfile, `vercel.json` `daemons` block (`root`, `entrypoint`, `instances` per region 0–100, optional `command`, `resources` memory tiers, `terminationGracePeriodSeconds`).
- Outputs: running daemon instances, logs, queue consumption.
- Tools: Vercel deploy/`vercel daemons scale`, `@vercel/queue` `PollingQueueClient`.

## 5 most important rules
1. Daemons sit at top level of vercel.json, never inside `services`; service fields (framework, runtime, bindings) fail validation.
2. Production only during beta — previews don't start daemons; test the image locally.
3. Names: lowercase, `_`/`__`/`-` joined, ≤64 chars; `a-b` vs `a--b` collide in the image repo and fail the build; use `instances` not deprecated `replicas`.
4. SIGTERM handling is mandatory: stop taking work, finish in-flight job, exit within the grace period (default 30s, max 3600); jobs must be idempotent since instances stop anytime.
5. Scaling overrides (dashboard/CLI) persist across deploys and override `instances` — check for overrides before assuming vercel.json changes apply; no autoscaling.

## Risks / things needing the owner
Beta product — availability/limits may change. Rollout runs old+new versions simultaneously, so both must tolerate the same queue/schema. Costs scale with instance counts; owner approves production deploys.

## Category / tags
cloud · vercel, daemons, workers, queues, beta

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\daemons\SKILL.md`. Only gemini-plugin holds it.
