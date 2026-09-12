# -*- coding: utf-8 -*-
"""Arma el PDF de fundamentación pedagógica — el PORQUÉ de cada decisión del programa.

Documento de verificación, no de contenido para el alumno: reúne la justificación
de la arquitectura completa (3 hitos + bonus) para revisar que el programa esté
bien construido antes de lanzarlo. Fuente: los 4 cuadernillos reales + auditoría
de cajas (scripts/auditar_cajas.py) + Estrategia-FLOW-guitarra-base.md.
"""
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle

from cuadernillo_comun import (H1, H2, H3, BODY, SMALL, CELL, CELLB, RED, DARK, GREY,
                               LIGHT, LIGHT2, BORDER, IG, documento, tabla, caja_oscura)

doc = documento("Fundamentacion-Pedagogica-Metodo-Flow.pdf",
                "FUNDAMENTACIÓN PEDAGÓGICA",
                "El porqué de cada decisión del programa — hito por hito, ejercicio por ejercicio",
                "Solo con Sabor · Fundamentación pedagógica",
                "Fundamentacion pedagogica - Metodo Flow")
W = doc.width
S = []

VERDE = colors.HexColor("#2e7d4f")
AMBAR = colors.HexColor("#b8860b")


def seccion_roja(titulo):
    t = Table([[Paragraph('<font color="white" size="13"><b>%s</b></font>' % titulo, BODY)]], colWidths=[W])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), RED),
                           ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                           ('TOPPADDING', (0, 0), (-1, -1), 7), ('BOTTOMPADDING', (0, 0), (-1, -1), 7)]))
    return t


def porque(titulo, texto):
    """Bloque 'PORQUÉ' — la unidad básica de este documento."""
    return [Paragraph('<font color="#%s"><b>¿POR QUÉ %s?</b></font>' % (RED.hexval()[2:], titulo.upper()), H3),
            Paragraph(texto, BODY)]


def dato(txt):
    return Paragraph('<font color="#%s"><b>Dato verificado:</b></font> %s' % (VERDE.hexval()[2:], txt), SMALL)


# ============================================================ PORTADA
S.append(Paragraph("MÉTODO FLOW — SOLO CON SABOR", H1))
S.append(Paragraph(
    "Este documento no enseña guitarra: <b>audita el programa</b>. Reúne, decisión por decisión, "
    "el porqué de cómo está armado — para poder mirarlo de punta a punta y confirmar que no hay nada "
    "puesto \"porque sí\". Cada afirmación de este documento está verificada contra los 4 cuadernillos "
    "reales (no contra la intención original) y contra una auditoría automática que decodifica cada nota "
    "de cada partitura a su traste real.", BODY))
S.append(Paragraph(
    "<b>Cómo leerlo:</b> cada bloque responde una sola pregunta — \"¿por qué esto está así?\". Donde hay "
    "un número, es un número medido, no estimado. Donde hay una debilidad, está marcada como tal, no "
    "disimulada.", SMALL))

S.append(Paragraph("EL MAPA DEL DOCUMENTO", H2))
S.append(tabla([
    [Paragraph("<b>Sección</b>", CELLB), Paragraph("<b>Responde</b>", CELLB)],
    [Paragraph("1 · La arquitectura", CELL), Paragraph("Por qué 3 hitos, por qué ese orden, por qué 12 semanas.", CELL)],
    [Paragraph("2 · Hito 1 — El Mapa", CELL), Paragraph("Por qué arranca ahí, por qué ese orden de cajas, por qué 47% fuera de caja 1.", CELL)],
    [Paragraph("3 · Hito 2 — El Sabor", CELL), Paragraph("Por qué se concentra, por qué en caja 1 y no otra, por qué ese orden de recursos.", CELL)],
    [Paragraph("4 · Hito 3 — El Vocabulario", CELL), Paragraph("Por qué 5 pasos, por qué dos escuelas, por qué cada lick vive donde vive.", CELL)],
    [Paragraph("5 · Bonus", CELL), Paragraph("Por qué existe afuera del programa y no adentro.", CELL)],
    [Paragraph("6 · El balance completo", CELL), Paragraph("La curva de los 4 números juntos, y por qué esa forma es la correcta.", CELL)],
    [Paragraph("7 · El repertorio", CELL), Paragraph("Por qué un banco fijo de solos, por qué esos.", CELL)],
    [Paragraph("8 · Lo que se dejó afuera", CELL), Paragraph("Ritmo, cambios de acorde, prebend — por qué no están, y por qué eso está bien.", CELL)],
    [Paragraph("9 · Síntesis", CELL), Paragraph("Checklist final de justificación.", CELL)],
], [4.6 * cm, W - 4.6 * cm]))

# ============================================================ 1. LA ARQUITECTURA
S.append(PageBreak())
S.append(seccion_roja("1 · LA ARQUITECTURA GENERAL"))
S.append(Spacer(1, 8))

S.extend(porque("tres hitos, y en ESE orden",
    "El programa sigue Punto A → Puente → Punto B. El Punto A real del avatar es \"sé la caja 1, sueno "
    "escolar, no me muevo\". Eso define el orden con precisión quirúrgica: primero hay que resolver el "
    "\"no me muevo\" (Mapa) — sin territorio, nada de lo que sigue tiene dónde pasar. Después el \"sueno "
    "escolar\" (Sabor) — de nada sirve tener territorio si cada nota suena a ejercicio. Recién con las dos "
    "cosas resueltas tiene sentido el Vocabulario: robar licks sin mapa no tiene dónde aplicarse, y sin "
    "sabor suena a fotocopia. El orden no es arbitrario, es una cadena de dependencias reales."))
S.append(Spacer(1, 4))

S.extend(porque("12 semanas, 4 por hito",
    "Cada hito tiene su propio arco completo (territorio nuevo → técnica → integración → entregable) y "
    "4 semanas es el mínimo para que ese arco no se sienta apurado. Se probó explícitamente: en la primera "
    "versión el Hito 3 tenía 27 ejercicios contra 16 de los otros dos — se detectó el desbalance y se "
    "corrigió moviendo contenido al bonus post-programa (ver sección 5). El número de semanas es fijo; "
    "lo que se ajustó fue cuánto entra en cada una."))
S.append(Spacer(1, 4))

S.extend(porque("un entregable grabado en cada hito",
    "No es un capricho de \"tarea para la casa\": es el mecanismo que convierte una promesa de marketing "
    "en algo verificable. El alumno no reporta que aprendió — <b>lo prueba en video</b>. Y esos mismos "
    "videos son el material de testimonio que alimenta el embudo de ventas de la próxima cohorte. "
    "Entregable pedagógico y entregable de marketing son la misma pieza."))

# ============================================================ 2. HITO 1
S.append(PageBreak())
S.append(seccion_roja("2 · HITO 1 — EL MAPA (ej. 1 a 16)"))
S.append(Spacer(1, 8))

S.extend(porque("arranca en la caja 1",
    "Es el único territorio que el avatar ya tiene. Empezar ahí no es \"repasar\": es anclar lo nuevo "
    "(los puentes, el resto del mástil) a algo que la mano ya conoce sin pensar. Arrancar en una caja "
    "desconocida sumaría dos cosas nuevas a la vez — territorio Y técnica de orientación — cuando el "
    "objetivo de la semana 1 es una sola: soltar la mano en terreno conocido."))
S.append(Spacer(1, 4))

S.extend(porque("el orden de las 4 semanas (1 → 2 → 3/4 → 5)",
    "Cada semana sale de la anterior por una nota compartida, nunca por un salto. Caja 1→2 comparten "
    "los trastes 7-8 (el primer puente). Caja 2→3→4 se dan juntas porque están todas en la zona aguda "
    "y encadenan con dos puentes más. Caja 5 cierra último porque es la única que no tiene territorio "
    "vecino en un extremo — hasta ahí el alumno no tiene con qué compararla, y al final sí: cierra el "
    "círculo con la caja 1 (comparten tónica en el mismo traste, ej. 14)."))
S.append(Spacer(1, 4))

S.extend(porque("el eje son los PUENTES, no las cajas",
    "Está dicho explícito en el propio cuadernillo: \"si te salteás esos, vas a saber 5 cajas y vas a "
    "seguir sin poder moverte\". Los ejercicios 7, 11, 12 y 14 son los que enseñan el cruce — memorizar "
    "5 dibujos sueltos no cumple la promesa del hito, conectarlos sí. Por eso el ejercicio 12 (el "
    "recorrido diagonal) está marcado como \"el ejercicio clave del hito\", no uno más de la lista."))
S.append(Spacer(1, 4))

S.append(dato("47,2% de las notas del hito caen fuera de la ventana de la caja 1 (160 de 339). "
             "Es correcto que sea el más alto de los tres: acá no hay técnica motriz nueva en riesgo — "
             "es geografía pura, y moverse es literalmente el objetivo."))

# ============================================================ 3. HITO 2
S.append(PageBreak())
S.append(seccion_roja("3 · HITO 2 — EL SABOR (ej. 17 a 34)"))
S.append(Spacer(1, 8))

S.extend(porque("\"no vas a aprender ni una nota nueva\"",
    "Es la frase de apertura del propio cuadernillo, y es la tesis del hito: la diferencia entre sonar "
    "escolar y sonar a Gary Moore no son las notas — es el tratamiento. Prometer notas nuevas acá "
    "distraería del punto real: <b>las mismas cinco notas de siempre, atacadas distinto</b>."))
S.append(Spacer(1, 4))

S.extend(porque("la mitad de las notas por ejercicio, comparado con el Hito 1",
    "Regla explícita del mes: \"si tocás muchas notas no podés cuidar ninguna\". El sabor se entrena "
    "nota por nota — bending afinado, vibrato controlado — y eso es incompatible con ejercicios densos. "
    "Es la razón por la que el Hito 2 tiene MENOS notas totales (253) que el Hito 1 (339) a pesar de "
    "tener más ejercicios (18 contra 16)."))
S.append(Spacer(1, 4))

S.extend(porque("el orden de los 4 recursos (ligados → bending → vibrato → espacio)",
    "También está justificado dentro del propio cuadernillo, semana por semana: ligados primero porque "
    "es \"lo más mecánico y lo menos dependiente del oído\" — se aprende rápido y cambia el sonido ya. "
    "Bending segundo porque es el más difícil de afinar y necesita las 4 semanas completas para asentar. "
    "Vibrato tercero porque \"lo mejor de todo es bendear Y vibrar la misma nota\" — necesita el bending "
    "ya asentado. Espacio y dinámica al final porque \"no se hace con los dedos, se hace con la cabeza\" "
    "— es la habilidad menos mecánica y la que más tarda en madurar."))
S.append(Spacer(1, 4))

S.extend(porque("se concentra en 1-2 cajas (y no reparte como el Hito 1)",
    "Acá se enseñan habilidades motrices finas por primera vez — afinar un bending de oído, controlar la "
    "velocidad de un vibrato. Sumarle \"¿dónde estoy parado?\" a \"¿cómo hago esto?\" en simultáneo es "
    "exactamente el tipo de doble carga cognitiva que hace fallar el aprendizaje de una técnica nueva. "
    "El propio cuadernillo lo dice en la semana 5: \"si tenés que pensar dónde estás parado, no te queda "
    "cabeza para pensar cómo suena\"."))
S.append(Spacer(1, 4))

S.extend(porque("caja 1 específicamente, y no caja 3, 4 o 5",
    "El principio de aislar posición no exige que sea justo la caja 1 — técnicamente cualquiera serviría. "
    "Pero caja 1 gana por tres razones concretas, no por costumbre: (1) es el territorio que el alumno "
    "ya tenía ANTES de arrancar el programa, no uno aprendido el mes pasado — el mínimo cognitivo posible. "
    "(2) Los trastes son más cómodos ahí que en la caja 4, donde el propio Hito 1 (ej. 10) ya advierte "
    "\"los trastes son más angostos, apretá con menos fuerza\" — aprender a afinar un bending por primera "
    "vez en la posición físicamente más incómoda sumaría dificultad de dedos a dificultad de oído. "
    "(3) Caja 1 y caja 5 comparten tónica (Hito 1, ej. 14): cuando el hito necesita una segunda caja para "
    "una variante (ej. 31), no es territorio nuevo de cero, es la vecina de la que el alumno ya sale."))
S.append(Spacer(1, 4))

S.extend(porque("el blue note entra en la semana 6 y no antes",
    "Es la primera nota del programa que no pertenece a la escala. Se introduce recién cuando el alumno "
    "\"ya tiene control de mano\" — meterla antes, con la mano todavía peleando con lo básico, la "
    "convertiría en una fuente más de error en vez de en color."))
S.append(Spacer(1, 4))

S.extend(porque("existe el puente \"esto ya te sirve en las 5 cajas\" antes del solo final",
    "El entregable del hito (ej. 34) ya recorre las 5 cajas (38% fuera de la ventana de caja 1) — pero "
    "sin ese puente, el alumno llega ahí sin haberlo practicado ni una vez. La sección agregada convierte "
    "una sorpresa en una consigna anunciada: 10 minutos de práctica libre, bendeando de oído en cajas "
    "3/4/5 y repitiendo el vibrato medido en las cinco, antes de que el solo se lo pida sin avisar."))
S.append(Spacer(1, 4))

S.append(dato("20,9% de las notas del hito caen fuera de la ventana de caja 1 (53 de 253) — subió desde "
             "un 14,1% original. Ningún ejercicio de los 18 queda 100% encerrado en la ventana. Es más "
             "bajo que el Hito 1 y el Hito 3 A PROPÓSITO: es el único hito que enseña técnica motriz "
             "nueva, no geografía ni vocabulario."))

# ============================================================ 4. HITO 3
S.append(PageBreak())
S.append(seccion_roja("4 · HITO 3 — EL VOCABULARIO (ej. 35 a 53)"))
S.append(Spacer(1, 8))

S.extend(porque("robar en 5 pasos, y no simplemente \"copiar\"",
    "El error más común (quedarse en el paso 3, copiar) está nombrado explícitamente porque es el fracaso "
    "típico: \"hay gente que sabe 200 licks y suena a nadie\". Los 5 pasos (escuchar, sacar, copiar, "
    "variar, apropiar) no son burocracia — cada uno resuelve un fracaso real y conocido de cómo la gente "
    "aprende licks mal: sin escuchar de verdad, sin sacarlo de oído, sin variarlo (queda pegado al "
    "original), sin apropiarlo (nunca sale solo improvisando)."))
S.append(Spacer(1, 4))

S.extend(porque("dos escuelas (británica / americana), y no una sola forma de frasear",
    "Son dos lógicas genuinamente distintas de hacer que una frase signifique algo — insistencia contra "
    "melodía. Enseñar solo una dejaría al alumno con la mitad del vocabulario real del género. Además "
    "las dos escuelas sirven de comparación cruzada: el ej. 38 (encadenado británico) sube de caja 1 a 3, "
    "el ej. 42 (encadenado americano) baja de caja 4 a 1 — la dirección opuesta refuerza el contraste "
    "entre \"empujar\" y \"dejar caer\"."))
S.append(Spacer(1, 4))

S.extend(porque("cada lick de escuela vive en una caja distinta desde el ejercicio 35",
    "Decisión tomada en la revisión final del programa: el alumno de este nicho es intermedio, ya sabe "
    "cómo funciona un lick — lo que le falta es ver el patrón replicado. Tener las primeras páginas del "
    "hito ancladas en caja 1 contradecía la promesa del programa antes de que el lector llegara a la "
    "nota al pie que lo explicaba. Cada recurso (celda repetida, dobles cuerdas, unísono, frase vocal, "
    "línea fluida, ligados) se enseña en una caja propia — no es aislar-después-integrar, es integrar "
    "desde el primer contacto, porque la técnica de robo de licks ya no es nueva en este punto del "
    "programa (sí lo era el bending en el Hito 2)."))
S.append(Spacer(1, 4))

S.extend(porque("el ejercicio 35 es la única excepción, y sigue en caja 1",
    "Es el punto de comparación contra el que se mide el ejercicio 47 (\"la misma celda, tres cajas más "
    "arriba\"). Sin una referencia fija en el oído, \"el mismo patrón suena distinto\" no se puede "
    "demostrar — se necesita un ancla, y ésta es la única del hito."))
S.append(Spacer(1, 4))

S.extend(porque("el \"color de los grados\" (ej. 43) es la bisagra teórica del programa",
    "Hasta ese punto el alumno sabe que cerrar en la tónica suena a conclusión, pero no por qué. El "
    "ejercicio 43 le da el mapa completo — qué siente cada grado — y recién ahí el concepto deja de ser "
    "teoría: los ejercicios siguientes (44, 45) son exactamente esa idea aplicada a variar remates. "
    "Va en la semana 11 y no antes porque es donde el alumno lo puede usar de inmediato, no memorizar "
    "en abstracto."))
S.append(Spacer(1, 4))

S.extend(porque("las \"notas de afuera\" (2ª/9ª, 6ª, blue note) entran acá y no antes",
    "Son literalmente las cuatro notas que la pentatónica excluye a propósito (2ª, 3ª mayor, 6ª, 7ª "
    "mayor) — meterlas antes de que el alumno entienda POR QUÉ la pentatónica no tiene notas "
    "equivocadas (ej. 43) las volvería arbitrarias. Recién con el mapa de grados en la cabeza, agregar "
    "3 notas con sus reglas es \"correr un dedo\", no aprender una escala nueva. Es a propósito el techo "
    "del programa, no el piso de otro — frase textual del propio cuadernillo."))
S.append(Spacer(1, 4))

S.extend(porque("la 6ª necesita un recuadro aparte y las otras dos no",
    "Es la única de las tres que exige una decisión: la 6ª menor (oscura, de balada) y la 6ª mayor "
    "(dulce, el \"BB box\") son casi opuestas y dependen del acompañamiento. Enseñar las dos sin avisar "
    "que hay que elegir generaría errores reales, no de oído — la nota chocando de verdad contra el "
    "acorde. El blue note y la 2ª/9ª no necesitan esa aclaración porque no tienen versión contradictoria."))
S.append(Spacer(1, 4))

S.extend(porque("el ejercicio 46 (el mismo lick en las 5 cajas) es el ejercicio central del hito",
    "Es la única forma de DEMOSTRAR, no solo afirmar, que \"un lick no es un lugar del mástil, es un "
    "patrón\". La partitura es idéntica las 5 veces; la tablatura no se parece en nada entre una y otra. "
    "Es prueba visual, no argumento — el alumno lo ve con los ojos antes de que se lo tengan que explicar."))
S.append(Spacer(1, 4))

S.extend(porque("el esqueleto (ej. 50) tiene sus 4 llegadas en 4 cajas distintas, sin excepción",
    "Es el cambio de mayor impacto de todo el rebalanceo: como el alumno escribe lo que va en el medio, "
    "las llegadas fijas lo OBLIGAN a atravesar el mástil para conectarlas — no hay forma de completar el "
    "ejercicio quedándose en un solo lugar. El movimiento deja de ser una sugerencia y pasa a estar en la "
    "estructura misma de lo que el alumno tiene que escribir."))
S.append(Spacer(1, 4))

S.extend(porque("el entregable exige explícitamente \"no puede vivir en la caja 1\"",
    "Es el gate real del programa completo. Antes de esto, la promesa de moverse por las 5 cajas vivía "
    "solo en el copy de marketing — el solo final podía aprobarse sonando perfecto y sin salir nunca de "
    "la caja 1, y nadie se lo iba a notar al alumno. Ahora el propio checklist se lo impide: "
    "\"Territorio: que se mueva por al menos 3 cajas.\""))
S.append(Spacer(1, 4))

S.append(dato("46,8% de las notas del hito caen fuera de la ventana de caja 1 (152 de 325) — es más alto "
             "que el Hito 1. Recuperó paridad después de que el primer rebalanceo (mover 8 licks al "
             "bonus) le hubiera dejado sin querer solo 8,2%. Cero ejercicios de los 19 quedan encerrados."))

# ============================================================ 5. BONUS
S.append(PageBreak())
S.append(seccion_roja("5 · EL BONUS (ej. 54 a 59, post-programa)"))
S.append(Spacer(1, 8))

S.extend(porque("existe AFUERA de las 12 semanas, y no adentro",
    "El Hito 3 original tenía 27 ejercicios contra 16 de los otros dos — carga escondida, no una decisión "
    "consciente. Mover el contenido de cajas 3/4/5 al bonus resolvió el desbalance de golpe, y de paso "
    "convirtió lo que era sobrecarga en un motivo de continuidad después del cierre: un lick por semana, "
    "sin apuro, en vez de doce ejercicios apretados en la última semana del programa."))
S.append(Spacer(1, 4))

S.extend(porque("quedaron 6 licks y no los 8 originales",
    "Dos de los ocho (la celda repetida en caja 3 y el riff de la zona grave en caja 5) se repatriaron al "
    "Hito 3 como ejercicios 47 y 48 durante el rebalanceo de cajas — hacían falta ADENTRO del programa "
    "para que el hito no dependiera de un cuadernillo posterior para demostrar su propia promesa."))
S.append(Spacer(1, 4))

S.append(dato("73,3% de las notas del bonus caen fuera de la ventana de caja 1 (55 de 75). Es correcto "
             "que sea el número más alto de los cuatro: es, literalmente, el cuadernillo dedicado a "
             "todo lo que el programa de 12 semanas no alcanzó a cubrir en profundidad."))

# ============================================================ 6. BALANCE COMPLETO
S.append(PageBreak())
S.append(seccion_roja("6 · EL BALANCE COMPLETO — LA CURVA, NO SOLO LOS NÚMEROS"))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "Los 4 números juntos no son parejos, y esa forma es la que tiene sentido — no una casualidad ni "
    "un defecto a corregir:", BODY))
S.append(Spacer(1, 4))
S.append(tabla([
    [Paragraph("<b>Bloque</b>", CELLB), Paragraph("<b>% fuera de caja 1</b>", CELLB),
     Paragraph("<b>Por qué ESE nivel, no otro</b>", CELLB)],
    [Paragraph("Hito 1 — El Mapa", CELLB), Paragraph("47,2%", CELL),
     Paragraph("Alto: es geografía pura, no hay técnica motriz en riesgo.", CELL)],
    [Paragraph("Hito 2 — El Sabor", CELLB), Paragraph("20,9%", CELL),
     Paragraph("El más bajo, a propósito: es el único hito con técnica motriz nueva que aislar.", CELL)],
    [Paragraph("Hito 3 — El Vocabulario", CELLB), Paragraph("46,8%", CELL),
     Paragraph("Vuelve a subir: la técnica ya está asentada, el vocabulario se integra desde el vamos.", CELL)],
    [Paragraph("Bonus (post-programa)", CELLB), Paragraph("73,3%", CELL),
     Paragraph("El más alto: es exactamente el material dedicado a lo que faltaba cubrir.", CELL)],
], [4.0 * cm, 3.0 * cm, W - 7.0 * cm]))
S.append(Spacer(1, 6))
S.append(Paragraph(
    "<b>La forma es un valle, no una línea recta ascendente — y tiene que serlo.</b> Una curva pareja "
    "(todos los hitos al mismo %) ignoraría que el Hito 2 enseña algo cualitativamente distinto a los "
    "otros dos. Una curva plana en el Hito 3 (si se hubiera quedado en el 8,2% original) hubiera "
    "contradicho la promesa central del programa en el momento exacto en que el alumno arma su "
    "entregable. El valle en el medio ES la firma pedagógica correcta de este programa específico.", BODY))
S.append(Spacer(1, 4))
S.append(Paragraph(
    "<b>Herramienta de verificación:</b> <font face=\"Courier\">scripts/auditar_cajas.py</font> decodifica "
    "cada nota de cada partitura LilyPond a su traste real y calcula estos números de forma automática. "
    "No son una estimación de lectura — es lo que hay, medido. Vale la pena correrlo de nuevo cada vez "
    "que se edite una partitura.", SMALL))

# ============================================================ 7. REPERTORIO
S.append(PageBreak())
S.append(seccion_roja("7 · EL REPERTORIO — POR QUÉ UN BANCO FIJO DE SOLOS"))
S.append(Spacer(1, 8))

S.extend(porque("un banco FIJO de 4 solos, y no un solo nuevo cada semana",
    "Viene del principio central de Nico: \"no crees cosas distintas para cada momento, la información "
    "es la misma — lo que cambia es el vehículo\". Preparar un solo distinto cada una de las 12 semanas "
    "es trabajo no reusable: hay que rehacerlo entero con cada cohorte nueva. Un banco fijo se graba una "
    "vez y sirve para siempre — es la diferencia entre construir Capa 1 (contenido a medida) y Capa 2 "
    "(contenido reusable) sin darse cuenta."))
S.append(Spacer(1, 4))

S.extend(porque("esos 4 solos específicos, uno por hito más el de graduación",
    "Cada uno enseña algo que los otros no: Angus (Back in Black) es la primera copia posible, técnica "
    "simple, sin exigir bending — sirve para el Hito 1. B.B. King (The Thrill Is Gone) es una clase viva "
    "de vibrato y espacio con pocas notas — la tesis exacta del Hito 2. Jimmy Page (Since I've Been "
    "Loving You) conecta varias cajas con licks robables — el mecanismo del Hito 3. Gilmour (Comfortably "
    "Numb) integra las tres capas en un arco largo — sirve de referencia del objetivo final, no para "
    "copiar nota por nota."))
S.append(Spacer(1, 4))

S.extend(porque("ninguno de los 4 es pentatónico 100% puro, y eso no es un problema",
    "Los cuatro meten alguna nota de color (blue note, 3ª mayor tipo B.B. box). Es un gancho pedagógico "
    "a propósito: \"esa nota que se sale de la escala es lo que separa sonar a escuela de sonar a disco\" "
    "— conecta directo con la sección de \"notas de afuera\" del Hito 3."))

# ============================================================ 8. LO QUE QUEDÓ AFUERA
S.append(PageBreak())
S.append(seccion_roja("8 · LO QUE SE DEJÓ AFUERA A PROPÓSITO"))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "Un programa bien construido no es el que cubre todo — es el que sabe explicar por qué no cubre "
    "algo. Estos tres huecos están identificados, no escondidos:", BODY))
S.append(Spacer(1, 4))

S.append(tabla([
    [Paragraph("<b>Qué falta</b>", CELLB), Paragraph("<b>Por qué está bien que falte (por ahora)</b>", CELLB)],
    [Paragraph("Ritmo (subdivisión, shuffle vs. recto, dónde cae la nota respecto del pulso)", CELL),
     Paragraph("Es central para sonar a Page o a Slash, pero es un eje de estudio propio, del tamaño de "
               "un módulo entero — meterlo como parche dentro de estos 3 hitos diluiría el foco de cada "
               "uno. Queda identificado como contenido natural de un Módulo 2 futuro.", CELL)],
    [Paragraph("Cambios de acorde (los 3 hitos improvisan sobre un vamp estático en La menor)", CELL),
     Paragraph("El alumno nunca ve qué pasa cuando el acorde se mueve (un blues de 12 compases, por "
               "ejemplo). Mismo criterio que el ritmo: es la puerta de entrada natural a una segunda "
               "cohorte o a Capa 2, no un parche de las 12 semanas actuales.", CELL)],
    [Paragraph("Prebend (estirar en silencio antes de puntear)", CELL),
     Paragraph("Es una técnica real y usada (Hendrix, Clapton), y hoy no está en ningún ejercicio del "
               "programa. A diferencia de ritmo y cambios de acorde, este SÍ es del tamaño de una nota "
               "corta dentro del bloque de bending existente (semana 6) — no necesita un módulo aparte. "
               "Queda pendiente de decisión: sumarlo como variante del ej. 21-24, o dejarlo también "
               "para después.", CELL)],
], [5.2 * cm, W - 5.2 * cm]))
S.append(Spacer(1, 6))
S.append(Paragraph(
    "El riesgo de NO decir esto explícitamente en algún lugar que el alumno vea (hoy solo está en este "
    "documento y en la estrategia interna) es que termine el programa creyendo que ya sabe todo lo que "
    "hace falta para sonar como sus referentes. Vale la pena una frase honesta en el cierre del Hito 3 "
    "reconociendo el límite — no como excusa, como mapa de lo que sigue.", SMALL))

# ============================================================ 9. SÍNTESIS
S.append(PageBreak())
S.append(seccion_roja("9 · SÍNTESIS — CHECKLIST DE JUSTIFICACIÓN PEDAGÓGICA"))
S.append(Spacer(1, 8))
S.append(tabla([
    [Paragraph("", CELLB), Paragraph("<b>Verificación</b>", CELLB), Paragraph("<b>Estado</b>", CELLB)],
    [Paragraph("☑", CELLB), Paragraph("¿Cada hito tiene una razón de ser distinta a los otros dos?", CELL),
     Paragraph("Sí — Mapa/Sabor/Vocabulario son 3 problemas distintos del mismo Punto A.", CELL)],
    [Paragraph("☑", CELLB), Paragraph("¿El orden interno de cada hito está justificado, no es arbitrario?", CELL),
     Paragraph("Sí, con texto explícito en cada cuadernillo (semana por semana, ejercicio por ejercicio).", CELL)],
    [Paragraph("☑", CELLB), Paragraph("¿Las decisiones de \"quedarse\" en una caja tienen un motivo, no son descuido?", CELL),
     Paragraph("Sí — caja 1 en Hito 2 es aislamiento de técnica motriz nueva, con 3 razones concretas.", CELL)],
    [Paragraph("☑", CELLB), Paragraph("¿El entregable de cada hito prueba la promesa del hito, o solo la simula?", CELL),
     Paragraph("Sí, con gate explícito en el Hito 3 (\"no puede vivir en la caja 1\").", CELL)],
    [Paragraph("☑", CELLB), Paragraph("¿Los números de distribución de cajas están medidos, no estimados?", CELL),
     Paragraph("Sí — auditoría automática sobre las partituras reales, no lectura a ojo.", CELL)],
    [Paragraph("☑", CELLB), Paragraph("¿Lo que falta está identificado y explicado, no escondido?", CELL),
     Paragraph("Sí — ritmo, cambios de acorde y prebend, con el porqué de cada ausencia.", CELL)],
    [Paragraph("~", CELLB), Paragraph("¿El alumno mismo puede ver esas ausencias, o solo están en documentos internos?", CELL),
     Paragraph("Parcial — pendiente sumar una frase honesta en el cierre del Hito 3.", CELL)],
], [1.0 * cm, 7.0 * cm, W - 8.0 * cm]))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="#f7d7d2" size="9">Este documento se actualiza cada vez que se toca la estructura de '
    'cajas o el orden de un hito. Si en algún momento un ejercicio cambia de posición sin que la '
    'justificación de esta sección se actualice también, es señal de que el cambio se hizo por '
    'estética y no por pedagogía — <b><font color="white">y ahí hay que parar y preguntarse por qué.'
    '</font></b></font>', W))

doc.build(S)
print("OK Fundamentacion-Pedagogica-Metodo-Flow.pdf")
