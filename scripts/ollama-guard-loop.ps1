<#
    Runs the Ollama guard for the whole logon session.
    Started once at logon from the Startup folder (SIR-Ollama-Guard.vbs), no scheduled task and no admin needed.
    A named mutex guarantees a single instance even if the file is launched twice.
    First pass: warm qwen3.5:9b (see ollama-warmup.ps1 rules). After that: the guard every 5 minutes.
#>
param(
    [int]$IntervalSeconds = 300
)

$ErrorActionPreference = "SilentlyContinue"
$mutex = New-Object System.Threading.Mutex($false, "Global\SIR_Ollama_Guard_Loop")
if (-not $mutex.WaitOne(0)) { exit 0 }   # another copy is already running

$guard = "D:\Projects\_SIR\scripts\ollama-guard.ps1"
$warm = "D:\Projects\_SIR\scripts\ollama-warmup.ps1"

& $warm | Out-Null
while ($true) {
    Start-Sleep -Seconds $IntervalSeconds
    & $guard -Quiet | Out-Null
}
