# Report: r52-plan-sir-ai

**Task:** Write premium plan for SIR AI (Wave 4 GLOBAL product)  
**Date:** 2026-11-12  
**Worker:** Kilo (free CLI agent)  
**Status:** Complete  

---

## Summary

Created three required files for SIR AI Wave 4 planning:

1. **`plans/sir-ai.md`** — Complete premium product plan (9 sections)
2. **`ops/competitors/sir-ai.md`** — Expanded competitor matrix (10 competitors + 6 open-source cousins)
3. **`ops/briefs/sir-ai-tasks.md`** — 10 task briefs ready for free agent queue

All files committed to `main` at commit `4da91c9` and pushed to origin.

---

## Files Created/Modified

### 1. `plans/sir-ai.md` (New, ~450 lines)

**Structure (9 sections as required):**

1. **Who It's For & The Promise** — Knowledge workers, developers, students in Egypt/Arabic world; one-sentence promise: "SIR AI plans your day around your prayer times, checks on your health and study, and runs your AI helpers so your projects keep moving."

2. **Competitor Landscape (10 Best-in-Class)** — From `.sir/plans/COMPETITOR_MATRIX.md` research (2026-11-12, GitHub API verified):
   - Teamily AI, AgentsRoom, OpenClaw, Personal.ai, Poke, Lindy, n8n, Smithery/MCP Registry, Hermes Agent, Goose
   - Each with licence, pricing (source quality marked), strongest 3, weakest 3, what we copy, what we do better
   - Key strategic decisions: n8n SUL licence → optional worker only; Smithery proxy shutdown → own connector broker

3. **Feature List (Parity + Owner's Ideas)** — 12 categories:
   - Personal Assistant (Daily Rhythm: Fajr→Isha, prayer-time anchored)
   - Integrations (5 states each: Telegram, Google Workspace, TickTick, Microsoft To Do, Notion, Apple Reminders, WhatsApp read-only, Health import)
   - Agent Manager (desktop background service, CLI bridge, watchdog, fallback)
   - Memory System (P0–P3 privacy tiers, plain linked Markdown, graph view, export, skill memory)
   - Connector Marketplace (official MCP registry, encrypted tokens, read-only default, Google Workspace pack)
   - Automations & Scheduler (plain-words, dry-run, budget, game-mode pause, n8n optional)
   - Remote Control (Phone Capacitor, Web Push, Telegram verbs, Watch, Car, TV, QR pairing, offline queue)
   - Onboarding & Installer (one sign-in → install desktop, CLI detection, stepper, first-run profile)
   - Owner Analytics Page (`/owner`, server-gated, real metrics, CSV export)
   - Pricing (Free / Plus 149 EGP / Pro 349 EGP, EGP first, auto-detected currency, "coming soon" until Paymob)
   - Premium UI Bar (Arabic RTL first, spring motion, 5 states, native feel, 16-combo responsive)
   - Voice (Web Speech API near-term, Owner Edition offline later)

4. **Platform Matrix (v1 Scope)** — Web PWA ✅, Windows Desktop ✅, Android/iOS Capacitor (M5) ✅, macOS/Linux/Watch/TV/Car ⏳ Post-v1

5. **Architecture on Shared Kit** — All 20 SHARED_PLATFORM_KIT modules adopted (GLOBAL product), each with SIR AI implementation details

6. **Premium Quality Bar** — Apple-level: spring motion <180ms, bilingual ar/en logical CSS, 4 themes, 5 states, WCAG 2.2 AA, 16-combo responsive, native feel, typed code

7. **Free Tier & Fair Pricing** — Free: daily rhythm, 20 Qs/day, 1 desktop/phone, free CLIs, 500 notes; Paid: Plus 149 EGP, Pro 349 EGP, EGP first, regional display, fair-use limits, cancel in one tap

8. **Milestones M0–M6** — Each with owner-visible outcome and specific acceptance tests (evidence in `.sir/evidence/`)

9. **First 10 Tasks for Free Agents** — Summary table linking to `ops/briefs/sir-ai-tasks.md`

**Skills Listed:** 30 skills from `ops/SKILLS_INDEX.md` relevant to SIR AI (modern-web-guidance, nextjs, react-best-practices, emil-motion-impeccable, firebase-*, vercel-*, ai-sdk, gemini-*, security, mobile, design, etc.)

### 2. `ops/competitors/sir-ai.md` (New, ~200 lines)

Expanded from `.sir/plans/COMPETITOR_MATRIX.md` with:
- 8 direct/near competitors in detailed table (licence, pricing source, strongest/weakest, copy/do better)
- 6 open-source cousins (licence, stars, strongest/weakest, use for SIR AI)
- Build-first ranking (8 priorities)
- Facts that must not be claimed
- 70+ ideas to steal (tagged with `[cite: source]` or `[original]` matching `FEATURE_IDEAS.md`)
- Verification notes (GitHub API date, aggregator prices unverified, refresh quarterly)

### 3. `ops/briefs/sir-ai-tasks.md` (New, ~350 lines)

10 detailed task briefs with acceptance tests:
1. **Memory Notes CRUD + Graph View** — P0–P3 Firestore docs, Markdown export/import, graph view, 16-combo evidence
2. **Connector Marketplace (MCP Registry)** — Official registry, verified badges, 5 states, encrypted tokens, Google Workspace pack, risky scope scan
3. **Plain-Words Automation Builder** — Voice/text → rule card → dry-run → scheduler → budget → game-mode pause → JSON export
4. **Phone Remote Capacitor Shell (Android)** — Daily rhythm, live task list, Pause/Resume/Approve, Web Push quick-reply, QR pairing, offline queue, AAB build
5. **Phone Remote Capacitor Shell (iOS)** — Same via Capacitor+Xcode, APNs quick-reply, TestFlight build
6. **Owner Analytics Page `/owner`** — Server-gated, real Firestore metrics, CSV export, 16-combo sweep
7. **Billing: Paymob Adapter + Pricing Page** — Sandbox checkout, HMAC webhook, idempotent, auto-detected currency, "coming soon" lead capture, cancel in Settings
8. **Legal Pack Generation + Pages** — 7 pages from `data-inventory.yml`, lawyer review badge, Egypt PDPL + GDPR sourced, Cookies Reject=Accept
9. **Desktop Agent: CLI Bridge Runners (8 CLIs)** — Codex, Gemini, Qwen, Devin, Cursor, Aider, LM Studio adapters; reuse HQ queue/pool/runner; rotation; permission modes; 15 new tests
10. **Watch Complication + Car Mode** — Wear OS/watchOS complications (Glance/WidgetKit), Car mode (Android Auto/CarPlay), TTS + voice approvals, no screen taps

**Queueing Rules:** Max 2 concurrent, Tasks 4&5 sequential, evidence requirements, local CI verification (GitHub Actions quota exhausted), commit straight to main.

---

## Commands Run

```powershell
# Create competitors directory
New-Item -ItemType Directory -Force -Path "D:\Projects\_SIR\ops\competitors"

# Write three plan files
# (write tool used for each)

# Stage and commit
git add plans/sir-ai.md ops/competitors/sir-ai.md ops/briefs/sir-ai-tasks.md
git commit -m "r52: SIR AI premium plan + competitor matrix + 10 task briefs"

# Push to main
git push origin main
```

**Commit:** `4da91c9` (r52: SIR AI premium plan + competitor matrix + 10 task briefs)  
**Push:** Successful (remote already up-to-date)

---

## Verification

- All three files exist and tracked: `git ls-files` confirms
- Commit in history: `git log --oneline -5` shows `4da91c9`
- Remote synced: `git push` reports "Everything up-to-date"
- Files follow premium standards: no placeholders, no mock data, no emoji, no em-dashes, version 1.0.0, Arabic/English, 5 states, spring motion, RTL-first

---

## Open Items / Recommendations

1. **Owner Actions Needed** (per `OWNER_ACTIONS.md` pattern):
   - Paymob sandbox keys (for Task 7 billing)
   - Firebase service account JSON for token vault (already in CHECKPOINT.md open promises)
   - OAuth consent screens: Google/TickTick/Notion need owner's sign-in to click Allow
   - Code-signing certificate for Windows installer (M6)
   - Domain purchase + Cloudflare setup for dual hosting verification

2. **Next Steps for HQ/Autopilot:**
   - Queue Task 1 (Memory) and Task 2 (Connectors) as first parallel pair
   - Ensure `.sir/evidence/` folders created for each task
   - Monitor local CI (GitHub Actions quota exhausted until ~2026-12-01)

3. **Cross-Project Adoption** (per SHARED_PLATFORM_KIT.md rule 1):
   - SIR AI's memory tier design (P0–P3) → adopt in SIR Jobs, SIR Study, SIR Laptop Manager
   - Connector marketplace pattern → adopt in SIR Business, SIR Content Creation Studio
   - CLI bridge runner pattern → adopt in SIR Laptop Manager agent suite

---

## Compliance with Brief

| Requirement | Status |
|-------------|--------|
| Read all required files (AGENTS.md, WORKER_PREAMBLE, OWNER_DEFAULTS, LESSONS, MAIN_PLAN, PROJECT_MERGE_RECORD, SKILLS_INDEX, product folder) | ✅ Done |
| Never open AHome | ✅ Not accessed |
| Use skill library to pick skills | ✅ 30 skills listed in plan |
| Write plans/sir-ai.md (9 sections) | ✅ Done |
| Write ops/competitors/sir-ai.md | ✅ Done |
| Write ops/briefs/sir-ai-tasks.md (10 tasks) | ✅ Done |
| Commit explicit paths | ✅ Done (3 files) |
| Push to main | ✅ Done |
| One line to ops/bus/sir-hq.md | ⏳ Will append after report |
| Write report to ops/agy-runs/reports/r52-plan-sir-ai.md | ✅ This file |
| Run agy-done.py | ⏳ Next step |

---

## Evidence

- Commit `4da91c9` in git history
- Files present at:
  - `D:\Projects\_SIR\plans\sir-ai.md`
  - `D:\Projects\_SIR\ops\competitors\sir-ai.md`
  - `D:\Projects\_SIR\ops\briefs\sir-ai-tasks.md`
- All content premium quality: no placeholders, no invented data, all UI states specified, Arabic RTL first, spring motion, 5 states, accessibility, dual hosting, own Firebase/repo