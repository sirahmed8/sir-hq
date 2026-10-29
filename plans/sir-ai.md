# PLAN: SIR AI
Status: planned, not started. Wave 3. Replaces: SIR AI v1. Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.

## 0. THIS IS A MERGE PROJECT (read first)
The old projects below were physically moved into this folder (`legacy/`, or `materials/` for study) with their complete code, git history, structure and assets. Many projects with many features are being merged into this ONE new product so one agent can finish it end to end.
- SIR AI (v1)
Your job: read `_SIR/ops/inventory/` for each source, then port everything of value into the new clean structure (apps/, packages/) with professional, high quality code and clean architecture; fully set up and configured; tested; deployed to Cloudflare; pushed to the private repo; in production mode (real env vars by name, real domain or pages.dev, monitoring, backups). Never edit `legacy/` except to read. When M6 is complete, move every `legacy/*` folder to `D:/Projects/old projects/` and record it in the checkpoint.

## 1. Mission and audience
A voice and vision personal assistant that runs on Ahmed's PC with local models first, and the home of the AI gateway concept that SIR Platform's ai-proxy extracts. Audience: Ahmed first, then power users.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR AI` |
| GitHub (private) | `sirahmed8/sir-ai` |
| Firebase project / OAuth app name | `sir-ai-assistant` / "SIR AI" |
| Cloudflare project | `sir-ai` (`sir-ai.pages.dev` until a domain is affordable) |
| App ids | `app.sir.sir-ai` (Android, iOS, Windows) |
| Platforms | Windows desktop + local web UI; Python core |
| Money | Free local use; Pro for cloud models and sync (EGP); Launching Soon fallback |

## 3. Why rebuild (evidence from the Phase 3 inventories)
- Session tokens in localStorage, client-trusted owner paths (stopgap merged), hard-coded OwnerManager identities, a mock dev token bypass, privacy page claiming SOC 2/ISO, a 73 MB model blob tracked in git, a literal Firebase key in several JS files.

## 4. What to port from the old project
- Core agents, voice pipeline, telegram bridge ideas, 259 tests (keep).

## 5. Screens and entities
**Screens:** Chat, Voice mode, Camera/vision, Tasks, Memory (what it remembers, with delete), Settings/providers, Owner dashboard, Help
**Entities:** Conversation, Message, Memory, Tool, Provider, Quota, User
**UX rules:** Every screen implements the 5 states: first use, loading skeleton matching the final layout, empty (one clear action), error (human message + Retry), populated (paginated or virtualized, fine with 1,000+ items). Arabic RTL (CSS logical properties) + English + Simplified Chinese + Hindi; light, dark, system and high-contrast themes; keyboard shortcuts; 320 px to 4K; zoom 80%-200%; spring motion with a reduced-motion path; WCAG 2.2 AA. Own colour seed and icon; the same Profile and Settings screens as every SIR product.

## 6. AI at the core
This product is the AI: provider chain with local-first routing; private data never goes to outside providers.

## 7. Security checklist (all must pass)
- Owner/admin only from a server-verified Firebase ID token (JWKS) plus OWNER_EMAILS / OWNER_UIDS; email path needs email_verified; fail closed when unset (SIR Platform `owner-auth`).
- Every webhook: HMAC over the raw body with the timestamp inside the signed payload, timing-safe compare, idempotent activation (SIR Platform `signed-webhook`).
- No AI key, token or secret in any client bundle or git; AI only through the server proxy with per-user quota; owner unmetered (SIR Platform `ai-proxy`).
- Sessions in HttpOnly + Secure + SameSite=Strict cookies, never localStorage. Rate limits on login/register/reset. Input validated with zod at every boundary.
- Firestore/D1 rules deny by default, per-user/per-tenant claims, tested in the emulator. CSP with nonces, no unsafe-eval.
- gitleaks in CI and pre-commit; dependency audit; licence audit (no GPL/AGPL in proprietary code).
- Cookie sessions only; owner by verified claims; mock tokens removed from production; model blobs out of git (download script with checksum).

## 8. Milestones
### M0 Foundations
- [x] Create the folder from `plans/MASTER_REBUILD_PLAN.md` naming rules; `git init`, private GitHub repo `sirahmed8/sir-ai`.
- [ ] `.sir/` file set (project.yml, CHECKPOINT.md, BOARD.md) from `standard/project-templates.md`; AGENTS/CLAUDE/GEMINI from `standard/agent-files.md`.
- [ ] New Firebase project `sir-ai-assistant` (Auth Google, Firestore) and Cloudflare project; OAuth app name "SIR AI", logo, support email.
- [ ] Login brand check: sign in with Google in a real browser; the screen must not show a Firebase project id; screenshot saved in `.sir/evidence/`.
- [ ] CI: typecheck, lint, test, build, gitleaks on every push; first green run.
### M1 Core slice
- [ ] Local chat with Ollama, provider chain with failover, memory with delete, tests.
### M2 Parity with the old project
- [ ] Voice, vision, tool plugins; owner dashboard with real token/cost numbers.
### M3 Security, legal, billing
- [ ] Security checklist above is green with tests (forged cookie, unsigned webhook, unverified email, cross-tenant read all fail).
- [ ] Legal pack generated from what the product really collects; cookie banner with equal Reject; account and data deletion flow.
- [ ] Billing via SIR Platform with the "Subscriptions Launching Soon" fallback and email capture; activates when gateway keys are added.
### M4 AI
- [ ] Eval set (Arabic/English) for routing, refusal and tool-use accuracy.
### M5 Quality sweep
- [ ] 5 states on every screen, 4 locales complete (no missing keys), 4 themes, a11y audit, Lighthouse budgets, e2e for the critical journeys, screenshots of each at 390 px and 1280 px in LTR and RTL.
### M6 Release and retirement
- [ ] Installer, update channel, retire v1; remove the leaked key literal from history by rewrite after rotation.

## 9. Risks and open decisions
- Hardware limits (RTX 4050, 24 GB RAM): small models locally, cloud only for non-private text.

## 10. How any chat continues this project
Read this file, then `.sir/CHECKPOINT.md`, then work the first unchecked box in section 8. Tick boxes only with evidence (command output or screenshot path). After each box update the checkpoint and commit. Never ask Ahmed; if blocked by a permission, write the single command in `NEXT.md` and continue with the next box.
