# brand-check

Source read: `C:\Users\a7med\.gemini\config\plugins\canva\skills\canva--brand-check.md` (gemini-plugin revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A brand compliance skill that validates visual assets against a brand style guide. It checks color usage, typography, logo placement, iconography, and imagery style to ensure consistency across all marketing and product materials. The skill can scan designs, generate compliance reports, and suggest corrections for brand violations.

## When to use / when NOT
Use before releasing any public-facing design — the skill will catch brand inconsistencies that could confuse customers or dilute brand identity. Do NOT skip the style guide upload step — the skill requires a brand style guide (colors, fonts, logo specifications) to validate against; without it, the skill cannot produce meaningful results. Do NOT rely on the skill's automated suggestions alone — the owner must review each flagged issue and decide on the appropriate correction.

## Inputs, outputs, tools
- Inputs: design file (PNG, JPG, SVG), brand style guide (JSON or Figma file), taget audience (optional).
- Outputs: compliance report ( violations with descriptions, severity scores), corrected asset recommendations, brand consistency score (0-100).
- Tools: image analysis API, color Thief for palette extraction, typography detection, Figma API. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always upload the complete brand style guide** — the skill checks colors against specified hex values, typography against approved font families, and logo usage against clearspace requirements; incomplete guides produce incomplete results.
2. **Set the compliance threshold appropriately** — the skill produces a 0-100 consistency score; the owner can set what score is acceptable for release (e.g., 90+ for public marketing, 80+ for internal documents).
3. **Review all high-severity flags manually** — the skill auto-flags logo distortion, color shifts, and incorrect typefaces; each must be reviewed and approved or corrected by the owner.
4. **Test with diverse asset types** — the skill can check social media graphics, website headers, product photos, and email templates; run the skill on each type to ensure consistent brand representation.
5. **Save compliance reports for audit trails** — the skill writes reports to a persistent location; do not delete these as they may be needed for brand audits or marketing reviews.

## Risks / owner notes
The skill's image analysis may not capture subtle brand issues that a human designer would notice (e.g., gradient nuances, hand-drawn icon style variations). The owner should use the skill as a first pass and then do a visual review of flagged items. Brand consistency scores below the threshold may still be acceptable in certain contexts (e.g., regional variations, seasonal campaigns); the owner should define these exceptions explicitly.

## Category / tags
brand · compliance, style-guide, design-review, visual-assets, marketing

## Revisions
The gemini-plugin copy is the only revision available; no codex, kilo, or cursor copies exist. This is the canonical source for this skill.