# Inventory: EGFootball5 "Kickoff" (2026-10-29, scout, read-only; tests not run)

**What:** 5-a-side pitch booking, match lobbies (Hagaz), stadium admin; Arabic/English; Egypt. Owner sirahmed8. No `.sir/` folder.
**Live (all 200):** egfootball5.web.app /en/, /ar/, /en/privacy/, /api/health. Firebase Hosting site `egfootball5`, Next 16 `output: export`.
**Stack:** Next ^16.3.6, React 19.2.4, Tailwind v4, Firebase ^12.14, framer-motion 12, next-intl 4.13, zustand 5, TanStack Query 5, TS 5, ESLint 9.
**Repo:** `sirahmed8/EGFootball5`, main, clean, 177 commits, last 5f0f91b (2026-10-26), local branch `pre-sir-snapshot`. No CI (only copilot-instructions in `.github`). 2 test files (about 6 cases).
**Platforms:** web + PWA manifest only; `GoogleService-Info.plist` and `google-services.json` in root but no native projects.
**Data/auth/AI:** Firestore (74 allow rules), RTDB rules, Cloud Functions (`lockSlot`, `verifyMatchResult`, 218 lines), Cloudinary. Firebase Auth (Google + email); zustand persists the app user to localStorage (useAuthStore.ts:36). AI via `/api/ai/chat`.
**Secrets:** `.env`, `.env.local` gitignored and untracked; only `.env.example` tracked. Values not read.
**Legal:** /privacy /terms /refund /cookies, root policy .md, CookieConsentBanner. **Desktop:** `EGFootball5.lnk` and `Stop EGFootball5.lnk` (launch/stop .vbs).

## Scores (0-5)
| Area | Score | Evidence |
|---|---|---|
| Architecture | 3 | clean split; API routes conflict with static export |
| Code quality | 3 | 21 `any`, 3 eslint-disable, 1 dangerouslySetInnerHTML |
| Security | 2 | hardcoded owner email (login/page.tsx:35); CSP unsafe-inline/eval |
| UX/design | 3 | bilingual, Geist/Cairo; 254 `rounded-full`, 17 em-dashes in src |
| Performance | 2 | owner analytics reads whole collections |
| Completeness | 2 | `/api/ai/chat`, `/api/ai/tts`, `/api/admin/role` return 404 live |
| Store readiness | 1 | |

## Red flags
1. Server API routes missing on the live host (404): AI chat and admin-role dead in production.
2. Owner check is client-side by literal email.
3. Weak CSP. 4. No CI.

## Overlap with Merged sites
EGFootball5 has what Merged lacks (partial route diff): 15-min slot lock, deposit receipt upload + verification queue, Hagaz lobbies, jersey designer, owner dashboards, achievements/XP, notifications, communities and chat, support tickets, announcements, onboarding, guide. Merged has its own Dockerfile, subscriptions checkout/webhook, data deletion, unsubscribe.

## Upgrade size: M (L if AI/admin must go live). Top 5 fixes
1. Move the three API routes to `functions/` + rewrites in firebase.json. 2. Owner check by custom claims/env. 3. Drop unsafe-eval/unsafe-inline (nonces). 4. Add CI (lint, test, build). 5. Aggregate owner analytics server-side.
Business ops: partial (booking, deposit verification, support tickets, EGP/USD formatting; no MRR/invoices/unsubscribe/live payment).
