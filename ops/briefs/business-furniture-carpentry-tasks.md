# First 10 tasks: SIR Business sector Furniture and carpentry (أثاث ونجارة)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/furniture-carpentry.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add design spec editor with Ar/En sketches and dimensions (M1)

**Brief:** Build the design spec screen: client name/phone, sketches Ar/En, dimensions l/w/h, material and finish. Done when the spec is saved and linked to an order.

**Files:** packages/core/src/sectors/furniture-carpentry/ and packages/core/src/sectors/furniture-carpentry/__tests__/

**Done when:** When design spec editor works and links to order creation

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add order creation with deposit and delivery slot (M1)

**Brief:** Build the order screen: select design spec, set deposit % and amount, compute balance, set delivery slot and date, set status. Done when the order saves all fields and the status updates correctly.

**Files:** packages/core/src/sectors/furniture-carpentry/ and packages/core/src/sectors/furniture-carpentry/__tests__/

**Done when:** When order creation works end-to-end with deposit and delivery slot

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add delivery slot scheduler with available slots (M1)

**Brief:** Build the delivery slot screen: available slots per day, assign slot, mark assigned, update status. Done when the scheduler saves the slot and displays availability correctly.

**Files:** packages/core/src/sectors/furniture-carpentry/ and packages/core/src/sectors/furniture-carpentry/__tests__/

**Done when:** When delivery slot scheduler works end-to-end with availability display

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add payment screen against order balance (M1)

**Brief:** Build the payment screen: record payment against order balance, update status, print receipt. Done when the payment saves and the order balance updates correctly.

**Files:** packages/core/src/sectors/furniture-carpentry/ and packages/core/src/sectors/furniture-carpentry/__tests__/

**Done when:** When payment screen works end-to-end and receipt prints

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add order book report with status breakdown (M2)

**Brief:** Build the report showing all orders by status, total revenue, total deposits, total outstanding balance. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/furniture-carpentry/ and packages/core/src/sectors/furniture-carpentry/__tests__/

**Done when:** When order book report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add deposit tracking report (M2)

**Brief:** Build the report showing total deposits received vs total orders, outstanding deposits per order. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/furniture-carpentry/ and packages/core/src/sectors/furniture-carpentry/__tests__/

**Done when:** When deposit tracking report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add delivery slot utilisation report (M2)

**Brief:** Build the report showing slots booked vs available per period, on-time delivery rate. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/furniture-carpentry/ and packages/core/src/sectors/furniture-carpentry/__tests__/

**Done when:** When delivery slot utilisation report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add revenue per period report (M2)

**Brief:** Build the report showing total sales, deposits collected, balance collected per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/furniture-carpentry/ and packages/core/src/sectors/furniture-carpentry/__tests__/

**Done when:** When revenue per period report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add popular materials and finishes report (M3)

**Brief:** Build the report showing which material/finish combinations are most requested. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/furniture-carpentry/ and packages/core/src/sectors/furniture-carpentry/__tests__/

**Done when:** When popular materials report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add onboarding flow for initial furniture shop setup (M1)

**Brief:** Build the onboarding flow: shop basics, initial design specs, deposit policy, staff addition. Done when the flow completes and the shop appears with all defaults.

**Files:** packages/core/src/sectors/furniture-carpentry/ and packages/core/src/sectors/furniture-carpentry/__tests__/

**Done when:** When onboarding flow works end-to-end and shop is created

**Check:** `npm test -- sectors/{slug}` prints passed
