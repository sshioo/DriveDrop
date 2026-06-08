@echo off

reg delete "HKEY_CURRENT_USER\Software\Classes\*\shell\DriveDrop" /f
reg delete "HKEY_CURRENT_USER\Software\Classes\Directory\shell\DriveDrop" /f

echo.
echo DriveDrop fue removido del menu contextual.
pause