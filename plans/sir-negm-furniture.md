# PLAN: SIR Negm Furniture
Status: planned, not started. Wave 3. Replaces: Negm Furniture (client brand). Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.

## 0. THIS IS A MERGE PROJECT (read first)
The old projects below were physically moved into this folder (`legacy/`, or `materials/` for study) with their complete code, git history, structure and assets. Many projects with many features are being merged into this ONE new product so one agent can finish it end to end.
- Negm Furniture
Your job: read `_SIR/ops/inventory/` for each source, then port everything of value into the new clean structure (apps/, packages/) with professional, high quality code and clean architecture; fully set up and configured; tested; deployed to Cloudflare; pushed to the private repo; in production mode (real env vars by name, real domain or pages.dev, monitoring, backups). Never edit `legacy/` except to read. When M6 is complete, move every `legacy/*` folder to `D:/Projects/old projects/` and record it in the checkpoint.

## 1. Mission and audience
Bilingual showroom catalog and lead capture for Negm Furniture EG (Ain Shams and Roxy showrooms). Public brand stays Negm Furniture; folder, repo and cloud projects use the SIR prefix.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Negm Furniture` |
| GitHub (private) | `sirahmed8/sir-negm-furniture` |
| Firebase project / OAuth app name | `sir-negm-furniture` / "SIR Negm Furniture" |
| Cloudflare project | `sir-negm-furniture` (`sir-negm-furniture.pages.dev` until a domain is affordable) |
| App ids | `app.sir.sir-negm-furniture` (Android, iOS, Windows) |
| Platforms | Web (static + Workers API) on Cloudflare |
| Money | client service; site itself free |

## 3. Why rebuild (evidence from the Phase 3 inventories)
- Fake login user, fabricated ratings (4.95 / 38 reviews) and '+285K' followers, simulated uploads, client-only admin, hosted inside SIR's Firebase project.

## 4. What to port from the old project
- Catalog data, 158 passing tests, showroom pages, decor AI rule engine.

## 5. Screens and entities
**Screens:** Home, Catalog, Product, Showrooms, Inquiry form, Admin catalog, Legal
**Entities:** Product, Category, Showroom, Inquiry, AdminUser
**UX rules:** Every screen implements the 5 states: first use, loading skeleton matching the final layout, empty (one clear action), error (human message + Retry), populated (paginated or virtualized, fine with 1,000+ items). Arabic RTL (CSS logical properties) + English + Simplified Chinese + Hindi; light, dark, system and high-contrast themes; keyboard shortcuts; 320 px to 4K; zoom 80%-200%; spring motion with a reduced-motion path; WCAG 2.2 AA. Own colour seed and icon; the same Profile and Settings screens as every SIR product.

## 6. AI at the core
Decor assistant: server route with quota; offline rule engine as fallback.

## 7. Security checklist (all must pass)
- Owner/admin only from a server-verified Firebase ID token (JWKS) plus OWNER_EMAILS / OWNER_UIDS; email path needs email_verified; fail closed when unset (SIR Platform `owner-auth`).
- Every webhook: HMAC over the raw body with the timestamp inside the signed payload, timing-safe compare, idempotent activation (SIR Platform `signed-webhook`).
- No AI key, token or secret in any client bundle or git; AI only through the server proxy with per-user quota; owner unmetered (SIR Platform `ai-proxy`).
- Sessions in HttpOnly + Secure + SameSite=Strict cookies, never localStorage. Rate limits on login/register/reset. Input validated with zod at every boundary.
- Firestore/D1 rules deny by default, per-user/per-tenant claims, tested in the emulator. CSP with nonces, no unsafe-eval.
- gitleaks in CI and pre-commit; dependency audit; licence audit (no GPL/AGPL in proprietary code).
- Admin by custom claims; no fabricated social proof; image licences confirmed with the client; client owns the Firebase/Cloudflare projects at handover.

## 8. Milestones
### M0 Foundations
- [x] Create the folder from `plans/MASTER_REBUILD_PLAN.md` naming rules; `git init`, private GitHub repo `sirahmed8/sir-negm-furniture` (the delivery channel for the friend).
- [x] `.sir/` file set (project.yml, CHECKPOINT.md, BOARD.md) from `standard/project-templates.md`; AGENTS/CLAUDE/GEMINI from `standard/agent-files.md`.
- [ ] Handoff pack in the repo: `HANDOFF.md`, `docs/CLIENT_SETUP.md`, `FRIEND_AGENT_PROMPT.md`, `docs/AGENT_PLAYBOOK.md` (the friend's AI agent works in Antigravity with Gemini high, so write short explicit steps, checklists and exact commands).
- [ ] No Firebase, Cloudflare or GitHub organization is created by Ahmed for this project: the friend creates his own accounts with the agent's help.
- [ ] CI: typecheck, lint, test, build, gitleaks on every push; first green run.
### M1 Core slice
- [ ] Catalog from real client-supplied data; inquiry form stored in Firestore with validation.
### M2 Parity with the old project
- [ ] Admin CRUD with real Cloudinary/R2 upload; SEO and structured data.
### M3 Security and legal
- [ ] Lead form protections (rate limit, honeypot, no email exposed), privacy page and cookie consent that match what the site really collects; security checklist green with tests.
### M4 AI
- [ ] Decor suggestions with citations to real catalog items only.
### M5 Quality sweep
- [ ] 5 states on every screen, ar/en with RTL, 4 themes, a11y audit, Lighthouse budgets, e2e for the critical journeys, screenshots at 390 px and 1280 px.
### M6 Handoff
- [ ] The friend pulls the repo, follows `docs/CLIENT_SETUP.md` with his agent, and the site is live on his own Cloudflare account; Ahmed's repo access is kept or removed as the friend decides.
- [ ] Handover checklist to the client; domain `negm-furniture.eg` pointed at Cloudflare.

## 9. Risks and open decisions
- Client approvals for photos and contact details.

## 10. How any chat continues this project
Read this file, then `.sir/CHECKPOINT.md`, then work the first unchecked box in section 8. Tick boxes only with evidence (command output or screenshot path). After each box update the checkpoint and commit. Never ask Ahmed; if blocked by a permission, write the single command in `NEXT.md` and continue with the next box.
