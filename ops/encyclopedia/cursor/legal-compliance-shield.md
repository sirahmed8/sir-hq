# legal-compliance-shield

Source read: `C:\Users\a7med\.claude\skills\legal-compliance-shield\SKILL.md` (4.7 KB; claude revision; codex/cursor/kilo/opencode/windsurf listed).

## Summary
The "Anti-Sue" legal architecture for production apps: four mandatory public routes. `/privacy` — exact-match data disclosure, published sub-processor directory, downloadable DPA for B2B, explicit "no AI training on customer data without opt-in" clause, GDPR Art.15-22 self-serve export/delete, COPPA/age disclaimers. `/terms` — liability cap at greater of $100 or 12-month fees, "AS IS" warranty disclaimer, truthful-claims guard (no SOC 2/ISO claims without audit, no impossible SLAs, no customer logos without written permission), AUP, binding arbitration + class-action waiver. `/refunds` — auto-renewal disclosure before checkout, 1-click cancellation matching signup click-count (FTC), digital-goods cooling-off waiver. `/cookies` — pre-consent tracker blocking (no GA/Meta/Hotjar/TikTok pixels before accept), equal-prominence Reject All, granular unticked-by-default toggles. Plus form/licensing/email hygiene: unchecked ToS checkbox, SPDX license audit (kill GPL/AGPL in proprietary code), commercial font/asset licensing, CAN-SPAM unsubscribe + physical address + <24h honoring, WCAG 2.1 AA.

## When to use / when NOT
Use when adding or reviewing legal pages, checkout flows, cookie banners, or auditing licenses/assets for a commercial product. Do NOT treat it as legal advice — it is a compliance checklist; jurisdiction-specific counsel may still be needed. Not for internal tools with no public users.

## Inputs, outputs, tools
- Inputs: the app's actual data collection, payment/subscription model, trackers in use, dependency list.
- Outputs: the four routes' content requirements, consent/banner specs, audit checklist results.
- Tools: none — guidance only; pairs with the project's router/pages.

## 5 most important rules
1. Privacy policy must match REAL data collection exactly — no aspirational claims.
2. No trackers load before cookie consent; Reject All has equal visual weight to Accept All.
3. Cancellation takes the same number of clicks as signup; auto-renewal disclosed pre-checkout.
4. Never claim certifications (SOC 2, ISO) or uptime numbers that aren't audited/true; no customer logos without written permission.
5. Audit dependency licenses (SPDX) and asset/font licenses; GPL/AGPL and unlicensed fonts must go.

## Risks / owner notes
Non-compliance is the owner's legal exposure — GDPR fines and ADA lawsuits are named risks. Pages must be customized to what the product actually does/collects; copying boilerplate creates false statements.

## Category and tags
Category: security. Tags: legal, privacy, gdpr, cookies, terms, refunds, licensing, compliance.
