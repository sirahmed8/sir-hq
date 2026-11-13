# SIR AI = the Agentic OS (owner vision, 2026-11-13)

Ahmed's direction: SIR AI becomes THE connected app for everything — the place he opens on mobile and PC to pick his manager, see every tool's status and usage, chat with any agent, and control the whole team. Hermes, OpenClaw, the CLI team, local models and the SIR manager bot all surface inside SIR AI.

## What exists already (verified 2026-11-13)
- Monorepo: `apps/web` (today, automations, settings, download pages), `apps/bot` (Telegram bot with privacy classifier P0-P3), `packages/core`.
- Latest cycle r70: a11y audit clean (0 findings), 324 tests, typecheck+eslint+build green. Next lens queued: offline/error recovery or security/auth.
- Privacy classifier routes private content local-only — keep this as the privacy backbone for the whole OS.

## Vision features to plan (from owner, tonight)
1. Manager picker: choose which agent is "the manager" (Hermes / OpenClaw / backup chain / per-project leads) from one screen.
2. Tool fleet dashboard: every CLI/app (kilo, opencode, devin, aider, cline, codex, gemini, kimi, qwen, goose, crush, dsh, agy, pi, cursor, factory/droid, bionic, hermes, openclaw) with live status, which provider/account it uses, quota/cooldown state, last result.
3. Unified chat: talk to any tool through SIR AI; messages route to the right backend with automatic fallback.
4. Voice: real voice conversations — local STT (whisper-class) for transcripts, local TTS for replies. All on loopback Ollama/sidecar, private audio never leaves the machine.
5. Fallbacks everywhere: every AI call has a best-to-worst chain; every project has an error-recovery path. Local models first for private content.
6. Mobile + PC parity: PWA/Android app already partially exists (download page, APK flow in AHome pattern).

## Constraints
- RAM budget: max ~4 heavy agent processes at once (see FREE_TOOLS_ORGANIZATION.md). SIR AI dashboards must poll status cheaply (files/HTTP), never spawn agents per view.
- No secrets in git; tokens stay in `_local/` env files.
- AHome private content never enters SIR AI cloud paths — local only.
- Version stays 1.0.0; commit straight to main after local verify (CI is quota-red, local gates are the proof).

## Next step for the project chat
Take the first unchecked box in `SIR AI/.sir/PLAN.md` section 8, then add a "Fleet/Manager" epic: read `_SIR/ops/FREE_TOOLS_ORGANIZATION.md` + `ops/backup-manager/latency.json` as the data source for the tool-status API.
