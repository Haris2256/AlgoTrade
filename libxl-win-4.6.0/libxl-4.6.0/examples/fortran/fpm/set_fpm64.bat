doskey fpm="D:\Program Files\fpm\fpm-0.9.0-windows-x86_64.exe" $*
set path=%path%;D:\Program Files\mingw64\bin
set FPM_LDFLAGS=..\..\..\bin64\libxl.dll
set path=%path%;..\..\..\bin64
cmd