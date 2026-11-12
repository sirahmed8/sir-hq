# queues

Tools: gemini-plugin (vercel-plugin). Source: C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\queues\SKILL.md (146 lines, read in full)

## Summary
Expert guide to Vercel Queues (public beta): durable append-only topics with at-least-once delivery, independent consumer groups, 24h default retention (up to 7 days), push (function-invoked) or poll (own workers) modes, `@vercel/queue` SDK with `send`/`handleCallback`, idempotency keys, and retry/acknowledge policies for poison messages.

## When to use / not use
Use for fire-and-forget background jobs, fan-out, buffering, or agent events on Vercel. NOT for multi-step logic needing sleep/hooks/human approval (use Workflows), cron triggers (use cron), or when you need exactly-once semantics (delivery is at-least-once). Queues is the primitive Workflows is built on.

## Inputs, outputs, dependencies
Input: messages (JSON by default; BufferTransport/StreamTransport for binary/large) published via `send(topic, payload, options)`. Output: consumed messages in push handlers (`handleCallback`) or poll workers. Needs: `@vercel/queue` npm package (or `vercel-queue` Python), `vercel link` + `vercel env pull` for local dev, `experimentalTriggers` entry in vercel.json per consumer.

## Key rules
1. Register EVERY consumer topic in vercel.json/vercel.ts `experimentalTriggers` (`queue/v2beta`) — a `handleCallback` route without it never receives messages.
2. Handlers MUST be idempotent — at-least-once delivery means duplicates; key side effects on `metadata.messageId` or `idempotencyKey`.
3. Always define a poison-message policy: `retry` callback acknowledging after deliveryCount threshold, or `maxDeliveries` cap — otherwise failing messages retry until expiry.
4. Send options matter: `idempotencyKey` (dedup within min(retention,24h)), `delaySeconds`, `retentionSeconds` (60s–7d), `region`.
5. Choose the right primitive: Queues for buffering/fan-out, Workflows for durable multi-step, cron for schedules — don't chain topics by hand for workflow logic.

## Risks / owner items
- Public beta: API surface (`queue/v2beta` trigger type) may change.
- Local dev fails without `vercel link`/`env pull` (OIDC token error).
- Poison messages without a cap burn retries and cost; retention max 7 days bounds replay.
- Python SDK exists but Celery/Dramatiq integrations are documented separately.

## Category and tags
cloud, build, automation — vercel, queues, messaging, background-jobs, serverless, beta.

## Revision note
Single plugin revision; concise SDK reference with explicit pitfall list.
