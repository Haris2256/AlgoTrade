doskey fpm="D:\Program Files\fpm\fpm-0.9.0-windows-x86_64.exe" $*
set FPM_FC=ifort
set FPM_FFLAGS=/libs:dll
set FPM_LDFLAGS=../../../lib64/libxl.lib
set path=%path%;..\..\..\bin64
call "C:\Program Files (x86)\Intel\oneAPI\setvars.bat"
cmd
