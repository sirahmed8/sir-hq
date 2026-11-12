# base44-sdk

Source read: `C:\Users\a7med\.gemini\config\plugins\base44\skills\base44--base44-sdk.md` (gemini-plugin revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A software development kit skill for Base44 encoding/decoding in application code. It provides language-specific functions for Base44 encode and decode operations in JavaScript/TypeScript, Python, and Go. The SDK handles the 44-character alphabet, padding, and error handling, and can be used for embedding binary data in JSON, URLs, or other text-based protocols.

## When to use / when NOT
Use when your application needs to encode/decode Base44 data programmatically — the SDK handles the low-level details so you can focus on business logic. Do NOT use if you need maximum compatibility — Base64 is more universally supported across legacy systems and platforms. Do NOT skip the input validation step — the SDK will throw errors for inputs containing characters outside the 44-character alphabet; handle these gracefully in your application.

## Inputs, outputs, tools
- Inputs: data string or buffer, operation (encode, decode), optional custom alphabet (rare).
- Outputs: encoded text string or decoded binary data, operation status, error messages for invalid input.
- Tools: base44 SDK (npm package for JS/TS, pip package for Python, Go standard library integration), language runtime. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always validate decoded data** — the SDK may produce corrupted output if the input was not properly encoded; verify the round-trip encode-decode cycle.
2. **Handle alphabet boundary cases** — the 44-character alphabet excludes `+`, `/`, `=`; if your data contains these, the SDK will encode them differently than Base64; document this behavior for downstream consumers.
3. **Use the SDK's built-in error handling** — do not attempt manual Base44 implementation; the SDK has been tested for edge cases including empty strings, null values, and maximum-size inputs.
4. **Cache encoded results for repeated use** — the SDK does not include caching; if you're encoding the same data multiple times, implement a simple cache to avoid redundant computation.
5. **Test with your specific language's edge cases** — JavaScript's string handling may differ from Python's bytes handling; the SDK abstracts these differences but testing is still recommended.

## Risks / owner notes
The most common issue is silently ignoring encode/decode errors — the SDK throws specific errors for invalid input; these should be caught and handled gracefully, not ignored. Downstream systems that expect Base64 may not handle Base44 output correctly; verify compatibility before widespread adoption.

## Category / tags
development · sdk, base44, encoding, python, javascript, go, data-formats

## Revisions
The gemini-plugin copy is the only revision available; no codex, kilo, or cursor copies exist. This is the canonical source for this skill.