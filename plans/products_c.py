C = [
    dict(
        slug="sir-controller",
        display="SIR Controller",
        folder="SIR Controller",
        repo="sir-controller",
        firebase="sir-controller",
        replaces="SIR Controller v1 + SIR Optimizer (PulseTools)",
        wave=3,
        mission="One Windows app and website for game-controller mapping and PC optimization. Audience: PC gamers in Egypt and the Gulf.",
        platforms="Windows desktop (.NET/WPF existing core; rebuild UI on WinUI 3 or Tauri after a spike) + web portal on Cloudflare",
        money="Free controller mapping; Pro in EGP for profiles sync and the optimizer suite; Launching Soon fallback",
        why="- Controller: unsigned webhook (stopgap merged), client-side owner gate with hardcoded email, LGPL-3.0 text against a proprietary EULA, about 20 binaries in git, download button pointing at a private repo.\n- Optimizer: client could grant itself OP mode, AI keys in the bundle (stopgap merged), simulated owner transactions.\n- Both solve the same job; Laptop manager shares hardware code.",
        port="- Controller: 298 MSTest cases (keep), mapping engine, installer. Optimizer: tweak catalog (only tweaks that are safe and reversible), PulseTools UI ideas.\n- Extract hardware helpers shared with Laptop manager once.",
        screens="Dashboard, Controllers, Profile editor, Test pad, Optimizer scan + reversible tweaks with restore points, Downloads, Pricing, Account, Owner dashboard, Help",
        entities="Profile, Mapping, Device, Tweak, TweakRun, RestorePoint, Subscription, DownloadRelease",
        ai="Flagship: explains each tweak and its risk in plain Arabic/English before applying; assistant grounded in docs.",
        security_extra="- Every tweak reversible with a recorded restore point; installer and downloads served from public release repo with checksums; licence text matches the real licence.",
        m1=[
            "Profile load/save + test pad on the existing engine with tests; web portal sign-in brand check."
        ],
        m2=[
            "Optimizer tweaks ported with undo; installer; downloads page pointing at real releases."
        ],
        m4=[
            "Tweak explainer and risk labels from a cited catalog; no performance claims without benchmark output."
        ],
        m6=[
            "Publish release with checksums; archive SIR Optimizer repo; retire both v1 folders."
        ],
        risks="- Licence audit of the mapping engine (LGPL parts) before selling.\n- Driver-level tweaks are risky: ship read-only scan first.",
    ),
    dict(
        slug="sir-ai",
        display="SIR AI",
        folder="SIR AI",
        repo="sir-ai",
        firebase="sir-ai-assistant",
        replaces="SIR AI v1",
        wave=3,
        mission="A voice and vision personal assistant that runs on Ahmed's PC with local models first, and the home of the AI gateway concept that SIR Platform's ai-proxy extracts. Audience: Ahmed first, then power users.",
        platforms="Windows desktop + local web UI; Python core",
        money="Free local use; Pro for cloud models and sync (EGP); Launching Soon fallback",
        why="- Session tokens in localStorage, client-trusted owner paths (stopgap merged), hard-coded OwnerManager identities, a mock dev token bypass, privacy page claiming SOC 2/ISO, a 73 MB model blob tracked in git, a literal Firebase key in several JS files.",
        port="- Core agents, voice pipeline, telegram bridge ideas, 259 tests (keep).",
        screens="Chat, Voice mode, Camera/vision, Tasks, Memory (what it remembers, with delete), Settings/providers, Owner dashboard, Help",
        entities="Conversation, Message, Memory, Tool, Provider, Quota, User",
        ai="This product is the AI: provider chain with local-first routing; private data never goes to outside providers.",
        security_extra="- Cookie sessions only; owner by verified claims; mock tokens removed from production; model blobs out of git (download script with checksum).",
        m1=[
            "Local chat with Ollama, provider chain with failover, memory with delete, tests."
        ],
        m2=[
            "Voice, vision, tool plugins; owner dashboard with real token/cost numbers."
        ],
        m4=["Eval set (Arabic/English) for routing, refusal and tool-use accuracy."],
        m6=[
            "Installer, update channel, retire v1; remove the leaked key literal from history by rewrite after rotation."
        ],
        risks="- Hardware limits (RTX 4050, 24 GB RAM): small models locally, cloud only for non-private text.",
    ),
    dict(
        slug="sir-laptop-manager",
        display="SIR Laptop Manager",
        folder="SIR Laptop Manager",
        repo="sir-laptop-manager",
        firebase="sir-laptop-manager",
        replaces="Laptop manager + antigravity-agent-suite",
        wave=4,
        mission="Ahmed's Personal OS: PC care, cleanup with quarantine, routines, the one canonical agent configuration (agents, skills, rules) synced to every AI tool, local RAG and automations. Internal tool, not sold.",
        platforms="Windows (PowerShell + Python + small desktop UI); private repo",
        money="none (internal)",
        why="- A Telegram bot token is hard-coded in 5 tracked files; cleaners delete without quarantine; an academic automation script conflicts with the graded-work rule; skills in antigravity-agent-suite (97) are synced nowhere and mix licences.",
        port="- agent-config (18 agents, rules, sync script), local-ai RAG, PC cleaner logic, storage watchdog, the 97 skills after a licence audit.",
        screens="Dashboard (disk, startup, health), Cleanup (dry run -> quarantine), Routines, Agent config sync, Local AI (RAG), Settings",
        entities="CleanupPlan, QuarantineItem, Routine, AgentProfile, Skill, SyncRun",
        ai="Local models only for private text; routine briefs; skill discovery.",
        security_extra="- Secrets only in Credential Manager/env; deletes always quarantine first; sync script never deletes; no graded-work automation.",
        m1=["Dry-run cleanup report + quarantine with manifest and restore, tests."],
        m2=[
            "Agent config sync tested on a temp workspace; skills imported after licence audit; routines registered."
        ],
        m4=["RAG over notes with Arabic + English evals."],
        m6=["Retire both v1 folders; archive suite repo."],
        risks="- Global config edits are blocked by the safety classifier: project-scope parity only.",
    ),
]
