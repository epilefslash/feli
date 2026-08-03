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
> `python3 scripts/auditar_cajas.py` y leer la fuente LilyPond**. Hasta ahora, 100% de los errores
> musicales reportados por Design estaban en la versión de Design.

## 31) MATERIAL QUE FELI PRODUCE APARTE (no está en este repo)

- **Módulo de ritmo del Hito 2** (`Cuadernillo_ritmo_hito_2_Sabor_2_ejercicios.pdf`, 19 pág.): cierra el
  hueco de ritmo que estaba documentado como pendiente para el Módulo 2. Corre **en paralelo** al Hito 2
  (no reemplaza semanas), 10 células rítmicas, 0 notas nuevas, entregable de 1 min. Basado en **Pozzoli**
  (*Guía Teórico-Práctica para la Enseñanza del Dictado Musical*) con página y serie citadas — fuente real
  y verificable. Usa palabras mnemotécnicas (PEZ · PA-TO · CHO-CO-LA-TE · PI-CAN-TE) para las células.
  Cita correctamente el ej. 42 del Hito 3 ("el ritmo es el 70% de la identidad de una frase").
- **Las "Guías del Profe"** (3 documentos) y una carpeta de **backing tracks propios**: existen en la
  máquina de Feli, no en el repo. Una auditoría externa las evaluó bien.
