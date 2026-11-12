# First 10 tasks: SIR Business sector Repair shop (صيانة أجهزة وموبايلات)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/repair-shop.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add ticket intake screen with quote generation (M1)

**Brief:** Build the ticket screen: enter device type (phone/appliance), imei/serial, complaint, generate quote (quotePiasters), set status (draft). Done when the ticket is saved with draft status and quote amount.

**Files:** packages/core/src/sectors/repair-shop/ and packages/core/src/sectors/repair-shop/__tests__/

**Done when:** When ticket intake works end-to-end with quote generation

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add customer approval via SMS/link (M1)

**Brief:** Build the approval screen: via SMS link or web, view ticket quote, approve/reject, update status to customer-approved. Done when the approval updates the ticket status and saves the approval method.

**Files:** packages/core/src/sectors/repair-shop/ and packages/core/src/sectors/repair-shop/__tests__/

**Done when:** When customer approval via link works end-to-end with status update

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add ticket list with status filters (M1)

**Brief:** Build the ticket list: all tickets with device type, imei/serial, complaint, quote amount, status, approval status, completed. Done when the list loads and filters correctly by status.

**Files:** packages/core/src/sectors/repair-shop/ and packages/core/src/sectors/repair-shop/__tests__/

**Done when:** When ticket list works and filters by status correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add spare part catalogue with reorder point (M1)

**Brief:** Build the spare part catalogue: grid of spare parts with name, model, price, stock qty, reorder point, reorder badge. Done when the catalogue loads and displays parts with reorder badges when below threshold.

**Files:** packages/core/src/sectors/repair-shop/ and packages/core/src/sectors/repair-shop/__tests__/

**Done when:** When spare part catalogue displays live data with reorder badges

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add part replacement screen (M1)

**Brief:** Build the part replacement screen: select spare part, enter quantity, install, record installedAt, update ticket status to completed. Done when the replacement is saved and ticket status updates correctly.

**Files:** packages/core/src/sectors/repair-shop/ and packages/core/src/sectors/repair-shop/__tests__/

**Done when:** When part replacement works end-to-end with status update

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add cash register with ticket scanning (M1)

**Brief:** Build the cash register: scan ticket reference or device IMEI, record payment, print receipt with ticket details. Done when the sale records the ticket and receipt prints correctly.

**Files:** packages/core/src/sectors/repair-shop/ and packages/core/src/sectors/repair-shop/__tests__/

**Done when:** When cash register works end-to-end with ticket scanning and receipt prints

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add ticket pipeline report (M2)

**Brief:** Build the report showing ticket pipeline by status and average duration per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/repair-shop/ and packages/core/src/sectors/repair-shop/__tests__/

**Done when:** When ticket pipeline report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add spare part stock report (M2)

**Brief:** Build the report showing total stock, reorder point, items below reorder point, reorder frequency. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/repair-shop/ and packages/core/src/sectors/repair-shop/__tests__/

**Done when:** When spare part stock report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add part replacement volume report (M2)

**Brief:** Build the report showing per ticket how many parts replaced, per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/repair-shop/ and packages/core/src/sectors/repair-shop/__tests__/

**Done when:** When part replacement volume report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add customer repeat rate report (M2)

**Brief:** Build the report showing visit count per customer, total spent per customer, re-book rate. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/repair-shop/ and packages/core/src/sectors/repair-shop/__tests__/

**Done when:** When customer repeat rate report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed
