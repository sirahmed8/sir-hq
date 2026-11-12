# Install/update SIR_HQ_Publish scheduled task: deploys the Control Room mirror to Cloudflare Pages every 30 minutes (hidden, BelowNormal inside the script).
$ErrorActionPreference = "Stop"
$taskName = "SIR_HQ_Publish"
$py = "C:\Users\a7med\AppData\Local\Python\pythoncore-3.14-64\pythonw.exe"
if (-not (Test-Path $py)) { $py = (Get-Command pythonw.exe).Source }
$script = "D:\Projects\_SIR\scripts\publish_control_room.py"
# Fire at :10 and :40, ten minutes after SIR_HQ_Dashboard regenerates at :00 and :30.
$start = (Get-Date).Date.AddHours((Get-Date).Hour).AddMinutes(10)
if ($start -le (Get-Date)) { $start = $start.AddMinutes(30) }
$triggerRepeat = New-ScheduledTaskTrigger -Once -At $start -RepetitionInterval (New-TimeSpan -Minutes 30) -RepetitionDuration (New-TimeSpan -Days 365)
$triggerLogon = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 5) -ExecutionTimeLimit (New-TimeSpan -Minutes 15) -MultipleInstances IgnoreNew
$existing = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
if ($existing) { Unregister-ScheduledTask -TaskName $taskName -Confirm:$false }
$action = New-ScheduledTaskAction -Execute $py -Argument "`"$script`"" -WorkingDirectory "D:\Projects\_SIR"
Register-ScheduledTask -TaskName $taskName -Action $action -Trigger @($triggerLogon,$triggerRepeat) -Settings $settings -Description "SIR Control Room Cloudflare Pages mirror publish (hidden, every 30 min)" | Out-Null
Write-Host "registered $taskName (first run $start)"
