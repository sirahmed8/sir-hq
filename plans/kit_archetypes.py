"""Archetype data for the readiness kit: layout, team, toolkit, design direction, production, quality, extra tasks.
Skill and MCP names come from what exists in the HQ environment on 2026-10-30; anything else is 'discover and vet' (verify-first)."""

from kit_platforms import (
    WEB_SAAS,
    POS_DESKTOP,
    DESKTOP_ENGINE,
    WINDOWS_TOOL,
    INTERNAL_OPS,
    PRIVATE_LOCAL,
    STATIC_SITE,
    GAME_MOD,
    SELF_HOST,
    LIFE_APP,
    PLATFORM_KIT,
)

WEB_MCP = [
    (
        "cloudflare plugin (docs, execute, search)",
        "Pages/Workers/D1/KV/R2 setup and deploy",
    ),
    ("firebase plugin", "Auth, Firestore rules, project config"),
    (
        "chrome-devtools plugin + built-in browser",
        "login brand check, screenshots, Lighthouse, a11y",
    ),
    ("figma plugin (needs /mcp sign-in)", "design import and tokens, optional"),
    ("firecrawl plugin", "benchmark research and docs lookup"),
    (
        "PostHog `exec`, Black SEO Analyzer",
        "analytics after consent, technical SEO audit",
    ),
]
WEB_SKILLS = [
    "nextjs",
    "react-best-practices",
    "shadcn",
    "modern-web-guidance",
    "frontend-design",
    "emil-motion-impeccable",
    "taste-design-engine",
    "anti-vibecoded-design-system",
    "mobile-ergonomics-polish",
    "vibe-auth-hardening",
    "owasp-vulnerability-shield",
    "zero-trust-security-hardening",
    "legal-compliance-shield",
    "high-conversion-copywriting",
    "database-reliability-transactions",
    "open-seo-auditor",
    "firebase_auth_basics",
    "firebase_firestore",
    "firestore_rules_creation",
    "cloudflare:wrangler",
    "cloudflare:workers-best-practices",
    "cloudflare:web-perf",
]
MOBILE_SKILLS = ["android-cli", "modern-app-engineering", "mobile-ergonomics-polish"]
DESK_MCP = [
    ("computer-use", "drive the installed Windows app for smoke tests (grant per app)"),
    ("Microsoft Learn docs MCP", "Windows, .NET, WinUI, MSIX facts"),
    ("chrome-devtools plugin", "debug the web view of Electron/Tauri"),
    ("firecrawl plugin", "benchmark and docs lookup"),
]
DESK_SKILLS = [
    "modern-app-engineering",
    "pulse-engineering",
    "emil-motion-impeccable",
    "taste-design-engine",
    "anti-vibecoded-design-system",
    "zero-trust-security-hardening",
    "owasp-vulnerability-shield",
    "legal-compliance-shield",
    "ponytail-yagni-optimizer",
]
PY_SKILLS = [
    "managing-python-dependencies",
    "production-engineering-standards",
    "zero-trust-security-hardening",
    "owasp-vulnerability-shield",
    "ponytail-yagni-optimizer",
]

LAYOUT_WEB = "apps/web, apps/api (Workers/Hono), apps/mobile (Expo), packages/core (domain, zod), packages/data (repositories), packages/ui, docs/, scripts/, .sir/"
LAYOUT_DESK = "apps/desktop (Electron or Tauri shell), apps/web (portal), apps/api (Workers), packages/core, packages/data, packages/ui, engine/ (local service if any), docs/, scripts/, .sir/"
LAYOUT_PY = "src/<package>/ (presentation, domain, data, core), tests/, docs/, scripts/, .sir/ (pyproject.toml, uv, ruff, mypy)"
LAYOUT_SITE = "apps/web (static first), apps/api (one small Worker), content/ (JSON/markdown), packages/ui, docs/, scripts/, .sir/"

TEAM_WEB = [
    ("architect", "ADRs, data model, security rules design, task specs", "sonnet high"),
    ("builder", "web and API features from specs", "haiku max"),
    (
        "mobile-engineer",
        "Expo app, widgets, tablet layouts, watch targets",
        "haiku max",
    ),
    ("ui-craftsman", "design tokens, a11y, RTL, screenshots", "haiku max"),
    (
        "ui-motion-director",
        "springs, shared-element transitions, reduced-motion path",
        "haiku max",
    ),
    ("ai-engineer", "AI feature, prompts, evals, quotas", "sonnet high"),
    ("localizer", "ar/en/zh-Hans/hi strings and glossary", "haiku medium"),
    ("qa-breaker", "unit, e2e, adversarial tests", "haiku max"),
    ("security-auditor", "auth, rules, webhooks, secrets review", "sonnet high"),
    (
        "legal-compliance-counsel",
        "privacy/terms/cookies/refunds from real data use",
        "sonnet high",
    ),
    ("seo-specialist", "technical SEO, structured data, ASO", "haiku medium"),
    ("release-manager", "CI, versions, changelog, store metadata", "haiku max"),
    ("reviewer", "fresh-eyes review of every diff", "sonnet high"),
    ("docs-keeper", "checkpoint, board, README, session end", "haiku medium"),
]
TEAM_DESK = [
    ("architect", "ADRs, process and data design", "sonnet high"),
    ("desktop-engineer", "shell, installer, signing, auto-update", "haiku max"),
    ("builder", "engine and API features", "haiku max"),
    ("ui-craftsman", "design system, a11y, screenshots", "haiku max"),
    ("ui-motion-director", "motion and polish", "haiku max"),
    ("ai-engineer", "AI features and evals", "sonnet high"),
    ("localizer", "four locales", "haiku medium"),
    ("qa-breaker", "tests, adversarial cases", "haiku max"),
    ("security-auditor", "licences, secrets, updates, IPC", "sonnet high"),
    ("desktop-release-qa", "installer size, startup, release checks", "haiku max"),
    ("legal-compliance-counsel", "legal pages", "sonnet high"),
    ("release-manager", "CI and releases", "haiku max"),
    ("reviewer", "review every diff", "sonnet high"),
    ("docs-keeper", "docs and checkpoint", "haiku medium"),
]
TEAM_PY = [
    ("architect", "ADRs and design", "sonnet high"),
    ("builder", "implementation from specs", "haiku max"),
    ("qa-breaker", "pytest, adversarial tests", "haiku max"),
    ("security-auditor", "secrets, subprocess, file access review", "sonnet high"),
    ("automation-engineer", "n8n/scheduler flows", "haiku max"),
    ("ai-engineer", "local model use and evals", "sonnet high"),
    ("reviewer", "review every diff", "sonnet high"),
    ("docs-keeper", "docs and checkpoint", "haiku medium"),
]
TEAM_SITE = [
    ("architect", "information architecture, ADRs", "sonnet high"),
    ("builder", "site and Worker", "haiku max"),
    ("ui-craftsman", "design system, a11y, screenshots", "haiku max"),
    ("ui-motion-director", "motion", "haiku max"),
    ("seo-specialist", "SEO, structured data, hreflang", "haiku medium"),
    ("localizer", "four locales", "haiku medium"),
    ("qa-breaker", "e2e, Lighthouse budgets", "haiku max"),
    ("legal-compliance-counsel", "privacy and cookies", "sonnet high"),
    ("reviewer", "review every diff", "sonnet high"),
    ("docs-keeper", "docs and checkpoint", "haiku medium"),
]

DESIGN_WEB = [
    "Own seed colour and Arabic+Latin type pairing (module 05); calm neutral canvas, accent only for primary actions and key numbers.",
    "One signature interaction that people remember (named per product below), built with springs on transform/opacity only.",
    "Shared-element transitions between list and detail; skeletons that match final geometry; optimistic feedback under 100 ms.",
    "RTL is designed first, not mirrored last: logical properties, flipped directional icons, Arabic line heights.",
    "Banned: purple-blue gradients, sparkle AI icons, emoji headings, pill buttons on data inputs, stock filler, hype words, em-dashes in copy.",
]
DESIGN_DESK = [
    "Native feel on Windows 11 (Mica/Acrylic used sparingly, snap layouts, system accent respected) inside the product's own colour language.",
    "Dense but calm: keyboard-first (Ctrl+K palette, shortcut map), command palette, context menus, drag and drop, remembered window state.",
    "Signature interaction per product (below); long tasks show real progress and can be cancelled; nothing blocks the UI thread.",
    "Same 5 states, 4 themes, 4 locales and RTL rules as every SIR product; installer and first run are part of the design.",
]
DESIGN_PY = [
    "Local tools still get a designed surface: a clean terminal UX (rich output, clear exit codes) and, where there is a UI, the SIR design tokens.",
    "Reports and dashboards are readable at a glance: one number that matters first, details on demand.",
]

PROD_WEB = [
    "Hosting: Cloudflare Pages/Workers (free tier), preview deploy per branch, production on main; custom domain later (owner action, never blocking).",
    "Data: Firestore (Spark) + D1/KV/R2 where server-side; env var NAMES documented in `docs/ENV.md`, values only in Cloudflare/GitHub secrets.",
    "Monitoring: Workers logs + Sentry-class free tier decided by ADR; uptime check; error budget in the runbook.",
    "Backups: scheduled Firestore/D1 export to R2 with a restore drill recorded in `.sir/evidence/`.",
    "Releases: Conventional Commits, generated changelog shown in-app (What's new), semantic version in `project.yml`.",
    "Stores: free channels first (web/PWA, GitHub Releases APK, Microsoft Store direct installer, Edge/Firefox add-ons); Google Play/App Store when the reinvestment ladder allows.",
]
PROD_DESK = [
    "Release channels: GitHub Releases (signed where possible), Microsoft Store (MSIX) when the account exists, winget manifest; auto-update with rollback.",
    "Installer budget and startup time recorded each release (desktop-release-qa); crash reports opt-in only.",
    "Server side (portal, licences, sync): Cloudflare Workers + Firestore/D1, same rules as web products; webhooks signed.",
    "Backups of user data are local and exportable; cloud sync is Pro only and encrypted in transit and at rest.",
]
PROD_PY = [
    "Runs locally; scheduled by Windows Task Scheduler or n8n (register only with Ahmed's approval, never by agents).",
    "Secrets in Windows Credential Manager or `.env` outside git; logs rotate; a `doctor` command prints health in one screen.",
    "Backups: the data directory is copied to `D:/Projects/Backups` by the nightly routine; restore steps in `docs/RUNBOOK.md`.",
]
PROD_SITE = [
    "Hosting: Cloudflare Pages (static) + one Worker for forms; preview per branch; custom domain later.",
    "Performance budget: Lighthouse 95+ mobile, LCP under 2.0 s on 4G, CLS 0; images AVIF/WebP with srcset.",
    "Analytics only after consent; uptime check; sitemap and robots; structured data validated.",
]

QUALITY_COMMON = [
    "`pnpm verify` (or `uv run verify` / `pwsh scripts/verify.ps1`) runs typecheck, lint, tests, build, gitleaks; CI runs the same command.",
    "Files under 300 lines; strict typing; zod/pydantic at every boundary; no `any`; no TODO placeholders; no mock data in production paths.",
    "Every screen has the 5 states; four locales with no missing keys; four themes; WCAG 2.2 AA; keyboard map; zoom 80-200%; 320 px to 4K.",
    "Security checklist in PLAN section 7 is green with negative tests; licences audited (no GPL/AGPL in proprietary code).",
    "Evidence for each ticked box in `.sir/evidence/` (command output or screenshot) plus one line in the checkpoint.",
]
QUALITY_WEB = [
    "e2e (Playwright) for the critical journeys on 390 px and 1280 px, LTR and RTL; Lighthouse budgets; Firestore rules tested in the emulator.",
    "Visual regression screenshots for light, dark and high-contrast in every locale.",
]
QUALITY_DESK = [
    "Install, update, uninstall and rollback tested on a clean Windows 11 profile; startup time and installer size recorded.",
    "IPC surface reviewed (no remote content with node access); code-signing plan written even when unsigned.",
]
QUALITY_PY = [
    "pytest with coverage on the domain layer; ruff + mypy clean; property tests for parsers and scoring.",
    "A `doctor` command and a dry-run mode for anything that moves or deletes files.",
]

ARCH = {
    "platform-kit": dict(
        label="Shared TypeScript kit (npm workspace)",
        platforms=PLATFORM_KIT,
        layout="packages/* (@sir/owner-auth, signed-webhook, ai-proxy, billing, legal, ui, tokens, i18n, settings, project-kit), docs/, .sir/",
        team=TEAM_WEB,
        mcp=WEB_MCP,
        skills=WEB_SKILLS,
        design=DESIGN_WEB,
        prod=PROD_WEB[:1]
        + [
            "Published privately (GitHub Packages or workspace links); semver per package; every package has tests and a README with a usage example."
        ],
        quality=QUALITY_COMMON
        + ["Each package ships with negative tests; no package imports a product."],
    ),
    "web-saas": dict(
        label="Web + PWA + mobile product on the SIR Platform",
        platforms=WEB_SAAS,
        layout=LAYOUT_WEB,
        team=TEAM_WEB,
        mcp=WEB_MCP,
        skills=WEB_SKILLS + MOBILE_SKILLS,
        design=DESIGN_WEB,
        prod=PROD_WEB,
        quality=QUALITY_COMMON + QUALITY_WEB,
    ),
    "pos-desktop": dict(
        label="Offline-first desktop POS + web portal",
        platforms=POS_DESKTOP,
        layout=LAYOUT_DESK,
        team=TEAM_DESK,
        mcp=DESK_MCP + WEB_MCP[:2],
        skills=DESK_SKILLS + ["database-reliability-transactions", "nextjs"],
        design=DESIGN_DESK,
        prod=PROD_DESK,
        quality=QUALITY_COMMON
        + QUALITY_DESK
        + [
            "Offline test: a full sale cycle with the network cut, then sync without duplicates (idempotency keys)."
        ],
    ),
    "desktop-engine": dict(
        label="Desktop app with a local engine",
        platforms=DESKTOP_ENGINE,
        layout=LAYOUT_DESK,
        team=TEAM_DESK,
        mcp=DESK_MCP + WEB_MCP[:2],
        skills=DESK_SKILLS + PY_SKILLS,
        design=DESIGN_DESK,
        prod=PROD_DESK,
        quality=QUALITY_COMMON + QUALITY_DESK + QUALITY_PY,
    ),
    "windows-tool": dict(
        label="Windows utility (native or hybrid) + web portal",
        platforms=WINDOWS_TOOL,
        layout=LAYOUT_DESK,
        team=TEAM_DESK,
        mcp=DESK_MCP + WEB_MCP[:2],
        skills=DESK_SKILLS,
        design=DESIGN_DESK,
        prod=PROD_DESK,
        quality=QUALITY_COMMON
        + QUALITY_DESK
        + [
            "Hardware-facing code has an abstraction with fakes for tests; every system change is reversible with a restore point."
        ],
    ),
    "internal-ops": dict(
        label="Internal Windows operations tool",
        platforms=INTERNAL_OPS,
        layout=LAYOUT_PY,
        team=TEAM_PY,
        mcp=[
            ("computer-use", "verify UI pieces"),
            ("scheduled-tasks MCP", "routines (register only with approval)"),
        ],
        skills=PY_SKILLS
        + [
            "pc-storage-guardian",
            "laptop-admin",
            "customization-architect",
            "repomix-token-optimizer",
        ],
        design=DESIGN_PY,
        prod=PROD_PY,
        quality=QUALITY_COMMON + QUALITY_PY,
    ),
    "private-local": dict(
        label="Private local app (never public)",
        platforms=PRIVATE_LOCAL,
        layout=LAYOUT_PY,
        team=TEAM_PY,
        mcp=[
            ("computer-use", "verify UI pieces"),
            ("Google Calendar/Drive/Gmail MCPs", "only where the plan names them"),
        ],
        skills=PY_SKILLS,
        design=DESIGN_PY,
        prod=PROD_PY,
        quality=QUALITY_COMMON
        + QUALITY_PY
        + [
            "Privacy test: nothing leaves the machine except the named channels; AI calls use local models for private text."
        ],
    ),
    "static-site": dict(
        label="Static-first site on Cloudflare",
        platforms=STATIC_SITE,
        layout=LAYOUT_SITE,
        team=TEAM_SITE,
        mcp=WEB_MCP,
        skills=WEB_SKILLS[:9]
        + ["open-seo-auditor", "cloudflare:web-perf", "website-traffic-analytics"],
        design=DESIGN_WEB,
        prod=PROD_SITE,
        quality=QUALITY_COMMON + QUALITY_WEB,
    ),
    "game-mod": dict(
        label="Game launcher/installer + web hub",
        platforms=GAME_MOD,
        layout=LAYOUT_DESK,
        team=TEAM_DESK,
        mcp=DESK_MCP + WEB_MCP[:2],
        skills=DESK_SKILLS + ["binary-reverse-engineer"],
        design=DESIGN_DESK,
        prod=PROD_DESK,
        quality=QUALITY_COMMON
        + QUALITY_DESK
        + [
            "Third-party binaries are fetched from official sources at install time, hash-checked, never redistributed; single-player only."
        ],
    ),
    "selfhost-oss": dict(
        label="Open-source self-hosted distribution",
        platforms=SELF_HOST,
        layout=LAYOUT_WEB + "; legacy/ holds the upstream source (read-only)",
        team=TEAM_WEB,
        mcp=WEB_MCP[2:] + DESK_MCP[:2],
        skills=WEB_SKILLS[:8] + PY_SKILLS + ["legal-compliance-shield"],
        design=DESIGN_WEB,
        prod=PROD_DESK[:2]
        + [
            "Docker image published to GitHub Container Registry; docker compose with pinned digests; upgrade and rollback notes."
        ],
        quality=QUALITY_COMMON
        + [
            "Licence compliance (AGPL-3.0): source offer, notices and attribution tested in CI; no proprietary code linked into AGPL parts."
        ],
    ),
    "life-app": dict(
        label="Local-first Expo app + PWA",
        platforms=LIFE_APP,
        layout=LAYOUT_WEB,
        team=TEAM_WEB,
        mcp=WEB_MCP[:3]
        + [
            (
                "Islamic sources MCPs (Quran, hadith, tafsir, duas, prayer times)",
                "cite real references; never recite from memory",
            ),
            ("Android-MCP", "drive the Android emulator or phone"),
        ],
        skills=WEB_SKILLS + MOBILE_SKILLS,
        design=DESIGN_WEB,
        prod=PROD_WEB,
        quality=QUALITY_COMMON
        + QUALITY_WEB
        + [
            "Religious content is cited from the MCP/source with reference; reviewed text only; prayer-time calculation tested against two sources per city."
        ],
    ),
}
