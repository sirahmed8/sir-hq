# vibe-auth-hardening

- Tool: `codex`
- Category: security
- Source: `C:\Users\a7med\.codex\skills\vibe-auth-hardening\SKILL.md`
- SKILL.md size: 3336 chars

## What it does

Fixes 5 critical auth flaws: cookie security, server-side RBAC, 2FA/OTP, and rate-limited endpoints.

## When to use (from skill text)

- - **Per-Account**: Max 5 failed attempts per 15 minutes; trigger account lock and notification email on excess failures.

## Structure (headings inside SKILL.md)

- Vibe-Coded Auth Hardening Shield
- 1. The 5 Fatal Flaws & Required Fixes
- 2. Implementation Specifications
- Flaw 1: Session Token in `localStorage`
- Flaw 2: Client-Side Admin Checks
- Flaw 3: Missing 2FA / OTP Flow
- Flaw 4: Missing Rate Limiting on Login & Password Reset
- Flaw 5: Weak Passwords & Missing Breach Verification
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Vulnerability**: Any XSS vulnerability allows malicious JavaScript to execute `localStorage.getItem('token')` and hijack the account.
- - Store tokens strictly in **`HttpOnly; Secure; SameSite=Strict`** cookies.
- - Implement short-lived Access Tokens (15 min) + Refresh Tokens stored in partitioned database tables with rotation on each refresh.
- - Provide standard Time-based One-Time Password (TOTP) compatible with Google Authenticator / 1Password using `speakeasy` or `otplib`.

## Key rules (verbatim lines from SKILL.md)

1. - Apply progressive delays (exponential backoff) after consecutive failed attempts.

## Files inside the skill

- (SKILL.md only)
