---
name: legal-compliance-shield
description: "Use when adding or reviewing a product's legal pages and agreements: privacy policy matching data collection, liability caps, cookie reject buttons, and DPAs."
---

# Legal Compliance Shield & Agreements Engine ("Anti-Sue" Protocol)

Comprehensive legal compliance, regulatory adherence, and agreement architecture across web and mobile applications to protect businesses from litigation, fines, and user lawsuits.

---

## 1. Mandatory Legal Pages Architecture

Every production application must provide dedicated, publicly accessible routes:

### 1. `/privacy` — Privacy Policy (GDPR / CCPA / CalOPPA compliant)
- **Data Minimization & Exact Match**: State explicitly only what the app genuinely collects (identity, tokens, telemetry).
- **Sub-Processor Directory**: Publish a comprehensive, regularly updated table of third-party sub-processors (AWS, Firebase, Stripe, PostHog, OpenAI, etc.) with location and processing purpose.
- **Data Processing Agreement (DPA)**: Offer a downloadable, legally binding DPA for B2B/enterprise customers.
- **AI Training Consent Shield**: Explicitly state: *"We do NOT train artificial intelligence or machine learning models on customer data without express affirmative opt-in consent."*
- **User Rights (GDPR Art. 15-22)**: Direct self-serve flows to export data (data portability) and permanently delete account data (GDPR Art. 17).
- **Children's Privacy (COPPA / GDPR-K)**: Strict age verification disclaimer (<13 or <16). Zero tracking of minors.

### 2. `/terms` — Terms of Service / Terms & Conditions
- **Liability Cap**: Express liability ceiling capped at the greater of $100 or the total amount paid by user in the preceding 12 months.
- **Warranty Disclaimers**: Disclaim all implied warranties ("AS IS", "AS AVAILABLE").
- **Truthful Claims Guard**:
  - Never claim **SOC 2 Type II** or **ISO 27001** certification unless certified and audited by an accredited independent auditor.
  - Never promise unachievable uptime (e.g., 99.999% SLA) without defined maintenance windows, exclusions, and SLA credit remedies.
- **Customer Logo Permission**: Forbid displaying customer brand logos or testimonials without written authorization.
- **Acceptable Use Policy (AUP)**: Prohibit abuse, scraping, reverse engineering, and unlawful activities.
- **Governing Law & Dispute Resolution**: Mandatory binding arbitration and waiver of class action lawsuits where legally enforceable.

### 3. `/refunds` — Refund & Cancellation Policy
- **Auto-Renewal Disclosure**: Clearly disclose subscription billing frequency, auto-renewal terms, and upcoming charge dates **before** checkout.
- **1-Click Online Cancellation**: In compliance with FTC guidelines, users must be able to cancel their subscription online in the exact same number of clicks it took to sign up (no calling phone numbers or emailing support to cancel).
- **Digital Goods Waiver**: Clear statutory withdrawal terms (e.g., 14-day EU cooling-off waiver upon immediate digital fulfillment).

### 4. `/cookies` — Cookie Policy & Pre-Consent Blocking
- **Pre-Consent Tracker Blocker**: **Strictly forbid loading tracking pixels (Google Analytics, Meta Pixel, Hotjar, TikTok) before the user accepts cookies**.
- **Prominent Reject Button**: The cookie consent banner must provide a **"Reject All"** button with equal visual weight and prominence to the "Accept All" button (GDPR requirement).
- **Granular Controls**: Opt-in toggles for Necessary, Functional, Analytics, and Advertising categories. Never pre-check non-essential categories.

---

## 2. Forms, Consents, Licenses & Email Hygiene

- **Explicit Checkbox Consent**: Signup and checkout forms must feature an un-checked box:
  `[ ] I agree to the Terms of Service and Privacy Policy.`
- **Package & Dependency License Audit**:
  - Automatically audit `package.json` / `requirements.txt` against open-source licenses (SPDX).
  - Flag and eliminate viral GPL/AGPL licenses in proprietary commercial codebases; enforce permissive licenses (MIT, Apache-2.0, BSD-3, ISC).
- **Asset & Font Licensing**:
  - Verify all fonts, icons, and imagery have commercial use licenses. Eliminate unlicensed Google Fonts downloads or pirated typography.
- **Marketing & Transactional Email Compliance (CAN-SPAM / GDPR)**:
  - Every marketing email must include a verified, 1-click `Unsubscribe` link and a physical corporate address in the footer.
  - Honor unsubscribes immediately (<24 hours) via automated webhook.
- **Accessibility Checks (ADA / WCAG 2.1 AA)**:
  - Maintain WCAG 2.1 AA compliance across all public pages to prevent predatory ADA accessibility lawsuits.
