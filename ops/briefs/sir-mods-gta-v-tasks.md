# SIR Mods for GTA V: the first ten tasks for the free agents (queue ready)

Round r52, 2026-11-12. Source of truth for the plan: `D:/Projects/_SIR/plans/sir-mods-for-gta-v.md`. Product folder: `D:/Projects/SIR Mods for GTA V` (private repo `sirahmed8/sir-mods-for-gta-v`, branch `main`).

**How to queue these.** One task per agent round, in the order below. Tasks 1 to 3 are independent of each other and can run side by side; everything from 4 on depends on the scaffold from task 2. Every task starts with the same preamble: read `D:/Projects/AGENTS.md`, `D:/Projects/_SIR/ops/WORKER_PREAMBLE.md`, `D:/Projects/_SIR/standard/23-premium-code-bar.md`, the project `AGENTS.md` and `.sir/CHECKPOINT.md`, then run `git status` and `git log -5` in the product folder and never revert another agent's edits. Every task ends with the project checkpoint updated, a small commit pushed to `main`, a report in `D:/Projects/_SIR/ops/agy-runs/reports/`, and the done signal `python D:/Projects/_SIR/scripts/agy-done.py <task-id> ok "<one line>"`. No pull requests, no version above 1.0.0, no fake players or pitches in any path a user sees, `legacy/` is read-only, and the AHome folder is never opened.

**Done means the same thing for all ten:** the verify command passes (typecheck, lint, tests, build, secret scan), the CI run was seen green or, while the GitHub Actions quota flag `D:/Projects/_SIR/ops/ci-quota-exhausted.flag` exists, the full local verification output is pasted into the checkpoint, the exit check named in the task was performed on screen with a screenshot in `D:/Projects/SIR Mods for GTA V/.sir/evidence/`, and the report says honestly what was seen and what was not.

---

## T1. Legacy parity matrix (read-only deep scan)

Scan the three legacy apps in `D:/Projects/SIR Mods for GTA V/legacy/` (SIR Mods for GTA V v1: OpenIV `.oiv` packages, custom vehicle models, ScriptHookV script plugins, handling meta files, and web configuration prototypes) and write one honest matrix to `.sir/reports/parity.md`: every route, every API route and every component with no route, each with the source file that proves it, and a verdict of keep, port, drop or drop-with-reason, plus the target module of the new build (`mods`, `installer`, `catalog`, `admin`, `ai`, `npc`, `profile`). The numbers to start from are in `D:/Projects/_SIR/ops/inventory/SIR-ModPack-and-GTA-V-mods.md`: the legacy inventory has 90 third-party DLLs (ScriptHookV by Alexander Blade, MinHook, dinput8 and about 87 script DLLs) with unverified licence status; about 28 tests (README claimed 79). Read the code, do not trust the READMEs: the legacy README claims "281/281 tests" and that claim is unverified, and the 62 files over 300 lines are real and must appear as size notes. Read only, write nothing into `legacy/`. Exit check: every route listed in the three inventories has a row in the matrix, and the matrix names the feature that no competitor has covered yet (the split bill with a fairness meter). Report: what was found, the count of routes per app, the ten biggest files to split, and the list of features that must be dropped on purpose.

---

## T2. Monorepo scaffold, tokens, RTL, health route and CI

Create the new build structure in `D:/Projects/SIR Mods for GTA V`: `apps/web` (Next.js 15+ App Router, React 19, TypeScript strict, Tailwind v4 with the design tokens), `packages/core` (domain types and zod schemas for Mod, Manifest, Install, Backup, Supporter, Inquiry, NpcSession, Profile), `packages/data`, `packages/ui`, `packages/kit`, `apps/api`, `docs/`, `scripts/`, with layers depending inward only, files under 300 lines, absolute imports and no `any`. Seed the token file from the project seed green `#16A34A` with light, dark, system and high-contrast themes, logical CSS properties only, an RTL-first global stylesheet and the Arabic screen face (IBM Plex Sans Arabic, Cairo or Tajawal). Add the `verify` script (typecheck, lint, tests, build, secret scan) and a GitHub Actions workflow that runs exactly that on `main`. Add a health route at `/api/health` returning real status values, never fake ones. Exit check: the verify command output is pasted into the report, the CI run URL is in it, and one screenshot of the shell exists in Arabic and in English at 390 px and 1280 px in `.sir/evidence/`. Report: the tree, the commands with their real output, and anything that could not be installed for free.

---

## T3. The product's own Firebase project and the `owner-auth` package

Create the Firebase project named exactly `sir-mods-for-gta-v` on the free Spark plan, keep it separate from every other SIR product and never reuse another project's, and put its id in `.firebaserc` in the product root. Build `packages/kit/owner-auth`: Google sign-in through Firebase Auth, server-side ID token verification with JWKS, an owner and admin allow-list that fails closed, the session in an HttpOnly, Secure, SameSite=Strict cookie with no token in localStorage, rate limits on sign-in, and a second factor offer for owner accounts. Write the negative tests: a forged token gets 403, a client-side flag flip grants nothing, a non-owner token on the owner route gets 403. Exit check: the three negative tests run and fail in the expected way (the request is refused), the owner sign-in works in the browser on screen, and no key is printed or committed. Report: the project id, the commands with their real output, the keys file path that stays ignored, and the confirm that the Gemini and OpenRouter keys for this product will be created on this same project and never on a shared one.

---

## T4. The data model and the Firestore rules, with emulator tests

Write the Firestore data model and `firestore.rules` for Mod, Manifest, Install, Backup, Supporter, Inquiry, NpcSession, Profile, with the compound indexes the queries need, and `docs/data-model.md` describing each collection, its fields and its access rules. The rules deny by default, check `request.auth` on every read and write, scope a pitch owner to their own mods, and let a player read a mod only when they are on it. Write the emulator tests that prove it, including a cross-tenant read that must fail and a write with a forged role claim that must fail. Use the `firestore_rules_creation` and `firebase_security_rules_auditor` skills from `D:/Projects/_SIR/ops/encyclopedia/`. Exit check: the emulator tests pass and their real output is pasted in the report, and the rules compile with no warning. Report: the rules file, the test output, the indexes, and every rule that was deliberately made stricter than the legacy rules.

---

## T5. The installer core and game folder detection

Build the installer core in `packages/installer-core/`: detect game folder, copy with backup, uninstall. Files: `packages/installer-core/`. Check: temp-folder test, hashes equal after uninstall. Report: the installer code path, the test output with before/after hashes, and the backup restore verification.

---

## T6. The shared UI kit: tokens, four themes, five states, spring components

Build `packages/ui` with one component per control, following the shared kit in `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md` section 7 and 8 and the motion rules in `D:/Projects/_SIR/plans/GEMINI_QUALITY_CHARTER.md`: InputBox, TabBar, BottomSheet, SidePanel, Modal, Card, Chip, Button, Select, Avatar, Toast, Skeleton. Every sheet and panel opens and closes with the same spring (stiffness 300 to 400, damping 28 to 30), transform and opacity only, reduced motion honoured. The tab bar shows the label of the active tab only, keeps 44 px targets, and scrolls the active tab into view on mount and on change. Every view has the five states: idle, loading skeleton, empty with one action, error with retry, populated. The inputs detect Arabic or Latin per character and set the direction and the caret live, mixed runs are isolated with `<bdi>`, and the words "RTL" and "LTR" never reach the user. Exit check: a component gallery page at `/dev/kit` shows every component in the four themes and the five states, screenshotted at 390 px and 1280 px in Arabic and English. Report: the component list, the spring constants used, and the gallery screenshots.

---

## T7. The portal catalog page with five states

Build the portal catalog page with five states (idle, loading skeleton, empty with one action, error with retry, populated) and honest claims lint. Check: screenshots at 390 px; lint rejects "undetectable". Report: the catalog page code, the five states implemented, the lint errors fixed, and the 390 px screenshots in Arabic and English.

---

## T8. The NPC server skeleton with cost cap

Create NPC server skeleton with provider interface and per-session cost cap. Check: cap test stops after N tokens. Report: the server code, the cost cap test output, and the kill switch behaviour.

---

## T9. The owner-only analytics page and the billing fallback page

Build `/owner`, gated by a server-verified owner token from T3, showing real metrics only: installs, uninstalls, NPC sessions, errors, AI cost. A non-owner token gets 403 and a forged token gets 403, and the page shows a dash with the reason when a metric has no data, never a zero dressed as a fact. Build the pricing page too: the plan table from `plans/sir-mods-for-gta-v.md` section 7 with the currency auto-detected from the visitor locale with a manual override on top, "Subscriptions launching soon" and an email capture that writes a Lead document and rejects an invalid address. Exit check: the 403 tests pass and their output is pasted in, the owner page is shown on screen with real numbers from the emulator, and the lead capture is shown creating a document. Report: the metrics list with the query behind each one, the screenshots, and the list of numbers that still need a real venue before they mean anything.

---

## T10. The licence CSV and the publisher policy doc

Write `docs/THIRD_PARTY.csv` with name, author, licence text, source URL and "redistribution allowed: yes/no with proof" for every top-level dependency (ScriptHookV, MinHook, dinput8 and about 87 script DLLs). Check: row count equals binary count, no cell empty or marked "unknown, do not bundle". Write `docs/PUBLISHER_POLICY.md` with URL and read date. Check: file exists with quoted headings. Exit check: the CSV has a row for every binary, the policy doc has quoted headings, and the gitleaks check passes. Report: the CSV file, the policy doc, the row count, and the gitleaks findings.

---

**Queue order and dependencies.** T1, T2 and T3 can run in parallel (T1 is read-only, T2 owns the repo scaffold, T3 owns the Firebase project and auth). T4 needs T2 and T3. T5 needs T2. T6 needs T2. T7 needs T2 and T6. T8 needs T2. T9 needs T3 and T2 and T6. T10 needs T2 and the legacy inventory. Each task writes to its own area of the repository so two agents never fight over one file: T1 writes `.sir/reports/parity.md`, T2 writes the scaffold, `packages/ui` skeleton and the workflow, T3 writes `packages/kit/owner-auth` and `.firebaserc`, T4 writes `firestore.rules`, `docs/data-model.md` and the emulator tests, T5 writes `packages/installer-core/`, T6 writes `packages/ui`, T7 writes `apps/web/app/(player)/catalog`, T8 writes `packages/installer-core` and its tests, T9 writes `apps/web/app/owner` and `apps/web/app/pricing`, T10 writes `docs/THIRD_PARTY.csv` and `docs/PUBLISHER_POLICY.md`. Each task writes to its own area of the repository so two agents never fight over one file.

**What is deliberately not in these ten:** the tournaments engine, the owner console with the cash register, the Windows installer, the AI features beyond the NPC support bot, the marketing work. They are M4, M5 and M6 in `plans/sir-mods-for-gta-v.md` and each one needs the ten above to be green first.