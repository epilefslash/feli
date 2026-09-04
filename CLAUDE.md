# Método FLOW — Solo con Sabor (contexto del proyecto)

> Programa de guitarra de Nico Galliussi (mentor) aplicado por Feli (alumno/profesor que enseña con
> este método). Objetivo: pasar de clases 1 a 1 a un programa grupal online — improvisación en rock
> sobre pentatónica menor "con sabor", en 12 semanas (3 hitos + bonus post-programa).

**Quién es quién:** Feli = el usuario de esta sesión, alumno de Nico y quien da el programa. Nico Galliussi
= el mentor, no está en la conversación. **No confundirlos.**

**Repo:** epilefslash/feli · branch `claude/music-teacher-workflow-rHifB`.

Este archivo es el índice. La memoria completa del proyecto está partida en `memoria/`, un archivo por
tema — se carga automáticamente al abrir el repo. Si buscás algo puntual, andá directo al archivo que
corresponda en vez de releer todo.

## Índice de memoria

@memoria/00-resumen-y-estado.md
@memoria/01-avatar-y-oferta.md
@memoria/02-principios-nico-y-delivery.md
@memoria/03-formatos-y-creencias.md
@memoria/04-guiones-videos.md
@memoria/05-contenido-embudo-copy.md
@memoria/06-programa-semanal-y-clase.md
@memoria/07-simulacion-y-proximos-pasos.md
@memoria/08-repertorio-solos.md
@memoria/09-evaluacion-pedagogica.md
@memoria/10-notas-tecnicas-asistente.md

| Archivo | Para qué sirve |
|---|---|
| `00-resumen-y-estado.md` | **Leer primero.** Estado actual, decisiones tomadas, prioridad declarada. |
| `01-avatar-y-oferta.md` | A quién le vendemos, promesa, la oferta completa armada. |
| `02-principios-nico-y-delivery.md` | Por qué programa grupal (no clases sueltas), y el modelo de delivery actual (pregrabado + vivo liviano, caso Sergio Assat). |
| `03-formatos-y-creencias.md` | Los 3 formatos de contenido (A/B/C) y el banco de creencias limitantes para reels. |
| `04-guiones-videos.md` | Guiones completos de todos los videos, filmados y por filmar. |
| `05-contenido-embudo-copy.md` | Orden de publicación, bio/destacadas, copy maestro, carruseles. |
| `06-programa-semanal-y-clase.md` | Qué se enseña cada una de las 12 semanas + mecánica de la clase en vivo. |
| `07-simulacion-y-proximos-pasos.md` | Simulación del "después" + lista corta de qué sigue. |
| `08-repertorio-solos.md` | Banco fijo de 4 solos de referencia + piezas de color opcionales. |
| `09-evaluacion-pedagogica.md` | Auditoría del programa terminado y el ajuste de Hito 2 que salió de ahí. |
| `10-notas-tecnicas-asistente.md` | Notas operativas de sesión a sesión (repo, quién es quién, qué métrica importa). |

## Dónde está cada cosa (fuera de memoria/)

- **Cuadernillos de ejercicios (PDF, para el alumno):** `Cuadernillo-Hito1-El-Mapa-EJERCICIOS.pdf`,
  `Cuadernillo-Hito2-El-Sabor-EJERCICIOS.pdf`, `Cuadernillo-Hito3-El-Vocabulario-EJERCICIOS.pdf`,
  `Cuadernillo-BONUS-Licks-Fuera-de-la-Caja1.pdf`.
- **Anexo de ritmo (PDF, va en paralelo al Hito 3):** `Anexo-Ritmo-y-Construccion-de-Frases.pdf`
  — el árbol de las figuras + la misma celda en negras/corcheas/semicorcheas + tresillo y swing +
  síncopa, anticipación (el *push*) y el puntillo. Sus ejercicios se numeran **con letras (A a J)**
  justamente para no tocar la numeración 1-59.
- **Guiones de video (PDF):** `Guiones-Historia-Fijado-Vendedores.pdf`,
  `Guiones-Pregrabado-Hito1-El-Mapa.pdf`.
- **Documentos de síntesis (PDF):** `Resumen-Ejecutivo-para-Nico.pdf` (para la mentoría),
  `Fundamentacion-Pedagogica-Metodo-Flow.pdf` (el porqué de cada decisión del programa completo).
- **Generadores (Python/ReportLab/LilyPond):** todo en `scripts/`. Cada cuadernillo tiene su
  `build_*.py` (arma el PDF) y su `gen_scores_*.py` (genera las partituras). `cuadernillo_comun.py`
  tiene los estilos y diagramas compartidos (incluye `MapaCompleto`, `MapaBlueNotes`, `Diagrama`).
- **Auditoría de cajas:** `scripts/auditar_cajas.py` — decodifica cada nota de cada partitura a su
  traste real y reporta qué % de cada hito sale de la ventana de la caja 1 (trastes 5-8). Correrlo de
  nuevo cada vez que se toque una partitura. Referencia sana: Hito 1 ~47% · Hito 2 ~21% · Hito 3 ~47% ·
  Bonus ~73% — si el Hito 3 baja de ~30%, algo se volvió a concentrar en la caja 1 sin querer.
  Con `--tabla` imprime qué traste de cada cuerda es qué nota y de qué caja. **Si hay que escribir
  esa tabla en un briefing para otra sesión, correr el comando y pegar la salida — nunca de memoria**
  (ya pasó: se listó el traste 7 de la 6ª cuerda como nota válida y ahí hay un SI, fuera de escala).

## ⚠️ Lo primero que hay que saber antes de auditar nada

**Los PDF que genero acá NO son los que Feli le entrega al alumno.** Los manda a Claude Design, que hace
una versión maquetada más linda y más larga. **Ese paso redibuja las tablaturas y les mete errores
musicales reales** (verificado: un FA fuera de escala repetido 6 veces en el ej. 47, las llegadas del
ej. 50 todas en caja 1 cuando acá están en 4 cajas distintas). Detalle completo y el chequeo de 30
segundos para detectarlo: `memoria/10-notas-tecnicas-asistente.md`, sección 30.

Consecuencia práctica: si alguien reporta un error, **primero verificar en cuál de las dos versiones
está** — mi fuente puede estar limpia y el entregable roto al mismo tiempo.

## ⚠️ Si una sesión anterior quedó cortada (por límite de créditos o lo que sea)

**Instrucción permanente de Feli:** *"Cuando se restablezca el límite, retomá automáticamente desde el
último estado disponible. Revisá qué tareas quedaron incompletas, verificá los cambios ya realizados y
terminá la implementación sin repetir trabajo ni deshacer avances."*

Traducido a qué hacer, **sin esperar que Feli lo pida de nuevo** — alcanza con que escriba cualquier cosa:

1. `git log --oneline -10` y `git status` — qué se llegó a commitear y qué quedó sin guardar.
2. Leer la última sección de `memoria/10-notas-tecnicas-asistente.md`: ahí se documenta cada ronda de
   trabajo terminada. Si lo último que hay en el log **no** está documentado ahí, esa es la tarea cortada.
3. `python3 scripts/auditar_cajas.py` — si falla, hay una partitura a medio editar.
4. Si había un Workflow corriendo, sus resultados parciales están en el `journal.jsonl` del run
   (`subagents/workflows/<run_id>/`). **Leerlo antes de re-lanzar nada:** puede que la mitad del trabajo
   ya esté hecha y solo falte sintetizarla. Se retoma con `resumeFromRunId` — los agentes que sí
   terminaron se replayean desde cache y no se pagan de nuevo.
5. Terminar lo que faltaba y recién ahí avisar. **No volver a empezar desde cero ni deshacer lo hecho.**

> Nota honesta para el asistente: no podés auto-despertarte. Esto se dispara con el primer mensaje que
> mande Feli, sea cual sea. Si alguna vez hace falta arranque sin intervención, es una tarea programada
> (cron), no esta regla.

## Reglas de trabajo en este repo

- El usuario filma y edita él mismo (guitarra, CapCut). Mi rol: guiones, estrategia, copy, pedagogía,
  auditoría de contenido, fact-check — nunca inventar datos musicales que no pueda verificar (transcripciones
  de solos ajenos, por ejemplo) sin decir explícitamente que es una aproximación.
- Métrica que importa en Instagram: comentarios con palabra clave (leads) y guardados. NO los likes.
- Antes de afirmar un número sobre los cuadernillos (páginas, % de cajas, cantidad de ejercicios),
  verificarlo contra el PDF/script real — no contra lo que dice la conversación de memoria. Ya pasó
  que una sesión externa reportó números inventados.
- Balance de ejercicios por hito: 16 (Hito 1) · 18 (Hito 2) · 19 (Hito 3) · 6 (Bonus), numeración
  corrida 1 a 59. Si se agrega o saca contenido, mantener la numeración corrida y actualizar
  `memoria/09-evaluacion-pedagogica.md` con el motivo.
- **Todo lo que Feli suba de Nico Galliussi (o de su equipo) es la biblia del proyecto.** Se le hace
  caso tal cual, no se lo cuestiona ni se lo pesa contra un criterio propio — el trabajo acá es
  cruzarlo contra lo que ya está armado y activarlo, no evaluarlo. Si algo de Nico entra en tensión
  con una decisión previa del proyecto, se documenta la tensión y se resuelve a favor de Nico (o se
  lleva como pregunta a la mentoría si hace falta que él la desempate), nunca se descarta su material
  por preferencia propia.
