A = [
    dict(
        slug="sir-education-hub",
        display="SIR Education Hub",
        folder="SIR Education Hub",
        repo="sir-education-hub",
        firebase="sir-education-hub",
        replaces="Obour Academic Hub",
        wave=1,
        mission="A study platform for Obour Higher Institutes computer science students: notes, past exams, quizzes, Q&A, study planner and an AI tutor that explains and quizzes but never does graded work. Audience: Ahmed's classmates first, then other Egyptian institutes.",
        platforms="Web + PWA (Cloudflare), later Android/iOS via Expo",
        money="Free tier covers notes, exams and 5 AI questions a day; Pro in EGP for unlimited AI, offline packs and exam simulator (Launching Soon fallback until Paymob keys exist)",
        why="- Old app is the closest to shippable (CI, 47 tests, httpOnly session) but has `allow read: if true` on 5 Firestore collections, CSP unsafe-inline/eval, 24+ files over 530 lines and analytics before consent.\n- It ships `solve_assignment` and `solve_quiz` modes plus fabricated fallback solutions: graded work, removed in the rebuild.\n- Firebase ids `obourinstitutes1` show on login today.",
        port="- Content model and subjects/exams/sections data (export from Firestore, dry-run import with counts).\n- Rate-limit design (Upstash) as Workers KV limiter; CI backup workflow idea (daily Firestore export).\n- Pages: main, subject, exams, quiz, qa, todo, market, alumni, pricing, admin.",
        screens="Landing, Sign in, Home (today plan), Subject, Lecture notes viewer, Exams, Quiz runner, Q&A, Study planner, AI tutor, Pricing, Profile, Settings, Admin/Owner dashboard, Help center, Legal",
        entities="User, Subject, Lecture, Note, Exam, Question, QuizAttempt, Thread, Reply, StudyTask, Subscription, AiUsage",
        ai="Flagship: AI tutor that explains a lecture, makes practice questions and gives hints with sources from the uploaded notes. Hard rule: no full solutions to graded assignments or live quizzes; refuses and offers hints instead. Assistant: grounded support bot. Free provider chain via the shared kit.",
        security_extra="- Firestore read rules per collection (signed-in, published only); admin only by custom claim.\n- Analytics only after consent.",
        m1=[
            "Sign in with Google (brand check), Subject list, Lecture notes viewer, Quiz runner with real persisted attempts.",
            "Cloudflare deploy at `sir-education-hub.pages.dev` with preview per branch.",
        ],
        m2=[
            "Import subjects/exams/notes with a dry run and record counts matching the old DB.",
            "Q&A, study planner, alumni and market pages; admin dashboard with real counts only (no simulated data).",
            "Pricing page with EGP plans and the Launching Soon fallback.",
        ],
        m4=[
            "AI tutor with source citations, hint ladder (hint 1/2/3 then explanation), quota badge '3 / 5 free questions today'; eval set proving it refuses to write a submission."
        ],
        m6=[
            "Redirect old `obourinstitutes1.web.app` to the new domain after parity; export old data once more; move `Obour Academic Hub` to `old projects`.",
            "Announce to classmates only when real content exists.",
        ],
        risks="- Content copyright: only publish notes Ahmed or classmates own; no copied course PDFs.\n- Paymob needs a business account (owner action); fallback covers the gap.",
    ),
    dict(
        slug="sir-hagoozat",
        display="SIR Hagoozat",
        folder="SIR Hagoozat",
        repo="sir-hagoozat",
        firebase="sir-hagoozat",
        replaces="Hagoozat Elite (Merged sites), 11Players, EGFootball5",
        wave=2,
        mission="Five-a-side football in Egypt: book a pitch, split the cost, balance squads, rate players, run matches and communities. Audience: players, captains and pitch owners.",
        platforms="Web + PWA (Cloudflare), Android/iOS (Expo), owner dashboard web",
        money="Free for players; Pro 59 EGP/month (priority booking, stats, FUT cards, no ads); pitch owners pay a monthly fee; Launching Soon fallback until Paymob/Fawry keys",
        why="- Three apps with overlapping code; the merge in `Hagoozat Elite` has 29 pages vs 55 and 36 in the originals.\n- Critical `dev_signature` payment bypass (stopgap PR merged separately), client-side owner gate, 62 files over 300 lines in 11Players, API routes dead on static hosting in EGFootball5.\n- Fake players generator in 11Players admin, placeholder Firebase config.",
        port="- From EGFootball5: 15-minute slot lock, deposit receipt upload + verification queue, Hagaz lobbies, jersey designer, owner dashboards, achievements/XP, notifications, support tickets, Cloud Functions logic.\n- From 11Players: AI layer, captain draft room, communities, global ranking, owner analytics, pro pass.\n- From Hagoozat Elite: pitches, players, tactics, split-bill, VAR voting, data deletion, unsubscribe.",
        screens="Landing, Sign in, Onboarding, Home, Find pitch, Pitch page, Booking wizard (linear stepper), Deposit/payment, My bookings, Match lobby, Squad balancer, Draft room, Live match, Player card, Rankings, Communities + chat, Notifications, Pro pass, Owner/pitch dashboard, Support, Settings, Legal",
        entities="User, PlayerCard, Pitch, Slot, Booking, Deposit, Match, Squad, Community, Message, Rating, Notification, Subscription, SupportTicket",
        ai="Flagship: squad balancer and position coach (explains what the player must do in each situation). Assistant: booking help and rules Q&A grounded in the app docs. Server proxy only.",
        security_extra="- Slot booking and deposits are transactions with idempotency keys; double-booking test with parallel requests.\n- Receipt images validated and stored privately.",
        m1=[
            "Pitch list + pitch page from real data, booking wizard with slot lock and transaction, Google sign-in brand check."
        ],
        m2=[
            "Deposit upload + verification queue, matches and lobbies, squad balancer, player cards and ratings.",
            "Communities + chat, notifications, achievements, owner dashboard with real revenue/booking counts.",
            "Feature-parity checklist ticked against `ops/inventory/Merged-sites.md` route lists.",
        ],
        m4=[
            "Squad balancer explanation, position coach, support assistant; eval sets in Arabic and English."
        ],
        m6=[
            "Data import from the three Firestore projects with dry run and counts; 301 redirects from `an-11-players.web.app`, `egfootball5.web.app`, `hagoozat-elite.web.app`; move old folders (already in `old projects`) to archive repos."
        ],
        risks="- Three user bases with duplicate accounts: merge by verified email, never by display name.\n- Real payments need a gateway account (owner); fallback until then.",
    ),
]
