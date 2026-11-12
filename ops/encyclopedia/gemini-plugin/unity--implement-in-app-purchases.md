# implement-in-app-purchases

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\implement-in-app-purchases\SKILL.md`
- SKILL.md size: 10642 chars

## What it does

Implements, configures, and debugs Unity In-App Purchases, including subscriptions, receipt validation, and direct-to-customer payments via Stripe or Coda. Use when asked about real-money purchases or microtransactions, or migrating from native store billing, RevenueCat, Adapty, Essential Kit, or UniPay.

## When to use (from skill text)

- `store.RestoreTransactions(callback)` re-delivers non-consumable and subscription purchases. Each restored purchase triggers `OnPurchasePending`.
- Use when you don't have the `Order` and want to know the status of a specific product (replaces v4's `product.hasReceipt`). If you already have the `Order`, check its type instead: `PendingOrder` maps to `EntitledUntilConsumed` (consumables) or `EntitledButNotFinished` (non-consumables/subscriptions

## Structure (headings inside SKILL.md)

- Unity In-App Purchasing
- Before You Start
- Detailed References
- Initialization Flow
- Fetching Products
- Two-Step Purchase Flow
- Restore Transactions
- Receipt Validation
- Entitlement Checking
- Fetch Existing Purchases
- Subscription Info
- Required Event Subscriptions
- Failure Description Property Names
- Validation
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Convert native Google BillingClient to Unity IAP 5:** See [references/path-convert-native-google-billing.md](references/path-convert-native-google-billing.md)
- - **Convert Essential Kit billing to Unity IAP 5:** See [references/convert-essentialkit.md](references/convert-essentialkit.md)
- - **Implement IAP D2C Capabilities (third-party payment provider — Stripe/Coda, requires v5.4+):** See [references/path-implement-iap-d2c.md](references/path-implement-iap-d2c.md)
- 4. On `OnStoreConnected`, call `store.FetchProducts(List<ProductDefinition>)` to load the catalog

## Key rules (verbatim lines from SKILL.md)

1. - **Implement IAP D2C Capabilities (third-party payment provider — Stripe/Coda, requires v5.4+):** See [references/path-implement-iap-d2c.md](references/path-implement-iap-d2c.md)
2. 2. Subscribe to **all** required events (see Required Event Subscriptions below) **before** calling `Connect()`
3. 2. Confirm all API calls match the v5 signatures in [api-notes.md](references/api-notes.md) — do NOT use v4 legacy patterns (`IStoreListener`, `UnityPurchasing.Initialize`, `ConfigurationBuilder`).
4. 3. Check the "Anti-Hallucination: Common v5 Mistakes" table in api-notes.md — do NOT use `OnStoreConnectionFailed` (use `OnStoreDisconnected`), do NOT pass callbacks to `FetchProducts`/`FetchPurchases` (use events), do NOT use `product.receipt` (use `order.Info.Receipt`).
5. 4. Check that all required events are subscribed **before** calling `Connect()` (see Required Event Subscriptions table above).

## Files inside the skill

- `references/api-notes.md` — "Unity IAP API Notes"
- `references/codeless-catalog.md` — "Editing `IAPProductCatalog.json`"
- `references/convert-adapty.md` — "Adapty — Conversion Assessment and Guidance"
- `references/convert-essentialkit.md` — "Convert Essential Kit Billing to Unity IAP 5"
- `references/convert-revenuecat.md` — "RevenueCat — Conversion Assessment and Guidance"
- `references/convert-unipay.md` — "UniPay IAP — Assessment and Guidance"
- `references/migration-v4-to-v5.md` — "Unity IAP v4 to v5 Migration Guide"
- `references/path-add-iap-to-new-project.md` — "Add Unity IAP 5 to a Project With No IAP"
- `references/path-convert-native-google-billing.md` — "Convert Native Google Billing to Unity IAP 5"
- `references/path-convert-native-storekit.md` — "Convert Native iOS StoreKit to Unity IAP 5"
- `references/path-implement-iap-d2c.md` — "Implement Unity IAP D2C Capabilities (Third-Party Payment Provider)"
- `references/platform-notes.md` — "Unity IAP Platform-Specific Notes"
- `references/pre-check.md` — "Pre-Check: Project Scan and Path Routing"
