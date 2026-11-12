# generate-deck

- Tool: `gemini-plugin` (plugin: `canva`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\canva\inactive-skills\generate-deck\SKILL.md`
- SKILL.md size: 6596 chars

## What it does

Create branded marketing and sales presentation decks with Canva AI using the connected Canva app's list_brand_kits and direct generate-design flow. Use when the user asks to generate, create, draft, or build a Canva sales deck, marketing deck, pitch deck, product deck, or other branded slide presentation; always suggest available brand kits and ask the user to choose before generation. Do not use for Canva Docs, reports, proposals, single-page visual designs, templates, prepare-design-generation, or _prepare_design_generation flows.

## When to use (from skill text)

- Use this skill only for creating new Canva AI presentation drafts through `list_brand_kits`, direct `generate-design`, and create-from-candidate. For editing an existing Canva design, implementing reviewer feedback, translating, resizing, brand-checking, prepare-design-generation, or template-based 

## Structure (headings inside SKILL.md)

- Canva Presentation Builder
- Core Rule
- Deck Focus
- Inputs
- Brand Kit Handling
- Generation Prompt
- Candidate Finalization
- Boundaries
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Purpose: position the brand or product, communicate value, support a campaign, enable sales, pitch an offer, or drive a next step.
- - Market shift -> customer need -> product story -> differentiation -> results -> CTA.
- - Objective: derive the intended commercial outcome, such as generate interest, persuade buyers, pitch a product, enable sales, recap a campaign, or align go-to-market teams.
- - If the user explicitly chooses to continue without a brand kit, keep the deck brand-aware using the supplied company, product, tone, colors, or messaging, without inventing brand rules.

## Key rules (verbatim lines from SKILL.md)

1. - Suggest the available brand kits to the user and ask them to choose one before generation.
2. - Do not auto-select a brand kit, even if only one kit is available or one kit seems obviously relevant.
3. - If `list_brand_kits` reports missing `brandkit:read` scopes, ask the user to disconnect and reconnect the Canva app before continuing.

## Files inside the skill

- (SKILL.md only)
