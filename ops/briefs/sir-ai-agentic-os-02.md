# SIR AI Agentic OS - phase 2: chat stream parser

Read first, in order:
1. D:/Projects/_SIR/ops/briefs/SIR_AI_AGENTIC_OS.md (the owner-approved vision brief)
2. D:/Projects/SIR AI/docs/AGENTIC_OS_PHASE1.md (phase 1 outcome and next slice)
3. D:/Projects/SIR AI/packages/core/src/agentic.ts (shared contracts: ChatEventSchema, CliBridgeOptions.onEvent, ModelPool)
4. D:/Projects/SIR AI/.sir/CHECKPOINT.md

Context: Phase 1 shipped the adapter registry, priority-aware ModelPool, and a CliBridge that emits real status/output events. The honest gap recorded in AGENTIC_OS_PHASE1.md: the stream parser that upgrades raw output into thinking/tool_call/file_diff events and emits fallback when AgentRunner rotates providers is next.

This cycle (phase 2):
1. Implement the chat event stream parser for CliWorker/CliBridge: map raw CLI output chunks into the defined ChatEvent types (thinking, tool_call, file_diff, output, status, error, fallback). Provider-specific patterns may live in a small per-adapter parser module; keep it real, no mocks.
2. Emit a fallback event whenever ModelPool rotates to the next provider mid-request; include the provider that failed and the one taking over.
3. Surface the parsed events through the existing apps/agent -> Firestore path so the web chat UI can render them (extend the CliFleet/chat panel only as needed; reuse existing i18n ar/en).
4. Add tests covering at least: thinking extraction, tool_call extraction, file_diff extraction, fallback event on provider rotation, and error event.
5. Run npm run typecheck, npm run lint, npm test, npm run build; commit and push to main; update .sir/CHECKPOINT.md with evidence.

Constraints: version stays 1.0.0, no PRs, commit straight to main, never touch AHome private content, no secrets in git, RAM rule applies (no heavy local model loads; use CLI adapters only).
