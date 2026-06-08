@echo off
setlocal

set "PROJECT_DIR=%~dp0"
set "BAT_PATH=%PROJECT_DIR%app\drivedrop.bat"
set "ICON_PATH=%PROJECT_DIR%assets\drivedrop.ico"
set "REG_FILE=%TEMP%\drivedrop_context_menu.reg"

(
echo Windows Registry Editor Version 5.00
echo.
echo [HKEY_CURRENT_USER\Software\Classes\*\shell\DriveDrop]
echo @="Subir con DriveDrop"
echo "Icon"="%ICON_PATH:\=\\%"
echo.
echo [HKEY_CURRENT_USER\Software\Classes\*\shell\DriveDrop\command]
echo @="\"%BAT_PATH:\=\\%\" \"%%1\""
echo.
echo [HKEY_CURRENT_USER\Software\Classes\Directory\shell\DriveDrop]
echo @="Subir con DriveDrop"
echo "Icon"="%ICON_PATH:\=\\%"
echo.
echo [HKEY_CURRENT_USER\Software\Classes\Directory\shell\DriveDrop\command]
echo @="\"%BAT_PATH:\=\\%\" \"%%1\""
) > "%REG_FILE%"

reg import "%REG_FILE%"

echo.
echo DriveDrop fue agregado al menu contextual.
echo Si no aparece de inmediato, reinicia el Explorador de Windows.
pause