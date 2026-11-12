# First 10 tasks: SIR Business sector Dessert and ice cream (حلويات وأيس كريم)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/dessert-ice-cream.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add flavour catalogue with variants (M1)

**Brief:** Build the flavour catalogue: grid of flavours with name, variants Ar/En, base type, price, default flag. Done when the catalogue loads and displays flavours with variant badges correctly.

**Files:** packages/core/src/sectors/dessert-ice-cream/ and packages/core/src/sectors/dessert-ice-cream/__tests__/

**Done when:** When flavour catalogue displays live data with variants

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add assembly notes editor (M1)

**Brief:** Build the assembly notes screen: select flavour, enter steps Ar/En (marble-slab style), set as default. Done when the notes are saved and linked to the flavour.

**Files:** packages/core/src/sectors/dessert-ice-cream/ and packages/core/src/sectors/dessert-ice-cream/__tests__/

**Done when:** When assembly notes editor works and links to flavour

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add bundle manager (M1)

**Brief:** Build the bundle screen: select flavour IDs, set discount percent, set bundle price, set status. Done when the bundle is saved and can be applied to orders.

**Files:** packages/core/src/sectors/dessert-ice-cream/ and packages/core/src/sectors/dessert-ice-cream/__tests__/

**Done when:** When bundle manager works and bundle can be applied to orders

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add order creation with bundle discount (M1)

**Brief:** Build the order screen: select flavour, set quantity, compute total, apply bundle discount if applicable, set status. Done when the order saves all fields and receipt prints correctly.

**Files:** packages/core/src/sectors/dessert-ice-cream/ and packages/core/src/sectors/dessert-ice-cream/__tests__/

**Done when:** When order creation works end-to-end with bundle discount and receipt prints

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add flavour popularity report (M1)

**Brief:** Build the report showing which flavours sell most and revenue per flavour per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/dessert-ice-cream/ and packages/core/src/sectors/dessert-ice-cream/__tests__/

**Done when:** When flavour popularity report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add bundle volume report (M1)

**Brief:** Build the report showing how many bundles created and revenue per bundle per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/dessert-ice-cream/ and packages/core/src/sectors/dessert-ice-cream/__tests__/

**Done when:** When bundle volume report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add daily waste log report (M1)

**Brief:** Build the report showing waste in piasters per period, reasons, trends. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/dessert-ice-cream/ and packages/core/src/sectors/dessert-ice-cream/__tests__/

**Done when:** When daily waste log report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add stock turnover report (M1)

**Brief:** Build the report showing current stock levels, reorder frequency, waste vs stock ratio. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/dessert-ice-cream/ and packages/core/src/sectors/dessert-ice-cream/__tests__/

**Done when:** When stock turnover report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add onboarding flow for initial dessert shop setup (M1)

**Brief:** Build the onboarding flow: shop basics, initial flavours, assembly notes, bundle structure, staff addition. Done when the flow completes and the shop appears with all defaults.

**Files:** packages/core/src/sectors/dessert-ice-cream/ and packages/core/src/sectors/dessert-ice-cream/__tests__/

**Done when:** When onboarding flow works end-to-end and shop is created

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add flavour popularity trend report (M2)

**Brief:** Build the report showing which flavours are gaining/losing popularity per month. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/dessert-ice-cream/ and packages/core/src/sectors/dessert-ice-cream/__tests__/

**Done when:** When flavour popularity trend report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed
