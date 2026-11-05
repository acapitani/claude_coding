@echo off
chcp 65001 >nul
rem PROVA A SECCO: prepara piano.csv con i nuovi nomi. Non tocca nessun file.
where py >nul 2>nul || (echo Manca Python: chiedi all'ufficio informatico di installarlo. & pause & exit /b)
if "%~1"=="" (echo Trascina sull'icona di questo file la cartella che contiene la sottocartella foto. & pause & exit /b)
cd /d "%~1"
py "%~dp0strumenti\rinomina.py" foto
echo.
pause
