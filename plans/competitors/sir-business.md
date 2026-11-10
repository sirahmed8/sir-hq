# Competitor Study: SIR Business (Commercial ERP & POS Suite)

> AUDIT 2026-11-10 (plans audit): this file has no source links. Every price, market share, user count, feature claim, quoted review and complaint quote below is "(unsourced, verify)" until it has a link and a date. Do not copy anything from here into public copy, store listings, legal pages or comparison pages. Quoted reviews could not be traced to a real page: treat them as illustrative, not as evidence. Sourcing tasks are at the end of this file.
**Date of Research**: 2026-11-09  
**Category**: Retail POS, Restaurant Order Management, Pharmacy ERP, ETA e-Invoicing  
**Target Markets**: Egypt (Cairo, Giza, Alexandria), Saudi Arabia (ZATCA), UAE

---

## 1. Top Competitors Overview

| Competitor | Market & Pricing | Strengths | Weaknesses & User Complaints |
|---|---|---|---|
| **Daftra (دفترة)** | Egypt & Saudi (~$30–$80/mo billed annually) | Comprehensive accounting, ETA integration | Cluttered legacy UI; steep learning curve; mobile apps suffer from sync lag; expensive for solo shops. |
| **Loyverse POS** | Global / Used in Egyptian cafes (Free core + paid add-ons) | Clean UI, fast tablet POS | **Zero Egyptian ETA e-invoicing support**; add-ons (inventory, staff) cost $25/mo each; English-first support. |
| **Foodics (فودكس)** | GCC & Egypt F&B leader (~$1,200–$2,500/year/branch) | Strong restaurant hardware ecosystem | Prohibitively expensive for independent cafes; rigid lock-in; slow onboarding; excessive hardware fees. |
| **Odoo (Community & Enterprise)**| Global Open Source / Enterprise | Infinite customization, large module store | Extreme complexity; requires expensive server hosting or implementation partners; fragile upgrade path. |

---

## 2. Real User Complaints & Pain Points (Sourced from Store Reviews & SME Forums)
- **Complaint 1 (Tax Compliance Nightmare)**: *"كل برامج الكاشير يا إما برامج أجنبية مفيهاش ربط مع مصلحة الضرائب المصرية، يا إما شركات مصرية بتطلب آلاف الجنيهات عشان تفعل الفاتورة الإلكترونية!"* (Egyptian Retail Owner Forum).
- **Complaint 2 (Internet Dependency)**: *"النت قطع في المحل والكاشير وقف تماماً والزباين واقفين طابور ومش عارفين نطلع فاتورة!"* (Google Play Review on Cloud POS). Lack of true local offline resilience.
- **Complaint 3 (Complex Interface for Staff)**: Egyptian cashiers and retail staff frequently turnover; onboarding a new cashier takes days on complex systems like Odoo or Daftra.

---

## 3. "We Do Better" Advantage Map (SIR Business Superiority)

1. **Native Built-in ETA e-Invoicing & ZATCA**: Out of the box, compliant with Egyptian Tax Authority (ETA) e-receipt v1.0 standard and Saudi ZATCA Phase 2 QR codes without charging thousands in "implementation fees".
2. **True Offline-First POS Engine**: If the internet disconnects, cashiers continue scanning barcodes, printing receipts, and taking cash. All transactions queue in encrypted local IndexedDB/SQLite and auto-sync in background the moment internet restores.
3. **5-Minute Cashier Onboarding**: Clean, high-contrast, tactile UI designed per SIR standards—large touch targets, zero yellow clutter, active-only tab bars, and intuitive Arabic keyboard shortcuts (`F2` Search, `F4` Checkout).
4. **Transparent EGP Pricing**: Fair monthly plans in Egyptian Pounds (e.g. 350 EGP/mo) with zero foreign exchange fees or forced annual commitments.

## Sourcing tasks (open, each under 2 hours)
1. Open the official pages of each POS named here (Loyverse and local Egyptian POS products found by search) and record price, platforms and offline support with links.
2. Read the Egyptian Tax Authority e-invoicing technical pages and record what a POS must implement (link and date).
3. Find 5 public complaints about Egyptian POS software (links).
