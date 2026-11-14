# Report: r79-sir-ai-branding

## What changed
- Copied `D:\Projects\SIR AI\assets\brand\icon.png` (256x256 PNG) to `D:\Projects\SIR AI\apps\web\public\brand-icon.png` and `D:\Projects\SIR AI\assets\brand\icon.ico` to `D:\Projects\SIR AI\apps\web\public\favicon.ico`.
- `D:\Projects\SIR AI\apps\web\index.html`: set `<link rel="icon" type="image/png" href="/brand-icon.png" />`, `<link rel="alternate icon" href="/favicon.ico" />`, and `<link rel="apple-touch-icon" href="/brand-icon.png" />`.
- `D:\Projects\SIR AI\apps\web\public\sw.js`: updated app shell precache (`v2`) to include `/brand-icon.png` and `/favicon.ico` and intercept precached `SHELL_URLS` requests in `fetch` (network-first with cache fallback so brand icons render offline instead of breaking).
- `D:\Projects\SIR AI\apps\web\src\App.tsx`: rendered `<img src="/brand-icon.png" alt="" aria-hidden="true" width={28} height={28} ... />` beside `{t("app.name")}` in the desktop `<Shell>` navbar (`hidden shrink-0 items-center gap-2 md:flex`).
- `D:\Projects\SIR AI\apps\web\src\screens\Auth.tsx`: rendered the matching 28x28 `<img src="/brand-icon.png" ... />` beside `{t("app.name")}` in the `AuthScreen` header.
- Commits pushed to `main`: `d4e9208` and `cfadcb4`.

## Verification
- Build & gates: `npm run typecheck` (exit 0), `npm run lint` (exit 0), `npm test` (`34 test files passed, 341 tests passed`, exit 0), `npm run build` (`3.61s`, exit 0).
- `vite preview` + Playwright:
  - `GET /brand-icon.png` -> HTTP 200 `image/png` (`89504e47`), `GET /favicon.ico` -> HTTP 200 `image/x-icon` (`00000100`).
  - `Auth` screenshots at `1280x800` EN light and `390x844` AR dark (`img.complete === true`, `naturalWidth === 256`, `scrollWidth === innerWidth`, 0 console/page errors).
  - `node apps/web/e2e/pwa.mjs http://127.0.0.1:4173 .sir/evidence/r79/pwa-offline.png` -> all checks passed; visually inspected `pwa-offline.png` to confirm `/brand-icon.png` renders offline.
- Authenticated `<Shell>` (`vite` dev + Auth emulator + Firestore emulator):
  - Verified desktop navbar logo at `1280x800`, `1920x1080`, `768x1024` (0 wrapped tabs, 79px nav height, `naturalWidth === 256`) and Arabic RTL dark mode (`1280x800`, `dir="rtl"`), plus mobile `390x844` and `320x700` (0 horizontal overflow, 0 console errors).
  - Evidence screenshots in `D:\Projects\SIR AI\.sir\evidence\r79\`.

## Honest gaps
- PWA manifest icons (`/icon-192.png`, `/icon-512.png`, `/icon-maskable-512.png`) and unused legacy `/favicon.svg` file in `apps/web/public` were left untouched; browser `<link rel="icon">` uses `/brand-icon.png` and `/favicon.ico`.
- On mobile (`< 768px`) inside `<Shell>`, the navbar stays bottom-docked tab icons/labels only (`hidden md:flex` hides the brand text/icon to keep 7 tabs unobstructed at 320px/390px); the brand logo + title renders in `AuthScreen` on mobile and in the top navbar on desktop (`>= 768px`).
