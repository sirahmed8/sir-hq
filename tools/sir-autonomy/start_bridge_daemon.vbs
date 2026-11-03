Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "D:\Projects\_SIR\tools\sir-autonomy"
WshShell.Run "cmd /c """"""D:\Projects\_SIR\tools\sir-autonomy\.venv\Scripts\python.exe"""" """"D:\Projects\_SIR\tools\sir-autonomy\bridge_server.py"""" > """"D:\Projects\_SIR\tools\sir-autonomy\bridge.log"""" 2>&1""", 0, False
