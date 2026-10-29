<#
.SYNOPSIS
  Runs the SIR HQ Remote Control server in D:\Projects inside a relaunch loop.
.DESCRIPTION
  Server mode exits after about 10 minutes without network, so this loop restarts it.
  Phone sessions start in D:\Projects (same-dir) and rely on the lock protocol in _SIR/ops/locks.
  Remote Control needs claude.ai login: ANTHROPIC_API_KEY / ANTHROPIC_AUTH_TOKEN must not be set.
  -Once runs a single launch for testing, -DebugLog writes a debug file.
.EXAMPLE
  pwsh -NoProfile -File D:\Projects\_SIR\scripts\rc-hq.ps1
#>
param([switch]$Once, [string]$DebugLog = '')
$ErrorActionPreference = 'Continue'
foreach ($v in 'ANTHROPIC_API_KEY', 'ANTHROPIC_AUTH_TOKEN') {
  if (Test-Path "Env:$v") { Write-Error "$v is set; Remote Control needs the claude.ai login. Unset it first."; exit 2 }
}
Set-Location 'D:\Projects'
$args = @('remote-control', '--name', 'SIR HQ', '--spawn', 'same-dir', '--capacity', '8', '--chrome')
if ($DebugLog) { $args += @('--verbose', '--debug-file', $DebugLog) }
do {
  Write-Output "[$(Get-Date -Format s)] starting claude $($args -join ' ')"
  & claude @args
  Write-Output "[$(Get-Date -Format s)] claude exited with $LASTEXITCODE"
  if ($Once) { break }
  Start-Sleep -Seconds 20
} while ($true)
