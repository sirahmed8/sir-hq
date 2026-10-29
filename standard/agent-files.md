# B1. Templates

## `AGENTS.md` (fill the `{{…}}` values from `.sir/project.yml`)

````markdown
# AGENTS.md — {{PRODUCT_NAME}} · SIR Standard v{{STANDARD_VERSION}}

{{PRODUCT_NAME}} is part of the SIR product family. Owner: Ahmed Alaa (@sirahmed8).
Every agent and human working here follows this file: Claude Code, Antigravity/Gemini, Codex, Cursor, anyone.
If a request conflicts with this file, say so and propose the premium way. If you're unsure, research and verify; if it's still unclear, choose the safest reversible option, record why, and continue.

## 0. Start every session like this
1. Read `.sir/CHECKPOINT.md` (current state), `.sir/BOARD.md` (tasks), `.sir/project.yml` (facts). Do it again after every compaction or `/clear`: your memory is the files, not the chat.
2. If `D:\Projects\_SIR\ops\locks\` exists (Ahmed's workstation), check it. If another session holds this project, coordinate through `.sir/inbox/` instead of editing.
3. `git status` and the current branch. Never work directly on `main`.
4. Run `pnpm verify` (or the command in section 6) to know the baseline before changing anything.
5. Scan: a full deep scan on the first session, after big merges and weekly; otherwise an incremental scan (git log and diff since the last checkpoint, plus the areas the task touches). Read `.sir/inbox/` for new requests.
6. Write the session goal and its Definition of Done in one short paragraph.

## 1. Project facts
- Type: {{TYPE}} · Tier: {{TIER}} · Status: {{STATUS}} · Version: {{VERSION}}
- Platforms: {{PLATFORM_MATRIX}}
- IDs: {{BUNDLE_IDS}} · Domains: {{DOMAINS}} · Firebase: {{FIREBASE_PROJECTS}}
- Brand: {{BRAND_SEED_COLOR}} · Locales: {{LOCALES}} (default `ar`, `en`, `zh-Hans`, `hi`; Arabic is RTL) · Search indexing: {{INDEXING}}
- Source of truth: `D:\Projects\{{FOLDER}}` (Desktop folders hold shortcuts only)

## 2. Laws (non-negotiable)
1. **Verify, don't assume.** Read the code and docs before changing them. Check current official docs for anything version-sensitive.
2. **Think before coding.** Plan; list edge cases (empty, error, offline, slow, concurrent, RTL, huge data); define how you'll prove it works.
3. **Simple beats clever.** The least code that fully solves the problem. No speculative abstractions, no unrequested config, no premature microservices.
4. **Surgical changes.** Touch only what the task needs. No drive-by reformatting. Refactors go in separate commits, with tests first.
5. **Never break what works.** Tests before refactors; feature flags for risky changes; keep it building at every commit.
6. **Done means proven.** Lint, typecheck, tests and build pass; you ran it and looked at it. Report the evidence.
7. **Nothing fake.** No mock, sample or invented data anywhere a user can see (apps, sites, store listings, screenshots): no fake users, reviews, statistics, logos or prices, no fake loaders. Show empty states instead of sample content. Fixtures live only in tests and the local emulator.
8. **Security by default.** Assume attackers: validate every input at the boundary, authorize every read and write, rate-limit what can be abused, keep secrets out of clients and git. Read module 04 before any auth, data, API or upload work.
9. **One platform, one way.** Use the shared `@sir/*` packages and established patterns. Don't fork them; improve them upstream.
10. **Never lower the bar.** Don't delete or skip tests to go green, lower thresholds, bypass hooks (`--no-verify`), or swap libraries or architecture without an ADR approved by a separate reviewer agent.
11. **Leave it better.** Each change improves the types, tests or docs it touches, within scope.
12. **Honesty.** Report failures, unknowns and anything you couldn't verify. Never present a guess as a fact.
13. **Smart with resources.** Use the cheapest capable model or tool for each job. Reuse verified facts from `D:\Projects\_SIR\knowledge\` when it exists. Don't re-read what you already know. Disk space is tight: no large downloads without checking free space.
14. **Honest, plain words.** No hype or inflated claims ("revolutionary", "best", "#1", "seamless", "unleash", "magic"). Every claim is specific and true.

## 3. Workflow (every task)
Recon → Plan → Implement in small Conventional Commits → Verify → Fresh-eyes review → Document (CHECKPOINT, CHANGELOG, ADR if a decision was made) → Report.
Large or parallel work: follow the Orchestra Protocol (delegation briefs, `.sir/BOARD.md`, inbox, reports).

## 4. Definition of Done (summary; full gates in module 12)
- Code: strict types, 0 lint warnings, no dead code, no unexplained TODOs, errors handled, logs useful and PII-free.
- Tests: domain logic covered; critical journeys have e2e tests; all green.
- UX: all 5 states (first-use, loading skeleton, empty, error with retry, populated incl. huge data); WCAG 2.2 AA; every project locale (RTL for Arabic); token-based light, dark, system and high-contrast themes; keyboard shortcuts; responsive from the smallest phone to large desktop; motion respects reduced-motion.
- Security & privacy: the module 04 checklist passes (inputs validated, access rules tested, rate limits, headers, no secrets, security scans green); consent respected.
- Performance: within the budgets in modules 06, 07 and 09.
- Docs: CHECKPOINT, CHANGELOG (Unreleased), ADRs, README commands still true.
- Reach: every locale complete (no missing keys); for public products, the search and store basics in module 16; automations documented (module 18); the completeness sweep (module 19) run at each milestone.
- Product: AI at the core (the flagship AI feature, the assistant and the free provider chain; module 10); a real changelog generated from releases (never hard-coded), notifications, the owner dashboard, help center, FAQ, support and suggestions, a fair subscription model (AHome: none), the benchmark gaps closed (module 21); smooth at 120 Hz and above; works at every screen size and zoom level.

## 5. Architecture at a glance
- `apps/web` (Next.js) · `apps/desktop` (Electron) · `apps/mobile` (Expo: Android, iOS, iPadOS; TV builds from the same app with `EXPO_TV=1`; the watchOS app and widgets live in `apps/mobile/targets/`) · `apps/wear` (Wear OS)
- `packages/core`: domain types, Zod schemas, business rules. No UI, no I/O.
- `packages/*`: data access, features, UI built on shared `@sir/*` packages.
- `services/functions`: backend (Cloudflare Workers on the free plan, or Cloud Functions once Blaze is funded), the AI gateway, webhooks.
- Dependency direction: UI → application → domain. Never the reverse. Details in module 02 and `docs/ARCHITECTURE.md`.

## 6. Commands
{{COMMANDS}}  <!-- generated from package.json: dev:web, dev:mobile, dev:desktop, verify, test, e2e, build:*, release -->

## 7. Read the module before you touch the area
| When you are… | Read `docs/sir/standard/…` |
|---|---|
| writing any code | 01-engineering |
| changing structure or packages | 02-architecture |
| touching data, Firebase, backend | 03-data-backend |
| touching auth, secrets, personal data, APIs, uploads, or anything attackers could abuse | 04-security-privacy |
| building UI, UX or motion | 05-design-system |
| working on web | 06-web |
| working on Android, iOS, iPad, foldables | 07-mobile |
| working on watch apps | 08-watch |
| working on Windows or macOS | 09-desktop |
| building AI features (every product has them) | 10-ai |
| touching legal, consent, store listings | 11-legal-stores |
| writing tests or CI | 12-quality-gates |
| versioning or releasing | 13-release |
| ending a session or handing off | 14-continuity |
| icons, launchers, folders | 15-launchpad |
| SEO, AI-assistant visibility, store listings | 16-search-discovery |
| planning, reviews, reliability, design docs | 17-engineering-playbook |
| n8n and AI automations | 18-automations |
| reaching a milestone (did we forget anything?) | 19-completeness |
| TV and car apps, widgets, XR, Linux, extensions | 20-platforms-tv-car |
| notifications, owner dashboard, help and support, subscriptions, benchmarking competitors | 21-product-essentials |
| choosing or changing a hosted service, database, file storage, email, analytics, CI, or any free tier | 22-free-stack |

## 8. Boundaries
- Don't ask; decide, log, continue. Allowed after review: merging to `main` once CI is green and a reviewer agent approved; production deploys with staged rollouts and rollback.
- List for Ahmed in `OWNER_ACTIONS.md`, and never wait for it: anything that costs money (there is no budget; free tiers only), identity, 2FA and payment verification, signing legal agreements, and actions a platform's terms reserve for a human. Never permanently delete anything personal.
- Never: commit secrets; bypass security, CAPTCHAs or 2FA; fake reviews or engagement; disable tests or hooks to pass; expose private user data.

## 9. End every session like this
Ask the owner's questions and write the answers down: Did we forget anything? What's still missing compared with the best apps in this category? What should we do next? What would Ahmed think of this, and what else might he need? Then update `.sir/CHECKPOINT.md`, `.sir/BOARD.md`, `CHANGELOG.md` (Unreleased) and `.sir/status.json` → commit → release the lock → report (outcome, evidence, risks, next step).
````

## `CLAUDE.md`

````markdown
@AGENTS.md

## Claude Code notes
- Use the global agent roster (`~/.claude/agents/`) and the Orchestra Protocol in `D:\Projects\_SIR\core\03-team.md` for multi-agent work.
- Manager: Sonnet (high). Builders: Haiku (max), each working from a task spec in `.sir/tasks/` (template in `D:\Projects\_SIR\standard\project-templates.md`). Sonnet reviews every diff.
- Project skills: `.claude/skills/`. Project MCP servers: `.mcp.json`.
- Memory: update `.sir/CHECKPOINT.md` after every finished step, not only at the end. After a compaction, `/clear` or resume, the memory hook prints the checkpoint; re-read the files it lists before continuing.

## When the conversation is compacted
Keep in the summary: the current task and its acceptance criteria, files changed and why, decisions and their reasons, failing commands with their exact errors, what's verified and what isn't, and the exact next step.
````

## `GEMINI.md`

````markdown
# Gemini / Antigravity guardrails — {{PRODUCT_NAME}}

You are continuing a codebase built to the SIR Standard. AGENTS.md is binding; it loads alongside this file.
- Read `.sir/CHECKPOINT.md` and the relevant `docs/sir/standard/` module before editing, and again after any context reset.
- Match existing patterns and shared `@sir/*` packages. Don't introduce new libraries, rewrite architecture or restructure folders without an ADR in `.sir/decisions/` reviewed by a second agent, and never as a side effect of another task.
- Never delete or skip tests, lower CI thresholds, use `--no-verify`, or commit secrets.
- Run `pnpm verify` before claiming anything is done, and show the output.
- If something looks wrong, record it in `.sir/inbox/orchestrator.md` and mention it in your report; don't rewrite it as a side effect.
- End of session: update CHECKPOINT, BOARD, CHANGELOG (Unreleased) and `status.json`.
````

## `.agents/rules/sir-standard.md`

````markdown
---
trigger: model_decision
description: "SIR Standard index. Read the matching module in docs/sir/standard/ before working on code, architecture, data, security, UI, web, mobile, watch, desktop, AI, legal, testing, releases, handoff, launchers, SEO and store listings, engineering practices, automations, milestone checks, TV and car apps, notifications, the owner dashboard, support, subscriptions, AI providers or free services."
---
Modules: 01-engineering, 02-architecture, 03-data-backend, 04-security-privacy, 05-design-system, 06-web, 07-mobile, 08-watch, 09-desktop, 10-ai, 11-legal-stores, 12-quality-gates, 13-release, 14-continuity, 15-launchpad, 16-search-discovery, 17-engineering-playbook, 18-automations, 19-completeness, 20-platforms-tv-car, 21-product-essentials, 22-free-stack (all in docs/sir/standard/).
````
