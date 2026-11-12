# SIR Mods for GTA V: task queue (45 tasks, refreshed 2026-11-12, round r61)

Source of truth for the plan: `D:/Projects/_SIR/plans/sir-mods-for-gta-v.md` (section 23 is the current delta). Competitor facts: `D:/Projects/_SIR/ops/competitors/sir-mods-for-gta-v.md`. Product folder: `D:/Projects/SIR Mods for GTA V` (private repo `sirahmed8/sir-mods-for-gta-v`, branch `main`).

**How to queue these.** One task per agent round, in the order below. Tasks are grouped by milestone; inside a group the order matters, between groups follow dependencies. Every task starts with the same preamble: read `D:/Projects/AGENTS.md`, `D:/Projects/_SIR/ops/WORKER_PREAMBLE.md`, `D:/Projects/_SIR/standard/23-premium-code-bar.md`, the project `AGENTS.md` and `.sir/CHECKPOINT.md`, then run `git status` and `git log -5` in the product folder and never revert another agent's edits. Every task ends with the project checkpoint updated, a small commit pushed to `main`, a report in `D:/Projects/_SIR/ops/agy-runs/reports/`, and the done signal `python D:/Projects/_SIR/scripts/agy-done.py <task-id> ok "<one line>"`. No pull requests, no version above 1.0.0, no fake players or pitches in any path a user sees, `legacy/` is read-only, and the AHome folder is never opened.

**Done means the same thing for all 45:** the verify command passes (typecheck, lint, tests, build, secret scan), the CI run was seen green or, while the GitHub Actions quota flag `D:/Projects/_SIR/ops/ci-quota-exhausted.flag` exists, the full local verification output is pasted into the checkpoint, the exit check named in the task was performed with evidence in `D:/Projects/SIR Mods for GTA V/.sir/evidence/`, and the report says honestly what was seen and what was not.

**Skills column.** Skill names refer to `D:/Projects/_SIR/ops/SKILLS_INDEX.md`; the agent loads the digest in `ops/encyclopedia/<tool>/<name>.md` before starting the task.

---

## Milestone M0-M1: gate, scaffold, core slice (T1-T14)

### T1. Legacy parity matrix (read-only deep scan)

Scan `D:/Projects/SIR Mods for GTA V/legacy/` (`SIR Mods for GTA V (v1)`: OpenIV `.oiv` packages, custom vehicle models, ScriptHookV script plugins, handling meta files, web configuration prototypes) and write one honest matrix to `.sir/reports/parity.md`: every route, every API route and every component with no route, each with the source file that proves it, and a verdict of keep, port, drop or drop-with-reason, plus the target module (`installer`, `catalog`, `admin`, `ai`, `npc`, `profile`, `web`). Start numbers from `D:/Projects/_SIR/ops/inventory/SIR-ModPack-and-GTA-V-mods.md`: 90 third-party DLLs with unverified licences, about 28 tests while the README claimed 79. Read the code, do not trust READMEs. Read only, write nothing into `legacy/`.
**Acceptance test:** every route in the legacy inventories has a matrix row; the matrix names the features to drop on purpose and the ten biggest files over 300 lines.
**Skills:** `repomix-token-optimizer`, `graphify-ast-memory`.

### T2. Monorepo scaffold, tokens, RTL, health route and CI

Create the new build in `D:/Projects/SIR Mods for GTA V`: `apps/web` (Next.js 15+ App Router, React 19, TypeScript strict, Tailwind v4), `packages/core` (domain types + zod schemas for Mod, Manifest, Install, Backup, Supporter, Inquiry, NpcSession, Profile), `packages/data`, `packages/ui`, `packages/kit`, `apps/api`, `docs/`, `scripts/`; layers depend inward only, files under 300 lines, absolute imports, no `any`. Seed tokens from the project seed green `#16A34A`, light/dark/system/high-contrast themes, logical CSS properties only, RTL-first stylesheet, Arabic screen face (IBM Plex Sans Arabic, Cairo or Tajawal). Add `verify` script (typecheck, lint, tests, build, secret scan) and a GitHub Actions workflow running exactly that on `main`. Add `/api/health` returning real status.
**Acceptance test:** verify command output pasted into the report; CI run URL in it; shell screenshots in Arabic and English at 390 px and 1280 px in `.sir/evidence/`.
**Skills:** `next-forge`, `modern-web-guidance`, `deployments-cicd`.

### T3. The product's own Firebase project and the `owner-auth` package

Create Firebase project `sir-mods-for-gta-v` on the free Spark plan (never reuse another product's project), write `.firebaserc`. Build `packages/kit/owner-auth`: Firebase Auth Google sign-in, server-side ID token verification with JWKS, owner/admin allow-list failing closed, HttpOnly Secure SameSite=Strict session cookie, no localStorage tokens, sign-in rate limits, 2FA offer for owner accounts.
**Acceptance test:** forged token -> 403, client-side flag flip grants nothing, non-owner on owner route -> 403; owner sign-in works on screen; no key printed or committed.
**Skills:** `firebase_basics`, `firebase_auth_basics`, `vibe-auth-hardening`, `zero-trust-security-hardening`.

### T4. The data model and the Firestore rules, with emulator tests

Write `firestore.rules` and `docs/data-model.md` for the collections in plan section 23.4 (mods, manifests, installs+events, backups, supporters, inquiries, npcSessions, profiles, leads, auditLog). Deny by default, `request.auth` on every read/write, curator scoped to own mods, players read only published mods.
**Acceptance test:** emulator tests pass: cross-tenant read fails, forged role claim write fails; rules compile with no warning; real output pasted in report.
**Skills:** `firestore_rules_creation`, `firebase_security_rules_auditor`, `firebase_firestore`, `database-reliability-transactions`.

### T5. Installer core: game folder detection, copy with backup, uninstall

Build `packages/installer-core/`: detect game folder, copy with backup, uninstall. 
**Acceptance test:** temp-folder test - install then uninstall leaves SHA-256 hashes equal to the start; backup restore verified; before/after hashes in report.
**Skills:** `production-engineering-standards`, `karpathy-skills`.

### T6. The shared UI kit: tokens, four themes, five states, spring components

Build `packages/ui` per `plans/SHARED_PLATFORM_KIT.md` sections 7-8 and `plans/GEMINI_QUALITY_CHARTER.md`: InputBox, TabBar, BottomSheet, SidePanel, Modal, Card, Chip, Button, Select, Avatar, Toast, Skeleton. Springs stiffness 300-400, damping 28-30, transform+opacity only, reduced motion honoured. Tab bar: active label only, 44 px targets, scrolls active tab into view. Five states on every view. Bidi per character, `<bdi>` for mixed runs, never show "RTL"/"LTR".
**Acceptance test:** `/dev/kit` gallery shows every component in four themes and five states, screenshotted at 390 px and 1280 px in Arabic and English.
**Skills:** `modern-ui-ux-design-system`, `emil-motion-impeccable`, `anti-vibecoded-design-system`.

### T7. The portal catalog page with five states

Build the public catalog page: five states, honest claims lint (rejects "undetectable", unproven numbers).
**Acceptance test:** screenshots at 390 px in Arabic and English; lint rejects "undetectable".
**Skills:** `react-best-practices`, `high-conversion-copywriting`, `taste-design-engine`.

### T8. The NPC server skeleton with provider interface and cost cap

Create the NPC dialog server skeleton: provider interface (Gemini flash-lite -> flash -> OpenRouter free -> local, per `ai-proxy`), per-session token cap, daily cost cap, `AI_ENABLED` kill switch.
**Acceptance test:** cap test stops after N tokens; kill switch returns a clean disabled response; output pasted in report.
**Skills:** `ai-gateway`, `ai-sdk`, `omniroute-resilience-gateway`, `gemini-api-dev`.

### T9. The owner-only analytics page and the billing fallback page

Build `/owner` gated by server-verified owner token: real metrics only (installs, uninstalls, NPC sessions, errors, AI cost); dash-with-reason when a metric has no data. Build the pricing page: plan table, currency auto-detected from locale with manual override, "Subscriptions launching soon" + email capture writing a Lead doc and rejecting invalid addresses. Monetisation sells services/supporter perks, never mod files (plan 23.2).
**Acceptance test:** 403 tests pass for forged and non-owner tokens; owner page shows real emulator numbers on screen; lead capture creates a document and rejects a bad address.
**Skills:** `firebase_firestore`, `high-conversion-copywriting`, `legal-compliance-shield`.

### T10. The licence CSV, the publisher policy doc, the September 2026 guidelines

Write `docs/THIRD_PARTY.csv` (name, author, licence text, source URL, "redistribution allowed: yes/no with proof") for every binary in `legacy/` (ScriptHookV, MinHook, dinput8, ~87 script DLLs). Write `docs/PUBLISHER_POLICY.md` quoting the official Rockstar single-player mods support page (`support.rockstargames.com/articles/5NVOAYjcTomO8v6SX2k76k/pc-single-player-mods`, updated 2026-09-15) and, if fetchable, the linked Mod Guidelines PDF headings; record read dates and URLs.
**Acceptance test:** CSV row count equals binary count, no empty/"unknown" cells without "do not bundle"; policy doc has quoted headings and dates; gitleaks passes.
**Skills:** `legal-compliance-shield`, `zero-trust-security-hardening`, `open-seo-auditor` (for fetching discipline, n/a - use webfetch).

### T11. Edition detection: Legacy vs Enhanced

Detect which GTA V edition is installed: exe name (`GTA5.exe` vs `GTA5_Enhanced.exe`), build number from PE header, launcher (Steam/Epic/Rockstar). Result drives which mods the catalogue offers (`editions` field) and which loader is required (`OpenIV.asi` vs `OpenRPF.asi`). Refuse with a clear bilingual message when a Legacy-only mod is selected on Enhanced.
**Acceptance test:** unit tests with fixture folders for both editions; wrong-edition install attempt is blocked with the correct message; detection result shown on the installer Home screen.
**Skills:** `production-engineering-standards`, `verification`.

### T12. Signed manifests per game build

Manifest generator emits `manifests/{edition}/{gameBuild}` docs: mod ids, file hashes, loader requirements; server signs with Ed25519 (key in Secret Manager); installer verifies signature and refuses unsigned manifests.
**Acceptance test:** tampered manifest fails verification; manifest for an unknown game build is not served; signature verification unit test passes.
**Skills:** `database-reliability-transactions`, `zero-trust-security-hardening`, `firebase_security_rules_auditor`.

### T13. `.oiv` / `.oivs` package parser v1

Parse OpenIV `assembly.xml` packages: list contents, metadata (name, author, version, target archives), produce an install plan preview (files, target RPF paths inside `mods\`) before anything is written.
**Acceptance test:** fixture `.oiv` parses to the expected file list; malformed package produces a clean error, not a crash; install plan preview matches the fixture contents.
**Skills:** `production-engineering-standards`, `binary-reverse-engineer` (format only, no DRM circumvention).

### T14. Curator admin: mod catalogue CRUD with licence gate

Admin screens (server-verified owner/curator token) to create/edit/publish mods: slug, AR/EN names and descriptions, category, `editions[]`, `loader`, files with SHA-256, licence block (name, author, sourceUrl, redistributionProof). Status flow `draft -> review -> published -> blocked`; publish is impossible without a complete licence block.
**Acceptance test:** publish attempt without licence proof is refused; a published mod appears in the public catalogue API; non-curator gets 403.
**Skills:** `react-best-practices`, `firestore_rules_creation`, `a11y-debugging`.

---

## Milestone M2: installer depth, safety, NPC AI (T15-T28)

### T15. Install profiles

Named sets of mods the player switches between in one click (e.g. "Graphics + Handling", "Cars only"). Stored per user in `profiles/{uid}`.
**Acceptance test:** create two profiles on a temp install, switch, verify active file set matches the profile manifest hashes.
**Skills:** `database-reliability-transactions`, `react-best-practices`.

### T16. Load order and per-file conflict resolution

Mod load order list (drag to reorder, top wins); when two mods write the same target file the UI shows the conflict and lets the player pick the winner per file.
**Acceptance test:** two fixture mods writing the same file - conflict is detected, chosen winner is the one installed, order change flips the winner.
**Skills:** `production-engineering-standards`, `modern-web-guidance`.

### T17. Check-and-repair after game updates

One button verifies every installed file against the manifest hashes and re-installs or removes stale copies (the classic "everything broke after an update" failure ModDrop V advertises solving).
**Acceptance test:** corrupt one installed file, run check-and-repair, hash matches manifest again; report lists what was repaired.
**Skills:** `verification`, `production-engineering-standards`.

### T18. Uninstall-all and orphan vacuum

Every install writes a ledger of exact files touched; uninstall-all removes exactly those files and vacuums orphans left by older installs.
**Acceptance test:** install 3 fixture mods, uninstall all, directory tree hash-equals the pre-install state; orphan fixture file is removed.
**Skills:** `production-engineering-standards`, `accidental-data-loss-prevention` (skill: verify before destructive ops).

### T19. DLC add-on installer (`dlc.rpf` + `dlclist.xml`)

Accept a `dlc.rpf` (or folder containing one), copy into `mods\update\x64\dlcpacks`, register in `dlclist.xml` inside `mods\update.rpf`-equivalent path per OpenIV conventions, support enable/disable.
**Acceptance test:** fixture dlc.rpf installs, appears in dlclist.xml, disable removes the entry, game-folder tree restores on uninstall.
**Skills:** `production-engineering-standards`, `open-seo-auditor` (n/a - use `verification`).

### T20. Game version and ScriptHookV compatibility checker

Read `GTA5.exe`/`GTA5_Enhanced.exe` PE version, compare against a maintained table of ScriptHookV builds (from `docs/` data file updated by the update watcher), warn before launch when incompatible.
**Acceptance test:** fixture exe versions map to correct compatibility verdicts; outdated ScriptHookV shows the warning modal with the download link.
**Skills:** `verification`, `website-traffic-analytics` (n/a - use `production-engineering-standards`).

### T21. GTA Online safety interlock

When the player launches GTA Online (or the interlock is enabled), rename `dinput8.dll`/`OpenIV.asi`/`OpenRPF.asi` loaders to `.disabled` and block ScriptHookV; restore on return to story mode. Visible status badge in the installer.
**Acceptance test:** on a temp game folder the toggle renames and restores the loader files; badge state matches filesystem state; test proves no loader file is active while "online mode" is on.
**Skills:** `zero-trust-security-hardening`, `production-engineering-standards`.

### T22. Consent-gated telemetry and data deletion

Install reports (success/failure, edition, game build - never file paths or account ids beyond uid) only after explicit opt-in; Settings toggle; "Delete my data" removes `installs/{uid}`, `npcSessions`, `profiles` for that uid.
**Acceptance test:** with consent off, zero network calls from the installer (verified by test double); delete-my-data removes the emulator docs; privacy page documents exactly this.
**Skills:** `firebase_security_rules_auditor`, `legal-compliance-shield`, `zero-trust-security-hardening`.

### T23. NPC dialog engine v1

Persona-grounded NPC conversations through the provider chain: system prompt per NPC persona, safety + profanity filter on input and output, streaming replies, per-session token cap, conversation context window, session metadata (never raw text beyond 24h).
**Acceptance test:** `npm run eval:npc` - 40 prompts pass safety/persona checks; latency p50 recorded in report; filter blocks a test profanity set.
**Skills:** `ai-sdk`, `ai-gateway`, `gemini-api-dev`, `omniroute-resilience-gateway`.

### T24. Support assistant grounded in the guide

Chat widget/drawer answering only from `docs/` guide content (retrieval-grounded, zero hallucinated policies), 5 free questions/day per user, visible quota badge "X / 5 free questions remaining today", graceful upgrade prompt at zero.
**Acceptance test:** question outside the docs gets a "check the guide / contact support" answer, not an invention; quota decrements and resets; badge text correct in AR and EN.
**Skills:** `ai-sdk`, `firebase_firestore`, `react-best-practices`.

### T25. AI cost controls end-to-end

Per-session cap, daily cost cap in `config/limits.json`, `AI_ENABLED` kill switch, cost recorded per session in `npcSessions`, owner alert (Telegram) when daily spend crosses 50% and 90%.
**Acceptance test:** scripted session hits the cap and stops mid-conversation with a clean message; kill switch disables all AI routes; cost numbers reconcile with provider usage logs.
**Skills:** `ai-gateway`, `omniroute-resilience-gateway`, `zero-trust-security-hardening`.

### T26. Leads capture and currency auto-detection (pricing page deep pass)

Email capture writes `leads/{id}` (email, locale, created_at), rejects invalid addresses server-side; currency auto-detects from visitor locale/IP with manual override; EGP first with USD/SAR/AED toggle; all prices are services/supporter perks, never mod files.
**Acceptance test:** invalid email rejected with field error; locale `ar-EG` shows EGP, `en-US` shows USD with override working; lead doc appears in emulator.
**Skills:** `react-best-practices`, `high-conversion-copywriting`, `firebase_firestore`.

### T27. Legal pack: privacy, terms/EULA, refunds, cookies

`/legal/*` pages: privacy (exact data list, sub-processors directory, DPA note, "we do NOT train AI on customer data" clause), terms/EULA (single-player, no warranty, user installs at own risk, capped liability, arbitration), refunds/cancellation, cookies with reject-all equal prominence. NPC text retention (24h) documented.
**Acceptance test:** every data type in the data model appears in the privacy page; cookie banner blocks trackers before consent and Reject is as prominent as Accept; pages render AR and EN.
**Skills:** `legal-compliance-shield`, `modern-web-guidance`, `a11y-debugging`.

### T28. Bidi and Arabic-first pass across all built screens

Per-character direction detection in every input, `<bdi>` isolation for mixed runs, logical CSS properties audit (no physical margin/padding in components), Arabic copy review (Egyptian for players, MSA only in legal), no "(RTL)"/"(LTR)" literals anywhere.
**Acceptance test:** mixed AR/EN input test shows correct caret direction per character; grep finds zero physical-direction CSS properties in `packages/ui`; screenshots AR/EN of every built screen.
**Skills:** `modern-web-guidance`, `anti-vibecoded-design-system`, `a11y-debugging`.

---

## Milestone M3-M4: portal completeness, quality, owner tools (T29-T40)

### T29. Theme engine: four themes, high contrast, zero-flash switch

Light, dark, system, high contrast via design tokens only; theme switch with zero white flash; persists per user.
**Acceptance test:** switching themes on every screen shows no flash (screenshot sequence); high-contrast theme passes WCAG contrast on all text pairs used.
**Skills:** `emil-motion-impeccable`, `modern-ui-ux-design-system`, `a11y-debugging`.

### T30. Responsive and five-states audit, 320 px to 4K

Playwright matrix: every portal screen at 320/390/768/1280/1920 in Arabic RTL and English LTR, light and dark; zero horizontal overflow; five states verified per screen.
**Acceptance test:** matrix script output shows 0 overflow and all five states present per screen; screenshots stored in `.sir/evidence/`.
**Skills:** `verification`, `mobile-ergonomics-polish`, `a11y-debugging`.

### T31. WCAG 2.2 AA audit and fixes

Tool-measured contrast (not eyeballed), 44 px targets, focus order, aria labels, keyboard navigation for installer and portal.
**Acceptance test:** axe/Lighthouse accessibility score >= 95 on portal pages; contrast report file in `.sir/evidence/`; zero critical findings.
**Skills:** `a11y-debugging`, `verification`, `mobile-ergonomics-polish`.

### T32. Offline PWA for the portal and config tools

Service worker caches the portal shell and the offline-capable tools (handling calculator, car spec viewer); manifest for installability.
**Acceptance test:** airplane-mode reload serves the shell; offline handling calculator works; SW update flow tested.
**Skills:** `modern-web-guidance`, `firebase_hosting_basics`.

### T33. Landing page, guide hub, and mods catalog public pages

Landing (Stranger Test: what it is, who for, next step in 5 seconds), installation guide hub (AR-first, per-edition), public catalog with licence badges.
**Acceptance test:** five states on each page; screenshots 390/1280 AR/EN; no banned AI vocabulary in copy (grep list).
**Skills:** `high-conversion-copywriting`, `taste-design-engine`, `react-best-practices`.

### T34. SEO and GEO pack

`llms.txt`, `/facts` page with structured data, `SoftwareApplication` JSON-LD, AR/EN meta targeting the queries in plan 23.8, weekly `scripts/check_ai_visibility.py`.
**Acceptance test:** JSON-LD validates; `llms.txt` served; visibility script runs and records baseline.
**Skills:** `open-seo-auditor`, `website-traffic-analytics`, `modern-web-guidance`.

### T35. Operations runbook and Telegram digest

`docs/OPS.md`: nightly game-build version check, ScriptHookV update watcher (writes manifest freshness), error-log digest, `/api/health` dashboard, emergency alerts (admin auth failure spikes, key leak) to the owner Telegram bot. Weekly Telegram line: installs, uninstalls, NPC sessions.
**Acceptance test:** watcher detects a fixture "new game build" and queues a manifest refresh task; Telegram digest script sends one formatted line to the test chat.
**Skills:** `production-engineering-standards`, `verification`.

### T36. Dual hosting: Firebase + Vercel live

Deploy the portal to Firebase Hosting AND Vercel (Vercel CLI import of the GitHub repo), identical build and env vars on both; custom-domain-ready config.
**Acceptance test:** both URLs curl 200 (retry once on timeout) and are written in the checkpoint; env parity verified (no key present on one host only).
**Skills:** `firebase_hosting_basics`, `firebase_app_hosting_basics`, `env-vars`, `deployments-cicd`.

### T37. Owner actions pack: domain, code signing, payment accounts

Write exact owner steps (names/links only, no secrets) to `ops/OWNER_ACTIONS.md` via the project docs: domain purchase (`sirgtamods.com` or `.app`, owner picks), code-signing certificate for the Windows installer, Paymob/payment account only if the legal gate passes. Everything is "launching soon" until keys exist.
**Acceptance test:** `docs/OWNER_STEPS.md` lists each step with cost and link; nothing is purchased or signed by the agent; pricing page still shows the fallback.
**Skills:** `legal-compliance-shield`, `env-vars`.

### T38. Secrets rotation list from legacy `.env` findings

From the inventory (`ops/inventory/SIR-ModPack-and-GTA-V-mods.md`): list every secret name that was committed in legacy `.env` files (Telegram token etc.), mark each rotate/revoke/reissue, names only - never values.
**Acceptance test:** list in `docs/OWNER_STEPS.md`; grep of the repo finds no legacy `.env` values; gitleaks clean.
**Skills:** `zero-trust-security-hardening`, `vibe-auth-hardening`.

### T39. CI hardening: every gate in `verify`

`.github/workflows/verify.yml` runs typecheck, lint, tests, build, secret scan, binary-vs-CSV check, rules compile check; while the Actions quota flag exists, paste full local verification output instead of a CI URL.
**Acceptance test:** an injected binary fails the CSV check locally; a planted secret fails gitleaks; workflow file reviewed line by line.
**Skills:** `deployments-cicd`, `zero-trust-security-hardening`, `verification`.

### T40. End-to-end install flow proof on a temp game folder

Full run on a synthetic game folder: detect edition -> pick mods -> resolve conflicts -> install -> verify hashes -> simulate "game update" (touch a file) -> check-and-repair -> uninstall-all -> hash-equal restore. Screenshots at each step.
**Acceptance test:** the scripted E2E passes start to finish; every step has a screenshot; report includes the hash-equality proof.
**Skills:** `verification`, `production-engineering-standards`, `agent-supercharged-os`.

---

## Milestone M5-M6: polish, launch prep, release (T41-T45)

### T41. Clean-machine QA pass and bugfix sweep

Fresh checkout on a clean profile (or clean VM if available): run the whole flow, file every defect, fix all criticals, re-run.
**Acceptance test:** defect list in report with severity; zero open criticals; verify green after fixes.
**Skills:** `verification`, `review-agent`, `agent-supercharged-os`.

### T42. Performance budgets

Portal Lighthouse mobile >= 90 (JSON saved), installer cold start < 3 s on the owner's laptop class, catalog API p95 < 300 ms on emulator, NPC first-token latency recorded.
**Acceptance test:** Lighthouse JSON in `.sir/evidence/`; timings in report; budgets enforced in CI where automatable.
**Skills:** `website-traffic-analytics`, `verification`, `ponytail-yagni-optimizer`.

### T43. Launch content pack (owner approves before anything posts)

Draft only, stored in `ops/` of _SIR or `docs/marketing/`: Arabic YouTube tutorial script (Egyptian), GTA5-Mods.com tool-page draft (only if the tool qualifies as a file tool, not a mod - policy check first), r/GTAMods post draft, Discord server plan, 12-week calendar from DEEP plan 5.4 updated with the Enhanced-edition angle.
**Acceptance test:** every draft passes the banned-vocabulary and honest-claims lint; nothing is posted; owner approval requested via the bus.
**Skills:** `social-creator-studio`, `high-conversion-copywriting`, `open-seo-auditor`.

### T44. Legacy archive preparation for M6

Finalize the parity matrix, write `docs/LEGACY_ARCHIVE.md` (what was ported where, what was dropped and why), prepare the `legacy/` -> `D:/Projects/old projects/` move script (dry-run only; the real move happens at M6 with owner-visible checkpoint).
**Acceptance test:** every parity-matrix "port" row maps to a real file in the new build or is marked "deferred to M6"; dry-run output clean.
**Skills:** `repomix-token-optimizer`, `production-engineering-standards`.

### T45. Release candidate 1.0.0

Version stays 1.0.0. Release notes AR/EN, changelog, final verify, CI state recorded (or local-verify paste while quota flag exists), checkpoint updated with both hosting URLs, domain status, and the honest list of what is not verified.
**Acceptance test:** `verify` green; release notes exist in both languages; checkpoint names every open item with its reason; report written and `agy-done.py` run.
**Skills:** `verification`, `legal-compliance-shield`, `agent-supercharged-os`.

---

## Dependency map

- T1, T2, T3 parallel. T4 needs T2+T3. T5-T8 need T2. T9 needs T2+T3+T6. T10 needs T2.
- T11 needs T5. T12 needs T4+T5. T13 needs T5. T14 needs T4+T6.
- T15-T18 need T13+T16 area (installer-core); T19 needs T13; T20 needs T2; T21 needs T5; T22 needs T3+T5.
- T23-T25 need T8 (+T3 for keys). T26 needs T9 area. T27 needs T4 (data list) + T9.
- T28 needs T6+T7+T9+T26+T27. T29 needs T6. T30-T31 need T28+T33. T32 needs T33. T33 needs T6+T7. T34 needs T33.
- T35 needs T20+T36 area. T36 needs T2+T3. T37-T38 need T10. T39 needs T10+T2. T40 needs T11-T21. T41 needs T40. T42 needs T33+T40. T43 needs T10+T33. T44 needs T1+T40. T45 needs everything above.

## Deliberately not in this queue

The Windows installer packaging (MSI/EXE signing pipeline), the in-game ASI telemetry plugin build (needs game-side testing hardware), the GTA Online block at OS level beyond the loader interlock, and any paid-mod storefront work - each is gated on the M0 licence/policy checks and owner decisions listed in plan section 23.9-23.10.
