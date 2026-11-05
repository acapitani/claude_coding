@echo off
chcp 65001 >nul
rem Unisce gli estratti mensili Excel in riepilogo.xlsx, con formule e grafico.
where py >nul 2>nul || (echo Manca Python: chiedi all'ufficio informatico di installarlo. & pause & exit /b)
if "%~1"=="" (echo Trascina sull'icona di questo file la cartella che contiene la sottocartella estratti. & pause & exit /b)
cd /d "%~1"
py "%~dp0strumenti\unisci.py" estratti
echo.
pause
