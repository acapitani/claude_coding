@echo off
chcp 65001 >nul
rem Stampa unione: una lettera per ogni riga di clienti.xlsx, dal modello Word.
where py >nul 2>nul || (echo Manca Python: chiedi all'ufficio informatico di installarlo. & pause & exit /b)
if "%~1"=="" (echo Trascina sull'icona di questo file la cartella con clienti.xlsx e modello-sollecito.docx. & pause & exit /b)
cd /d "%~1"
py "%~dp0strumenti\lettere.py"
echo.
pause
