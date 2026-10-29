<#
 Restores items that a faulty merge step (2026-10-30) moved from D:\Projects into SIR Controller\legacy\SIR Optimizer.
 Never overwrites: if a destination already exists the item is left where it is and reported.
#>
$ErrorActionPreference = 'Continue'
$root = 'D:\Projects'
$L = "$root\SIR Controller\legacy\SIR Optimizer"
function MoveSafe($src, $dst) {
  if (-not (Test-Path -LiteralPath $src)) { "missing source: $src"; return }
  if (Test-Path -LiteralPath $dst) { "CONFLICT (kept both): $dst"; return }
  try { Move-Item -LiteralPath $src -Destination $dst -ErrorAction Stop; "restored: $dst" } catch { "FAILED: $src -> $dst : $($_.Exception.Message)" }
}
"== workspace files back to D:\Projects"
foreach ($n in 'AGENTS.md', 'CLAUDE.md', 'GEMINI.md', 'START_HERE.md', 'SIR-Mission.zip', '.agents', '.remember') { MoveSafe "$L\$n" "$root\$n" }

"== Jobs -> SIR Jobs\legacy\Jobs"
New-Item -ItemType Directory -Force "$root\SIR Jobs\legacy" | Out-Null
MoveSafe "$L\Jobs" "$root\SIR Jobs\legacy\Jobs"

"== Laptop manager (split in two places) -> SIR Laptop Manager\legacy\Laptop manager"
New-Item -ItemType Directory -Force "$root\SIR Laptop Manager\legacy" | Out-Null
$lm = "$root\SIR Laptop Manager\legacy\Laptop manager"
MoveSafe "$L\Laptop manager" $lm
if (Test-Path "$root\Laptop manager") {
  Get-ChildItem "$root\Laptop manager" -Force | ForEach-Object { MoveSafe $_.FullName "$lm\$($_.Name)" }
  if (-not (Get-ChildItem "$root\Laptop manager" -Force)) { Remove-Item "$root\Laptop manager" -Force; 'removed the now-empty top-level Laptop manager' }
}

"== AI_Models_Hub (split in two places) -> stays at D:\Projects\AI_Models_Hub"
if (Test-Path "$L\AI_Models_Hub") {
  Get-ChildItem "$L\AI_Models_Hub" -Force | ForEach-Object { MoveSafe $_.FullName "$root\AI_Models_Hub\$($_.Name)" }
  if (-not (Get-ChildItem "$L\AI_Models_Hub" -Force)) { Remove-Item "$L\AI_Models_Hub" -Force }
}

"== the real SIR Optimizer is nested one level too deep"
$tmp = "$root\SIR Controller\legacy\_opt_real"
if (Test-Path "$L\SIR Optimizer") {
  MoveSafe "$L\SIR Optimizer" $tmp
  $left = Get-ChildItem $L -Force
  if (-not $left) { Remove-Item $L -Force; Move-Item $tmp $L; 'SIR Optimizer is in place' } else { "left over inside outer folder: " + (($left | Select-Object -ExpandProperty Name) -join ', ') }
}
"== result"
"top-level: " + ((Get-ChildItem $root -Force | Select-Object -ExpandProperty Name) -join '; ')
