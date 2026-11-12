# performance-testing

Tools: gemini-plugin (postman plugin). Source: C:\Users\a7med\.gemini\config\plugins\postman\skills\performance-testing\SKILL.md (68 lines) + references/jmeter-import/, references/gatling-import/

## Summary
Guides load-testing and benchmarking APIs with Postman's `postman performance run`: pick the failure mode first (fixed/ramp-up/spike/peak), establish targets and authorization before sending load, choose local vs postman-cloud runners by reachability, set percentile/error thresholds, isolate test data, and honestly report generator vs target limits. Also covers importing JMeter .jmx and Gatling simulations into collections — approximations are marked, never faked.

## When to use / not use
Use for load tests, benchmarks, or migrating JMeter/Gatling plans into Postman. Not for functional API correctness (that's api-testing) or for CI gating design (that's ci-integration, though this feeds it).

## Inputs, outputs, dependencies
Input: an existing Postman collection (auth + assertions) or a JMeter .jmx / Gatling simulation to convert. Output: a performance run with workload, runner, achieved traffic, latency/error metrics, and threshold verdict. Needs: Postman CLI/MCP tools, `postman performance run`, optionally datasets and setup/teardown collections.

## Key rules
1. Choose the failure mode before the profile: fixed=sustained, ramp-up=degradation curve, spike=surges, peak=max sustained.
2. Authorization and blast radius first: resolve VU count, duration, and write-request effects before stressing shared/production services; thresholds evaluate AFTER the run so a failing gate won't stop traffic.
3. Runner choice matters: `local` can bottleneck on your CPU/network; `postman-cloud` offloads generation; `postman-cloud-static-ip` for IP-allowlisted targets. Verify reachability before blaming service capacity.
4. Thresholds like `--pass-if "less_than(p95, 500)"` support avg/p90/p95/p99/error_rate/rps — latency alone looks good when requests fail fast.
5. Import honesty: JMeter think-time/concurrent groups/non-HTTP samplers and Gatling WebSocket/open-model injection are reported as gaps, never silently faked; open-model converts via Little's law with shown arithmetic.

## Risks / owner items
- Load testing production or shared services needs explicit user authorization for that scope — the skill requires resolving missing limits first.
- `--use-mock` baselines overhead only; its numbers cannot establish real backend capacity.
- Write requests under load can corrupt shared data — isolate test data (datasets distribute rows across VUs).

## Category and tags
build, data — postman, load-testing, performance, jmeter, gatling, api.

## Revision note
Single plugin revision; stands out for explicit "report gaps, never fake" import semantics.
