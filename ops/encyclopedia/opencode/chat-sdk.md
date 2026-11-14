# chat-sdk

## Summary
Vercel Chat SDK: a unified TypeScript SDK for building chat bots once and running them across Slack, Teams, Google Chat, Discord, Telegram, GitHub, Linear, WhatsApp (Instagram/Signal/X/Messenger coming). Provides a `Chat` coordinator plus per-platform adapters and state adapters (Redis, ioredis, Postgres, memory). Core model: Chat, Adapter, StateAdapter, Thread, Message, Channel. Handlers cover mentions, DMs, subscribed messages, regex matches, reactions, actions, modals, slash commands, assistant threads, app home, member-joined. Supports streaming via AsyncIterable (prefer AI SDK `result.fullStream`), JSX cards/modals, files, locking/dedupe. Custom adapters implement verification, webhook parsing, thread/channel/message ops, ID encode/decode, and a format converter via `BaseFormatConverter`.

## When to use / when NOT
Use when a bot must run on more than one platform or you want normalized threads/messages/cards/actions with pluggable state. Do NOT use for a single-platform quick bot where the native SDK is simpler, or if you cannot install the `chat` package and read its bundled `node_modules/chat/docs`.

## Inputs, outputs, tools
- Inputs: platform credentials, adapter config, state backend, event handlers, optional JSX cards/modals.
- Outputs: webhook routes (`bot.webhooks.<name>`), normalized messages, posted/edited/deleted messages, streams, cards, modals.
- Tools: TypeScript/Node, `chat` + `@chat-adapter/*`, framework routes (Next.js/Nuxt/Hono), Redis/Postgres for state.

## 5 most important rules
1. Read the published docs in `node_modules/chat/docs` first; exact API is in `dist/index.d.ts` — never guess method names.
2. Stream with `result.fullStream` (not `textStream`) so AI SDK step boundaries survive.
3. Set `jsxImportSource: "chat"` in tsconfig before using JSX cards/modals.
4. Persist state via a state adapter (subscriptions, locks, dedupe, thread state); memory adapter is dev-only.
5. Wire each adapter's `bot.webhooks.<name>` to your HTTP framework routes — one route per platform.

## Risks / things needing the owner
Needs platform app credentials and, for production, a real state backend; adapter feature matrix varies (structured `StreamChunk` is Slack-only). Coming-soon platforms are not available yet.

## Category / tags
design · chat, bots, slack, teams, discord, telegram, adapters, streaming, jsx

## Revisions
Five tools hold it (codex, cursor, kilo, opencode, windsurf — byte-identical codex family, kilo copy used, 8238 chars); gemini-plugin (vercel-plugin) ships a separate newer variant with scaffold/create-chat-sdk and resource guides. No claude copy.