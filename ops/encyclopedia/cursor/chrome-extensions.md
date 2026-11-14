# chrome-extensions

## Summary
Manifest V3 Chrome extension development and Chrome Web Store publishing playbook. Part 1 lists 20 mandatory rules that prevent common broken builds: real icon files or omit them; explicit side-panel open triggers; CSP-safe code execution (sandbox/blob/srcdoc); `tabs` permission for `tab.url`; async/await only; batched content-script DOM updates; no state in service-worker globals (use `chrome.storage` + `chrome.alarms`); stable extension ID via manifest `key` for OAuth; context-menu user feedback; Prompt API availability; `action` manifest key for `chrome.action`; `activeTab` limits; DevTools panel paths relative to extension root; offscreen document API restrictions; real image files for notifications/badges; tab/desktop capture state locking; `desktopCapture` targetTab; user-scripts pitfalls; no `chrome.windows.query()`; gesture-safe `permissions.request`. Part 2 maintains `CHROMEWEBSTORE.md` as the single source of truth, with a pre-publish checklist and store-listing copy rules.

## When to use / when NOT
Use when creating, modifying, debugging, or publishing a Chrome extension (MV3). Do NOT generate Manifest V2 code or skip the output checklist.

## Inputs, outputs, tools
- Inputs: `manifest.json`, source files, icon assets, `CHROMEWEBSTORE.md`.
- Outputs: unpacked extension, store listing metadata, privacy policy, ZIP (excluding `.git/`, `node_modules/`, `.env`, `CHROMEWEBSTORE.md`).
- Tools: Chrome, `chrome://extensions`, Chrome Developer Dashboard, `references/extensions/*.md` and `references/webstore/*.md`.

## 5 most important rules
1. Manifest V3 only: `service_worker`, `chrome.action`, `chrome.scripting`, separate `host_permissions`, no inline scripts.
2. Never reference icon/image files that do not exist; generate them or omit the field.
3. Service workers are ephemeral — persist all state in `chrome.storage`; use `chrome.alarms`, not `setTimeout`.
4. Side panels need an explicit open trigger (`onClicked` or `setPanelBehavior` with `openPanelOnActionClick`).
5. Every permission and host_permission needs a specific justification in `CHROMEWEBSTORE.md`.

## Risks / things needing the owner
Publishing needs a Chrome Developer account, OAuth client updates after store assignment, a live privacy policy URL, and screenshots. Some APIs require user gestures or toggles (user scripts "Allow User Scripts").

## Category / tags
security · chrome, extensions, manifest-v3, csp, service-worker, webstore, publishing

## Revisions
Five tools hold it (codex, cursor, gemini-plugin, kilo, opencode, windsurf — no claude); codex copy chosen, all 26273 chars identical across tools. References: 19 extension + 4 webstore docs.