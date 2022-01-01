@echo off

cd /d "%~dp0"

:SELECTGAMEPATH

FFXIIIGetPath.exe LRFF13.exe Select the 'LRFF13.exe' file in the LIGHTNING RETURNS FINAL FANTASY XIII game directory.

if exist selectedPath.txt goto PATHSELECTED

@echo Game path cancelled or error occurred.  Exiting.
goto ENDBATCH

:PATHSELECTED

set /p lrpath=<SelectedPath.txt

if exist "%lrpath%LRFF13.exe" goto GOODDIR

@echo Incorrect path chosen as the LRFF13.exe file is not found in
@echo %lrpath%
@echo.

CHOICE /C ET /N /M "(E)xit installer or (T)ry again? "

if %ERRORLEVEL% EQU 1 goto ENDBATCH
goto SELECTGAMEPATH


:GOODDIR

@echo.
@echo Setting Volume....
cd /d "%lrpath%weiss_data\
del "%lrpath%weiss_data\db\resident\wdbpack.bin"> nul
del "%lrpath%weiss_data\sound\pack\8000\music_W_title4.win32.scd"> nul


cd /d "%~dp0"\level_2\db\resident
copy wdbpack.bin "%lrpath%"weiss_data\db\resident\*.* > nul

cd /d "%~dp0"\level_2\sound\pack\8000
copy music_W_title4.win32.scd "%lrpath%"weiss_data\sound\pack\8000\*.* > nul



echo MSGBOX "Music volume is set to level 2", 64, "LR music volume slider" > msgbox.vbs
call msgbox.vbs
