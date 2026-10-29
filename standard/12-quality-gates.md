# 12 — Quality gates, testing and CI

- **One local gate: `pnpm verify`** = format check, lint (0 warnings), typecheck, unit tests, security-rules tests, locale completeness (no missing keys, placeholders match), build. CI runs the same gate, plus Lighthouse (SEO ≥ 90 as well as the other categories) and structured-data validation on public sites.
- **Test pyramid:**
  - Unit tests on `packages/core` (≥ 85% line coverage).
  - Integration tests against the Firebase emulator and APIs.
  - Component tests for shared UI.
  - E2E for critical journeys: Playwright for web and Electron, Maestro for mobile.
  - Visual regression for shared components (Storybook or Playwright screenshots).
  - Automated accessibility checks (axe, Lighthouse) plus a manual checklist per release.
- **Performance:** Lighthouse CI against the module 06 budgets; bundle-size limits per route and app; mobile startup tracked.
- **Security in CI:** the required security job from module 04 (secrets, static analysis, dependencies, rules tests, and a DAST baseline scan against the preview), all free tools.
- **GitHub Actions:**
  - On every PR: verify, web e2e, the security job, a preview deployment, and a manual trigger for EAS preview builds (to save build credits).
  - On release tags: desktop builds (Windows runner; macOS runner only for releases, since macOS minutes cost the most), EAS production builds, GitHub Release.
  - Required checks plus branch protection on `main` (module 03 explains the GitHub plan requirement for private repos).
- **Pre-commit (lefthook):** lint-staged, typecheck of changed packages, commitlint, gitleaks.
- **PR template:** the DoD checklist, screenshots for UI changes, and the commands run.
- **Quality ratchet:** coverage, performance and accessibility thresholds can only go up. A flaky test is a bug; fix it or quarantine it with a ticket, never delete it to go green.
