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
  ⚠️ **Cita mal el ejercicio:** dice ej. 42, y "el ritmo es el 70% de la identidad de una frase" está en
  el **ej. 44** (verificado en `build_hito3.py`). Esta memoria decía antes "cita correctamente el ej. 42",
  o sea que avalaba el error — corregido el 4/8. Hay que arreglarlo en el PDF de Pozzoli, que vive en la
  máquina de Feli.

### Dónde va cada módulo de ritmo (decisión del 4/8)

Había dos documentos de ritmo diciendo los dos "corre en paralelo al Hito 2", los dos con entregable de
1 minuto y los dos cubriendo el puntillo. Una auditoría externa lo detectó y propuso jubilar el de
Pozzoli. **Se resolvió separándolos por mes en vez de descartar uno:**

| | Cuadernillo principal | Ritmo, en paralelo |
|---|---|---|
| **Mes 2 — El Sabor** | El Sabor (ej. 17-34) | **Pozzoli** — enseña a *leer* ritmo |
| **Mes 3 — El Vocabulario** | El Vocabulario (ej. 35-53) | **Anexo A-G** — enseña a *aplicarlo* |

**El anexo se movió al mes 3 por dependencias, no por carga:** (a) su operación es "agarrá un lick que ya
sabés y movelo", y los primeros licks del programa aparecen recién en la semana 6 — al mes 3 el alumno
llega con un banco, al mes 2 con dos; (b) citaba el ej. 44 y el 46, los dos del Hito 3, o sea referencias
a futuro; (c) el ej. 44 es justamente lo que el anexo desarrolla — el 44 muestra tres ritmos terminados,
el anexo entrega la palanca que los produce. Dato lateral: el archivo ya estaba guardado en la carpeta de
hito 3 en la máquina de Feli. No estaba en la carpeta equivocada, tenía el rótulo equivocado.
- **Las "Guías del Profe"** (3 documentos) y una carpeta de **backing tracks propios**: existen en la
  máquina de Feli, no en el repo. Una auditoría externa las evaluó bien.

## 32) ANEXO DE RITMO — el árbol de las figuras y las 3 velocidades (4/8/2026)

`Anexo-Ritmo-y-Construccion-de-Frases.pdf` (13 pág.) · `scripts/gen_scores_ritmo.py` + `build_ritmo.py`.
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

### Bloque de síncopa (ejercicios D a G) — segunda ronda del anexo

Feli volvió con un prompt pidiendo "más variedad rítmica". **El prompt venía con el género equivocado**
(preguntaba por chamamé, chacarera, samba y "peña" — es una plantilla de otro proyecto). Se le marcó y se
contestó sobre rock/blues, que es lo que el programa enseña. La intuición de Feli era correcta; el
diagnóstico del prompt, no.

**La recomendación del prompt era llevar las semicorcheas al 20%. Se rechazó, y el motivo importa:** en
blues-rock la semicorchea no da sabor, da shred — y contradiría el reel #3 ("¿hay que tocar rápido?").
Además, **contar duraciones de nota no mide ritmo**: un solo puede ser 100% corcheas y tener un swing
bárbaro. El 50%/28% mide el esqueleto, no el feel.

**Los gaps reales, medidos sobre la fuente:** de 217 compases, sólo **15 arrancan a contratiempo (7%)**;
hay **8 puntillos** en todo el programa y **los ocho son notas finales sostenidas**, ninguno una figura
rítmica adentro de una frase; y en los 4 cuadernillos hay **18 ligaduras, todas dentro del compás** —
ninguna cruza la barra. Ésos eran los huecos, no la semicorchea.

**Lo que se agregó (4 ejercicios, D a G, sin tocar los hitos):**
- **D — el número y el "y":** UNA sola nota repetida, más el flowable `GrillaDelCompas` (los 8 casilleros
  del compás, oscuros los fuertes). Arranca **sin guitarra**: pie y voz primero. Si hay que digitar algo,
  la atención se va a los dedos y no al lugar del pulso.
- **E — mover una nota, no agregarla:** tres compases, y **el 2 está MAL a propósito** (anticipa y vuelve
  a pegar la nota). Se detecta contando la tablatura: 5 números contra 4. El rótulo "MAL" vive dentro de
  la partitura, no sólo en el texto — si Design la redibuja, se nota.
- **F — el push:** las mismas 7 notas (8-5-8-5-7-5-7) rectas y anticipadas. Es la **primera ligadura del
  repo que cruza una barra de compás**, y el último compás queda con la **tablatura vacía**: ahí cae el 1.
- **G — el puntillo:** compases 1 y 2 suenan igual y sus tablaturas son idénticas (8-5-8), uno con
  ligaduras y otro con puntillos. Encaje con el árbol: el árbol **parte** por la mitad, el puntillo
  **suma** la mitad — por eso no entra en el árbol y por eso sincopa. Cierra con el 3+3+2.

**La regla de blindaje, en su segunda cara:** *sincopar no agrega notas, mueve una — y la síncopa no se
escucha en la nota que tocás, se escucha en el tiempo fuerte que dejaste vacío.* Prueba interna: en todo
el bloque no hay una sola semicorchea, y el compás más sincopado (3+3+2) es el que tiene **menos** notas.

**Los 3 correctores para practicar solo** (el click flaco a la mitad del BPM sonando sólo en 1 y 3 ·
contar en voz alta *mientras* se toca · filmarse el pie) están porque éste es el primer bloque del anexo
que **no se puede practicar sin metrónomo**: una síncopa mal medida suena igual que llegar tarde, y el
error típico —que el pulso se mude y el "y" se vuelva el 1— es invisible desde adentro.

> ⚠️ **Nota de lectura de TAB que hay que dejar dicha:** una nota ligada **no lleva número** en la
> tablatura, porque no se vuelve a puntear. En el ej. F eso deja el compás final en blanco. Es correcto y
> es el punto del ejercicio, pero un alumno que sólo lee TAB lo puede leer como un error de impresión —
> por eso está aclarado en el pie del ejercicio.

**Por qué NO se metió en el Hito 2, que era lo que pedía el prompt:** rompería el balance 16/18/19,
rompería la numeración corrida 1-59, y contradiría el diseño del Hito 2 (tiene la mitad de notas que el
Hito 1 a propósito).

> Este anexo **no cierra** el hueco de cambios de acorde (sigue pendiente para el Módulo 2). Cierra el
> de ritmo, junto con el módulo de Pozzoli.

### QUINTA RONDA (5/8/2026) — la masterclass de fraseo de Ross Campbell

Feli trajo una masterclass de **Ross Campbell** (bulletproofguitarplayer.com) con 3 PDF de tablatura
(*5 Level Phrasing Challenge* · *Subdivision Exercises* · *Repetition*). Los tres en **Do menor**,
♩=115, con copyright explícito al pie. Se auditaron sus **5 niveles** contra el programa.

**Tres de los cinco ya estaban cubiertos, y dos mejor que en su material:**

| Nivel de Ross | Dónde está en lo nuestro |
|---|---|
| 5 · Bookends | **Ej. 52** del Hito 3 — y le da el nombre real (*leitmotiv*) y su origen. |
| 4 · Espacio ("café challenge") | **Ej. 31** del Hito 2 + el checklist, que pide *4 silencios de +2 tiempos por minuto*: una métrica verificable que Ross no tiene. |
| 2 · Ritmo | El árbol del anexo. Sólo faltaba el tresillo de negra. |

> ⚠️ **En la primera lectura reporté el bookend como hueco. Era falso** — se detectó leyendo la fuente
> (`build_hito3.py`), no la memoria. Regla que se confirma: antes de declarar un hueco, `grep` al script.

**Los 4 huecos reales → ejercicios H, I, J del anexo + el tresillo de negra en B.** Detalle completo en
el commit y en el docstring de `gen_scores_ritmo.py`. Lo que más valía de todo el material era una sola
frase suya: **al desplazar el arranque de una frase hay que ajustar el FINAL** (sacar o agregar una
nota). Sin eso el alumno prueba solo, no le cierra el compás y concluye que la síncopa no le sale.

**Dos agregados de texto en los hitos, sin ejercicio nuevo:**
- **Hito 2, ej. 31** — el café como variante *física* de la regla de las 3 notas. Contar es mental y se
  puede hacer mientras seguís tocando; con la taza en la mano no. El silencio deja de ser una decisión.
- **Hito 3, ej. 49** — el arco crecía en 2 variables (altura + velocidad, regla de Brian May). Se suma
  la **tercera: la densidad de silencio baja a medida que el solo crece**.

**Sobre copiar el material:** los conceptos no son de él (están en Pozzoli y en cualquier tratado de
fraseo) y usarlos es libre. Las frases escritas sí, están con copyright y son de un challenge público.
Además la transposición literal Cm→Am sería **peor** para nosotros: no usa nuestras células, no engancha
con el ej. 44 ni el 46. Se tomó la estructura y se escribieron las notas nuestras.

**Lo que Feli reportó y no pude confirmar:** dijo haber visto **fusas** en el EX3 de subdivisión. Los
rótulos explícitos del PDF llegan hasta *16TH NOTES* y su propio resumen de la masterclass lista las
subdivisiones cuatro veces sin mencionar fusas. Sospecha: corchea con puntillo + semicorchea, o
semicorcheas beameadas junto a corcheas. **Queda abierto** — se resuelve contando barras de plica
(1=corchea · 2=semicorchea · 3=fusa). No cambia ninguna decisión: ese ejercicio es el que no copiamos.

> **El anexo vive 98% en la caja 1 y es a propósito** — aislar la variable rítmica, mismo criterio que
> mantiene juntas las 3 versiones de los ej. 44 y 45. Está escrito en el docstring **y en el PDF** para
> que una auditoría externa no lo "arregle". Única excepción: el ej. I, donde mudarse de caja *es* el
> contenido. **Anexo: 4 → 11 páginas, A-G → A-J. La numeración 1-59 no se tocó.**

### SEXTA RONDA (5/8/2026) — notación estándar de guitarra en los 4 cuadernillos

Feli, mirando los PDF de Ross Campbell: *"hay más expresión en sus partituras que en las nuestras"*.
Medido sobre la fuente, **tenía razón — pero el diagnóstico real es otro**: no enseñábamos menos
expresión (el Hito 2 entero es expresión), **no la notábamos**. Escribíamos la técnica en prosa
castellana arriba del pentagrama, y sobre la TABLATURA no aparecía nada: el alumno veía un 7 pelado
con un cartel lejos que decía "bend 1 tono".

**Lo que soporta LilyPond 2.24.3, probado:**

| Recurso | Cómo sale |
|---|---|
| Hammer-on / pull-off | **Nativo**: slur `( )` + `^"H"` / `^"P"`. Dibuja el arco en la tablatura. |
| Slide | **Nativo**: `\glissando`. Ya lo teníamos, faltaba usarlo y rotularlo `sl.` |
| Bending | ⚠️ El `Bend_engraver` **NO** pone flecha sobre el traste (probado con y sin `Glissando_engraver`: dibuja una línea de slide). Se resolvió con markup. |
| Vibrato | `\draw-squiggle-line` — la línea ondulada de siempre. |

**Los helpers nuevos viven en el TEMPLATE de `gen_scores.py`** y los usan los cinco generadores:
`\tabSym` + `\bendFull` · `\bendHalf` · `\bendRel` · `\vib`.

> ⚠️ **`\tabSym` se hace con `\tweak`, NO con `\once \override`, y el motivo importa.** El override
> alcanzaba a *todos* los markups de esa nota, así que cuando había símbolo Y texto en la misma nota
> el texto se duplicaba sobre la tablatura ("dejala morir" aparecía dos veces en el ej. 24). Con
> `\tweak` el símbolo va a los dos pentagramas y la prosa sólo al de arriba. Si alguna vez se ve un
> cartel repetido sobre la TAB, es que alguien volvió al override.

**La regla de redacción que salió de acá, y que vale para cualquier ejercicio nuevo:**
*si la notación ya lo dice, el texto no lo repite.* Salieron "bend 1 tono", "vibrato", "slide",
"traste 9"; se quedaron "escuchá el destino", "blue note", "caés en la tónica de la caja 2" — eso la
notación no lo dice. El ej. 21 es el caso testigo: decía *"escuchá el destino: traste 9"* + *"ahora
bendeá el 7 hasta que suene IGUAL"*, y ahora dice *"1 · escuchá el destino"* con `full ▲` sobre el 7.

**Aplicado a los 4 cuadernillos** (Hito 1 también: Feli lo sospechaba y era cierto — 2 bendings y 6
vibratos en prosa, más 3 slides rotulados "slide" en vez de `sl.`). **El Hito 1 no lleva H ni P a
propósito:** los ligados se enseñan recién en el ej. 17. Y en el Hito 2 hay ligaduras que **no** son
hammer ni pull porque cruzan de cuerda (ej. 30: 2ª/8 → 3ª/9; ej. 34, dos casos) — van sin letra. Ésa
es la parte que hace que el rollout no sea mecánico.

**Verificado tras el cambio:** barcheck OK en las 71 partituras · escala OK · cajas **47,1 / 20,9 /
47,1 / 73,3 %**, o sea idénticas a la referencia sana: la notación no movió una sola nota.

**Sobre el material de Campbell (decisión de Feli):** dijo que transcribe él los licks a La menor con
Guitar Pro. Es su decisión y está tomada. Lo que quedó dicho de mi lado: los conceptos son libres, las
frases escritas tienen copyright, y **en el 5-Level Phrasing Challenge no hay ningún Hendrix** — no
hay título de canción ni crédito, y las notas son pentatónica de Do menor pura. Lo de "es un fragmento
de un solo de Hendrix" venía del backing del video, no de la partitura.

### SÉPTIMA RONDA — segunda pasada por los PDF de Campbell: 2 rescates

Feli pidió releer *Subdivision* y *Repetition* "muy atentamente, a ver si rescatamos algo". Salieron dos
cosas, y la primera es un hueco que llevaba 59 ejercicios sin que nadie lo viera.

**1. Cero bendings de MEDIO TONO en todo el programa.** Los `½` de Campbell (dos, en LONG PHRASE 2) lo
delataron: los 59 ejercicios usan sólo bendings de tono entero. Y el **blue note del ej. 26 sólo existía
como nota PISADA** — cuando en el blues casi siempre se llega a él **estirando** el RE medio tono. La
ironía: el solo de referencia del Hito 2 es *The Thrill Is Gone*, cuyo vocabulario entero son medios tonos.

Arreglado extendiendo el ej. 26 (sin ejercicio nuevo, sin tocar la numeración): compases 1-2 el blue note
pisado en el traste 8, compases 3-4 **la misma frase** estirando el 7 medio tono. Misma altura, otra mano.
El texto explica por qué suena distinto: pisado aparece de golpe, estirado la cuerda **recorre el camino**,
y ese recorrido es el quejido. Hito 2 pasó de 20,9% a 22,1% fuera de caja 1.

> El `\bendHalf` ya existía en el template desde la ronda anterior y no lo usaba nadie. Eso fue la pista.

**2. Al comprimir, la mano derecha tiene que cambiar.** El EX3 de subdivisión de Campbell llena de
hammer-ons y slides justo el tramo de semicorcheas. O sea: **cuando la figura se achica, se pica menos**.
Nosotros enseñábamos ligados (Hito 2, ej. 17-20) y subdivisión (anexo) sin conectarlos nunca. Se agregó
una sección al anexo, después del ej. A. De paso le da sentido retroactivo al **ej. 19** ("una púa cada 3
notas"), que no era de velocidad sino de **economía de púa** y nunca se había dicho.

**Lo que NO se tomó, y por qué:** el EX3 completo (sube a semicorcheas hasta el traste 18) es shred y
contradice el reel #3. La escalera de 5 subdivisiones seguidas de su EX2 mezcla el eje binario con el
tresillo, que nosotros separamos a propósito.

### OCTAVA RONDA — Feli: "¿le di todo el mapa para que se quede en la caja 1?"

Objeción de Feli sobre el Hito 2. **Medida contra la fuente, tenía razón y con margen:**

| | Ejercicios que no pasan del traste 10 |
|---|---|
| Hito 1 | 10 de 16 |
| **Hito 2** | **16 de 18** |
| Hito 3 | 6 de 19 |

Semana 5 vivía entera en trastes **5-8** y la semana 6 (todo el bending del programa) en **5-10**.

**El argumento que cierra el caso no es el de variedad — es físico.** Un bending de un tono en el
traste 7 y otro en el 12 **no son el mismo gesto**: arriba la porción vibrante de la cuerda es más
corta, el mismo empujón da más altura y la cuerda se siente más blanda. Un alumno que sólo bendeó
entre los trastes 5 y 10 **no aprendió a bendear, aprendió a bendear ahí** — y se va a pasar de largo
en el clímax del ej. 53, que tiene el bend en el traste 12.

> **Esto INVIERTE la razón que sostenía el diseño anterior.** "Aislar la posición mientras se aprende
> la técnica" vale cuando la posición no es parte de la técnica. En el bending sí lo es. Y el propio
> cuadernillo se contradecía: el **ej. 28 ya hacía exactamente esto para el vibrato** (tres registros,
> cruza al traste 17). Era una inconsistencia, no un principio.

**Los 3 ejercicios mudados** (ninguno agregado, numeración 1-59 intacta):
- **Ej. 20** (frase aplicada de la semana 5) → caja 3. Tenía un *slide* adentro de la caja 1, que es
  casi una contradicción en los términos.
- **Ej. 22** → **el cambio principal**: los tres bendings pasan a trastes **7 · 12 · 15**. Antes los
  tres caían en 5-8, o sea que el alumno repetía el mismo esfuerzo y no aprendía nada del 2º al 3º.
  Texto nuevo explicando por qué la fuerza cambia con la posición — contenido que no estaba en ningún
  lado del programa.
- **Ej. 24** (lick escuela Gary Moore) → caja 3. Es de aplicación, y la aplicación es donde va la
  transferencia.

**Lo que NO se movió, y por qué:** ej. 17-19 (primera exposición a hammer/pull, mecánica pura —
aislar está bien ahí) · ej. 21 y 29 (se referencian entre sí para comparar) · ej. 26 (su contenido
*es* traste 7 vs traste 8).

**Resultado: Hito 2 de 20,9% a 32,8% fuera de la caja 1.** Semana 5: 5-13. Semana 6: 5-15.

> **La regla que sale de acá, para cualquier técnica nueva:** aislar la posición en la ADQUISICIÓN
> (primer ejercicio), variarla en la APLICACIÓN. Antes aislábamos en las dos.

### NOVENA RONDA — el recorrido horizontal (idea de Feli) y la tónica con dos humores

Feli pidió "jugársela un poco más" y propuso un ejercicio concreto: **recorrer la pentatónica entera
por una sola cuerda**, ligando, desde el traste 2 hasta el 14, y rematar con un bending de medio tono
en el traste 13 de la 2ª resolviendo al 14 de la 3ª. Se implementó tal cual, reescribiendo dos
ejercicios existentes (sin tocar la numeración 1-59 ni el balance 16/18/19/6).

**Ej. 20 — toda la pentatónica en UNA cuerda.** 3ª cuerda, trastes **2 · 5 · 7 · 9 · 12 · 14**: la
octava completa sin cambiar de cuerda. Es el mejor ejercicio anti-caja del programa por una razón
visual: la tablatura es **una sola línea de números**, y ninguna caja tiene esa forma. Los saltos de
2 trastes van con hammer/pull y los de 3 con slide, porque a tres trastes el hammer ya no suena
parejo — eso también hay que decirlo. El compás 2 es el remate de Feli: bend de ½ en la 2ª/13 y
resolución con vibrato en la 3ª/14. **Segundo bending de medio tono del programa** (el otro es el ej. 26).

**Ej. 32 — pregunta abajo, respuesta arriba.** Antes vivía entero en la caja 2. Ahora la pregunta está
en la **caja 5** (trastes 2-5) y la respuesta en la **caja 4** (12-15). El contenido nuevo no es la
estructura pregunta/respuesta —ya estaba— sino que **el registro es parte de lo que la frase dice**:
abajo suena gorda y pesa, arriba suena brillante y "llega". Cubre además las dos cajas que el Hito 2
menos pisaba.

**Tres textos que quedaron desactualizados y se corrigieron en la misma pasada** (esto es lo que se
olvida y después contradice a la partitura):
- La bajada de la semana 5 decía *"todo el mes se toca en la caja 1 y algo de la 2"*. Ya es falso.
- La tabla de bloques decía que la semana 6 *"cierra mudándose a la caja 2"*. Ahora son 3 zonas.
- La regla *"aislar, después integrar"* pasó a **"aprender quieto, aplicar moviéndose"**, con el motivo
  físico escrito.

**Hito 2: 20,9% → 33,3% fuera de la caja 1.** Ejercicios que no pasan del traste 10: de 16 a **12**.
Y las cuatro semanas pisan ahora alguna caja **exclusiva** (4 o 5), cosa que antes no pasaba en
ninguna.

### DÉCIMA RONDA — se importan las transcripciones de Feli (y aparece un bug grave)

Feli transcribió a La menor en Guitar Pro el material de fraseo de Ross Campbell y pidió meterlo
**calcado**. Mandó los MusicXML. Decisiones suyas: *Reto de construcción* y *llamada y respuesta*
entran; *subdivisiones* queda afuera (lo ubica él en otro lado); las cromáticas se habilitan.

**`scripts/importar_musicxml.py` (nuevo).** Parsea el pentagrama de TABLATURA del XML (el único que
trae `<string>`/`<fret>`) y emite el dialecto LilyPond del repo. **El motivo de que exista es el mismo
error que venimos cazando hace rondas:** re-tipear una tablatura mirándola es lo que hizo Design
cuando metió el FA del ej. 47. Acá no hay lectura humana en el medio.

> Le faltaba soportar **tresillos** y el ej. I falló el barcheck (un compás daba 18/16). Se agregó
> `<time-modification>` → `\tuplet`. **El barcheck de LilyPond es el que valida la importación, no la
> vista.** Con la partitura ya renderizada, el error no se veía.

**🔴 EL BUG GRAVE, y es del validador de escala.** El regex era `([a-g][,']*)\d*\.*\\(\d)` y **no
contemplaba alteraciones**: `ees'` y `dis'` no matcheaban nunca. O sea que `auditar_cajas.py` venía
informando *"escala OK"* **sin haber mirado una sola nota alterada** — justo las que más probable es
que estén mal. Arreglado a `([a-g](?:isis|eses|is|es)?[,']*)...`, y **lo primero que cazó fue un FA#
en el ej. 54 del bonus** que llevaba invisible desde siempre (es la 6ª del BB box, intencional y
documentada en la memoria, pero nadie la había validado).

**`CROMATICAS` (dict nuevo, aparte del MAPA).** Las notas fuera de la pentatónica que entran a
propósito, con el motivo escrito al lado: **MIb** (blue note, ej. 26) · **SI** (la 2ª, ej. I) ·
**FA#** (6ª del BB box, ej. 54). Van separadas del MAPA para que se vean. Cualquier alterada que no
esté ahí sigue haciendo fallar el build.

**Ubicación (decidida con Feli):** *Reto de construcción* → **ej. H** del anexo, partido en H (los 5
puntos de entrada, 18 compases) y **H-bis** (el encadenado, 16) porque 34 compases no entran en una
página. *llamada y respuesta* → **ej. I**, 14 compases. Las letras no tocan la numeración 1-59.

**Resultado:** anexo **12 → 15 páginas**, 397 notas, **46% fuera de la caja 1** (era 98% adentro), y
por primera vez el programa usa **cuerda al aire** (traste 0) y llega al **traste 17**.

### AUDITORÍA DEL BLOQUE (panel de agentes) — encontró 4 errores reales, 3 míos

El panel de diseño del bloque de síncopa se cortó por límite de créditos (2 de 4 agentes). Al retomarlo
se le cambió el trabajo al juez: en vez de sintetizar un diseño que ya estaba implementado, **auditarlo**.
Valió la pena — encontró cuatro cosas reales, y **la peor estaba en material ya entregado**:

| # | Qué | Dónde |
|---|---|---|
| 1 | **Un compás de 4/4 con 4 tiempos y medio adentro** (`g8 e d c2.` = 4,5) | `gen_scores.py`, ej. 7 del **Hito 1** — PDF ya entregado |
| 2 | **Las "395 notas" y todo el reparto de figuras estaban mal** | tapa del anexo, README, esta memoria |
| 3 | El compás rotulado "3+3+2" era en realidad **3+3+1+1**, y tenía 4 ataques | anexo, ej. G (`r07`) |
| 4 | "los otros **202** arrancan justo en el 1" era una resta, no un conteo | anexo, sección de síncopa |

**El #1 es el más grave y sobrevivió meses.** LilyPond lo venía avisando en *cada* build
(`warning: barcheck failed`), pero el aviso se perdía entre el resto de la salida. **Arreglo de fondo:
`auditar_cajas.py --compases`** compila todas las partituras y falla con exit 1 si alguna tiene un compás
que no suma. Verificado: el ej. 7 era el único de las 65 partituras. Corregido a `g8 e d c ~ c2` — mismas
alturas, mismo contorno.

**El #2 tiene una causa que hay que recordar: en LilyPond la duración se HEREDA.** En
`c''8\1 a'\1 g'\2 e'\2` hay **cuatro corcheas y un solo `8` escrito**. Mi conteo original contaba tokens
con duración explícita, no notas. Números reales: **995 notas · corchea 74% · negra 17% · blanca 5% ·
redonda 3% · 2 semicorcheas (no 1) · 5 puntillos (no 8) · 0 fusas**. El argumento del anexo *se refuerza*:
74% de corcheas es más monolítico que el 50% que decía antes.

**El #3 era un error musical de verdad, no de redacción.** `c''4. a'4. g'8 e'8` es 3+3+1+1, y encima
tiene 4 ataques — lo que desmentía la frase de la caja ("el más sincopado es el que tiene menos notas"),
contable a la vista en la tablatura de la misma página. Peor: **el compás 2 ya era el verdadero 3+3+2**
(1,5+1,5+1). Se reescribió el compás 3 como el mismo 3+3+2 bajando (`g'4. e'4. d'4`): ahora los tres
compases tienen 3 ataques, el rótulo dice la verdad, y de paso prueba que el patrón es transportable.

> ⚠️ **Lección de método, para no repetirla:** escribí un script en Python para verificar las sumas de
> compás y reportó ~160 compases malos. Eran **casi todos falsos positivos**: el regex tomaba las letras
> a-g de adentro de los `\markup` como si fueran notas. La aritmética de compases **no se verifica con
> regex** — hay duraciones heredadas, tresillos y ligaduras. Se le pregunta a LilyPond, que ya sabe.
> Casi reporto 160 errores inventados por confiar en mi propio script sin contrastarlo.

## 33) ESTADO AL CORTE DEL 19/8 — qué quedó hecho y qué falta

> Sesión larga, retomada después de un ensayo de Feli. Se liquidó el ITEM 1 del backlog de la noche
> anterior y se avanzó fuerte en el ITEM 2 (citas reales para la escuela británica). Esto es el
> corte real: si la sesión se corta acá, **empezar por "LO QUE FALTA" de abajo, no repetir lo ya hecho.**

### Lo que quedó HECHO y commiteado (branch `claude/music-teacher-workflow-rHifB`)

1. **Ej. 44 (Hito 3):** agregado el párrafo que conecta con "Las 3 velocidades" del Anexo de Ritmo
   Hito 2 (ej. A) — mover el ritmo sin tocar las notas vs. comprimir la misma idea en menos espacio.
   Commit `72dcbd0`.
2. **Escuela británica — 3 citas reales de Angus Young/AC/DC**, transcriptas por Feli (no compuestas
   "al estilo de", como el resto del hito):
   - **Ej. 35** reemplazado entero: *Highway to Hell*, el bend-y-soltá repetido que abre el solo.
     Se queda en caja 1 a propósito (sigue siendo el punto de comparación contra el ej. 47).
   - **Ej. 36-bis** (nuevo): *"pentatónica + 6"*, el color Dorian (FA#) de Angus sobre dobles cuerdas.
     Caja 3-4.
   - **Ej. 37-bis** (nuevo): *Lick 1*, compases 2 a 4 — los 4 bendings descendentes (12→10→8→5) +
     remate legato.
   - Se agregó el helper compartido **`bendQuarter`** (bending de ¼ de tono) en `gen_scores.py`,
     junto a `bendFull`/`bendHalf` ya existentes — es la primera vez que el programa usa un micro-bend.
   - `CROMATICAS`: se sumó `b'` (SI) en la 1ª cuerda, traste 7 — lo usa el 37-bis.
   - El ej. 35 ahora referencia hacia adelante al ej. 47 ("vas a volver a ver este mecanismo, tres
     cajas más arriba") — antes la referencia solo iba en un sentido (47→35).
   - **Verificado:** escala OK (`auditar_cajas.py`) y barcheck de compases OK en las 65 partituras
     del hito (`auditar_cajas.py --compases`). Los primeros intentos de e35/e36-bis/e37-bis fallaron
     el barcheck (compases mal medidos) y se corrigieron antes de tocar el PDF — commit `0d74140`.
   - PDF `Cuadernillo-Hito3-El-Vocabulario-EJERCICIOS.pdf` regenerado y commiteado.

### Material descartado en esta sesión (con motivo, para no volver a evaluarlo)

Feli pasó 5 PDF de licks ("Eric liks", "Licks Tony Iommi", "LICK repetitivos inglesa Rock", "Some
Jimi Hendrix Licks", "Some Licks From Jimmy Page"). **Ninguno es transcripción real** — son ejercicios
compuestos "al estilo de" (créditos: "Feli bayá" o "Words & Music by Sukko", no el artista real).
Se rescató UNA sola cosa: el concepto de **bending de ¼ de tono**, que aparece repetido en varios de
esos PDF y hoy sí está incorporado (ver arriba, `bendQuarter`). El resto se descartó: nivel técnico
de shred (sextillizos, posiciones hasta traste 20), acordes con extensiones de jazz (Am7, A7#9,
C7#9+) que no encajan con el vamp estático del programa, y Tony Iommi ni siquiera está en el panel
de referentes (metal/doom, no rock/blues pentatónico). No hace falta revisarlos de nuevo.

### LO QUE FALTA — el backlog de 5 items sigue así:

1. ✅ Ej. 44 connector — DONE (ver arriba)
2. 🟡 Escuela británica — **HECHO el reemplazo de citas reales** (35, 36-bis, 37-bis). Lo que
   queda de este item: **Clapton**. Sigue sin cita propia — se mencionaba solo de pasada. Candidata
   ya identificada en rondas anteriores: *Crossroads* (Cream). Ubicación a decidir: ¿ej. 43-bis
   (después de "el color de cada grado"), o reemplazar algo existente? Ver
   `/scratchpad/ITEM3_CLAPTON.md` para el detalle completo de opciones — sigue vigente.
3. ⬜ Balance escuela americana — ¿agregar Slash real (Sweet Child O' Mine intro) o B.B. King real
   (Thrill Is Gone) para emparejar con Gary Moore/Hendrix que ya tienen cita real? Ver
   `/scratchpad/ITEM4_AMERICAN_BALANCE.md`.
4. ⬜ Apoyatura — falta nombrar el concepto en el Hito 2 (El Sabor). Aparece implícito en el 39-bis
   y el 41 del Hito 3 pero nunca se explica qué es. Propuesta: ej. 35-bis en Hito 2, después del
   ej. 34. Ver `/scratchpad/ITEM5_APOYATURA.md`.
5. Pendiente transversal: cuando se cierre Clapton, actualizar `hoja_de_recursos_hito3.md` (la hoja
   de cierre del Hito 3) sumando las filas de los nuevos ejercicios (36-bis, 37-bis y lo que salga
   de Clapton) a la tabla "DOBLES CUERDAS" / "MOTIVO E INSISTENCIA" correspondiente, antes de mandarla
   a Design — ver `/scratchpad/cierre_bonus/PROMPT_CIERRE_PARA_DESIGN.txt`, que todavía no se envió.

### Nota sobre archivos del scratchpad (no están en el repo, son de esta sesión)

Los documentos de decisión (`ITEM2_BRITISH_CITATIONS.md`, `ITEM3_CLAPTON.md`, `ITEM4_AMERICAN_BALANCE.md`,
`ITEM5_APOYATURA.md`, `SUMMARY_BACKLOG_5_ITEMS.md`, `BACKLOG_PENDIENTE_NOCHE.md`) viven en el directorio
scratchpad de la sesión, **no en el repo** — si una sesión nueva arranca en un container fresco, esos
archivos no van a estar. Esta sección de la memoria es el resumen que sobrevive; si hace falta el detalle
completo de las opciones A/B/C/D de cada item, está en el mensaje del chat donde se escribieron (buscar
"ITEM2_BRITISH_CITATIONS" en el historial) o simplemente re-derivarlas — el razonamiento está resumido
arriba.
