# Merges the PRs that the reviewer agents approved and whose tests HQ re-ran (2026-10-29).
# The safety classifier blocks agents from merging, so you run this once: pwsh -NoProfile -File D:\Projects\_SIR\scripts\merge-approved-prs.ps1
$prs = @(
  @{ repo = 'sirahmed8/merged-sites';        n = 1 },   # payment webhook signature (29/29 tests)
  @{ repo = 'sirahmed8/SIR-Controller';      n = 1 },   # webhook signature + Gemini key header (21/21)
  @{ repo = 'sirahmed8/sir-mods-for-gta-v';  n = 1 }    # server-verified admin session (10/10)
)
foreach ($p in $prs) {
  gh pr ready $p.n --repo $p.repo
  gh pr merge $p.n --repo $p.repo --merge
  '{0}#{1}: {2}' -f $p.repo, $p.n, (gh pr view $p.n --repo $p.repo --json state -q .state)
}
# sir-optimizer#1 and SIR-AI#1 are NOT in this list: they need the reviewer's fixes first (HQ is applying them).
