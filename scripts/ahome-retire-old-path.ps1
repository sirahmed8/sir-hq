<#
.SYNOPSIS
  Phase 2.2: make D:\Projects\AHome the real folder and retire the old name AhmedAndHabiba.

.DESCRIPTION
  Today AHome is a junction to AhmedAndHabiba. This script:
    1. checks the zip backup exists and the junction is intact
    2. stops the AHome python daemons (the only processes that hold the old path)
    3. removes the junction (rmdir, never recursive) and renames the folder to AHome
       (if the rename fails, the junction is restored and the stack is restarted from the old path)
    4. rewrites the old path inside infra-daemons scripts and the Startup shortcut
    5. commits the path change on a branch (never main)
    6. starts the stack through the supervisor and checks port 8090 and each daemon

  Run it from a normal PowerShell window:  pwsh -NoProfile -File D:\Projects\_SIR\scripts\ahome-retire-old-path.ps1
  Add -WhatIf to see the steps without changing anything.
#>
[CmdletBinding(SupportsShouldProcess)]
param(
    [string]$Backup = 'D:\Backups\AHome-2026-10-29\AhmedAndHabiba-before-rename.zip'
)

$ErrorActionPreference = 'Stop'
$old = 'D:\Projects\AhmedAndHabiba'
$new = 'D:\Projects\AHome'
$startup = Join-Path $env:APPDATA 'Microsoft\Windows\Start Menu\Programs\Startup\OurSanctuary Daemon Stack.lnk'
$files = 'ahome-service-supervisor.ps1', 'jarvis_agy_bridge.py', 'launch_sanctuary_stack.vbs', 'launch_silent_core.vbs', 'register-startup-daemons.ps1'

function Start-Stack([string]$root) {
    Start-Process wscript.exe -ArgumentList ('"{0}\infra-daemons\launch_sanctuary_stack.vbs"' -f $root) -WindowStyle Hidden
}

if (-not (Test-Path -LiteralPath $Backup)) { throw "Backup not found: $Backup" }
$link = Get-Item -LiteralPath $new -Force
if ($link.LinkType -ne 'Junction') { throw "$new is not a junction. Nothing to do or already migrated." }
if (-not (Test-Path -LiteralPath $old)) { throw "$old does not exist." }
Set-Location 'D:\Projects'

# 1. stop daemons
$procs = Get-CimInstance Win32_Process -Filter "Name='python.exe'" | Where-Object { $_.CommandLine -like '*AhmedAndHabiba*' }
Write-Output ("Stopping {0} process(es) that hold the old path" -f @($procs).Count)
if ($PSCmdlet.ShouldProcess('AHome daemons', 'stop')) {
    $procs | ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
    Start-Sleep -Seconds 2
}

# 2. swap junction for the real folder
if ($PSCmdlet.ShouldProcess("$old -> $new", 'rename')) {
    cmd /c rmdir "$new"
    try {
        Rename-Item -LiteralPath $old -NewName 'AHome'
    } catch {
        Write-Output ("Rename failed: {0}. Restoring the junction and restarting from the old path." -f $_.Exception.Message)
        cmd /c mklink /J "$new" "$old" | Out-Null
        Start-Stack $old
        exit 1
    }
    Write-Output 'Renamed AhmedAndHabiba -> AHome'
}

# 3. rewrite old path references
foreach ($f in $files) {
    $p = Join-Path $new "infra-daemons\$f"
    if (-not (Test-Path -LiteralPath $p)) { continue }
    $text = [IO.File]::ReadAllText($p)
    $fixed = $text.Replace('D:\Projects\AhmedAndHabiba', 'D:\Projects\AHome').Replace('D:/Projects/AhmedAndHabiba', 'D:/Projects/AHome')
    if ($fixed -ne $text -and $PSCmdlet.ShouldProcess($p, 'rewrite path')) {
        [IO.File]::WriteAllText($p, $fixed, (New-Object Text.UTF8Encoding($false)))
        Write-Output "Updated $f"
    }
}
if (Test-Path -LiteralPath $startup) {
    $lnk = (New-Object -ComObject WScript.Shell).CreateShortcut($startup)
    $lnk.WorkingDirectory = 'D:\Projects\AHome\infra-daemons'
    if ($PSCmdlet.ShouldProcess($startup, 'set working directory')) { $lnk.Save(); Write-Output 'Updated Startup shortcut' }
}

# 4. commit on the branch (never main)
if ($PSCmdlet.ShouldProcess($new, 'git commit')) {
    git -C $new add infra-daemons
    git -C $new commit -m "Point daemon scripts at D:\Projects\AHome

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
}

# 5. start and verify
if ($PSCmdlet.ShouldProcess('AHome stack', 'start and verify')) {
    Start-Stack $new
    Start-Sleep -Seconds 25
    $port = [bool](Get-NetTCPConnection -LocalPort 8090 -State Listen -ErrorAction SilentlyContinue)
    Write-Output ("Port 8090 (local core): {0}" -f $(if ($port) { 'listening' } else { 'NOT listening' }))
    foreach ($n in 'telegram_gateway_bot.py', 'firebase_bridge.py', 'web_push_delivery.py') {
        $up = Get-CimInstance Win32_Process -Filter "Name='python.exe'" | Where-Object { $_.CommandLine -like "*$n*" }
        Write-Output ("{0}: {1}" -f $n, $(if ($up) { 'running' } else { 'not running (check local-vault\logs, and whether its token is set)' }))
    }
    if (-not $port) { exit 2 }
}
Write-Output ("Done. Old name retired; backup is at {0}" -f $Backup)
