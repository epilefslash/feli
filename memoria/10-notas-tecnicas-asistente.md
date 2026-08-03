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

## 31) MATERIAL QUE FELI PRODUCE APARTE (no está en este repo)

- **Módulo de ritmo del Hito 2** (`Cuadernillo_ritmo_hito_2_Sabor_2_ejercicios.pdf`, 19 pág.): cierra el
  hueco de ritmo que estaba documentado como pendiente para el Módulo 2. Corre **en paralelo** al Hito 2
  (no reemplaza semanas), 10 células rítmicas, 0 notas nuevas, entregable de 1 min. Basado en **Pozzoli**
  (*Guía Teórico-Práctica para la Enseñanza del Dictado Musical*) con página y serie citadas — fuente real
  y verificable. Usa palabras mnemotécnicas (PEZ · PA-TO · CHO-CO-LA-TE · PI-CAN-TE) para las células.
  Cita correctamente el ej. 42 del Hito 3 ("el ritmo es el 70% de la identidad de una frase").
- **Las "Guías del Profe"** (3 documentos) y una carpeta de **backing tracks propios**: existen en la
  máquina de Feli, no en el repo. Una auditoría externa las evaluó bien.
