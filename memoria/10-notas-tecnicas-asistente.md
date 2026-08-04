<!-- Parte de la memoria del proyecto. Ver /CLAUDE.md en la raíz del repo para el índice completo. -->

# Notas técnicas para el asistente

> Contexto operativo de sesión a sesión: repo, quién es el usuario, qué métricas importan.

---

## 15) NOTAS DE CONTEXTO TÉCNICO (para mí, el asistente, en sesiones futuras)
- Repo: epilefslash/feli, branch `claude/music-teacher-workflow-rHifB`. PR #4 ya existe (no crear otro).
- El usuario = Feli. Habla español rioplatense. NO confundir Feli con Nico.
- El usuario filma y edita él mismo (guitarra, CapCut). Mi rol: guiones, estrategia, copy, pedagogía,
  auditoría de contenido, fact-check.
- Métrica que importa: comentarios con palabra clave (leads) y guardados. NO los likes.

## 30) ⚠️ EL FLUJO DE DISEÑO — LOS PDF QUE ENTREGA FELI NO SON LOS QUE GENERO YO

**Esto es lo más importante de esta sección.** Los cuadernillos que salen de `scripts/build_*.py` NO son
los que Feli le entrega al alumno: los manda a **Claude Design**, que hace una versión maquetada más
linda (y más larga — 30/32/51/19 páginas contra las 11/13/20/8 mías). Ese paso es el que llega al alumno.

**El problema verificado (3/8/2026):** Design **redibuja las tablaturas en vez de embeber mis imágenes**,
y al transcribirlas introduce errores musicales reales. Encontrados en la versión diseñada del Hito 3:

| Ejercicio | Mi fuente (correcta) | Versión diseñada (rota) |
|---|---|---|
| 47 | 1ª cuerda 12→10 (MI) | 1ª cuerda **13**→10 = **FA, fuera de la pentatónica, 6 veces** |
| 50 (el esqueleto) | Llegadas 7 · 10 · 12 · 5 | Llegadas 5 · 7 · 7 — **todas en caja 1** |
| 49 | "Desarrolla" en caja 2 (8-10) | "Desarrolla" en caja 1 (5-7) |
| 48 | 15 notas | Falta casi todo el 2º compás |

**La firma del problema:** el TEXTO de la versión diseñada está actualizado (el ej. 50 dice "caja 1,
caja 2, caja 3 y caja 5") pero la TABLATURA de abajo es vieja o mal transcrita. Si texto y música no
coinciden, es que se redibujó.

**La instrucción para Design:** *"las imágenes de partitura/tablatura se insertan tal cual, sin
redibujar ni re-tipografiar. Podés cambiar tamaño y posición, nunca el contenido."*

**Chequeo rápido antes de entregar cualquier cuadernillo:** abrir el ej. 50 y verificar que las cuatro
llegadas digan **7, 10, 12, 5**. Si dicen 5-7-7, la tablatura se redibujó y hay que revisar el archivo
entero.

**Consecuencia para auditorías externas:** si otra sesión audita los PDF de `D:\METODO FLOW 2026` va a
encontrar errores que NO existen en el repo. Ambas cosas pueden ser ciertas a la vez — mi fuente limpia
y el entregable roto. Antes de "corregir" algo, verificar en cuál de los dos está el problema.

### SEGUNDA RONDA (3/8/2026) — la sesión de Design devolvió una lista de 18 "cambios a aplicar"

Feli le pasó los cuadernillos nuevos a Design y Design devolvió un checklist de 18 ítems (5 críticos,
9 importantes, 4 cosméticos). **Se verificaron uno por uno contra la fuente: los 5 críticos y varios de
los importantes describen errores de la propia versión diseñada, no del repo.** Detalle:

| Ítem de Design | Qué dice | Realidad verificada en la fuente |
|---|---|---|
| 1 · ej. 47 con FA (traste 13) | "1ª cuerda 13 → cambiar a 12" | La fuente **ya dice 12** (`e''\1`). Error de Design. |
| 2 · ej. 50 con las 4 llegadas en caja 1 | "redistribuir a 4 cajas" | La fuente **ya está en 4 cajas**: trastes 7·10·12·5. Error de Design. |
| 6 · ej. 51 con los 3 finales en caja 1 | "reescribir 2 de 3" | La fuente **ya está en 3 cajas**: trastes 5-7 · 12 · 12-13. Error de Design. |
| 7 · ej. 53 no cumple lo que promete | "el bend está en caja 1" | La fuente **ya cumple**: bend en traste 12 (caja 3), cierre en traste 5 de la 6ª (caja 5). Error de Design. |
| 8 · diagramas con puntos de más | "3ª cuerda tr. 9 en caja 1", etc. | Las 5 cajas de `cuadernillo_comun.py` tienen 12 puntos exactos y todos son de la pentatónica. Error de Design. |
| 9 · "Los 5 recursos" (Hito 2) | "el título dice 5, la tabla lista 4" | Ya corregido antes: dice **"LOS 4 BLOQUES DEL MES"**. |
| 10 · "40 solos de Frusciante" | "sacar la cifra inventada" | Ya sacado en una sesión anterior. |
| 3 y 4 · el bonus duplicado / "8 licks" | numeración 52-59 vs 54-59 | En el repo el bonus **ya es 54-59** y el Hito 3 no menciona "8 licks del bonus". El PDF viejo de 8 licks vive solo en la máquina de Feli. |

**Lo que sí era real y se aplicó en esta sesión:**
- `auditar_cajas.py` ahora **valida escala explícitamente**: reporta cualquier nota fuera de la pentatónica
  de La menor y termina con `exit 1`. Probado inyectando el FA del ej. 47 — lo caza. (Antes la validación
  existía implícita: el mapa de trastes es una whitelist, pero fallaba en silencio.)
- Header del script actualizado (decía Hito 2 14% / Hito 3 21%, valores viejos; ahora 21% / 47%).
- `scripts/README.md` decía "51 ejercicios" y "bonus 52-59" → corregido a 53 y 54-59.
- Hito 3: nota al pie **"los nombres son de estilo, no de pasaporte"** (Gary Moore es de Belfast y está
  en la columna americana) — ítem 15 de Design, era válido.
- Hito 3, cierre: sección nueva **"LO QUE ESTE PROGRAMA NO TE DIO"** (ritmo y cambios de acorde) — ítem 16.
  El hueco estaba documentado internamente pero el alumno no lo veía. Ahora sí.
- Hito 1: se sacó el "buscá en YouTube …" y se apunta a la carpeta de backings propios — ítem 13.

**Ítems 11, 12, 18 (espacio en blanco, capa de texto, carpetas):** son del lado de Design / de la máquina
de Feli, no del repo. Los PDF que genero acá tienen capa de texto y 11/13/20/8 páginas.

**Ítem 14 (convertir el puente del Hito 2 en ejercicio numerado):** rechazado a propósito. Ese puente
("ANTES DEL SOLO: ESTO YA TE SIRVE EN LAS 5 CAJAS") es práctica libre de oído sin partitura por diseño —
escribirlo en TAB lo convierte en otra cosa. Además rompería la numeración corrida 1-59.

> **Regla que sale de todo esto:** cuando una sesión externa reporte un error musical, **primero correr
> `python3 scripts/auditar_cajas.py` y leer la fuente LilyPond**. Hasta ahora, casi todos los errores
> musicales reportados por Design estaban en la versión de Design — pero ver abajo la excepción.

### TERCERA RONDA — el re-chequeo encontró UN error real: las ventanas de caja se solapan

Design re-auditó y reportó que el ej. 50 pisaba cajas 1, 2 y 3 pero **no la caja 5**, aunque el texto
la promete. **Tenía razón, y la causa es estructural:** las ventanas de las cajas se superponen.

| Traste | Cajas a las que pertenece |
|---|---|
| 5 | **caja 1 y caja 5** |
| 12 y 13 | **caja 3 y caja 4** |

El ej. 50 cerraba en el traste 5 de la 6ª cuerda. Eso es la tónica grave, y técnicamente está dentro
de la caja 5 — pero también dentro de la caja 1, así que **no prueba nada**: leyendo la tablatura no
se puede saber si el alumno bajó a la caja 5 o se quedó en casa. Lo mismo pasaba en el ej. 53 (mismo
cierre) y en el ej. 51, donde el 3er final caía en trastes 12-13, ambiguo entre cajas 3 y 4 — o sea
indistinguible del 2º final.

**Los 3 arreglos aplicados:**
- **Ej. 50 y 53:** el último compás ahora baja primero al **traste 3** (SOL, exclusivo de la caja 5) y
  recién después resuelve en la tónica del traste 5. Un solo gesto de dos notas y la caja 5 queda
  probada, sin perder el cierre en la tónica grave.
- **Ej. 51:** el 3er final se mudó del traste 12-13 al **traste 15** (doble cuerda RE + SOL), exclusivo
  de la caja 4. Ahora los tres finales están en 5-7 · 12 · 15 — inconfundibles entre sí.
- Los textos de los ej. 50 y 51 ahora **nombran los trastes**, no sólo las cajas. Doble beneficio: la
  promesa es verificable, y si Design redibuja, el texto y la tablatura se contradicen a la vista.

**Y el arreglo de fondo, en `auditar_cajas.py`:** columna nueva **`exclusivas`**, que lista sólo las
cajas pisadas en trastes que no comparte ninguna otra. Es la métrica que faltaba: `cajas` puede decir
`[1,2,3,4,5]` con el ejercicio entero metido en la caja 1.

> ⚠️ **Al leer la columna `exclusivas`, las cajas 2 y 3 NUNCA aparecen, y no es un bug.** Sus trastes
> exclusivos son el 6 y el 11, y ahí no hay ninguna nota de la pentatónica de La menor. La columna
> sirve para las cajas 1, 4 y 5. No perseguir un imposible en una sesión futura.

**Lo que Design reportó como "sin tocar" (bonus duplicado, "8 licks", "los 5 recursos", Frusciante):**
sigue siendo lo mismo de la segunda ronda — en el repo ya está bien; lo que está desactualizado son
los PDF maquetados que viven en la máquina de Feli. Se resuelve re-mandando los 4 archivos a Design,
no editando la fuente.

### CUARTA RONDA (4/8/2026) — Design maquetó bien, y el error esta vez fue MÍO

La sesión externa auditó el PDF maquetado del Hito 3 (48 páginas) extrayendo las tablaturas como
vectores, no a ojo. **Los tres arreglos de la tercera ronda sobrevivieron a la remaquetación:**

| Verificación | Resultado en el PDF de Design |
|---|---|
| Ej. 50 · llegadas 7·10·12·5 + traste 3 antes del cierre | ✅ 4ª/7 · 2ª/10 · 3ª/12 · 6ª/3→5 |
| Ej. 51 · tercer final en traste 15 (RE + SOL) | ✅ 1ª/15 + 2ª/15 |
| Ej. 53 · último compás 3→5 en la 6ª | ✅ y el bend del clímax en 3ª/12 |
| Los textos nombran trastes y coinciden con la música | ✅ los dos |
| Sin regresiones (ej. 47 en 12, ej. 46 en las 5 cajas, diagramas de 12 puntos) | ✅ |

**El único error real de la ronda estuvo en el briefing que escribí yo.** La tabla de referencia
decía *"traste 7 = SI (caja 1 y 2)"* para la 6ª cuerda, y abajo aclaraba que lo que no estuviera en
la lista era nota fuera de escala. **SI no pertenece a la pentatónica de La menor.** El traste 7 sí
es LA — pero en la **4ª** cuerda, que es donde está la llegada 1 del ej. 50. Confundí una cuerda con
otra. No afectó a ningún cuadernillo (la fuente estaba bien), pero una tabla así aprueba una nota
mala en la ronda siguiente.

**Arreglo de fondo:** `auditar_cajas.py --tabla` ahora imprime la tabla completa cuerda por cuerda,
generada desde el mismo `MAPA` que usa la auditoría. **Nunca más escribir esa tabla de memoria en un
briefing: correr el comando y pegar la salida.** La 6ª cuerda es 3·5·8·10·12·15 — el 7 no está.

**Los 4 "pendientes" que reportó la sesión, verificados contra la fuente:** los cuatro son de los PDF
que viven en la máquina de Feli, no del repo.

| Reporte | Realidad en la fuente |
|---|---|
| "Los 5 recursos" (Hito 2) sigue diciendo 5 y lista 4 | `build_hito2.py` dice **"LOS 4 BLOQUES DEL MES"**. PDF viejo. |
| "Las 8 semanas del bonus… los 8 licks" (Hito 3, última pág.) | En la fuente **no existe esa frase**. Los dos "8 licks" que hay (líneas 502 y 530) son la meta de licks propios del alumno, no el bonus — la propia sesión lo reconoce en su punto 5. La única mención al bonus en el Hito 3 es "ej. 54, el BB box". |
| "40 solos de Frusciante" sin fuente | **No existe ninguna cifra** en la fuente: las 3 menciones a Frusciante no llevan número. Ya se había sacado. |
| Bonus duplicado (`liks fuera de la box 1.pdf`, numerado 52-59) | Archivo viejo en la máquina de Feli. En el repo el bonus es 54-59 y la tapa dice 6 licks. |

> **Acción para Feli, no para el repo:** borrar de `D:\METODO FLOW 2026` los PDF viejos (el bonus
> numerado 52-59 y cualquier Hito 2 anterior al 3/8) y re-mandar los 4 archivos actuales. Mientras
> los dos juegos convivan en la misma carpeta, cada auditoría externa va a seguir reportando estos
> mismos cuatro fantasmas.

## 31) MATERIAL QUE FELI PRODUCE APARTE (no está en este repo)

- **Módulo de ritmo del Hito 2** (`Cuadernillo_ritmo_hito_2_Sabor_2_ejercicios.pdf`, 19 pág.): cierra el
  hueco de ritmo que estaba documentado como pendiente para el Módulo 2. Corre **en paralelo** al Hito 2
  (no reemplaza semanas), 10 células rítmicas, 0 notas nuevas, entregable de 1 min. Basado en **Pozzoli**
  (*Guía Teórico-Práctica para la Enseñanza del Dictado Musical*) con página y serie citadas — fuente real
  y verificable. Usa palabras mnemotécnicas (PEZ · PA-TO · CHO-CO-LA-TE · PI-CAN-TE) para las células.
  Cita correctamente el ej. 42 del Hito 3 ("el ritmo es el 70% de la identidad de una frase").
- **Las "Guías del Profe"** (3 documentos) y una carpeta de **backing tracks propios**: existen en la
  máquina de Feli, no en el repo. Una auditoría externa las evaluó bien.

## 32) ANEXO DE RITMO — el árbol de las figuras y las 3 velocidades (4/8/2026)

`Anexo-Ritmo-El-Arbol-y-las-3-Velocidades.pdf` (4 pág.) · `scripts/gen_scores_ritmo.py` + `build_ritmo.py`.
Pedido de Feli, complementa el módulo de ritmo de Pozzoli de la sección 31 (que sigue viviendo en su
máquina). **Va en paralelo al Hito 2 y sus ejercicios se numeran A · B · C**, para no romper la
numeración corrida 1-59.

**El dato que lo justifica, contado sobre la fuente (no sobre la conversación):** de las **395 notas**
de los 4 cuadernillos → corchea 50% · negra 28% · blanca 13% · redonda 8% · **una sola semicorchea** ·
**cero fusas** · 32 tresillos (sólo en Hitos 2 y 3). El alumno termina el programa con un vocabulario
rítmico de dos figuras. El conteo se rehace con una línea de Python sobre los `EJ` de cada
`gen_scores*.py` — si se agregan ejercicios, volver a correrlo antes de repetir el número.

**Qué tiene, y las 3 decisiones de diseño que importan:**
1. **El árbol** (`ArbolFiguras`, en `cuadernillo_comun.py`): redonda → 2 blancas → 4 negras → 8 corcheas
   → 16 semicorcheas, con las líneas de parentesco dibujadas. El punto NO es memorizar duraciones: es
   que **las cinco filas duran lo mismo** y bajar un escalón es partir la figura al medio, no "ir más
   rápido".
2. **Las 3 velocidades (ej. A):** la misma celda (8-5-8-5, caja 1) en negras, corcheas y semicorcheas.
   Se presenta como cambio de **función**, no de velocidad — negras = frase, corcheas = comentario,
   semicorcheas = adorno. Es el mismo truco del ej. 46 del Hito 3 (un lick en las 5 cajas) en el otro
   eje: aquel probaba que un lick no es un lugar, éste que tampoco es una velocidad.
3. **La regla que protege al Hito 2** — y es lo más importante del anexo:
   > *Comprimir un lick no te ahorra tiempo: te regala silencio.*
   Sin esa regla, el ejercicio se convierte en un drill de velocidad en tres días y contradice todo
   lo que el Hito 2 enseñó sobre espacio (y el reel #6). Los silencios están **escritos** en la
   partitura a propósito: son el contenido, no relleno. La escalera de práctica insiste en que **el
   BPM no se toca** en ningún paso.

**Tresillo y swing van en bloques SEPARADOS del árbol, a propósito.** Son otro eje: el árbol dice *qué
figura* usás (divide por 2), el tresillo divide por 3 y el swing dice *dónde cae* la segunda corchea
dentro del pulso. Mezclarlos en un mismo ejercicio confunde. El swing va escrito (negra + corchea en
tresillo) para que se vea de dónde sale.

> Este anexo **no cierra** el hueco de cambios de acorde (sigue pendiente para el Módulo 2). Cierra el
> de ritmo, junto con el módulo de Pozzoli.
