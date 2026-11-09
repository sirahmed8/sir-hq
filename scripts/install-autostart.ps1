<#
.SYNOPSIS
Installs SIR Control Room dashboard server as an autostart background daemon for the current user.
.DESCRIPTION
Registers a Windows Scheduled Task "SIR_ControlRoom_Server" that launches at logon headless via wscript.exe and pythonw.exe.
#>

[CmdletBinding()]
param (
    [switch]$Force,
    [switch]$Start
)

$ErrorActionPreference = "Stop"

$ProjectRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$VbsLauncher = Join-Path $ProjectRoot "scripts\dev-start.vbs"
$TaskName = "SIR_ControlRoom_Server"

if (-not (Test-Path $VbsLauncher)) {
    Write-Error "Launcher script not found at $VbsLauncher"
    exit 1
}

Write-Host "Registering autostart scheduled task for current user: $TaskName"

$Action = New-ScheduledTaskAction -Execute "wscript.exe" -Argument "`"$VbsLauncher`"" -WorkingDirectory "$ProjectRoot"
$Trigger = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Days 0)

$registered = $false
try {
    # Check if task already exists
    $existing = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
    if ($existing) {
        Write-Host "Task $TaskName already exists. Updating..."
        Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    }

    Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Description "SIR Control Room Headless Server Daemon" | Out-Null
    Write-Host "Successfully installed autostart task '$TaskName'."
    $registered = $true
} catch {
    Write-Host "Register-ScheduledTask cmdlet warning: $_. Trying schtasks.exe fallback..."
    $trArg = "wscript.exe `"$VbsLauncher`""
    & schtasks.exe /create /tn $TaskName /tr $trArg /sc onlogon /f
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Successfully installed autostart task '$TaskName' via schtasks.exe."
        $registered = $true
    } else {
        Write-Error "Failed to install scheduled task via both cmdlets and schtasks.exe."
        exit 1
    }
}

if ($Start -or $Force) {
    Write-Host "Starting scheduled task '$TaskName'..."
    Start-ScheduledTask -TaskName $TaskName
    Start-Sleep -Seconds 2
    $state = (Get-ScheduledTask -TaskName $TaskName).State
    Write-Host "Task '$TaskName' state: $state"
} else {
    Write-Host "Task registered. To run now: Start-ScheduledTask -TaskName '$TaskName'"
}
