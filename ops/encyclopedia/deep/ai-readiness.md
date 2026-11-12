# ai-readiness

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\ai-readiness\SKILL.md` (gemini-plugin revision; not found in codex/kilo/cursor/windsurf/opencode or claude skills dirs).

## Summary
A skill that assesses whether a team or project is prepared to integrate AI capabilities into their product or workflow. It evaluates technical readiness (API access, development environment, data labeling), organizational readiness (team expertise, change management processes), and security readiness (data privacy, compliance, access controls). The output is a readiness score with specific gap analysis and recommendations for bridging identified gaps before AI integration begins.

## When to use / when NOT
Use at the start of any AI project to avoid investing in infrastructure or talent that the team cannot effectively utilize. Do NOT skip this assessment — projects that skip ai-readiness often fail to deliver ROI because the team lacks the necessary skills or access. Do NOT use as a one-time checklist; reassess when switching LLM providers, changing data sources, or onboarding new team members.

## Inputs, outputs, tools
- Inputs: team size and expertise matrix, current API subscriptions, data availability and quality, compliance requirements (GDPR, HIPAA, etc.), preferred LLM provider.
- Outputs: readiness score (0-100), gap analysis report (technical, organizational, security), prioritized remediation plan with timeline and budget estimates.
- Tools: internal documentation scanner, API subscription checker, compliance checklist validator, survey/feedback tools. MCP: postman-mcp-server connector for test step management.

## 5 most important rules
1. **API access must be validated before the assessment** — ensure test credits or production keys are available for the chosen LLM provider.
2. **Include at least one team member with LLM experience** in the assessment panel — otherwise the gap analysis will be inaccurate.
3. **Document compliance constraints explicitly** — GDPR, CCPA, or industry-specific regulations can significantly impact AI deployment options.
4. **Prioritize gaps by impact and effort** — focus on fixing high-impact/low-effort gaps first to show quick wins.
5. **Re-assess after remediation** — the initial score is a baseline; re-measure after addressing the top 3 gaps to track progress.

## Risks / owner notes
The skill's accuracy depends on honest self-reporting; teams may overestimate their expertise or underestimate compliance burdens. The owner should validate the assessment results with a short proof-of-concept using the intended LLM provider before committing to full integration.

## Category / tags
assessment · ai-readiness, ai-integration, gap-analysis, compliance, team-expertise, project-planning

## Revisions
The gemini-plugin copy is the only revision available; no codex, claude, or kilo versions exist. This is the canonical source for this skill.