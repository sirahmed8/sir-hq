# First 10 tasks: SIR Business sector Florist (محل زهور)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/florist.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add flower bundle catalogue (M1)

**Brief:** Build the bundle catalogue: list of bundles with name, flower types, price, bundle price, discount %, validity days, status. Done when the catalogue loads and displays bundles with correct badge and validity info.

**Files:** packages/core/src/sectors/florist/ and packages/core/src/sectors/florist/__tests__/

**Done when:** When bundle catalogue displays live data with validity and discount info

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add flower stock level with FEFO vase-life (M1)

**Brief:** Build the stock screen: stems per type, source, reorder point, FEFO vase-life badge and expiry alert. Done when the stock level saves and vase-life alert triggers correctly when approaching expiry.

**Files:** packages/core/src/sectors/florist/ and packages/core/src/sectors/florist/__tests__/

**Done when:** When flower stock level works and vase-life alerts trigger correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add customer order creation with delivery slot (M1)

**Brief:** Build the order screen: select bundle, enter customer name/phone, select delivery date/time slot, set status (pending/confirmed), compute total (bundle price - discount), set payment status. Done when the order saves all fields and the receipt prints correctly.

**Files:** packages/core/src/sectors/florist/ and packages/core/src/sectors/florist/__tests__/

**Done when:** When customer order creation works end-to-end with delivery slot and receipt prints

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add vase life tracker per flower type (M1)

**Brief:** Build the vase life screen: average days per flower type, care instructions Ar/En, fade alert per bundle. Done when the tracker saves and fade alerts update correctly.

**Files:** packages/core/src/sectors/florist/ and packages/core/src/sectors/florist/__tests__/

**Done when:** When vase life tracker works end-to-end with fade alerts

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add supplier management (M1)

**Brief:** Build the supplier screen: list of suppliers per shop, payment terms, lead time, contact. Done when the supplier is saved and appears in the purchase order screen.

**Files:** packages/core/src/sectors/florist/ and packages/core/src/sectors/florist/__tests__/

**Done when:** When supplier management works and suppliers appear in purchase orders

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add purchase order and stock update (M1)

**Brief:** Build the purchase order screen: create per shop, receive from supplier, update flower stock. Done when the order saves and stock increments correctly and FEFO badge updates.

**Files:** packages/core/src/sectors/florist/ and packages/core/src/sectors/florist/__tests__/

**Done when:** When purchase order works end-to-end with stock update and FEFO badge

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add cash register per shop with FEFO discount (M1)

**Brief:** Build the cash register per shop: scan bundle SKU or product, apply FEFO discount if urgent, tender payment, print receipt with bundle details and vase-life notes. Done when the sale records correctly and receipt prints with bundle name and vase-life notes.

**Files:** packages/core/src/sectors/florist/ and packages/core/src/sectors/florist/__tests__/

**Done when:** When cash register per shop works end-to-end with FEFO discount and receipt prints

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add bundle sales per period report (M1)

**Brief:** Build the report showing bundles created, sold, expired per month and revenue per bundle per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/florist/ and packages/core/src/sectors/florist/__tests__/

**Done when:** When bundle sales report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add FEFO vase-life aggregate report (M1)

**Brief:** Build the report showing total stems fading per period by days (3/5/7), value at risk, discounts applied. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/florist/ and packages/core/src/sectors/florist/__tests__/

**Done when:** When FEFO vase-life aggregate report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add order pipeline report (M1)

**Brief:** Build the report showing orders by status per period and average delivery time per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/florist/ and packages/core/src/sectors/florist/__tests__/

**Done when:** When order pipeline report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed
