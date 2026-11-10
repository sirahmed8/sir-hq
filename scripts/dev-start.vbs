' Silent background launcher for SIR Control Room dashboard server daemon
' Runs pythonw.exe completely hidden (SW_HIDE=0) without console windows or visual interruption
' Checks for existing instance before launching to prevent duplicates
' Interpreter: ops/pythonw.path (one line, full path) wins; otherwise the user Python 3.14,
' then msys64, then Python312, then PATH pythonw. Single source: scripts/install-control-task.ps1.
Option Explicit

Dim WshShell, fso, scriptDir, opsDir, pyScript, cmd, pyw, lockFile, pid, cfgFile
Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)
opsDir = fso.BuildPath(scriptDir, "..", "ops")
pyScript = fso.BuildPath(scriptDir, "serve-control-room.py")
lockFile = fso.BuildPath(opsDir, "control-room.lock")
cfgFile = fso.BuildPath(opsDir, "pythonw.path")

' Check if lock file exists and process is still alive
If fso.FileExists(lockFile) Then
    Dim ts, pidStr, proc
    Set ts = fso.OpenTextFile(lockFile, 1) ' ForReading
    pidStr = ts.ReadAll
    ts.Close
    If IsNumeric(pidStr) Then
        pid = CLng(pidStr)
        ' Try to get process - if it exists and is our script, don't launch
        On Error Resume Next
        Set proc = WshShell.Exec("tasklist /FI ""PID eq " & pid & """ /FI ""IMAGENAME eq pythonw.exe"" /FO CSV")
        Dim output
        output = proc.StdOut.ReadAll
        If InStr(output, "serve-control-room.py") > 0 Then
            WScript.Quit ' Another instance is running
        End If
        On Error GoTo 0
    End If
End If

pyw = ""
' Optional operator override: full path to pythonw.exe, one line
If fso.FileExists(cfgFile) Then
    Dim cfgTs
    Set cfgTs = fso.OpenTextFile(cfgFile, 1)
    pyw = Trim(cfgTs.ReadAll)
    cfgTs.Close
    If pyw <> "" And Not fso.FileExists(pyw) Then pyw = ""
End If

If pyw = "" Then
    If fso.FileExists("C:\Users\a7med\AppData\Local\Python\pythoncore-3.14-64\pythonw.exe") Then
        pyw = "C:\Users\a7med\AppData\Local\Python\pythoncore-3.14-64\pythonw.exe"
    ElseIf fso.FileExists("C:\msys64\ucrt64\bin\pythonw.exe") Then
        pyw = "C:\msys64\ucrt64\bin\pythonw.exe"
    ElseIf fso.FileExists("C:\Users\a7med\AppData\Local\Programs\Python\Python312\pythonw.exe") Then
        pyw = "C:\Users\a7med\AppData\Local\Programs\Python\Python312\pythonw.exe"
    Else
        pyw = "pythonw.exe"
    End If
End If

cmd = """" & pyw & """ """ & pyScript & """"

' Run with window style 0 (hidden) and do not block (bWaitOnReturn = False)
WshShell.Run cmd, 0, False
