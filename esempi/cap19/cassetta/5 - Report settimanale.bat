@echo off
chcp 65001 >nul
rem Report delle vendite della settimana scorsa (Word + email in bozza) da vendite.csv.
where py >nul 2>nul || (echo Manca Python: chiedi all'ufficio informatico di installarlo. & pause & exit /b)
if "%~1"=="" (echo Trascina sull'icona di questo file la cartella che contiene vendite.csv. & pause & exit /b)
cd /d "%~1"
py "%~dp0strumenti\report.py" %2
echo.
pause
