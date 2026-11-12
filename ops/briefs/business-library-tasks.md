# First 10 tasks: SIR Business sector Library (مكتبة)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/library.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add OPAC public search page (M1)

**Brief:** Build the public search page: search books by ISBN, title or author, view availability status. Done when the page loads and displays matching books from Firestore.

**Files:** packages/core/src/sectors/library/ and packages/core/src/sectors/library/__tests__/

**Done when:** When OPAC search works and displays live book data

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add member check-in with scan (M1)

**Brief:** Build the member check-in screen: scan member card, view active borrowings, due dates. Done when the scan works and displays member data correctly.

**Files:** packages/core/src/sectors/library/ and packages/core/src/sectors/library/__tests__/

**Done when:** When member check-in works with barcode scan and displays data

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add book checkout and check-in screen (M1)

**Brief:** Build the checkout screen: scan book barcode, record borrowing with due date, decrement availability. Done when checkout records borrowing and check-in updates status and computes fines.

**Files:** packages/core/src/sectors/library/ and packages/core/src/sectors/library/__tests__/

**Done when:** When book checkout/check-in works end-to-end with due dates and fines

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add study desk booking screen (M2)

**Brief:** Build the desk booking screen: available desks, book slot, confirm, cancel. Done when a desk can be booked and the booking is saved to Firestore.

**Files:** packages/core/src/sectors/library/ and packages/core/src/sectors/library/__tests__/

**Done when:** When study desk booking works end-to-end

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add fine management screen (M2)

**Brief:** Build the fine screen: unpaid fines per member, receipt print, write-off reason. Done when fines are tracked and receipts print correctly.

**Files:** packages/core/src/sectors/library/ and packages/core/src/sectors/library/__tests__/

**Done when:** When fine management works and receipts print

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add member registration with parent consent for children (M2)

**Brief:** Build the member screen: name, phone, class, membership type, parent consent flag for under-18. Done when the member is saved with consent flag and minimal child data.

**Files:** packages/core/src/sectors/library/ and packages/core/src/sectors/library/__tests__/

**Done when:** When member registration works with parent consent flag

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add overdue fines revenue report (M3)

**Brief:** Build the report showing total unpaid, collected and written-off fines per period. Done when the report pulls live data and displays correct figures.

**Files:** packages/core/src/sectors/library/ and packages/core/src/sectors/library/__tests__/

**Done when:** When fines revenue report pulls live data and displays correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add study desk utilisation report (M3)

**Brief:** Build the report showing booked hours vs available per day. Done when the report computes from Firestore and displays correct utilisation.

**Files:** packages/core/src/sectors/library/ and packages/core/src/sectors/library/__tests__/

**Done when:** When study desk utilisation report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add book circulation by category report (M4)

**Brief:** Build the report showing which genres are most borrowed per period. Done when the report computes from Firestore and displays correct circulation counts.

**Files:** packages/core/src/sectors/library/ and packages/core/src/sectors/library/__tests__/

**Done when:** When book circulation report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add onboarding flow for initial library setup (M1)

**Brief:** Build the onboarding flow: library basics, initial book inventory, membership types, study desks. Done when the flow completes and the library appears with all defaults.

**Files:** packages/core/src/sectors/library/ and packages/core/src/sectors/library/__tests__/

**Done when:** When onboarding flow works end-to-end and library is created

**Check:** `npm test -- sectors/{slug}` prints passed
