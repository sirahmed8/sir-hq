<#
 Generates a professional AI logo for every SIR product with the Antigravity CLI (agy), then rebuilds the icons.
 Run once from a normal PowerShell:  pwsh -NoProfile -File D:\Projects\_SIR\scripts\generate-icons-agy.ps1
 Needs: agy logged in. Re-run safe: skips products that already have assets\brand\source.png (use -Force to redo).
 Prompts: D:\Projects\_SIR\plans\icon-prompts.json (generic descriptions only, no private data).
#>
param([switch]$Force)
$items = Get-Content 'D:\Projects\_SIR\plans\icon-prompts.json' -Raw -Encoding UTF8 | ConvertFrom-Json
foreach ($p in $items.PSObject.Properties) {
  $v = $p.Value; $dir = "D:\Projects\$($v.folder)\assets\brand"
  if (-not (Test-Path "D:\Projects\$($v.folder)\.sir")) { "skip (no project folder): $($v.folder)"; continue }
  New-Item -ItemType Directory -Force $dir | Out-Null
  $out = "$dir\source.png"
  if ((Test-Path $out) -and -not $Force) { "have: $($v.folder)"; continue }
  $prompt = "Use your image generation tool to create ONE professional app icon logo for a product called $($v.display). Concept: $($v.concept). Style: modern premium flat vector look, one bold simple symbol, clean geometry, strong silhouette that stays readable at 16 pixels, generous padding, solid background in the color $($v.color) filling the whole square, white or light symbol with at most one accent tint, no gradients, no text, no letters, no watermark. Save the final image as source.png in the current directory (square, at least 1024 pixels). Reply with only the saved path."
  Push-Location $dir
  agy --print $prompt --mode auto --print-timeout 300s 2>&1 | Select-Object -Last 2
  Pop-Location
  if (Test-Path $out) { "ok: $($v.folder)" } else { "NO IMAGE: $($v.folder)" }
}
pwsh -NoProfile -File 'D:\Projects\_SIR\scripts\make-icons-and-desktop.ps1'
