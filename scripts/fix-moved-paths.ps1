<# D:\Projects\Android and D:\Projects\Backups were moved into D:\Projects (2026-10-30). Points the Android SDK variables at the new place. User-level only, nothing else changed. #>
$old = 'D:\Projects\Android'; $new = 'D:\Projects\Android'
foreach ($v in 'ANDROID_HOME', 'ANDROID_SDK_ROOT') {
  $cur = [Environment]::GetEnvironmentVariable($v, 'User')
  if ($cur -and $cur.StartsWith($old)) { [Environment]::SetEnvironmentVariable($v, $cur.Replace($old, $new), 'User'); "$v -> " + $cur.Replace($old, $new) }
}
$path = [Environment]::GetEnvironmentVariable('Path', 'User')
if ($path -and $path.Contains($old)) { [Environment]::SetEnvironmentVariable('Path', $path.Replace($old, $new), 'User'); 'User PATH entries under D:\Projects\Android repointed' }
'Android SDK exists at new path: ' + (Test-Path "$new\Sdk\platform-tools")
