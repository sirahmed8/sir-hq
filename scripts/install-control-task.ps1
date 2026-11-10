# Install/update SIR Control Room server scheduled task (5-min repeat, hidden)
$ErrorActionPreference = "Stop"
$taskName = "SIR_ControlRoom_Server"
$action = New-ScheduledTaskAction -Execute "wscript.exe" -Argument "//B //Nologo `"D:\Projects\_SIR\scripts\dev-start.vbs`"" -WorkingDirectory "D:\Projects\_SIR"
$triggerLogon = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
# 5-minute repeat for 365 days (re-armed on logon/re-register)
$triggerRepeat = New-ScheduledTaskTrigger -Once -At (Get-Date).Date.AddMinutes(1) -RepetitionInterval (New-TimeSpan -Minutes 5) -RepetitionDuration (New-TimeSpan -Days 365)
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -RestartCount 5 -RestartInterval (New-TimeSpan -Minutes 2) -ExecutionTimeLimit (New-TimeSpan -Days 0) -MultipleInstances IgnoreNew
$existing = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
if ($existing) { Unregister-ScheduledTask -TaskName $taskName -Confirm:$false }
Register-ScheduledTask -TaskName $taskName -Action $action -Trigger @($triggerLogon,$triggerRepeat) -Settings $settings -Description "SIR Control Room server (hidden, 5-min repeat)" | Out-Null
Write-Host "registered $taskName"
