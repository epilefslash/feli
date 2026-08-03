# Prompt para Claude Design — maquetar los cuadernillos

> Copiá y pegá esto junto con el PDF cada vez que le mandes un cuadernillo a diseñar.
> Existe porque en la versión anterior se detectaron errores musicales reales introducidos
> al re-dibujar las tablaturas (ver el final del archivo).

---

## PROMPT (copiar desde acá)

Te paso un cuadernillo de ejercicios de guitarra para que lo maquetes con mejor diseño.

**REGLA NÚMERO 1, INNEGOCIABLE — LAS PARTITURAS Y TABLATURAS NO SE TOCAN.**

Cada bloque de partitura + tablatura de este PDF es una **imagen generada automáticamente** con
LilyPond a partir de código musical verificado nota por nota. Son datos, no ilustraciones.

Con esas imágenes podés:
- ✅ Cambiarlas de tamaño (manteniendo la proporción)
- ✅ Moverlas de lugar en la página
- ✅ Ponerles un marco, un fondo, un número de ejercicio al lado

Con esas imágenes NO podés, bajo ningún concepto:
- ❌ Volver a dibujarlas
- ❌ Re-tipografiarlas o "pasarlas en limpio"
- ❌ Reconstruirlas a partir de lo que dice el texto
- ❌ Cambiar un solo número de traste, ni agregar o sacar una sola nota
- ❌ Recortarlas, ni dejar compases afuera

**Por qué:** un número de traste mal copiado es una nota equivocada. En la versión anterior, un
`12` se convirtió en `13` y eso puso una nota que no pertenece a la escala del curso, repetida seis
veces, en un ejercicio que el alumno tiene que memorizar. No es un detalle estético: es un error
musical que el alumno va a aprender mal.

**Si una imagen de partitura no entra bien en la página:** achicala, o dale su propia página, o
reacomodá el texto alrededor. Nunca la redibujes para que entre.

---

**REGLA 2 — No se pierde ningún ejercicio ni ningún compás.**

Antes de entregar, contá: el PDF original tiene N ejercicios numerados. El tuyo tiene que tener los
mismos N, cada uno con su partitura completa. En la versión anterior hubo un ejercicio que quedó
**sin partitura** (solo el título y la página en blanco) y otro al que le faltaba **medio compás**.

---

**REGLA 3 — El texto se puede mejorar visualmente, pero no reescribir.**

Podés cambiar tipografías, jerarquías, colores, poner recuadros y destacados. No cambies las
palabras, y sobre todo **no cambies ningún número que aparezca en el texto** (trastes, BPM, números
de ejercicio, números de caja). El texto y la tablatura tienen que decir lo mismo.

---

**REGLA 4 — Aprovechá la página.**

En la versión anterior quedó mucho espacio vacío: el contenido cortaba cerca del 60% de la altura y
abajo quedaba un hueco grande, con varias páginas al 90% en blanco. Preferimos menos páginas y mejor
usadas. Si un ejercicio entra completo en media página, que la otra media la use el siguiente.

---

**REGLA 5 — El PDF final tiene que tener capa de texto.**

Que se pueda buscar con Ctrl+F y copiar. Exportá como PDF con texto real, no como imágenes de página.
(Las partituras sí van como imagen — eso está bien y es lo correcto. El resto no.)

---

## CHECKLIST antes de darlo por terminado

Marcá estas cinco cosas mirando el PDF que generaste:

1. ☐ **Ejercicio 50** (Hito 3, "El esqueleto"): las cuatro llegadas dicen **7 · 10 · 12 · 5**.
   Si dicen 5-7-7 o cualquier otra cosa, redibujaste la tablatura → volvé a empezar.
2. ☐ **Ejercicio 47** (Hito 3): la primera cuerda dice **12 → 10** (no 13).
3. ☐ **Ejercicio 51** (Hito 3, "los tres finales"): los tres finales están en trastes distintos —
   el 1º alrededor del 5-7, el 2º en el **12**, el 3º en el **12-13**. Si los tres caen entre 5 y 8,
   redibujaste.
4. ☐ **Ejercicio 53** (el solo final): el bending del clímax está en el traste **12** de la 3ª cuerda,
   y la última nota es el traste **5** de la 6ª cuerda.
5. ☐ **Diagramas de mástil:** cada caja tiene exactamente **12 puntos** (2 por cuerda). Si alguna
   cuerda tiene 3, agregaste un punto que no existe.
6. ☐ Todos los ejercicios numerados del original están, y todos tienen su partitura.
7. ☐ Ningún ejercicio quedó con la partitura cortada o con compases de menos.
8. ☐ El PDF se puede buscar con Ctrl+F.

---

## (Fin del prompt — lo de abajo es para vos, no para Design)

### Qué pasó exactamente la vez anterior

Verificado comparando la versión diseñada del Hito 3 contra la fuente:

| Ejercicio | Fuente (correcto) | Versión diseñada (roto) |
|---|---|---|
| 47 | 1ª cuerda 12→10 = MI | 1ª cuerda **13**→10 = **FA, fuera de la pentatónica**, 6 veces |
| 50 | Llegadas 7 · 10 · 12 · 5 (4 cajas) | Llegadas 5 · 7 · 7 → **todas en caja 1** |
| 49 | "Desarrolla" en caja 2 (trastes 8-10) | "Desarrolla" en caja 1 (trastes 5-7) |
| 48 | 15 notas | Falta casi todo el 2º compás |

**Cómo se detecta rápido:** si el *texto* de un ejercicio menciona cajas o trastes que la *tablatura*
de abajo no muestra, la tablatura se redibujó. En el ej. 50 el texto decía "caja 1, caja 2, caja 3 y
caja 5" con las cuatro llegadas dibujadas en caja 1 — texto nuevo, música vieja.

**El chequeo de 30 segundos:** abrí el ej. 50 y mirá los cuatro números. 7, 10, 12, 5 → está bien.
Cualquier otra cosa → revisá el archivo entero antes de mandarlo.
