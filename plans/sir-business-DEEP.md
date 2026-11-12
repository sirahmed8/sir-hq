# DEEP PLAN & MASTER SPEC: SIR Business
**Project**: SIR Business (`D:/Projects/SIR Business`)  
**Mission**: Sovereign Multi-Vertical Retail POS, Inventory Engine & Commerce Operating System  
**Consolidation**: Unifies `SIR Market`, `SIR Restaurant`, `SIR Pharmacy`, and `SIR Library`  
**Offline Invariant**: 100% offline-first operations; cash drawer and barcode scanner work with zero internet  
**Version**: 1.0.0 (Strictly enforced)  
**Standard**: `_SIR/standard/23-premium-code-bar.md` & `_SIR/plans/GEMINI_QUALITY_CHARTER.md`

---

## 1. Executive Summary & Product Purpose
SIR Business is an agency-grade, offline-resilient point-of-sale (POS) and inventory operating system built specifically for small-to-medium businesses across Egypt. By unifying four previously isolated vertical applications (`SIR Market`, `SIR Restaurant`, `SIR Pharmacy`, `SIR Library`), SIR Business provides a unified modular engine that adapts dynamically to the merchant's business model while maintaining lightning-fast offline barcode checkouts, thermal receipt printing, stock expiry alerts, and real-time sales telemetry.

---

## 2. Legacy Forensic Audit & Porting Analysis

### 2.1 Existing Legacy Assets (`SIR Business/legacy/`)
1. **`SIR Market`**: Retail grocery POS with USB barcode reader support, quick-key produce items, cashier shift closing, and stock reorder warnings.
2. **`SIR Restaurant`**: Kitchen Display System (KDS), table floor plan mapping, dine-in/takeaway/delivery modes, and split billing.
3. **`SIR Pharmacy`**: Drug inventory tracking active pharmaceutical ingredients (API), Egyptian trade names, generic alternatives, and batch expiry dates.
4. **`SIR Library`**: Book borrowing cycles, membership barcode scanner, overdue fine calculators, and stationery inventory.

### 2.2 What is Valuable to Port
- **Sub-100ms Barcode & SKU Checkout Engine**: Keyboard-only checkout flow designed for rapid cashiers with instant numpad shortcuts.
- **Raw ESC/POS Thermal Receipt Generator**: Native binary command generator for 58mm and 80mm ESC/POS thermal printers via USB/Bluetooth/Network.
- **Pharmacy Generic Drug Substitution Engine**: Algorithmic cross-referencing of active chemical ingredients to suggest in-stock alternatives.
- **Kitchen Order Routing (KDS)**: Order status pipelines routing hot items to kitchen displays and cold items to beverage stations.

### 2.3 What Must Be Discarded
- Duplicate redundant Electron wrappers across each vertical; replaced with a single high-performance Tauri/PWA architecture.
- Hardcoded database credentials and brittle flat-file JSON databases.

---

## 3. Architecture & Design Identity

### 3.1 Technical Architecture
- **Frontend / Client**: Next.js 14 / Tauri desktop client with local SQLite database for 100% offline execution.
- **Sync Engine**: Background WebSocket synchronization replicating offline sales transactions to central cloud when connectivity is available.
- **Hardware Integration**: WebHID and WebSerial APIs for direct USB barcode scanners, electronic weighing scales, and cash drawer kickers.
- **Thermal Printing**: Direct binary ESC/POS byte-stream generator with customizable logo and QR code encoding.

### 3.2 Design Identity
- **Brand Aesthetic**: Merchant Ledger Emerald & Brushed Brass. Professional, surgical, trustworthy, and lucrative.
- **Palette**:
  - Primary Merchant Emerald: `#059669` (Emerald 600) / `#047857` (Emerald 700)
  - Secondary Brass Gold: `#D97706` (Amber 600)
  - Dark Surface Base: Deep Ledger Obsidian (`#07100D` / `#0C1D18`)
  - Elevated Glass: Translucent Slate Glass (`rgba(12, 29, 24, 0.75)` with `backdrop-filter: blur(14px)`)
  - High-Contrast Text: `#F0FDF4`
  - **Zero Yellow Buttons**: Enforced semantic emerald, sapphire, and slate tokens.
- **Typography**: Precision billing typography (`Inter`, `Cairo`, `JetBrains Mono` for currency amounts, barcodes, and SKUs).
- **Motion**: Dynamic Island spring transitions (`cubic-bezier(0.16, 1, 0.3, 1)`), active-only tab labels, tactile numpad press scale (`0.98`).
- **Emblem**: Vector SVG geometric commerce hexagonal seal with central balancing scale and golden merchant grain.

---

## 4. Dependencies, Cross-Project Links & Risks
- **Provides**: Real-world commercial transaction processing and inventory models to `the shared kit`.
- **Consumes**: Owner authentication, signed webhooks, and billing fallback from `the shared kit`.
- **Risks**: Connectivity drops during peak shopping hours; thermal printer driver fragmentation; stock count drift between shifts.

---

## 5. The First 25 Prioritized Tasks

### BZ-101 | Unified Multi-Vertical SQLite Schema Architecture
- **Files**: `src/db/schema.sql`, `src/db/migrations/001_business_core.sql`
- **Steps**: Build normalized schema supporting products, variants, batches, orders, order items, tables, and customers with vertical-specific JSON extensions.
- **Acceptance**: Schema compiles with foreign keys and indexes on `barcode`, `sku`, `category_id`, and `created_at`.

### BZ-102 | Sub-50ms Offline Barcode Checkout Engine
- **Files**: `src/components/pos/CheckoutTerminal.tsx`, `src/lib/barcodeScanner.ts`
- **Steps**: Implement keyboard-first POS terminal: global barcode scanner listener, instant SKU match, quantity multiplier (`3*123456`), and subtotal update.
- **Acceptance**: Scanning barcode adds item to cart and recalculates tax/discounts in under 50ms with zero network calls.

### BZ-103 | Raw ESC/POS Thermal Receipt Binary Generator
- **Files**: `src/lib/escposGenerator.ts`, `src/lib/printerService.ts`
- **Steps**: Author pure JavaScript binary generator outputting ESC/POS byte streams (header logo, itemized table, QR code, cut command).
- **Acceptance**: Sends binary payload over WebSerial or raw network socket; prints crisp, perfectly aligned 80mm receipt.

### BZ-104 | Dynamic Island Active-Only Tab Navigation
- **Files**: `src/components/nav/TabBar.tsx`, `src/app/globals.css`
- **Steps**: Unified navigation bar (POS, Inventory, Orders, Kitchen/Tables, Reports) displaying text label only on active tab.
- **Acceptance**: Inactive tabs collapse to monochrome SVG icons; active tab smoothly reveals text label.

### BZ-105 | Pharmacy Generic Drug Chemical Substitution Engine
- **Files**: `src/lib/drugSubstitution.ts`, `src/components/pharmacy/AlternativeModal.tsx`
- **Steps**: Index active pharmaceutical ingredients (API); when an out-of-stock medicine is searched, list in-stock generic equivalents with identical dosage.
- **Acceptance**: Searching out-of-stock "Panadol Extra" instantly suggests available "Adol Extra" with price comparison.

### BZ-106 | Restaurant Interactive Table Floor Plan & Bill Splitter
- **Files**: `src/components/restaurant/TableGrid.tsx`, `src/components/restaurant/BillSplitterModal.tsx`
- **Steps**: Visual table layout showing occupied/vacant states, seated duration, order subtotal, and 1-tap bill splitting by seat.
- **Acceptance**: Dragging table layout persists positions; splitting bill creates separate itemized receipts.

### BZ-107 | Kitchen Display System (KDS) Real-Time Order Pipeline
- **Files**: `src/components/restaurant/KitchenDisplay.tsx`
- **Steps**: Dedicated full-screen kitchen tablet view; orders appear in real time with cooking timer alerts (Green <10m, Amber 10-20m, Red >20m).
- **Acceptance**: Tapping "Mark Ready" sends audio chime to waiter tablet and advances order state.

### BZ-108 | Library Member Card Barcode Scanner & Borrow Tracker
- **Files**: `src/components/library/BorrowTerminal.tsx`, `src/lib/overdueCalculator.ts`
- **Steps**: Scan member card, scan book barcode; automatically calculate return due date (14 days) and compute overdue fine accruals.
- **Acceptance**: System records checkout in 1 tap and displays member's current active borrowed book count.

### BZ-109 | Cashier Shift Reconciliation & Cash Drawer Float Audit
- **Files**: `src/components/pos/ShiftClosingModal.tsx`, `src/lib/shiftReport.ts`
- **Steps**: End-of-shift closing workflow: input counted cash, card receipts, and expenses; compute over/short variance with printed Z-Report.
- **Acceptance**: Generates printable shift summary showing expected vs actual cash with signature lines.

### BZ-110 | Batch Expiry Date Tracking & Early Warning Dashboard
- **Files**: `src/components/inventory/ExpiryTracker.tsx`
- **Steps**: Track expiration dates per inventory lot/batch; highlight products expiring in 30, 60, and 90 days with discount promotion tags.
- **Acceptance**: Expiry tab lists urgent batches in crimson with 1-tap "Apply 25% Clearance Discount".

### BZ-111 | Electronic Weighing Scale WebSerial Bridge
- **Files**: `src/lib/weighingScale.ts`
- **Steps**: Connect electronic weighing scale via WebSerial API; automatically capture live weight for produce items and calculate price.
- **Acceptance**: Placing item on scale updates weight in POS cart instantly without manual typing.

### BZ-112 | Egyptian Tax Authority (ETA) e-Invoicing Compliance Blueprint
- **Files**: `src/lib/etaCompliance.ts`, `docs/E_INVOICE_SPEC.md`
- **Steps**: Implement JSON invoice formatting, canonical hashing (SHA-256), and e-seal placeholder specs matching Egyptian Tax Authority regulations.
- **Acceptance**: Generates ETA-compliant UBL 2.1 invoice JSON payload with validated UUID.

### BZ-113 | Bespoke Vector SVG Merchant Brand Assets
- **Files**: `public/logo.svg`, `public/favicon.svg`
- **Steps**: Craft vector logo featuring hexagonal merchant seal and golden balance scales; render multi-size favicons and PWA icons.
- **Acceptance**: Clean vector SVG rendering across mobile PWA and POS terminals.

### BZ-114 | Low-Stock Automatic Reorder Draft Generator
- **Files**: `src/lib/reorderAdvisor.ts`, `src/components/inventory/ReorderModal.tsx`
- **Steps**: Calculate average daily sales velocity; automatically generate purchase order drafts to suppliers when stock falls below reorder point.
- **Acceptance**: 1-tap "Generate Supplier PO" compiles itemized purchase order PDF.

### BZ-115 | Offline First Data Sync & Conflict Resolution Protocol
- **Files**: `src/lib/offlineSync.ts`
- **Steps**: Store all offline sales in SQLite transaction queue; replicate to remote cloud when online using deterministic timestamp sequencing.
- **Acceptance**: Disconnecting network during 20 checkouts and reconnecting syncs all 20 orders with zero duplicates.

### BZ-116 | Customer Loyalty Points & WhatsApp Digital Receipts
- **Files**: `src/lib/loyaltyEngine.ts`, `src/lib/whatsappReceipt.ts`
- **Steps**: Accrue loyalty points per pound spent; offer customer choice between paper thermal receipt or instant WhatsApp digital PDF link.
- **Acceptance**: WhatsApp link dispatches formatted digital receipt with customer's earned reward balance.

### BZ-117 | Multi-User Role Permissions & Manager Override PIN
- **Files**: `src/lib/authRoles.ts`, `src/components/auth/ManagerPinModal.tsx`
- **Steps**: Enforce cashier role permissions (cannot delete items or apply >10% discount without manager PIN challenge).
- **Acceptance**: Attempting to void a line item prompts for Manager PIN with visual shake animation on failure.

### BZ-118 | Fast Numpad Keyboard Shortcuts Cheat Sheet
- **Files**: `src/components/pos/ShortcutModal.tsx`
- **Steps**: Map entire checkout flow to standard numpad: `+` for cash exact, `Enter` to finalize, `F1` search, `F4` discount, `Esc` cancel.
- **Acceptance**: Pressing `?` displays tactile shortcut cheat sheet modal.

### BZ-119 | Multi-Screen Responsive POS Verification (320px to 4K)
- **Files**: `tests/responsive_business.test.mjs`
- **Steps**: Playwright tests verifying checkout terminals, tables, and inventory tables across 320px mobile, 1024px iPad, and 1080p POS touchscreens.
- **Acceptance**: Zero horizontal overflow and zero button clipping across all devices.

### BZ-120 | Owner Mobile Companion Live Sales Stream
- **Files**: `src/components/owner/MobileSalesStream.tsx`
- **Steps**: Mobile-optimized dashboard view for business owner on iPhone showing live hourly sales, cash in register, and top-selling items.
- **Acceptance**: Updates sales metrics over Tailnet connection in real time.

### BZ-121 | Inventory Stock Count Audit with Camera Barcode Scanner
- **Files**: `src/components/inventory/CameraAuditor.tsx`
- **Steps**: Mobile camera barcode scanner for fast physical stocktaking in warehouse; scan shelf items to record actual vs system quantity.
- **Acceptance**: Scanning items rapidly increments counted stock and flags inventory discrepancies.

### BZ-122 | Dark Slate & Daylight Retail Glass Theme Engine
- **Files**: `src/hooks/useMerchantTheme.ts`
- **Steps**: Zero-flash theme switcher; daylight mode tuned for high-ambient retail shop lighting with 7:1+ contrast.
- **Acceptance**: Switching theme updates all CSS custom properties instantly with zero white flash.

### BZ-123 | Automated Daily Financial Reconciliation Digest Routine
- **Files**: `scripts/daily_financial_digest.py`
- **Steps**: Scheduled midnight task compiling total revenue, gross margin, cash vs card breakdown, and tax into an executive PDF/Telegram report.
- **Acceptance**: Script delivers concise Arabic daily finance brief to Ahmed's iPhone.

### BZ-124 | Cash Drawer Hardware Kick Pulse Driver
- **Files**: `src/lib/cashDrawer.ts`
- **Steps**: Generate standard ESC/POS pulse command (`ESC p m t1 t2` / `\x1b\x70\x00\x19\xfa`) to trigger RJ11/RJ12 cash drawer opening on cash payment.
- **Acceptance**: Finalizing cash payment sends kick pulse to connected thermal printer.

### BZ-125 | End-to-End Automated Business Verification Suite
- **Files**: `scripts/verify.ps1`, `tests/test_business_integrity.py`
- **Steps**: Validate offline checkout, barcode math, ESC/POS generator, drug substitution, and verify gates.
- **Acceptance**: `verify.ps1` runs in under 3 seconds with 100% green gates.


---

## 5. Mandatory Standards 24 to 27 Architecture

### 5.1 Launch Package (Standard 24)
- **Identity & Domain**: Fresh dedicated repository (`sirahmed8/sir-business`), clean Supabase project (`sir-business-prod`), target domain `sirbusiness.app` or `sirbusiness.eg` (~$12.00 / ~550 EGP/yr).
- **Supported Platforms & Build Commands**:
  - Web & PWA: `npm run build` (Next.js 15 static + SSR).
  - Desktop (Windows / macOS / Linux): `npm run tauri build` (Tauri v2 native shell with embedded SQLite).
  - Tablet (Android / iPadOS): `npx cap sync && npx cap build` (Capacitor tablet POS).
- **Security Tasks**:
  - Server-side role-based access control (Admin, Manager, Cashier).
  - HMAC-SHA256 signature verification and 5-minute replay window on all Paymob webhooks.
  - Encryption-at-rest for local offline SQLite database using SQLCipher.
- **Fair EGP Subscription Model**:
  - Starter Plan: 350 EGP / month or 3,500 EGP / year.
  - Growth Plan: 650 EGP / month or 6,500 EGP / year.
  - Payment Gateway: Paymob (Cards, Mobile Wallets, Meeza) and Fawry.
  - Fallback Mode: When live payment keys are missing, displays "Subscriptions Launching Soon - Contact Sales" with email capture.
- **Owner Activation Checklist (Plain Arabic & English for Ahmed)**:
  1. Buy domain `sirbusiness.app` on Namecheap (~$12.00 / 550 EGP) and point DNS CNAME to Vercel.
  2. Paste Paymob keys into `D:\Projects\SIR Business\.env`.
  3. Verify: Open `/pricing`, test 350 EGP checkout in test mode, verify receipt renders with ETA compliance.

### 5.2 Market-Grade Compliance (Standard 25)
- **Competitor Study**: Documented in `_SIR/plans/competitors/sir-business.md` with cited sources comparing against Daftra, Loyverse, Foodics, and Odoo.
- **Regional Regulatory & Tax Compliance**:
  - Egypt: Full compliance with Egyptian Tax Authority (ETA) e-receipt v1.0 standard and Egyptian Data Protection Law 151/2020.
  - Saudi Arabia: Compliance with ZATCA (Fatoora) Phase 2 QR code standards.
- **Privacy-First Analytics**: Opt-in anonymized telemetry measuring transaction velocity and error stack traces; zero customer phone numbers or basket item details captured.
- **Legal Pack with Lawyer Disclaimer**: Pre-drafted Terms of Service, SLA, and Privacy Policy, marked: *"AI-drafted for technical clarity; to be reviewed by a qualified Egyptian attorney before commercial launch."*

### 5.3 Autonomous Operations (Standard 26)
- **In-Product Assistant**: "مساعد التاجر" - embedded support assistant grounded in POS user manuals, printer setup guides, and ETA tax guidelines.
- **Operations Runbook**: Nightly database snapshots, automated offline transaction reconciliation daemon, error log digests, and health check route (`/api/v1/status`).
- **12-Week Marketing Launch Calendar**: Pre-launch merchant waitlist (Weeks -2 to 0), local retail onboarding in Obour City and New Cairo (Weeks 1 to 4), pharmacy network outreach (Weeks 5 to 8), restaurant chain referral blitz (Weeks 9 to 12).
- **Escalation & Guard Rails**: Maximum daily external AI spend capped at $4.00/day. Chairman notified via Telegram bot ONLY for tax server disconnections or payment gateway disruptions.

### 5.4 Visibility & Discovery (Standard 27)
- **High-Intent Search Queries**:
  - Arabic: *"برنامج كاشير سحابي مصر", "برنامج الفاتورة الإلكترونية المصرية", "سيستم إدارة مطاعم ونقاط بيع"*
  - Egyptian Slang: *"أفضل سيستم كاشير للمحلات", "برنامج فواتير للمحل سهل ورخيص", "كاشير بالجنيه"*
  - English: *"Egyptian POS software", "ETA e-invoicing ERP Egypt", "cloud retail point of sale"*
- **Generative Engine Optimization (GEO)**: Publishes validated `llms.txt` and `/facts` page with structured POS pricing, tax capabilities, and direct entity definitions.
- **Technical SEO & Structured Data**: Pre-rendered Next.js metadata, valid `SoftwareApplication` JSON-LD schema, and automated weekly AI visibility testing script (`scripts/check_ai_visibility.py`).
