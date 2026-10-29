# Inventory: 11Players (2026-10-29, scout, read-only, nothing built or run)

**What:** Arabic-first football player rating, matchmaking, community and match-day PWA (package name `hagoozat-elite`). EGP pricing copy (59 EGP/mo Pro).
**Live:** https://an-11-players.web.app (hardcoded in layout and sitemap; not checked). **Build:** `next build --webpack`, `output: "export"`; `out/` exists.
**Stack:** Next 16.2.11, React 19.2.8, TS ^5.4.5, Tailwind 4.3.3, Firebase 12.16, framer-motion 12.42, zod 4.4.3, vitest 4.1.10.
**Repo:** `sirahmed8/11Players`, main = origin/main, 430 commits, last 7aec96ea (2026-10-26), clean tree, branch `pre-sir-snapshot`. 333 tracked files. No CI (only copilot-instructions in `.github`).
**Platforms:** PWA only (service worker disabled). `eas.json` is orphaned (no native project). Icons: logo.jpg used for 192 and 512 (no PNGs). Desktop: `11Players.lnk` + `Stop 11Players.lnk` (launch-dev.ps1); Desktop folder "Hagoozat Elite" holds 2 shortcuts.
**Data/auth/AI:** Firestore (rules 239 lines), Cloudinary unsigned preset, Vercel Blob (avatars). Firebase Auth, no tokens in localStorage. AI: aiService.ts (Gemini + OpenRouter, server-side keys); `api/ai/chat` has in-memory 15 req/min per IP, no auth; avatar upload checks only that a Bearer header exists. `out/api` is empty, so API routes do not ship on Firebase static hosting.
**Legal:** /privacy /terms /tos /refund(s) /cookie(s); AI training ban, liability cap, arbitration present. PRIVACY_POLICY.md:32 claims SOC 2 Type II / ISO 27001 (truthful-claims risk). Pre-consent blocking and 1-click deletion not verified.
**Code:** 267 src files, about 60,100 lines; 62 files over 300 lines (largest MatchConfigModal.tsx 2,864). 9 unit test files, not run.

## Scores (0-5)
| Area | Score | Evidence |
|---|---|---|
| Architecture | 2 | layered folders but 62 oversized files |
| Code quality | 2 | dummy generator in admin path, placeholder config fallbacks |
| Security | 1 | client-only owner check, unauthenticated AI route, weak avatar auth |
| UX/design | 3 | bilingual, dark/light; screens not reviewed |
| Performance | 2 | no-cache on all paths, heavy deps (jspdf, html2canvas, emoji-picker) |
| Completeness | 3 | about 50 page dirs; server features dead on static host |
| Store readiness | 0 native / 2 web | PWA only |

## Red flags
- Fake players: `generateDummyPlayersForCommunity` (src/lib/dummyData.ts) called from AdminTable.tsx:386.
- Placeholder and literal apiKey fallbacks in src/lib/firebase.ts:8-13 (value not printed).
- `.env.local` holds GEMINI and OPENROUTER keys (untracked); service-account JSON `an-11-players-firebase-adminsdk-*.json` sits in the repo root (gitignored): move it out. Git history not scanned for keys.
- Chat prompt (route.ts:161) says payment methods are live; they are not integrated.

## Overlap with Merged sites
Merged has: scouting component, live match, tactics, chat drawer, PitchSplitBillCalculator, subscriptions with checkout/webhook, data deletion, Dockerfile.
11Players only (not found in Merged src): AI layer (aiService, api/ai/*), captain draft room, communities/global pages, owner analytics.

## Upgrade size: L. Top 5 fixes
1. Verified custom claims or Firestore role checked in rules instead of the client owner check.
2. Decide hosting: API routes need Vercel or Cloud Functions, plus auth and App Check on /api/ai/chat.
3. Remove dummyData from AdminTable and the placeholder fallbacks.
4. Move the service-account JSON out of the repo; scan git history for keys.
5. Split the 62 oversized files; add real PNG PWA icons.

Business ops: partial (legal, support and owner analytics pages; no gateway, webhook, billing ledger or 1-click cancel).
