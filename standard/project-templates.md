# B3. Project templates

## `.sir/project.yml`

```yaml
id: sir-health              # permanent; kebab-case
name: SIR Health
type: consumer-app          # consumer-app | business-app | utility | profile | tooling | game-mod | private
tier: flagship              # flagship | core | maintenance | concept
wave: 1
status: planned             # planned | building | beta | store-ready | live | paused
version: 1.0.0-alpha.0
owner: Ahmed Alaa (@sirahmed8)
standard_version: 1.0.0
platforms:                  # each: required | optional | skip (+ adr: when skipped)
  web: required
  windows: required
  macos: required
  linux: required
  android: required
  ios: required
  ipados: required
  wearos: required
  watchos: required
  android_tv: required      # yoga and meditation sessions on TV
  tvos: required
  android_auto: required    # Car App Library category: media (audio meditations)
  carplay: required         # audio category; needs Apple's CarPlay entitlement
  widgets: required         # home and lock screen, Live Activities, Android widgets
  xr_compat: required       # iPad on Vision Pro, large-screen Android on Android XR
  browser_extension: skip   # adr: ADR-007 (no browser use case)
ids:
  bundle_prefix: TBD       # permanent once published; the agent decides by ADR, Ahmed can override before the first store upload
  android_package: TBD
  ios_bundle_id: TBD
brand:
  seed_color: "#0F766E"
  personality: calm, encouraging, precise
locales: [ar, en, zh-Hans, hi]   # Arabic + English + the two most-spoken others (Ethnologue 2026); change per market via ADR
indexing: true                   # AHome and workspaces: false
automations: automations/n8n/
launch_state: pre-launch         # pre-launch | live (live = real users: staged rollouts, production care)
merged_from: []                  # e.g. [11Players, EGFootball5]; see MERGE.md
owner_dashboard: true
subscriptions: freemium          # module 21; AHome: none (no subscriptions, ads or paywalls)
notifications: [push, web, desktop, email, in_app]
domains: [TBD]
firebase: { dev: sir-health-dev, prod: sir-health-prod }
ai:                              # module 10: AI is at the core of every product
  mode: cloud                    # AHome: local
  flagship: meal-photo-calories
  features: [meal-photo-calories, coach, assistant, smart-search]
  chain: [on-device, gemini-free, groq, cerebras, workers-ai, openrouter-free]   # default order; each capability's order lives in the gateway config
stack: { hosting: cloudflare, server: workers, data: [firestore, d1], files: r2, media: cloudinary }   # module 22
distribution: [web, microsoft-store, github-releases, appgallery, galaxy-store, google-play-when-funded, app-store-when-funded]
repo: github.com/<org>/sir-health
```

## `.sir/CHECKPOINT.md`

```markdown
# CHECKPOINT — <Product> — updated <YYYY-MM-DD HH:mm> by <agent>
## Goal (current phase)
## Now (the step in progress, exactly where it stands)
## Next step (exact command, file or task ID), then the 2 after it
## Done (evidence: commit, command output, screenshot paths)
## In progress (who · branch · since)
## Decisions this phase (one line each, with ADR links)
## Open promises (started or promised, not finished)
## Owner actions listed (never blocking)
## Last green: `pnpm verify` at <commit> — <date>
## Re-read after a reset (the files that matter right now)
## Notes for the next agent
```

Update it after every finished step and keep it under about 100 lines: move finished items to `CHANGELOG.md` or `.sir/reports/` each week. The memory hook prints it after every compaction, so its first lines matter most.

## `docs/PRODUCT.md` (new products: be exhaustive)

1. One-line pitch and the problem, in the user's words.
2. Users and personas (Egypt first, then the region); jobs-to-be-done.
3. Market and benchmark: competitors (local and global), why we win, the Egypt angle (price sensitivity, Arabic-first, payment habits, connectivity), and the feature matrix and gaps from `docs/BENCHMARK.md` (module 21).
4. Features: MVP (must ship), v1.x, later. Each with a user story and acceptance criteria.
5. Screens and flows for each platform, including the shared Profile/Settings/Onboarding/Consent.
6. Data model draft and security rules outline; sensitive data categories.
7. AI at the core (module 10): the flagship AI feature, the assistant and its actions, each feature's data class and provider chain, the on-device path, evaluation sets, guardrails.
8. Monetization: free / premium / B2B pricing in EGP; in-app purchase vs payment gateway; unit economics.
9. Platform matrix with reasons for any skips; watch use cases.
10. Legal and policy risks (health, religion, location, biometrics, minors, payments).
11. Success metrics (activation, retention D1/D7/D30, revenue) and analytics events.
12. Launch plan: testers, store assets, content plan, first 100 users.
13. Support: help-center topics, FAQ, contact channels, suggestions board, status page (module 21).
14. Open questions, each with the decision taken for now and why (Ahmed can override through the Ideas Inbox).

## `.sir/decisions/ADR-NNN-title.md`

```markdown
# ADR-NNN: <decision>
Date · Status (proposed | accepted | superseded by ADR-MMM) · Deciders
## Context   ## Options (with pros/cons)   ## Decision   ## Consequences   ## Sources checked
```

## `.sir/status.json` (read by the Command Center)

```json
{
  "id": "sir-health", "version": "1.0.0-beta.3", "tier": "flagship", "wave": 1,
  "health": 4.2, "updated": "2026-11-05T18:00:00+02:00",
  "platforms": { "web": "beta", "windows": "building", "macos": "building", "android": "beta",
                 "ios": "building", "ipados": "building", "wearos": "planned", "watchos": "planned" },
  "ci": "green", "lastCommit": "abc1234", "preview": "https://…", "blockers": ["Apple account"],
  "ownerActions": 2
}
```

---

## `.sir/tasks/T-NNN.md`: task spec (written by the PM so Haiku can build it well)

```markdown
# T-NNN: <imperative title>     owner: <agent> · branch/worktree: <name> · depends: <T-…>
## Why
One or two sentences: the user or business outcome.
## Read first
- AGENTS.md §… · docs/sir/standard/<module>.md
- <path>:<lines> (what to learn from it) · pattern to copy exactly: <path of a similar finished file>
## Exact changes
| File | Create/modify | What, precisely |
|---|---|---|
| packages/core/src/booking/schema.ts | create | `BookingInput` Zod schema: fields, types, constraints … |
| … | … | … |
Types and signatures (paste them):
    export function createBooking(input: BookingInput, ctx: Ctx): Promise<Result<Booking, BookingError>>
## Behavior and edge cases
- Empty / error / offline / slow / concurrent / RTL / 10k items / invalid input / permission denied …
## UI (if any)
- The 5 states, i18n keys (all project locales), accessibility labels, motion, haptics.
## Acceptance criteria (each one testable)
- [ ] …
## Tests to write
- unit: … · integration: … · e2e: …
## Must pass
`pnpm verify` · `pnpm test --filter …` · (e2e command)
## Don't touch
<files and areas outside ownership>
## Return
≤250-word summary, files changed, command output, screenshots, open questions.
## Budget
~N tool calls. Blocked or unsure → stop and write to .sir/inbox/orchestrator.md.
```

## `MERGE.md` (one per merge, kept in the surviving project's `docs/`)

```markdown
# Merge: <source A> + <source B> → <product> (<date>)
Decision: ADR-NNN · New name/identity or kept name: … (domain, store-name and trademark checks: …)
## Feature parity
| Feature / behavior | From | Status in new product | Verified how |
|---|---|---|---|
## Data migration
Source → target, scripts, dry-run result, record counts before/after, rollback plan
## Redirects and links
Old URL → new URL (301) · deep links · old app's final update (if it was published)
## Infrastructure
New: GitHub repo, Firebase projects, Vercel project, EAS project, others · archived: old repos
## Presence updated
TickTick · Command Center · PORTFOLIO · sirahmed8 portfolio and pinned repos · LinkedIn (draft) · ByteVibeHQ bios · domains · store listings
## Old folders
Moved to D:\Projects\old projects\<name>\ (with a pointer README) on <date>
```

## `BUILDS.md` (per product, updated at every milestone)

```markdown
# Builds — <Product> v<version> (<date>)
| Platform | Artifact | Link | SHA-256 | Installed & smoke-tested on | Notes |
|---|---|---|---|---|---|
| Android | app-release.apk / .aab | <GitHub Release or Drive link> | … | Ahmed's Android phone, emulator API 37 | |
| iPhone/iPad | unsigned .ipa, simulator .app | … | … | iPhone 14 via SideStore; iPad simulator | no push with free Apple ID |
| … | | | | | |
## How to install
- Android: `adb install -r app-release.apk` (or open it from Drive and allow this source)
- iPhone: SideStore → + → choose the .ipa (free Apple ID: max 3 apps, refresh within 7 days)
- Windows / macOS / Linux: …
## Known limitations
```

## `D:\Projects\_SIR\ops\IDEAS_INBOX.md`

```markdown
# Ideas Inbox (Ahmed writes here anytime; HQ triages every session)
- [ ] 2026-11-02 · "<idea in Ahmed's words>" · from: phone/TickTick/file
  → triage: <project BOARD T-…> | <standard proposal P-…> | declined: <reason> · ledger row R-… · by HQ on <date>
```

## `D:\Projects\_SIR\knowledge\<topic>.md`: verified fact cache

```markdown
# <Topic> (for example: Google Play target API)
Fact: …
Source: <URL> · Checked: <YYYY-MM-DD> by <agent> · Re-verify after: <date + 30 days>
Implications for SIR projects: …
```
