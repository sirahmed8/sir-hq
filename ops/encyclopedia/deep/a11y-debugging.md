# a11y-debugging

Source read: `C:\Users\a7med\.config\kilo\skills\a11y-debugging\SKILL.md` (kilo revision; identical copies in codex/cursor/windsurf/opencode; also in gemini-plugin).

## Summary
An accessibility debugging skill that uses Chrome DevTools to audit semantic HTML, ARIA labels, focus order, keyboard navigation, tap target sizes, and color contrast ratios, ensuring interfaces are perceivable and operable for users with disabilities. It generates reports identifying violations of WCAG success criteria and provides actionable remediation steps.

## When to use / when NOT
Use during UI development, redesigns, or before any public-facing release to catch accessibility blockers early. Do NOT assume the app is accessible just because it "works" — many disabilities require intentional design. Do NOT skip on mobile or touch-screen interfaces, which have additional tap-target and contrast requirements.

## Inputs, outputs, tools
- Inputs: a web page or React Native component tree, ideally in a development environment with DevTools open.
- Outputs: an accessibility audit report (Violations, Warnings, Notices) with element selectors and recommended fixes.
- Tools: Chrome DevTools Accessibility pane, `axe-core` eslint plugin, `react-aria` hooks for React, `nodeca/accessibility` for native apps. MCP: chrome-devtools connector.

## 5 most important rules
1. **Color contrast must meet WCAG AA**: No text less than 4.5:1 against background (3:1 for large text).
2. **All interactive elements have a minimum 44x44 px tap target** on mobile; ensure spacing around small targets.
3. **ARIA labels are provided for custom controls** without visible text; use `aria-label` or `aria-labelledby`, never leave empty.
4. **Focus order is logical and keyboard-navigable**: Tab sequence should match visual flow; do not trap focus unless in a modal.
5. **Images have meaningful alt text**: Decorative images should have `alt=""`; informative images must describe their content.

## Risks / owner notes
Running automated a11y scans without manual review can produce false positives (e.g., focusing on low-contrast text that is intentional for branding). Owner must review each report and decide on trade-offs. Accessibility is a legal requirement in many jurisdictions; shipping without an audit can expose the product to litigation.

## Category / tags
accessibility · a11y, wcag, frontend, testing, chrome-devtools, inclusive-design

## Revisions
The kilo, codex, cursor, and windsurf copies are byte-identical (identical SKILL.md). The gemini-plugin version includes an additional `axe-core` configuration line. The kilo revision is the canonical source; all tool digests should use it as the base.