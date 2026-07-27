@echo off
REM Script para sincronizar Estrategia-FLOW-guitarra-base.md a D:\METODO FLOW 2026
REM Ejecutar desde la carpeta del proyecto en Windows

echo ========================================
echo Sincronizando FLOW Strategy Document
echo ========================================
echo.

REM Actualizar repo
echo [1/3] Actualizando repo desde GitHub...
git fetch origin claude/music-teacher-workflow-rHifB
git pull origin claude/music-teacher-workflow-rHifB

if errorlevel 1 (
    echo ERROR: No se pudo actualizar el repo. Verifica tu conexión.
    pause
    exit /b 1
)

echo OK: Repo actualizado
echo.

REM Crear carpeta si no existe
echo [2/3] Verificando carpeta D:\METODO FLOW 2026\...
if not exist "D:\METODO FLOW 2026" (
    echo Creando carpeta D:\METODO FLOW 2026\...
    mkdir "D:\METODO FLOW 2026"
)

echo OK: Carpeta lista
echo.

REM Copiar archivo principal
echo [3/3] Copiando archivos...

copy "Estrategia-FLOW-guitarra-base.md" "D:\METODO FLOW 2026\Estrategia-FLOW-guitarra-base.md"
if errorlevel 1 (
    echo ERROR: No se pudo copiar el archivo principal.
    pause
    exit /b 1
)
echo   [✓] Estrategia-FLOW-guitarra-base.md

REM Copiar archivos auxiliares si existen
if exist "Carruseles-para-disenar.md" (
    copy "Carruseles-para-disenar.md" "D:\METODO FLOW 2026\Carruseles-para-disenar.md"
    echo   [✓] Carruseles-para-disenar.md
)

if exist "Guiones-para-filmar.pdf" (
    copy "Guiones-para-filmar.pdf" "D:\METODO FLOW 2026\Guiones-para-filmar.pdf"
    echo   [✓] Guiones-para-filmar.pdf
)

if exist "Guiones-vendedor-6-7-8.pdf" (
    copy "Guiones-vendedor-6-7-8.pdf" "D:\METODO FLOW 2026\Guiones-vendedor-6-7-8.pdf"
    echo   [✓] Guiones-vendedor-6-7-8.pdf
)

if exist "Cuadernillo-Mes1-El-Mapa.pdf" (
    copy "Cuadernillo-Mes1-El-Mapa.pdf" "D:\METODO FLOW 2026\Cuadernillo-Mes1-El-Mapa.pdf"
    echo   [✓] Cuadernillo-Mes1-El-Mapa.pdf
)

if exist "Cuadernillo-Expresividad-Sabor.pdf" (
    copy "Cuadernillo-Expresividad-Sabor.pdf" "D:\METODO FLOW 2026\Cuadernillo-Expresividad-Sabor.pdf"
    echo   [✓] Cuadernillo-Expresividad-Sabor.pdf
)

if exist "Cuadernillo-Mes3-El-Vocabulario.pdf" (
    copy "Cuadernillo-Mes3-El-Vocabulario.pdf" "D:\METODO FLOW 2026\Cuadernillo-Mes3-El-Vocabulario.pdf"
    echo   [✓] Cuadernillo-Mes3-El-Vocabulario.pdf
)

echo.
echo ========================================
echo ✓ SINCRONIZACIÓN COMPLETADA
echo ========================================
echo.
echo Archivos en: D:\METODO FLOW 2026\
echo.
pause
