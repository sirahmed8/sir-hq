# ponytail-yagni-optimizer

- Tool: `gemini-plugin` (plugin: `advanced-engineering`)
- Category: ops
- Source: `C:\Users\a7med\.gemini\config\plugins\advanced-engineering\skills\ponytail-yagni-optimizer\SKILL.md`
- SKILL.md size: 1971 chars

## What it does

YAGNI minimalist engineering to cut code.

## Structure (headings inside SKILL.md)

- Ponytail YAGNI Optimizer (Senior Minimalist Engineering)
- 1. The YAGNI Question Ladder
- 2. Token-Saving & Anti-Bloat Substitutions
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - CSS `:has()`, Container Queries, and `dialog` element replace heavy JS modal/dropdown managers.

## Key rules (verbatim lines from SKILL.md)

1. - **Native Fetch instead of Axios**: Modern Node 18+ and browsers have `fetch`, `AbortController`, and `FormData` built-in.
2. - **Modern CSS instead of Complex JS Libraries**:
3. - **Native Web Crypto instead of `crypto-js`**: Use `crypto.subtle` for hashing, HMAC, and random UUID generation (`crypto.randomUUID()`).
4. - **Standard Date handling instead of Moment.js**: Use native `Intl.DateTimeFormat` or lightweight `date-fns` functions instead of 70KB Moment.js bundles.
5. - **Surgical Code Generation**: Never generate 300 lines of boilerplate when 40 lines of elegant, readable code fulfill the requirements.

## Files inside the skill

- (SKILL.md only)
