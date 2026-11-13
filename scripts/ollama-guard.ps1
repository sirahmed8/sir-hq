<#
    Ollama memory guard for the one local brain (AHome).
    Runs from scheduled task SIR_Ollama_Guard every 5 minutes and is safe to run by hand.

    What it protects, in order:
      1. The laptop: when available RAM drops below -MinAvailableMB, a background light model is unloaded
         first and qwen3.5:9b only as the last resort.
      2. A game: while AHome's game mode is active, every model is unloaded so the game owns the 6 GB of VRAM;
         the chat model is warmed again when the game closes.
      3. The first message of the day: when nothing is loaded and the machine is idle, qwen3.5:9b is warmed
         at the fixed 16384 context so the next request does not pay a 15 s load.

    Log: D:\Projects\AHome\local-vault\logs\ollama-guard.log (model names and MB only, no message text).
#>
param(
    [int]$MinAvailableMB = 1500,
    [int]$ChatWindow = 16384,
    [string]$ChatModel = "qwen3.5:9b",
    [switch]$Quiet
)

$ErrorActionPreference = "SilentlyContinue"
$OllamaUrl = "http://127.0.0.1:11434"
$ProjectRoot = "D:\Projects\AHome"
$GameState = Join-Path $ProjectRoot "local-vault\state\game-mode.json"
$LogFile = Join-Path $ProjectRoot "local-vault\logs\ollama-guard.log"

function Write-GuardLog([string]$Line) {
    $stamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    try {
        $null = New-Item -ItemType Directory -Force -Path (Split-Path -Parent $LogFile)
        Add-Content -LiteralPath $LogFile -Value "$stamp $Line" -Encoding UTF8
    } catch { }
    if (-not $Quiet) { Write-Output "$stamp $Line" }
}

function Get-AvailableMB {
    try {
        $counter = Get-CimInstance Win32_PerfFormattedData_PerfOS_Memory -ErrorAction Stop
        return [int]$counter.AvailableMBytes
    } catch {
        $os = Get-CimInstance Win32_OperatingSystem -ErrorAction SilentlyContinue
        if ($os) { return [int]($os.FreePhysicalMemory / 1024) }
        return -1
    }
}

function Get-LoadedModels {
    try {
        $ps = Invoke-RestMethod -Uri "$OllamaUrl/api/ps" -TimeoutSec 5
        return @($ps.models)
    } catch { return @() }
}

function Unload-Model([string]$Name) {
    try {
        $body = @{ model = $Name; keep_alive = 0 } | ConvertTo-Json -Compress
        $null = Invoke-RestMethod -Uri "$OllamaUrl/api/generate" -Method Post -Body $body -ContentType "application/json" -TimeoutSec 20
        Write-GuardLog "unloaded $Name"
        return $true
    } catch {
        Write-GuardLog "could not unload $Name ($($_.Exception.GetType().Name))"
        return $false
    }
}

function Test-OllamaUp {
    try {
        $null = Invoke-RestMethod -Uri "$OllamaUrl/api/version" -TimeoutSec 4
        return $true
    } catch { return $false }
}

function Test-GameMode {
    try {
        $state = Get-Content -LiteralPath $GameState -Raw -Encoding UTF8 | ConvertFrom-Json
        if (-not $state.active) { return $false }
        if ($state.updated_epoch) {
            $age = [DateTimeOffset]::UtcNow.ToUnixTimeSeconds() - [int64]$state.updated_epoch
            if ($age -gt 120) { return $false }
        }
        return $true
    } catch { return $false }
}

function Start-WarmChat {
    param([string]$Reason)
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
        Write-GuardLog "warmed $ChatModel at $ChatWindow context ($Reason)"
    } catch {
        Write-GuardLog "warm failed for $ChatModel ($($_.Exception.GetType().Name))"
    }
}

if (-not (Test-OllamaUp)) { Write-GuardLog "ollama is not answering on $OllamaUrl"; exit 1 }

$available = Get-AvailableMB
$loaded = Get-LoadedModels
$loadedNames = @($loaded | ForEach-Object { $_.name })
$vramMB = 0
foreach ($m in $loaded) { $vramMB += [int]($m.size_vram / 1MB) }
$summary = "ram_available_mb=$available loaded=[$($loadedNames -join ',')] vram_mb=$vramMB"

if (Test-GameMode) {
    if ($loadedNames.Count -gt 0) {
        foreach ($name in $loadedNames) { Unload-Model $name }
        Write-GuardLog "game mode active: freed GPU memory ($summary)"
    } else {
        Write-GuardLog "game mode active: nothing loaded ($summary)"
    }
    exit 0
}

if ($available -ge 0 -and $available -lt $MinAvailableMB) {
    Write-GuardLog "memory low: $summary"
    $others = @($loadedNames | Where-Object { $_ -ne $ChatModel })
    foreach ($name in $others) { Unload-Model $name }
    Start-Sleep -Seconds 3
    $available = Get-AvailableMB
    if ($available -lt $MinAvailableMB -and ($loadedNames -contains $ChatModel)) {
        Write-GuardLog "still low after background unload (ram_available_mb=$available): unloading $ChatModel as the last resort"
        Unload-Model $ChatModel
    } else {
        Write-GuardLog "background models unloaded, ram_available_mb=$available"
    }
    exit 0
}

if ($loadedNames -contains $ChatModel) {
    Write-GuardLog "ok: chat model resident ($summary)"
    exit 0
}
if ($loadedNames.Count -gt 0) {
    foreach ($name in $loadedNames) { Unload-Model $name }
}
Start-WarmChat "idle warm"
exit 0
