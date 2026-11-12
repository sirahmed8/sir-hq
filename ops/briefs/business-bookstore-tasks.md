# First 10 tasks: SIR Business sector Bookstore (مكتبة بيع)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/bookstore.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add product catalogue grid with condition states (M1)

**Brief:** Build the product catalogue: grid of books with title, author, ISBN, price, condition (new/used), availability. Done when the catalogue loads and displays books from Firestore with correct condition badges.

**Files:** packages/core/src/sectors/bookstore/ and packages/core/src/sectors/bookstore/__tests__/

**Done when:** When product catalogue displays live data with condition badges

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add wishlist manager per customer (M1)

**Brief:** Build the wishlist screen: customer wishes, notify when available, prioritise purchases. Done when a wishlist item can be added and the notification flag is saved.

**Files:** packages/core/src/sectors/bookstore/ and packages/core/src/sectors/bookstore/__tests__/

**Done when:** When wishlist manager works and saves notification flag

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add customer profile with purchase history (M1)

**Brief:** Build the customer profile screen: purchase history, total spent, wishlist, opt-in status. Done when the profile saves and displays customer data correctly.

**Files:** packages/core/src/sectors/bookstore/ and packages/core/src/sectors/bookstore/__tests__/

**Done when:** When customer profile works and displays live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add purchase order receipt screen (M2)

**Brief:** Build the purchase order screen: receive shipment from supplier, record items, update stock. Done when the order saves and stock increments correctly.

**Files:** packages/core/src/sectors/bookstore/ and packages/core/src/sectors/bookstore/__tests__/

**Done when:** When purchase order works end-to-end and stock updates

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add cash register with SKU scanning (M2)

**Brief:** Build the cash register: scan SKU, apply discount, tender payment, print receipt. Done when the sale is recorded and receipt prints correctly.

**Files:** packages/core/src/sectors/bookstore/ and packages/core/src/sectors/bookstore/__tests__/

**Done when:** When cash register works end-to-end and receipt prints

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add customer lifetime value report (M3)

**Brief:** Build the LTV report: total spent, visit frequency, average ticket per customer. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/bookstore/ and packages/core/src/sectors/bookstore/__tests__/

**Done when:** When LTV report pulls live data and displays correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add wishlist conversion report (M3)

**Brief:** Build the report showing how many wishes turned into purchases per period. Done when the report computes from Firestore and displays correct conversion rates.

**Files:** packages/core/src/sectors/bookstore/ and packages/core/src/sectors/bookstore/__tests__/

**Done when:** When wishlist conversion report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add inventory aging report by condition (M4)

**Brief:** Build the aging report: copies in stock by condition (new/used) and how long. Done when the report computes from Firestore and displays correct aging buckets.

**Files:** packages/core/src/sectors/bookstore/ and packages/core/src/sectors/bookstore/__tests__/

**Done when:** When inventory aging report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add onboarding flow for initial bookstore setup (M1)

**Brief:** Build the onboarding flow: shop basics, initial inventory, product categories, staff addition. Done when the flow completes and the shop appears with all defaults.

**Files:** packages/core/src/sectors/bookstore/ and packages/core/src/sectors/bookstore/__tests__/

**Done when:** When onboarding flow works end-to-end and shop is created

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add personalisation engraving flow (M1)

**Brief:** Build the engraving flow: enter text, real-time preview on product item, save engraving details per order. Done when the engraving text is saved and preview updates instantly.

**Files:** packages/core/src/sectors/bookstore/ and packages/core/src/sectors/bookstore/__tests__/

**Done when:** When personalisation engraving flow works end-to-end

**Check:** `npm test -- sectors/{slug}` prints passed
