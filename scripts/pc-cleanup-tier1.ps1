<#
.SYNOPSIS
  Phase 2.4 Tier 1 cleanup: removes only regenerable caches and build output named in ops/PC_CLEANUP_DRYRUN.md (2026-10-29).

.DESCRIPTION
  Removes: npm _cacache, NuGet v3-cache, dead Temp folders, node_modules of the retired SIR Tele Gateway,
  and the .next build output of projects with no dev server running. Personal files are never touched.
  It does NOT touch npm-cache\_npx (running MCP servers load from it), WinGet staging, C:\Windows, the Recycle Bin,
  duplicates, game folders or Antigravity history.

  Preview:  pwsh -NoProfile -File D:\Projects\_SIR\scripts\pc-cleanup-tier1.ps1 -WhatIf
  Run:      pwsh -NoProfile -File D:\Projects\_SIR\scripts\pc-cleanup-tier1.ps1
  Close every `next dev` server first. Expected: about 1.5 GB (caches and temp) plus up to 3.2 GB (.next folders).
#>
[CmdletBinding(SupportsShouldProcess)]
param()
$ErrorActionPreference = 'Continue'

function SizeGB($p) {
    if (-not (Test-Path -LiteralPath $p)) { return 0 }
    $s = (Get-ChildItem -LiteralPath $p -Recurse -Force -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum
    [math]::Round($s / 1GB, 3)
}
function Free($d) { [math]::Round((Get-PSDrive $d).Free / 1GB, 2) }

$devServers = Get-CimInstance Win32_Process -Filter "Name='node.exe'" | Where-Object { $_.CommandLine -match 'next(\.js)?[\\/ ]+(dev|start)|next dev' }
if ($devServers) { throw 'A Next.js server is running. Stop it first, then run this again.' }

$before = @{ C = Free 'C'; D = Free 'D' }
$targets = @(
    "$env:LOCALAPPDATA\npm-cache\_cacache",
    "$env:LOCALAPPDATA\NuGet\v3-cache",
    "$env:LOCALAPPDATA\Temp\test-mcp",
    "$env:LOCALAPPDATA\Temp\tmp1t_jbj_x", "$env:LOCALAPPDATA\Temp\tmpat0hx40f", "$env:LOCALAPPDATA\Temp\tmpc2qny41w",
    "$env:LOCALAPPDATA\Temp\tmpcne6kowp", "$env:LOCALAPPDATA\Temp\tmpeg8ef2tt", "$env:LOCALAPPDATA\Temp\tmpk4e9mko7", "$env:LOCALAPPDATA\Temp\tmpymyvylml",
    'D:\Projects\old projects\SIR Tele Gateway\node_modules',
    'D:\Projects\Obour Academic Hub\.next',
    'D:\Projects\11Players\.next',
    'D:\Projects\AHome\apps\web\.next',
    'D:\Projects\AhmedAndHabiba\apps\web\.next',
    'D:\Projects\EGFootball5\.next',
    'D:\Projects\Negm Furniture\.next',
    'D:\Projects\SIR Optimizer\PulseTools-Web\.next',
    'D:\Projects\SIR ModPack\website-next\.next',
    'D:\Projects\Merged sites\.next',
    'D:\Projects\SIR Mods for GTA V\web-portal\.next',
    'D:\Projects\SIR Controller\web\.next'
)
$log = foreach ($t in $targets) {
    if (-not (Test-Path -LiteralPath $t)) { continue }
    # While AHome is still a junction to AhmedAndHabiba, count that folder once (via its real name)
    if ($t -like 'D:\Projects\AHome\*' -and (Get-Item -LiteralPath 'D:\Projects\AHome' -Force).LinkType) { continue }
    if ((Get-Item -LiteralPath $t -Force).LinkType) { [pscustomobject]@{ Path = $t; GB = 0; Result = 'skipped (link)' }; continue }
    $sz = SizeGB $t
    if ($PSCmdlet.ShouldProcess($t, "remove ($sz GB)")) {
        try { Remove-Item -LiteralPath $t -Recurse -Force -ErrorAction Stop; $r = 'removed' }
        catch { $r = 'partial: ' + $_.Exception.Message }
    } else { $r = 'would remove' }
    [pscustomobject]@{ Path = $t; GB = $sz; Result = $r }
}
$log | Format-Table -AutoSize -Wrap | Out-String -Width 200
if ($PSCmdlet.ShouldProcess('pip cache', 'purge')) { pip cache purge 2>&1 | Select-Object -Last 1 }
$after = @{ C = Free 'C'; D = Free 'D' }
'Free C: {0} -> {1} GB | D: {2} -> {3} GB' -f $before.C, $after.C, $before.D, $after.D
