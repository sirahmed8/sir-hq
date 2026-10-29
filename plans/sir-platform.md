# PLAN: SIR Platform
Status: planned, not started. Wave 1. Replaces: nothing (new shared kit). Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.

## 1. Mission and audience
The shared `@sir/*` kit that every product imports, so each defect found in 16 inventories is fixed once. Used by Ahmed's agents and every SIR product; not sold.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Platform` |
| GitHub (private) | `sirahmed8/sir-platform` |
| Firebase project / OAuth app name | `sir-platform-dev` / "SIR Platform" |
| Cloudflare project | `sir-platform` (`sir-platform.pages.dev` until a domain is affordable) |
| App ids | `app.sir.sir-platform` (Android, iOS, Windows) |
| Platforms | TypeScript packages (npm workspace), Python helper for SIR AI, CLI `sir-kit` |
| Money | none (internal) |

## 3. Why rebuild (evidence from the Phase 3 inventories)
- Client-side owner gates, unsigned webhooks, client AI keys, fake login/payment/AI screens and unprovable SOC 2/ISO text repeat in nearly every project.
- The five Wave 0 fixes already exist as reviewed references; they must become packages, not copies.

## 4. What to port from the old project
- owner-auth: `SIR Mods for GTA V/web-portal/lib/admin/*`, `SIR AI/core/security/owner_access.py`.
- signed-webhook: `Hagoozat Elite/src/lib/server/webhookSignature.ts` (put the timestamp inside the signed payload).
- ai-proxy and chat guard: `SIR Optimizer/PulseTools-Web/src/lib/chatGuard.ts`, `entitlements.ts`.

## 5. Screens and entities
**Screens:** none (libraries); `docs` site with live examples
**Entities:** Plan, Entitlement, WebhookEvent, QuotaCounter, LeadEmail, LegalDocument
**UX rules:** Every screen implements the 5 states: first use, loading skeleton matching the final layout, empty (one clear action), error (human message + Retry), populated (paginated or virtualized, fine with 1,000+ items). Arabic RTL (CSS logical properties) + English + Simplified Chinese + Hindi; light, dark, system and high-contrast themes; keyboard shortcuts; 320 px to 4K; zoom 80%-200%; spring motion with a reduced-motion path; WCAG 2.2 AA. Own colour seed and icon; the same Profile and Settings screens as every SIR product.

## 6. AI at the core
`ai-proxy` package: provider chain with automatic failover (Gemini, OpenRouter free models, Groq, local Ollama for private data), per-user daily quota, owner unmetered, prompt/eval sets, privacy routing (module 10).

## 7. Security checklist (all must pass)
- Owner/admin only from a server-verified Firebase ID token (JWKS) plus OWNER_EMAILS / OWNER_UIDS; email path needs email_verified; fail closed when unset (SIR Platform `owner-auth`).
- Every webhook: HMAC over the raw body with the timestamp inside the signed payload, timing-safe compare, idempotent activation (SIR Platform `signed-webhook`).
- No AI key, token or secret in any client bundle or git; AI only through the server proxy with per-user quota; owner unmetered (SIR Platform `ai-proxy`).
- Sessions in HttpOnly + Secure + SameSite=Strict cookies, never localStorage. Rate limits on login/register/reset. Input validated with zod at every boundary.
- Firestore/D1 rules deny by default, per-user/per-tenant claims, tested in the emulator. CSP with nonces, no unsafe-eval.
- gitleaks in CI and pre-commit; dependency audit; licence audit (no GPL/AGPL in proprietary code).
- The kit is the security boundary: every package ships negative tests (forged, expired, tampered, replayed, unverified, cross-tenant).

## 8. Milestones
### M0 Foundations
- [ ] Create the folder from `plans/MASTER_REBUILD_PLAN.md` naming rules; `git init`, private GitHub repo `sirahmed8/sir-platform`.
- [ ] `.sir/` file set (project.yml, CHECKPOINT.md, BOARD.md) from `standard/project-templates.md`; AGENTS/CLAUDE/GEMINI from `standard/agent-files.md`.
- [ ] New Firebase project `sir-platform-dev` (Auth Google, Firestore) and Cloudflare project; OAuth app name "SIR Platform", logo, support email.
- [ ] Login brand check: sign in with Google in a real browser; the screen must not show a Firebase project id; screenshot saved in `.sir/evidence/`.
- [ ] CI: typecheck, lint, test, build, gitleaks on every push; first green run.
### M1 Core slice
- [ ] `owner-auth` package (JWKS verify with `jose`, allow-list, cookie session) with 12+ negative tests, usable from Workers and Node.
- [ ] `signed-webhook` package with timestamp-in-payload, replay window, idempotency store interface, adapters for Paymob, Fawry, Stripe.
### M2 Parity with the old project
- [ ] `ai-proxy` with quota store (Firestore or D1) and the provider chain; `billing` with the Launching Soon fallback and lead capture.
- [ ] `legal-pack` generator (privacy, terms, refunds, cookies, DPA, sub-processors) from a `data-inventory.yml` per product; `ui` kit with tokens, 5-state components, RTL, themes.
- [ ] `project-kit` CLI: scaffold folder, `.sir/` files, CI workflow, gitleaks, Firebase + Cloudflare checklist.
### M3 Security, legal, billing
- [ ] Security checklist above is green with tests (forged cookie, unsigned webhook, unverified email, cross-tenant read all fail).
- [ ] Legal pack generated from what the product really collects; cookie banner with equal Reject; account and data deletion flow.
- [ ] Billing via SIR Platform with the "Subscriptions Launching Soon" fallback and email capture; activates when gateway keys are added.
### M4 AI
- [ ] Prompt and eval sets for the support assistant grounded in each product's docs; refusal tests for out-of-scope and graded-work requests.
### M5 Quality sweep
- [ ] 5 states on every screen, 4 locales complete (no missing keys), 4 themes, a11y audit, Lighthouse budgets, e2e for the critical journeys, screenshots of each at 390 px and 1280 px in LTR and RTL.
### M6 Release and retirement
- [ ] Version 1.0 tag, private npm registry (GitHub Packages) or git dependency, changelog generated from commits.
- [ ] Obour Hub consumes it end to end; any gap found there is fixed upstream.

## 9. Risks and open decisions
- Over-building: ship the three security packages first, the rest as products need them.
- Cloudflare Workers runtime limits (no Node-only APIs): test every package in a Workers runtime.

## 10. How any chat continues this project
Read this file, then `.sir/CHECKPOINT.md`, then work the first unchecked box in section 8. Tick boxes only with evidence (command output or screenshot path). After each box update the checkpoint and commit. Never ask Ahmed; if blocked by a permission, write the single command in `NEXT.md` and continue with the next box.
