# plain-writing

Tools: gemini-plugin (mobbin plugin). Source: C:\Users\a7med\.gemini\config\plugins\mobbin\skills\plain-writing\SKILL.md (218 lines, read in full)

## Summary
A prose-quality pass that Mobbin skills run on their own output before returning it to the user — a detailed anti-AI-writing rulebook for design work: no em/en dashes, no invented facts, fixed section shapes for options answers, banned vocabulary lists, before/after examples, and explicit "what not to strip" exceptions. It rewrites words, never structure, facts, links, or code spans.

## When to use / not use
Applies automatically inside Mobbin skills (redesign-screen etc.) whenever they produce readable prose. Outside a Mobbin skill it explicitly does not apply — it is scoped to that plugin family's reports, options lists, briefs, and whys.

## Inputs, outputs, dependencies
Input: draft prose produced by a calling Mobbin skill. Output: the same content rewritten plainly — returned alone, no draft/audit/note that a pass happened. Needs: nothing external; it is a self-edit checklist.

## Key rules
1. Three outranking rules: zero em/en dashes in prose (mechanical scan), invent nothing, keep exactly what the caller asked for (sections, order, labels).
2. Voice: senior designer leaving crit notes — name the concrete thing, allow abstractions only when tied to a screen part, opinions open with "My opinion is to", never say "the run/the skill", no manufactured warmth.
3. Options answers get a fixed shape: bold name → one-sentence description → References line → optional Downside/Also/My-opinion → optional "Not confirmed:" line last; ~30 words per option.
4. Large banned-tell list: made-up product reasons, name-dropping, vague authorities, AI vocabulary (delve, seamless, pivotal...), "-ing" tails, "serves as", synonym cycling, hedging, aphorisms, chatbot ceremony, scattered bold.
5. Protect the real: precise design terms (auto layout, token, bottom sheet), secondhand text (on-screen copy keeps its exact form), one emphatic sentence, natural sentence-length variety.

## Risks / owner items
- Provenance: adapted from the `humanizer` skill / Wikipedia "Signs of AI writing" — the dash rule here has NO pasted-text exception, stricter than upstream.
- Over-application risk: it's a rewrite pass, so a lazy application could flatten legitimate voice; the "what not to strip" section exists precisely to prevent that.
- Only governs Mobbin plugin outputs — Ahmed's other products need equivalent rules elsewhere (his own CLAUDE.md covers similar ground).

## Category and tags
design, ops — writing, anti-ai-slop, copy-editing, mobbin, style-guide.

## Revision note
Single plugin revision; the most detailed prose-style skill in the slice.
