# First 10 tasks: SIR Business sector Factory workshop (مصنع وورشة إنتاج)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/factory-workshop.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add bill of materials editor (M1)

**Brief:** Build the BOM screen: product name/SKU, component lines (name, quantity per unit), save BOM, set status. Done when the BOM is saved and can be selected for work order creation.

**Files:** packages/core/src/sectors/factory-workshop/ and packages/core/src/sectors/factory-workshop/__tests__/

**Done when:** When BOM editor works and BOM can be selected for work order

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add work order creation and component consumption (M1)

**Brief:** Build the work order screen: select BOM, enter customer and phone, quantity ordered, set status, due date, compute components needed. Done when the work order saves and component consumption tracker updates correctly.

**Files:** packages/core/src/sectors/factory-workshop/ and packages/core/src/sectors/factory-workshop/__tests__/

**Done when:** When work order creation works end-to-end with component consumption

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add component consumption tracker (M1)

**Brief:** Build the component tracker: per work order, view components, mark consumed, update remaining qty. Done when marking a component as consumed updates the remaining qty correctly.

**Files:** packages/core/src/sectors/factory-workshop/ and packages/core/src/sectors/factory-workshop/__tests__/

**Done when:** When component consumption tracker works end-to-end with remaining qty update

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add output record screen (M1)

**Brief:** Build the output screen: enter actual output qty, compare to expected, enter scrap qty, add notes, save. Done when the output record saves and the work order status updates correctly.

**Files:** packages/core/src/sectors/factory-workshop/ and packages/core/src/sectors/factory-workshop/__tests__/

**Done when:** When output record works end-to-end with work order status update

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add work order list with status and due date (M1)

**Brief:** Build the work order list: all orders with status, customer, quantity ordered, completed, scrapped, due date. Done when the list loads and filters correctly by status.

**Files:** packages/core/src/sectors/factory-workshop/ and packages/core/src/sectors/factory-workshop/__tests__/

**Done when:** When work order list works and filters by status correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add BOM component consumption report (M2)

**Brief:** Build the report showing per BOM which components are low or consumed per period and reorder suggestions. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/factory-workshop/ and packages/core/src/sectors/factory-workshop/__tests__/

**Done when:** When BOM component consumption report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add output summary report (M2)

**Brief:** Build the report showing actual vs expected per period, scrap total per period and reason. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/factory-workshop/ and packages/core/src/sectors/factory-workshop/__tests__/

**Done when:** When output summary report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add revenue per product report (M2)

**Brief:** Build the report showing total completed work orders and revenue per product type per month. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/factory-workshop/ and packages/core/src/sectors/factory-workshop/__tests__/

**Done when:** When revenue per product report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add supplier performance report (M2)

**Brief:** Build the report showing lead time actual vs expected per supplier per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/factory-workshop/ and packages/core/src/sectors/factory-workshop/__tests__/

**Done when:** When supplier performance report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add onboarding flow for initial workshop setup (M1)

**Brief:** Build the onboarding flow: workshop basics, initial BOM, work order types, staff addition. Done when the flow completes and the workshop appears with all defaults.

**Files:** packages/core/src/sectors/factory-workshop/ and packages/core/src/sectors/factory-workshop/__tests__/

**Done when:** When onboarding flow works end-to-end and workshop is created

**Check:** `npm test -- sectors/{slug}` prints passed
