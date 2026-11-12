# brand-check

- Tool: `gemini-plugin` (plugin: `canva`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\canva\skills\brand-check\SKILL.md`
- SKILL.md size: 5099 chars

## What it does

Check a Canva design against a brand kit and report where it diverges — off-palette colors, non-brand fonts, logo misuse, and off-tone copy. Read-only; makes no changes. Use when the user asks "is this on brand", "check this against our brand kit", "do a brand review", "does this match our brand guidelines", or "brand-check my design".

## Structure (headings inside SKILL.md)

- Brand Checker
- The brand-kit data gap — read this first
- Reading the design's actual colors and fonts
- Workflow
- Step 1: Resolve the design
- Step 2: Get the brand kit
- Step 3: Read the design
- Step 4: Compare against the brand
- Step 5: Report
- Brand check — "<design title>" vs "<brand kit name>"
- Off brand
- Can't verify (need input)
- On brand
- Step 6: Offer to fix
- Rules
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Apply the data-gap handling above. If scopes are missing (e.g. "Missing scopes: [brandkit:read]"), tell the user to disconnect and reconnect the Canva connector to refresh the token.

## Key rules (verbatim lines from SKILL.md)

1. - A **read-only** editing transaction (`Canva:start-editing-transaction` → inspect → `Canva:cancel-editing-transaction`, always cancel) reliably gives element **text, positions, and sizes**.
2. - **Colors and fonts are NOT reliably exposed** by the transaction — tested: it often returns only text + position + dimension, with no color/font attributes. So the **thumbnail is your primary evidence** for color and typography. Use any style data the payload happens to include, but never assert a
3. - Read-only: always `cancel-editing-transaction` after inspecting. Never commit.
4. - Never fabricate brand values — use the kit's real data or what the user provides, otherwise mark **Can't verify**.
5. - Always name the specific page/element and the offending value vs. the brand value.

## Files inside the skill

- (SKILL.md only)
