Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "D:\Projects\_SIR\tools\sir-autonomy"
WshShell.Run """D:\Projects\_SIR\tools\sir-autonomy\.venv\Scripts\pythonw.exe"" ""D:\Projects\_SIR\tools\sir-autonomy\bridge_server.py""", 0, False
