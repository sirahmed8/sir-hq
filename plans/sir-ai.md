# SIR AI: Premium Product Plan

**Version:** 1.0.0 (stays 1.0.0 while under development)  
**Date:** 2026-11-12  
**Project Folder:** `D:\Projects\SIR AI`  
**Firebase Project:** `sir-ai-official` (display name "SIR AI")  
**GitHub Repo:** `sirahmed8/sir-ai` (private)  
**Hosts:** Firebase Hosting `https://sir-ai-official.web.app` + Vercel `https://sir-ai-pi.vercel.app` (same build, dual hosting)  
**Wave:** 4 (GLOBAL product, after PERSONAL wave 2)  
**Owner:** Ahmed Alaa (Vibe Coder)  

---

## 1. Who It's For & The Promise

**For:** Knowledge workers, developers, students, and professionals in Egypt and the Arabic-speaking world who want a personal AI that manages their day around prayer times, checks on health and study, and runs AI coding agents on their projects — all without surrendering privacy.

**One-sentence promise:**  
"SIR AI plans your day around your prayer times, checks on your health and study, and runs your AI helpers so your projects keep moving."

---

## 2. Competitor Landscape (10 Best-in-Class)

From `.sir/plans/COMPETITOR_MATRIX.md` (research 2026-11-12, GitHub API verified):

| # | Product | Licence | Pricing (source) | Strongest 3 | Weakest 3 | Our Edge |
|---|---------|---------|------------------|-------------|-----------|----------|
| 1 | **Teamily AI** | Closed | Not stated | Shared memory, sub-agent teams, proactive summaries | Weak personal-life scope; no desktop agent; unverified "5M users" | Single-owner personal agent; desktop runs local CLIs; explicit P0–P3 privacy tiers |
| 2 | **AgentsRoom** | Closed | Free: 2 projects/6 agents; Pro EUR 7.99/mo or 75/yr (conflicting) | Split view of parallel agents; project cockpit; BYO key no markup | Desktop only, no phone remote; no personal memory; price conflicts on own site | Phone remote + memory across days; personal+work in one place; free CLI agents included |
| 3 | **OpenClaw** | MIT | Free (self-host) | 394k⭐; WhatsApp/Telegram/Slack/Discord gateway; skill folders | Self-hosting burden; community skill security risk; not production-hardened | Hosted account, no server setup; skills sandboxed with per-skill permissions |
| 4 | **Personal.ai** | Closed | ~USD 40/mo (unverified) | Long-term memory product story | Proprietary model only; memory trapped in trained weights; unclear pricing | Memory as readable, editable, exportable plain notes |
| 5 | **Poke** | Closed | Free / Pro USD 19 / Ultra USD 199 (unverified; acquired by Cognition 2026-07) | Zero-app setup via iMessage/SMS/Telegram; human call option | Closed; ownership change = plan uncertainty; platform-dependent | Owner keeps data on own machine/models; no sale risk |
| 6 | **Lindy** | Closed | Plus USD 29.99 / Pro 99.99 / Max 199.99 (no free plan) | Easy agent builder; many integrations; voice calls | Credit pricing unpredictable; no free tier; cloud-only | Free local CLI agents; flat monthly cost, not metered credits |
| 7 | **n8n** | SUL (fair-code) | Cloud: no free plan; Starter ~EUR 20/mo (conflicting) | 400+ integrations; visual editor; self-host | Licence forbids selling as core product; execution pricing | n8n as optional worker behind SIR AI; automations in plain words with sandbox |
| 8 | **Smithery / MCP Registry** | Public dir / Open | Smithery connections reportedly shut down 2026-10 | Huge catalogue (6k–27k servers, unverified) | 22/100 scanned had findings; hosted proxy broke users | Own connector broker on official MCP registry; per-user encrypted tokens; no third-party proxy |
| 9 | **Hermes Agent** | MIT | 262k⭐ | Self-improving skills; persistent memory; multi-platform gateway; cron | Developer-heavy setup; 400 MB clone | Skill creation loop; cron scheduling ideas |
| 10 | **Goose (Block)** | Apache-2.0 | 56k⭐ | Desktop + CLI + API from one core; MCP tools; ACP for IDEs | Large (651 MB); desktop-first, not phone | Desktop packaging + MCP model adapted for phone remote |

**Key strategic decisions from research:**
- n8n's Sustainable Use License forbids selling it as a product core → SIR AI uses n8n only as an optional worker, never the product.
- Smithery hosted proxy reportedly shut down → SIR AI builds its own connector broker on the official MCP registry with per-user encrypted tokens.
- Competitors lack **phone remote + desktop agent + readable memory + flat pricing + free CLI agents** in one package → this is SIR AI's moat.

---

## 3. Feature List (Parity + Owner's Ideas)

### 3.1 Personal Assistant (Daily Rhythm)
- **Fajr Plan**: Full day plan (tasks, calendar, study, sport slot) anchored to that day's Fajr, quick replies: Start / Move / Too much
- **Midday Check-in** (after Dhuhr): Health progress — Done / Partly / Skipped / Tired
- **Evening Check-in** (after Asr/Maghrib): Sport & meal — Trained / Rest day / Injured
- **Isha Summary**: Day recap (user + agents) — Plan tomorrow / Nothing needed
- **Proactive messages** (max 2/day, never during prayer/sleep): growth recommendations (video/article/tool/course with one-line why), deadline warnings, task move suggestions
- **Prayer-time engine**: `adhan` library offline from user coordinates + calculation method; tested against Aladhan API for Cairo; sleep hours only delay, never move earlier

### 3.2 Integrations (Five States Each: Not Connected / Connecting / Connected / Error+Retry / Revoked)
- **Telegram** (first): send/receive, bot `@SirAiAssistantBot` with `/status /pause /resume /tasks /approve`
- **Google Workspace**: Gmail read, Calendar read+write, Drive search, Tasks read+write (with consent)
- **TickTick** / **Microsoft To Do** / **Notion** / **Apple Reminders** (CalDAV/ICS)
- **WhatsApp** (read only, user consent, Cloud API or exported chats; no scraping)
- **Health data import**: file import of exports (Apple Health, Google Fit, Samsung Health)

### 3.3 Agent Manager (Desktop Background Service)
- Task queue with briefs, one writer per project
- Shared model pool with cooldowns (60 min quota / 6 h rejected key / 15 min fast failure)
- Runner rotates models on quota end
- Watchdog restarts stuck workers, queues "fix CI"
- Fallback manager takes over after 50 min silence
- Daily report on Telegram in standard message format
- Free CLI agents (Claude Code, OpenCode, Kilo, Ollama runnable; Codex, Gemini/Antigravity, Qwen Code, Devin, Cursor Agent, Aider, LM Studio detect-only) via `packages/cli-bridge`
- Never stores credentials; signs user in through each CLI's own login flow

### 3.4 Memory System (Per-User Firestore, P0–P3 Privacy Tiers)
- **P0 Public**: Prayer times, generic tips → any provider
- **P1 Personal**: Plans, check-in answers, tasks → no-training providers, minimised
- **P2 Sensitive**: Health notes, mood, email/chat bodies → user-chosen provider with explicit consent, else local only
- **P3 Private Vault**: User-marked private → local models only, never leaves device/server; router refuses (never downgrades) on P3→outside
- Memory as plain linked Markdown notes (Obsidian pattern): user can open, edit, delete any note
- Graph view filtered by project/person
- "Why do you think this?" button on every fact showing source message
- One-tap export all memory as Markdown folder + JSON
- Weekly memory review card (5 unsure facts, confirm/delete)
- Per-context boundaries (work/family/study) never leak (Teamily pattern)
- Skill memory: successful multi-step task → reusable editable skill file (Hermes pattern)
- Agent-owned tiers: core facts always in context, archive searched on demand (Letta pattern)
- Forget-by-topic: "forget everything about project X" removes notes + embeddings

### 3.5 Connector Marketplace (Official MCP Registry)
- Catalogue from official MCP registry with verified-publisher badge
- Per-user OAuth tokens encrypted server-side (AES-256-GCM); no third-party proxy ever holds them
- Five connection states + one retry button
- Permission scopes in plain words before consent
- Read-only by default; write actions need explicit approval from phone/desktop
- Google Workspace pack: Calendar, Gmail read, Drive search, Tasks (one toggle each)
- Connector health page: last successful call, error codes
- Local MCP servers on desktop for files/apps, never exposed to internet
- Connector sharing between user's devices through account, never public link
- Scan each listing for risky scopes before catalogue appearance

### 3.6 Automations & Scheduler
- Built-in scheduler: daily plan, midday/evening check-ins, weekly review anchored to prayer times
- Plain-words automations: "every Sunday at 9 summarize my unread WhatsApp groups" → assistant writes rule, user sees card to pause/edit
- n8n as optional worker (webhooks); never sold as product (licence)
- Automation run history with single "why did it run" line
- Dry-run mode: shows what would send/change before real run
- Daily automation budget (runs + model calls) with 80% warning
- Pause all automations during game/heavy task (game-mode from owner rules)
- Export automation as JSON for sharing/moving

### 3.7 Remote Control (Phone, Watch, Car, TV)
- **Phone remote** (Capacitor shell): live desktop task list with pause/resume/approve
- **Quick-reply Web Push**: "Send / Edit / Later" buttons
- **Telegram verbs**: `/status /pause /resume /tasks /approve`
- **Voice note in Telegram** → becomes task
- **Watch complication** (Wear OS / Apple Watch later): next plan item + check-in time
- **Car mode**: read-aloud day summary, voice-only approvals, no screen taps
- **TV/large-screen**: read-only today's plan
- **QR pairing** for new device (10 min expiry, single use)
- **Offline queue** on phone: write now, sync when connected, idempotency keys
- **Desktop asleep state**: phone offers to wake via relay, never open ports

### 3.8 Onboarding & Installer
- One Google sign-in → account created → next screen "install desktop app" (platform detected)
- Installer checks for free CLI agents on machine, offers to install missing from official sources only
- Setup stepper: step 2 locked until step 1 validates (cognitive-product-intuition rule)
- First-run "tell me about your week" voice/text prompt fills profile in <2 min
- Empty-state cards explain what each screen will do after first connection (no fake data)
- Install-size and disk-space check before download (Windows)

### 3.9 Owner-Only Analytics Page (`/owner`)
- Server-verified owner token (custom claim), fail closed → 403 for everyone else
- Active users, 30-day retention, funnel (visit → sign-up → paid) from real Firestore counts
- AI spend per user/day with free-tier cap line
- Error heatmap by screen + API route (4xx/5xx counts)
- Export owner metrics as CSV for accountant (no user content)

### 3.10 Pricing & Subscriptions (EGP First)
| Plan | Price | Includes |
|------|-------|----------|
| **Free** | 0 | Daily rhythm (Fajr–Isha), 20 quick questions/day, Telegram + web, 1 desktop, 1 phone, free CLI agents, memory up to set note limit |
| **Plus** | 149 EGP/mo / 1,490 EGP/yr | WhatsApp read, full Google + task-app sync, voice, unlimited chat |
| **Pro** | 349 EGP/mo / 3,490 EGP/yr | Agent manager (10 projects), always-on watchdogs, fallback manager |

- USD/EUR/SAR/AED shown by region (auto-detected from locale/IP, manual override)
- Annual shown as monthly equivalent + yearly total
- Paid buttons show "الاشتراكات تتوفر قريباً" + email lead form until Paymob keys exist
- Cancel in one tap in Settings (same place as subscribe)
- No credit meter on Pro for normal use; fair-use limits written plainly

### 3.11 Premium UI Bar (All Platforms)
- Arabic RTL first, English second; CSS logical properties only
- Spring motion (transform/opacity, 120 Hz safe); matching open/close for every sheet/panel/modal
- Dynamic Island pattern: continuous morph, single instance, never covers composer/tab bar
- Tab bar: swipe, active label centered in pill, icon-only inactive, min 44 px
- Active tab scrolls into view on mount and tab change
- Bidi: per-character detection in inputs (Arabic types from right, Latin from left); mixed content uses `<bdi>`/`unicode-bidi: isolate`; never show "(RTL)"/"(LTR)"
- Dark/light/system/high-contrast themes (WCAG 2.2 AA)
- Five states on every screen: idle, loading skeleton, empty+CTA, error+retry, populated
- Native feel: disable browser default text selection & right-click; app's own context menu (relevant actions + refresh); inputs keep normal select/copy/paste
- Touch targets ≥ 44 px; zero horizontal scroll at 320/390/768/1280/1920 px
- Click-target audit in CI (no covered/zero-size hit areas)

### 3.12 Voice (Near-Term, Not M5)
- Browser Web Speech API: speech-to-text into Ask box, text-to-speech read-back of answer (Arabic + English)
- Owner Edition later: offline Faster-Whisper / Piper via `AI_Models_Hub`

---

## 4. Platform Matrix (v1 Scope)

| Platform | v1 Status | Notes |
|----------|-----------|-------|
| **Web (PWA)** | ✅ Primary | Next.js 15 App Router, React 19, TypeScript strict, Tailwind v4 tokens; offline queue (IndexedDB, idempotency keys); service worker |
| **Windows (Desktop)** | ✅ Primary | Electron shell, per-user NSIS installer, auto-update via electron-updater (GitHub Releases), Google sign-in (same Firebase Auth), loads hosted web app, strict CSP, devtools blocked in packaged build |
| **macOS** | ⏳ M6+ | Electron build target; not in v1 |
| **Linux** | ⏳ M6+ | Electron build target; not in v1 |
| **Android** | ✅ M5 | Capacitor shell around same web build; daily-rhythm surface; Web Push quick replies; QR pairing |
| **iOS** | ✅ M5 | Capacitor shell; same as Android; TestFlight for beta |
| **Wear OS** | ⏳ Post-v1 | Complication: next plan item + check-in time |
| **watchOS** | ⏳ Post-v1 | Same as Wear OS |
| **TV (Android TV / tvOS)** | ⏳ Post-v1 | Read-only large-screen view of today's plan |
| **Car (Android Auto / CarPlay)** | ⏳ Post-v1 | Read-aloud day summary, voice-only approvals, no screen taps |

**v1 = Web PWA + Windows Desktop + Android/iOS Capacitor (M5).**  
Desktop is the full assistant (runs background agent, CLI bridge, voice); phone/web are the remote control.

---

## 5. Architecture on Shared Kit (`SHARED_PLATFORM_KIT.md`)

SIR AI adopts **ALL** shared kit components (GLOBAL product):

| Kit Module | SIR AI Implementation |
|------------|----------------------|
| **owner-auth** | Firebase Auth (Google sign-in), ID token verified server-side with JWKS; owner/admin gate via `OWNER_EMAILS`/`OWNER_UIDS` custom claims; HttpOnly Secure SameSite=Strict session cookie; rate limits on sign-in/AI/mutating endpoints; 2FA offer for admin |
| **billing-fallback** | Pricing page with "Subscriptions launching soon" + email capture (Firestore lead); EGP first, USD/SAR/AED auto-detected from locale/IP with manual override; Paymob (Egypt) test mode in code, keys in env only; subscription state server-side only with grace period; signed webhook (HMAC-SHA256, timestamp inside payload, idempotent activation); owner permissions = all permissions in owner dashboard |
| **owner-analytics** | `/owner` route, server-verified owner token fail-closed; real metrics only (users, retention, funnel, AI cost, errors, subscriptions, downloads); 403 for non-owners |
| **notifications** | Telegram sender `_SIR/scripts/deliver/send-telegram.mjs` (token in user env var); report format: title, ≤5 one-fact lines, numbers with meaning, Egyptian Arabic, ends with "المطلوب منك: لا شيء"; weekly report at round times (:00/:30); emergency alerts (outage, leaked key, cost over cap, auth spikes); one bot per product (`@SirAiAssistantBot`), user links account via OAuth PKCE |
| **bot-link** | Telegram bot `@SirAiAssistantBot`; user links account via OAuth through app; states: not linked / linking / linked / syncing / failed+Retry; commands: approval taps, status queries, sync now, unlink |
| **ai-proxy** | Provider chain: 1) Gemini flash-lite-latest 2) Gemini flash 3) Any Gemini 4) OpenRouter free 5) Other free (Groq) 6) Local Ollama; per-project keys on project's own Firebase/GCP + own OpenRouter key; `private=true` forces local, fail closed if unavailable; free users 5/rolling 24h with badge; owners unmetered; `AI_ENABLED` kill switch; daily cost cap in `config/limits.json`; per-product eval sets (Arabic+English), runner exits non-zero below threshold; model selection from `ops/MODELS.json` |
| **design-tokens** | Themes: light, dark, system, high contrast (WCAG 2.2 AA); tokens for colors, spacing (4/8px), radii, shadows, typography, motion; CSS logical properties only, RTL-first; bidi per-character input detection; mixed content `<bdi>` isolation; touch targets ≥44px; five states on every screen; test: screenshots at 320/390/768/1280/1920 LTR/RTL light/dark/contrast; Lighthouse mobile 90+ |
| **motion** | Spring physics only (transform/opacity, 120Hz safe); no layout-thrashing; matching open/close for every sheet/panel/modal/drawer/overlay; Dynamic Island continuous morph, single instance, never covers composer/tab bar; tab bar swipe, centered active label, icon-only inactive, 44px min; active tab scrolls into view on mount/change; reduced-motion path works |
| **changelog** | `CHANGELOG.md` per product, reverse chronological, grouped by version (stays 1.0.0); categories: Added/Changed/Fixed/Security/Removed; owner-visible from Settings + Owner dashboard |
| **help-center** | Grounded in `docs/help/*.md` only; floating drawer support assistant (shared component); local search index; five states; eval set: 20 grounded + 10 ungrounded prompts |
| **signed-webhook** | HMAC-SHA256 with timestamp inside signed body; server-side verification rejects tampered/replayed/unsigned/wrong-timestamp; idempotency keys stored; 10 negative tests |
| **legal-pack** | Generated from `data-inventory.yml`; documents: Privacy, Terms, Refunds (auto-renewal text), Cookies, DPA, Sub-processors, AI-use note; marked "AI-drafted, to be reviewed by qualified Egyptian lawyer before paid launch"; Egypt PDPL 151/2020, GDPR, Saudi PDPL as tasks with "(unsourced, verify)" until sourced; lawyer review mandatory before paid launch |
| **i18n** | Arabic (Egyptian dialect) first, English second; RTL-first logical CSS; bidi isolation; per-character input detection; currency/region auto-detected from locale/IP with manual override; date/time prayer-time aware where relevant; `Intl` for formatting; test: every screen at 320/390/768/1280 Arabic RTL + English LTR |
| **ui/styles/hooks** | Shared components: InputBox (chat, AI, voice, search), TabBar, BottomSheet, SidePanel, Modal, Card, Chip, Button, Select, Avatar, Toast, DynamicIsland; spring config shared; InputBox voice recorder grows from input with spring; reply preview matches input surface; TabBar swipe, centered active label, icon-only inactive, 44px min; Card 8px grid spacing, no sticking, button labels wrap; click-target audit (min 44px, no covered hit areas) automated in CI |
| **dual-hosting** | Firebase Hosting (primary, custom domain, clean Google sign-in) + Vercel (import GitHub repo with Vercel CLI, same build, same env vars); both addresses curl-checked (retry once on timeout); written in checkpoint; DNS: owner buys domain, points to both |
| **competitor-matrix** | `ops/competitors/sir-ai.md` with columns: Competitor, Strengths, Flaws, Our Edge, Ideas to Steal; every claim has source link or "(unsourced, verify)"; parity target: match/exceed best-in-category |
| **security-baseline** | Firestore rules: deny by default, per-tenant/per-user claims, emulator tests (cross-tenant read fails); secrets in env only, gitleaks in CI, legacy keys rotated at launch; CSP no unsafe-inline/eval; analytics load after consent; Reject All as prominent as Accept; user data deletion/export one tap each; graded work never done by AI (100% refusal on assignment/quiz/exam); no fake data |
| **operations-standard-26** | `/api/health`; error digest daily/weekly; nightly backup (Firestore → R2/Cloud Storage) with monthly restore test; weekly dependency update with tests; status page (static JSON); support inbox triaged by assistant (grounded in `docs/help`); weekly Telegram report (simple Arabic, product metrics); emergency alerts; owner contact only for emergencies + sign-in/payment; AI daily cost cap + ad spend cap in `config/limits.json` |
| **launch-package-24** | Domain, Cloudflare project, Firebase project (brand-clean Google sign-in), payment accounts (test mode); legal pack generated, marked for lawyer review; code-signing cert (desktop); dual hosting verified; old site 301 redirects, keys rotated; real content/partners onboarded before invite |
| **visibility-standard-27** | Arabic queries first, Egyptian dialect; one landing page per major feature/entity; `llms.txt`, facts page, JSON-LD (WebApplication, FAQPage, BreadcrumbList, domain-specific); Search Console + Bing steps for owner; weekly AI-answer check script; YouTube tutorials later; no fake reviews/user counts |

---

## 6. Premium Quality Bar (Apple-Level)

| Requirement | Standard |
|-------------|----------|
| **Motion** | Spring physics (transform/opacity only, 120 Hz safe); micro-interactions <180 ms; layout morphing <300 ms; press feedback scale 0.98; matching open/close for every panel; Dynamic Island continuous morph |
| **Bilingual** | Arabic (Egyptian dialect) first, English second; logical CSS properties; per-character bidi detection in inputs; `<bdi>` isolation for mixed content; never show "(RTL)"/"(LTR)" |
| **Themes** | Light, dark, system, high contrast (WCAG 2.2 AA); all colors/spacing/radii/shadows via tokens |
| **Five States** | Every screen: idle, loading skeleton, empty+one CTA, error+retry, populated |
| **Accessibility** | WCAG 2.2 AA; browser audit probe composites translucent ancestors + gradient stops for contrast; wrapping `<label>`/pseudo-element hit area = real touch target; 44 px minimum touch targets; reduced-motion respected; focus visible; ARIA labels on all interactive elements |
| **Responsive** | Zero horizontal scroll at 320, 390, 768, 1280, 1920 px; verified by automated sweep with screenshots |
| **Native Feel** | Browser default text selection & right-click disabled site-wide; app's own context menu (relevant actions + refresh); inputs keep normal select/copy/paste; no visible browser chrome affordances |
| **Code Quality** | Next.js 15+ App Router, React 19, TypeScript strict, Tailwind v4 tokens; layered architecture (presentation/domain/data/core); files <300 lines; no god components; absolute imports; typed everything, no `any`; tsc/eslint/tests green before done |

---

## 7. Free Tier & Fair Pricing (EGP + USD)

### Free Tier (Useful Every Day)
- Daily rhythm: Fajr plan, Isha summary, 2 check-ins
- 20 quick questions/day to AI
- Telegram bot + web PWA
- 1 desktop installation, 1 phone remote
- Free CLI agents (user's own subscriptions)
- Memory up to 500 notes (configurable)
- No ads, no tracking

### Paid Plans (EGP First, Auto-Detected Currency)
| Plan | Monthly | Yearly | Key Unlocks |
|------|---------|--------|-------------|
| **Plus** | 149 EGP | 1,490 EGP | WhatsApp read, full Google Workspace + task apps sync, voice, unlimited chat |
| **Pro** | 349 EGP | 3,490 EGP | Agent manager (10 projects), always-on watchdogs, fallback manager |

- USD ≈ 3.0 / 7.0; EUR ≈ 2.8 / 6.5; SAR ≈ 11.5 / 115; AED ≈ 11.5 / 115 (rates updated from config, not hardcoded)
- Annual shown as "149 EGP/mo (1,490 EGP/yr)" — monthly equivalent + total
- Fair-use limits written plainly on pricing page (no hidden credit meter)
- Cancel in one tap in Settings
- Paid buttons show "الاشتراكات تتوفر قريباً" + email lead until Paymob keys exist
- Owner buys gateway accounts (Paymob, Fawry) himself → `OWNER_ACTIONS.md`

---

## 8. Milestones M0–M6 (With Acceptance Tests)

| Milestone | Owner-Visible Outcome | Acceptance Tests (Evidence in `.sir/evidence/`) |
|-----------|----------------------|------------------------------------------------|
| **M0** Plans & Accounts | Firebase `sir-ai-official` reused; repo `sirahmed8/sir-ai`; paid buttons "coming soon"; dual hosting live | `curl` both hosts → 200, same HTML hash; `/api/health` → `aiConfigured: false`; `.sir/CHECKPOINT.md` updated |
| **M1** Vertical Slice | Web + Telegram live on both hosts; Fajr plan, midday/evening check-ins, Isha summary anchored to prayer times; Google sign-in; onboarding stepper; settings | 16 combo sweep (320/390/768/1280 × ar/en × light/dark) → 0 findings; Telegram bot `/start <code>` links chat; Fajr message at day's Fajr (not fixed clock); Isha summary at day's Isha; 5 quick questions work; typecheck/lint/tests green |
| **M2** Integrations Live | Google Workspace, TickTick, Microsoft To Do, Notion, WhatsApp import, health import; five connection states each; recommendation picks start when AI key exists | Each integration: OAuth consent screen completes → tokens encrypted in Firestore → five states visible in UI → retry works; recommendation card appears with "why" line; `/api/ask` answers live with AI key; 16 combo sweep → 0 findings |
| **M3** Agent Manager | Queue, model pool, watchdog, fallback manager, daily reports on Telegram; runs in desktop agent service | Desktop agent spawns CLI task (Claude Code/OpenCode/Kilo/Ollama) → output streams to timeline; quota rotation works (mock 60 min limit); watchdog restarts stuck worker → "fix CI" queued; fallback takes over after 50 min silence → daily report on Telegram; 10 projects limit enforced on Pro |
| **M4** Billing, Legal, Admin | Paymob adapter behind owner keys; data export/delete; owner portal `/owner`; legal pages reviewed | Sandbox Paymob payment → plan activates; export all data (Markdown + JSON) in two taps; delete account in two taps; `/owner` → 200 for owner, 403 for others; legal pages at `/legal/*` exist, marked for lawyer review; 16 combo sweep → 0 findings |
| **M5** Platforms & Voice | Capacitor phone shells (Android/iOS); Web Push quick replies; QR device pairing; Web Speech voice on Ask card; Owner Edition local daemon after web slice | Phone app builds + runs on device/emulator; Web Push "Send/Edit/Later" works; QR pairing 10 min single-use; voice STT→Ask box, TTS reads answer (ar/en); Owner Edition daemon starts (Ollama via `AI_Models_Hub`, Faster-Whisper, SQLite); 16 combo sweep on phone → 0 findings |
| **M6** Release & Legacy Retirement | Lighthouse/WCAG audit; security review; signed Windows installer; `legacy/*` moved to `D:\Projects\old projects\` | Lighthouse mobile ≥90, desktop ≥95, accessibility ≥95, best practices ≥95; WCAG 2.2 AA audit → 0 violations; security review (OWASP Top 10) → 0 critical/high; signed NSIS installer installs + auto-updates on clean machine; `legacy/` moved, folder empty; all products on dual hosting curl-checked |

---

## 9. First 10 Tasks for Free Agents (Ready to Queue)

See `ops/briefs/sir-ai-tasks.md` for full briefs. Summary:

| # | Task Title | One-Paragraph Brief |
|---|------------|---------------------|
| 1 | **Memory Notes CRUD + Graph View** | Build the core memory system: per-user Firestore documents for P0–P3 notes with create/read/update/delete, linked Markdown export, and a graph view filtered by project/person. Acceptance: user creates 10 linked notes, exports as folder+JSON, graph renders at 320/1280 ar/en light/dark with 0 horizontal scroll. |
| 2 | **Connector Marketplace (MCP Registry)** | Implement the connector catalogue from the official MCP registry with verified-publisher badges, five connection states, per-user encrypted OAuth tokens, read-only default with explicit write approval, and Google Workspace pack. Acceptance: user connects Google Calendar → tokens encrypted server-side → five states shown → write action requires phone approval → catalogue scan blocks risky scopes. |
| 3 | **Plain-Words Automation Builder** | Build the "every Sunday at 9 summarize my unread WhatsApp groups" flow: user speaks/writes plain words → assistant generates rule card → user pauses/edits → dry-run shows preview → runs on schedule with "why" line in history. Acceptance: 3 automations created via voice/text, dry-run matches actual run, budget warning at 80%, pause during game-mode works. |
| 4 | **Phone Remote Capacitor Shell (Android)** | Wrap the web PWA in Capacitor for Android: daily-rhythm surface (plan, check-ins, pause/resume/approve), Web Push quick-reply buttons, QR pairing (10 min), offline queue with idempotency keys. Acceptance: APK builds, installs on device, shows live desktop task list, quick-reply buttons fire `/approve`, QR pairing works, offline write syncs on reconnect. |
| 5 | **Phone Remote Capacitor Shell (iOS)** | Same as Task 4 for iOS via Capacitor + Xcode: TestFlight build, same feature parity, Web Push via APNs fallback. Acceptance: TestFlight build installs, all Android parity features work, APNs quick-reply delivers. |
| 6 | **Owner Analytics Page `/owner`** | Server-gated page showing active users, 30-day retention, sign-up→paid funnel, AI spend/user/day with free-tier cap line, error heatmap by screen/route, CSV export for accountant. Acceptance: owner token → 200 with real Firestore counts; non-owner token → 403; forged token → 403; CSV contains no user content; 16 combo sweep → 0 findings. |
| 7 | **Billing: Paymob Adapter + Pricing Page** | Paymob sandbox integration: checkout session, webhook (HMAC-SHA256, idempotent), plan activation, grace period. Pricing page: EGP first, auto-detected currency, "coming soon" + email lead until keys exist, cancel in one tap. Acceptance: sandbox payment → plan activates; webhook replay → no double-charge; pricing page shows correct currency by IP; email lead stored in Firestore; cancel button works. |
| 8 | **Legal Pack Generation + Pages** | Generate Privacy, Terms, Refunds, Cookies, DPA, Sub-processors, AI-use note from `data-inventory.yml`; mark "AI-drafted, lawyer review required"; Egypt PDPL 151/2020 + GDPR sourced; pages at `/legal/*`. Acceptance: all 7 pages exist, no fake claims (SOC 2, ISO), lawyer review badge visible, 16 combo sweep → 0 findings. |
| 9 | **Desktop Agent: CLI Bridge Runners (Codex, Gemini, Qwen, Devin, Cursor, Aider, LM Studio)** | Extend `packages/cli-bridge` to run tasks (not just detect) for the 8 remaining CLIs using their non-interactive flags/permission modes; reuse HQ queue/pool/runner; rotation on quota/refusal/fast failure. Acceptance: each CLI runs a sample task in a test project → output streams to timeline → rotation triggers on mock quota limit → all 12 CLIs runnable. |
| 10 | **Watch Complication + Car Mode (Watch OS / Wear OS)** | Wear OS complication: next plan item + check-in time; watchOS same; Car mode: read-aloud day summary, voice-only approvals, no screen taps. Acceptance: complication updates at check-in boundaries; car mode reads Arabic/English correctly, voice approval fires `/approve`, no screen interaction needed. |

---

## Skills to Use (from `ops/SKILLS_INDEX.md` + `ops/encyclopedia/deep/`)

| Skill | Category | Why for SIR AI |
|-------|----------|----------------|
| `modern-web-guidance` | security | Mandatory for all HTML/CSS/JS tasks (App Router, PWA, bidi, motion) |
| `nextjs` | design | Next.js 15 App Router, Server Components, Server Actions |
| `react-best-practices` | design | Hooks, component structure, performance, a11y, TS patterns |
| `shadcn` | design | Radix UI + Tailwind v4 component patterns |
| `emil-motion-impeccable` | design | Spring physics, micro-interactions, layout morphing |
| `anti-vibecoded-design-system` | design | Bespoke high-contrast tactile UI, no purple gradients/pill buttons |
| `taste-design-engine` | design | Premium visual polish, self-audit, image-to-code replication |
| `mobile-ergonomics-polish` | build | Fluid drawers, responsive touch targets, feedback, no horizontal scroll |
| `a11y-debugging` | design | Chrome DevTools MCP for WCAG AA, semantic HTML, ARIA, focus, tap targets |
| `firebase-auth-basics` | security | Firebase Auth setup, Google sign-in, custom claims, middleware |
| `firebase-firestore` | data | Firestore data models, compound indexes, client SDKs |
| `firestore-rules-creation` | security | Production-grade security rules, deny-by-default, per-user claims |
| `firebase-hosting-basics` | data | Firebase Hosting deploy, custom domains, preview channels |
| `vercel-cli` / `deployments-cicd` | design | Vercel deploy, env vars, project linking, dual hosting |
| `vercel-functions` | design | Serverless/Edge Functions, Fluid Compute, streaming, Cron |
| `ai-sdk` | design | Streaming chat, structured output, tool calling, agents |
| `gemini-api-dev` | design | Gemini API: text, multimodal, structured output, streaming, function calling |
| `gemini-live-api-dev` | design | Real-time bidirectional streaming, voice activity detection |
| `omniroute-resilience-gateway` | automation | AI model routing with multi-provider failover on quota/rate limits |
| `database-reliability-transactions` | data | Atomic transactions, rollback, idempotency keys, keyset pagination |
| `zero-trust-security-hardening` | security | RLS tenant isolation, parameterized queries, secure cookies, rate limiting |
| `vibe-auth-hardening` | security | Cookie security, server-side RBAC, 2FA/OTP, rate-limited endpoints |
| `owasp-vulnerability-shield` | security | OWASP Top 10 audit: injection, SSRF, broken auth, privilege escalation |
| `legal-compliance-shield` | security | Privacy policy matching collection, liability caps, cookie reject, DPAs |
| `modern-app-engineering` | design | Production desktop (Tauri/Electron), mobile (Compose/SwiftUI), cross-platform |
| `android-cli` / `compose-preview` / `device-hub` | design | Android AVDs, Compose previews, device mirroring for Capacitor builds |
| `chrome-devtools` / `debug-optimize-lcp` | research | LCP optimization, performance profiling, browser automation |
| `high-conversion-copywriting` | design | Direct-response copy, sells end state, eliminates AI buzzwords |
| `open-seo-auditor` | design | SEO/GEO: keywords, JSON-LD, AI search visibility |
| `commercial-app-blueprint` | design | llms.txt, case studies, sticky CTAs, trust signals |
| `production-engineering-standards` | ops | Zero-mock persistence, atomic transactions, schema validation, testing |
| `verification` | build | Full-story E2E across browser, API, data flow, runtime |
| `karpathy-skills` | data | Think before code, simplicity first, surgical changes, goal-driven verification |
| `ponytail-yagni-optimizer` | automation | Cut bloat, prefer native platform features over dependencies |
| `sir-ecosystem-orchestrator` | automation | Coordinate Sir Ahmed's workspaces, health check validation |
| `customization-architect` | automation | Audit, token-optimize, cross-platform sync AI customizations |
| `skill-creator` / `skills-discovery-engine` | automation | Find/install/vetted skills for specialized tasks |

---

## Truth Rule Compliance

Nothing in this plan is called "working," "live," or "finished." Status lives only in `.sir/CHECKPOINT.md` and `.sir/TASKS.md` with evidence (command output, screenshots in `.sir/evidence/`). Every claim in this plan is a **target**, not a fact. Verification today is the only truth.

---

## Files to Commit (Explicit Paths)

- `plans/sir-ai.md` (this file)
- `ops/competitors/sir-ai.md` (competitor matrix expanded from `.sir/plans/COMPETITOR_MATRIX.md`)
- `ops/briefs/sir-ai-tasks.md` (10 task briefs)

One line to `ops/bus/sir-hq.md` after push.