# First 10 tasks: SIR Business sector Photography studio (استوديو تصوير)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/photography-studio.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add session calendar with gallery link expiry (M1)

**Brief:** Build the session calendar: day/week view with client names, session status, gallery link expiry timer. Done when the calendar loads and displays sessions with expiry timers correctly.

**Files:** packages/core/src/sectors/photography-studio/ and packages/core/src/sectors/photography-studio/__tests__/

**Done when:** When session calendar works and displays expiry timers

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add shot list editor per session (M1)

**Brief:** Build the shot list screen: add description Ar/En per shot, mark isCompleted, set completedAt. Done when the shot list is saved and linked to the session.

**Files:** packages/core/src/sectors/photography-studio/ and packages/core/src/sectors/photography-studio/__tests__/

**Done when:** When shot list editor works and links to session

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add order creation with types and deposit (M1)

**Brief:** Build the order screen: select session, type (album/print/watermarkedGallery/retouching), compute total, set deposit and balance, set status. Done when the order saves all fields and status updates correctly.

**Files:** packages/core/src/sectors/photography-studio/ and packages/core/src/sectors/photography-studio/__tests__/

**Done when:** When order creation works end-to-end with types and deposit

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add gallery link manager with expiry and revocation (M1)

**Brief:** Build the gallery link screen: generate expiring link, set expiry date, view link history, revoke and regenerate. Done when the link is generated with expiry and history is saved.

**Files:** packages/core/src/sectors/photography-studio/ and packages/core/src/sectors/photography-studio/__tests__/

**Done when:** When gallery link manager works end-to-end with expiry and revocation

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add order status tracker with pipeline (M1)

**Brief:** Build the order tracker: per order view progress (pending/confirmed/in-progress/done/ready-for-pickup), print ready notice with gallery link. Done when the tracker updates status and prints ready notice correctly.

**Files:** packages/core/src/sectors/photography-studio/ and packages/core/src/sectors/photography-studio/__tests__/

**Done when:** When order status tracker works end-to-end with pipeline and receipt printing

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add client profile with consent and gallery history (M1)

**Brief:** Build the client profile: visit count, total spent, last visit, consent flag for watermarks, gallery link history. Done when the profile saves and displays correct data.

**Files:** packages/core/src/sectors/photography-studio/ and packages/core/src/sectors/photography-studio/__tests__/

**Done when:** When client profile works and displays live data with consent and history

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add session volume per period report (M1)

**Brief:** Build the report showing sessions booked/in-progress/done per month and revenue per session per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/photography-studio/ and packages/core/src/sectors/photography-studio/__tests__/

**Done when:** When session volume report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add order pipeline report (M1)

**Brief:** Build the report showing orders by status per period and average duration per status. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/photography-studio/ and packages/core/src/sectors/photography-studio/__tests__/

**Done when:** When order pipeline report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add gallery link expiry report (M1)

**Brief:** Build the report showing how many links expired per period, how many regenerated, average sessions per link. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/photography-studio/ and packages/core/src/sectors/photography-studio/__tests__/

**Done when:** When gallery link expiry report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add client repeat rate report (M1)

**Brief:** Build the report showing visit count per client, total spent per client, re-book rate. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/photography-studio/ and packages/core/src/sectors/photography-studio/__tests__/

**Done when:** When client repeat rate report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed
