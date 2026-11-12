# implement-in-app-purchases (unity plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\unity\skills\implement-in-app-purchases\SKILL.md` (10.7 KB; unity plugin; `references/` has 13 files: pre-check, api-notes, platform-notes, codeless-catalog, migration-v4-to-v5, and per-path conversion guides for native Google Billing, native StoreKit, Essential Kit, UniPay, RevenueCat, Adapty, new-project, and IAP D2C/Stripe-Coda).

## Summary
Unity IAP v5 (`com.unity.purchasing`, namespaces `UnityEngine.Purchasing` + `.Security`) implementation guide. Initialization is its own path (`UnityIAPServices.StoreController()` → `store.Connect()`, no `UnityServices.InitializeAsync` needed). It mandates reading `references/pre-check.md` FIRST to scan the project for competing billing (third-party IAP, native Google BillingClient, StoreKit, RevenueCat, Adapty, Essential Kit, UniPay) and route to the right path. Covers the full lifecycle: subscribe ALL success+failure events before `Connect()`, `FetchProducts(List<ProductDefinition>)`, the mandatory two-step purchase (`PurchaseProduct` → `OnPurchasePending` → grant → `ConfirmPurchase(pendingOrder)` → `OnPurchaseConfirmed`), de-dup on restart, deferred purchases (`OnPurchaseDeferred` = Ask-to-Buy, never grant), `RestoreTransactions` (required on iOS), receipt validation (`CrossPlatformValidator`+GooglePlayTangle locally; Apple StoreKit2 is server-side via `jwsRepresentation`), entitlement checks (`CheckEntitlement`/`EntitlementStatus`), `IsSubscribed()==Result.True`, and a v4→v5 anti-hallucination table of wrong API names.

## When to use / when NOT
Use for implementing, configuring, or debugging real-money purchases/subscriptions in a Unity project, including migrations from other billing systems and direct-to-customer (Stripe/Coda, v5.4+) flows. Not for Unity Gaming Services non-IAP features or non-Unity stores.

## Inputs, outputs, tools
- Inputs: target platform(s), product catalog (`IAPProductCatalog.json`/`ProductDefinition`), store credentials/tangle data, existing billing code to migrate.
- Outputs: compiling C# purchase flows with correct event wiring and validation.
- Tools: Unity IAP package v5, Services window (Receipt Validation Obfuscator for tangle), platform stores (Google Play, App Store).

## 5 most important rules
1. Read `pre-check.md` before ANY other reference or change — routing decides everything.
2. Subscribe to BOTH success and failure events for every async call BEFORE `Connect()`; also `OnPurchaseDeferred` always.
3. Two-step flow is mandatory: grant content on `OnPurchasePending`, then `ConfirmPurchase(pendingOrder)` — unconfirmed purchases redeliver on next launch; de-dupe grants yourself.
4. v5 names are not interchangeable: `OnStoreDisconnected` (not OnStoreConnectionFailed), events not callbacks for Fetch*, `order.Info.Receipt` (not product.receipt), `IsSubscribed()==Result.True` not bool, `CartItem` has no subscription info (use `order.Info.PurchasedProductInfo`).
5. Apple non-renewable subs can't be restored via `RestoreTransactions` — track server-side; consumables aren't re-fetched by `FetchPurchases` — track grants yourself.

## Risks / owner notes
Real-money transactions: receipt validation gaps = revenue theft; iOS restore button is App-Store-mandatory. Migration paths touch live billing — test sandbox purchases end-to-end. Store accounts/keys are owner territory.

## Category and tags
Category: mobile. Tags: unity, in-app-purchases, subscriptions, receipts, storekit, google-play, migration.
