# Inventory: Negm Furniture (2026-10-29, scout, read-only; vitest was run by the scout)

**What:** bilingual (ar RTL / en) furniture showroom catalog and lead-capture site for Negm Furniture EG (two Cairo showrooms). **Client brand** built by Ahmed (operator in `src/lib/products-data.ts` CORPORATE_ENTITY; origin `sirahmed8/...`, upstream `negmomar28-lgtm/...`).
**Live:** https://negm-furniture.eg (not checked). Firebase Hosting site `negm-furniture-eg` under SIR's project `sir-ai-official`.
**Stack:** Next ^16.4.2, React 19.3.1, TS 5.7 strict, Tailwind 3.4, Firebase 13, @google/genai, Vitest 5.0.5, `output: 'export'`.
**Repo:** clean, main, 17 commits, 135 tracked files. **Tests:** `npx vitest run` = 12 files, 158 passed (2.7 s); docs report stale counts. No CI.
**Data:** static `products-data.ts`; no Firestore reads/writes; admin CRUD is `useState` only; Cloudinary upload simulated. **Auth:** Firebase Google popup; `AdminGuard` client-side; admin store in localStorage.
**AI:** `POST /api/ai/decor` (Gemini key server-side) cannot run under static export; offline rule engine exists.
**Legal:** /privacy /terms /cookies /refunds /returns; cookie banner has Reject All; no tracker scripts. Image and logo licences unknown. **Desktop:** `Negm Furniture\` has Desktop App / Negm Furniture / Stop Server / Installer shortcuts.

## Scores (0-5)
Architecture 2 (static export + server route) · Code quality 3 (strict TS, 158 tests, simulated CRUD) · Security 2 (client-only admin, Firestore rules unenforced) · UX/design 3 · Performance 3 (not measured) · Completeness 2 (no persistence/analytics) · Store readiness 1.

## Red flags (nothing fake may ship)
1. Fake login: `UserProfileCard.tsx:32-38` writes a fake "vip.client@gmail.com" user.
2. Fabricated ratings (`products-data.ts:89-90`: 4.95, 38 reviews) and "+285K" followers (`products-data.ts:339`, `page.tsx:102`, `showrooms/page.tsx:82`) with no source.
3. "Zero Fake Data" comment on the admin dashboard (`admin/page.tsx:115`) is false.
4. Client site hosted in SIR's Firebase project; `firebase.ts` fallback project id mismatches `.firebaserc`.
5. Product photo and logo licences unknown.

## Upgrade size: M (8-12 focused days, estimate). Top 5 fixes
1. Remove fake login and unsourced ratings/followers or use client-supplied real data. 2. Resolve static export vs API route. 3. Real catalog (Firestore with validated rules or a documented static pipeline); remove simulated upload. 4. Server-verified admin (custom claims). 5. Confirm photo/logo licences; move hosting to the client's own Firebase project; add ESLint deps and a real build check.
**Decision:** stays separate from SIR products (client brand, own domain, owner, Firebase project). Share tooling only, not code or data.
