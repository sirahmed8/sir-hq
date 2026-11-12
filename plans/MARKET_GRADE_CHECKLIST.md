# SIR PORTFOLIO MARKET-GRADE COMPLIANCE CHECKLIST
**Target**: Autonomous Gemini HQ Manager & Product Auditors  
**Standard**: Standard 25 (`25-market-grade.md`)  
**Scope**: All 17 Workspace Projects (`D:\Projects`) · Version: 1.0.0 (Strictly enforced)

---

## 1. Portfolio Compliance Matrix by Product

| Project | Competitor File | Egypt PDPL / Tax | Gulf (KSA/UAE) Fit | GDPR / CCPA Pack | Privacy Analytics | Legal Disclaimers | Enterprise Extra |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **SIR Hagoozat** | `competitors/sir-hagoozat.md` | Yes Paymob/ETA | Yes Mada/ApplePay | Yes WCAG 2.2 AA | Yes Opt-in | Yes Lawyer Notice | Yes Status page |
| **SIR Business** | `competitors/sir-business.md` | Yes ETA e-invoice | Yes ZATCA Phase 2 | Yes Full DPA | Yes Opt-in | Yes Lawyer Notice | Yes Multi-tenant |
| **SIR Education Hub** | `competitors/sir-education-hub.md` | Yes Student privacy | N/A | Yes Safe storage | Yes Pseudonymous | Yes Terms of Use | Yes Rate-limiting |
| **SIR Negm Furniture** | `competitors/sir-negm-furniture.md`| Yes Consumer Prot. | Yes GCC Shipping | Yes Export terms | Yes Privacy-first | Yes Lawyer Notice | Yes 3D fallback |
| **SIR Content Studio** | `competitors/sir-content-creation-studio.md`| Yes Local creator | Yes Arabic LLM | Yes GDPR export | Yes Opt-in | Yes AI Disclosure | Yes Token caps |
| **SIR AI** | `competitors/sir-ai.md` | Yes Local models | Yes Arabic tokens | Yes Local-first | Yes Zero cloud PII | Yes AI Output limit | Yes Offline sync |
| **SIR Controller** | `competitors/sir-controller.md` | Yes HW privacy | Yes Universal | Yes Zero tracking | Yes Local telemetry| Yes HW Safe terms | Yes Rollback safe |
| **SIR Laptop Manager**| N/A (Internal tool) | Yes Local hardware | N/A | Yes Local only | No Local only | N/A | Yes Silent daemons |
| **AHome** | N/A (STRICTLY PRIVATE) | No Zero outside | No Zero outside | No Zero outside | No Zero analytics| No Private | Yes Air-gapped |
| **SIR Jobs** | N/A (Private career) | Yes Private user | N/A | Yes Local-first | No Private only | N/A | Yes Encrypted DB |
| **SIR Study** | N/A (Private study) | Yes Student notes | N/A | Yes Local-first | No Private only | N/A | Yes Backup drill |
| **SIR Life** | `competitors/sir-life.md` | Yes Health privacy | Yes Hijri calendar| Yes GDPR health | Yes Opt-in local | Yes Medical limit | Yes Export JSON |
| **SIR ModPack** | `competitors/sir-modpack.md` | Yes Local mirrors | Yes Universal | Yes COPPA (age 13+)| Yes Opt-in | Yes Minecraft EULA | Yes Hash verify |
| **SIR Mods for GTA V** | `competitors/sir-mods-for-gta-v.md`| Yes Local mirrors | Yes Universal | Yes Fair use DMCA | Yes Opt-in | Yes Rockstar EULA | Yes Safe backup |
| **SIR Portfolio** | `competitors/sir-portfolio.md` | Yes Founder profile | Yes Regional bio | Yes Cookie banner | Yes Plausible/Umami| Yes Copyright | Yes GEO llms.txt |
| **the shared kit** | N/A (Shared library) | Yes Standard | Yes RTL standard | Yes A11y standard | No Library only | Yes MIT / Proprietary| Yes Test suite |
| **_SIR** | N/A (HQ Control Room) | Yes Ops truth | N/A | N/A | No Internal only | N/A | Yes Telegram bot |

---

## 2. Universal Country & Regional Compliance Verification

### Egypt (Primary Home Market)
- [ ] **Egyptian Data Protection Law (Law 151/2020)**: User consent recorded, data controller role defined, right to modify and purge personal data within 72 hours.
- [ ] **Egyptian Tax Authority (ETA) e-Invoicing**: SIR Business and SIR Hagoozat include valid Tax ID fields, 14% VAT calculation, and standard Egyptian electronic receipt formatting.
- [ ] **Payment Methods**: Paymob (Cards, Mobile Wallets: Vodafone Cash, Orange Money, Etisalat Cash, WE Pay, Meeza) and Fawry Reference Code.
- [ ] **Localization**: Arabic (Egyptian dialect support for marketing & conversational UI; Modern Standard Arabic for formal receipts and legal pages).

### Gulf Region (Saudi Arabia & UAE)
- [ ] **KSA Personal Data Protection Law (PDPL)** & **UAE Federal Decree-Law No. 45/2021**: Mandatory explicit consent checkboxes; data residency compliance for commercial records.
- [ ] **ZATCA (Fatoora) Phase 2**: Standardized QR code generation in invoices (Base64 TLV format: Seller Name, VAT Number, Timestamp, Total with VAT, VAT Total).
- [ ] **Payments**: Mada debit cards, Apple Pay integration, STC Pay.
- [ ] **Calendar & Typography**: Dual Gregorian/Hijri date picker toggle; high-contrast Arabic typography (Alexandria / Cairo font).

### European Union & United Kingdom
- [ ] **GDPR / UK GDPR**:
  - Zero non-essential cookies or trackers executed before affirmative user consent.
  - Granular consent preferences modal (Necessary, Functional, Analytics).
  - One-click "Download My Data" (JSON export) and "Delete Account & All Data" flows.
- [ ] **European Accessibility Act & WCAG 2.2 AA**:
  - Minimum 4.5:1 text contrast ratio (3:1 for large text).
  - Complete keyboard navigation with visible focus rings (`focus-visible:ring-2`).
  - Screen reader tested ARIA labels on all SVG icons and buttons.

### United States
- [ ] **CCPA / CPRA**: "Do Not Sell or Share My Personal Information" link in footer.
- [ ] **COPPA Compliance**: Age gate (13+ or 18+ depending on product category). No targeted profiling of minors.

---

## 3. Privacy-First Opt-In Analytics Architecture

For all public commercial products (Hagoozat, Business, Education Hub, Studio, Controller, Life):
1. **Zero Tracking by Default**: No telemetry beacons send data until the user confirms on the privacy banner.
2. **Pseudonymous UUID**: User IDs are hashed with a daily salt; no real IP addresses, phone numbers, or email addresses in telemetry payloads.
3. **Excluded Telemetry**:
   - Zero chat prompt content or message bodies.
   - Zero form input values or financial credentials.
   - Zero personal media files or camera/microphone streams.
4. **Permitted Signals**: Aggregate page load latency, feature click frequency, error stack traces (sanitized), viewport device category (Mobile/Desktop/Tablet).

---

## 4. Legal Protection Pack & Honest Limitation

Every public product repository MUST include pre-drafted legal pages in `public/legal/` or `src/app/legal/`:
1. `terms-of-service.md`: Clear user commitments, fair subscription renewal, payment terms, and limitation of liability.
2. `privacy-policy.md`: Exact description of collected data, retention duration, and deletion rights.
3. `cookie-policy.md`: Explicit list of cookies, local storage keys, and third-party gateways.
4. `refund-policy.md`: Clear Egyptian Consumer Protection Law (Law 181/2018) compliance (14-day defect refund, digital subscription policy).

> [!IMPORTANT]
> **The Honest Legal Disclaimer**:
> Every legal document generated across SIR products must prominently state:
> *"This agreement is AI-drafted for technical and operational transparency. It must be reviewed and endorsed by a qualified legal attorney in the relevant jurisdiction prior to commercial launch."*
> This lawyer review step is permanently tracked in `LAUNCH_CHECKLIST_ALL.md`.

---

## 5. Enterprise "Big Company" Extra Polish Checklist

Before any public product is deemed "Market-Grade", it must satisfy all 10 polish bars:
- [ ] **1. Public Status Page**: Configured or pre-built (e.g. `/status` route displaying API latency, DB connectivity, and uptime).
- [ ] **2. Security Vulnerability Disclosure**: `/.well-known/security.txt` containing security email contact and PGP key placeholder.
- [ ] **3. Rate Limiting**: Token bucket rate-limiter on all public API endpoints (max 60 requests/min per IP).
- [ ] **4. Atomic Rollback Transactions**: All database writes executed inside transactions; automatic rollback on failure.
- [ ] **5. Tested Backup & Restore**: Automated nightly database dump script with verified test restore script.
- [ ] **6. In-App Contextual Help**: Searchable FAQ drawer answering common user hurdles in Arabic and English.
- [ ] **7. Honest Empty States**: Zero fake reviews or placeholder cards; clear actionable illustration with "Add your first item" prompt.
- [ ] **8. Email Delivery Authentication**: SPF, DKIM, and DMARC DNS records documented for transactional mail domains.
- [ ] **9. Fast CDN Asset Delivery**: Images converted to WebP/AVIF with responsive `srcset` and `fetchpriority="high"` on LCP hero elements.
- [ ] **10. Zero Dependency Security Flaws**: `npm audit` or `pip audit` returning 0 high or critical vulnerabilities.
