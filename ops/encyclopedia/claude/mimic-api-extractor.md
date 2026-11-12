# mimic-api-extractor

- Tool: `claude`
- Category: security
- Source: `C:\Users\a7med\.claude\skills\mimic-api-extractor\SKILL.md`
- SKILL.md size: 2052 chars

## What it does

Use when reverse-engineering network traffic from a HAR file, proxy capture, or DevTools log into typed Python or TypeScript client SDKs.

## Structure (headings inside SKILL.md)

- Mimic API Extractor (Traffic-to-Code Reverse Engineering)
- 1. Core Workflow
- 2. Extraction & Deconstruction Protocol
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Identify base URLs, versioned endpoints (`/api/v1/...`), HTTP methods (`GET`, `POST`, `PUT`, `DELETE`).
- - Extract Bearer JWT tokens, OAuth token refresh patterns, session cookies, CSRF tokens, custom headers (e.g. `x-api-key`, device fingerprint headers).
- - Abstract auth into a pluggable `AuthHandler` or token refresh manager so credentials aren't hardcoded.
- - Produce a single, modular client library:

## Key rules (verbatim lines from SKILL.md)

1. 1. **Traffic Capture Analysis**:
2. - Inspect HAR archives, mitmproxy dumps, or Chrome DevTools network logs (`list_network_requests`).
3. - Identify base URLs, versioned endpoints (`/api/v1/...`), HTTP methods (`GET`, `POST`, `PUT`, `DELETE`).

## Files inside the skill

- (SKILL.md only)
