# SIR AI — First 10 Tasks for Free Agents

**Version:** 1.0.0  
**Date:** 2026-11-12  
**Source:** `plans/sir-ai.md` section 9  
**Target:** Free CLI agents (Kilo, OpenCode, Devin CLI, ZCode) via HQ autopilot queue  
**Rule:** Each task has title + one-paragraph brief + acceptance test. Nothing is "live" until verified with evidence in `.sir/evidence/`.

---

## Task 1: Memory Notes CRUD + Graph View

**Brief:** Build the core memory system: per-user Firestore documents for P0–P3 notes with create/read/update/delete, linked Markdown export, and a graph view filtered by project/person. Notes are short Markdown with links to people, projects, dates. User can open, edit, delete any note. Graph view uses force-directed layout (D3 or Cytoscape) with project/person filters. Privacy tier (P0–P3) shown as badge on each node. Export produces a folder of `.md` files + `index.json` with all links. Import validates and restores. All operations idempotent with keys.

**Acceptance Test:**  
1. Signed-in user creates 10 linked notes across 3 projects and 2 people via UI.  
2. Export → folder of 10 `.md` + `index.json` downloads.  
3. Import the folder → 10 notes restored with links intact.  
4. Graph view renders at 320px and 1280px, Arabic RTL + English LTR, light + dark → 0 horizontal scroll, all nodes visible, privacy badges correct.  
5. Firestore rules: cross-uid read/write fails in emulator tests.  
6. Evidence: screenshots in `.sir/evidence/task-1/` at 4 widths × 2 languages × 2 themes.

---

## Task 2: Connector Marketplace (Official MCP Registry)

**Brief:** Implement the connector catalogue sourced from the official MCP registry (registry.modelcontextprotocol.io) with verified-publisher badges. Each connector shows: name, description, publisher, required scopes in plain words, five connection states (not connected / connecting / connected / needs re-auth / error) with one retry button. Per-user OAuth tokens encrypted server-side (AES-256-GCM, `TOKEN_ENCRYPTION_KEY`) in Firestore; tokens never reach browser. Read-only mode by default; write actions require explicit approval from phone/desktop (approval ID with 10-min expiry). Google Workspace pack: Calendar, Gmail read, Drive search, Tasks — one toggle each. Connector health page shows last successful call timestamp + error codes. Local MCP servers on desktop for files/apps (never exposed to internet). Connector sharing between user's devices via account (not public link). Pre-listing scan blocks risky scopes (e.g., `gmail.send` without explicit user consent).

**Acceptance Test:**  
1. User opens Connectors screen → catalogue loads from official registry (cached), verified badges shown.  
2. User clicks "Connect Google Calendar" → OAuth consent screen → tokens encrypted in Firestore (verify in emulator: raw token not readable).  
3. Five states transition correctly: not connected → connecting → connected → (revoke) → not connected.  
4. Write action (create Calendar event) → approval request sent to phone/desktop → user taps Approve → action executes → audit log shows approval ID.  
5. Google Workspace pack: four toggles, each independent, state persists.  
6. Health page shows last success + error codes for each connected connector.  
7. Risky scope scan: connector requiring `gmail.send` without explicit write consent is blocked from catalogue (stays in "review" state).  
8. Evidence: emulator test output + 16-combo screenshots in `.sir/evidence/task-2/`.

---

## Task 3: Plain-Words Automation Builder

**Brief:** Build the "plain words → rule card → dry-run → scheduled execution" flow. User speaks or types: "every Sunday at 9 summarize my unread WhatsApp groups." Assistant parses into structured rule (cron + action + data source), shows as a card with Pause/Edit/Delete. Dry-run button shows preview: "Would fetch 3 groups, summarize each, send 1 Telegram message." User confirms → automation saves. Scheduler runs at specified time (prayer-time aware: "after Fajr" resolves to that day's Fajr). Run history shows single "why" line: "Scheduled: every Sunday 09:00, triggered by cron." Daily automation budget (runs + model calls) with 80% warning banner. Pause all automations during game-mode (foreground game detection via `packages/core/src/manager/resources.ts` or manual focus mode). Export automation as JSON for sharing.

**Acceptance Test:**  
1. User creates 3 automations via voice/text: (a) "every Sunday at 9 summarize WhatsApp" (b) "after Fajr check calendar conflicts" (c) "every weekday 18:00 send me a stretch reminder".  
2. Each shows as editable card with correct cron + action.  
3. Dry-run for (a) shows correct preview (mock WhatsApp data).  
4. Scheduler triggers (a) at next Sunday 09:00 → run history shows "why" line.  
5. Budget warning appears at 80% of daily limit (configurable).  
6. Game-mode pause: start a game → automations pause → game ends → automations resume (verify via `resources.ts` game detection).  
7. Export (a) → JSON imports on another device → runs identically.  
8. Evidence: emulator test output + 16-combo screenshots in `.sir/evidence/task-3/`.

---

## Task 4: Phone Remote Capacitor Shell (Android)

**Brief:** Wrap the existing web PWA (`apps/web`) in Capacitor for Android. Daily-rhythm surface: plan (Fajr), check-ins (midday/evening), Isha summary — all read-only from Firestore. Live desktop task list via `users/{uid}/devices/{desktopId}/commands` with real-time listeners. Buttons: Pause / Resume / Approve (write to `users/{uid}/approvals/{id}` with idempotency key). Web Push with quick-reply actions: "Send / Edit / Later" (Service Worker + Push API, VAPID keys in env). QR pairing: phone scans QR on desktop → writes device record with 10-min expiry, single-use. Offline queue: writes to IndexedDB with idempotency keys; syncs on reconnect (replay with deduplication). Capacitor config: Android permissions for camera (QR), notifications, network. Build: `gradlew assembleRelease` produces signed AAB (debug keystore for dev, release keystore from owner later).

**Acceptance Test:**  
1. `npm run cap:android:build` → AAB builds without errors.  
2. Install on physical device/emulator → app opens, shows daily rhythm (plan + 2 check-ins + summary) from Firestore.  
3. Desktop agent running → phone shows live task list (command ID, status, output tail).  
4. Tap "Pause" on a running task → desktop agent receives approval → task pauses → phone updates status.  
5. Web Push: send test push → notification appears with "Send / Edit / Later" → tap "Send" → `/approve` fires.  
6. QR pairing: desktop shows QR → phone scans → device linked → 10-min expiry enforced (second scan fails).  
7. Offline: airplane mode → create check-in response → reconnect → syncs to Firestore with idempotency key (no duplicate).  
8. 16-combo sweep (320/390/768/1280 × ar/en × light/dark) → 0 horizontal scroll, 0 findings.  
9. Evidence: build log + device screenshots in `.sir/evidence/task-4/`.

---

## Task 5: Phone Remote Capacitor Shell (iOS)

**Brief:** Same as Task 4 for iOS via Capacitor + Xcode. Daily-rhythm surface, live desktop task list, Pause/Resume/Approve, quick-reply notifications via APNs (Apple Push Notification service) fallback since Web Push not fully supported on iOS Safari. QR pairing identical. Offline queue with IndexedDB (Capacitor Storage) + idempotency keys. Capacitor config: iOS permissions for camera (QR), notifications, network. Build: `xcodebuild` produces `.ipa` for TestFlight (debug profile for dev, App Store profile from owner later). TestFlight upload script included.

**Acceptance Test:**  
1. `npm run cap:ios:build` → Xcode project builds, `.ipa` produced.  
2. Install via TestFlight on physical device → all Task 4 features work identically.  
3. APNs quick-reply: send test push → notification with "Send / Edit / Later" → tap "Send" → `/approve` fires.  
4. QR pairing works, 10-min expiry enforced.  
5. Offline queue syncs on reconnect with deduplication.  
6. 16-combo sweep → 0 horizontal scroll, 0 findings.  
7. Evidence: Xcode build log + TestFlight screenshots in `.sir/evidence/task-5/`.

---

## Task 6: Owner Analytics Page `/owner`

**Brief:** Build server-gated `/owner` route (Next.js App Router, Server Component). Gate: middleware verifies Firebase ID token → custom claim `role === 'owner'` (or `OWNER_UIDS` allow-list) → fail closed (403). Content: real-time metrics from Firestore only — active users (7-day), 30-day retention cohort, funnel (visit → sign-up → paid), AI spend per user/day with free-tier cap line (configurable), error heatmap by screen + API route (4xx/5xx counts from logs), subscription counts by plan. All queries use compound indexes (defined in `firestore.indexes.json`). CSV export button: streams CSV of owner metrics (no user content, no PII). Page uses design tokens, five states, 16-combo responsive.

**Acceptance Test:**  
1. Owner signs in → `/owner` returns 200 with real counts from Firestore (verify against emulator seeded data).  
2. Non-owner signs in → `/owner` returns 403 (middleware blocks).  
3. Forged token → 403 (JWKS verification fails).  
4. CSV export → file downloads, contains only aggregate numbers, no UIDs/emails/PII.  
5. Error heatmap: seed 5xx on `/api/ask` → heatmap shows `/api/ask` with count.  
6. AI spend line: free-tier cap shown as horizontal rule with label.  
7. 16-combo sweep → 0 findings, WCAG AA contrast.  
8. Evidence: middleware test output + 16-combo screenshots in `.sir/evidence/task-6/`.

---

## Task 7: Billing — Paymob Adapter + Pricing Page

**Brief:** Implement Paymob (Egypt) payment adapter for Plus/Pro plans. Paymob sandbox: create checkout session (amount in EGP, currency `EGP`, items = plan), redirect user to Paymob hosted page. Webhook: HMAC-SHA256 signature with timestamp inside payload (verify via `signed-webhook` kit), idempotent activation (store `payment_id` in Firestore, duplicate = no-op). On success: set user custom claim `plan = 'plus'|'pro'`, `planExpiresAt` (server time + 30/365 days), grace period 7 days (no mid-service lockout). Pricing page (`/pricing`): EGP first, auto-detected currency from `Accept-Language` + IP (GeoIP) with manual override dropdown (never manual-only). Show monthly + yearly total: "149 EGP/mo (1,490 EGP/yr)". Until Paymob keys exist: buttons show "الاشتراكات تتوفر قريباً" + email lead form (stored in `leads` collection). Cancel in one tap in Settings → immediate cancellation at period end, no prorate refund (per Refunds page). All env keys in Vercel only (`PAYMOB_API_KEY`, `PAYMOB_HMAC_SECRET`, `PAYMOB_INTEGRATION_ID`).

**Acceptance Test:**  
1. Sandbox Paymob payment for Plus (149 EGP) → redirect → complete → webhook fires → user `plan` claim = 'plus', `planExpiresAt` set.  
2. Replay same webhook → no double activation (idempotent).  
3. Pricing page: access from Egypt IP → shows EGP; from US IP → shows USD ≈ 3.0/7.0; manual override works.  
4. No Paymob keys in env → buttons show "الاشتراكات تتوفر قريباً" + email lead form → lead stored in Firestore.  
5. Cancel in Settings → `plan` claim reverts to 'free' at `planExpiresAt` (grace period respected).  
6. 16-combo sweep → 0 findings.  
7. Evidence: Paymob sandbox logs + 16-combo screenshots in `.sir/evidence/task-7/`.

---

## Task 8: Legal Pack Generation + Pages

**Brief:** Generate 7 legal pages from `data-inventory.yml` (what data collected, where it goes, retention). Pages: `/legal/privacy`, `/legal/terms`, `/legal/refunds`, `/legal/cookies`, `/legal/dpa`, `/legal/sub-processors`, `/legal/ai-disclosure`. Each page: markdown in `docs/legal/*.md` → rendered via shared `LegalPage` component. Header badge: "AI-drafted, to be reviewed by a qualified Egyptian lawyer before paid launch". Egypt PDPL 151/2020 + GDPR sourced (links to official texts); Saudi PDPL + others as tasks with "(unsourced, verify)" until sourced. Privacy page: data map table, sub-processor list, no-training clause prominent. Cookies page: Reject All as prominent as Accept (same size/color). Refunds page: auto-renewal notice, one-tap cancel link. DPA: standard clauses for Egypt/EU. AI-disclosure: not medical/legal/religious rulings; prayer times are calculated estimates.

**Acceptance Test:**  
1. All 7 pages exist at `/legal/*` → 200, render correctly.  
2. No fake claims (SOC 2, ISO, "bank-grade encryption", "military-grade", etc.).  
3. Lawyer review badge visible on every page.  
4. Egypt PDPL 151/2020 link works (official Gazette); GDPR link works (eur-lex.europa.eu).  
5. Cookies page: Reject All button = Accept button (size, color, position).  
6. Refunds page: auto-renewal text present, cancel link → Settings page.  
7. 16-combo sweep → 0 findings, WCAG AA.  
8. Evidence: 16-combo screenshots in `.sir/evidence/task-8/`.

---

## Task 9: Desktop Agent — CLI Bridge Runners (8 Remaining CLIs)

**Brief:** Extend `packages/cli-bridge` to run tasks (not just detect) for the 8 remaining CLIs: Codex CLI, Gemini/Antigravity CLI, Qwen Code, Devin CLI, Cursor Agent, Aider, LM Studio. Each adapter implements: `detect()` → returns `{ installed: boolean, signedIn: boolean, version: string }`; `runTask(projectPath, brief, permissionMode)` → spawns CLI non-interactively with its flags (e.g., `codex --non-interactive --permission-mode=auto`), streams stdout/stderr via EventSource/SSE to timeline UI, returns exit code. Reuse HQ queue/pool/runner from `packages/core/src/manager/` (task queue, model pool, runner, watchdog, fallback manager) — not a second implementation. Rotation: on quota limit (60 min cooldown), rejected key (6 h), fast failure (15 min) → runner picks next available CLI. Permission modes: `read-only` (no file writes), `ask` (prompt for each write), `auto` (allow all). Mock CLI test harness for CI (simulates each CLI's output).

**Acceptance Test:**  
1. Each of 8 CLIs: `detect()` returns correct installed/signedIn status on test machine.  
2. Each runs a sample task (`brief: "create hello.txt with content 'test'"`) in a temp project → file created, output streams to timeline.  
3. Rotation: mock quota limit on CLI A → runner switches to CLI B → task completes.  
4. Permission modes: `read-only` blocks writes; `ask` prompts (mocked); `auto` allows.  
5. All 12 CLIs (4 existing + 8 new) runnable via unified API.  
6. Unit tests: 8 new adapter tests + 4 rotation tests + 3 permission tests = 15 new tests pass.  
7. Evidence: test output + timeline screenshots in `.sir/evidence/task-9/`.

---

## Task 10: Watch Complication + Car Mode (Wear OS / watchOS)

**Brief:** Build Wear OS complication (Jetpack Compose + Glance) and watchOS complication (SwiftUI + WidgetKit) showing: next plan item (title + time) and next check-in time (e.g., "Midday check-in in 2h 15m"). Updates at check-in boundaries (Fajr, midday, evening, Isha) via `WorkManager` (Android) / `BackgroundTasks` (iOS) — not push. Car mode: Android Auto + CarPlay screen reading day summary (TTS via Web Speech API / native TTS), voice-only approvals ("Approve task 3" → sends `/approve` via phone relay), no screen taps required. Car mode activates automatically when phone connects to car Bluetooth or Android Auto/CarPlay session starts. All strings from shared i18n (ar/en), bidi isolated.

**Acceptance Test:**  
1. Wear OS: complication installs on emulator/device → shows next plan item + check-in countdown → updates at each prayer-time boundary.  
2. watchOS: complication installs on simulator/device → same data, same update cadence.  
3. Car mode: connect phone to Android Auto (emulator) → screen reads day summary in Arabic/English → say "Approve task 3" → `/approve` fires on backend → desktop agent receives approval.  
4. Voice recognition: Arabic + English commands work (test with 5 phrases each).  
5. No screen interaction needed in car mode (verify: no touch targets on CarPlay/Android Auto screen).  
6. 16-combo sweep on watch complication (circular/rectangular, ar/en, light/dark) → 0 clipping.  
7. Evidence: emulator screenshots + car mode video in `.sir/evidence/task-10/`.

---

## Queueing Rules for HQ Autopilot

- Each task is independent; can run in parallel (max 2 concurrent per `LOW_USAGE_MODE.md`).
- Tasks 4 & 5 (Android/iOS) share Capacitor setup — run sequentially or coordinate.
- Tasks 1, 2, 3, 6, 7, 8, 9, 10 can run in any order.
- Each task brief goes to `ops/briefs/sir-ai-task-{N}.md` when queued.
- Worker reads brief, works in `D:\Projects\SIR AI`, commits to `main`, pushes, updates `.sir/CHECKPOINT.md`.
- Evidence required: command output + 16-combo screenshots (320/390/768/1280 × ar/en × light/dark) in `.sir/evidence/task-{N}/`.
- CI green (local verification while GitHub Actions quota exhausted) before push.
- No pull requests — commit straight to `main`.