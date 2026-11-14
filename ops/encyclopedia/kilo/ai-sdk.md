# ai-sdk

Source read: `C:\Users\a7med\.codex\skills\ai-sdk\SKILL.md` plus `references/ai-gateway.md`, `references/common-errors.md`, `references/devtools.md`, `references/type-safe-agents.md`, and `overlay.yaml`.

## Summary
This skill is the working guide for Vercel's AI SDK in TypeScript projects. It insists that agents verify every API against the installed package because the SDK changes often, then covers model access through AI Gateway, agents and tools, structured output, streaming, type-safe `useChat` consumption, DevTools, and a catalog of renamed or removed APIs.

## When to use / when NOT
Use when writing or reviewing code that imports `ai`, `@ai-sdk/*`, `useChat`, `streamText`, `generateText`, `ToolLoopAgent`, structured output, embeddings, or provider integrations. Do not use it to justify direct provider SDKs by default, and do not trust remembered model IDs or API names without checking the installed docs.

## Inputs, outputs, tools
Inputs are the project stack, installed `ai` version, desired AI feature, model requirement, and provider or gateway choice. Outputs are current, type-checked code using `generateText`, `streamText`, `ToolLoopAgent`, `Output.*`, typed tool parts, and framework-specific chat wiring. Tools are the `ai` package, provider packages such as `@ai-sdk/openai` or `@ai-sdk/anthropic`, `@ai-sdk/react`, `@ai-sdk/gateway`, Zod schemas, Node.js 22+, the live model list endpoint, bundled `node_modules/ai/docs` and `src`, and optional `@ai-sdk/devtools`.

## 5 most important rules
1. Install only `ai` first, then add provider or framework packages when the task actually needs them.
2. Treat memory as unreliable: search `node_modules/ai/docs/` and `node_modules/ai/src/`, then ai-sdk.dev only when the bundled docs do not answer.
3. Fetch current model IDs from the gateway model endpoint and choose the newest appropriate `provider/model` instead of hardcoding remembered names.
4. Build agents with `ToolLoopAgent` and consume them with inferred `UIMessage` types, typed `tool-{name}` parts, `input`/`output`, and state checks before accessing results.
5. Check `references/common-errors.md` before fixing type errors, then run the project type checker and specify only non-default options.

## Risks / owner notes
The SDK's frequent changes make stale examples dangerous, especially for `useChat`, tool parts, structured output, and renamed parameters. DevTools is local-only and should not ship as a production dependency. The owner should keep the installed `ai` version current, verify provider credentials or gateway access, and confirm model IDs at implementation time.

## Category / tags
ai · ai-sdk, vercel, llm, streaming, tool-calling, agents, structured-output, typescript, usechat

## Revisions
The codex, kilo, cursor, and windsurf copies are identical and selected here because codex includes the reference pack with common errors, gateway, DevTools, and type-safe agent guidance. The gemini-plugin Vercel copy is slightly longer and emphasizes bundled docs plus version checks, but it lacks this encyclopedia entry's fuller reference set.
