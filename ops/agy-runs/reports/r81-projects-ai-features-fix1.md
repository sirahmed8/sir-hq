# r81-projects-ai-features-fix1 report
Static export site: browser cannot reach ask.ps1, so brief item 3 applied: AIChat.tsx copy now says it is a search over site facts, not an AI model (welcome text EN/AR, aria-labels, avatars). Keyword matcher unchanged.
Test: 'chat honesty' in tests/portfolio-knowledge.test.ts. npm test: tests 849, pass 849, fail 0. npm run typecheck: content check 0 errors, tsc clean. npm run build: exit 0. No lint script in package.json.
Not done: 390px screenshot (not taken); CI quota-blocked so not watched. The commit also contains the earlier uncommitted r83 AIChat focus/portal edits.
Recommend: add a server runtime before claiming AI.
