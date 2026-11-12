# google-antigravity-sdk

Source read: `C:\Users\a7med\.claude\skills\google-antigravity-sdk\SKILL.md` (claude revision; codex/cursor/gemini-plugin/kilo/opencode/windsurf listed as holders — claude copy chosen per brief priority). Companion `references/` (architecture, agent_configuration, mcp_integration, safety_policies, error_handling, observability, built_in_tools, local_models) and `examples/getting_started/` (20+ topic files) exist; this digest is based on SKILL.md routing plus the referenced topics.

## Summary
Setup-and-routing skill for the `google-antigravity` Python SDK, which builds autonomous agents (Agent, Conversation, Connection) on hosted Gemini models by default (`LocalAgentConfig` + `GEMINI_API_KEY`), with alternatives for Gemini Enterprise/Vertex (Standard ADC or Express API-key mode) and on-device/local models (`LiteRTAgentConfig`, `LocalOpenAIAgentConfig` for Ollama/LM Studio, no key needed). The SKILL.md is mostly a routing table: it points each need (config, MCP, safety policies, error recovery, observability, built-in tools, local models) to a `references/` doc and each pattern (streaming, custom tools, persona, multimodal, subagents, MCP tools, periodic triggers, hooks, cancellation, persistence, structured output, skills, web tools, budget limits, compaction) to an `examples/getting_started/` file.

## When to use / when NOT
Use when designing, implementing, or debugging agents/workflows with the Google Antigravity Python SDK. Do NOT use for the Antigravity IDE product itself or for non-Python agent frameworks.

## Inputs, outputs, tools
- Inputs: an agent task (chat, tools, subagents, triggers, safety policies); auth choice (Gemini API key, Vertex ADC/express key, or local model config).
- Outputs: Python agent code following the SDK's Agent/Conversation/Connection model.
- Tools: `google-antigravity` pip package; env `GEMINI_API_KEY` or `.env`; `gcloud auth application-default login` for Vertex; LiteRT runtime for local models; MCP servers (stdio/SSE) for external tools.

## 5 most important rules
1. Verify the SDK fits the project and install `google-antigravity` before writing code; never assume credentials exist.
2. Hosted Gemini is the default; if `GEMINI_API_KEY` is missing, help the user get one via AI Studio (`aistudio.google.com/app/api-keys`) — do not fabricate a key.
3. Vertex has two modes: Standard (ADC via `gcloud auth application-default login` + `vertex=True` + project/location) and Express (`vertex=True` + `api_key`, no ADC).
4. Route every sub-question to its reference/example file instead of improvising (agent_configuration warns about model-identifier rules; safety_policies covers predicates, ordering, OS sandboxing).
5. Use the budget/compaction examples for long sessions: session operational limits, token budgets, `StopReason` handling, and context compaction thresholds.

## Risks / owner notes
Needs an API key or cloud credentials — owner action if absent. Local models need capable hardware (e.g., Gemma 4 26B class). Safety policies and sandboxing are the owner's responsibility to configure for anything touching real commands.

## Category and tags
Category: ai. Tags: python-sdk, agents, gemini, vertex, mcp, subagents, local-models, safety-policies.
