# PLAN: SIR Platform (Wave 7 in MAIN_PLAN, started early; internal kit)
Audited 2026-11-10. Internal shared kit, not sold, not listed. It is the one place for pieces that two or more products need. Other plans point here instead of rebuilding.
Order note (conflict reported in the audit): MAIN_PLAN and WAVE_STUDY say "Platform last", but the folder already holds a first kit and other plans depend on it. Default decision until the manager rules: Platform keeps only the small, tested packages listed in section 3; each product builds its own copy behind the same package name and interface (`packages/<name>` in the product), and Platform becomes the single source when two products have copies that pass the same test file. No product waits for Platform.

## 1. Purpose (plain words)
A set of tested building blocks that every SIR website and app can use: owner login that cannot be faked, signed payment webhooks, a safe AI gateway with quotas, a "Subscriptions launching soon" billing fallback, legal pages generated from what a product really collects, and one shared look (colors, motion, Arabic right-to-left layout). Fix a defect once, every product gets the fix.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Platform` |
| GitHub (private) | `sirahmed8/sir-platform` |
| Layout | npm/pnpm workspace (`package.json` workspaces and `pnpm-workspace.yaml` both exist; pick pnpm, remove the other, task 2) |
| Packages today | `@sir/ui`, `@sir/styles`, `@sir/hooks`, `@sir/payments` (`packages/`) |
| Packages planned | `@sir/owner-auth`, `@sir/signed-webhook` (split out of payments), `@sir/ai-proxy`, `@sir/billing-fallback`, `@sir/legal-pack`, `@sir/i18n`, `@sir/telegram` (thin wrapper of the shared sender), CLI `sir-kit` |
| Platforms | TypeScript packages for Workers and Node, a docs/gallery site (web, PWA). Windows/Android/iOS/macOS/TV: skipped, a library |
| Money | none. Billing package is code for other products |

## 3. Current state
Claimed in `.sir/CHECKPOINT.md` (2026-11-10): PLAT-01 to PLAT-05 done (Spring island, active tab bar, RTL stylesheet, visual viewport hook, Paymob/Fawry test modal with HMAC webhook verifier), GitHub Actions pipeline added. PORTFOLIO.md: 29 tasks planned, 9 commits.
Verified today: `node tests/unit/test-platform-suite.mjs` = 5 passed, 0 failed; `python scripts/lint_design_tokens.py` = pass on 15 files. These tests are file-based checks; **typecheck, build and a React render test were not run and not shown to exist**, so the TSX components are built, unverified.
Gaps seen in files: `packages/payments/src/PaymobModal.tsx` is 328 lines (limit 300); no `owner-auth`, `ai-proxy`, `legal-pack`, `i18n`, `sir-kit`; the webhook verifier has a 5 minute replay window but no idempotency store interface (planned in the old plan).
Not started: everything in "Packages planned", the docs/gallery site, publishing (private registry or git dependency), consumer integration in a real product.

## 4. Security rules for the kit
1. `owner-auth`: server-verified ID token (JWKS) plus allow-list from `OWNER_EMAILS` / `OWNER_UIDS`; `email_verified` required; fail closed when unset. Negative tests: forged, expired, wrong issuer, unverified email, tampered cookie.
2. `signed-webhook`: HMAC over the raw body with the timestamp inside the signed payload, timing-safe compare, replay window, idempotency interface. Negative tests: tampered body, old timestamp, replay.
3. `ai-proxy`: no key in any client bundle; per-user daily quota; owner unmetered; provider chain with failover; private-data routing flag sends only to local models. Tests: quota exhaustion, provider 429 failover, private flag never calls an outside provider.
4. Sessions in HttpOnly, Secure, SameSite=Strict cookies; never localStorage (lint rule scans for it).
5. gitleaks and dependency/licence audit in CI; no GPL/AGPL.
6. Every package ships tests that run in a Workers-like runtime (no Node-only APIs) as well as Node.

## 5. What Platform provides to each plan (single list used by all plans)
| Need | Package | Status |
|---|---|---|
| Owner admin login and unmetered owner | `owner-auth` | not started |
| Paid plans, EGP, "Launching soon" + lead capture, webhooks | `billing-fallback`, `signed-webhook`, `payments` | payments modal built, unverified; rest not started |
| AI with fallback, quota, privacy routing | `ai-proxy` | not started (idea source: SIR AI) |
| Look and motion, tab bar, RTL | `ui`, `styles`, `hooks` | built, unverified |
| Legal pages, cookie banner with equal Reject, deletion flow | `legal-pack` | not started |
| Arabic/English strings, plural, numerals | `i18n` | not started |
| Telegram reports and approvals | `telegram` (wraps `_SIR/scripts/deliver/`) | wrapper not started; sender verified 6/6 |
| Project scaffold, CI, checks | `sir-kit` CLI | not started |

## 6. Screens
Only the docs/gallery site: component gallery with RTL/LTR and light/dark toggles, token tables, package READMEs with copy-paste examples. Five states where data loads. 320 px to 4K.

## 7. AI and assistant
`ai-proxy` only. Eval set: 20 prompts per language checking refusal of out-of-scope and graded-work requests, quota messages and failover. Support-assistant prompt template grounded in a product's docs folder (used by Business, Hagoozat, Obour Hub, Controller).

## 8. Operations
CI on every push (typecheck, lint, tests, gitleaks, token lint). Changelog from commits. Weekly dependency update with tests. Telegram weekly line via the shared sender.

## 9. Milestones with exit checks
| M | Goal | Exit check |
|---|---|---|
| M0 | Honest base | `tsc --noEmit` and build pass for all 4 packages; one workspace manager; files under 300 lines; CI green URL |
| M1 | Security trio | `owner-auth`, `signed-webhook`, `ai-proxy` each with 10+ negative tests passing |
| M2 | Billing and legal | `billing-fallback` renders "launching soon" without keys (test); `legal-pack` generates 5 pages from a sample `data-inventory.yml` |
| M3 | i18n and CLI | missing-key test fails the build; `sir-kit new` scaffolds a project that passes its own verify |
| M4 | First consumer | one real product imports the kit and passes its tests (record which) |
| M5 | Quality | gallery screenshots 390 and 1280, LTR and RTL, light and dark; a11y check |
| M6 | Release | tag stays 1.0.0 (version rule); packages consumed by git dependency; changelog present |

## 10. Next 10 tasks (each under 2 hours)
1. Add `tsc --noEmit` per package and a root `typecheck` script; fix errors. Files: `packages/*/tsconfig.json`, `package.json`. Check: `npm run typecheck` exit 0.
2. Pick pnpm: delete the duplicate workspace config choice (keep `pnpm-workspace.yaml`, drop `workspaces` or the reverse) and document it. Check: `pnpm install` works, README says which.
3. Split `PaymobModal.tsx` (328 lines) into modal, formatter and fallback view. Files: `packages/payments/src/`. Check: each file under 300 lines; test suite still 5 passed.
4. Move `webhookVerifier.ts` into `packages/signed-webhook` and add idempotency interface plus 10 negative tests. Check: `node --test` green; replay test fails the second call.
5. `packages/owner-auth`: JWKS verify with `jose`, allow-list, fail-closed, 12 negative tests. Check: tests green under Node and a Workers-like runtime (miniflare or `wrangler dev --test`).
6. React render tests for `SpringIsland` and `ActiveTabBar` (vitest + testing-library): keyboard, reduced motion. Check: tests green.
7. `packages/billing-fallback`: component and hook reading `PAYMENTS_ENABLED` env; "Subscriptions launching soon" (Arabic and English) with lead capture interface. Check: render test with and without keys.
8. `packages/legal-pack` skeleton: `data-inventory.yml` schema (zod) plus privacy page generator and test. Check: sample inventory produces a page listing exactly the declared data; each page carries "AI-drafted, to be reviewed by a qualified lawyer before paid launch".
9. `packages/i18n`: ar/en dictionaries, missing-key test, Arabic-Indic numeral option. Check: test fails when a key is missing in one locale.
10. CI: run typecheck, tests, token lint, gitleaks; record the Actions URL. Files: `.github/workflows/`. Check: green run URL in checkpoint.

## 11. Risks and open questions (defaults)
- Over-building: default is ship the three security packages first, the rest only when two products need them.
- Premature extraction before products exist: default is write each package against its own test file so a product copy can be swapped in.
- Workers runtime limits: default is test in a Workers-like runtime from the first package.
- Payment provider terms and API shapes for Paymob and Fawry: "(unsourced, verify)" at build time from their official docs; use test modes only.

## 12. Only the owner can do
Create the real Paymob, Fawry, Stripe or LemonSqueezy accounts and paste keys in one `.env`; buy domains; create Firebase and Cloudflare logins; legal review by a lawyer before paid launch.

## 13. Market-grade note
Competitors (Clerk, Auth0, Stripe Billing, Lemon Squeezy) are in `plans/competitors/sir-platform.md`; price claims there need links or "(unsourced, verify)". Internal kit: no visibility or marketing work, but its docs site stays `noindex`.
