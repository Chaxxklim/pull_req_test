



if not exist %LIBRARY_LIB%\cfitsio.lib exit 1
IF %ERRORLEVEL% NEQ 0 exit /B 1
if not exist %LIBRARY_BIN%\cfitsio.dll exit 1
IF %ERRORLEVEL% NEQ 0 exit /B 1
exit /B 0
