$root = 'D:\Projects'
$L = "$root\SIR Controller\legacy\SIR Optimizer"
$realW = "$L\AI_Models_Hub\whisper"
if (Test-Path $realW) {
  Move-Item $realW "$root\AI_Models_Hub\_whisper_duplicate_from_restore"
  'duplicate whisper cache parked in AI_Models_Hub (same model as the complete one in whisper\; delete it when you like)'
}
if ((Test-Path "$L\AI_Models_Hub") -and -not (Get-ChildItem "$L\AI_Models_Hub" -Force)) { Remove-Item "$L\AI_Models_Hub" -Force; 'removed empty leftover folder' }
if ((Test-Path $L) -and -not (Get-ChildItem $L -Force) -and (Test-Path "$root\SIR Controller\legacy\_opt_real")) {
  Remove-Item $L -Force
  Move-Item "$root\SIR Controller\legacy\_opt_real" $L
  'SIR Optimizer is in place'
} else { 'outer folder still has: ' + ((Get-ChildItem $L -Force -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Name) -join ', ') }
'legacy now: ' + ((Get-ChildItem "$root\SIR Controller\legacy" -Force | Select-Object -ExpandProperty Name) -join '; ')
'optimizer is a git repo: ' + (Test-Path "$L\.git")
