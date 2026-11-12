# postman-mcp-server

Tools: gemini-plugin (postman plugin). Source: C:\Users\a7med\.gemini\config\plugins\postman\skills\postman-mcp-server\SKILL.md (65 lines) + references/{setup,search,sync,mock,test,docs,security,learn,mcp-limitations}.md

## Summary
Operating discipline for working through Postman's MCP server: treat exposed tools as the actual surface (not assumed names), search-then-fetch to locate entities, match mutation scope (request-level updates vs whole-collection replacement), preserve spec↔collection source-of-truth direction, and separate editing from publication. Includes a per-task reference router.

## When to use / not use
Use when the task must go through Postman MCP tools — inspecting/changing workspace collections, specs, examples, environments — especially when the local CLI workflow (api-engineer) isn't available. Not for repo edits/Git review where local tools are preferred.

## Inputs, outputs, dependencies
Input: a Postman workspace task plus the connected MCP tool surface. Output: verified resource changes with honest reporting of what the surface could/couldn't do. Needs: Postman MCP connection; `getEnabledTools` to inspect the active toolset; per-task reference docs.

## Key rules
1. Tool availability varies by mode — a name in a reference is not proof it's exposed; call `getEnabledTools` (or host discovery) before diagnosing a missing operation; report limitations instead of assuming.
2. Search previews are insufficient evidence — fetch collection/spec/workspace detail to establish IDs, ownership, content before mutating.
3. Match mutation scope: request-level updates preserve unrelated content; whole-collection replacement needs the complete current object.
4. Sync direction matters: spec→collection generates the interface, collection→spec carries changes back; async acceptance needs a completed task result before claiming sync.
5. Publication is separate from editing — docs/mocks aren't public merely because they exist; apply audience/authorization before publishing or changing shared resources.

## Risks / owner items
- "Tool success alone does not establish" run completion, sync completion, or reachable URLs — verification must check the actual resource state.
- Each exposed tool definition costs context; prefer the smallest toolset covering the task.
- Workspace is a container/access boundary, not a reason to duplicate resources per task.

## Category and tags
build, data — postman, mcp, api, collections, workspace, governance.

## Revision note
Single plugin revision; meta-skill about using the MCP correctly rather than doing API work itself.
