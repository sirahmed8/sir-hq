# Inventory: SIR Restaurant (repo `restaurant-os`) (2026-10-29, scout, read-only; nothing built, run or tested)

**What:** Electron + React desktop and web POS for restaurants: POS, KDS, waiter, kiosk, floor plan, inventory, delivery aggregator, WhatsApp bot, ZATCA (Saudi e-invoicing) phase 2. Arabic/English; subscription tiers in EGP (`src/lib/subscription.ts`: 0 / 450 / 750 / 1950).
**Stack:** React 19.0, Vite 6.1, TS 5.7, Tailwind 4.0, Zustand 5, TanStack Query 5, Firebase 12.17, framer-motion 12.4, Electron 34.2, electron-builder 25.1.8, vitest 4.1.10. `dist:win` builds an NSIS x64 installer (appId com.sirrestaurant.app); installer on disk at `public/downloads/` (gitignored).
**Repo:** `sirahmed8/restaurant-os`, main, clean, HEAD 17e6d84. CI `.github/workflows/ci.yml` (windows-latest, Node 20: npm ci, typecheck, test, build) not run. 20 test files. Only `continuation_checkpoint.md` (Oct 5), no `.sir/`. AGENTS/CLAUDE/GEMINI.md are identical generic copies.
**Live:** not verified (commit 04ba279 mentions a Vercel deploy; kill-switch heartbeat points to `security.sir-restaurant.cloud`, not probed).
**Data/auth/AI:** Realtime DB + Firestore; 12+ local stores; `src/db/mock-data.ts` (usage not traced). Auth: TenantAuthModal, BusinessAuthScreen, LockScreen, `lib/rbac.ts`; owner check via `VITE_OWNER_EMAIL` (client bundle, not a boundary). AI: `aiRouter.ts` calls Google (key in URL query, line 215) and OpenRouter (line 280) from the browser.
**Legal:** root PRIVACY/TERMS/REFUND/COOKIE/EULA .md; in-app LegalModal and CookieConsentBanner; no /privacy route verified.

## Scores (0-5)
Architecture 3 · Code quality 2 (about 637 any/TODO/mock hits across 88 files) · Security 1 · Completeness 3 · Store readiness 1 (unsigned unless CSC_* set). UX/design and performance not scored (nothing run).

## Red flags
1. `src/services/security/killSwitch.ts` line 46: a hardcoded master rescue PIN in client code (value was printed by accident in the scout's tool output; treat as exposed, rotate or remove; not repeated here).
2. `src/services/zatcaPhase2Service.ts` lines 222 and 1347 contain "BEGIN EC PRIVATE KEY" headers: verify real key material or placeholders.
3. `database.rules.json` and `firestore.rules`: any signed-in user can read/write all branches, orders, shifts, inventory (no tenant check). This is the tenant-isolation bug the TickTick sprint lists for Days 13-14.
4. The kill switch lets a vendor heartbeat lock out "non-paying" installs (killSwitch.ts header, lines 5-6). Needs disclosure in the EULA and privacy text; the same flags exist in all four verticals.
5. Owner gate client-side. 6. Installer unsigned by default.

## Upgrade size: M for this app, but fix the shared core once (see the combined Library/Market/Pharmacy file)
Top 5 fixes: 1. remove the rescue PIN, rotate, make overrides server-verified. 2. Confirm or remove the EC key blocks; rotate if real. 3. Per-tenant claims and deny-by-default rules. 4. AI behind a server proxy, no key in the URL. 5. Run `ci.yml` locally and record the output; sign the installer when a certificate is affordable.
**Restaurant-only modules:** KDS, Waiter, Kiosk, FloorPlan, TableGuestPortal, DeliveryHub, Zatca, tableOrderService, recipeService, deliveryAggregatorService, zatcaPhase2Service.
