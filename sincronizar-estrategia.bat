@echo off
REM Script para sincronizar CLAUDE.md + memoria/ + los PDFs del proyecto a D:\METODO FLOW 2026
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

REM Copiar archivo principal (CLAUDE.md + memoria/, reemplaza a Estrategia-FLOW-guitarra-base.md)
echo [3/3] Copiando archivos...

copy "CLAUDE.md" "D:\METODO FLOW 2026\CLAUDE.md"
if errorlevel 1 (
    echo ERROR: No se pudo copiar CLAUDE.md.
    pause
    exit /b 1
)
echo   [✓] CLAUDE.md

if exist "memoria" (
    if not exist "D:\METODO FLOW 2026\memoria" mkdir "D:\METODO FLOW 2026\memoria"
    copy "memoria\*.md" "D:\METODO FLOW 2026\memoria\" >nul
    echo   [✓] memoria\ (carpeta completa)
)

if exist "CONTEXTO-PARA-NUEVA-SESION.md" (
    copy "CONTEXTO-PARA-NUEVA-SESION.md" "D:\METODO FLOW 2026\CONTEXTO-PARA-NUEVA-SESION.md" >nul
    echo   [✓] CONTEXTO-PARA-NUEVA-SESION.md
)

REM Se conserva por compatibilidad / historial - la memoria activa ya esta en memoria/
if exist "Estrategia-FLOW-guitarra-base.md" (
    copy "Estrategia-FLOW-guitarra-base.md" "D:\METODO FLOW 2026\Estrategia-FLOW-guitarra-base.md" >nul
    echo   [✓] Estrategia-FLOW-guitarra-base.md (archivo historico)
)

REM Copiar archivos auxiliares si existen
if exist "Carruseles-para-disenar.md" (
    copy "Carruseles-para-disenar.md" "D:\METODO FLOW 2026\Carruseles-para-disenar.md"
    echo   [✓] Carruseles-para-disenar.md
)

if exist "Cuadernillo-Hito1-El-Mapa-EJERCICIOS.pdf" (
    copy "Cuadernillo-Hito1-El-Mapa-EJERCICIOS.pdf" "D:\METODO FLOW 2026\Cuadernillo-Hito1-El-Mapa-EJERCICIOS.pdf"
    echo   [✓] Cuadernillo-Hito1-El-Mapa-EJERCICIOS.pdf
)

if exist "Cuadernillo-Hito2-El-Sabor-EJERCICIOS.pdf" (
    copy "Cuadernillo-Hito2-El-Sabor-EJERCICIOS.pdf" "D:\METODO FLOW 2026\Cuadernillo-Hito2-El-Sabor-EJERCICIOS.pdf"
    echo   [✓] Cuadernillo-Hito2-El-Sabor-EJERCICIOS.pdf
)

if exist "Cuadernillo-Hito3-El-Vocabulario-EJERCICIOS.pdf" (
    copy "Cuadernillo-Hito3-El-Vocabulario-EJERCICIOS.pdf" "D:\METODO FLOW 2026\Cuadernillo-Hito3-El-Vocabulario-EJERCICIOS.pdf"
    echo   [✓] Cuadernillo-Hito3-El-Vocabulario-EJERCICIOS.pdf
)

if exist "Cuadernillo-BONUS-Licks-Fuera-de-la-Caja1.pdf" (
    copy "Cuadernillo-BONUS-Licks-Fuera-de-la-Caja1.pdf" "D:\METODO FLOW 2026\Cuadernillo-BONUS-Licks-Fuera-de-la-Caja1.pdf"
    echo   [✓] Cuadernillo-BONUS-Licks-Fuera-de-la-Caja1.pdf
)

if exist "Guiones-Historia-Fijado-Vendedores.pdf" (
    copy "Guiones-Historia-Fijado-Vendedores.pdf" "D:\METODO FLOW 2026\Guiones-Historia-Fijado-Vendedores.pdf"
    echo   [✓] Guiones-Historia-Fijado-Vendedores.pdf
)

if exist "Resumen-Ejecutivo-para-Nico.pdf" (
    copy "Resumen-Ejecutivo-para-Nico.pdf" "D:\METODO FLOW 2026\Resumen-Ejecutivo-para-Nico.pdf"
    echo   [✓] Resumen-Ejecutivo-para-Nico.pdf
)

if exist "Fundamentacion-Pedagogica-Metodo-Flow.pdf" (
    copy "Fundamentacion-Pedagogica-Metodo-Flow.pdf" "D:\METODO FLOW 2026\Fundamentacion-Pedagogica-Metodo-Flow.pdf"
    echo   [✓] Fundamentacion-Pedagogica-Metodo-Flow.pdf
)

if exist "Guiones-Pregrabado-Hito1-El-Mapa.pdf" (
    copy "Guiones-Pregrabado-Hito1-El-Mapa.pdf" "D:\METODO FLOW 2026\Guiones-Pregrabado-Hito1-El-Mapa.pdf"
    echo   [✓] Guiones-Pregrabado-Hito1-El-Mapa.pdf
)


echo.
echo ========================================
echo ✓ SINCRONIZACIÓN COMPLETADA
echo ========================================
echo.
echo Archivos en: D:\METODO FLOW 2026\
echo.
pause
