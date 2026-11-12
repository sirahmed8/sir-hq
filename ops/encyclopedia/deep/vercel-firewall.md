# vercel-firewall (gemini-plugin: vercel)

## Summary
vercel-firewall is expert guidance for Vercel's multi-layer WAF/DDoS platform via the `vercel firewall` CLI: platform-wide automatic DDoS mitigation (free, all plans, L3/L4/L7, unbilled for blocked traffic), custom rules (deny/challenge/log/bypass/rate_limit/redirect matching on ~20 field types incl. ja4_digest, geo, headers), IP blocks, system bypass (Pro/Enterprise, exempts trusted IPs from system mitigations), Attack Mode (emergency challenge-everyone), system mitigations pause/resume, and traffic inspection (`traffic list/inspect`, `alerts`, `persistent-actions`, `bot-management`). Key mechanics: `rules` and `ip-blocks` changes are staged DRAFTS needing `vercel firewall publish --yes`; system-bypass/attack-mode/mitigations apply immediately. vercel.json `routes`+`mitigate` supports only challenge/deny declaratively.

## When to use / when NOT
Use for configuring/blocking/tuning Vercel firewall rules, rate limits, IP blocks, attack response, or reviewing firewall traffic. Do NOT use for application-level auth (that's vercel-connect/auth skills) or for rules needing fields the CLI lacks (use Rate Limiting SDK for custom buckets/sliding windows).

## Inputs, outputs, tools
- Inputs: rule intent (condition JSON + action), IPs/CIDRs, time windows for traffic queries.
- Outputs: staged draft changes + `diff` review; published live rules; JSON traffic reports.
- Tools: `vercel firewall` CLI subcommands (overview, rules, ip-blocks, system-bypass, attack-mode, system-mitigations, traffic, alerts, status), dashboard traffic URL `/<team>/<project>/firewall/traffic?filter=<ruleId>`.

## 5 most important rules
1. STAGED ROLLOUT is mandatory: log everywhere → user reviews dashboard filtered by rule ID → deny in preview only (add `environment=preview` condition) → deny in production. Never skip stages; JA4/UA rules over-match real users badly.
2. Drafts vs immediate: rules/ip-blocks need `publish`; system-bypass/attack-mode/mitigations are immediate. Always `diff` + `inspect` before handing publish to the user — agents must NOT publish themselves.
3. NEVER run agent-blocked commands: `--ai`/wizard rule creation (TTY-only — use --condition/--json), `attack-mode enable`, `system-mitigations pause` — surface them for the user to run.
4. Rate limits: start `log` action at 5-10x expected rate; counters are PER REGION (~Nx effective); scope by method since GET/POST need different limits.
5. Keep bypasses narrow (shared-secret header AND IP/CIDR); `edit --condition` REPLACES all conditions; persistent deny durations survive rule removal.

## Risks / things needing the owner
A loose deny can take down the whole site or SEO crawlers; misconfigured JA4/UA blocks hit entire browser cohorts. Publishing, attack-mode, and mitigation-pausing are explicitly user-triggered — the skill forbids agents from doing them. `vercel login`/linking needs owner auth. High blast radius = high care.

## Category / tags
security · vercel, waf, ddos, rate-limiting, firewall

## Revisions
Single revision read: `C:\Users\a7med\.gemini\config\plugins\cel-plugin\skills\vercel-firewall\SKILL.md` — actual path `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\vercel-firewall\SKILL.md` (310 lines). Gemini-plugin only.
