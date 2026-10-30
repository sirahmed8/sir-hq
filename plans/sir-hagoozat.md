# PLAN: SIR Hagoozat
Status: planned, not started. Wave 3. Replaces: Hagoozat Elite (Merged sites), 11Players, EGFootball5. Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.

## 0. THIS IS A MERGE PROJECT (read first)
The old projects below were physically moved into this folder (`legacy/`, or `materials/` for study) with their complete code, git history, structure and assets. Many projects with many features are being merged into this ONE new product so one agent can finish it end to end.
- Hagoozat Elite
- 11Players
- EGFootball5
Your job: read `_SIR/ops/inventory/` for each source, then port everything of value into the new clean structure (apps/, packages/) with professional, high quality code and clean architecture; fully set up and configured; tested; deployed to Cloudflare; pushed to the private repo; in production mode (real env vars by name, real domain or pages.dev, monitoring, backups). Never edit `legacy/` except to read. When M6 is complete, move every `legacy/*` folder to `D:/Projects/old projects/` and record it in the checkpoint.

## 1. Mission and audience
Five-a-side football in Egypt: book a pitch, split the cost, balance squads, rate players, run matches and communities. Audience: players, captains and pitch owners.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Hagoozat` |
| GitHub (private) | `sirahmed8/sir-hagoozat` |
| Firebase project / OAuth app name | `sir-hagoozat` / "SIR Hagoozat" |
| Cloudflare project | `sir-hagoozat` (`sir-hagoozat.pages.dev` until a domain is affordable) |
| App ids | `app.sir.sir-hagoozat` (Android, iOS, Windows) |
| Platforms | Web + PWA (Cloudflare), Android/iOS (Expo), owner dashboard web |
| Money | Free for players; Pro 59 EGP/month (priority booking, stats, FUT cards, no ads); pitch owners pay a monthly fee; Launching Soon fallback until Paymob/Fawry keys |

## 3. Why rebuild (evidence from the Phase 3 inventories)
- Three apps with overlapping code; the merge in `Hagoozat Elite` has 29 pages vs 55 and 36 in the originals.
- Critical `dev_signature` payment bypass (stopgap PR merged separately), client-side owner gate, 62 files over 300 lines in 11Players, API routes dead on static hosting in EGFootball5.
- Fake players generator in 11Players admin, placeholder Firebase config.

## 4. What to port from the old project
- From EGFootball5: 15-minute slot lock, deposit receipt upload + verification queue, Hagaz lobbies, jersey designer, owner dashboards, achievements/XP, notifications, support tickets, Cloud Functions logic.
- From 11Players: AI layer, captain draft room, communities, global ranking, owner analytics, pro pass.
- From Hagoozat Elite: pitches, players, tactics, split-bill, VAR voting, data deletion, unsubscribe.

## 5. Screens and entities
**Screens:** Landing, Sign in, Onboarding, Home, Find pitch, Pitch page, Booking wizard (linear stepper), Deposit/payment, My bookings, Match lobby, Squad balancer, Draft room, Live match, Player card, Rankings, Communities + chat, Notifications, Pro pass, Owner/pitch dashboard, Support, Settings, Legal
**Entities:** User, PlayerCard, Pitch, Slot, Booking, Deposit, Match, Squad, Community, Message, Rating, Notification, Subscription, SupportTicket
**UX rules:** Every screen implements the 5 states: first use, loading skeleton matching the final layout, empty (one clear action), error (human message + Retry), populated (paginated or virtualized, fine with 1,000+ items). Arabic RTL (CSS logical properties) + English + Simplified Chinese + Hindi; light, dark, system and high-contrast themes; keyboard shortcuts; 320 px to 4K; zoom 80%-200%; spring motion with a reduced-motion path; WCAG 2.2 AA. Own colour seed and icon; the same Profile and Settings screens as every SIR product.

## 6. AI at the core
Flagship: squad balancer and position coach (explains what the player must do in each situation). Assistant: booking help and rules Q&A grounded in the app docs. Server proxy only.

## 7. Security checklist (all must pass)
- Owner/admin only from a server-verified Firebase ID token (JWKS) plus OWNER_EMAILS / OWNER_UIDS; email path needs email_verified; fail closed when unset (SIR Platform `owner-auth`).
- Every webhook: HMAC over the raw body with the timestamp inside the signed payload, timing-safe compare, idempotent activation (SIR Platform `signed-webhook`).
- No AI key, token or secret in any client bundle or git; AI only through the server proxy with per-user quota; owner unmetered (SIR Platform `ai-proxy`).
- Sessions in HttpOnly + Secure + SameSite=Strict cookies, never localStorage. Rate limits on login/register/reset. Input validated with zod at every boundary.
- Firestore/D1 rules deny by default, per-user/per-tenant claims, tested in the emulator. CSP with nonces, no unsafe-eval.
- gitleaks in CI and pre-commit; dependency audit; licence audit (no GPL/AGPL in proprietary code).
- Slot booking and deposits are transactions with idempotency keys; double-booking test with parallel requests.
- Receipt images validated and stored privately.

## 8. Milestones
### M0 Foundations
- [x] Create the folder from `plans/MASTER_REBUILD_PLAN.md` naming rules; `git init`, private GitHub repo `sirahmed8/sir-hagoozat`.
- [x] `.sir/` file set (project.yml, CHECKPOINT.md, BOARD.md) from `standard/project-templates.md`; AGENTS/CLAUDE/GEMINI from `standard/agent-files.md`.
- [ ] New Firebase project `sir-hagoozat` (Auth Google, Firestore) and Cloudflare project; OAuth app name "SIR Hagoozat", logo, support email.
- [ ] Login brand check: sign in with Google in a real browser; the screen must not show a Firebase project id; screenshot saved in `.sir/evidence/`.
- [ ] CI: typecheck, lint, test, build, gitleaks on every push; first green run.
### M1 Core slice
- [ ] Pitch list + pitch page from real data, booking wizard with slot lock and transaction, Google sign-in brand check.
### M2 Parity with the old project
- [ ] Deposit upload + verification queue, matches and lobbies, squad balancer, player cards and ratings.
- [ ] Communities + chat, notifications, achievements, owner dashboard with real revenue/booking counts.
- [ ] Feature-parity checklist ticked against `ops/inventory/Merged-sites.md` route lists.
### M3 Security, legal, billing
- [ ] Security checklist above is green with tests (forged cookie, unsigned webhook, unverified email, cross-tenant read all fail).
- [ ] Legal pack generated from what the product really collects; cookie banner with equal Reject; account and data deletion flow.
- [ ] Billing via SIR Platform with the "Subscriptions Launching Soon" fallback and email capture; activates when gateway keys are added.
### M4 AI
- [ ] Squad balancer explanation, position coach, support assistant; eval sets in Arabic and English.
### M5 Quality sweep
- [ ] 5 states on every screen, 4 locales complete (no missing keys), 4 themes, a11y audit, Lighthouse budgets, e2e for the critical journeys, screenshots of each at 390 px and 1280 px in LTR and RTL.
### M6 Release and retirement
- [ ] Data import from the three Firestore projects with dry run and counts; 301 redirects from `an-11-players.web.app`, `egfootball5.web.app`, `hagoozat-elite.web.app`; move old folders (already in `old projects`) to archive repos.

## 9. Risks and open decisions
- Three user bases with duplicate accounts: merge by verified email, never by display name.
- Real payments need a gateway account (owner); fallback until then.

## 10. How any chat continues this project
Read this file, then `.sir/CHECKPOINT.md`, then work the first unchecked box in section 8. Tick boxes only with evidence (command output or screenshot path). After each box update the checkpoint and commit. Never ask Ahmed; if blocked by a permission, write the single command in `NEXT.md` and continue with the next box.
