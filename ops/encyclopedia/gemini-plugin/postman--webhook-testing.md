# webhook-testing

- Tool: `gemini-plugin` (plugin: `postman`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\postman\skills\webhook-testing\SKILL.md`
- SKILL.md size: 6201 chars

## What it does

Capture, forward to localhost, replay, and validate webhook deliveries using a reusable public URL. Keep sender configuration across debugging sessions and record arrivals even while local forwarding is stopped, helping distinguish delivery failures from local connectivity issues. Use for implementing or debugging incoming handlers and testing webhooks an API sends, whether or not Postman is mentioned. Example requests include "get payment events to localhost," "inspect a webhook delivery," and "replay an event after a fix"; these illustrate intent, not an exhaustive list or exact phrases to match.

## When to use (from skill text)

- `stripe trigger <event>` or a GitHub redelivery), then replay that recorded

## Structure (headings inside SKILL.md)

- Webhook Testing
- Get a sender reaching localhost
- Gotchas / Notes
- Handing over
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **A permission error needs workspace context.** Check the selected workspace
- - **Confirm before `delete`.** It's permanent, and a sender still registered

## Key rules (verbatim lines from SKILL.md)

1. - **Confirm before `delete`.** It's permanent, and a sender still registered

## Files inside the skill

- `reference/forwarding.md` — "Forwarding lifecycle"
- `reference/outbound_webhooks.md` — "Testing the webhooks your API sends"
- `reference/webhook_scripts.md` — "Webhook scripts"
