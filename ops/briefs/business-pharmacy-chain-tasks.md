# First 10 tasks: SIR Business sector Pharmacy chain (سلسلة صيدليات)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/pharmacy-chain.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add chain overview with branch switching (M1)

**Brief:** Build the chain screen: all branches, branch stock summary, central buying dashboard, expiry aggregate view. Done when the chain overview loads and branch switching works correctly.

**Files:** packages/core/src/sectors/pharmacy-chain/ and packages/core/src/sectors/pharmacy-chain/__tests__/

**Done when:** When chain overview works and branch switching displays correct per-branch data

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add branch-specific product catalogue with FEFO (M1)

**Brief:** Build the product catalogue per branch: grid of products with name, active ingredient, price, FEFO badge, expiry date badge, stock qty. Done when the catalogue loads and displays products with FEFO badges correctly per branch.

**Files:** packages/core/src/sectors/pharmacy-chain/ and packages/core/src/sectors/pharmacy-chain/__tests__/

**Done when:** When product catalogue per branch displays live data with FEFO badges

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add FEFO food radar per branch (M1)

**Brief:** Build the FEFO radar screen per branch: items expiring in 30/60/90 days, value at risk, one-tap discount tag. Done when the radar pulls branch-specific live data and the discount tag works.

**Files:** packages/core/src/sectors/pharmacy-chain/ and packages/core/src/sectors/pharmacy-chain/__tests__/

**Done when:** When FEFO radar per branch works end-to-end with discount tag

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add controlled drug log per branch (M1)

**Brief:** Build the controlled drug log per branch: append-only list of administered/sold/wasted drugs with date, batch, quantity, authorised user. Done when the log saves each entry as append-only and the audit trail is persistent per branch.

**Files:** packages/core/src/sectors/pharmacy-chain/ and packages/core/src/sectors/pharmacy-chain/__tests__/

**Done when:** When controlled drug log per branch works end-to-end with append-only audit

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add supplier management per chain (M1)

**Brief:** Build the supplier screen: list of suppliers per chain, preferred flag, lead time, contact. Done when the supplier is saved and appears in the purchase order screen.

**Files:** packages/core/src/sectors/pharmacy-chain/ and packages/core/src/sectors/pharmacy-chain/__tests__/

**Done when:** When supplier management works and suppliers appear in purchase orders

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add purchase order per branch (M1)

**Brief:** Build the purchase order screen: create per branch, receive from supplier, update branch stock. Done when the order saves and branch stock increments correctly.

**Files:** packages/core/src/sectors/pharmacy-chain/ and packages/core/src/sectors/pharmacy-chain/__tests__/

**Done when:** When purchase order per branch works end-to-end with stock update

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add cash register per branch with FEFO discount (M1)

**Brief:** Build the cash register per branch: scan SKU or product, apply FEFO discount if urgent, tender payment, print receipt with branch name. Done when the sale records correctly and receipt prints with branch name.

**Files:** packages/core/src/sectors/pharmacy-chain/ and packages/core/src/sectors/pharmacy-chain/__tests__/

**Done when:** When cash register per branch works end-to-end with FEFO discount and receipt prints

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add chain-wide expiry aggregate report (M1)

**Brief:** Build the report showing items expiring in 30/60/90 days across all branches and total value at risk. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/pharmacy-chain/ and packages/core/src/sectors/pharmacy-chain/__tests__/

**Done when:** When chain-wide expiry aggregate report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add branch product sales report (M1)

**Brief:** Build the report showing which products sell most per branch and revenue per branch per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/pharmacy-chain/ and packages/core/src/sectors/pharmacy-chain/__tests__/

**Done when:** When branch product sales report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add controlled drug log per branch audit report (M1)

**Brief:** Build the report showing administered vs sold vs wasted counts per period per branch with audit trail. Done when the report computes from Firestore and displays correct figures and the append-only nature is verifiable per branch.

**Files:** packages/core/src/sectors/pharmacy-chain/ and packages/core/src/sectors/pharmacy-chain/__tests__/

**Done when:** When controlled drug log audit report computes correctly from live data per branch and shows append-only

**Check:** `npm test -- sectors/{slug}` prints passed
