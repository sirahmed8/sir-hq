B = [
    dict(
        slug="sir-business",
        display="SIR Business",
        folder="SIR Business",
        repo="sir-business",
        firebase="sir-business",
        replaces="SIR Restaurant, SIR Market, SIR Pharmacy, SIR Library",
        wave=2,
        mission="One point-of-sale and operations suite for small Egyptian businesses with four modes: restaurant, supermarket, pharmacy, library/bookstore. Audience: shop owners and their cashiers.",
        platforms="Windows desktop (Electron, offline first) + web portal + Android tablet later; Arabic first",
        money="Free single-device starter; paid monthly plans in EGP (Restaurant 450/750/1950 today; Market 950/2450/4900 today, to be re-priced from real costs); Launching Soon fallback",
        why="- Four copies of one shell with no data layer, seeded mock arrays, hardcoded admin and preset PINs, fake upgrade success and canned AI answers (Pharmacy invents stock; patient-safety risk).\n- Restaurant rules let any signed-in user read/write every branch; kill switch with a hardcoded rescue PIN.\n- Electron build deps missing in three repos; `node_modules` symlinked between projects.",
        port="- Shared: shell, POS, shifts, receipts and ESC/POS, scale driver, FEFO inventory, reports, PIN lock UX, updater, Electron main/preload (sandbox on).\n- Restaurant: KDS, waiter, kiosk, floor plan, delivery hub, ZATCA phase 2. Market: procurement, Customer 360, e-commerce, ETA/ZATCA signers. Pharmacy: expiry radar, controlled-drug log. Library: borrowing + deposits, study desks, members, catalog.",
        screens="Onboarding wizard (linear), Lock screen, POS, Orders/KDS, Inventory, Purchasing, Customers, Reports, Staff, Devices, Settings, Billing, Owner dashboard, Help; mode-specific screens per vertical",
        entities="Tenant, Branch, User/Role, Product, StockLot, Sale, Shift, Supplier, PurchaseOrder, Customer, Table/Order (restaurant), Prescription/Patient (pharmacy), Loan/Member (library)",
        ai="Flagship: demand and expiry forecasting with plain-language suggestions from real sales only. Assistant: grounded help. Pharmacy: no clinical advice; interactions only from a cited dataset with a pharmacist-review disclaimer, otherwise the feature is off.",
        security_extra="- Per-tenant claims in rules; tenant-isolation tests with two tenants.\n- PINs hashed (argon2/scrypt); no preset users; license check server-side; kill switch removed or disclosed in the EULA.\n- Patient data: consent, encryption at rest, deletion flow.",
        m1=[
            "Core with SQLite (encrypted) + sync to Firestore; Restaurant POS sale end to end with receipt print preview."
        ],
        m2=[
            "Restaurant mode complete (KDS, floor plan, delivery, ZATCA behind a flag until keys), then Market, Pharmacy, Library modes on the same core.",
            "Parity checklist per mode from the four inventories.",
        ],
        m4=["Forecast + help assistant; eval sets; no invented numbers."],
        m6=[
            "Signed installer only when a certificate is affordable; until then SmartScreen note in install guide; migration importer from old exports; archive the four old repos."
        ],
        risks="- Hardware drivers (printers, scales) need real devices to test.\n- ZATCA/ETA certificates are owner/government steps.",
    ),
    dict(
        slug="sir-content-creation-studio",
        display="SIR Content Creation Studio",
        folder="SIR Content Creation Studio",
        repo="sir-content-creation-studio",
        firebase="sir-content-studio",
        replaces="SIR Content Creation Studio v1 (with the SIR Media idea and ByteVibeHQ publishing)",
        wave=3,
        mission="Offline-first AI video studio for Shorts/Reels/TikTok and long form, plus scheduled publishing for ByteVibeHQ's accounts. Audience: Ahmed first, then creators.",
        platforms="Windows desktop (Electron) + local engine (Python FastAPI, Remotion) + web dashboard",
        money="Free local editing; Pro for cloud render queue and scheduler (EGP); Launching Soon fallback",
        why="- No server-side token check (owner gating by env in 6 files), personal state files tracked in git (profile, uid, pro flag, studio.db), unsigned stale installer, Python 3.10/3.11/3.13 mismatch, CI failing.\n- No Launching Soon fallback; payment SDK names scattered in 5 files.",
        port="- Engine: transcript, captions, reframing, b-roll, sound effects pipeline, Remotion templates, 120 test files (keep the good ones).\n- UI flows for project, timeline, export.",
        screens="Projects, Import, Transcript editor, Timeline, Captions, Templates, Export queue, Scheduler (ByteVibeHQ calendar), Settings, Owner dashboard, Help",
        entities="Project, Asset, Transcript, Caption, Template, RenderJob, ScheduledPost, Account (official API tokens stored server-side)",
        ai="Flagship: AI clip finder + caption writer. Providers via ai-proxy; local Whisper/Ollama for private media.",
        security_extra="- Personal state never in git; Python version pinned once; installer signed when possible; social tokens only server-side; no X website scripting (official APIs/schedulers only).",
        m1=[
            "Local engine health endpoint, project create/open, transcript from a sample clip, tests for each."
        ],
        m2=[
            "Captions, reframing, export; scheduler for Instagram/TikTok/Facebook/Reddit via official APIs; calendar with 24-hour veto window."
        ],
        m4=[
            "Clip finder and caption writer with eval clips; hashtag and title helper."
        ],
        m6=["Rebuilt installer, update channel, retire v1 folder."],
        risks="- Platform API approvals take time (owner accounts); keep drafts-only mode.\n- GPU/disk limits on Ahmed's laptop: render budgets and cleanup.",
    ),
]
