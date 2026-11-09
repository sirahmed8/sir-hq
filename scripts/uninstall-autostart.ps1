<#
.SYNOPSIS
Uninstalls SIR Control Room autostart scheduled task and stops the running process.
#>

[CmdletBinding()]
param ()

$TaskName = "SIR_ControlRoom_Server"

Write-Host "Stopping and removing scheduled task: $TaskName"

try {
    Stop-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
} catch {}

try {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
    Write-Host "Successfully unregistered $TaskName."
} catch {
    & schtasks.exe /delete /tn $TaskName /f 2>$null
    Write-Host "Unregistered via schtasks fallback."
}

# Stop any running serve-control-room python processes
$procs = Get-CimInstance Win32_Process -Filter "CommandLine LIKE '%serve-control-room%'" -ErrorAction SilentlyContinue
foreach ($p in $procs) {
    Write-Host "Stopping process PID $($p.ProcessId)..."
    Stop-Process -Id $p.ProcessId -Force -ErrorAction SilentlyContinue
}
Write-Host "Cleaned up $TaskName."
