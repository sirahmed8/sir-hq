# PLAN: SIR Portfolio
Status: planned, not started. Wave 2. Replaces: the GitHub profile README (sirahmed8) and scattered product pages. Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.

## 1. Mission and audience
Ahmed's personal website, the one link he can give anyone: who he builds for, every SIR product with its real status and link, selected work, and his public social accounts. No personal data (no phone, address, family, study details). It must be the best site in the portfolio: fast, accessible, Arabic and English, memorable design, truthful.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Portfolio` |
| GitHub (private) | `sirahmed8/sir-portfolio` |
| Firebase project / OAuth app name | `sir-portfolio` / "SIR Portfolio" |
| Cloudflare project | `sir-portfolio` (`sir-portfolio.pages.dev` until a domain is affordable) |
| App ids | `app.sir.sir-portfolio` (Android, iOS, Windows) |
| Platforms | Web on Cloudflare Pages (static first, tiny Worker for the contact form), later a custom domain |
| Money | none (free site); it also feeds sales pages of the products |

## 3. Why rebuild (evidence from the Phase 3 inventories)
- The current profile README has hype and unprovable claims ('8+ Production Applications', 'Sub-48h velocity', 'Recognized in Global AI Developer Ecosystems'), emoji headers, a 404 link and missing projects.
- There is no single place showing every product with honest status.

## 4. What to port from the old project
- Facts only from `_SIR/ops/PORTFOLIO.md` and each product's real status; social links from Ahmed's accounts (ByteVibeHQ and personal); screenshots taken from the real built products.

## 5. Screens and entities
**Screens:** Home (one clear sentence + the product wall), Products (cards with status: Live / Beta / In build / Planned), Product detail pages (what it does, who for, screenshots, link), Work and writing, Social links, Contact (form with spam protection, no email exposed), Legal (privacy, cookies), 404
**Entities:** Product(status, links, screenshots) read from a JSON file generated from the portfolio data; SocialLink; Post (optional, markdown)
**UX rules:** Every screen implements the 5 states: first use, loading skeleton matching the final layout, empty (one clear action), error (human message + Retry), populated (paginated or virtualized, fine with 1,000+ items). Arabic RTL (CSS logical properties) + English + Simplified Chinese + Hindi; light, dark, system and high-contrast themes; keyboard shortcuts; 320 px to 4K; zoom 80%-200%; spring motion with a reduced-motion path; WCAG 2.2 AA. Own colour seed and icon; the same Profile and Settings screens as every SIR product.

## 6. AI at the core
Optional small assistant that answers 'what does Ahmed build?' strictly from the site's own JSON (no invented facts), behind the server proxy with a daily quota.

## 7. Security checklist (all must pass)
- Owner/admin only from a server-verified Firebase ID token (JWKS) plus OWNER_EMAILS / OWNER_UIDS; email path needs email_verified; fail closed when unset (SIR Platform `owner-auth`).
- Every webhook: HMAC over the raw body with the timestamp inside the signed payload, timing-safe compare, idempotent activation (SIR Platform `signed-webhook`).
- No AI key, token or secret in any client bundle or git; AI only through the server proxy with per-user quota; owner unmetered (SIR Platform `ai-proxy`).
- Sessions in HttpOnly + Secure + SameSite=Strict cookies, never localStorage. Rate limits on login/register/reset. Input validated with zod at every boundary.
- Firestore/D1 rules deny by default, per-user/per-tenant claims, tested in the emulator. CSP with nonces, no unsafe-eval.
- gitleaks in CI and pre-commit; dependency audit; licence audit (no GPL/AGPL in proprietary code).
- No personal info anywhere (checked by a build-time scan for phone/email patterns); contact form via Worker with rate limit and honeypot; cookie banner only if analytics is used; no fake counters or testimonials.
- Status badges are generated from real product metadata, never typed by hand.

## 8. Milestones
### M0 Foundations
- [x] Create the folder from `plans/MASTER_REBUILD_PLAN.md` naming rules; `git init`, private GitHub repo `sirahmed8/sir-portfolio`.
- [x] `.sir/` file set (project.yml, CHECKPOINT.md, BOARD.md) from `standard/project-templates.md`; AGENTS/CLAUDE/GEMINI from `standard/agent-files.md`.
- [ ] New Firebase project `sir-portfolio` (Auth Google, Firestore) and Cloudflare project; OAuth app name "SIR Portfolio", logo, support email.
- [ ] Login brand check: sign in with Google in a real browser; the screen must not show a Firebase project id; screenshot saved in `.sir/evidence/`.
- [ ] CI: typecheck, lint, test, build, gitleaks on every push; first green run.
### M1 Core slice
- [ ] Static site with Home + Products wall from `content/products.json` generated from `_SIR/ops/PORTFOLIO.md`; Lighthouse 95+ on mobile; login not needed (no Firebase Auth), still own Cloudflare project.
### M2 Parity with the old project
- [ ] Product detail pages, Work page, Social links (real URLs), contact Worker, Arabic/English/Chinese/Hindi, themes.
- [ ] Design system from SIR ui kit; real screenshots of each product at 390 px and 1280 px.
### M3 Security, legal, billing
- [ ] Security checklist above is green with tests (forged cookie, unsigned webhook, unverified email, cross-tenant read all fail).
- [ ] Legal pack generated from what the product really collects; cookie banner with equal Reject; account and data deletion flow.
- [ ] Billing via SIR Platform with the "Subscriptions Launching Soon" fallback and email capture; activates when gateway keys are added.
### M4 AI
- [ ] Grounded 'ask about Ahmed's work' box with refusal tests for personal-info questions.
### M5 Quality sweep
- [ ] 5 states on every screen, 4 locales complete (no missing keys), 4 themes, a11y audit, Lighthouse budgets, e2e for the critical journeys, screenshots of each at 390 px and 1280 px in LTR and RTL.
### M6 Release and retirement
- [ ] Domain decision (free `.pages.dev` until a domain is affordable); replace the GitHub profile README with a short honest one that links here; submit sitemap.

## 9. Risks and open decisions
- Showing products that are not ready: statuses must be honest ('In build').
- Privacy: nothing about Habiba, family, study or address; AHome/SIR Home is never listed.

## 10. How any chat continues this project
Read this file, then `.sir/CHECKPOINT.md`, then work the first unchecked box in section 8. Tick boxes only with evidence (command output or screenshot path). After each box update the checkpoint and commit. Never ask Ahmed; if blocked by a permission, write the single command in `NEXT.md` and continue with the next box.
