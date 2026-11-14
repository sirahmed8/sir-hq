# HQ Manager Update: Mobile Cache, Currency Display & Bot Commands Sync

## 1. SIR AI Mobile Cache & UI Overhaul (Live on Dual Hosts)
- **Root Cause of Stale Phone UI:** Mobile Chrome had aggressively cached the first-ever deployment in Service Worker CacheStorage (`sirai-shell-v1`). Because there was no `controllerchange` reload listener and navigations were handled inside the SPA hash router, the phone never loaded updated bundles, continuing to display the old colliding tabs and the 5 raw currency buttons.
- **Service Worker v7 & Auto-Reload:**
  - Bumped to `v7` in `apps/web/public/sw.js` with instant cache purge on activate (`caches.delete`).
  - Added `skipWaiting()` and message listener `{ type: "SKIP_WAITING" }`.
  - Added foreground update check on `visibilitychange` and automatic `window.location.reload()` on `controllerchange` in `apps/web/src/lib/pwa.ts`.
  - Upgraded App Menu "Refresh" to explicitly purge `window.caches` and unregister stale workers before reloading.
- **Locale-Aware Currency Display:**
  - `Plan.tsx` & `Pricing.tsx` now use locale-appropriate currency formatting: displays `0 EGP` in English (preventing reversed `0 p.2` glyph bidi inversion) and `0 ج.م` in Arabic.
  - Streamlined currency selector into an auto-detected regional badge + compact accessible selector that never spills outside mobile cards.
  - Added `gap-1.5` and `p-1.5` to `packages/ui/src/TabBar.tsx` ensuring generous breathing room between tabs on 320px-390px screens.
- **Dual-Host Verification:**
  - Firebase: `https://sir-ai-official.web.app` (HTTP 200 OK, bundle `index-C00Zg8eg.js`)
  - Vercel: `https://sir-ai-pi.vercel.app` (HTTP 200 OK, bundle `index-C00Zg8eg.js`)
  - Both fingerprints match: `b879333a6232`.
  - Committed and pushed to `main` (`667752b`).

## 2. Connected Phone APK Deployments
- Pushed `AHome-v1.0.0.apk` (5.2 MB) directly to phone storage: `/sdcard/Download/AHome-v1.0.0.apk`.
- Pushed `SIR-AI-v1.0.0.apk` (6.6 MB) directly to phone storage: `/sdcard/Download/SIR-AI-v1.0.0.apk`.
- Both are ready for single-tap install directly from your phone's file manager or downloads without MIUI "Install via USB" permission timeouts.

## 3. Telegram Bot Ecosystem Updates
- **Private Project Bot (`Personal1AI1Bot`):**
  - Updated bot description and short description to personal family AI.
  - Deployed real working command menu live to Telegram via Bot API: `/start`, `/today`, `/remind`, `/list`, `/done`, `/delete`, `/undo`, `/mode`, `/newchat`, `/status`, `/privacy`, `/app`, `/link`.
  - Committed and pushed to `main` (`c4e7343`).
- **SIR AI Bot (`@SirAiAssistantBot`):**
  - Configured with bot token `9070003164:...` and active webhook at `https://sir-ai-pi.vercel.app/api/telegram/webhook`.

## 4. Background Health & Management
- 0 rogue CMD/conhost windows visible.
- Autopilot watchdog guarded with active manager flag.
- Periodic manager tick scheduled and monitoring.
