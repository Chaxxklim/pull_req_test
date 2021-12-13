



curl --help
IF %ERRORLEVEL% NEQ 0 exit /B 1
curl https://raw.githubusercontent.com/conda-forge/curl-feedstock/master/LICENSE.txt
IF %ERRORLEVEL% NEQ 0 exit /B 1
if not exist %LIBRARY_BIN%\curl.exe exit 1
IF %ERRORLEVEL% NEQ 0 exit /B 1
exit /B 0
