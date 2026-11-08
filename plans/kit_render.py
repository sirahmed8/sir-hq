"""Renderers for the per-project readiness kit. Each function returns the text of one file."""

from kit_platforms import PLATFORM_NAMES, BUILD_TOOL

LOCALES = "[ar, en, zh-Hans, hi]"


def bullets(items):
    return "\n".join("- " + x for x in items)


def project_yml(p, a, b, brand, matrix):
    plats = "\n".join(
        f"  {k}: {matrix[k][0]}   # {matrix[k][1]}" for k, _ in PLATFORM_NAMES
    )
    private = b["arch"] == "private-local"
    local = b["arch"] in ("private-local", "internal-ops")
    return f"""id: {p["slug"]}
name: {p["display"]}
type: {b["arch"]}
archetype: {a["label"]}
tier: {"internal" if b["arch"] in ("internal-ops", "platform-kit") else "product"}
wave: {p["wave"]}
status: planned
version: 0.0.0
owner: Ahmed Alaa (@sirahmed8)
standard_version: 1.0.0
platforms:
{plats}
ids:
  bundle_prefix: app.sir
  app_id: app.sir.{p["slug"].replace("sir-", "")}
  github: sirahmed8/{p["repo"]}   # private
  firebase: {"none" if local else p["firebase"]}   # {"local tool: no cloud login" if local else "new project per product"}
  cloudflare: {"none" if local else p["repo"]}
brand:
  seed_color: "{brand["color"]}"
  monogram: {brand["mono"]}
  personality: {b["personality"]}
  signature_interaction: {b["signature"]}
locales: {LOCALES}
indexing: {"false" if private else "true"}
launch_state: pre-launch
owner_dashboard: {"false" if private else "true"}
subscriptions: {"none" if p["money"].startswith("none") else "freemium"}
repo_visibility: private
pull_requests: never   # Ahmed 2026-10-30: commit and push straight to main
"""


def tasks_md(p, tasks):
    out = [
        f"# TASKS: {p['display']}",
        "",
        "Generated from PLAN section 8 plus the kit tasks. Work the first unchecked task whose dependencies are done. Tick with evidence in `.sir/evidence/`.",
        "",
    ]
    for ms, items in tasks:
        out.append(f"## {ms}")
        for t in items:
            dep = f" | depends: {t['dep']}" if t["dep"] else ""
            out.append(
                f"- [{'x' if t['done'] else ' '}] {t['id']} | owner: {t['owner']} | {t['text']}{dep}"
            )
        out.append("")
    return "\n".join(out)


def board_md(p, tasks):
    flat = [t for _, items in tasks for t in items]
    todo = [t for t in flat if not t["done"]]
    ready, backlog = todo[:3], todo[3:]
    line = lambda t: f"- {t['id']} | owner: {t['owner']} | {t['text'][:110]}"
    return (
        f"# BOARD: {p['display']}\n\nOne line per task; claim by writing your agent name in `owner`, release when done. Full list in TASKS.md.\n\n## Ready\n"
        + "\n".join(line(t) for t in ready)
        + "\n\n## Doing\n\n## Review\n\n## Backlog\n"
        + "\n".join(line(t) for t in backlog[:40])
        + f"\n(+{max(len(backlog) - 40, 0)} more in TASKS.md)\n\n## Done\n"
        + "\n".join(line(t) for t in flat if t["done"])
        + "\n"
    )


def team_md(p, a):
    rows = "\n".join(f"| `{n}` | {own} | {m} |" for n, own, m in a["team"])
    return f"""# TEAM: {p["display"]}

The project chat is the **Project Manager** (`.claude/agents/{p["slug"]}-pm.md` describes the role). It plans, writes task specs, reviews, and spawns the specialists below. Subagents live in `%USERPROFILE%\\.claude\\agents`; each gets a delegation brief (`_SIR/core/03-team.md`).

| Agent | Owns in this project | Model/effort |
|---|---|---|
{rows}

## Model and effort by task level (full table: `D:/Projects/_SIR/plans/MODEL_ROUTING.md`)
Level 0 search, logs, inventory, simple edits: haiku, low. Level 1 implement from a written spec, tests, UI, translations, app chores: haiku, high (max for big modules). Level 2 design, specs, reviews, hard debugging, refactors: sonnet, high. Level 3 auth, security, payments, migrations, legal: sonnet plus a second sonnet reviewer, high (xhigh for threat models). Level 4 stuck twice or expensive to undo: opus, high or xhigh, with the reason logged. Always spawn with `model` and `effort` set; send independent tasks together; at most 6 agents at once.

## Rules for this project
- Spawn only for work that is independent, big, or needs fresh eyes: at most 6 agents at once, 2 heavy builds or emulators at once.
- Disjoint file ownership per agent; each builder works in its own git worktree and branch, then the PM merges to `main` (no pull requests).
- Anything touching auth, payments, data migration or security rules is done by a Sonnet-level agent and reviewed by `security-auditor`.
- The author never grades its own work: `reviewer` approves every significant diff; `qa-breaker` writes the adversarial tests.
- Results come back as <=250 words plus a report in `.sir/reports/`; decisions go to `.sir/decisions/`.

## Task spec template
Use `_SIR/standard/project-templates.md` (T-NNN): why, read first, exact files, edge cases, acceptance criteria, tests, must-pass commands, don't-touch list, return format, budget.
"""


def toolkit_md(p, a):
    mcp = "\n".join(f"| {n} | {u} |" for n, u in a["mcp"])
    return f"""# TOOLKIT: {p["display"]}

## Available now in this environment (verified 2026-10-30)
| MCP / connector | Use here |
|---|---|
{mcp}

## Skills to load before the matching work
{bullets("`" + s + "`" for s in a["skills"])}

## Logins already in place (checked 2026-10-30, names only)
- GitHub CLI: signed in as sirahmed8 (repos, releases). Firebase CLI: signed in (project create, rules, deploy). Cloudflare MCP: signed in (Pages/Workers/D1/KV/R2 via `execute`).
- Wrangler CLI: signed in (OAuth, account a7medorabe7@gmail.com, 2026-10-30); `wrangler whoami` shows it. If the token expires, run `wrangler login --browser=false`, open the printed link in Chrome, continue with Google and Authorize.
- Not available without Ahmed: domains, store developer accounts, payment gateway keys (Paymob/Fawry/Stripe). The kit's fallback modes cover these.

## Discover and install more (verify-first)
1. Search: `mcp__mcp-registry__search_mcp_registry`, the `skills-discovery-engine` skill, `npx skills find`.
2. Vet before enabling: publisher, licence, requested permissions, last update; prefer official servers. Never paste secrets into a new tool.
3. Record every addition in `D:/Projects/_SIR/ops/TOOLS.md` (name, version, why, how to remove). System and security settings stay off-limits.
4. Free tier or free tool only (no budget). Check data terms: private text stays local.

## CLIs this project will need (install at M0 if missing)
{bullets(cli_list(a))}
"""


def cli_list(a):
    base = [
        "git, gh (logged in as sirahmed8), gitleaks (in `_SIR/ops/inventory/gitleaks`)"
    ]
    if a["layout"].startswith("src/"):
        return base + ["uv (Python), ruff, mypy, pytest"]
    return (
        base
        + [
            "node + pnpm, wrangler (Cloudflare), firebase-tools",
            "Playwright (Chromium installed), Lighthouse via chrome-devtools MCP",
        ]
        + (
            ["JDK 17 + Android SDK at `D:/Projects/Android/Sdk`, Maestro, adb"]
            if "mobile" in a["layout"]
            else []
        )
        + (
            ["electron-builder or Tauri toolchain (Rust) per ADR"]
            if "desktop" in a["layout"]
            else []
        )
    )


def design_md(p, a, b, brand):
    return f"""# DESIGN: {p["display"]}

Seed colour `{brand["color"]}`, monogram `{brand["mono"]}`, personality: **{b["personality"]}**.
Signature interaction: **{b["signature"]}**.

## Direction
{bullets(a["design"])}

## Must be true on every screen
- Tokens only (`@sir/tokens`): no raw hex in components; light, dark, system and high-contrast; no flash of the wrong theme.
- Motion: 100-150 ms micro, 200-300 ms standard, 300-500 ms large; springs for direct manipulation (stiffness 300-400, damping 28-30); animate transform and opacity only; reduced-motion path.
- Type: a deliberate pairing plus an Arabic screen face (IBM Plex Sans Arabic, Cairo or Tajawal), Noto fallbacks for zh-Hans and Devanagari; `tabular-nums` on numbers; `text-wrap: balance` on headings.
- The shared Profile, Settings, Onboarding and Consent screens come from `@sir/settings`; only tokens differ.
- Copy: plain and specific; Egyptian Arabic for friendly consumer text, MSA for legal; no hype words, no em-dashes.

## Deliverables in M0
1. `docs/DESIGN.md` brief with three explored directions and the chosen one (screenshots).
2. Token file from the seed; type scale; icon set rules; the signature interaction prototype running at 120 Hz.
3. Screenshots of the key screens at 390 px and 1280 px, LTR and RTL, light and dark.
"""


def architecture_md(p, a, b):
    ents = "\n".join(f"| {k} | {v} |" for k, v in b["entities"].items())
    return f"""# ARCHITECTURE: {p["display"]}

Archetype: {a["label"]}. Layout: `{a["layout"]}`.
Four layers, dependencies inward only: presentation, domain (no I/O), data, core. Standard modules 01-03 apply.

## Modules (build in this order)
{bullets(b["modules"])}

## Core entities (first draft, refine in M0 with zod schemas in `packages/core`)
| Entity | Fields |
|---|---|
{ents}

## Decisions to record first (ADRs in `.sir/decisions/`)
{bullets(b["adrs"])}

## Boundaries
- Server verifies every identity and role; clients never decide privileges. Secrets only in Cloudflare/GitHub secrets (names in `docs/ENV.md`).
- All AI calls go through the SIR Platform `ai-proxy` (or local models for private apps) with quota and refusal tests.
- Every external webhook is HMAC-signed with the timestamp inside the payload; idempotent handlers.
"""


def production_md(p, a, matrix):
    local = a["layout"].startswith("src/")
    return f"""# PRODUCTION: {p["display"]}

Target: hosted and installable, not a demo. Free tiers only (module 22). Owner-only steps (domains, store accounts, gateway keys) go to `_SIR/ops/OWNER_ACTIONS.md` and never block work.

## Plan
{bullets(a["prod"])}

## Names
GitHub `sirahmed8/{p["repo"]}` (private) | Firebase {"none (local tool)" if local else "`" + p["firebase"] + "`"} | Cloudflare {"none (local tool)" if local else "`" + p["repo"] + "`"} | app id `app.sir.{p["slug"].replace("sir-", "")}`

## Production-ready checklist (all true before the first public announcement)
- [ ] CI green on `main`; `pnpm verify` (or the project's verify command) passes from a clean clone.
- [ ] Secrets only in secret stores; gitleaks clean; env var names documented; `.env.example` complete.
- [ ] Monitoring and an uptime check; a runbook (`docs/RUNBOOK.md`) with rollback steps tested once.
- [ ] Backup and restore drill recorded in `.sir/evidence/`.
- [ ] Legal pages match what the product collects; consent before analytics; account and data deletion works.
- [ ] Billing shows "Subscriptions Launching Soon" until gateway keys exist, then activates without UI changes.
- [ ] Store listings drafted in 4 languages with real screenshots; changelog generated from commits.
- [ ] Owner dashboard shows real numbers only.
"""


def platforms_md(p, matrix):
    rows = "\n".join(
        f"| {n} | {matrix[k][0]} | {matrix[k][1]} | {BUILD_TOOL[k]} |"
        for k, n in PLATFORM_NAMES
    )
    return f"""# PLATFORMS: {p["display"]}

Widest legitimate coverage from one codebase (module 20). Changing a state needs an ADR with the reason.

| Platform | State | Reason | Build and test |
|---|---|---|---|
{rows}

Distribution order: web/PWA, GitHub Releases, Microsoft Store direct installer, F-Droid-style APK, Edge/Firefox add-ons; Google Play and App Store when the reinvestment ladder allows.
"""


def quality_md(p, a):
    return f"""# QUALITY (Definition of Done): {p["display"]}

{bullets(a["quality"])}

Benchmarks to beat at M5: Lighthouse 95+ (web), cold start under 2 s (desktop), accessible name on every control, 0 console errors, 0 dead buttons, 0 horizontal scroll from 320 px.
"""


def benchmark_md(p, b):
    return f"""# BENCHMARK: {p["display"]}

Study these at M0 (research targets, verify every feature claim from the product itself before writing it down):
{bullets(b["compete"])}

Write `docs/BENCHMARK.md` with a feature matrix, what each does best, gaps we can own, and the Egypt/Arabic angle (price sensitivity, payment habits, connectivity). Use the firecrawl MCP and the built-in browser for screenshots. Do not copy their assets or text.
"""
