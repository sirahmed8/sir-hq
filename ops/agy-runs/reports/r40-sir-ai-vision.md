# REPORT: SIR AI round 40 (2026-11-12) — PLANNING AND RESEARCH ROUND
Worker: Kilo (kilo/kilo-auto/free). Session date: 2026-11-12. Status: ok.
Repo: sirahmed8/sir-ai (commit 9f4937f, pushed to main). Shared: sirahmed8/sir-hq (commit b84afae, pushed to main).
CI: GitHub Actions run 43127101895 `verify` (typecheck, lint, test, firebase-emulator rules, build, gitleaks) — conclusion success, completed 2026-11-12T00:27:34Z.

## 1. What was done

### 1.1 Research — agentic OS platforms, memory systems, local voice
Researched (web search + licence check) and cloned shallow (`git clone --depth 1`) as read-only reference into `D:\Projects\SIR AI\legacy\agentic-os-research/` with licences kept; nothing edited, nothing deleted, nothing copied into SIR AI code (clean-room rule; legacy/Odysseus app AGPL remains reference only). `legacy/` is gitignored so clones are local reference, not committed.

| Project | Repo | Licence | Cloned OK | What we reuse / learn |
|---|---|---|---|---|
| Agent OS | use-agent-os/agent-os | Apache 2.0 | yes | pilot router (cheapest capable model per task), multi-provider support |
| Open Agent OS | openit-ai/open-agent-os | Apache 2.0 / BSL 1.1 | yes | Telegram channel, self-hosted mini-PC-to-team edition model |
| OpenHands | All-Hands-AI/OpenHands | MIT | yes | agent control center, agent abstraction, sandboxed execution |
| Goose | aaif-goose/goose | Apache 2.0 | retry running (network stalled twice; last attempt in progress) | desktop app + CLI + API, MCP tool connections, ACP IDE integration |
| Hermes Agent | NousResearch/hermes-agent | MIT | yes (LICENSE verified) | self-improving skills, persistent memory, multi-platform gateway incl. Telegram |
| mem0 | mem0ai/mem0 | Apache 2.0 | yes | add()/search() per-user memory layer |
| Letta | letta-ai/letta | Apache 2.0 | yes | stateful agent runtime, agent-edited memory tiers |
| Whisper | openai/whisper | MIT | yes | local STT for Owner Edition offline voice |

Decisions recorded in `.sir/plans/PERSONAL_AI_PLATFORM.md` section 3: no code copied; mem0-style per-user memory over tiered P0-P3 Firestore documents; Letta whole-runtime kept for Owner Edition later; voice starts with browser Web Speech API (T-06E), upgrades to local Faster-Whisper/Piper (T-06A); desktop bundles or installs the user's own free CLI agents and signs into them via each CLI's own login flow.

### 1.2 New plan: `.sir/plans/PERSONAL_AI_PLATFORM.md`
Sections: 1 purpose; 2 architecture (accounts/identity, Firebase sync, desktop agent, phone remote, tool and CLI bundling, memory model P0-P3, permissions and privacy, anti-copy account gating); 3 research table; 4 phased roadmap M0-M6 with owner-visible milestones; 5 free-tier cost plan (Firebase Spark, Firebase Hosting, Vercel Hobby, Telegram, Gemini free tier, OpenRouter free models only, local Ollama; nothing purchased); 6 open decisions and risks.

### 1.3 Website audit
There is no separate "AI Hub" screen; the AI surface is the Ask card (`apps/web/src/screens/AskCard.tsx`) calling `POST /api/ask` on the Vercel API (`apps/web/src/lib/ai.ts`).

**Connection / "needs a connection" states found:**
- Integrations (`apps/web/src/screens/Integrations.tsx`, `apps/web/src/data/integrations.ts`): google, ticktick, ms-todo, notion, caldav (apple), whatsapp (file import), health-import (file import). Each has five states: not_connected (default), connecting, connected, error, revoked. All start not_connected. OAuth connect returns `setup_needed` ("This connection needs server keys that are not set up yet.") when `OAUTH_*_CLIENT_ID/SECRET` are missing server side.
- Telegram (`apps/web/src/screens/Telegram.tsx`): unlinked / waiting / linked; `tg.unavailable.body` ("The bot name is not set yet") shows when `VITE_TELEGRAM_BOT_USERNAME` is unset; deep link `https://t.me/SirAiAssistantBot?start=<code>` only renders when username configured.
- Devices (`apps/web/src/screens/Devices.tsx`): "No device connected yet" until the agent service runs and registers.
- Ask card AI: `ask.err.not_configured` ("The AI service is not switched on yet. Asking works as soon as a key is added.") — `/api/ask` answers 503 `ai_not_configured` while no provider key exists (`apps/api/src/handler.ts:80`).

**Features missing against the owner vision (MASTER_PLAN / PLATFORMS / SIR_AI_ASSISTANT_REQUIREMENTS):**
- Live OAuth consents (Google, TickTick, Microsoft To Do, Notion): server routes and encrypted vault tested on fakes; live consent needs owner's own sign-in to click Allow.
- Paymob payments / plan activation: checkout route tested on fake Paymob; activation callback not built (T-051 open; sandbox keys do not exist).
- Phone Capacitor shells (iOS/Android): not built (T-066).
- Web Push with quick replies (T-061): not started.
- QR device pairing (T-063): devices/commands/approvals collections exist; pairing by QR not built.
- Signed Windows installer / first GitHub Release for auto-update and `#/download` Windows link (T-06C): not published.
- Voice model picker and model list UI: none. Voice is browser speechSynthesis with `lang` from locale (ar-EG/en-US), no voice selection (`apps/web/src/lib/voice.ts`).
- Local STT/TTS Owner Edition (T-06A/T-06E): T-06E screen exists (mic + speaker on Ask card); T-06A not started.
- Proactive recommendations: server generator verified on fakes; real picks need an AI key.
- Episodic memory learning: profile exists; learning loop not built.

**AI model list / voice models (current state):**
- Model list is configuration-only: env `AI_BASE_URL`, `AI_API_KEY`, `AI_MODEL`, `AI_ID` plus `AI2_*` (`packages/core/src/providers.ts:196`). No user-visible model list, picker, or refresh from `GET /v1beta/models` or OpenRouter in the UI.
- Fallback chain implemented in code (`packages/core/src/providers.ts`, `packages/ai-chain`): Gemini flash-lite-latest, flash-latest, other Gemini text models, OpenRouter free ranked daily, Groq/Cerebras/Mistral/Cloudflare/NVIDIA/GitHub Models/Hugging Face, local Ollama last; cooldowns 60 min quota / 6 h rejected key / 15 min fast failure. Privacy router enforces tiers (`packages/core/src/privacy.ts`); P3 to external throws `PrivacyBlocked`.
- No live key: `/api/health` reports aiConfigured false until the owner adds keys.

**Upgrade plan:** add a model list + provider choice in Settings (or a new AI screen) refreshed from Gemini model endpoint and OpenRouter daily; add voice selection from `speechSynthesis.getVoices()` with locale-matched defaults; wire a live key once the owner adds it; keep privacy tiers enforced.

### 1.4 Plan updates and checklist
- `_SIR/plans/SIR_AI_ASSISTANT_REQUIREMENTS.md`: added section 4 "Platform research (round 40, 2026-11-12)" with the research table and decisions.
- `.sir/MASTER_PLAN.md`: added section 19 "Platform research round 40 (2026-11-12)" pointing to PERSONAL_AI_PLATFORM.md.
- `.sir/TASKS.md`: added "R40 Research and planning round (2026-11-12)" section, T-080 to T-083 ticked with evidence:
  - T-080 research — clones present + PERSONAL_AI_PLATFORM.md section 3
  - T-081 docs — PERSONAL_AI_PLATFORM.md sections 1-6
  - T-082 qa — website audit (this report)
  - T-083 docs — both plan files updated
- `_SIR/ops/bus/sir-hq.md`: added one line at top (newest first): `2026-11-12 from sir-ai (SIR AI - r40-sir-ai-vision: planning and research round)` with done/evidence/signal.

## 2. Commands run and real output

- `npm run typecheck` (SIR AI): all 10 workspaces clean (`@sir-ai/agent`, `@sir-ai/api`, `@sir-ai/bot`, `@sir-ai/desktop`, `@sir-ai/web`, `tsc -p . --noEmit` each with no output).
- `npm run lint` (SIR AI): `eslint .` clean, no output.
- `npm test` (SIR AI): `24 passed (24)`, `210 passed (210)`, duration 2.12s.
- `npm run build` (SIR AI): `✓ built in 2.93s`; one chunk-size warning (index-I6WxyHQE.js 859.02 kB, over 500 kB advisory only), not an error.
- Commits: `9f4937f docs(r40): personal AI platform plan, agentic OS research, website audit` (3 files, 123 insertions); `b84afae docs(sir-ai r40): platform research decisions in requirements and HQ bus note` (2 files, 37 insertions).
- `git push`: `8012ade..9f4937f main -> main` (sirahmed8/sir-ai); `4082538..b84afae main -> main` (sirahmed8/sir-hq).
- `gh run view 43127101895`: `{"conclusion":"success","status":"completed",...}`.

## 3. Unsure / open
- `goose` clone stalled twice on network timeout; retry (`bgp_1cd24186500181ozJ62JtFskd5`) was still running at session end. Research table already documents goose from web sources; licence (Apache 2.0) confirmed via web. Re-verify clone next round.
- CI verified only for `sirahmed8/sir-ai`. `_SIR` (sirahmed8/sir-hq) has pre-existing uncommitted changes from other rounds (r41 disk cleanup deletions etc.) which I deliberately did not touch or commit, per "never revert previous model's work".
- No screenshots taken this round (research/planning, no UI changes); evidence is command output and files.
- `_SIR` repo CI not checked (no workflow verified for it).

## 4. Recommended next steps
1. Owner adds AI provider keys (`GEMINI_API_KEY`, `OPENROUTER_API_KEY`) to Vercel so `/api/ask` works live; complete one live OAuth consent screen per provider (owner sign-in only).
2. T-051 Paymob sandbox run and plan-activation callback.
3. T-061 Web Push, T-066 Capacitor shells, QR pairing (T-063), signed Windows installer + first GitHub Release (T-06C).
4. AI UI upgrades: model list + provider picker, voice model selection.
5. Commit this report to `sirahmed8/sir-hq` and run `python D:/Projects/_SIR/scripts/agy-done.py r40-sir-ai-vision ok "..."`.

## 5. Files changed (this round)
New: `.sir/plans/PERSONAL_AI_PLATFORM.md` (SIR AI).
Modified: `.sir/MASTER_PLAN.md` (section 19), `.sir/TASKS.md` (R40 section, T-080..T-083 ticked), `_SIR/plans/SIR_AI_ASSISTANT_REQUIREMENTS.md` (section 4), `_SIR/ops/bus/sir-hq.md` (one bus line).
Not committed (gitignored/local only): `legacy/agentic-os-research/` clones (8 directories; goose clone finishing), `.sir/.memory/` (pre-existing untracked), `_SIR` unrelated pre-existing modifications from other rounds (left untouched).
