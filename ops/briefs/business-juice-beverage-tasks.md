# First 10 tasks: SIR Business sector Juice and drinks (عصائر ومشروبات)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/juice-beverage.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add modifier grid with sizes and extras (M1)

**Brief:** Build the modifier grid: sizes (small/medium/large), extras (extra shot, syrup, whipped cream), price delta per modifier, required/optional flag. Done when the grid loads and modifiers can be added to an order.

**Files:** packages/core/src/sectors/juice-beverage/ and packages/core/src/sectors/juice-beverage/__tests__/

**Done when:** When modifier grid works and modifiers can be added to orders

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add flavour matrix (M1)

**Brief:** Build the flavour screen: list of flavours with ingredients Ar/En, price delta, default flag. Done when the flavour matrix loads and flavours can be selected.

**Files:** packages/core/src/sectors/juice-beverage/ and packages/core/src/sectors/juice-beverage/__tests__/

**Done when:** When flavour matrix works and flavours can be selected per order

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add daily prep checklist (M1)

**Brief:** Build the daily prep screen: date, flavours prepared (array), modifiers used (array), waste in piasters, notes. Done when the prep is saved and waste is tracked.

**Files:** packages/core/src/sectors/juice-beverage/ and packages/core/src/sectors/juice-beverage/__tests__/

**Done when:** When daily prep checklist works end-to-end with waste tracking

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add order creation with modifiers (M1)

**Brief:** Build the order screen: select menu item, add modifiers from the grid, set quantity, compute total with modifier deltas, set status. Done when the order saves all fields and the receipt prints correctly.

**Files:** packages/core/src/sectors/juice-beverage/ and packages/core/src/sectors/juice-beverage/__tests__/

**Done when:** When order creation works end-to-end with modifiers and receipt prints

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add sales by hour report (M1)

**Brief:** Build the report showing revenue per hour and per day. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/juice-beverage/ and packages/core/src/sectors/juice-beverage/__tests__/

**Done when:** When sales by hour report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add flavour popularity report (M1)

**Brief:** Build the report showing which flavours sell most and revenue per flavour per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/juice-beverage/ and packages/core/src/sectors/juice-beverage/__tests__/

**Done when:** When flavour popularity report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add modifier performance report (M1)

**Brief:** Build the report which sizes and extras are most added and revenue per modifier per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/juice-beverage/ and packages/core/src/sectors/juice-beverage/__tests__/

**Done when:** When modifier performance report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add daily waste log report (M1)

**Brief:** Build the report showing waste in piasters per period, reasons, trends. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/juice-beverage/ and packages/core/src/sectors/juice-beverage/__tests__/

**Done when:** When daily waste log report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add stock turnover report (M1)

**Brief:** Build the report showing current stock levels, reorder frequency, waste vs stock ratio. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/juice-beverage/ and packages/core/src/sectors/juice-beverage/__tests__/

**Done when:** When stock turnover report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add onboarding flow for initial juice shop setup (M1)

**Brief:** Build the onboarding flow: shop basics, initial menu, modifier grid, flavour matrix, daily prep checklist, staff addition. Done when the flow completes and the shop appears with all defaults.

**Files:** packages/core/src/sectors/juice-beverage/ and packages/core/src/sectors/juice-beverage/__tests__/

**Done when:** When onboarding flow works end-to-end and shop is created

**Check:** `npm test -- sectors/{slug}` prints passed
