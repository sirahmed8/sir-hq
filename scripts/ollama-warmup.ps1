<#
    Warm-up for the one local brain (AHome): make qwen3.5:9b resident right after logon.
    Runs from scheduled task SIR_Ollama_Warmup at logon (Ollama autostarts; this waits for it to answer).
    The model stays loaded (keep_alive -1) at the same 16384 context every AHome request uses, so the first
    message of the day is not a 15 s cold load. Safe to run by hand at any time.
#>
param(
    [string]$ChatModel = "qwen3.5:9b",
    [int]$ChatWindow = 16384,
    [int]$WaitSeconds = 180
)

$ErrorActionPreference = "SilentlyContinue"
$OllamaUrl = "http://127.0.0.1:11434"
$LogFile = "D:\Projects\AHome\local-vault\logs\ollama-guard.log"

function Write-WarmLog([string]$Line) {
    $stamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    try {
        $null = New-Item -ItemType Directory -Force -Path (Split-Path -Parent $LogFile)
        Add-Content -LiteralPath $LogFile -Value "$stamp warmup: $Line" -Encoding UTF8
    } catch { }
    Write-Output "$stamp warmup: $Line"
}

$deadline = (Get-Date).AddSeconds($WaitSeconds)
$up = $false
while ((Get-Date) -lt $deadline) {
    try {
        $null = Invoke-RestMethod -Uri "$OllamaUrl/api/version" -TimeoutSec 4
        $up = $true
        break
    } catch { Start-Sleep -Seconds 3 }
}
if (-not $up) {
    Write-WarmLog "ollama did not answer within $WaitSeconds s; skipping"
    exit 1
}

$gameFile = "D:\Projects\AHome\local-vault\state\game-mode.json"
try {
    $state = Get-Content -LiteralPath $gameFile -Raw -Encoding UTF8 | ConvertFrom-Json
    if ($state.active) { Write-WarmLog "game mode is active; not loading the model"; exit 0 }
} catch { }

$started = Get-Date
try {
    $body = @{
        model      = $ChatModel
        messages   = @(@{ role = "user"; content = "hi" })
        stream     = $false
        think      = $false
        keep_alive = -1
        options    = @{ num_ctx = $ChatWindow; num_predict = 2 }
    } | ConvertTo-Json -Depth 6 -Compress
    $null = Invoke-RestMethod -Uri "$OllamaUrl/api/chat" -Method Post -Body $body -ContentType "application/json" -TimeoutSec 240
} catch {
    Write-WarmLog "warm failed ($($_.Exception.GetType().Name))"
    exit 1
}

$loaded = @()
try { $loaded = @((Invoke-RestMethod -Uri "$OllamaUrl/api/ps" -TimeoutSec 5).models) } catch { }
$entry = $loaded | Where-Object { $_.name -eq $ChatModel } | Select-Object -First 1
if ($entry) {
    $vram = [math]::Round($entry.size_vram / 1MB)
    $total = [math]::Round($entry.size / 1MB)
    $seconds = [int]((Get-Date) - $started).TotalSeconds
    Write-WarmLog "$ChatModel resident in ${vram} MB of ${total} MB, context $($entry.context_length), ready in ${seconds}s"
} else {
    Write-WarmLog "$ChatModel answered but is not listed by /api/ps"
}
exit 0
