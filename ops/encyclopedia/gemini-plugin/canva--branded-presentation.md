# branded-presentation

Source read: `C:\Users\a7med\.gemini\config\plugins\canva\skills\canva--branded-presentation.md` (gemini-plugin revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A presentation design skill that creates brand-compliant slide decks using Canva or similar tools. It applies brand colors, typography, and logo placement rules to produce professional presentations consistent with the organization's visual identity. The skill can generate slide templates, apply master slide styles, and export presentations in multiple formats (PDF, PowerPoint, HTML).

## When to use / when NOT
Use when you need to create a professional slide deck quickly while maintaining brand consistency — the skill handles design details so you can focus on content. Do NOT use for highly technical or data-dense presentations where custom design is required for clarity — the skill's template-focused approach may sacrifice readability for consistency. Do NOT skip the brand style guide upload — the skill requires brand assets (colors, fonts, logo) to apply the correct visual identity; without it, the skill cannot produce on-brand presentations.

## Inputs, outputs, tools
- Inputs: presentation topic or outline, brand style guide, number of slides, export format (PDF, PPTX, HTML).
- Outputs: slide deck with brand-applied styles, master slide configuration, exported file (PDF/PPTX/HTML), presentation notes suggestions.
- Tools: Canva API, design template library, export utilities, file format converters. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always include the brand style guide** — the skill uses it to set colors, fonts, and logo placement; without it, the skill generates generic presentations with no brand identity.
2. **Limit slide count to 15-20 for optimal readability** — the skill can generate more slides, but research shows attention spans decrease after 20 slides; the owner should aim for conciseness.
3. **Use the skill's suggested layout for data-heavy slides** — the skill has built-in chart and graph templates that are both brand-compliant and readable; do not override these with custom designs that may violate contrast rules.
4. **Export to PDF for distribution and PPTX for further editing** — the skill produces both formats; PDF is best for final delivery, PPTX if the team needs to make adjustments later.
5. **Include speaker notes in the export** — the skill can generate outline-style notes for each slide; these are useful for rehearsals and for team members who could not attend.

## Risks / owner notes
Presentations that are too text-heavy may become difficult to read even with the skill's design optimizations. The owner should aim for the 60-30-10 color rule and high-contrast text within the skill's templates. If the brand style guide is outdated, the skill will apply old colors/fonts; always verify the guide is current before generating a presentation.

## Category / tags
presentation · design, brand-consistency, canva, slide-deck, export, visual-communication

## Revisions
The gemini-plugin copy is the only revision available; no codex, kilo, or cursor copies exist. This is the canonical source for this skill.