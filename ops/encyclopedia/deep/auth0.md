# auth0

**Source:** `C:\Users\a7med\.gemini\antigravity\cache\marketplaces\antigravity-plugins-partners\plugins\auth0\2.8.0\skills\auth0\SKILL.md` (newest revision; installed config copy is 2.6.0) plus the `references/` tree
**Category:** security
**Tags:** auth0, authentication, mfa, passkeys, organizations, sso, audit, nextjs, multi-framework

## Summary
A large, intent-routing Auth0 skill (official Auth0 agent skill) that detects what the developer wants (login integration, MFA, passkeys, Organizations, Enterprise Connect, Universal Portals, custom domains, ACUL, branding, DPoP, token exchange, Token Vault, tenant audit, health check, debugging, migration, SDK upgrade, CLI tooling), detects the framework from workspace dependencies, detects the tooling (CLI, MCP, Terraform or Vercel), and then loads two or three targeted reference files from a tree of about 140 files. The SKILL.md is a routing table; the real content lives in the per-intent and per-framework references.

## When to use / when not to
Use it for any Auth0 work across more than twenty frameworks, especially when the request is ambiguous or spans features such as MFA, SSO, Organizations, custom domains, tenant audit or health check. Do not use it for non-Auth0 providers (use `auth` for Clerk, Descope and Better Auth), or when the framework and tooling are already obvious and a single framework reference would suffice.

## Inputs, outputs, tools
Inputs: the developer's request, the project's dependency files (package.json, requirements.txt, build.gradle, .csproj, composer.json, go.mod, pubspec.yaml, Package.swift) and tooling signals. Outputs: framework- and intent-specific integration code, tenant configuration steps, audit and health-check reports, and debugging fixes. Tools: the Auth0 CLI (`auth0`, v1.37.0 or newer with agent mode), optionally the Auth0 MCP server, Terraform, or the Vercel Marketplace integration.

## Five most important rules
1. Follow the four-step order: detect intent, detect framework, detect tooling, then load only the reference files the matching intent section lists.
2. Stop at the first framework tier that matches; workspace signals outrank the prompt, and material conflicts are stated and asked rather than silently resolved.
3. For MFA, enforce in two independent places (the tenant/login flow and the application's own verification); a frontend `amr` check is UX, never security.
4. Trust the per-SDK example files' method and option names; do not grep node_modules, read SDK source, or hand-roll token grants and MFA API URLs.
5. For a tenant audit, apply findings only with per-command confirmation and verify each change by re-fetching it.

## Risks and owner actions
Auth0 tenant and API credentials are needed, and some flows require interactive OAuth or device login, which is an owner action. The reference tree is large, so an incorrect intent pick loads the wrong reference; the routing step is the skill's critical control point.

## Revisions
The installed config copy is version 2.6.0 (20670 bytes, 2026-11-02). The marketplace cache also holds 2.6.0 (20901 bytes) and a newer 2.8.0 (21510 bytes, 2026-11-12) that adds React Router framework detection and a much fuller "when to use" description, plus a `framework-react-router` reference. The 2.8.0 cache copy is the best revision; the installed 2.6.0 copy is functionally the same except for React Router support.
