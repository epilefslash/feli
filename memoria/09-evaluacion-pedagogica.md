<!-- Parte de la memoria del proyecto. Ver /CLAUDE.md en la raíz del repo para el índice completo. -->

# Evaluación pedagógica final

> La auditoría completa del programa terminado — hallazgos y el ajuste de Hito 2 que salió de ahí. Complementa (no reemplaza) el PDF Fundamentacion-Pedagogica-Metodo-Flow.pdf.

---

## 29) EVALUACIÓN FINAL DEL PROGRAMA COMPLETO (3 hitos + bonus) — Y AJUSTE DE HITO 2

> Evaluación con los 3 roles (pedagogo, marketing, alumno intermedio) sobre los 4 PDFs reales, releídos
> completos para esta evaluación (no sobre el resumen que traía el prompt, que estaba desactualizado:
> decía Hito 3 en 21% cuando ya estaba en 38,7%, y mencionaba un "bono de escala menor natural" que
> no existe como cuadernillo — es la tabla de "notas de afuera" dentro del Hito 3).

**Veredicto: SÍ se lanza.** La pieza que faltaba y ya está resuelta: la consigna del solo final (Hito 3,
página de cierre) dice textual **"Territorio: que se mueva por al menos 3 cajas. No puede vivir en la
caja 1"** — es un gate real sobre el entregable, no una intención. Antes de esta sesión ese gate no
existía con esa fuerza.

**Hallazgo de la evaluación → acción tomada:** el Hito 2 (14,1% fuera de caja 1) tenía más semanas de
aislamiento del necesario. El ej. 25-26 ya sale a caja 2 en la semana 6; pero la semana 7 (vibrato,
ej. 27-30) y la semana 8 (espacio/dinámica, ej. 31-33) volvían enteras a la caja 1, con la única
excepción de un compás del ej. 28 y del ej. 31. Se resolvió así:

- **Ej. 27, 30, 32 y 33 se mudaron a la caja 2** (misma técnica, mismo objetivo, otro territorio).
  Quedan en caja 1: nada de la semana 7-8 excepto lo que ya tenía sentido ahí — el ej. 29 (bending +
  vibrato) sigue en caja 1 porque referencia directamente al ej. 21 ("volvé al ejercicio 21") para
  comparación 1 a 1.
- **Sin tocar:** ej. 21-24 y 28 (bending puro + el ejercicio de vibrato en 3 registros, que YA cruzaba
  a caja 4 a propósito), ej. 31 (ya tenía su variante en caja 5).
- **Resultado: Hito 2 pasó de 14,1% a 20,9%**, y de tener varios ejercicios 100% encerrados en la
  ventana 5-8 a **cero** — los 18 ejercicios del hito ahora salen de esa ventana en algún punto.

**Bug menor encontrado y corregido en la misma revisión:** la tapa del cuadernillo bonus decía
"8 LICKS FUERA DE LA CAJA 1" (quedó de antes de repatriar el 52 y el 56 al Hito 3) cuando el contenido
real y correcto son 6. Corregido en el título.

**Debilidades que quedaron anotadas, sin resolver todavía (no bloquean el lanzamiento):**
1. La promesa completa de bio ("de caja 1 a solo con sabor en 90 días") no aparece en la tapa de
   ningún cuadernillo — solo vive en documentos internos (este archivo, el Resumen Ejecutivo).
2. El hueco de ritmo (ya documentado en la sección de huecos del Módulo 2) no tiene una frase
   explícita dentro del material que ve el alumno — solo acá, en la estrategia interna.
3. Falta una expectativa explícita de cuánto hay que practicar por semana para que las 12 semanas
   cierren (el material asume 20 min/día, 7 días — no está escrito en ningún lado que vea el alumno).

**CUARTA RONDA — Feli: "por qué nos detenemos en 1 y 2, y no en todas".** Pregunta válida, verificada
con la auditoría: el Hito 2 nunca da un momento explícito de "las 5 cajas", a diferencia del Hito 1
(geografía pura) y del ej. 46 del Hito 3 (mismo lick, 5 cajas). La razón de fondo sigue siendo correcta
— aislar posición mientras se aprende una técnica física nueva (afinar bending, controlar vibrato) — pero
faltaba el momento de generalización una vez que la técnica ya está aprendida. Se agregó, sin sumar
ejercicio numerado: una sección nueva **"ANTES DEL SOLO: ESTO YA TE SIRVE EN LAS 5 CAJAS"**, justo antes
del ej. 34 (el solo de evaluación, que YA recorre las 5 cajas — 38% fuera de la ventana). Incluye el mapa
completo (`MapaCompleto`, reusado del Hito 1) y una consigna de práctica libre de 10 min: bendear de oído
en cajas 3/4/5 y repetir el vibrato medido del ej. 27 en las cinco. Convierte el "sorpresa, el solo se
mueve" en algo anunciado y practicado antes de llegar al entregable.

**QUINTA RONDA (9/9) — Feli: "el solo final del Hito 1 NO pasa por la caja 5".** Objeción sobre el
**ej. 16**, el entregable del propio Hito 1 (el "Mes 1: video recorriendo las 5 cajas sin pausa" de
`memoria/01` §3). Verificado decodificando nota por nota contra la fuente: **tenía razón.** El
ejercicio tocaba los trastes 5,7,8,9,10,12,13,14,15 — nunca 2 ni 3, los únicos exclusivos de la
caja 5 (`auditar_cajas.py --tabla`). Su único "contacto" con la caja 5 era el traste 5, compartido
con la caja 1 — la misma ambigüedad estructural que ya se había corregido en el Hito 3 (ver
`memoria/10` §30, tercera ronda: ej. 50, 51, 53), pero que nunca se aplicó acá porque esa ronda
solo auditó el Hito 3.

**El arreglo (mismo mecanismo ya validado, mismas dos notas):** el compás final pasó de un whole
note en la tónica (`a'1\1`, traste 5) a dos notas — primero el traste 3 (SOL, exclusivo de caja 5)
y recién después la tónica del traste 5, con el label "cerrás en casa" movido a la nota que
realmente resuelve. Mismo gesto que ej. 50/53: bajar a la caja 5 real antes de cerrar en casa.

**Resultado:** `exclusivas` pasa de `[4]` a `[4, 5]` — ahora hay evidencia real, no ambigua, de la
caja 5. Hito 1 completo: 47,1% → 47,2% fuera de la ventana 5-8 (cambio despreciable, un solo
ejercicio tocado). Verificado: escala OK y barcheck de compases OK en las 73 partituras
(`auditar_cajas.py --compases`). El resto del Hito 1 no se tocó.

> **La lección se repite, van tres veces:** un ejercicio puede decir "cajas: [1,2,3,4,5]" en el
> reporte crudo y no probar nada de la caja 5 si el único contacto es un traste compartido. La
> columna `exclusivas` es la que dice la verdad — y hay que mirarla ejercicio por ejercicio, no
> solo confiar en que una ronda anterior ya "arregló las cajas" en general.

---
