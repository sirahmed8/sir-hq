<#
.SYNOPSIS
  One wrapper for all AI providers (core/03-team.md, "External workforce").
.DESCRIPTION
  Runs a prompt file through a provider chain, writes the answer to -Out, logs every attempt to
  _SIR/ops/usage-ledger.jsonl, retries once, then falls back to the next provider.
  A provider that hit a quota/rate limit is marked "cooling" in _SIR/ops/provider-cooling.json.
  Never sends anything that looks like a secret to a non-local provider (rule 13); use -Sensitive
  to force local-only.
.PARAMETER Provider  local | gemini | opencode | kilo | auto, or a comma chain such as "gemini,local".
                     A chain item may carry a model: "opencode:opencode/deepseek-v4.1-flash-free".
.PARAMETER Task      Path to a UTF-8 text file holding the prompt.
.PARAMETER Out       Path for the answer text.
.PARAMETER Model     Model for a single provider (ignored when chain items carry their own).
.PARAMETER TimeoutMin  Per-attempt timeout in minutes (default 15).
.PARAMETER TaskId    Free-text label for the ledger.
.PARAMETER Sensitive Local only, never an outside provider.
.EXAMPLE
  ./ask.ps1 -Provider auto -Task prompt.txt -Out answer.txt -TaskId T-012
#>
[CmdletBinding()]
param(
  [string]$Provider = 'auto',
  [Parameter(Mandatory)][string]$Task,
  [Parameter(Mandatory)][string]$Out,
  [string]$Model = '',
  [int]$TimeoutMin = 15,
  [string]$TaskId = '',
  [switch]$Sensitive
)
$ErrorActionPreference = 'Stop'
$ops = Join-Path (Split-Path $PSScriptRoot -Parent -Resolve | Split-Path -Parent) 'ops'
$ledger = Join-Path $ops 'usage-ledger.jsonl'
$coolFile = Join-Path $ops 'provider-cooling.json'
$limitRx = 'quota|rate.?limit|429|RESOURCE_EXHAUSTED|usage limit|exceeded|authentication required'
$localDefault = 'qwen2.5:1.5b'
$cooldown = @{ gemini = 300; opencode = 120; kilo = 120; local = 0 }   # minutes

if (-not (Test-Path -LiteralPath $Task)) { throw "Task file not found: $Task" }
$prompt = Get-Content -LiteralPath $Task -Raw -Encoding UTF8
if ([string]::IsNullOrWhiteSpace($prompt)) { throw 'Task file is empty' }

# Rule 13: nothing secret-looking leaves the laptop.
$secretRx = 'AIza[0-9A-Za-z_\-]{30,}|sk-[A-Za-z0-9_\-]{20,}|gh[pousr]_[A-Za-z0-9]{30,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|\b\d{8,10}:AA[A-Za-z0-9_\-]{30,}|(?i)(password|passwd|secret|api[_-]?key|token)\s*[:=]\s*\S{8,}'
$looksSecret = $prompt -match $secretRx
if ($looksSecret) { Write-Warning 'Prompt looks like it contains a credential: outside providers are disabled for this call.' }
$localOnly = $Sensitive -or $looksSecret

function Read-Cooling { if (Test-Path $coolFile) { try { return (Get-Content $coolFile -Raw | ConvertFrom-Json -AsHashtable) } catch {} }; return @{} }
function Set-Cooling($name, $mins) { $c = Read-Cooling; $c[$name] = (Get-Date).AddMinutes($mins).ToString('o'); $c | ConvertTo-Json | Set-Content $coolFile -Encoding UTF8 }
function Is-Cooling($name) { $c = Read-Cooling; if ($c.ContainsKey($name)) { return ([datetime]$c[$name]) -gt (Get-Date) }; return $false }
function Write-Ledger($rec) { New-Item -ItemType Directory -Force -Path $ops | Out-Null; ($rec | ConvertTo-Json -Compress) | Add-Content -LiteralPath $ledger -Encoding UTF8 }

# Each invoker returns @{ ok; text; err } and never throws.
function Invoke-Local($m) {
  try {
    if (-not $m) { $m = $localDefault }
    $body = @{ model = $m; prompt = $prompt; stream = $false } | ConvertTo-Json -Compress
    $r = Invoke-RestMethod -Uri 'http://localhost:11434/api/generate' -Method Post -Body ([Text.Encoding]::UTF8.GetBytes($body)) -ContentType 'application/json; charset=utf-8' -TimeoutSec ($TimeoutMin * 60)
    return @{ ok = [bool]$r.response; text = $r.response; err = '' }
  } catch { return @{ ok = $false; text = ''; err = $_.Exception.Message } }
}
function Invoke-Cli($exe, $argList, [switch]$LineJson) {
  try {
    # npm installs an extensionless shell shim next to the .cmd; Start-Process needs a real .exe/.cmd.
    $cmd = Get-Command $exe -CommandType Application -ErrorAction SilentlyContinue | Where-Object { $_.Source -match '\.(exe|cmd|bat)$' } | Select-Object -First 1
    if (-not $cmd) { return @{ ok = $false; text = ''; err = "$exe not found on PATH" } }
    $exe = $cmd.Source
    $tmpOut = New-TemporaryFile; $tmpErr = New-TemporaryFile
    $p = Start-Process -FilePath $exe -ArgumentList $argList -NoNewWindow -PassThru -RedirectStandardOutput $tmpOut -RedirectStandardError $tmpErr
    if (-not $p.WaitForExit($TimeoutMin * 60 * 1000)) { Stop-Process -Id $p.Id -Force; return @{ ok = $false; text = ''; err = 'timeout (exit 124)' } }
    $so = Get-Content $tmpOut -Raw -Encoding UTF8; $se = Get-Content $tmpErr -Raw -Encoding UTF8
    Remove-Item $tmpOut, $tmpErr -Force -ErrorAction SilentlyContinue
    if ($p.ExitCode -ne 0) { return @{ ok = $false; text = ''; err = "exit $($p.ExitCode): $se $so" } }
    if ($LineJson) {
      $texts = foreach ($ln in ($so -split "`r?`n")) { if ($ln.Trim().StartsWith('{')) { try { $j = $ln | ConvertFrom-Json; if ($j.type -eq 'text') { $j.part.text } elseif ($j.type -eq 'error') { throw ($j.error.message) } } catch { if ($_.Exception.Message -and $_.Exception.GetType().Name -ne 'ArgumentException') { return @{ ok = $false; text = ''; err = $_.Exception.Message } } } } }
      $t = ($texts -join '')
      return @{ ok = [bool]$t.Trim(); text = $t; err = $(if ($t.Trim()) { '' } else { "empty result. $se" }) }
    }
    $j = $so | ConvertFrom-Json
    if ($j.status -ne 'SUCCESS') { return @{ ok = $false; text = ''; err = "$($j.status): $($j.error)" } }
    return @{ ok = [bool]$j.response.Trim(); text = $j.response; err = $(if ($j.response.Trim()) { '' } else { 'empty result' }) }
  } catch { return @{ ok = $false; text = ''; err = $_.Exception.Message } }
}
function Invoke-Provider($name, $m) {
  switch ($name) {
    'local'    { return Invoke-Local $m }
    'gemini'   { $a = @('-p', ('"' + ($prompt -replace '"', '\"') + '"'), '--output-format', 'json', '--print-timeout', "${TimeoutMin}m"); if ($m) { $a += @('--model', $m) }; return Invoke-Cli 'agy' $a }
    'opencode' { if (-not $m) { $m = 'opencode/deepseek-v4.1-flash-free' }; return Invoke-Cli 'opencode' @('run', '-m', $m, '--format', 'json', ('"' + ($prompt -replace '"', '\"') + '"')) -LineJson }
    'kilo'     { return Invoke-Cli 'kilo' @('run', '--auto', '--format', 'json', ('"' + ($prompt -replace '"', '\"') + '"')) -LineJson }
    default    { return @{ ok = $false; text = ''; err = "unknown provider $name" } }
  }
}

$chain = if ($Provider -eq 'auto') { @('local', 'gemini', 'opencode', 'kilo') } else { $Provider -split ',' | ForEach-Object { $_.Trim() } | Where-Object { $_ } }
if ($localOnly) { $chain = @($chain | Where-Object { ($_ -split ':')[0] -eq 'local' }); if (-not $chain) { $chain = @('local') } }
if (($prompt.Length -gt 24000) -and ($chain | Where-Object { ($_ -split ':')[0] -in 'gemini', 'opencode', 'kilo' })) { Write-Warning 'Prompt over 24k characters: CLI providers may hit the Windows command-line limit.' }

foreach ($item in $chain) {
  $name, $itemModel = $item -split ':', 2
  $m = if ($itemModel) { $itemModel } else { $Model }
  if (Is-Cooling $name) { Write-Ledger @{ time = (Get-Date).ToString('o'); provider = $name; model = $m; task = $TaskId; status = 'skipped-cooling' }; continue }
  foreach ($attempt in 1..2) {
    $sw = [Diagnostics.Stopwatch]::StartNew()
    $r = Invoke-Provider $name $m
    $sw.Stop()
    $status = if ($r.ok) { 'ok' } elseif ($r.err -match $limitRx) { 'limit' } else { 'error' }
    Write-Ledger @{ time = (Get-Date).ToString('o'); provider = $name; model = $m; task = $TaskId; attempt = $attempt; seconds = [math]::Round($sw.Elapsed.TotalSeconds, 1); status = $status; chars_in = $prompt.Length; chars_out = $r.text.Length; error = ($r.err -replace '\s+', ' ').Substring(0, [math]::Min(160, $r.err.Length)) }
    if ($r.ok) { $outDir = Split-Path -Parent $Out; if ($outDir) { New-Item -ItemType Directory -Force -Path $outDir | Out-Null }; Set-Content -LiteralPath $Out -Value $r.text -Encoding UTF8; Write-Output "provider=$name model=$m seconds=$([math]::Round($sw.Elapsed.TotalSeconds,1)) out=$Out"; exit 0 }
    if ($status -eq 'limit') { Set-Cooling $name $cooldown[$name]; break }
    if ($attempt -eq 1) { Start-Sleep -Seconds 3 }
  }
}
Write-Error 'All providers failed or are cooling. Mark the task blocked: usage and switch to other work.'
exit 1
