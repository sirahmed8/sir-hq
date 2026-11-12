# First 10 tasks: SIR Business sector Print shop (مطبعة)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/print-shop.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add job ticket list and detail screen (M1)

**Brief:** Build the job ticket screen: list all tickets with type, client, dimensions, copies, total, deposit, balance, status, ready date. Done when the ticket list loads and the detail screen shows full ticket info.

**Files:** packages/core/src/sectors/print-shop/ and packages/core/src/sectors/print-shop/__tests__/

**Done when:** When job ticket list and detail screen works and displays live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add paper stock level screen (M1)

**Brief:** Build the paper stock screen: sheets in stock, minimum threshold, low-stock alert, reorder suggestion. Done when the stock level saves and low-stock alert triggers correctly.

**Files:** packages/core/src/sectors/print-shop/ and packages/core/src/sectors/print-shop/__tests__/

**Done when:** When paper stock level works and alerts trigger correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add proof manager with upload and status (M1)

**Brief:** Build the proof screen: upload client proof PDF, status (pending/approved/rejected), approve/reject, add notes. Done when the proof is saved and status updates correctly.

**Files:** packages/core/src/sectors/print-shop/ and packages/core/src/sectors/print-shop/__tests__/

**Done when:** When proof manager works end-to-end with status tracking

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add proof gallery per job (M1)

**Brief:** Build the proof gallery: view all proofs per job, approve/reject per proof. Done when the gallery pulls and displays all proofs for a job and approve/reject works.

**Files:** packages/core/src/sectors/print-shop/ and packages/core/src/sectors/print-shop/__tests__/

**Done when:** When proof gallery works end-to-end with per-job display

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add purchase order and paper stock update (M1)

**Brief:** Build the purchase order screen: receive from supplier, update paper stock, record cost. Done when the order saves and paper stock increments correctly and low-stock alert triggers if below threshold.

**Files:** packages/core/src/sectors/print-shop/ and packages/core/src/sectors/print-shop/__tests__/

**Done when:** When purchase order works end-to-end with stock update and alert

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add cash register with job ticket scanning (M1)

**Brief:** Build the cash register: scan job ticket reference, record payment, print receipt with job details. Done when the sale records the job ticket and receipt prints correctly.

**Files:** packages/core/src/sectors/print-shop/ and packages/core/src/sectors/print-shop/__tests__/

**Done when:** When cash register works end-to-end with job ticket scanning and receipt prints

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add job ticket volume per period report (M2)

**Brief:** Build the report showing tickets created, proofing, printing, done per month. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/print-shop/ and packages/core/src/sectors/print-shop/__tests__/

**Done when:** When job ticket volume report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add proof approval rate report (M2)

**Brief:** Build the report showing approved vs rejected per period and reasons for rejection. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/print-shop/ and packages/core/src/sectors/print-shop/__tests__/

**Done when:** When proof approval rate report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add paper stock turnover report (M2)

**Brief:** Build the report showing sheets per period, low-stock alerts per period, reorder frequency. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/print-shop/ and packages/core/src/sectors/print-shop/__tests__/

**Done when:** When paper stock turnover report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add revenue per job type report (M2)

**Brief:** Build the report showing posters vs banners vs flyers vs invitations revenue per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/print-shop/ and packages/core/src/sectors/print-shop/__tests__/

**Done when:** When revenue per job type report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed
