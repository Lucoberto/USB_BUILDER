@echo off
:menu
color 0E
cls
echo.
echo    *************************
echo    * USB BUILDER  V1.0.7   *
echo    *************************
echo    * [+] Options.          *
echo    * [1] Repair USB!       *
echo    * [2] Help!             *
echo    * [3] Exit!             *
echo    *************************
echo [!] Developed by @lucoberto [!]
echo.
set /p op="Usb@usb$~> "
if %op%==1 goto reparacion
if %op%==2 goto ayuda
if %op%==3 exit

:reparacion
cls
color 0A
echo Checking Script .... [ OK ]
timeout /t 5 /nobreak > nul
echo Starting Script .... [ OK ]
timeout /t 5 /nobreak > nul
CHKDSK F: /X /F
timeout /t 1 /nobreak > nul
CHKDSK G: /X /F
timeout /t 1 /nobreak > nul
CHKDSK H: /X /F
timeout /t 1 /nobreak > nul
CHKDSK I: /X /F
timeout /t 1 /nobreak > nul
CHKDSK J: /X /F
timeout /t 1 /nobreak > nul
echo Closing Script .... [ OK ]
timeout /t 5 /nobreak > nul
goto menu
:ayuda
color 0E
cls
echo     *************************
echo     *        HELP!!         *
echo     *************************
echo     * This program tries to *
echo     * repair basic errors   *
echo     * at the logical level  *
echo     * in the USB memory (s).*
echo     *************************
echo     * We recommend making a *
echo     * backup.               *
echo     *************************
echo     * We do not take care   *
echo     * of the damages caused *
echo     * by the program.       *
echo     *************************
echo     * attentively @FuryOS   *
echo     *************************
pause
goto menu