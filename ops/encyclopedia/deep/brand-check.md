# brand-check

Tools: claude (canva connector). Source: C:\Users\a7med\.gemini\config\plugins\canva\skills\brand-check\SKILL.md (78 lines, read in full)

## Summary
Read-only Canva brand-audit skill: compare a design against a brand kit and report, per dimension, what follows the brand and what drifts. Specialised rubric version of canva-design-feedback; never edits the design. Handles the brand-kit data gap explicitly: kits often expose only IDs/names/thumbnails, not machine-readable hex values or font families, so the check frequently becomes a visual comparison plus user-supplied palette/fonts.

## When to use / not use
Use when the user asks "is this on brand", "check against our brand kit", "do a brand review", or "brand-check my design". NOT for actually fixing the design (use canva-edit-design) or for creating decks (use branded-presentation); also not when no brand kit exists.

## Inputs, outputs, dependencies
Input: a Canva design (short link/URL/raw ID) plus a brand kit. Output: a structured report (Off brand / Can't verify / On brand) per dimension (color, typography, logo, tone & copy, consistency). Needs: Canva connector with brandkit:read scope (reconnect if missing), get-design-thumbnail, read-only editing transaction, get-design-content.

## Key rules
1. Read-only: always cancel-editing-transaction after inspecting; never commit changes.
2. Never invent brand colors/fonts; if the kit lacks machine-readable values, mark findings "Can't verify" and ask the user to paste palette + fonts.
3. Thumbnail is primary evidence for color/typography; transaction reliably gives text + position + size only.
4. Name the specific page/element and the offending value vs. the brand value; distinguish hard violations from soft ones.
5. Offer fixes via canva-edit-design only for API-fixable issues (text color, font size/weight/style) — font family and background colors are manual in Canva.

## Risks / owner items
- Brand kit data gap means results are often approximate; must be explicit about uncertainty.
- Missing scopes ("brandkit:read") require user to disconnect/reconnect Canva connector to refresh token.
- Transaction payload may omit color/font attributes; never assert hex or font as fact unless present.

## Category and tags
canva, brand, audit, read-only — canva, brand-kit, design-review, compliance.

## Revision note
Single skill file, 78 lines, no references. Current through connector behavior documented in SKILL.md.