# claude-council

## Summary
A "Shark Tank" style advisory ritual: the same question is put to four persona seats — Visionary (growth vectors, timing), Skeptic (blind spots, failure modes), Investor (monetization, unit economics, CAC/LTV) and Chief Justice (synthesizes a decisive Go/No-Go verdict plus a 48-hour de-risking plan). It is used to vet startup ideas and architectural pivots before committing resources.

## When to use / when NOT
Use before big bets: new product direction, pricing model, architecture pivot, launch decision. Do NOT use for routine implementation choices, small bug fixes, or as a substitute for actually testing assumptions — it is advisory, not execution.

## Inputs, outputs, tools
- Inputs: the idea or decision under review, plus any context (market, constraints, current numbers).
- Outputs: four seat opinions and a final verdict with a concrete de-risking plan.
- Tools: none external — it is a structured reasoning protocol the agent performs itself; may optionally use subagents per seat.

## 5 most important rules
1. All four seats must argue in character; skipping a seat defeats the adversarial purpose.
2. The Skeptic must attack real failure modes, not strawmen — name the actual way this dies.
3. The Investor seat quantifies: CAC, LTV, margins, payback — no vague "it could make money".
4. The Chief Justice ends with an explicit Go/No-Go, not "it depends".
5. Every verdict ships with a 48-hour de-risking plan — cheapest test that could kill or confirm the idea.

## Risks / things needing the owner
Verdicts are opinion-shaped; the council can rationalize a favored idea. Owner should treat Go as "worth testing", not "approved to build". No external data is fetched — market claims stay unverified unless the agent researches them.

## Category / tags
ai · decision-making, review, multi-perspective, advisory

## Revisions
Six tools hold it. The claude copy (`C:\Users\a7med\.claude\skills\claude-council\SKILL.md`, 2274 chars) is preferred per brief ordering; codex/cursor/kilo/opencode/windsurf copies are 2236 chars and byte-near-identical — the claude revision carries slightly more frontmatter/description text. Content of the protocol is the same across copies.
