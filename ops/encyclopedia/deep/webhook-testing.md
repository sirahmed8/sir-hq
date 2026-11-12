# webhook-testing (gemini-plugin: postman)

## Summary
webhook-testing uses `postman webhook` to give webhook senders a hosted URL (`https://<webhookId>.webhook.pstmn.io`) that records every delivery (raw headers+body as sent) and forwards to a localhost port — no separate tunnel needed. Two design properties drive usage: REUSE the URL across debugging sessions (sender registered once; `list` resolves references, create new only for new endpoints) and EVERY request is recorded even while forwarding is stopped (`requests describe` shows exact delivery; `requests replay` resends after fixes without needing the sender to refire). Flow for reaching localhost: verify the local route EXISTS first (forwarding to a missing route = eternal 404; dedupe on sender's stable event id, ack intentionally-ignored valid events with 2xx) → reuse-or-create webhook → `postman webhook forward <id> <port>` in background → send one probe to the URL path → confirm 2xx + handler log via `requests list`. reference/webhook_scripts.md covers pm.test validation scripts; outbound_webhooks.md covers testing webhooks YOUR api sends.

## When to use / when NOT
Use for implementing/debugging incoming webhook handlers, getting payment/event webhooks to localhost, inspecting deliveries, replaying after fixes — with or without Postman mentioned. Do NOT use for outbound webhook testing of your own API (see outbound_webhooks.md reference) or when no webhook sender exists.

## Inputs, outputs, tools
- Inputs: webhook id/URL or new endpoint name, local port, sender's event contract.
- Outputs: recorded deliveries (headers+body), forwarded requests, replay capability, validation scripts.
- Tools: `postman webhook` CLI (create/list/forward/requests describe|list|replay/delete), signed-in Postman session.

## 5 most important rules
1. Reuse webhook URLs across sessions — each new one is another URL to register plus a second event history.
2. Check the local ROUTE exists before forwarding; `requests list` separates "never arrived" from "forwarding/routing problem".
3. Build replay/test payloads from the SENDER's documented schema or a real delivery — never from your own handler (that only proves handler agrees with itself).
4. Stripe/Slack signed events FAIL replay verification by design (5-min timestamp window) — send a fresh event, don't loosen verification; GitHub replays still verify.
5. `delete` is permanent and breaks registered senders; replay triggers real handler side effects — choose deliveries deliberately.

## Risks / things needing the owner
Needs a signed-in Postman session (`Authentication required` → sign in, owner auth). Workspace permission errors need the right `-w` workspace — ask if ambiguous. Replay causes real side effects in your handler. Forwarding runs until stopped — remember to kill it.

## Category / tags
automation · postman, webhooks, testing, localhost

## Revisions
Single revision read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\webhook-testing\SKILL.md` (103 lines + 2 references). Gemini-plugin only.
