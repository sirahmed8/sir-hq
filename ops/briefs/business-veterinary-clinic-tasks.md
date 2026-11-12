# First 10 tasks: SIR Business sector Veterinary clinic (عيادة بيطرية)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/veterinary-clinic.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add patient record with vaccination history (M1)

**Brief:** Build the patient screen: name, species, breed, owner name and phone, vaccination history (type, date, next due), notes, photo consent flag. Done when the patient is saved with vaccination history and consent flag.

**Files:** packages/core/src/sectors/veterinary-clinic/ and packages/core/src/sectors/veterinary-clinic/__tests__/

**Done when:** When patient record works with vaccination history and consent flag

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add drug catalogue with FEFO flag and expiry (M1)

**Brief:** Build the drug catalogue: list of drugs with active ingredient, price, FEFO flag, expiry date, supplier, reorder point. Done when the catalogue loads and displays drugs with FEFO badge and expiry.

**Files:** packages/core/src/sectors/veterinary-clinic/ and packages/core/src/sectors/veterinary-clinic/__tests__/

**Done when:** When drug catalogue displays live data with FEFO flag and expiry date

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add controlled drug append-only log (M1)

**Brief:** Build the controlled drug log: append-only list of administered/sold/wasted drugs with date, batch, quantity, authorised user. Done when the log saves each entry as append-only and the audit trail is persistent.

**Files:** packages/core/src/sectors/veterinary-clinic/ and packages/core/src/sectors/veterinary-clinic/__tests__/

**Done when:** When controlled drug log works end-to-end with append-only audit

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add drug sale screen with FEFO check (M1)

**Brief:** Build the drug sale screen: select drug, enter quantity, check FEFO expiry, record sale, compute price with tax. Done when the sale saves and the FEFO expiry check works correctly.

**Files:** packages/core/src/sectors/veterinary-clinic/ and packages/core/src/sectors/veterinary-clinic/__tests__/

**Done when:** When drug sale works end-to-end with FEFO check and price computation

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add vaccination reminder screen (M1)

**Brief:** Build the reminder screen: list of pets due for vaccination, send notice (WhatsApp/SMS). Done when the reminder list pulls live data and the notice can be sent.

**Files:** packages/core/src/sectors/veterinary-clinic/ and packages/core/src/sectors/veterinary-clinic/__tests__/

**Done when:** When vaccination reminder works end-to-end with notice sending

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add controlled drug log audit report (M2)

**Brief:** Build the report showing administered vs sold vs wasted counts per period with audit trail. Done when the report computes from Firestore and displays correct figures and the append-only nature is verifiable.

**Files:** packages/core/src/sectors/veterinary-clinic/ and packages/core/src/sectors/veterinary-clinic/__tests__/

**Done when:** When controlled drug log audit report computes correctly from live data and shows append-only

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add drug expiry radar report (30/60/90 days) (M2)

**Brief:** Build the radar report showing items expiring in 30/60/90 days and value at risk. Done when the report computes from Firestore and displays correct buckets and values.

**Files:** packages/core/src/sectors/veterinary-clinic/ and packages/core/src/sectors/veterinary-clinic/__tests__/

**Done when:** When drug expiry radar report computes correctly from live data and shows correct buckets

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add vaccination compliance report (due per period) (M2)

**Brief:** Build the report showing pets due for vaccination per period by vaccine type, with overdue notice rates. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/veterinary-clinic/ and packages/core/src/sectors/veterinary-clinic/__tests__/

**Done when:** When vaccination compliance report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add appointment no-show rate report (M2)

**Brief:** Build the report showing no-show rate per period by vet, with overdue notice rates. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/veterinary-clinic/ and packages/core/src/sectors/veterinary-clinic/__tests__/

**Done when:** When appointment no-show report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add onboarding flow for initial veterinary clinic setup (M1)

**Brief:** Build the onboarding flow: clinic basics, initial drug catalogue, vaccination schedule, staff addition. Done when the flow completes and the clinic appears with all defaults.

**Files:** packages/core/src/sectors/veterinary-clinic/ and packages/core/src/sectors/veterinary-clinic/__tests__/

**Done when:** When onboarding flow works end-to-end and clinic is created

**Check:** `npm test -- sectors/{slug}` prints passed
