# First 10 tasks: SIR Business sector Clothing retail (ملابس)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/clothing-retail.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add product catalogue with color/size badges (M1)

**Brief:** Build the product catalogue: grid of items with name, price, color badge, size badge, condition (new/used), availability. Done when the catalogue loads and displays items with correct variant badges.

**Files:** packages/core/src/sectors/clothing-retail/ and packages/core/src/sectors/clothing-retail/__tests__/

**Done when:** When product catalogue displays live data with variant badges

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add variant manager (M1)

**Brief:** Build the variant screen: add/edit variant (color, size, price delta, default flag, stock qty). Done when the variant is saved and linked to the product and stock updates correctly.

**Files:** packages/core/src/sectors/clothing-retail/ and packages/core/src/sectors/clothing-retail/__tests__/

**Done when:** When variant manager works and links variant to product with stock update

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add markdown tracker (M1)

**Brief:** Build the markdown screen: set markdown % per product per period, track original price vs discounted price, apply at till. Done when the markdown is saved and the till applies the discount correctly.

**Files:** packages/core/src/sectors/clothing-retail/ and packages/core/src/sectors/clothing-retail/__tests__/

**Done when:** When markdown tracker works end-to-end with discount application at till

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add exchange log (M1)

**Brief:** Build the exchange screen: record exchange reason (size/color/defect), update stock, issue refund note. Done when the exchange is saved and stock updates correctly and note is issued.

**Files:** packages/core/src/sectors/clothing-retail/ and packages/core/src/sectors/clothing-retail/__tests__/

**Done when:** When exchange log works end-to-end with stock update and refund note

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add customer profile with purchase history (M1)

**Brief:** Build the customer profile: purchase history, total spent, notes, opt-in status. Done when the profile saves and displays correct data.

**Files:** packages/core/src/sectors/clothing-retail/ and packages/core/src/sectors/clothing-retail/__tests__/

**Done when:** When customer profile works and displays live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add cash register with variant scanning and markdown (M1)

**Brief:** Build the cash register: scan SKU or variant, apply markdown/discount, tender payment, print receipt. Done when the sale records variant and markdown correctly and receipt prints.

**Files:** packages/core/src/sectors/clothing-retail/ and packages/core/src/sectors/clothing-retail/__tests__/

**Done when:** When cash register works end-to-end with variant scanning and markdown

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add variant performance report (M2)

**Brief:** Build the report showing which color/size combinations sell most and revenue per variant per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/clothing-retail/ and packages/core/src/sectors/clothing-retail/__tests__/

**Done when:** When variant performance report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add markdown effectiveness report (M2)

**Brief:** Build the report showing original price vs discounted price per period and sell-through rate at discount. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/clothing-retail/ and packages/core/src/sectors/clothing-retail/__tests__/

**Done when:** When markdown effectiveness report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add exchange volume report (M2)

**Brief:** Build the report showing exchanges per period, reasons, refund amount per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/clothing-retail/ and packages/core/src/sectors/clothing-retail/__tests__/

**Done when:** When exchange volume report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add onboarding flow for initial clothing shop setup (M1)

**Brief:** Build the onboarding flow: shop basics, initial inventory, product categories with variant flag, staff addition. Done when the flow completes and the shop appears with all defaults.

**Files:** packages/core/src/sectors/clothing-retail/ and packages/core/src/sectors/clothing-retail/__tests__/

**Done when:** When onboarding flow works end-to-end and shop is created

**Check:** `npm test -- sectors/{slug}` prints passed
