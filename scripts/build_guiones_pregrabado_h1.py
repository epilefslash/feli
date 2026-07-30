# -*- coding: utf-8 -*-
"""Arma el PDF de los 3 guiones de clases PREGRABADAS del Hito 1 — EL MAPA.

Contenido de enseñanza (no marketing): son las clases que el alumno mira dentro
del programa, grabadas una sola vez, reusables por cohorte. Basado en los
ejercicios 1-16 del Cuadernillo-Hito1-El-Mapa-EJERCICIOS.pdf.
"""
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle

from cuadernillo_comun import (H1, H2, H3, BODY, SMALL, CELL, CELLB, RED, DARK, GREY,
                               LIGHT, LIGHT2, BORDER, IG, documento, tabla, caja_oscura)

doc = documento("Guiones-Pregrabado-Hito1-El-Mapa.pdf",
                "CLASES PREGRABADAS — HITO 1",
                "3 guiones para grabar: El Mapa completo, ejercicios 1 a 16",
                "Solo con Sabor · Pregrabado Hito 1 — El Mapa",
                "Guiones pregrabado - Hito 1 El Mapa")
W = doc.width
S = []


def seccion_roja(titulo):
    t = Table([[Paragraph('<font color="white" size="13"><b>%s</b></font>' % titulo, BODY)]], colWidths=[W])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), RED),
                           ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                           ('TOPPADDING', (0, 0), (-1, -1), 7), ('BOTTOMPADDING', (0, 0), (-1, -1), 7)]))
    return t


def minuto(t, txt):
    return Paragraph('<font color="#%s"><b>%s</b></font> %s' % (RED.hexval()[2:], t, txt), CELL)


# ============================================================ PORTADA
S.append(Paragraph("GUIONES PREGRABADO — HITO 1: EL MAPA", H1))
S.append(Paragraph(
    "Estas son las <b>3 clases que el alumno mira dentro del programa</b> — no son reels de Instagram, "
    "son contenido de enseñanza. Se graban UNA vez, planeadas, y sirven para todas las cohortes futuras "
    "(el modelo de Sergio Assat: pregrabado + vivo liviano + WhatsApp). Cubren los 16 ejercicios del "
    "Hito 1 completo, reorganizados de 4 semanas en vivo a 3 videos pregrabados más densos.", BODY))
S.append(tabla([
    [Paragraph("<b>Video</b>", CELLB), Paragraph("<b>Título</b>", CELLB),
     Paragraph("<b>Cubre</b>", CELLB), Paragraph("<b>Duración</b>", CELLB)],
    [Paragraph("1", CELLB), Paragraph("Tu casa: la Caja 1 y el primer sabor", CELL),
     Paragraph("Ejerc. 1-4", CELL), Paragraph("~12 min", CELL)],
    [Paragraph("2", CELLB), Paragraph("Los puentes: de una caja a cuatro", CELL),
     Paragraph("Ejerc. 5-12", CELL), Paragraph("~18 min", CELL)],
    [Paragraph("3", CELLB), Paragraph("El círculo completo + tu solo de evaluación", CELL),
     Paragraph("Ejerc. 13-16", CELL), Paragraph("~15 min", CELL)],
], [1.6 * cm, 7.0 * cm, 3.0 * cm, W - 11.6 * cm]))
S.append(Paragraph(
    "<b>Nota de grabación:</b> guitarra + cámara fija sobre el mástil (el alumno necesita VER los dedos, "
    "no tu cara). Grabá cada video en una sola sesión si podés — la energía pareja importa más que la "
    "perfección de edición. Tono: profesor cercano explicando a un alumno real, no locutor.", SMALL))

# ============================================================ VIDEO 1
S.append(PageBreak())
S.append(seccion_roja("VIDEO 1 · TU CASA: LA CAJA 1 Y EL PRIMER SABOR"))
S.append(Spacer(1, 8))
S.append(tabla([
    [Paragraph("<b>Cubre</b>", CELLB), Paragraph("Ejercicios 1, 2, 3 y 4 (Semana 1 del cuadernillo)", CELL)],
    [Paragraph("<b>Objetivo</b>", CELLB),
     Paragraph("Que el alumno se vaya con la Caja 1 sonando limpia, sepa dónde están sus 3 tónicas, "
               "y sienta su primer bending + vibrato con sabor real.", CELL)],
    [Paragraph("<b>Necesitás en pantalla</b>", CELLB),
     Paragraph("Diagrama de la Caja 1 (trastes 5-8) visible todo el video, guitarra en cámara.", CELL)],
], [3.0 * cm, W - 3.0 * cm]))

S.append(Spacer(1, 8))
S.append(Paragraph("GUION", H2))

S.append(minuto("[0:00-0:45] Apertura",
    "\"Bienvenido al Hito 1: El Mapa. En este primer video vamos a hacer UNA sola cosa, pero bien "
    "hecha: dejar la Caja 1 sonando tan cómoda que dejes de mirarte la mano. Esto es la base de "
    "TODO lo que viene después — no te apures a otros videos si esto todavía no te sale limpio.\""))
S.append(Spacer(1, 6))

S.append(minuto("[0:45-3:00] Ejercicio 1 — La caja, ida y vuelta",
    "Mostrás el diagrama, explicás la digitación (un dedo por traste: índice-5, anular-7, meñique-8). "
    "Tocás el ejercicio despacio mientras contás en voz alta. \"Subís las 12 notas, bajás. Púa "
    "alternada desde el primer día, aunque te salga lento. Si una nota suena apagada, PARÁ — no sigas "
    "de largo, arreglá el dedo ahí mismo.\" Repetís a 60 BPM con metrónomo audible en pantalla."))
S.append(Spacer(1, 6))

S.append(minuto("[3:00-5:30] Ejercicio 2 — Las tónicas (tu casa)",
    "\"Ahora vamos a las tres puertas de tu casa: sexta cuerda traste 5, cuarta cuerda traste 7, "
    "primera cuerda traste 5. Las tres son la nota LA.\" Tocás cada una dejándola sonar, decís "
    "\"la\" en voz alta. \"Esto no es solo teoría — es entrenar el oído para que sepas, sin mirar, "
    "cuándo llegaste a casa. Vas a necesitar esto toda tu vida como guitarrista.\""))
S.append(Spacer(1, 6))

S.append(minuto("[5:30-8:00] Ejercicio 3 — Secuencia de a 4",
    "\"Este es el ejercicio más aburrido del cuadernillo, y te voy a explicar por qué es el que más "
    "se nota.\" Explicás el patrón de grupos de 4 (romper la línea recta). \"Cuando toques una escala "
    "de corrido vas a sonar a alumno. Cuando la mano sabe cambiar de dirección, sonás a música. "
    "Es la diferencia entre practicar y tocar.\""))
S.append(Spacer(1, 6))

S.append(minuto("[8:00-11:00] Ejercicio 4 — Tu primer lick con sabor",
    "\"Ahora el momento que estabas esperando: cuatro tiempos de música de verdad.\" Mostrás el "
    "bending de un tono en la 3ª cuerda traste 7. \"Tocá primero el traste 9 para saber a dónde "
    "tenés que llegar. Ahora bendeá el 7 hasta que suene IGUAL — no más, no menos.\" Mostrás el "
    "vibrato final. \"Esto separa a un alumno de un guitarrista: movelo parejo, sin apuro. Practicá "
    "esto 10 veces por día toda la semana antes de pasar al video 2.\""))
S.append(Spacer(1, 4))
S.append(Paragraph(
    "<i>Nota al pie — aclarar en cámara: \"Ojo, esto es solo una PROBADA. Todavía no te estoy "
    "enseñando a bendear y vibrar de verdad — eso es un mes entero, el Hito 2. Hoy quedate con la "
    "sensación de que la caja 1 puede sonar así. En el Hito 2 vas a aprender a hacerlo vos solo, "
    "afinado, en cualquier cuerda y con control real.\"</i>", SMALL))
S.append(Spacer(1, 6))

S.append(minuto("[11:00-12:00] Cierre",
    "\"Con esto ya tenés tu casa. En el próximo video salimos de acá — vamos a cruzar a otras tres "
    "cajas y vas a entender por qué esto que aprendiste hoy no era 'una caja más': era la base de "
    "todo el mástil. Nos vemos en el video 2.\""))

# ============================================================ VIDEO 2
S.append(PageBreak())
S.append(seccion_roja("VIDEO 2 · LOS PUENTES: DE UNA CAJA A CUATRO"))
S.append(Spacer(1, 8))
S.append(tabla([
    [Paragraph("<b>Cubre</b>", CELLB), Paragraph("Ejercicios 5 a 12 (Semanas 2 y 3 del cuadernillo)", CELL)],
    [Paragraph("<b>Objetivo</b>", CELLB),
     Paragraph("El alumno conecta las Cajas 1→2→3→4 sin frenar, entendiendo los puentes como el "
               "concepto central del hito (no las cajas sueltas).", CELL)],
    [Paragraph("<b>Necesitás en pantalla</b>", CELLB),
     Paragraph("Diagramas de cajas 2, 3 y 4. Este es el video más largo — si hace falta, se puede "
               "partir en 2A (cajas 2, ejerc. 5-8) y 2B (cajas 3-4, ejerc. 9-12).", CELL)],
], [3.0 * cm, W - 3.0 * cm]))

S.append(Spacer(1, 8))
S.append(Paragraph("GUION", H2))

S.append(minuto("[0:00-0:40] Apertura",
    "\"En el video pasado dejaste la Caja 1 sonando cómoda. Hoy vas a entender la idea más importante "
    "de todo el Hito 1: las cajas no son dibujos separados que memorizás una por una. Son UN circuito, "
    "y lo que las conecta son los puentes. Ese es el tema de hoy.\""))
S.append(Spacer(1, 6))

S.append(minuto("[0:40-2:30] Ejercicio 5 — Caja 2, ida y vuelta",
    "Diagrama de caja 2 (trastes 7-10). \"Fijate que arranca justo donde termina la que ya sabés: "
    "comparte los trastes 7 y 8. No es territorio nuevo de cero.\" Alertás la irregularidad: \"en la "
    "3ª cuerda los trastes son 7 y 9, no 7 y 10 — es la excepción de la escala, y es donde todos se "
    "equivocan la primera vez.\""))
S.append(Spacer(1, 6))

S.append(minuto("[2:30-3:30] Ejercicio 6 — Las tónicas de la caja 2",
    "\"Dos LA nuevos. Pero mirá este de acá — 4ª cuerda traste 7 — ya lo conocías del video 1. "
    "Ese es EL PUENTE: una misma nota que pertenece a las dos cajas al mismo tiempo.\""))
S.append(Spacer(1, 6))

S.append(minuto("[3:30-6:30] Ejercicio 7 — EL PUENTE (caja 1 a caja 2)",
    "\"Este es el ejercicio más importante de todo el mes, prestale toda tu atención.\" Tocás lento: "
    "subís por caja 1, y en la 1ª cuerda hacés un slide del traste 8 al 10. \"Ya estás en la caja 2, "
    "en un solo movimiento, sin frenar, sin mirar la mano. El slide no es un adorno — es el vehículo "
    "que te lleva de una zona a la otra.\" Mostrás que el mismo cruce funciona en la 2ª cuerda (8 a "
    "10) y en la 3ª (7 a 9). \"Es la misma idea repetida en tres cuerdas distintas.\""))
S.append(Spacer(1, 6))

S.append(minuto("[6:30-8:00] Ejercicio 8 — Un lick que cruza las dos cajas",
    "\"Ahora juntamos todo lo del video 1 y de hoy: bending en la caja 1, slide al medio, vibrato ya "
    "en la caja 2.\" Tocás el lick completo un par de veces. \"Cuando esto te salga sin pensarlo, "
    "dejaste de tener 'dos cajas' — tenés una sola zona de seis trastes. Improvisá 5 minutos usando "
    "SOLO estas dos antes de seguir.\""))
S.append(Spacer(1, 6))

S.append(minuto("[8:00-9:30] Ejercicios 9 y 10 — Cajas 3 y 4",
    "Diagramas de cajas 3 (trastes 9-13) y 4 (12-15). \"La caja 3 es la más cómoda de las cinco — "
    "y ojo, esa comodidad es una trampa: medio mundo se queda a vivir ahí y nunca sale. La caja 4 "
    "tiene los trastes más angostos: apretá cerca del metal, con menos fuerza. Si te duele la mano, "
    "parás — esto no se entrena con dolor.\""))
S.append(Spacer(1, 6))

S.append(minuto("[9:30-12:00] Ejercicio 11 — Dos puentes encadenados",
    "\"Ahora encadenamos dos cruces seguidos.\" Mostrás el slide del 10 al 12 en la 1ª cuerda (entra "
    "a caja 3) y del 10 al 13 en la 2ª (entra a caja 4). \"Terminás con un vibrato largo en el traste "
    "14 de la 3ª cuerda — esa nota es un LA. Por eso suena a que llegaste a algún lado.\""))
S.append(Spacer(1, 6))

S.append(minuto("[12:00-16:30] Ejercicio 12 — EL RECORRIDO DIAGONAL (el ejercicio clave del hito)",
    "Bajás el tono de voz, marcás que esto es LO más importante del video. \"Acá dejás de pensar en "
    "cajas del todo. En vez de subir y bajar adentro de una zona, atravesás el mástil en diagonal: "
    "subís de a poco por cada cuerda y cruzás las cuatro cajas de una sola vez.\" Tocás lento, "
    "señalando cada cambio de caja en cámara. \"Esto es exactamente lo que hace Page o Slash cuando "
    "parece que van a cualquier lado y nunca se pierden. No es magia — es este ejercicio, hecho mil "
    "veces. Practicalo todos los días, solo, y ya justifica el hito entero.\""))
S.append(Spacer(1, 6))

S.append(minuto("[16:30-18:00] Cierre",
    "\"Con esto ya conectaste cuatro cajas de las cinco. En el video 3 cerramos el círculo con la "
    "última caja, entendés por qué las cinco forman un aro y no una fila — y grabás tu solo de "
    "evaluación, el entregable del hito.\""))

# ============================================================ VIDEO 3
S.append(PageBreak())
S.append(seccion_roja("VIDEO 3 · EL CÍRCULO COMPLETO + TU SOLO DE EVALUACIÓN"))
S.append(Spacer(1, 8))
S.append(tabla([
    [Paragraph("<b>Cubre</b>", CELLB), Paragraph("Ejercicios 13, 14, 15 y 16 (Semana 4 del cuadernillo)", CELL)],
    [Paragraph("<b>Objetivo</b>", CELLB),
     Paragraph("Cerrar el mapa: caja 5, entender el círculo completo, bajar el mástil (no solo subir), "
               "y presentar el solo de evaluación como entregable del Hito 1.", CELL)],
    [Paragraph("<b>Necesitás en pantalla</b>", CELLB),
     Paragraph("Diagrama de caja 5 + el mapa completo de las 5 cajas juntas (última página del "
               "cuadernillo). Es el video que más se va a volver a mirar — el alumno vuelve a este "
               "para grabar su entregable.", CELL)],
], [3.0 * cm, W - 3.0 * cm]))

S.append(Spacer(1, 8))
S.append(Paragraph("GUION", H2))

S.append(minuto("[0:00-0:40] Apertura",
    "\"Último video del Hito 1. Hoy cerramos el mapa completo, y al final vas a grabar tu primer "
    "entregable: un solo de 8 compases que recorre las cinco cajas. Ese video es tuyo para siempre "
    "— es tu 'antes' del programa.\""))
S.append(Spacer(1, 6))

S.append(minuto("[0:40-2:30] Ejercicio 13 — Caja 5, ida y vuelta",
    "Diagrama de caja 5 (trastes 2-5). \"Vive debajo de la caja 1 — es la que menos se usa y la que "
    "más te va a servir, es la zona grave, la de los riffs.\" Alertás la digitación incómoda: "
    "\"en la 4ª y 3ª cuerda las notas son 2 y 5, un estirón de tres trastes. Es la más incómoda de "
    "las cinco — es normal, no la estás haciendo mal.\""))
S.append(Spacer(1, 6))

S.append(minuto("[2:30-4:30] Ejercicio 14 — El círculo: de la caja 5 a la 1",
    "\"Acá está la revelación de todo el mes.\" Subís por caja 5 y al llegar a la 1ª cuerda traste 5 "
    "te quedás quieto un segundo. \"Ya estás en la caja 1. No hubo slide, no hubo salto — es la MISMA "
    "nota. Las cinco cajas no son una fila del 1 al 5: son un círculo. Después de la 5 viene la 1 "
    "otra vez, una octava más arriba. Mirá el mapa completo mientras lo tocás de nuevo.\" Mostrás el "
    "diagrama del mástil entero."))
S.append(Spacer(1, 6))

S.append(minuto("[4:30-7:00] Ejercicio 15 — Bajar el mástil en diagonal",
    "\"El video 2 aprendiste a subir en diagonal. Esto es lo contrario, y es más difícil de lo que "
    "parece: casi todo el mundo sabe subir y no sabe volver. Un solo que sube y no baja se queda sin "
    "final.\" Tocás desde caja 4 hasta caja 5 bajando en diagonal, señalando cada cambio de caja. "
    "\"En dos compases pasás por las cinco cajas completas.\""))
S.append(Spacer(1, 6))

S.append(minuto("[7:00-12:00] Ejercicio 16 — EL SOLO DE EVALUACIÓN (tu entregable)",
    "Tono más ceremonial, marcás que esto es el cierre. \"Este solo de 8 compases usa todo lo que "
    "viste en el Hito 1: espacio, bending, vibrato, slides entre cajas, y termina resolviendo en la "
    "tónica.\" Tocás el solo completo, despacio primero, después a tempo. \"Tu tarea, antes de pasar "
    "al Hito 2, es grabarte tocando esto — de memoria, sin mirar el mástil — y guardar ese video. "
    "Cuando termines el programa entero lo vas a volver a mirar y no vas a poder creer la diferencia. "
    "Ese contraste es tu prueba de que el método funciona.\""))
S.append(Spacer(1, 6))

S.append(minuto("[12:00-13:30] Cierre del Hito 1",
    "\"Con esto cerrás El Mapa. Ya no hay cinco cajas sueltas — hay un mástil, y sabés moverte por "
    "él. Lo que te faltaba hasta ahora no era más escalas: era esto, conectar lo que ya sabías. "
    "En el Hito 2 vamos a trabajar que todo esto que tocás EMPIECE A SONAR a música: bending afinado, "
    "vibrato con carácter, espacio. Te espero ahí.\""))

# ============================================================ NOTA FINAL DE PRODUCCIÓN
S.append(PageBreak())
S.append(Paragraph("NOTA DE PRODUCCIÓN", H2))
S.append(Paragraph(
    "Estos 3 guiones están escritos para grabar TAL CUAL — son más largos y detallados que los reels "
    "de Instagram a propósito: es contenido de enseñanza, no de conversión. No hace falta un guion "
    "palabra por palabra memorizado; la estructura de minutos + la idea de cada bloque alcanza para "
    "grabar de corrido mirando la guitarra, no la cámara.", BODY))
S.append(Paragraph(
    "<b>Sobre reusar esto entre cohortes:</b> una vez grabado, este material no se vuelve a grabar. "
    "El tiempo en vivo (1-2 sesiones/semana + WhatsApp) se dedica a dudas puntuales, corrección "
    "personalizada, y el repertorio/impro con devolución — no a repetir esta explicación cada vez "
    "que arranca una cohorte nueva.", BODY))
S.append(Paragraph(
    "<b>Pendiente:</b> el mismo tratamiento para los Hitos 2 y 3, una vez que este primer bloque "
    "esté grabado y probado con la primera cohorte real.", SMALL))

doc.build(S)
print("OK Guiones-Pregrabado-Hito1-El-Mapa.pdf")
