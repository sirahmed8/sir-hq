# PLAN: SIR AI (Wave 4, plans done, no product code yet)
Audited 2026-11-10. Replaces the old `SIR AI (v1)`, `SIR Tele Gateway` and the archived AgentsRoom (all in `legacy/`, kept until M6). `Odysseus app` in `legacy/` is AGPL-3.0 and is reference only: no code is copied from it, ever.
Two tiers, built in this order: Tier 1 is Ahmed's personal assistant on his own PC (private, exempt from commercial items). Tier 2 is a paid multi-user cloud version and starts only after Tier 1 is verified end to end.

## 1. Purpose (plain words)
An assistant Ahmed talks to by voice, text or camera on his own computer. It uses models that run on his machine first, remembers things he allows it to remember (and forgets on request), runs approved tasks, and reaches him through Telegram. Tier 2 would let other people use a hosted version with their own accounts.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR AI` |
| GitHub (private) | `sirahmed8/sir-ai` |
| Stack (planned) | pnpm monorepo: `apps/gateway` (Python 3.12, uv, FastAPI), `apps/web` (local UI, Next.js or Vite), `packages/*`; local models via Ollama in `D:\Projects\AI_Models_Hub`; speech: Faster-Whisper on the laptop GPU, text to speech engine to choose in an ADR (Edge-TTS is an unofficial client of a Microsoft service: terms "(unsourced, verify)"; default fallback is a local open-source TTS) |
| Domain | none for Tier 1. Tier 2 candidate `sir-ai.app`, owner buys |
| Platforms | Tier 1: Windows desktop + local web UI + Telegram. Tier 2: web and PWA, Android later. macOS, Linux, TV, watch: skipped for now |
| Money | Tier 1 none. Tier 2: free local-only mode, Pro in EGP for cloud models and sync (price to test, "(unsourced, verify)"); "launching soon" fallback |

## 3. Current state
Not built. Verified from files: `legacy/` contains the old code; `.sir/reports/deep-scan.md` and an upgraded `.sir/PLAN.md`, `ARCHITECTURE.md`, `TASKS.md` (44 tasks over M0 to M6), `QUALITY.md`, `PRODUCTION.md` exist. The checkpoint (2026-11-08) says T-003 deep scan done and the next step is T-004, initialize the monorepo. No application code, no tests in this folder (git log: 10 commits, all documents). PORTFOLIO.md: 3 of 44 tasks. The old v1 claims (259 tests, voice pipeline, SQLite vector memory) are legacy, unverified.
Old defects to avoid (from the earlier inventory): session tokens in localStorage, client-trusted owner paths, hard-coded owner identities, a mock dev token bypass, a privacy page claiming SOC 2 and ISO that was not earned, a 73 MB model file tracked in git, a literal Firebase key in JS files.

## 4. Security and conduct rules
1. Telegram control: one allow-listed chat id; any action that changes files, runs a program or spends money needs an approval tap (inline button) and is written to an audit log. Test: a command from another chat id is ignored; an unapproved destructive tool call is refused.
2. No tool may run a shell command built from model output without an allow-list of commands and a dry run. Test: prompt-injection fixtures (web page text telling the agent to "delete files") do nothing.
3. Memory: the user sees, edits and deletes every memory; private text never goes to outside providers; routing flag `private=true` forces local models. Test: with `private=true` and the local model off, the call fails closed instead of using the cloud.
4. Provider chain with failover (local, then free cloud tiers); keys only on the server side, never in a client bundle or git; model files are not committed (git LFS or download script).
5. AGPL boundary: a CI check that no Odysseus source or dependency enters `apps/` or `packages/`.
6. Tier 2 only: cookies HttpOnly, per-user quota, tenant isolation tests, privacy page that claims only what is true (no SOC 2 or ISO claim).
7. Camera/microphone: explicit start button, visible indicator, nothing recorded without a switch; recordings stay local.

## 5. Shared pieces
This product is the idea source of Platform `ai-proxy`, but Platform builds its own small `ai-proxy` first (other products need it before SIR AI exists). SIR AI later consumes `@sir/ai-proxy` and adds local routing and tools on top. Telegram: the shared sender `_SIR/scripts/deliver/` for outbound; the inbound command handler is this product's (port ideas from `legacy/SIR Tele Gateway`). Design: Platform `ui/styles/hooks`. Laptop Manager's game-mode relief may need to pause Ollama: keep an endpoint for it.

## 6. Screens and entities
Chat, Voice mode, Camera/vision, Tasks (approval queue), Memory (what it remembers, with delete), Settings and providers, Owner dashboard (Tier 2), Help. Entities: Conversation, Message, Memory, Tool, Provider, Quota, User, AuditEntry.
Five states, Arabic RTL first and English, light/dark/contrast, 320 px to 4K, WCAG 2.2 AA, own logo.

## 7. AI features and evals
Chat and voice with citations when it uses notes; tool use limited to a small allow-list; eval sets (Arabic and English, 40 prompts each): factuality on a fixed notes set, refusal of unsafe tools, prompt-injection fixtures, latency budget on the laptop (first token under a number to be measured and written down, not guessed). New models chosen monthly from `ops/MODELS.json`. Kill switch per tool and global. Support assistant for Tier 2 grounded in docs, free quota 5 per day, owner unmetered.

## 8. Operations
Tier 1: daemon under Task Scheduler with restart, health endpoint, log rotation, weekly report to Telegram (tasks run, approvals, errors, local model disk use). Tier 2: standard 26 set (status JSON, backups with restore test, cost cap per day, emergency alerts) after launch.

## 9. Launch, legal and visibility (Tier 2 only)
Owner buys domain, cloud plans, payment accounts. Legal pack with an AI-training prohibition clause ("we do not train on customer data without opt-in"), sub-processors list of the real providers used, DPA; lawyer review. Visibility: Arabic and English pages for "local AI assistant for Windows", comparison pages vs named assistants once sourced, `llms.txt`, facts page. None of this starts before Tier 1 is verified.

## 10. Milestones with exit checks
| M | Goal | Exit check |
|---|---|---|
| M0 | Monorepo, CI, ADRs | `pnpm install && pnpm verify` green; ADR for TTS and database; green Actions URL |
| M1 | Text chat on local model | `POST /chat` returns an answer from Ollama; latency number recorded |
| M2 | Telegram bridge with approvals | allow-list and approval tests pass; one real approved task logged |
| M3 | Security | injection fixtures pass; private-routing test passes; AGPL check passes |
| M4 | Voice and memory | speech-to-text word error rate measured on 20 recorded Arabic/English clips; memory delete test |
| M5 | Quality | screenshots at 390/1280, LTR/RTL; offline/local-only mode test |
| M6 | Retirement and Tier 2 decision | legacy moved to `old projects`; written go/no-go for Tier 2 with evidence |

## 11. Next 10 tasks (each under 2 hours)
1. Initialize the pnpm monorepo with `apps/gateway` (uv, FastAPI health route) and `apps/web` shell (T-004). Check: `pnpm verify` green; `GET /health` returns 200.
2. CI: lint, typecheck, tests, gitleaks, AGPL boundary check. Files: `.github/workflows/verify.yml`, `scripts/check-agpl.mjs`. Check: green Actions URL; fixture with an Odysseus file path fails.
3. Provider interface and Ollama adapter with timeout and fallback. Files: `apps/gateway/providers/`. Check: unit tests with a fake server; failover test.
4. Privacy routing flag with fail-closed test. Check: test passes.
5. `/chat` endpoint streaming from the local model. Check: curl output shows streamed tokens; latency recorded in `.sir/evidence/latency.md`.
6. Chat screen with five states in the web shell. Check: screenshots at 390 and 1280.
7. Telegram inbound handler with allow-list and approval buttons (port ideas, not files). Files: `apps/gateway/telegram/`. Check: tests for wrong chat id and unapproved tool.
8. Audit log (append-only JSONL) and viewer. Check: every approved action appears; tamper check by hash chain test.
9. Memory store with list, edit, delete and export. Check: delete test removes it from retrieval.
10. Model download script instead of tracking model files, and `.gitignore` for models. Check: `git ls-files` shows no file over 5 MB.

## 12. Risks and open questions (defaults)
- Over-scope (assistant plus SaaS): default is Tier 1 only until M6.
- Laptop GPU limits: default is small quantized models and a documented minimum spec; measure, then write numbers.
- Unofficial TTS terms: default is local open-source TTS as the shipped default.
- Remote control by Telegram is a high-risk surface: default is read-only commands until M3 passes.
- Competitor and pricing statements: `plans/competitors/sir-ai.md` must carry links or "(unsourced, verify)".

## 13. Only the owner can do
Approve Windows prompts for microphone and camera; sign in to Telegram and provider accounts; paste provider keys into `.env`; Tier 2: buy domain and cloud plans, lawyer review.
