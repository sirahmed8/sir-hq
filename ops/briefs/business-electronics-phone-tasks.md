# First 10 tasks: SIR Business sector Electronics and mobile (إلكترونيات وموبايلات)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/electronics-phone.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add IMEI-tracked phone catalogue (M1)

**Brief:** Build the phone catalogue: grid of phone units with IMEI, model, colour, storage, price, warranty status, fault note. Done when the catalogue loads and displays units with IMEI badges correctly.

**Files:** packages/core/src/sectors/electronics-phone/ and packages/core/src/sectors/electronics-phone/__tests__/

**Done when:** When phone catalogue displays live data with IMEI tracking

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add repair job creation and status tracker (M1)

**Brief:** Build the repair job screen: enter phone IMEI, complaint, generate quote, set status (draft/approved/in-progress/completed). Done when the job is saved and status updates propagate.

**Files:** packages/core/src/sectors/electronics-phone/ and packages/core/src/sectors/electronics-phone/__tests__/

**Done when:** When repair job creation works end-to-end with status tracking

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add warranty claim creation and tracker (M1)

**Brief:** Build the warranty claim screen: enter phone IMEI, customer details, issue, set status (open/pending/resolved). Done when the claim is saved and status updates propagate.

**Files:** packages/core/src/sectors/electronics-phone/ and packages/core/src/sectors/electronics-phone/__tests__/

**Done when:** When warranty claim creation works end-to-end with status tracking

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add repair status tracker per job (M1)

**Brief:** Build the repair tracker: per job view progress, mark completed, print completion receipt. Done when the tracker updates job status and prints receipt correctly.

**Files:** packages/core/src/sectors/electronics-phone/ and packages/core/src/sectors/electronics-phone/__tests__/

**Done when:** When repair status tracker works end-to-end and receipt prints

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add warranty claim tracker per unit (M1)

**Brief:** Build the warranty tracker: per unit view status, resolution, update status. Done when the tracker updates claim status and displays correct state.

**Files:** packages/core/src/sectors/electronics-phone/ and packages/core/src/sectors/electronics-phone/__tests__/

**Done when:** When warranty claim tracker works end-to-end and displays correct state

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add cash register with IMEI/SKU scanning (M1)

**Brief:** Build the cash register: scan IMEI or SKU, apply discount, tender payment, print receipt with IMEI. Done when the sale records IMEI and receipt prints correctly.

**Files:** packages/core/src/sectors/electronics-phone/ and packages/core/src/sectors/electronics-phone/__tests__/

**Done when:** When cash register works end-to-end with IMEI scanning and receipt prints

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add phone inventory by model report (M2)

**Brief:** Build the report showing count per model/colour/storage and turnover rate. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/electronics-phone/ and packages/core/src/sectors/electronics-phone/__tests__/

**Done when:** When phone inventory report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add repair pipeline report (M2)

**Brief:** Build the report showing repair jobs by status (draft/approved/in-progress/completed) and average duration. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/electronics-phone/ and packages/core/src/sectors/electronics-phone/__tests__/

**Done when:** When repair pipeline report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add warranty claim rate report (M2)

**Brief:** Build the report showing warranty claims by status (open/pending/resolved) and resolution time. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/electronics-phone/ and packages/core/src/sectors/electronics-phone/__tests__/

**Done when:** When warranty claim rate report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add onboarding flow for initial electronics shop setup (M1)

**Brief:** Build the onboarding flow: shop basics, initial phone inventory with IMEI, repair types, staff addition. Done when the flow completes and the shop appears with all defaults.

**Files:** packages/core/src/sectors/electronics-phone/ and packages/core/src/sectors/electronics-phone/__tests__/

**Done when:** When onboarding flow works end-to-end and shop is created

**Check:** `npm test -- sectors/{slug}` prints passed
