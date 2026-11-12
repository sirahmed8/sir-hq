# First 10 tasks: SIR Business sector Wholesale and distribution (جملة وتوزيع)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/wholesale-distribution.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add product catalogue with price tier badges (M1)

**Brief:** Build the product catalogue: grid of products with name, price per unit, min/max order qty, price tier badge. Done when the catalogue loads and displays items with price tier badges correctly.

**Files:** packages/core/src/sectors/wholesale-distribution/ and packages/core/src/sectors/wholesale-distribution/__tests__/

**Done when:** When product catalogue displays live data with price tier badges

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add price tier manager (M1)

**Brief:** Build the price tier screen: add/edit tier (minQty, maxQty, discount%), set active, compute discounts. Done when the tier is saved and discounts apply correctly at sale.

**Files:** packages/core/src/sectors/wholesale-distribution/ and packages/core/src/sectors/wholesale-distribution/__tests__/

**Done when:** When price tier manager works end-to-end with discount computation at sale

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add customer account with credit and receivables (M1)

**Brief:** Build the customer screen: credit limit, credit used, payment terms, status, rep assigned, receivables list. Done when the customer is saved and credit used updates correctly.

**Files:** packages/core/src/sectors/wholesale-distribution/ and packages/core/src/sectors/wholesale-distribution/__tests__/

**Done when:** When customer account works with credit tracking and receivables list

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add receivable tracker with due dates and aging (M1)

**Brief:** Build the receivable screen: list outstanding, due dates, aging buckets, receive payment, mark paid. Done when the receivable is saved and aging computes correctly.

**Files:** packages/core/src/sectors/wholesale-distribution/ and packages/core/src/sectors/wholesale-distribution/__tests__/

**Done when:** When receivable tracker works end-to-end with aging computation

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add B2B invoice generator with ETA signing (M2)

**Brief:** Build the invoice screen: generate ETA-compliant invoice with QR code and seal hash, sign, send to customer. Done when the invoice is generated with correct ETA fields and the QR code is valid.

**Files:** packages/core/src/sectors/wholesale-distribution/ and packages/core/src/sectors/wholesale-distribution/__tests__/

**Done when:** When B2B invoice generator works end-to-end with ETA signing and valid QR

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add cash register with price tier discount (M1)

**Brief:** Build the cash register: scan SKU, apply price tier discount, tender payment, print receipt with invoice reference. Done when the sale applies the correct tier discount and receipt prints.

**Files:** packages/core/src/sectors/wholesale-distribution/ and packages/core/src/sectors/wholesale-distribution/__tests__/

**Done when:** When cash register works end-to-end with price tier discount

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add receivables aging report (M2)

**Brief:** Build the report showing total outstanding, by due date bucket, collection rate per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/wholesale-distribution/ and packages/core/src/sectors/wholesale-distribution/__tests__/

**Done when:** When receivables aging report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add B2B invoice volume report (M2)

**Brief:** Build the report showing invoices issued, paid, outstanding per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/wholesale-distribution/ and packages/core/src/sectors/wholesale-distribution/__tests__/

**Done when:** When B2B invoice volume report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add customer credit report (M2)

**Brief:** Build the report showing total credit used vs limit, top customers by volume. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/wholesale-distribution/ and packages/core/src/sectors/wholesale-distribution/__tests__/

**Done when:** When customer credit report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add onboarding flow for initial wholesale setup (M1)

**Brief:** Build the onboarding flow: distributor basics, initial product list, price tier scheme, customer setup. Done when the flow completes and the distributor appears with all defaults.

**Files:** packages/core/src/sectors/wholesale-distribution/ and packages/core/src/sectors/wholesale-distribution/__tests__/

**Done when:** When onboarding flow works end-to-end and distributor is created

**Check:** `npm test -- sectors/{slug}` prints passed
