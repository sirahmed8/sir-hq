# SIR Business sector: Grocery shop (بقالة)

> Round r56 (2026-11-12). Sector 2 of 41 in `plans/business-sectors/_INDEX.md`, wave 1.
> Base template `market`, group `food-and-drink`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The owner stands behind the counter, knows every customer by name and keeps the credit in a school notebook. Their day is short but the decisions are constant: what to buy from the wholesaler tomorrow, who owes what, and whether the price still covers the cost. They lose time re-counting, they lose money when a customer moves shop, and they have no idea which items actually make money.

Why this sector is in the catalogue: The smallest shop that still runs a real business, and the one where the credit book is the whole business: regulars who pay at the end of the month and a stock list that lives in the owner head.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Shop (id, name, branchId, address, phone, currency, openingHours, creditPolicyDays)
- Product (id, sku, barcode, nameAr, nameEn, categoryId, unit, unitPricePiasters, costPiasters, taxRate, supplierId, stockQuantity, reorderPoint)
- Category (id, nameAr, nameEn, parentId, shelfOrder, iconKey)
- CreditCustomer (id, name, phone, whatsappOptIn, creditLimitPiasters, balancePiasters, dueDate, lastPaymentAt, statementSentAt)
- CreditEntry (id, customerId, saleId, amountPiasters, kind, createdAt, settledAt, note)
- Sale (id, branchId, cashierId, lines, payments, totalPiasters, isCredit, customerId, createdAt, idempotencyKey)
- SaleLine (id, saleId, productId, quantity, unitPricePiasters, discountPiasters)
- Supplier (id, nameAr, phone, paymentTerms, visitDays, lastOrderAt)
- PurchaseOrder (id, supplierId, status, lines, expectedAt, totalPiasters)
- Shift (id, branchId, openedBy, openedAt, floatPiasters, closedAt, countedPiasters)
- StockCount (id, branchId, countedBy, lines, variancePiasters, countedAt)
- Owner (id, name, phone, role, branchId, pinHash)

Units in use: piece, pack, box, kilogram, gram, litre, and a small shop price for the loose item and a pack price for the same product

Batches: Usually no. A grocery shop buys in small quantities and sells fast. The pack supports an optional batch only for the shop that sells dairy or frozen, and the expiry is then per batch like the supermarket

Expiry and shelf life: Not a driver here. The shop sees the expiry only where it sells chilled or frozen, and the alert is one line on the stock screen, not a radar

Sector specific structures: The structures specific to this sector are the credit book (a per customer ledger with a limit, a due date and a statement), the customer price list (wholesale price for the regular who buys ten bags, shelf price for the walk in), and the daily note of what was bought from the wholesaler

## 3. Screens and workflows that belong to this sector

- Counter till: the simplest till in the product, fast on a phone, cash and wallet, and a keypad for the quantities the customer asks for
- Credit sale: choose the customer, the screen shows what they still owe and what their limit is, the sale goes on the ledger and the receipt prints with the new balance
- Credit book: every customer with the balance, the limit, the oldest unpaid entry and the due date, sorted by how late it is
- Statement: the month statement for one customer, printable and sendable on WhatsApp, with the items, the amounts and the payments received
- Stock list: what is left, what it cost, what it sells for, and the margin for each item
- Buy from the wholesaler: the list of what ran low with the last price, send it to the supplier on WhatsApp or print it
- End of day: the money counted against the sales, the credit given today listed, and the profit that is real after the cost of the goods
- Regular customer: what this customer buys, how often, what they owe and one tap to message them

## 4. Roles and permissions

- Owner: everything, including the credit book, the pricing and the staff
- Cashier: sells, takes payment, records a credit sale, cannot raise the credit limit
- Assistant: sells and counts, no access to the credit book and no price changes

## 5. Reports and KPIs

- Money in the drawer today against the sales of today
- The credit book: total owed, the top ten debtors, the oldest unpaid entry
- What makes money: margin per item, so the owner stops selling the items that lose
- What ran low this week: the buy list for the wholesaler
- Who comes back: the customers with a purchase every week and what they buy
- Waste and shrink: the counted difference per item

## 6. Integrations that matter

- Thermal printer through ESC/POS, optional because many shops print on the phone
- Barcode scanner in keyboard mode, optional because the owner types the code
- Cash drawer, optional
- WhatsApp for the statement to the customer and the buy list to the wholesaler, through the shop own account
- Daily backup of the sales and the credit book to the cloud with the offline queue

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Business basics: name, address, phone, currency and the opening hours
- Shelves: pick the categories the shop has and set the order
- Credit policy: the number of days a regular may pay later, and whether the shop wants a limit per customer
- Regulars: add the first credit customers with a phone number and a limit
- Stock: add the items the shop sells most, with the cost and the price
- First week plan: print one receipt, open the credit book, count the drawer at close, add the wholesaler
- Review and finish

Template data that is ready on day one (seeded and marked "review before going live", never shown as if it were the shop's own data):

- Category list in Arabic for a neighbourhood grocery: vegetables, fruit, bread, dairy, eggs, rice and pasta, oils, sugar, tea and coffee, water, snacks, household, cleaning
- A unit list with the loose and the pack price on the same item
- An empty credit customer list, never seeded with fake names
- A receipt layout with the shop header and the credit line that shows the new balance
- A short buying list template the owner can print and take to the wholesaler

## 8. The landing page outline

The sector gets its own page, its own words and its own proof. No shared generic copy.

### Arabic (ar-EG, written first)

- بقالة بتفوق على ذاكرتها: دفتر العملاء، والشراء من الجملة، وختام اليوم
- كاشير سريع على الموبايل، دفتر آجل للزبون الثابت، وقائمة الشراء جاهزة للجملة كل يوم
- الدفتر بدل الدفتر الورقي: كل زبون آجل ورصيده وموعد سداده في شاشة واحدة
- قائمة الشراء بتطلع لوحدها من اللي خلص
- بتعرف مين بيكسبلك ومين بيخسر عليك

Questions the page must answer:

- ينفع أشتغل بده ناقص؟ أيوه: البيع بيكمّل والديون بتتسجل، والمزامنة لما يرجع النت
- يعني الدفتر فيه فوائد؟ لأ: ده دفتر محل، من غير فوائد ولا تحصيل ولا قروض

### English

- A grocery shop that runs on more than memory: the credit book, the wholesaler list and the end of the day
- A fast till on the phone, a credit book for the regulars, and a buying list that writes itself when stock runs low
- The notebook becomes a screen: every credit customer with the balance and the due date in one place
- The buying list for the wholesaler writes itself from what ran low
- You see which items make money and which ones you are giving away

Questions the page must answer:

- Can it work with no connection? Yes: selling continues, debts are recorded, and everything syncs when the connection is back
- Does the credit book charge interest? No: it is a shop ledger, with no interest, no collections and no loans

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Counter till: the simplest till in the product, fast on a phone, cash and wallet, and a keypad for the quantities the customer asks for
- Credit sale: choose the customer, the screen shows what they still owe and what their limit is, the sale goes on the ledger and the receipt prints with the new balance
- Credit book: every customer with the balance, the limit, the oldest unpaid entry and the due date, sorted by how late it is
- Statement: the month statement for one customer, printable and sendable on WhatsApp, with the items, the amounts and the payments received
- Stock list: what is left, what it cost, what it sells for, and the margin for each item
- Buy from the wholesaler: the list of what ran low with the last price, send it to the supplier on WhatsApp or print it

## 9. Pricing tier notes

- The free tier is enough for one person behind the counter: one business, one branch, two seats, the till and the credit book
- Starter adds a year of history and five seats for the shop with a helper
- The Business tier adds the buying list from the velocity, the stock count by phone camera and the statements by WhatsApp
- The credit book is never behind the highest tier: a grocery shop that cannot see its own debts is a grocery shop in trouble

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Daftra (دفترة) | Free start, published rates not readable on the page opened (daftra.com, opened 2026-11-12) | Built as an ERP with a heavy interface, where a grocery owner wants ten fields and a receipt | A screen that fits a phone behind a counter, a credit book designed for a notebook, and a free tier that stays free |
| Loyverse | Free POS, add-ons from US$5 per store per month (loyverse.com/pricing, opened 2026-11-12) | No credit book, no customer ledger and no Arabic Egyptian workflow | The credit book, the customer price list and the statement are part of the pack |
| Odoo | One App Free at US$0, Standard US$8.95 per user per month on annual billing (odoo.com/pricing, opened 2026-11-12) | A partner project for a shop that needs one screen today | One price, ready today, and an Arabic cashier flow |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-grocery-shop-tasks.md`:

1. Register the grocery shop pack in the sector registry (M1)
2. Write the credit book data model (M1)
3. Build the grocery seed with the Arabic category list (M1)
4. Write the grocery terminology map in Arabic and English (M1)
5. Build the credit sale flow on the counter till (M2)
6. Build the credit book screen and the statement (M2)
7. Build the buying list from the low stock screen (M2)
8. Build the end of day screen for this sector (M2)
9. Write the margin and shrink report pack (M2)
10. Publish the grocery shop landing page in Arabic and English (M3)

## 12. Risks, unknowns and what we refuse to fake

- The credit book is a shop ledger, so no interest, no instalments, no collection agency and no legal claim is built into it
- Customer names are personal data of the shop, so they never enter our analytics and can be exported or deleted from the settings
- The margin report depends on real purchase costs, so an item without a cost is shown as missing a cost instead of being counted as zero
- No wholesaler name or price is published in our copy: the supplier data belongs to the shop

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-grocery-shop-tasks.md`
