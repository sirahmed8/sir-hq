# vercel-schedules

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\vercel-schedules\SKILL.md`
- SKILL.md size: 15612 chars

## What it does

Vercel Schedules guidance — run a private function, route, or Vercel Queues topic on a cron cadence or once at a set time. Covers static schedules in vercel.json, dynamic per-user schedules with @vercel/schedules, handleSchedule, the vercel schedules CLI, environments, jitter, and migrating from Cron Jobs. Use when adding scheduled or recurring work, one-time reminders, or replacing `crons`.

## When to use (from skill text)

- | Target | Use when | Retries |
- Prefer `function` over `path`. A `path` target exposes your handler to the public internet, and its only protection is a static `CRON_SECRET` that you have to store, check on every request, and rotate. A `function` target has neither problem. Don't pick `path` for new schedules, and don't pick it be
- "experimentalTriggers": [{ "type": "schedule/v1beta" }]

## Structure (headings inside SKILL.md)

- Vercel Schedules
- Choose static or dynamic
- Choose a target
- Quickstart: private function on a static schedule
- Rules that break deployments
- Static schedule properties
- Path targets (Cron Jobs migration only)
- Queue targets and dynamic schedules
- Handlers must be idempotent
- Environments
- Jitter and plan limits
- Migrate from Cron Jobs
- Never do this on Vercel
- Manage and debug
- Related

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - New static schedules start **active in production** and **inactive in Preview and custom environments**. Enable them in the dashboard or with `vercel schedules enable <name> --git-branch <branch> --for 2h`.
- - The CLI defaults to production. Use `--environment`, `--git-branch`, `--user`, or `--local` to pick another set.

## Key rules (verbatim lines from SKILL.md)

1. - The target function must declare `{ "type": "schedule/v1beta" }`, and it must be its **only** trigger. It can't also have a `queue/v2beta` trigger.
2. - Don't add routes or rewrites to a `schedule/v1beta` function. It is private by design.
3. - After an outage, every unexpired occurrence is delivered, so a frequent schedule can fire several times in a row. If the work only makes sense near its scheduled time, compare `scheduledAt` to now and return early.
4. - `node-cron`, `setInterval`, or any in-process scheduler. Functions aren't long-lived, so they never fire reliably.

## Files inside the skill

- (SKILL.md only)
