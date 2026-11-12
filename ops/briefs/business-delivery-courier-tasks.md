# First 10 tasks: SIR Business sector Delivery and courier (توصيل وشحن)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/delivery-courier.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add delivery order creation screen with COD field (M1)

**Brief:** Build the UI for creating a new delivery order: pickup, delivery address, COD amount, service type, zone assignment. Done when the form validates and creates an order doc in Firestore.

**Files:** packages/core/src/sectors/delivery-courier/ and packages/core/src/sectors/delivery-courier/__tests__/

**Done when:** When the order creation form works and persists data

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Implement rider assignment and zone picker (M2)

**Brief:** Build the rider assignment UI with zone picker. Done when a rider can be assigned to an order and the zone geometry validates.

**Files:** packages/core/src/sectors/delivery-courier/ and packages/core/src/sectors/delivery-courier/__tests__/

**Done when:** When rider assignment works end-to-end

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add COD shift reconciliation screen (M2)

**Brief:** Build the screen that counts cash collected vs expected per shift with variance and audit log. Done when the numbers reconcile and the log is append-only.

**Files:** packages/core/src/sectors/delivery-courier/ and packages/core/src/sectors/delivery-courier/__tests__/

**Done when:** When COD reconciliation works and saves to audit log

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add rider dashboard with order list and status update (M3)

**Brief:** Build the rider-side dashboard showing assigned orders, ETA and status buttons (picked, in-progress, completed, cancelled). Done when the rider can update status and it propagates.

**Files:** packages/core/src/sectors/delivery-courier/ and packages/core/src/sectors/delivery-courier/__tests__/

**Done when:** When rider status updates propagate to the dashboard

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add WhatsApp deep link for customer order status (M3)

**Brief:** Build the WhatsApp deep link that sends the customer a status update. Done when the link opens WhatsApp with a pre-filled status message.

**Files:** packages/core/src/sectors/delivery-courier/ and packages/core/src/sectors/delivery-courier/__tests__/

**Done when:** When the link opens WhatsApp with the correct chat

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add route map with rider location (M4)

**Brief:** Build the map view showing assigned orders and rider location with ETA. Done when the map loads and rider position updates.

**Files:** packages/core/src/sectors/delivery-courier/ and packages/core/src/sectors/delivery-courier/__tests__/

**Done when:** When the route map displays correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add electronic proof of delivery (photo/signature) (M4)

**Brief:** Build the proof capture UI: photo upload or signature input. Done when the proof is saved to the order doc and visible in the dashboard.

**Files:** packages/core/src/sectors/delivery-courier/ and packages/core/src/sectors/delivery-courier/__tests__/

**Done when:** When proof of delivery is saved and viewable

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add daily dispatch report (M5)

**Brief:** Build the report screen showing today's dispatched orders, on-time rate per zone, and unassigned count. Done when the report displays real data from Firestore.

**Files:** packages/core/src/sectors/delivery-courier/ and packages/core/src/sectors/delivery-courier/__tests__/

**Done when:** When the report pulls live data and displays correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add rider earnings calculator (M5)

**Brief:** Build the earnings calculator that computes rider commission per completed order. Done when the math matches the commission rate and order COD.

**Files:** packages/core/src/sectors/delivery-courier/ and packages/core/src/sectors/delivery-courier/__tests__/

**Done when:** When earnings compute correctly per rider

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add rider onboarding flow (first ride) (M1)

**Brief:** Build the onboarding flow for a new rider: company welcome, zone assignment, first order, first payout. Done when the flow completes and the rider appears in the system.

**Files:** packages/core/src/sectors/delivery-courier/ and packages/core/src/sectors/delivery-courier/__tests__/

**Done when:** When the onboarding flow works end-to-end

**Check:** `npm test -- sectors/{slug}` prints passed
