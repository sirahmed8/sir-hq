# Inventory: Merged sites "Hagoozat Elite" (2026-10-29, scout, read-only; no install, build or tests)

**What:** pitch booking (Fawry/InstaPay/Vodafone), PES squad balancing, FUT cards, VAR voting, broadcaster, ceremonies, for Egyptian 5-a-side players and pitch owners. README title and llms.txt both say "Hagoozat Elite".
**Live (not checked):** hagoozat-elite.web.app; 11-players.vercel.app redirect (public/index.html).
**Stack:** Next ^16.2.11, React 19, TS, Tailwind 4, Firebase 12, next-intl 4, zustand 5, vitest 4. **Repo:** `sirahmed8/merged-sites`, main, 21 commits, clean. **CI:** typecheck, lint, test, build. 50 test files; README claim 281/281 not verified.
**Data/auth:** Firestore + rules (32 `request.auth` refs), Google sign-in, Cloudinary. Admin gate client-side (`useAuth().isOwner`, OwnerFloatingBar); `src/proxy.ts` is only an in-memory rate limiter. **AI:** none (11Players and EGFootball5 both have Gemini + OpenRouter).
**Legal:** /privacy /terms /cookies exist; no sub-processors, DPA, AI-training clause, arbitration or EGP pricing text; /refunds is one line; cookie banner has Reject. **Platforms:** web/PWA only.
**Desktop `Hagoozat Elite\`:** 2 shortcuts (start/stop dev server, `launch-dev.vbs` / `stop-dev.vbs` in `Merged sites\scripts`) + `icon.ico`: a launcher for this project, not separate code.

## Is the merge complete? No. Feature parity (route paths)
- Merged: 29 pages, 7 API routes.
- Missing vs 11Players (55 pages): achievements, analytics, announcements, chat, communities, community-chat/settings, derby, draft, global, guide, inbox, match/draft, match/scouting, match/split-bill, matches, notifications, onboarding, owner/*, pro-pass, scouting, settings, split-bill, support, stats, tos, users, [username]; plus the whole AI layer.
- Missing vs EGFootball5 (36): achievements, announcements, book, challenges, checkout, communities, community-chat, guide, home, jersey-designer, live-stream, matches, notifications, onboarding, owner/*, profile, subscription, support; plus slot lock, deposit verification queue, Cloud Functions.
- Merged-only: pitches, players, tactics, community/[id], match/[id], unsubscribe, profile/data-deletion.
- Some gaps have components but no route (chat, scouting, gamification, xp, newspaper).
**Decision:** do NOT move 11Players or EGFootball5 to `old projects\` yet; finish parity first (Phase 5).

## Scores (0-5)
Architecture 2 (35 files over 300 lines, admin page 1,509) · Code quality 2 (dead FirestoreSeeder, 17 mock hits) · Security 1 · UX/design 3 · Performance 3 (not measured) · Completeness 2 · Store readiness 0.

## Red flags
1. **CRITICAL:** `src/app/api/subscriptions/webhook/route.ts:13` falls back to `'dev_signature'`; no HMAC check; schema only needs a non-empty string (`src/schemas/subscription.ts:44`). Anyone can POST `payment.success` with a userId and activate a tier.
2. Admin is client-gated; `NEXT_PUBLIC_OWNER_EMAIL` in client env.
3. Dead code `FirestoreSeeder.tsx` (0 importers). 4. AGENTS/CLAUDE/GEMINI.md identical (23,827 bytes each).

## Upgrade size: M-L. Top 5 fixes
1. Verify webhook signature (HMAC, timing-safe); delete the `dev_signature` fallback. 2. Server-side admin check (Firebase Admin claims) on /admin and owner APIs. 3. Legal: sub-processors, DPA, AI-training clause, EGP pricing, cancellation. 4. Split the 35 oversized files, admin/page.tsx first. 5. Delete dead code; run typecheck/lint/test to confirm 281/281.
**Name:** "Hagoozat Elite" is already used in README, llms.txt, 11Players package.json and the Desktop shortcuts: keep it (trademark not checked).
