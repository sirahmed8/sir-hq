# r70-cycle-sir-jobs — improvement cycle report

Date: 2026-11-13. Worker: devin (SWE-2 Flash). Project: D:/Projects/SIR Jobs.
Lens chosen: **performance and bundle size** (not used by earlier cycles; bidi/RTL, five-states, motion and click-targets were covered in r34/r37/r46/r60).

## 1. Audit (before numbers, all measured today against the live server)

Baseline cold load (uncompressed, `curl` byte counts on 127.0.0.1:3456):

| Asset | Bytes |
|---|---|
| index.html | 57,778 |
| app.css | 73,283 |
| 30 JS modules total | 176,593 |
| i18n en+ar | 24,435 |
| manifest + svg icons | ~1,700 |
| **subtotal** | **~334 KB** |
| /favicon.ico (auto-requested) | **370,070** (assets/brand/icon.ico) |

API boot payloads: /api/jobs **250,478 B** (15 items; `rawDescription` raw-HTML field alone = 151,003 B and is read by zero client code — grep `src/public` returns nothing; server-side scorer/drafter read the digest JSON files directly), /api/pipeline 18,353 B, /api/proposals 32,088 B, others <5 KB.

Serving defects found:
- Every static asset sent `Cache-Control: no-cache, no-store, must-revalidate` + `Pragma: no-cache` + `Expires: 0` despite working ETags → repeat visits re-downloaded everything instead of getting 304s.
- No compression anywhere (no gzip/brotli) for ~335 KB of text per cold load, and no `Content-Length`.
- `sendJson` set no Content-Length, no ETag, no compression.
- `fs.statSync` called 3x per request; SPA index.html fallback had no ETag at all.
- All 8 views statically imported by main.js; cash/profile/security (~22 KB raw) parsed at boot though rarely visited.
- `checkAuthSession` awaited `/api/auth/session` then `/api/session` sequentially.
- `loadDiagnostics` (2 API calls) ran at boot; the `security` tab had **no case in `renderCurrentView`** — a latent bug masked by the eager boot load.
- `resize` listener re-ran `updateNavIndicator` on every resize event.

Cycle plan written first: `.sir/cycles/2026-11-13-1.md` (includes "Found without being told" section).

## 2. Improvements shipped (one commit each, all pushed to main)

| # | Change | Evidence (before → after) | Commit |
|---|---|---|---|
| 1 | Compact favicon: built `src/public/favicon.ico` (PNG-in-ICO, 16/32/48) and serve it instead of `assets/brand/icon.ico` | 370,070 B → **11,100 B** (curl verified on prod :3456) | b2e4c24 |
| 2 | `/api/jobs` strips `rawDescription` (server-side consumers unaffected — they read digest files) | 250,478 B → **98,994 B** (−60.5%); `hasRaw:false`, `description` kept | 5c2b9a4 |
| 3+4 | `src/routes/static.mjs` rewrite: single statSync, Content-Length, `no-cache` (store + ETag revalidate) replacing `no-store`, `immutable` 1y for `?v=` URLs, gzip for text types (mtime-keyed buffer cache), ETag + gzip on SPA fallback | app.css 73,283→**12,917 B gz**; index.html 57,778→**12,236 B gz**; 304 verified (`304 0B`); `?v=` → `public, max-age=31536000, immutable` | 341ae23 |
| 5 | `sendJson` gzip on `Accept-Encoding` + Content-Length + `Vary` | /api/jobs wire: 98,994 → **29,340 B gz** (−88% vs original 250 KB); node fetch auto-decompress verified (items:15) | 4eca0b5 |
| 6 | `index.html` modulepreload for the 22-file eager module graph | 21 `<link rel="modulepreload">` hints added | d41aec0 |
| 7 | Parallel auth bootstrap (`Promise.all` on the two session fetches); `loadDiagnostics` deferred to first security visit; added missing `security` case to `renderCurrentView` | code diff; diagnostics no longer fetched at boot | 3cf70de |
| 8 | Lazy-load `cash`/`profile`/`security` via `import()` + `ensureView()` prototype mixin; FX helpers (`loadFxData`/`applyFxData`/`saveManualFx`/`refreshLiveFx`) moved to `api.js` (pipeline subtitle, negotiation EGP card, target calculator unaffected); profile data loads on first visit; palette/context-menu/retryLoad ensure module first; `sw.js` → v13 + favicon precache | eager JS drops ~22 KB raw; click-audit CDP 168 elements/36 clicks green | a0294b5 (+sw commit) |
| 9 | `resize` → `updateNavIndicator` rAF-throttled | code diff | d41aec0 |
| 10 | Gates + restart: `npm test` all suites pass, lint 0, typecheck 0, doctor ALL GATES GREEN; production server restarted via dev-stop/dev-start and verified | see §3 | 120e89a (checkpoint) |

Supporting test updates (same lazy-load commit): `test-r34-click-audit.mjs`, `test-r34-bidi.mjs`, `test-r34-redesign.mjs` CDP fixtures now `await app.ensureView(v)` before calling view render methods directly.

## 3. Verification (real output, today)

- `npm test` — full chain exit 0. Highlights: digest 11/11, dashboard 12/12, security 9/9, r34 click-audit **168 interactive elements, 36 real clicks across 7 views, 0 defects**, r34-topbar pass, r34-bidi pass (EN+AR), r34-redesign pass, r60 suites all pass (nudge 5/5 last suite).
- `npm run lint` — 0 problems (fixed one `no-unused-vars` on the rawDescription destructure → `_rawDescription`).
- `npm run typecheck` — 0 errors.
- `npm run doctor` — `OVERALL SYSTEM VERDICT: HEALTHY & PRODUCTION-READY (ALL GATES GREEN)`.
- Live curl proof on test instance (PORT=3466) and production (127.0.0.1:3456 after restart):
  - `GET /` gzip → 12,236 B (was 57,778), `Content-Encoding: gzip`, `Vary: Accept-Encoding`
  - `GET /app.css?v=3.2.0` → `Cache-Control: public, max-age=31536000, immutable`
  - `If-None-Match` → `304` with empty body
  - `GET /favicon.ico` → 11,100 B (was 370,070)
  - `GET /api/jobs` gzip → `Content-Length: 29340`, `Content-Encoding: gzip`
- Eager cold-load payload now **~96.9 KB gzipped total** (index+css+22 eager JS+i18n+manifest+favicon) vs ~705 KB uncompressed before; repeat visits cost ~200 B 304s per asset instead of full bodies.
- `ops/ci-quota-exhausted.flag` present → per WORKER_PREAMBLE rule 18 local verification substitutes for CI; commits pushed to `main` regardless (through `120e89a`).

## 4. "Found without being told"

- `/favicon.ico` was a **370 KB** brand icon auto-downloaded on every visit.
- `/api/jobs` shipped **151 KB of `rawDescription` HTML** the client never reads.
- `no-store` on every asset nullified the working ETag layer — every visit re-downloaded ~335 KB.
- Zero compression on the entire app.
- `renderCurrentView` had **no `security` case** — the diagnostics view could never self-render on tab switch; only the eager `loadAllData` masked it.
- `checkAuthSession` serialized two independent fetches on the boot critical path.
- SPA fallback (`/some/route` → index.html) had no ETag — full 57 KB on every client-side navigation fallback.

## 5. Adversarial / edge checks done

- HEAD requests return correct (gzipped) Content-Length; 405 on non-GET/HEAD preserved; path-traversal guard untouched.
- `Accept-Encoding` absent → identity bytes served (73,283 B css verified).
- Lazy views: `ensureView` dedupes concurrent calls, deletes itself from the ready-set on import failure (retry possible), mixin only accepts exports ending in `Methods`.
- Palette "Export CV"/"Copy proposal" and context-menu "Refresh" ensure the lazy module before invoking; `retryLoad` ensures too.
- `renderCurrentView` captures `tab` before `await` and bails if the user switched mid-import (no wrong-view render).
- inbox/contacts/proposals/openings/pipeline/details modules stay eager → their nav badges (pending files, counts) still populate at boot.

## 6. Still open / honest notes

- inbox/contacts/proposals/openings data still loads eagerly at boot (small payloads; badges depend on them). jobsData (~29 KB gz) stays eager for the openings badge and proposal cross-references.
- `br` (brotli) not implemented — gzip only; gains vs brotli are a few percent on this payload size.
- Lazy-loaded modules are still fully precached by sw.js v13 (offline-first kept deliberately; first visit pays the bytes in background, not on critical path).
- OWNER_REQUEST_LEDGER items for this project remain owner-side (LinkedIn/marketing capture, income-model quarterly refresh is tracked in `.sir/INCOME_MODEL.md`); `ops/briefs/sir-jobs-tasks.md` items 1–10 were already all complete from r60 — nothing unticked remained.
- GitHub Actions still quota-blocked (`ops/ci-quota-exhausted.flag`, reset ~2026-12-01); local gates are the green proof.

## 7. Recommendations for next cycle

- Next lens suggestion: **offline and error recovery** (sw.js network-first strategy, localStorage stale-while-revalidate coverage audit) or **security and auth** (guardPost coverage, rate limits on new endpoints).
- Possible follow-up: brotli static precompression at build/serve time; ETag for `/api/jobs` based on digest file mtime.
