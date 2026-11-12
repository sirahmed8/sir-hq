# First 10 Tasks to Hand to Free Agents: SIR Education Hub (sir-education-hub-tasks.md)

Tasks ready to queue for free CLI agents. Each task includes a title and one-paragraph brief. All tasks are designed to be completed in under 2 hours. Product folder: `D:\Projects\SIR Education Hub`. Product rules: read `AGENTS.md`, `.sir/PLAN.md`, `.sir/CHECKPOINT.md`, `D:\Projects\_SIR\plans\sir-education-hub.md` first. Never touch `D:\Projects\AHome`, never open AHome/Habiba material, never port `solve_*` graded-work code, version stays 1.0.0, no placeholders, no fake data, five states on every view, Arabic RTL + English, multi-tenant isolation proven by emulator tests.

## 1. Deep scan of legacy and plan upgrade
Scan the legacy application (`legacy/Obour Academic Hub/`, 344 TS/TSX files, ~62k lines) and `ops/inventory/Obour-Academic-Hub.md`. Write `.sir/reports/deep-scan.md`: every page and feature with a verdict (port / drop / rewrite), the data model to keep (subjects, exams, sections, questions, users, subscriptions), and the list of files that must never be ported (solve modes, fake fallbacks, credential scripts). Check: the report lists each of the 12+ pages with a verdict and names every file containing keys or graded-work logic (names only, no secret values), plus a mapping table from legacy feature to new module per plan section 5.

## 2. Secrets and quarantine report
Inside `legacy/Obour Academic Hub/`, list (names only, never contents) every file holding keys or credentials: the two Firebase admin JSON files, `new-service-account.json`, `.env.local`, Upstash/Cloudinary/Vercel Blob values. Confirm `git check-ignore` covers `legacy/` and the product `.gitignore` covers `.env*`. Append the key-rotation steps to `.sir/CHECKPOINT.md` open items. Check: report file exists with file names only, and `git status` shows nothing secret staged.

## 3. Scaffold the app shell
Create the Next.js (App Router, TypeScript, Tailwind v4) app skeleton in the product repo root per `plans/SHARED_PLATFORM_KIT.md` tokens: RTL logical CSS, light/dark/system/high-contrast themes, Cairo + Inter type pairing, `/api/health` route returning 200 JSON, root layout with bidi-safe input handling and five-state primitives, multi-tenant-aware routing (`/h/[slug]/...`). Check: `npm run build` exits 0, `npm run dev` serves `/api/health` 200, and a 390px screenshot shows no horizontal overflow.

## 4. Firestore deny-by-default rules + multi-tenant emulator tests
Write `firestore.rules` (deny by default; reads only for signed-in members of the Hub; writes owner/admin via custom claim only; cross-Hub read fails) and emulator tests under `tests/rules/` proving: anonymous read denied, cross-user read denied, cross-Hub read denied, owner write allowed, non-member write denied. Check: `firebase emulators:exec --only firestore 'npm run test:rules'` passes green.

## 5. Google sign-in with hardened session
Implement `src/server/auth/`: Firebase ID token verified server-side via JWKS, `OWNER_EMAILS`/`OWNER_UIDS` fail-closed owner check, HttpOnly+Secure+SameSite=Strict session cookie, rate limit on sign-in attempts, forged/expired token tests, Hub membership resolution. Check: unit tests prove forged token -> 403, expired token -> 401, valid token -> session cookie set; no token in localStorage anywhere; cross-Hub access denied.

## 6. Subject list + note viewer with five states
Build the Subject list and Lecture note viewer screens reading from Firestore/Storage: skeleton matching final geometry, empty state with one CTA, error state with Retry, populated state with keyset pagination, RTL/LTR and light/dark, scoped to the current Hub. Check: Playwright screenshots of all five states at 390px and 1280px archived in `.sir/evidence/`, zero console errors.

## 7. Legacy import script with dry run
Write `scripts/import-legacy.mjs`: connects to the old Firestore (service account from env only, never committed), exports subjects/exams/questions/notes/users/counts per collection, supports `--dry-run` printing per-collection counts and writing nothing, and `--apply` gated behind an explicit flag plus confirmation and a target Hub id. Check: `node scripts/import-legacy.mjs --dry-run` prints real counts (or a clear "no credentials configured" path) and creates zero writes; script has no embedded secrets; cross-Hub writes are rejected.

## 8. AI tutor refusal eval set and runner
Create `evals/tutor.jsonl` with 30 prompts (15 Arabic, 15 English) covering live-quiz answers, assignment solutions, exam leaks, plus hint/explanation requests that must pass, including prompts that try to leak another Hub's content. Write `scripts/eval-tutor.mjs` that calls the ai-proxy chain and exits non-zero below 100% correct behavior (refusal + hint offer on graded-work prompts; no cross-Hub leakage). Check: runner executes and reports per-prompt verdicts; CI step added.

## 9. Pricing page with launch fallback
Build `/pricing`: free vs Pro comparison in EGP with auto-detected USD/SAR/AED display, Hub trial vs subscription tiers, "Subscriptions launching soon" CTA opening an email-capture modal that writes one lead doc to Firestore via a validated server route, invalid email shows inline error. Check: submitting a valid email creates exactly one `leads` doc; invalid email rejected client and server side; no payment links anywhere; currency auto-detected from locale/IP.

## 10. CI pipeline green
Add `.github/workflows/ci.yml` (or fix existing): typecheck, lint, vitest, build, gitleaks, emulator rules tests on every push; deploy steps for Firebase Hosting and Vercel only after build passes. Check: latest `main` run is green (or, while `ops/ci-quota-exhausted.flag` exists, the full local verify output - typecheck, lint, test, build - is pasted into the checkpoint and report).
