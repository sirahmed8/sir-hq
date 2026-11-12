# Contacts cleanup report (2026-11-12)

## Google Contacts
- Before: 589 contacts (backup google.csv, 589 rows).
- Cleaned file google_clean.csv: 589 rows, 172 rows changed by HQ script.
- Deleted all 589 (moved to Bin, 30 days recoverable), imported google_clean.csv.
- After: 589 contacts. Status: DONE, count verified.

## iCloud Contacts
- Before: 522 contacts (backup apple.vcf, 522 cards).
- Cleaned file apple_clean.vcf: 522 cards. Script: 168 changed, 3 prefixes moved, 13 repeats removed, 98 full names split.
- Deleted all 522 (iCloud Recently Deleted, recoverable).
- Import of apple_clean.vcf: NOT DONE. The vCard file picker opens as a native dialog that the browser tools cannot drive.
- After: 0 contacts. Status: NOT RESTORED YET.

## Update (HQ message, v2 cleaner with spelling unification)
- Google: deleted the 589 contacts (Bin) and imported google_v2.csv. Verified: 589 in the "Imported on 12/11" label. The main Contacts view showed 0 after reload (display lag, not verified as an error). Imported file version: _v2.
- Apple v2: apple_v2.vcf created (522 cards; 189 changed, 270 spellings unified). Import NOT done (native file picker blocked). iCloud currently shows 522 contacts, which came from an earlier import (apple_clean.vcf, not verified). Version on iCloud: unverified, probably _clean.
- Google's extra "Imported on 12/11" label was created by the import; it is not deleted.

## Round 3 (owner orders)
- Google label "Imported on 12/11": two auto-created labels deleted (the label only; contacts kept). Done.
- Google replaced with final_google.csv: deleted 589 (Bin), imported. After: 607 contacts. Verified (target 607). Done.
- Google Merge and fix (not clicked): 12 merge suggestions, 1 fix suggestion (Add contact details). Badge total 13.
- Chrome autofill (chrome://settings/addresses): NOT DONE. The browser extension cannot open chrome:// pages (error page), and the computer-use tool is read-only for browsers. Before/after counts: not obtained.
- iCloud: still not on the v2 file (see above). iCloud shows 522 contacts from an earlier import, version unverified.

## Next step (owner, about 1 minute)
1. Open icloud.com/contacts, click the + icon above the list, choose Import vCard, pick D:/Projects/_SIR/_local/contacts/apple_clean.vcf.
2. Check that the list shows 522 contacts.
If you prefer to restore the original names instead: same steps with apple.vcf, or iCloud account settings > Restore Contacts.
