<#
 Organizes the OLD GitHub repos after the new SIR repos exist. Never deletes: it renames to sir-legacy-<name> and archives (read-only, reversible in Settings).
 Skips any repo that still has an open pull request (merge them first: scripts\merge-approved-prs.ps1) and the infrastructure repos.
 Preview: pwsh -NoProfile -File D:\Projects\_SIR\scripts\github-organize.ps1 -WhatIf     Run: same without -WhatIf
#>
[CmdletBinding(SupportsShouldProcess)]
param()
$owner = 'sirahmed8'
# old repo -> new legacy name (merged-away projects)
$retire = [ordered]@{
  '11Players'='sir-legacy-11players'; 'EGFootball5'='sir-legacy-egfootball5'; 'merged-sites'='sir-legacy-hagoozat-elite';
  'restaurant-os'='sir-legacy-restaurant'; 'sir-market'='sir-legacy-market'; 'sir-pharmacy'='sir-legacy-pharmacy'; 'sir-library'='sir-legacy-library';
  'sir-optimizer'='sir-legacy-optimizer'; 'SIR-Controller'='sir-legacy-controller'; 'SIR-AI'='sir-legacy-ai';
  'sir-content-creation-studio'='sir-legacy-content-creation-studio'; 'sir-mods-for-gta-v'='sir-legacy-gta-mods'; 'SIR-ModPack-private'='sir-legacy-modpack-private';
  'obour-academic-hub'='sir-legacy-obour-hub'; 'negm-furniture-eg'='sir-legacy-negm-furniture'; 'odysseus'='sir-legacy-odysseus';
  'antigravity-agent-suite'='sir-legacy-agent-suite'; 'sir-tele-gateway'='sir-legacy-tele-gateway'
}
# NOT touched now: laptop-manager (runs routines until SIR Laptop Manager replaces it), ahmed-and-habiba-sanctuary (AHome runs from it),
# sirahmed8 (profile), sir-hq, sir-backups, the SIR-*-Public release repos (download links; archive each when its new product ships), SIR-ModPack (public release).
foreach ($old in $retire.Keys) {
  $new = $retire[$old]
  $open = gh pr list --repo "$owner/$old" --state open --json number -q 'length' 2>$null
  if ($LASTEXITCODE -ne 0) { "skip (not found): $old"; continue }
  if ([int]$open -gt 0) { "skip (open PR, merge first): $old"; continue }
  if ($PSCmdlet.ShouldProcess("$owner/$old", "rename to $new and archive")) {
    gh repo rename $new --repo "$owner/$old" --yes 2>&1 | Select-Object -Last 1
    gh repo archive "$owner/$new" --yes 2>&1 | Select-Object -Last 1
    "archived: $old -> $new"
  }
}
