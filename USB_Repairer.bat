@echo off
:menu
color 0E
cls
echo.
echo    *************************
echo    * USB Repairer  V0.7    *
echo    *************************
echo    * [+] Options.          *
echo    * [1] USB Repair!       *
echo    * [2] Help!             *
echo    * [3] Exit!             *
echo    *************************
echo [!] Developed by @lucoberto [!]
echo.
set /p op="Usb@usb$~> "
if %op%==1 goto reparar
if %op%==2 goto ayuda
if %op%==3 exit

:reparar
color 0E
cls
echo.
echo    *************************
echo    *        Repair         *
echo    *************************
echo    * [+] Options.          *
echo    * [1] Default!          *
echo    * [2] Personalized!     *
echo    * [3] Back!             *
echo    *************************
echo [!] Developed by @lucoberto [!]
echo.
set /p op="Usb@usb$~> "
if %op%==1 goto Defecto
if %op%==2 goto personal
if %op%==3 goto menu

:Defecto
cls
color 0A
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
goto menu

:personal
cls
color 0A
echo.
echo Put the letter of the USB.
echo.
set /p op="Usb@usb$~> "
CHKDSK %op%: /X /F
timeout /t 1 /nobreak > nul
goto reparar

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
echo     *        @FuryOS        *
echo     *************************
pause
goto menu