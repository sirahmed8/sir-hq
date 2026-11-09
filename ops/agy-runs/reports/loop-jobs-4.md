# Perpetual Improvement Loop: SIR Jobs - Cycle 17

**Project**: SIR Jobs (`D:/Projects/SIR Jobs`)  
**Auditor**: Antigravity  
**Date**: 2026-11-09  
**Lens Audited**:
- **Cycle 17**: Performance, Memory Lifecycle and Event Listener Hygiene

---

## 1. Executive Summary

In accordance with `PERPETUAL_LOOP.md` and the standing directives in `00-master-directive.md` and `23-premium-code-bar.md`, Cycle 17 of the perpetual improvement loop was executed on SIR Jobs under the **Performance, Memory Lifecycle & Event Listener Hygiene** lens.

All improvements were implemented, unit-tested, verified across all 5 verification gates via `scripts/verify.ps1`, validated across 8 viewports via Chrome CDP deep scan (`scripts/audit_deep_scan.mjs`), and confirmed clean.

Total automated test count now stands at **18 test suites** with 100+ tests passing 100% green.

---

## 2. Work Delivered in Cycle 17

### 1. Memory Pruning in Sliding-Window Rate Limiter (`src/server.mjs`)
- **Issue**: The server sliding-window rate limiter stored IP addresses in a top-level `requestLog` Map. While timestamps older than 60s were filtered during individual checks, the Map keys themselves were never deleted. In prolonged 24/7 daemon execution or automated scraping, this created unbounded heap growth.
- **Fix**: Added proactive eviction when `requestLog.size > 50`. Any IP key whose recorded timestamps are entirely older than the sliding window (`now - RATE_LIMIT_WINDOW_MS`) is pruned via `requestLog.delete(key)`.

### 2. LocalStorage Quota Overflow Resilience (`src/public/app.js`)
- **Issue**: In `saveToCache(key, data)`, calling `localStorage.setItem` directly without a quota-exceeded handler could throw an unhandled `DOMException` if storage reached its 5MB limit, breaking offline caching.
- **Fix**: Wrapped cache writes in a resilient try-catch block. When a quota error occurs, the cache engine executes targeted cache eviction: it deletes older cached query keys prefixed with `sir_jobs_cache_`, clears expired items, and safely retries the save.

### 3. Search Input Debouncing (`src/public/app.js`)
- **Issue**: Both `#pipeline-search` and `#jobs-search` fired `input` event listeners immediately on every single keystroke. In the job feed with dozens of cards, typing rapidly caused immediate DOM destruction and rebuilding 5 to 10 times in under a second, leading to layout thrashing.
- **Fix**: Introduced a lightweight `debounce(fn, ms)` utility in `app.js` and wrapped search render triggers with a 100ms debounce interval, keeping input keystroke response snappy while eliminating DOM rebuilding churn.

### 4. Event Delegation on Kanban Drag and Drop (`src/public/app.js`)
- **Issue**: In `renderPipeline()`, every time the board was updated, individual event listeners (`dragstart`, `dragend`, `dragover`, `dragleave`, `drop`) were imperatively attached to each `.app-card` and `.funnel-col`. Repeated transitions or filters caused listener churn and retained closures in memory.
- **Fix**: Migrated the entire Kanban board to event delegation. A single set of permanent listeners is attached once to `#pipeline-populated`. The handlers resolve cards via `e.target.closest('.app-card')` and columns via `e.target.closest('.funnel-col')`, completely eliminating per-render listener attachments.

### 5. Personal Note Input Listener Optimization (`src/public/app.js`)
- **Issue**: In `renderProposals()`, re-rendering the proposal viewer re-bound an anonymous closure listener `addEventListener('input')` on `#prop-personal-note`, retaining closures in memory.
- **Fix**: Created an explicit instance method `savePersonalNote(val)` on `SirJobsApp` and bound `#prop-personal-note` using direct `oninput="app.savePersonalNote(this.value)"`.

### 6. Application Detail Fallback in Specs Modal (`src/public/app.js`)
- **Issue**: When an application card on the Pipeline Board had a matching record in the database but the original listing was not in the currently scraped `jobsData.items` feed (or after source expiration), clicking "Specs" only showed a toast notification and failed to open detailed criteria.
- **Fix**: Implemented `showApplicationDetail(app)` to render full specifications in the modal dialog: company, stage, pay, deadline, submission keywords, fit ratio, follow-up countdown status, and pipeline verified notes, with a direct link to the employer portal.

### 7. Toast Dismissal Lifecycle Hygiene (`src/public/app.js`)
- **Issue**: `showToast(msg)` attached a click listener without `{ once: true }` and did not cancel the auto-dismiss timer on manual user click, leaving orphaned timeouts running in the background.
- **Fix**: Attached the manual click listener with `{ once: true }` and explicitly invoked `clearTimeout(timer)` inside `dismiss()`.

---

## 3. "Found Without Being Told" (Root-Cause Discoveries)

| # | Bug / Deficiency Discovered | Root Cause | Permanent Root-Cause Fix |
|---|---|---|---|
| 1 | **Unbounded Rate-Limiter Map Heap Growth** | `requestLog` in `src/server.mjs` retained IP keys indefinitely with empty timestamp arrays after sliding-window expiration. | Added automatic Map key eviction when `requestLog.size > 50`. Tested in `test/test-cycle17-performance-hygiene.mjs`. |
| 2 | **Kanban DOM Event Listener Churn** | `renderPipeline()` repeatedly bound 5 event listeners to every card and column on each render cycle. | Replaced with container-level event delegation on `#pipeline-populated`. |
| 3 | **DOM Thrashing on Fast Search Keystrokes** | Keystrokes on `#pipeline-search` and `#jobs-search` immediately destroyed and rebuilt DOM cards synchronously. | Implemented 100ms debouncing utility on search inputs. |
| 4 | **Specs Modal Dead End for Staged Pipeline Cards** | If a pipeline card was not present in the volatile scraped feed, the details modal failed to open. | Built `showApplicationDetail(app)` fallback rendering full criteria, stage history, and follow-up deadlines. |
| 5 | **Toast Timer Orphan During Manual Dismissal** | Manually clicking a toast dismissed the element but left the scheduled `setTimeout` timer active. | Added explicit `clearTimeout(timer)` and `{ once: true }` click listener binding. |

---

## 4. Verification Evidence

### 1. Test Suite Execution (`npm test`)
```
> sir-jobs@1.0.0 test
> node scripts/digest/test/test-digest.mjs && node test/test-dashboard.mjs && node test/test-pipeline.mjs && node test/test-security.mjs && node test/test-undo.mjs && node test/test-evals.mjs && node test/test-a11y-ui.mjs && node test/test-scheduled-run.mjs && node test/test-motion-physics.mjs && node test/test-decision-velocity.mjs && node test/test-offline-resilience.mjs && node test/test-ux-friction.mjs && node test/test-theme-interaction.mjs && node test/test-auth-ui-flow.mjs && node test/test-cycle12-power-features.mjs && node test/test-fx.mjs && node test/test-round8-features.mjs && node test/test-cycle17-performance-hygiene.mjs

✔ All 18 test suites passed 100% green:
  - test-digest.mjs: 11/11 passed
  - test-dashboard.mjs: 12/12 passed
  - test-pipeline.mjs: 10/10 passed
  - test-security.mjs: 9/9 passed
  - test-undo.mjs: 3/3 passed
  - test-evals.mjs: 4/4 passed
  - test-a11y-ui.mjs: 8/8 passed
  - test-scheduled-run.mjs: passed
  - test-motion-physics.mjs: 8/8 passed
  - test-decision-velocity.mjs: 6/6 passed
  - test-offline-resilience.mjs: 7/7 passed
  - test-ux-friction.mjs: 9/9 passed
  - test-theme-interaction.mjs: 1/1 headless CDP passed
  - test-auth-ui-flow.mjs: 1/1 headless CDP passed
  - test-cycle12-power-features.mjs: 6/6 passed
  - test-fx.mjs: 4/4 passed
  - test-round8-features.mjs: 5/5 passed
  - test-cycle17-performance-hygiene.mjs: 5/5 passed
```

### 2. Operational Doctor Diagnostics (`npm run doctor`)
```
1. Runtime Environment: Node.js v26.13.0, Python 3.14.7 - PASS
2. Sovereign Storage & Database Integrity: PRAGMA integrity_check=ok, 6 tables, 291 opportunities, 24 staged - PASS
3. Backup & Snapshot Status: 47 verified snapshots in D:/Projects/Backups/SIR-Jobs-data - PASS
4. Zero-Trust Security & Privacy Gate: data/ and .env ignored, 0 leaks across tracked files - PASS
5. Server Daemon & Loopback Health: Running at http://127.0.0.1:3456/ - PASS
6. Sovereign Transport & Tailnet TLS Integrity: WireGuard ChaCha20-Poly1305 active, loopback isolation - PASS
>> OVERALL SYSTEM VERDICT: HEALTHY & PRODUCTION-READY (ALL GATES GREEN)
```

### 3. Responsive CDP Audit Across 8 Viewports (`scripts/audit_deep_scan.mjs`)
- 320px Foldable: `hasOverflow: false`
- 390px Phone Portrait: `hasOverflow: false`
- 844px Phone Landscape: `hasOverflow: false`
- 768px Tablet Portrait: `hasOverflow: false`
- 1024px Tablet Landscape: `hasOverflow: false`
- 1440px Desktop: `hasOverflow: false`
- 2560px QHD: `hasOverflow: false`
- 3840px 4K: `hasOverflow: false`
- All 4 themes (Dark, Light, High-Contrast, Amber): verified clean
- All 4 views (Pipeline, Openings, Proposals, Profile): verified clean
