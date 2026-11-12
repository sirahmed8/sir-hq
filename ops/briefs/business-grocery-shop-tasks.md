# First 10 tasks: SIR Business sector Grocery shop (بقالة)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/grocery-shop.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Register the grocery shop pack in the sector registry (M1)

**Brief:** Add the manifest for grocery-shop in packages/core/src/sectors/registry.ts with the id, the Arabic and English names, the base template market, the modules it turns on (pos, inventory, credits, customers, shifts), the feature flags, the role templates and the terminology map.

**Files:** packages/core/src/sectors/grocery-shop/ and packages/core/src/sectors/grocery-shop/__tests__/

**Done when:** getSector('grocery-shop') returns the manifest and the registry test asserts the modules and the roles.

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Write the credit book data model (M1)

**Brief:** Type the credit entities in packages/core/src/sectors/grocery-shop/schema.ts: credit customer with limit and due date, credit entry with kind, settlement and note, and the sale flag that points a sale at a customer. Validate that a sale cannot exceed the limit without an explicit override that is audited.

**Files:** packages/core/src/sectors/grocery-shop/ and packages/core/src/sectors/grocery-shop/__tests__/

**Done when:** The schema compiles, the validation rejects a sale over the limit, and the tests for the limit, the settlement and the statement balance pass.

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Build the grocery seed with the Arabic category list (M1)

**Brief:** Write packages/core/src/sectors/grocery-shop/seed.ts with the neighbourhood grocery categories in Arabic, the unit list with loose and pack prices, the receipt layout with the credit balance line, and the buying list template. No customer is ever seeded.

**Files:** packages/core/src/sectors/grocery-shop/seed.ts and packages/core/src/sectors/grocery-shop/schema.ts

**Done when:** The seed loads, the test asserts the category list and that the credit customer list is empty.

**Check:** `npm test -- sectors` prints passed and the seed count for this sector is asserted

## 4. Write the grocery terminology map in Arabic and English (M1)

**Brief:** Create packages/ui/src/sector/grocery-shop/glossary.ts with the words a neighbourhood shop uses: الآجل, الدفتر, الكاشير, الجملة, التالف, the till words and the receipt words, in Arabic and English.

**Files:** packages/ui/src/sector/grocery-shop/

**Done when:** The glossary covers every screen of the sector with no generic retail wording and the label test passes on the rendered till.

**Check:** the screenshot set exists at 320, 390, 768 and 1280 px in Arabic and English, light and dark

## 5. Build the credit sale flow on the counter till (M2)

**Brief:** Add the credit path to the till: pick the customer, see the balance and the limit before the sale is confirmed, block or escalate over the limit, and print the receipt with the new balance and the due date.

**Files:** apps/web/src/app/(sector)/grocery-shop/

**Done when:** A credit sale records the entry, updates the balance, refuses over the limit without the manager override, and the printed receipt shows the new balance.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 6. Build the credit book screen and the statement (M2)

**Brief:** Build the credit book: customers sorted by how late the oldest unpaid entry is, with the balance, the limit and the due date, plus a monthly statement view for one customer that prints and sends on WhatsApp.

**Files:** apps/web/src/app/(sector)/grocery-shop/

**Done when:** The book lists every customer with a balance, the statement totals match the entries, and the send action produces a shareable message.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 7. Build the buying list from the low stock screen (M2)

**Brief:** Build the screen that lists what ran low with the last purchase price and the quantity to order, and prints the list for the wholesaler or sends it on WhatsApp. The suggestion uses the real sales velocity and never orders on its own.

**Files:** apps/web/src/app/(sector)/grocery-shop/

**Done when:** The list names the items that ran low with a price from the last purchase order, and the quantity comes from the last thirty days of sales.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 8. Build the end of day screen for this sector (M2)

**Brief:** Build the close of day: money counted against money expected, the credit given today listed with the customers, the cost of the goods sold and the real margin, so the owner sees the truth after the shutters come down.

**Files:** apps/web/src/app/(sector)/grocery-shop/

**Done when:** The screen shows cash against sales, the credit list of today and the margin, and the numbers match a manual calculation in the test.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 9. Write the margin and shrink report pack (M2)

**Brief:** Add the reports of this sector: margin per item, the total of the credit book, the top debtors, the money in the drawer against the sales, the waste and shrink from the stock count, each with the CSV export.

**Files:** apps/web/src/app/(sector)/grocery-shop/

**Done when:** Every report returns its own numbers from the business documents, the test matches a manual calculation and the export opens in a spreadsheet.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 10. Publish the grocery shop landing page in Arabic and English (M3)

**Brief:** Build the sector page from the outline: the Arabic headline first, the credit book and the buying list as the two proof blocks with real screenshots, the two questions answered, and the English mirror.

**Files:** apps/web/src/app/(sector)/grocery-shop/

**Done when:** The page passes the layout rules at 320 to 1920 px in both languages and both themes, and no promise appears that the pack does not deliver.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px
