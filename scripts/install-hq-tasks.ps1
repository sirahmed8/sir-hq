# Registers the HQ background tasks (run at logon, hidden, restart on failure). Same method as Laptop Manager's install-autostart.ps1.
$ErrorActionPreference = "Stop"
$py = "C:\Users\a7med\AppData\Local\Python\pythoncore-3.14-64\pythonw.exe"
if (-not (Test-Path $py)) { $py = (Get-Command pythonw.exe).Source }
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -RestartCount 5 -RestartInterval (New-TimeSpan -Minutes 2) -ExecutionTimeLimit (New-TimeSpan -Days 0)
$trigger = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
foreach ($t in @(@{n="SIR_HQ_Autopilot"; a="D:\Projects\_SIR\scripts\hq_autopilot.py"})) {
  $existing = Get-ScheduledTask -TaskName $t.n -ErrorAction SilentlyContinue
  if ($existing) { Unregister-ScheduledTask -TaskName $t.n -Confirm:$false }
  $action = New-ScheduledTaskAction -Execute $py -Argument "`"$($t.a)`"" -WorkingDirectory "D:\Projects\_SIR"
  Register-ScheduledTask -TaskName $t.n -Action $action -Trigger $trigger -Settings $settings -Description "SIR HQ autopilot (independent of Claude)" | Out-Null
  Write-Host "registered $($t.n)"
}
