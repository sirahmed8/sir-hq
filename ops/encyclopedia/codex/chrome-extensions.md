# chrome-extensions

- Tool: `codex`
- Category: security
- Source: `C:\Users\a7med\.codex\skills\chrome-extensions\SKILL.md`
- SKILL.md size: 26273 chars

## What it does

> Build and publish Chrome Extensions using Manifest V3 best practices. Use this skill whenever the user asks to create, modify, debug, or understand Chrome browser extensions, add-ons, or anything involving the Chrome Extensions API. Trigger on mentions of: 'Chrome extension', 'browser extension', 'manifest.json', 'content script', 'service worker' (in browser context), 'popup' (in browser extension context), 'side panel', 'chrome.* API', 'declarativeNetRequest', 'omnibox', 'context menu' (in extension context), 'userScripts', 'user script', 'script manager', or any request to build functionality that integrates with the Chrome browser UI. Also trigger for publishing to the Chrome Web Store: 'publish extension', preparing an extension for publishing, responding to a review rejection, writing permission justifications, or drafting a privacy policy.

## When to use (from skill text)

- Defining `"side_panel": {"default_path": "..."}` does NOT make it openable. Add a trigger:
- easily trigger this. Use explicit state locking:
- - [ ] Side panel has an explicit open trigger (not just a manifest declaration)

## Structure (headings inside SKILL.md)

- Chrome Extensions
- Part 1 — Building Extensions
- Mandatory Rules
- Always Manifest V3
- Part 2 — Publishing to the Chrome Web Store
- Core Workflow
- How to fill it out
- CHROMEWEBSTORE.md Sections
- Pre-Publish Checklist
- Store Listing Copy Guidelines
- Reference Files
- Output Checklist
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - `host_permissions` is separate from `permissions`
- - **manifest.json changes**: If permissions, host_permissions, or content_scripts changed,
- - **Privacy-relevant changes**: If data collection, storage, or transmission changed,
- 1. Read `manifest.json` to extract name, version, description, permissions, host_permissions

## Key rules (verbatim lines from SKILL.md)

1. - **API throws on property access if not enabled.** Chrome 138+ requires the user to toggle "Allow User Scripts" on the extension's details page; Chrome < 138 requires Developer mode. Always call `isUserScriptsAvailable()` before any `chrome.userScripts.*` call and show an error UI when it returns f
2. - **Messaging requires explicit opt-in.** Call `configureWorld({ messaging: true })` first; listen on `runtime.onUserScriptMessage`, not `runtime.onMessage`.
3. - **`ScriptSource` constraint:** each `js` entry must have exactly one of `code` or `file`. **`id` constraint:** cannot start with `_`.
4. - Every permission and host_permission must have a specific justification (not "needed to work")
5. - Privacy policy URL must be live and match the data use disclosure form

## Files inside the skill

- `references/extensions/api-calling.md` — "Calling External APIs from Extensions"
- `references/extensions/auth-identity.md` — "Authentication with chrome.identity"
- `references/extensions/content-scripts.md` — "Content Scripts & DOM Manipulation"
- `references/extensions/context-menus.md` — "Context Menus"
- `references/extensions/csp-sandbox.md` — "CSP & Sandboxed Code Execution"
- `references/extensions/declarative-net-request.md` — "Declarative Net Request (Content Filtering)"
- `references/extensions/devtools.md` — "DevTools Panels"
- `references/extensions/icons.md` — "Generating Extension Icons"
- `references/extensions/media-capture.md` — "Media Capture (Tab & Desktop)"
- `references/extensions/message-passing.md` — "Message Passing"
- `references/extensions/omnibox.md` — "Omnibox Integration"
- `references/extensions/permissions.md` — "Permissions"
- `references/extensions/popup-ui.md` — "Popup UI"
- `references/extensions/prompt-api.md` — "Chrome Prompt API (LanguageModel) — Extension-Specific Notes"
- `references/extensions/service-worker.md` — "Service Worker Lifetime & State Management"
- `references/extensions/side-panel.md` — "Side Panel"
- `references/extensions/storage.md` — "Chrome Storage API"
- `references/extensions/tab-management.md` — "Tab Management & Groups"
- `references/extensions/user-scripts.md` — "User Scripts API"
- `references/webstore/chromewebstore-template.md` — "CHROMEWEBSTORE.md Template"
- `references/webstore/privacy-policy.md` — "Privacy Policy Guidance"
- `references/webstore/review-checklist.md` — "Pre-Publish Review Checklist"
- `references/webstore/store-listing.md` — "Store Listing Tips & Common Rejections"
