<#
 Lists the programs whose CURRENT FOLDER is inside D:\Projects (these are what stop Windows from moving or renaming a folder).
 Usage: pwsh -NoProfile -File who-holds.ps1 [-Kill] [-Match "Laptop manager"]
 -Kill stops only programs that are NOT Claude/Explorer/system and are not this session. Read-only without -Kill.
#>
param([switch]$Kill, [string]$Match = 'D:\Projects')
Add-Type -TypeDefinition @'
using System;
using System.Runtime.InteropServices;
using System.Text;
public static class Cwd {
  [DllImport("ntdll.dll")] static extern int NtQueryInformationProcess(IntPtr h, int cls, ref PBI pbi, int len, out int ret);
  [DllImport("kernel32.dll")] static extern IntPtr OpenProcess(int access, bool inherit, int pid);
  [DllImport("kernel32.dll")] static extern bool ReadProcessMemory(IntPtr h, IntPtr addr, byte[] buf, int size, out IntPtr read);
  [DllImport("kernel32.dll")] static extern bool CloseHandle(IntPtr h);
  [StructLayout(LayoutKind.Sequential)] struct PBI { public IntPtr Reserved1; public IntPtr PebBaseAddress; public IntPtr Reserved2_0; public IntPtr Reserved2_1; public IntPtr UniquePid; public IntPtr Reserved3; }
  public static string Get(int pid) {
    IntPtr h = OpenProcess(0x1010, false, pid);
    if (h == IntPtr.Zero) return null;
    try {
      PBI pbi = new PBI(); int ret;
      if (NtQueryInformationProcess(h, 0, ref pbi, Marshal.SizeOf(pbi), out ret) != 0) return null;
      byte[] b = new byte[8]; IntPtr rd;
      if (!ReadProcessMemory(h, new IntPtr(pbi.PebBaseAddress.ToInt64() + 0x20), b, 8, out rd)) return null;
      long pp = BitConverter.ToInt64(b, 0);
      byte[] us = new byte[16];
      if (!ReadProcessMemory(h, new IntPtr(pp + 0x38), us, 16, out rd)) return null;
      int len = BitConverter.ToUInt16(us, 0); long buf = BitConverter.ToInt64(us, 8);
      if (len <= 0 || len > 2048) return null;
      byte[] s = new byte[len];
      if (!ReadProcessMemory(h, new IntPtr(buf), s, len, out rd)) return null;
      return Encoding.Unicode.GetString(s);
    } finally { CloseHandle(h); }
  }
}
'@
$self = @($PID); $p = Get-CimInstance Win32_Process -Filter "ProcessId=$PID"
while ($p -and $p.ParentProcessId) { $self += $p.ParentProcessId; $p = Get-CimInstance Win32_Process -Filter "ProcessId=$($p.ParentProcessId)" -ErrorAction SilentlyContinue }
$protect = 'Claude', 'claude', 'explorer', 'System', 'svchost', 'csrss', 'winlogon', 'dwm', 'cmd'   # never touched
foreach ($proc in Get-Process) {
  $cwd = [Cwd]::Get($proc.Id)
  if ($cwd -and $cwd.StartsWith('D:\Projects', [StringComparison]::OrdinalIgnoreCase) -and $cwd -like "*$Match*" -and $cwd -notlike 'D:\Projects\_SIR*') {
    $mine = $self -contains $proc.Id
    '{0,6} {1,-16} {2}{3}' -f $proc.Id, $proc.ProcessName, $cwd, $(if ($mine) { '   (this session)' } else { '' })
    if ($Kill -and -not $mine -and $protect -notcontains $proc.ProcessName) { Stop-Process -Id $proc.Id -Force -ErrorAction SilentlyContinue; '        stopped' }
  }
}
