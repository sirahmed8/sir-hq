# 17 — Engineering playbook: how top companies build, adapted to a small studio

**Before building**

- **Design doc** (Google practice) for every new product or large feature: context, goals and non-goals, design, alternatives considered, risks, metrics, rollout plan. One to three pages, reviewed by the `reviewer` agent before any code.
- **Working backwards** (Amazon): write the launch announcement and FAQ first (`docs/PRFAQ.md`): who it's for, the problem, why it's better, what it costs. If the announcement isn't compelling, don't build yet.
- **Threat model at design time** (Microsoft Security Development Lifecycle): walk the data flows with STRIDE; write the security requirements into the spec.

**Writing and reviewing code**

- **Code review (Google's published guidelines):**
  - Approve a change once it definitely improves overall code health, even if it isn't perfect.
  - Review design first, then functionality, complexity, tests, naming, comments, style and docs.
  - Keep changes small and self-contained: around 100 lines is reasonable; 1,000 is almost always too big. Separate refactors from behavior changes.
  - Description: a short imperative first line, then what changed and why.
  - Technical facts beat opinions.
- **Tests:** if you'd be upset to see something break, it needs a test (Google's "Beyoncé rule"). Prefer small, fast, hermetic tests and few large ones. Flaky tests are bugs.
- **Hyrum's law:** with enough users, every observable behavior gets depended on. Treat public APIs, data shapes and URLs as contracts. Change them through versioning and deprecation, never silently.
- **API design** (Google's API guidelines, Stripe): resource-oriented, consistent names, cursor pagination, idempotency keys on every mutation, structured error codes and messages, versioning, documentation people enjoy reading.
- **One version policy:** one version of each dependency across the monorepo. Upgrades land everywhere at once through HQ codemods.

**Shipping**

- **Trunk-based development** with short-lived branches.
- **Feature flags** (Remote Config) to ship dark and turn on gradually.
- **Progressive delivery:** internal → beta → staged percentage rollout → 100%, halted automatically on error spikes. Fast rollback is a feature.
- **Launch checklist** (SRE style) for every release: monitoring and alerts in place, rollback tested, capacity and cost checked, security review done, legal and store items done, support ready, docs and changelog updated.

**Running in production**

- **SLOs** (Google SRE): every live product defines indicators and objectives, for example ≥ 99.5% successful requests, p95 latency ≤ 500 ms on core API calls, ≥ 99.5% crash-free sessions. The **error budget** sets priorities: once it's spent, reliability work comes before features.
- **Blameless postmortems** for every incident: timeline, impact, root causes, what went well, action items with owners. Stored in `docs/postmortems/`.
- **Eliminate toil:** anything done by hand twice gets automated (skills, scripts, n8n).
- **Observability:** structured logs, metrics and traces; a dashboard per product; alerts only on user-visible symptoms (SLO burn), sent to Ahmed's phone sparingly.
- **DORA metrics** per project in the Command Center: deployment frequency, lead time for changes, change failure rate, time to restore service.
- **Quarterly architecture review** of each flagship against the AWS Well-Architected pillars: operational excellence, security, reliability, performance efficiency, cost optimization, sustainability.

**Product and design**

- **Apple-level polish:** follow the Human Interface Guidelines and Material guidelines. Do a polish pass before every release: alignment, spacing, motion timing, copy, empty states, edge cases, accessibility, dark mode, every locale. Privacy is a feature. Consistency across the family.
- **Data-informed, privacy-first:** define the success metric before building. A/B test meaningful changes through Remote Config. Guardrail metrics (crashes, retention) can veto a "win". Never trade user trust for a metric.
- **Writing culture** (Amazon, Stripe): decisions are short written narratives (ADRs, design docs); the README quickstart runs in under 5 minutes; docs change in the same commit as the code.
