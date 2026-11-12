# First 10 tasks: SIR Business sector Optical shop (محل نظارات)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/optical-shop.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add frame catalogue with availability badge (M1)

**Brief:** Build the frame catalogue: grid of frames with name, brand, price, size, color, availability badge. Done when the catalogue loads and displays frames with correct availability badges.

**Files:** packages/core/src/sectors/optical-shop/ and packages/core/src/sectors/optical-shop/__tests__/

**Done when:** When frame catalogue displays live data with availability badges

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add lens type catalogue (M1)

**Brief:** Build the lens type catalogue: list of lens types with index, coating, price, cost. Done when the catalogue loads and displays lens types correctly.

**Files:** packages/core/src/sectors/optical-shop/ and packages/core/src/sectors/optical-shop/__tests__/

**Done when:** When lens type catalogue displays live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add prescription editor per client (M1)

**Brief:** Build the prescription screen: sphere, cylinder, axis, add, pupillary distance, validUntil, astigmatism flag, save per client. Done when the prescription is saved and linked to a client.

**Files:** packages/core/src/sectors/optical-shop/ and packages/core/src/sectors/optical-shop/__tests__/

**Done when:** When prescription editor works and saves per client

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add order creation with deposit and balance (M1)

**Brief:** Build the order screen: select frame, lens type, prescription, compute total, set deposit and balance, set status. Done when the order saves all fields and status updates correctly.

**Files:** packages/core/src/sectors/optical-shop/ and packages/core/src/sectors/optical-shop/__tests__/

**Done when:** When order creation works end-to-end with deposit and balance

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add client profile with prescription history (M1)

**Brief:** Build the client profile: visit count, total spent, last visit, prescription history. Done when the profile saves and displays correct data.

**Files:** packages/core/src/sectors/optical-shop/ and packages/core/src/sectors/optical-shop/__tests__/

**Done when:** When client profile works and displays live data with prescription history

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add order status tracker with pipeline (M1)

**Brief:** Build the order tracker: per order view progress (draft/confirmed/in-progress/ready/ready-for-pickup), print ready notice. Done when the tracker updates status and prints ready notice correctly.

**Files:** packages/core/src/sectors/optical-shop/ and packages/core/src/sectors/optical-shop/__tests__/

**Done when:** When order status tracker works end-to-end with pipeline and receipt printing

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add cash register with frame/Order scanning (M1)

**Brief:** Build the cash register: scan frame or order reference, record payment, print receipt. Done when the sale records correctly and receipt prints.

**Files:** packages/core/src/sectors/optical-shop/ and packages/core/src/sectors/optical-shop/__tests__/

**Done when:** When cash register works end-to-end and receipt prints correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add frame sales by model report (M2)

**Brief:** Build the report showing count per model/brand per month and revenue per model. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/optical-shop/ and packages/core/src/sectors/optical-shop/__tests__/

**Done when:** When frame sales report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add lens type performance report (M2)

**Brief:** Build the report showing which lens types sell most and revenue per lens type per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/optical-shop/ and packages/core/src/sectors/optical-shop/__tests__/

**Done when:** When lens type performance report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add prescription volume per optician report (M2)

**Brief:** Build the report showing how many prescriptions per optician per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/optical-shop/ and packages/core/src/sectors/optical-shop/__tests__/

**Done when:** When prescription volume report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed
