# First 10 tasks: SIR Business sector Real estate office (مكتب عقاري)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/real-estate-office.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add property list grid with status badge (M1)

**Brief:** Build the property list: grid of listings with title, price, status badge, area, location preview, commission %. Done when the list loads and displays listings with correct status badges.

**Files:** packages/core/src/sectors/real-estate-office/ and packages/core/src/sectors/real-estate-office/__tests__/

**Done when:** When property list displays live data with status badges

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add lead pipeline kanban board (M1)

**Brief:** Build the lead pipeline: kanban board with columns new/contacted/qualified/offerSent/closedLost, drag lead between columns, view lead details. Done when the pipeline works and leads can be moved between stages.

**Files:** packages/core/src/sectors/real-estate-office/ and packages/core/src/sectors/real-estate-office/__tests__/

**Done when:** When lead pipeline kanban works and leads can be moved between stages

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add lead detail screen (M1)

**Brief:** Build the lead detail: name, phone, source, status, expected deal size, follow-up date, notes, associated listings and contracts. Done when the detail screen loads and displays correct data.

**Files:** packages/core/src/sectors/real-estate-office/ and packages/core/src/sectors/real-estate-office/__tests__/

**Done when:** When lead detail screen works and displays live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add appointment scheduler (M1)

**Brief:** Build the appointment screen: select lead, date/time, type (viewing/consultation), set status (scheduled/completed/cancelled), add notes. Done when the appointment is saved and status updates correctly.

**Files:** packages/core/src/sectors/real-estate-office/ and packages/core/src/sectors/real-estate-office/__tests__/

**Done when:** When appointment scheduler works end-to-end with status update

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add contract editor with commission compute (M1)

**Brief:** Build the contract screen: select listing, enter buyer/seller, commission % and amount, signed date, expiry date, set status (draft/signed/expired), add notes, compute deposit. Done when the contract saves and commission computes correctly.

**Files:** packages/core/src/sectors/real-estate-office/ and packages/core/src/sectors/real-estate-office/__tests__/

**Done when:** When contract editor works end-to-end with commission computation

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add client list with visit count and total spent (M1)

**Brief:** Build the client list: all clients with visit count, total spent, consent photos flag. Done when the list loads and displays correct data.

**Files:** packages/core/src/sectors/real-estate-office/ and packages/core/src/sectors/real-estate-office/__tests__/

**Done when:** When client list displays live data with visit count and total spent

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add cash register with listing/lead scanning (M1)

**Brief:** Build the cash register: scan listing reference or lead ID, record commission payment, print receipt. Done when the sale records the commission and receipt prints correctly.

**Files:** packages/core/src/sectors/real-estate-office/ and packages/core/src/sectors/real-estate-office/__tests__/

**Done when:** When cash register works end-to-end with scanning and receipt prints

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add lead pipeline report (M1)

**Brief:** Build the report showing leads per status per period and conversion rates per stage. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/real-estate-office/ and packages/core/src/sectors/real-estate-office/__tests__/

**Done when:** When lead pipeline report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add property sales report (M1)

**Brief:** Build the report showing listings created, sold per period, revenue per period, average time to sell. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/real-estate-office/ and packages/core/src/sectors/real-estate-office/__tests__/

**Done when:** When property sales report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add commission collected report (M1)

**Brief:** Build the report showing total commission per period, per agent, collection rate. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/real-estate-office/ and packages/core/src/sectors/real-estate-office/__tests__/

**Done when:** When commission collected report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed
