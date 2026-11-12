# First 10 tasks: SIR Business sector Hardware and materials (عدد ومواد بناء)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/hardware-materials.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add product catalogue with contractor flag (M1)

**Brief:** Build the product catalogue: grid of materials with name, price per unit, unit measure, contractor badge. Done when the catalogue loads and displays items with contractor badges correctly.

**Files:** packages/core/src/sectors/hardware-materials/ and packages/core/src/sectors/hardware-materials/__tests__/

**Done when:** When product catalogue displays live data with contractor flags

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add contractor account screen (M1)

**Brief:** Build the contractor screen: credit limit, credit used, payment terms, status, assigned rep, history. Done when the contractor is saved and credit used updates correctly.

**Files:** packages/core/src/sectors/hardware-materials/ and packages/core/src/sectors/hardware-materials/__tests__/

**Done when:** When contractor account works and credit tracking is persistent

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add quote editor with validity and approval (M1)

**Brief:** Build the quote screen: select lines, set validUntil, compute total, approve/reject. Done when the quote saves with validity and approval status.

**Files:** packages/core/src/sectors/hardware-materials/ and packages/core/src/sectors/hardware-materials/__tests__/

**Done when:** When quote editor works end-to-end with validity and approval

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add delivery scheduler with waypoints and ETA (M1)

**Brief:** Build the delivery scheduler: assign orders to run, view waypoints, ETA, update status. Done when the scheduler saves the run and displays ETA correctly.

**Files:** packages/core/src/sectors/hardware-materials/ and packages/core/src/sectors/hardware-materials/__tests__/

**Done when:** When delivery scheduler works end-to-end with ETA tracking

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add cash register with contractor discount (M2)

**Brief:** Build the cash register: scan SKU, apply contractor discount, tender payment, print receipt. Done when the sale records contractor discount and receipt prints correctly.

**Files:** packages/core/src/sectors/hardware-materials/ and packages/core/src/sectors/hardware-materials/__tests__/

**Done when:** When cash register works end-to-end with contractor discount

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add contractor credit aging report (M2)

**Brief:** Build the report showing total credit used vs limit, aging of outstanding, top contractors. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/hardware-materials/ and packages/core/src/sectors/hardware-materials/__tests__/

**Done when:** When contractor credit aging report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add quote volume report (M2)

**Brief:** Build the report showing quotes created, approved, rejected per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/hardware-materials/ and packages/core/src/sectors/hardware-materials/__tests__/

**Done when:** When quote volume report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add delivery run efficiency report (M2)

**Brief:** Build the report showing orders per run, on-time rate, average duration. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/hardware-materials/ and packages/core/src/sectors/hardware-materials/__tests__/

**Done when:** When delivery run efficiency report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add inventory aging report by category (M3)

**Brief:** Build the aging report: items in stock by category and how long. Done when the report computes from Firestore and displays correct aging buckets.

**Files:** packages/core/src/sectors/hardware-materials/ and packages/core/src/sectors/hardware-materials/__tests__/

**Done when:** When inventory aging report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add onboarding flow for initial hardware store setup (M1)

**Brief:** Build the onboarding flow: shop basics, initial inventory, contractor types, staff addition. Done when the flow completes and the shop appears with all defaults.

**Files:** packages/core/src/sectors/hardware-materials/ and packages/core/src/sectors/hardware-materials/__tests__/

**Done when:** When onboarding flow works end-to-end and shop is created

**Check:** `npm test -- sectors/{slug}` prints passed
