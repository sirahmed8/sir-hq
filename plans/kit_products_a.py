"""Per-product blueprint data (part A). Competitor names are research targets to verify at M0, not claims."""

from kit_platforms import R, O, S

A = {
    "sir-platform": dict(
        arch="platform-kit",
        personality="precise, quiet, dependable",
        signature="the `sir-kit` CLI scaffolds a new product folder, CI and tokens in one command",
        modules=[
            "owner-auth: verify Firebase ID tokens via JWKS (jose), OWNER_EMAILS/OWNER_UIDS, email_verified, fail closed",
            "signed-webhook: HMAC over raw body with timestamp inside the payload, timing-safe, idempotent activation",
            "ai-proxy: provider chain (on-device, gemini-free, groq, cerebras, workers-ai, openrouter-free), per-user quota, owner unmetered, refusal hooks",
            "billing: gateway adapters (Paymob, Fawry, Stripe, LemonSqueezy) with the 'Subscriptions Launching Soon' fallback and email capture",
            "legal: pack generated from a product's real data map (privacy, terms, cookies, refunds, DPA, sub-processors)",
            "tokens + ui: palettes from a seed colour (light, dark, high-contrast), components, 5-state primitives, motion springs",
            "i18n + settings: ICU messages, ar/en/zh-Hans/hi, shared Profile/Settings/Onboarding/Consent screens",
            "project-kit: `sir-kit` CLI, CI template, verify script, evidence and checkpoint helpers",
        ],
        entities={
            "ProductConfig": "id, slug, seedColor, locales, platforms, ownerEmails",
            "QuotaLedger": "uid, day, used, limit, ownerBypass",
            "WebhookEvent": "id, provider, receivedAt, signatureOk, processedAt",
        },
        compete=[
            "shadcn/ui and Radix (component patterns)",
            "Supabase/Clerk (auth ergonomics)",
            "Vercel AI SDK (provider routing)",
        ],
        adrs=[
            "Monorepo tooling (pnpm workspaces + Turborepo?)",
            "How products consume the kit (private registry vs git workspace)",
            "Token format (CSS variables + JSON, Style Dictionary or own)",
        ],
        tasks={
            "M0": [
                "Create the workspace, `pnpm verify`, CI, gitleaks, licence audit job",
                "Write `docs/CONTRACTS.md`: public API of every package before coding",
            ],
            "M1": [
                "owner-auth with a forged-token test suite",
                "signed-webhook with replay and tamper tests",
                "tokens + ui kit with Storybook-style gallery used for screenshots",
            ],
            "M2": [
                "ai-proxy with eval harness",
                "billing fallback and email capture",
                "legal pack generator",
                "`sir-kit init` scaffolds a product that passes `verify`",
            ],
        },
    ),
    "sir-obour-hub": dict(
        arch="web-saas",
        personality="focused, encouraging, exam-season calm",
        signature="a 'today plan' card that turns the next exam date into a countdown ring and a three-step study path",
        modules=[
            "content: subjects, lectures, notes, exams, questions (Firestore, published/draft states)",
            "quiz: runner with timers, real persisted attempts, review mode, spaced repetition",
            "community: Q&A threads, replies, moderation queue, alumni",
            "planner: study tasks tied to exam dates, reminders (push, email)",
            "tutor: AI explain/quiz/hint ladder with citations from uploaded notes; refuses graded work",
            "admin: owner dashboard with real counts, content import with dry-run",
            "billing: free tier + Pro (EGP) via the kit fallback",
        ],
        entities={
            "Subject": "id, title, term, order, status",
            "Lecture": "id, subjectId, title, notesRef, status",
            "Question": "id, examId, type, body, options, answerRef, sourceNote",
            "QuizAttempt": "id, uid, quizId, answers, score, startedAt, finishedAt",
            "Thread": "id, subjectId, uid, title, status, createdAt",
            "AiUsage": "uid, day, used, limit",
        },
        compete=[
            "Quizlet",
            "Anki",
            "StudySmarter",
            "Notion (notes)",
            "Moodle (what students already use)",
        ],
        adrs=[
            "Next.js on Cloudflare via OpenNext vs Vite+Hono",
            "Offline packs: Cache API vs IndexedDB",
            "Content moderation approach for Q&A",
        ],
        tasks={
            "M0": [
                "Inventory-driven data export plan: counts per collection from the old DB (read-only)",
                "Choose and record the web stack ADR",
            ],
            "M1": [
                "Subject list + lecture viewer with skeletons, empty and error states",
                "Quiz runner persisting attempts server-side",
            ],
            "M2": [
                "Dry-run importer with counts report",
                "Planner and Q&A",
                "Owner dashboard from real data only",
            ],
            "M4": [
                "Tutor refusal eval set (at least 40 graded-work attempts must be refused with hints)"
            ],
        },
    ),
    "sir-hagoozat": dict(
        arch="web-saas",
        personality="energetic, local, matchday",
        signature="squad balancer: drag players into two teams and watch the fairness meter settle with a spring",
        modules=[
            "booking: pitches, slots, holds, split payment, cancellations",
            "players: profiles, ratings, FUT-style cards, stats",
            "matches: lineups, score, MVP voting, history",
            "communities: groups, invites, chat-lite",
            "owners: pitch owner dashboard (web) for slots, prices, no-shows, payouts",
            "billing: Pro 59 EGP/month and owner plans via the kit fallback (Paymob/Fawry later)",
            "notifications: push, web, in-app, WhatsApp-style reminders via official APIs only",
        ],
        entities={
            "Pitch": "id, ownerId, name, area, geo, pricePerHour, amenities",
            "Slot": "id, pitchId, start, end, status, holdUntil",
            "Booking": "id, slotId, captainUid, splitMode, status, paidAmount",
            "Player": "uid, positions, rating, attributes, cardTier",
            "Match": "id, bookingId, teams, score, mvpUid",
            "Community": "id, name, ownerUid, rules",
        },
        compete=[
            "Playtomic",
            "Spond",
            "Matchi",
            "Local pitch-booking apps and WhatsApp groups (research at M0)",
        ],
        adrs=[
            "Slot hold + double-booking prevention (Durable Objects vs Firestore transactions)",
            "Geo search (geohash on Firestore vs D1)",
            "Payment split model and refund rules",
        ],
        overrides={
            "android_tv": (O, "venue big-screen: today's matches and queue"),
            "wearos": (O, "match timer and score on the wrist (ADR)"),
        },
        tasks={
            "M0": [
                "Map the three old projects' features into one matrix (docs/MERGE.md) with source file paths"
            ],
            "M1": [
                "Pitch search + booking with hold, double-booking race test",
                "Player profile + rating v1",
            ],
            "M2": [
                "Squad balancer",
                "Owner dashboard",
                "FUT card renderer with real stats only",
            ],
        },
    ),
    "sir-business": dict(
        arch="pos-desktop",
        personality="fast, trustworthy, shop-floor tough",
        signature="a cashier screen that completes a sale in three taps with barcode, numpad and hold-to-split built for speed",
        modules=[
            "core-pos: cart, discounts, taxes, receipts (thermal ESC/POS), returns, shifts, cash drawer",
            "catalog: items, variants, units, barcodes, price lists",
            "inventory: stock moves, batches, expiry (pharmacy), reorder alerts",
            "modes: restaurant (tables, kitchen display, modifiers), market (weighing scale, loyalty), pharmacy (batch/expiry, controlled items), library (loans, fines)",
            "sync: offline-first local store with idempotent sync to the cloud, conflict rules per entity",
            "reports: daily Z-report, margins, top sellers, staff performance",
            "portal: owner web dashboard, subscriptions, licence activation (signed webhooks)",
            "compliance: Egyptian e-invoicing/ETA readiness and ZATCA only where the plan names it (verify rules at M0)",
        ],
        entities={
            "Item": "id, sku, barcodes, unit, price, cost, taxClass, mode",
            "Sale": "id, shiftId, lines, payments, status, idempotencyKey",
            "StockMove": "id, itemId, qty, reason, batchId, at",
            "Shift": "id, cashierId, openedAt, closedAt, cashCounted",
            "Licence": "id, tenantId, plan, devices, expiresAt",
        },
        compete=[
            "Foodics",
            "Loyverse",
            "Odoo POS",
            "Square",
            "Local Egyptian POS vendors (research at M0)",
        ],
        adrs=[
            "Electron vs Tauri for the cashier shell",
            "Local DB (SQLite via better-sqlite3 vs Drizzle) and sync protocol",
            "Receipt printer stack and driver strategy",
            "Licence activation without hard-coded keys",
        ],
        tasks={
            "M0": [
                "Merge matrix of the four old products (docs/MERGE.md), feature by feature",
                "Hardware list to test: thermal printer, barcode scanner, cash drawer, scale",
            ],
            "M1": [
                "Restaurant mode vertical slice: table, order, kitchen ticket, pay, receipt, Z-report",
                "Offline sale cycle with sync and no duplicates",
            ],
            "M2": ["Market, pharmacy, library modes on the same core"],
        },
    ),
    "sir-content-creation-studio": dict(
        arch="desktop-engine",
        personality="creative, fast, studio-dark",
        signature="paste a topic and watch a storyboard assemble scene by scene on a timeline you can scrub while it renders",
        modules=[
            "engine: FastAPI service (render queue, ffmpeg, Remotion compositions, TTS, captions, Arabic shaping check)",
            "studio: timeline editor, scene cards, caption styles, brand kits",
            "ideas: trend and keyword research (vidiq/YouTube data MCPs) into scripts",
            "publish: scheduler for ByteVibeHQ accounts via official APIs (never X's website)",
            "cloud: optional render queue (Pro) on a Worker + R2",
            "account: Profile/Settings, licence, usage",
        ],
        entities={
            "Project": "id, title, aspect, scenes, brandKitId",
            "Scene": "id, order, script, media, voice, captions, durationMs",
            "RenderJob": "id, projectId, status, progress, outputRef",
            "ScheduledPost": "id, platform, assetId, at, status",
        },
        compete=[
            "CapCut",
            "Descript",
            "OpusClip",
            "Submagic",
            "DaVinci Resolve (editing depth)",
        ],
        adrs=[
            "Electron shell + Python engine IPC (localhost socket with token)",
            "Remotion licence terms for commercial use (verify-first)",
            "GPU encoding paths (NVENC) and fallbacks",
        ],
        tasks={
            "M0": [
                "Verify Remotion, ffmpeg and model licences for commercial use and record in docs/LICENCES.md"
            ],
            "M1": [
                "One-minute short from a topic: script, voice, captions, render, preview"
            ],
            "M2": ["Brand kits, templates, scheduler dry-run mode"],
        },
    ),
    "sir-controller": dict(
        arch="windows-tool",
        personality="technical, confident, gamer-clean",
        signature="press any button and the on-screen controller lights up that input with live deadzone curves you can drag",
        modules=[
            "input: XInput/DirectInput/HID reading, virtual device layer, per-game profiles",
            "mapping: remaps, macros, deadzone and sensitivity curves, turbo, layers",
            "optimizer: reversible Windows tweaks with restore points, startup and storage review, game mode",
            "profiles: local first, cloud sync (Pro), community-shared profiles with moderation",
            "portal: product site, account, downloads, subscriptions",
        ],
        entities={
            "Profile": "id, game, mappings, curves, layers, updatedAt",
            "Tweak": "id, name, risk, apply, revert, requiresAdmin",
            "Device": "id, vendor, product, capabilities",
        },
        compete=[
            "DS4Windows",
            "reWASD",
            "x360ce",
            "Steam Input",
            "Razer Cortex (optimizer side)",
        ],
        adrs=[
            "Core language: keep .NET core + WinUI 3 vs Tauri after a spike",
            "Virtual device driver: ViGEm licence and distribution rules",
            "Anti-cheat compatibility policy",
        ],
        tasks={
            "M0": [
                "Spike: WinUI 3 vs Tauri on the same mapping screen; decide by ADR with startup and memory numbers",
                "Licence check of every driver/library (ViGEm etc.)",
            ],
            "M1": [
                "Read and display live input from one controller; save and load one profile"
            ],
            "M2": ["Mapping engine with curves, optimizer with restore points"],
        },
    ),
}
