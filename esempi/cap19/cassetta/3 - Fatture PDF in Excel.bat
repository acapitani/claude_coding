@echo off
chcp 65001 >nul
rem Legge le fatture PDF della sottocartella fatture e crea fatture.xlsx.
where py >nul 2>nul || (echo Manca Python: chiedi all'ufficio informatico di installarlo. & pause & exit /b)
if "%~1"=="" (echo Trascina sull'icona di questo file la cartella che contiene la sottocartella fatture. & pause & exit /b)
cd /d "%~1"
py "%~dp0strumenti\estrai.py" fatture
echo.
pause
