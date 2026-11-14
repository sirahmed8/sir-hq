# upstream

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\chat-sdk\upstream\SKILL.md`
- SKILL.md size: 7555 chars

## What it does

Build multi-platform chat bots with Chat SDK (`chat` npm package). Use when developers want to scaffold a bot with create-chat-sdk, build a Slack, Teams, Google Chat, Discord, Telegram, GitHub, Linear, or WhatsApp bot, handle mentions, direct messages, subscribed threads, reactions, slash commands, cards, modals, files, or AI streaming, set up webhook routes or multi-adapter bots, send rich cards or streamed AI responses to chat platforms, or build a custom adapter or state adapter.

## When to use (from skill text)

- - `node_modules/chat/resources/guides/build-a-slack-bot-with-vercel-connect.md` — Learn how to build your very own Slackbot with Chat SDK and AI SDK. Vercel Connect supplies runtime Slack tokens and forwards triggers, so you never store a long-lived bot token.

## Structure (headings inside SKILL.md)

- Chat SDK
- Scaffold a new project
- Start with Chat SDK documentation
- Available resources
- Guides
- Templates
- Chat SDK adapters
- Adapter directory
- Adapter catalog package
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - `node_modules/chat/resources/guides/slack-bot-vercel-blob.md` — Build a Slack bot that lists, reads, uploads, and deletes files in Vercel Blob through tool calls. Uses Chat SDK, AI SDK's ToolLoopAgent, and Files SDK's createFileTools factory with approval-gated write tools and a read-only mode.
- - `node_modules/chat/resources/guides/run-and-track-deploys-from-slack.md` — Build a Slack deploy bot with Chat SDK and Vercel Workflow. Dispatch GitHub Actions from a slash command, gate production behind approval, poll for completion, and notify Linear and GitHub when the run finishes.
- - `node_modules/chat/resources/guides/build-a-slack-bot-with-vercel-connect.md` — Learn how to build your very own Slackbot with Chat SDK and AI SDK. Vercel Connect supplies runtime Slack tokens and forwards triggers, so you never store a long-lived bot token.
- - `node_modules/chat/resources/guides/vercel-connect.md` — Use Vercel Connect to call provider APIs like Slack, GitHub, and Snowflake from your agents and services with short-lived, user-authorized tokens instead of long-lived secrets.

## Key rules (verbatim lines from SKILL.md)

1. - `node_modules/chat/resources/guides/build-a-slack-bot-with-vercel-connect.md` — Learn how to build your very own Slackbot with Chat SDK and AI SDK. Vercel Connect supplies runtime Slack tokens and forwards triggers, so you never store a long-lived bot token.
2. - `node_modules/chat/resources/guides/vercel-connect.md` — Use Vercel Connect to call provider APIs like Slack, GitHub, and Snowflake from your agents and services with short-lived, user-authorized tokens instead of long-lived secrets.
3. - Building setup or onboarding flows that need package names, peer dependencies, and install guidance before any adapter is installed.
4. - Discovering required, optional, and credential-mode environment variables for official and vendor-official adapters, including which variables are secrets.

## Files inside the skill

- (SKILL.md only)
