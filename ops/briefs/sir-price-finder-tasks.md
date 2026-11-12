# First 10 Tasks to Hand to Free Agents: SIR Price Finder (sir-price-finder-tasks.md)

Tasks ready to queue for the free CLI agents (Kilo, OpenCode, Devin CLI, ZCode). Each has a title and a one-paragraph brief. All are scoped to under 2 hours. Work in `D:\Projects\_SIR` (plan and ops code) and write reports/evidence only inside that project or `D:\Projects\_SIR\ops\`. Never open `D:\Projects\AHome`. Never put secrets in git. Version stays 1.0.0. No placeholders, no invented data, every screen keeps five states, Arabic RTL and English, 44 px targets, bidi-isolated mixed text.

## 1. Legacy parity matrix, read-only

Add `npm run proof-report` printing rows with and without proof, counts by stage, and the list of "Applied" rows missing a proof file. Files: read `plans/sir-deals.md` price section, write `.sir/reports/parity.md`. Check: every route of the legacy price section has a keep/port/drop/drop-reason verdict; the file lists each with the file that proves it; exits non-zero if any route is missing a verdict; `npm test` green.

## 2. Monorepo scaffold with tokens, RTL, the price-compare route and CI

Scaffold the monorepo (apps/web, apps/api, packages/core, packages/data, packages/ui, packages/kit) with strict TypeScript, Tailwind v4 tokens, RTL-first styles and the shared `verify` script. Files: `plans/sir-price-finder.md` structure, `packages/core/types.ts`, `packages/ui/tokens.ts`, `apps/web/next.config.mjs`, `scripts/verify.mjs`. Check: `pnpm verify` runs typecheck, lint, tests, build and gitleaks, and the output was seen green; the folder kit is recreated from scratch for the new build (folder.ico, Desktop lnk files, Versions.txt reading 1.0.0).

## 3. The product's own Firebase project and the owner-auth package with negative tests

Create the Firebase project `sir-price-finder` (free Spark plan), set up Firestore deny-by-default rules, Google sign-in, owner allow-list, HttpOnly Secure cookie, and write the `owner-auth` package with negative tests. Files: `scripts/create-firebase-project.mjs` (or manual Firebase console steps), `packages/owner-auth/owner-auth.mjs`, `test/owner-auth-test.mjs`. Check: the Firebase project exists and the GitHub repo `sirahmed8/sir-price-finder` is the only remote for it; a forged token gets 403, a non-owner token on `/owner` gets 403, a client-side flag flip gets nothing; `npm test` green.

## 4. The data model and the Firestore rules, with emulator tests

Write the Firestore data model for Product, Store, Price, Wishlist, Alert; write the deny-by-default rules; run the emulator tests including a cross-tenant read that must fail. Files: `packages/data/products.mjs`, `packages/data/stores.mjs`, `packages/data/prices.mjs`, `packages/data/wishlists.mjs`, `packages/data/alerts.mjs`, `firebase.rules`. Check: the emulator rules tests pass, including a cross-tenant read that must fail; `npm test` green.

## 5. The price fetch script for Amazon.eg (first product, offline fixture test)

Write a script that fetches the price of a single tracked product from Amazon.eg, stores the result in Firestore, and has an offline fixture test that can run without network. Files: `scripts/price-amazon-eg.mjs`, `test/fixtures/amazon-eg-sample.json`, `test/price-amazon-eg-test.mjs`. Check: the script fetches and stores the price for one product; the offline fixture test passes with the sample JSON; `npm test` green.

## 6. The price fetch script for Noon (first product, offline fixture test)

Write a script that fetches the price of a single tracked product from Noon, stores the result in Firestore, and has an offline fixture test that can run without network. Files: `scripts/price-noon.mjs`, `test/fixtures/noon-sample.json`, `test/price-noon-test.mjs`. Check: the script fetches and stores the price for one product; the offline fixture test passes with the sample JSON; `npm test` green.

## 7. The real-discount badge with the rubric

Implement the rubric: given a product's price history, determine if a "discount from X EGP" claim is "real" or "inflated"; display the badge with a one-line explanation; write the unit test for the rubric with Arabic and English eval sets. Files: `packages/core/real-discount.mjs`, `test/real-discount-test.mjs`. Check: the rubric correctly flags an "inflated" price when the "original price" never existed in the history, and shows "real" when the discount is genuine; the badge renders with the correct text and color at 390 px and 1280 px, in Arabic and English, light and dark; `npm test` green.

## 8. The wishlist save and unlimited items

Implement the wishlist save (product name, price, store URL), unlimited items, persistence across reloads, and the UI for viewing and managing the wishlist. Files: `packages/data/wishlists.mjs`, `apps/web/WishlistPage.tsx`, `test/wishlist-test.mjs`. Check: a user can save unlimited items to a wishlist; the wishlist persists across reloads and stores the product name, price, and store URL for each item; the UI shows the wishlist items at 320 px and 1280 px, in Arabic and English, light and dark; `npm test` green.

## 9. The price-drop alert and Telegram notification

Implement the alert target price, the one-alert-at-a-time limit, the logic to check the price against the target, and the Telegram notification (dry-run first, then real). Files: `packages/alerts/alert.mjs`, `test/alert-test.mjs`, `scripts/telegram-dryrun.mjs`. Check: a user can set an alert target price for a tracked product; when the price drops below the target, a Telegram alert is sent in dry-run mode (prints the message, does not send); in real mode, the Telegram notification is sent exactly once when the price drops below the target; the alert includes the product name, the new price, and a link to the product page; 5 parallel alert checks for one product produce exactly one alert and 4 clean rejections; `npm test` green.

## 10. The currency auto-detect from visitor locale and IP

Implement the locale/IP detection that shows EGP for Egypt, SAR for KSA, AED for UAE, etc., with a manual override widget on the settings page. Files: `packages/i18n/currency.mjs`, `apps/web/CurrencySelector.tsx`, `test/currency-test.mjs`. Check: the system shows EGP for Egypt visitors, SAR for KSA, AED for UAE, auto-detected from the visitor's locale and IP; a manual override widget allows changing the currency; the currency renders correctly at 320 px and 1280 px, in Arabic and English, light and dark; `npm test` green.

All tasks: after finishing, run the gates (`npm test`, `npm run lint`, `npm run typecheck`), update the project checkpoint, commit to `main` with a clear message. Do not push to `D:\Projects\_SIR` for project-code changes; push the SIR Price Finder repo. Reports go to `D:/Projects/_SIR/ops/agy-runs/reports\<task>.md`.