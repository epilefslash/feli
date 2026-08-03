# Contexto para arrancar una sesión nueva — Método FLOW / "Solo con Sabor"

> Pegá este archivo entero al abrir la conversación nueva, o subilo, y decí:
> *"Este es el contexto del proyecto, seguimos desde acá."* Si la sesión tiene acceso a esta carpeta
> o al repo (`epilefslash/feli`, branch `claude/music-teacher-workflow-rHifB`), pedile que abra
> `CLAUDE.md` primero — ahí está el índice completo y linkeado a todo lo demás.

---

## Quién es quién (no confundir)

- **Feli** = el usuario, alumno de Nico, y el que da el programa a sus propios alumnos.
- **Nico Galliussi** = el mentor del método. No participa en la conversación.

## El proyecto en 3 líneas

Método FLOW: programa grupal online de 12 semanas para guitarristas hobbistas (rock/blues), que pasan
de "sé la pentatónica caja 1 y sueno escolar" a "improviso un solo con sabor, moviéndome por las 5
cajas". Nombre provisorio: **"Solo con Sabor"**. Se vende antes de tener el delivery en vivo armado del
todo — la prioridad actual es contenido de Instagram + los 3 cuadernillos de ejercicios, que ya están
terminados y auditados.

## Estado ahora mismo (lo importante)

- **Los 3 cuadernillos de ejercicios + el bonus están TERMINADOS**, con 59 ejercicios numerados
  corridos (16 · 18 · 19 · 6), partitura real + tablatura, y auditados con una herramienta propia
  (`scripts/auditar_cajas.py`) que verifica en qué traste cae cada nota — no es una estimación.
- Ya se hicieron **varias pasadas de revisión pedagógica** sobre el balance de cajas (que el programa
  realmente cumpla la promesa de "moverte por las 5 cajas", no solo decirlo). El detalle completo de
  cada decisión y su porqué está en `Fundamentacion-Pedagogica-Metodo-Flow.pdf` y en
  `memoria/09-evaluacion-pedagogica.md`.
- **Próximo paso declarado por Feli:** dejar de tocar los cuadernillos por unas semanas y volver a
  filmar. Faltan: video #9 ("3 formas de romper las cajas", ya con tomas elegidas, en edición), el
  video de "Tu Historia", el "Reel Fijado", y uno de los dos guiones "Vendedor". Después de eso,
  arrancar a grabar las clases pregrabadas del programa (el guion del Hito 1 ya está escrito en
  `Guiones-Pregrabado-Hito1-El-Mapa.pdf`; Hito 2 y 3 quedan pendientes, pero van a salir rápido porque
  cada ejercicio del cuadernillo ya tiene su explicación redactada — es más leer que inventar).

## Cómo está organizada la carpeta

```
CLAUDE.md                    ← EMPEZAR ACÁ. Índice completo, conecta todo lo de memoria/.
memoria/                     ← 11 archivos, uno por tema (avatar, oferta, guiones, programa semanal,
                                repertorio, evaluación pedagógica, notas técnicas, etc.)

Cuadernillo-Hito1-El-Mapa-EJERCICIOS.pdf              ← ejercicios 1-16, con partitura+TAB
Cuadernillo-Hito2-El-Sabor-EJERCICIOS.pdf             ← ejercicios 17-34
Cuadernillo-Hito3-El-Vocabulario-EJERCICIOS.pdf       ← ejercicios 35-53
Cuadernillo-BONUS-Licks-Fuera-de-la-Caja1.pdf         ← ejercicios 54-59, post-programa

Guiones-Historia-Fijado-Vendedores.pdf                ← guiones de los próximos videos a filmar
Guiones-Pregrabado-Hito1-El-Mapa.pdf                  ← guion de las 3 clases pregrabadas del Hito 1

Resumen-Ejecutivo-para-Nico.pdf                       ← para la mentoría: todo lo decidido y producido
Fundamentacion-Pedagogica-Metodo-Flow.pdf             ← el "porqué" de cada decisión del programa

scripts/                     ← generadores Python/ReportLab/LilyPond de todos los PDFs de arriba.
                                build_*.py arma el PDF, gen_scores_*.py genera las partituras.
                                auditar_cajas.py = la herramienta de verificación de cajas.

archivo-viejo/                ← versiones previas ya reemplazadas (conceptuales, cortas). No se usan
                                más, se guardan solo por historial. No hace falta abrirlas.
```

## Reglas de trabajo que ya están validadas (no las reinventes)

1. **No inventar datos musicales sin decirlo.** Si hay que citar una transcripción de un solo ajeno y
   no se puede verificar nota por nota, decirlo explícitamente ("no puedo confirmarte esto sin
   transcribirlo"). Ya pasó que una sesión externa reportó números de páginas inventados — desconfiar
   de cualquier cifra que no salga de correr el script o abrir el PDF real.
2. **Verificar antes de afirmar.** Antes de decir un % de cajas, cantidad de páginas o de ejercicios,
   correr `python scripts/auditar_cajas.py` o abrir el PDF — no repetir un número de la conversación
   sin chequearlo contra el archivo actual.
3. **Numeración corrida.** Los 59 ejercicios van del 1 al 59 sin saltos. Si se agrega o saca contenido,
   hay que mantener la numeración y actualizar `memoria/09-evaluacion-pedagogica.md` con el motivo.
4. **Métrica que importa en Instagram:** comentarios con palabra clave (leads) y guardados. NO los likes.

## Qué pedirle a la sesión nueva, según lo que necesites

- Si es para seguir con **contenido de Instagram / guiones**: que lea `memoria/04-guiones-videos.md`
  y `memoria/03-formatos-y-creencias.md`.
- Si es para **retocar algo pedagógico de los cuadernillos**: que lea `memoria/09-evaluacion-pedagogica.md`
  y corra `scripts/auditar_cajas.py` ANTES de tocar nada, para tener la referencia real.
- Si es para **preparar la mentoría con Nico**: `Resumen-Ejecutivo-para-Nico.pdf` +
  `memoria/00-resumen-y-estado.md`.
- Si es para **grabar las clases pregrabadas de Hito 2 o 3**: usar de modelo
  `Guiones-Pregrabado-Hito1-El-Mapa.pdf` (mismo formato, minutado, tono) y basarse en los cuadernillos
  de ejercicios ya escritos.
