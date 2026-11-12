# SIR AI: what the owner asked for (Ahmed, 2026-11-11, from the HQ chat). Read by the SIR AI project agent.

SIR AI is a general product (subscriptions, many users in Egypt and beyond), not a private tool. It must give every subscriber what Ahmed's HQ gives him today, only better. Ahmed is the first user and the model for the defaults. Currency in EGP first.

## 1. Personal assistant, not only a project manager
- Lives in Telegram (and WhatsApp where allowed, web, mobile). Remembers the user's day: what he did, plans, health, study, work, prayer times, mood. Personalised more every week.
- Day rhythm (all times follow the user's own prayer times and timezone): at Fajr a plan of everything due that day; midday and evening health and sport check-ins that ask "what did you do today" and adapt; after Isha a summary of the day (what the user did, what his agents did, what is left); short quick-reply buttons on every question.
- Proactive: it does not wait to be asked. It finds videos, articles, tools and courses that fit the user and says why in one line. It suggests, warns, advises, thinks with the user. It is an adviser, a thinker and a planner.
- Health and sport: routine plans, reminders, check-ins, gentle follow-up, meals and sleep, no medical claims.
- Study: exam countdowns, plans, study packs per subject, reminders (the SIR Study project holds the study engine).
- Life admin: reads Google Workspace (Gmail, Calendar, Drive, Tasks), TickTick, Telegram and WhatsApp (read only, with the user's consent), keeps TickTick and Calendar current, writes events and reminders from messages it reads.
- Messages are clean: a short title, at most 5 lines, one fact per line, a single action at the end or "nothing needed from you".

## 2. Agent manager (what Ahmed's HQ does)
- Runs a team of AI agents on the user's projects: a queue, one writer per project, a pool of free and paid models with automatic switching when a quota ends, watchdogs that restart stuck workers and fix red CI, a fallback manager that takes over when the main one is gone, daily reports.
- Reference implementation lives in D:/Projects/_SIR: plans/AI_TOOLS_CONTROL.md, scripts/hq_autopilot.py, hq_watchdog.py, hq_manager_tick.py, cli_pool.py, cli-run2.sh, ops/WORKER_PREAMBLE.md, ops/MANAGER_PROMPT.md. Study it and turn the ideas into product architecture (no Ahmed-specific paths or data).
- Management rules to keep: never stop waiting for the user; review with evidence (CI green, screenshots); premium quality; truthful status; privacy tiers (private data never goes to outside models); no hard-coded personal data.

## 3. Product rules
- Own Firebase project and own GitHub repository named exactly SIR AI (create them only if they do not exist; reuse if a project with that name exists).
- Plans first: write MASTER_PLAN, ARCHITECTURE, TASKS, the privacy model, the subscription plan (free tier generous, paid tier for always-on automations), and the legal pages, in `.sir/`.
- Premium UI: Arabic RTL first, English, spring animations, no glitches, tab bars draggable by finger, one shared component set, five states on every view.
- Integrations: Telegram, WhatsApp, Google Workspace, TickTick, Microsoft To Do, Notion, Apple Reminders via CalDAV/ICS, health data import. Each with clear states and a retry.
- AI: several providers with fallback and privacy routing; local models for private data.

## 4. Platform research (round 40, 2026-11-12)
Researched agentic OS platforms, memory systems and local voice. Shallow read-only clones kept in `SIR AI/legacy/agentic-os-research/` with licences (never edited, never deleted):
- Agent OS (use-agent-os/agent-os, Apache 2.0) — pilot router, cheapest-capable-model routing, multi-provider support.
- Open Agent OS (openit-ai/open-agent-os, Apache 2.0/BSL 1.1) — Telegram channel, self-hosted mini-PC edition model.
- OpenHands (All-Hands-AI/OpenHands, MIT) — agent control center, agent abstraction, sandboxed execution.
- Goose (aaif-goose/goose, Apache 2.0) — desktop app + CLI + API, MCP tool connections, ACP IDE integration.
- Hermes Agent (NousResearch/hermes-agent, MIT) — self-improving skills, persistent memory, multi-platform gateway including Telegram.
- mem0 (mem0ai/mem0, Apache 2.0) — add()/search() per-user memory layer.
- Letta (letta-ai/letta, Apache 2.0) — stateful agent runtime with agent-edited memory tiers.
- Whisper (openai/whisper, MIT) — local STT for the offline Owner Edition voice path.
Decisions: no code is copied from any clone; every SIR AI module is clean-room written. Memory follows a mem0-style per-user add/search layer over per-user Firestore documents, tiered P0-P3 like the privacy router; Letta's whole-runtime option is kept for the Owner Edition later. Voice starts with the browser Web Speech API (T-06E) and upgrades to local Faster-Whisper/Piper in the Owner Edition (T-06A). AGPL material in legacy/Odysseus app is reference only, never copied.
