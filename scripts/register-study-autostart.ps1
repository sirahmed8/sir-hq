$arg = '-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File "D:\Projects\SIR Study\scripts\dev-start.ps1"'
$a = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument $arg
Register-ScheduledTask -TaskName 'SIR_Study_Server' -Action $a -Trigger (New-ScheduledTaskTrigger -AtLogOn) -Force | Out-Null
Get-ScheduledTask -TaskName 'SIR_Study_Server' | Select-Object TaskName, State
