# queues

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: build
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\queues\SKILL.md`
- SKILL.md size: 6701 chars

## What it does

Buffer asynchronous traffic and background.

## When to use (from skill text)

- | Scheduled invocation on a cron | Cron Jobs (`⤳ skill: vercel-functions`) | Time-based trigger, not message-based |
- "experimentalTriggers": [{ "type": "queue/v2beta", "topic": "orders" }]
- | `retry` | trigger `retryAfterSeconds` (60s) | `(error, metadata) => { afterSeconds } \| { acknowledge: true } \| undefined` |

## Structure (headings inside SKILL.md)

- Vercel Queues
- What It Is
- Choose Queues or Workflows
- Quickstart (Next.js App Router)
- Send Options
- Consumer Options and Retries
- Other Runtimes and Frameworks
- Errors
- Common Pitfalls
- References
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 5. **Local dev without credentials**: run `vercel link` and `vercel env pull` first; otherwise `send()` throws `Failed to get OIDC token for local development`.

## Key rules (verbatim lines from SKILL.md)

1. - **Delivery**: at-least-once; handlers must be idempotent
2. - **Poll mode**: pull messages from your own workers in any environment when push delivery to a Vercel Function does not fit. On Vercel, run an always-on poll-mode consumer as a daemon (`⤳ skill: daemons`).
3. 1. **Missing trigger**: a `handleCallback` route with no `experimentalTriggers` entry never receives messages. Register every consumer in `vercel.json`/`vercel.ts`.
4. 4. **Using Queues for multi-step logic**: if you need sleep, hooks, or approvals between steps, use Workflows instead of chaining topics by hand.

## Files inside the skill

- (SKILL.md only)
