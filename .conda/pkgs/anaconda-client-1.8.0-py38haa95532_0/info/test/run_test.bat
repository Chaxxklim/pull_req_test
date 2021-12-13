



pip check
IF %ERRORLEVEL% NEQ 0 exit /B 1
anaconda --help
IF %ERRORLEVEL% NEQ 0 exit /B 1
binstar --help
IF %ERRORLEVEL% NEQ 0 exit /B 1
conda-server --help
IF %ERRORLEVEL% NEQ 0 exit /B 1
exit /B 0
