# First 10 tasks: SIR Business sector Stationery and gifts (هدايا ومكتبة)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/stationery-gifts.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add product catalogue with personalisable flag (M1)

**Brief:** Build the product catalogue: grid of items with name, price, condition, personalisable badge. Done when the catalogue loads and displays items with personalisable badge correctly.

**Files:** packages/core/src/sectors/stationery-gifts/ and packages/core/src/sectors/stationery-gifts/__tests__/

**Done when:** When product catalogue displays live data with personalisable badges

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add gift wrap selector with preview (M1)

**Brief:** Build the gift wrap screen: wrapping paper, ribbon, card options, preview of packaged item. Done when the selector saves the wrap choice per order and displays the preview.

**Files:** packages/core/src/sectors/stationery-gifts/ and packages/core/src/sectors/stationery-gifts/__tests__/

**Done when:** When gift wrap selector works and saves choice per order

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add personalisation text preview (M1)

**Brief:** Build the personalisation screen: engraving text input, real-time preview on the product item. Done when the text is saved and preview updates instantly.

**Files:** packages/core/src/sectors/stationery-gifts/ and packages/core/src/sectors/stationery-gifts/__tests__/

**Done when:** When personalisation text preview works end-to-end

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add customer profile with purchase history (M1)

**Brief:** Build the customer profile screen: purchase history, total spent, notes, opt-in status. Done when the profile saves and displays customer data correctly.

**Files:** packages/core/src/sectors/stationery-gifts/ and packages/core/src/sectors/stationery-gifts/__tests__/

**Done when:** When customer profile works and displays live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add order creation with gift wrap and personalisation (M2)

**Brief:** Build the order screen: add items, select gift wrap, add personalisation, apply discount, tender payment. Done when the order saves all fields and the receipt prints correctly.

**Files:** packages/core/src/sectors/stationery-gifts/ and packages/core/src/sectors/stationery-gifts/__tests__/

**Done when:** When order creation works end-to-end with gift wrap and personalisation

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add cash register with gift wrap and scanning (M2)

**Brief:** Build the cash register: scan items, apply gift wrap, tender payment, print receipt with gift note. Done when the sale records all fields and receipt prints correctly.

**Files:** packages/core/src/sectors/stationery-gifts/ and packages/core/src/sectors/stationery-gifts/__tests__/

**Done when:** When cash register works end-to-end and receipt prints with gift note

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add customer LTV report (M3)

**Brief:** Build the LTV report: total spent, visit frequency, average ticket per customer. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/stationery-gifts/ and packages/core/src/sectors/stationery-gifts/__tests__/

**Done when:** When LTV report pulls live data and displays correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add order average report (items, gift wrap, personalisation rates) (M3)

**Brief:** Build the report showing items per order, gift wrap rate, personalisation rate per period. Done when the report computes from Firestore and displays correct rates.

**Files:** packages/core/src/sectors/stationery-gifts/ and packages/core/src/sectors/stationery-gifts/__tests__/

**Done when:** When order average report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add inventory aging report by category (M4)

**Brief:** Build the aging report: items in stock by category and how long. Done when the report computes from Firestore and displays correct aging buckets.

**Files:** packages/core/src/sectors/stationery-gifts/ and packages/core/src/sectors/stationery-gifts/__tests__/

**Done when:** When inventory aging report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add onboarding flow for initial gift shop setup (M1)

**Brief:** Build the onboarding flow: shop basics, initial inventory, product categories with personalisable flag, staff addition. Done when the flow completes and the shop appears with all defaults.

**Files:** packages/core/src/sectors/stationery-gifts/ and packages/core/src/sectors/stationery-gifts/__tests__/

**Done when:** When onboarding flow works end-to-end and shop is created

**Check:** `npm test -- sectors/{slug}` prints passed
