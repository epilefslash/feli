# -*- coding: utf-8 -*-
"""Arma el PDF resumen ejecutivo — todo lo resuelto/hecho, para llevar a la mentoría con Nico.

Es un documento de estado, no de contenido: qué está decidido, qué está producido,
y qué queda abierto para resolver en la mentoría. Fuente: Estrategia-FLOW-guitarra-base.md.
"""
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle

from cuadernillo_comun import (H1, H2, H3, BODY, SMALL, CELL, CELLB, RED, DARK, GREY,
                               LIGHT, LIGHT2, BORDER, IG, documento, tabla, caja_oscura)

doc = documento("Resumen-Ejecutivo-para-Nico.pdf",
                "RESUMEN EJECUTIVO",
                "Todo lo resuelto y producido, antes de arrancar la mentoría",
                "Solo con Sabor · Resumen ejecutivo para la mentoría",
                "Resumen ejecutivo - Metodo Flow")
W = doc.width
S = []


def estado(txt, color=RED):
    return Paragraph('<font color="%s"><b>%s</b></font>' % (color.hexval()[2:], txt), CELLB)


VERDE = colors.HexColor("#2e7d4f")
AMBAR = colors.HexColor("#b8860b")


def chip(txt, ok=True):
    c = VERDE if ok else AMBAR
    return Paragraph('<font color="#%s"><b>%s</b></font>' % (c.hexval()[2:], txt), CELLB)


def seccion_roja(titulo):
    t = Table([[Paragraph('<font color="white" size="13"><b>%s</b></font>' % titulo, BODY)]], colWidths=[W])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), RED),
                           ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                           ('TOPPADDING', (0, 0), (-1, -1), 7), ('BOTTOMPADDING', (0, 0), (-1, -1), 7)]))
    return t


# ============================================================ PORTADA
S.append(Paragraph("MÉTODO FLOW — SOLO CON SABOR", H1))
S.append(Paragraph(
    "Este documento reúne <b>todo lo que ya está decidido y todo lo que ya está producido</b>, para "
    "arrancar la mentoría con Nico sin perder tiempo repasando lo obvio. Separa dos cosas a propósito: "
    "<b>DECISIONES</b> (ya tomadas, algunas provisorias) y <b>ENTREGABLES</b> (material ya construido). "
    "Al final, la lista corta de lo que falta cerrar — y que es exactamente para eso que sirve la mentoría.", BODY))

S.append(Paragraph("EL PROYECTO EN 4 LÍNEAS", H2))
S.append(tabla([
    [Paragraph("<b>Modelo</b>", CELLB),
     Paragraph("Método FLOW de Nico Galliussi: pasar de clases 1 a 1 a un programa grupal online de "
               "alto valor para guitarristas.", CELL)],
    [Paragraph("<b>Nicho</b>", CELLB),
     Paragraph("Improvisación en rock/blues sobre <b>pentatónica menor con sabor</b>. La fusión mayor/menor "
               "queda como bonus avanzado, no como puerta de entrada.", CELL)],
    [Paragraph("<b>Avatar</b>", CELLB),
     Paragraph("Guitarrista hobbista, 28-45 años, autodidacta, 2-6 años tocando. Sabe la pentatónica menor "
               "caja 1 y poco más. Suena \"escolar\", quiere sonar a los discos que escucha.", CELL)],
    [Paragraph("<b>Promesa</b>", CELLB),
     Paragraph("\"De pentatónica caja 1 → improvisar con sabor en 90 días.\" Punto A: repetís siempre los "
               "mismos licks. Punto B: te movés por las 5 cajas con bending, vibrato y espacio.", CELL)],
], [2.6 * cm, W - 2.6 * cm]))

S.append(Paragraph("CÓMO LEER ESTE DOCUMENTO", H2))
S.append(tabla([
    [chip("✓ CERRADO", True), Paragraph("Decisión tomada. No hace falta volver a discutirla.", CELL)],
    [chip("~ PROVISORIO", False), Paragraph("Hay una decisión, pero está marcada para revisar con Nico.", CELL)],
    [chip("? ABIERTO", False), Paragraph("Todavía no se decidió. Es agenda de la mentoría.", CELL)],
], [3.4 * cm, W - 3.4 * cm]))

# ============================================================ IDENTIDAD Y NOMBRES
S.append(PageBreak())
S.append(seccion_roja("1 · IDENTIDAD DEL PROYECTO"))
S.append(Spacer(1, 8))
S.append(tabla([
    [Paragraph("<b>Ítem</b>", CELLB), Paragraph("<b>Estado</b>", CELLB), Paragraph("<b>Valor actual</b>", CELLB)],
    [Paragraph("Usuario de Instagram", CELL), chip("~ PROVISORIO", False),
     Paragraph("<b>@felibayamenor</b> — confirmar que sea exactamente así (sin tilde, sin mayúscula).", CELL)],
    [Paragraph("Nombre del programa", CELL), chip("~ PROVISORIO", False),
     Paragraph("<b>\"Solo con Sabor\"</b> — a Feli no lo convence del todo. No bloquea nada; se puede "
               "decidir en la mentoría o más adelante.", CELL)],
    [Paragraph("Keyword de CTA", CELL), chip("~ PROVISORIO", False),
     Paragraph("Rota por reel (PENTA, SOLO, ROCK, SABOR…). Keywords fijas ya asignadas: CLASE "
               "(reservada, aunque el video que la usaba se dio de baja del stock público).", CELL)],
    [Paragraph("Precio", CELL), chip("~ RECOMENDACIÓN", False),
     Paragraph("<b>USD 600</b> — no es el placeholder viejo (400): es el número al que convergieron 3 "
               "análisis independientes (el rango original de Nico, el sistema de venta recién armado, y "
               "el propio riesgo de \"grupal = barato\" que un video de Nico denuncia). 400 queda "
               "descartado como piso — tira justo hacia esa trampa. Confirmar en mentoría.", CELL)],
    [Paragraph("Garantía", CELL), chip("? ABIERTO", False),
     Paragraph("Dos propuestas armadas (30 días con devolución 100%, o 1ª clase). Sin elegir.", CELL)],
    [Paragraph("Fecha 1ª cohorte", CELL), chip("? ABIERTO", False),
     Paragraph("Sin definir. Es la decisión que más urge — desbloquea precio, keyword y ritmo de "
               "publicación.", CELL)],
], [3.4 * cm, 2.6 * cm, W - 6.0 * cm]))

# ============================================================ EL AVATAR Y LA PROMESA
S.append(Spacer(1, 10))
S.append(seccion_roja("2 · EL AVATAR (a quién le vendés)"))
S.append(Spacer(1, 8))
S.append(tabla([
    [Paragraph("<b>Quién es</b>", CELLB),
     Paragraph("Guitarrista hobbista, mayormente hombre, 28-45 años, 2-6 años tocando, autodidacta. "
               "Trabaja de otra cosa, toca 2-4 hs por semana en casa.", CELL)],
    [Paragraph("<b>Qué sabe</b>", CELLB),
     Paragraph("Acordes abiertos, power chords, la pentatónica menor caja 1 y poco más.", CELL)],
    [Paragraph("<b>Su dolor</b>", CELLB),
     Paragraph("\"Siempre suelto las mismas frases y suenan aburridas\" · \"Sé las cajas pero no sé "
               "conectarlas\" · \"Quiero sonar como Page/Slash/Hendrix pero no sé qué les falta a mis "
               "solos\" · mira tutoriales sueltos y nunca cierra la idea.", CELL)],
    [Paragraph("<b>Su deseo</b>", CELLB),
     Paragraph("Improvisar un solo de rock/blues que suene profesional y con sabor, no escolar.", CELL)],
    [Paragraph("<b>Tiene plata</b>", CELLB),
     Paragraph("Sí, si ve resultado real. No es un problema de presupuesto, es de confianza en el método.", CELL)],
], [2.6 * cm, W - 2.6 * cm]))

S.append(Spacer(1, 8))
S.append(Paragraph("REFERENTES / ESTILO DE LA MARCA", H3))
S.append(Paragraph(
    "Angus Young, Jimmy Page, Slash, Hendrix, Gary Moore, Joe Perry, Knopfler, Clapton, B.B. King, "
    "SRV, Billy Gibbons. Inspiración de formato de Instagram: personas que trabajaron con Nico — copy "
    "largo + destacada \"Método\".", BODY))

# ============================================================ LA OFERTA
S.append(PageBreak())
S.append(seccion_roja("3 · LA OFERTA (el qué vendés)"))
S.append(Spacer(1, 8))
S.append(tabla([
    [Paragraph("<b>Formato</b>", CELLB),
     Paragraph("Grupal online, <b>4 a 6 alumnos</b> por cohorte. No 1 a 1.", CELL)],
    [Paragraph("<b>Duración</b>", CELLB), Paragraph("12 semanas (3 meses).", CELL)],
    [Paragraph("<b>Tu tiempo</b>", CELLB),
     Paragraph("1-2 encuentros en vivo por semana para 4-6 personas + contenido pregrabado + grupo de "
               "WhatsApp de seguimiento. Bajó de 4 hs/semana (plan original) a esto — modelo de delivery "
               "inspirado en el caso Sergio Assat, decisión ya tomada.", CELL)],
    [Paragraph("<b>Precio</b>", CELLB),
     Paragraph("USD 600 recomendado (ver sección 1) — provisorio hasta confirmarlo con Nico. Rango "
               "original: 600-900, subir a 900 con 2 testimonios.", CELL)],
], [2.6 * cm, W - 2.6 * cm]))

S.append(Paragraph("EL DELIVERY REAL (no las 4 sesiones del plan original)", H3))
S.append(Paragraph(
    "El borrador original tenía 4 sesiones en vivo por semana (Lunes teoría, Martes técnica, Jueves "
    "repertorio, Sábado improvisación) — <b>ese plan quedó reemplazado</b>. El delivery vigente:", BODY))
S.append(tabla([
    [Paragraph("<b>Capa</b>", CELLB), Paragraph("<b>Qué es</b>", CELLB)],
    [Paragraph("Pregrabado", CELLB),
     Paragraph("Cubre lo que antes daban las 4 sesiones en vivo. Se graba una vez con los 3 cuadernillos "
               "ya escritos como guion — sirve para todas las cohortes, no se regraba cada vez.", CELL)],
    [Paragraph("1-2 vivos/semana", CELLB),
     Paragraph("Se reserva para lo que sí necesita presencia real: dudas puntuales, corrección "
               "personalizada, repertorio e improvisación con devolución.", CELL)],
    [Paragraph("WhatsApp", CELLB),
     Paragraph("Seguimiento constante entre encuentros — mensaje semanal con la tarea y qué viene.", CELL)],
], [3.2 * cm, W - 3.2 * cm]))
S.append(Paragraph(
    "El QUÉ se enseña cada semana (los 4 ángulos temáticos por hito, los solos de referencia, las "
    "consignas) sigue tal cual estaba diseñado — lo que cambió es cuántas veces por semana hay encuentro "
    "en vivo, no el contenido pedagógico.", SMALL))

S.append(Paragraph("LOS 3 HITOS (el camino de transformación)", H3))
S.append(tabla([
    [Paragraph("<b>Hito</b>", CELLB), Paragraph("<b>Qué logra el alumno</b>", CELLB),
     Paragraph("<b>Entregable-prueba</b>", CELLB)],
    [Paragraph("<b>1 · EL MAPA</b>", CELLB),
     Paragraph("Las 5 cajas de la pentatónica menor conectadas. Se mueve por todo el mástil.", CELL),
     Paragraph("Video recorriendo las 5 cajas sin pausa.", CELL)],
    [Paragraph("<b>2 · EL SABOR</b>", CELLB),
     Paragraph("Bending, vibrato, espacio, dinámica. Las frases suenan a música, no a ejercicio.", CELL),
     Paragraph("Video tocando 5 licks con sabor sobre backing + antes/después.", CELL)],
    [Paragraph("<b>3 · EL VOCABULARIO</b>", CELLB),
     Paragraph("Licks propios, robados honestamente a los grandes. Arma su propio solo.", CELL),
     Paragraph("<b>Solo propio de 1 minuto grabado</b> — su trofeo y tu testimonio.", CELL)],
], [3.4 * cm, W - 3.4 * cm - 4.2 * cm, 4.2 * cm]))
S.append(Paragraph(
    "Bonus post-programa (no entra en las 12 semanas): 6 licks más fuera de las cajas 1 y 2, para "
    "seguir creciendo después de terminar.", SMALL))

S.append(Paragraph("GARANTÍA — dos propuestas, sin elegir todavía", H3))
S.append(tabla([
    [Paragraph("<b>Opción</b>", CELLB), Paragraph("<b>Texto</b>", CELLB)],
    [Paragraph("1 · Participación (fuerte)", CELLB),
     Paragraph("\"Si venís a las clases, hacés las tareas y en 30 días no ves un cambio real en cómo "
               "suena tu solo, te devuelvo el 100%.\"", CELL)],
    [Paragraph("2 · Primera clase (suave)", CELLB),
     Paragraph("\"Si después de la primera semana sentís que no es para vos, te devuelvo todo, sin "
               "preguntas.\"", CELL)],
], [4.4 * cm, W - 4.4 * cm]))

# ============================================================ CONTENIDO PRODUCIDO — VIDEOS
S.append(PageBreak())
S.append(seccion_roja("4 · CONTENIDO YA GRABADO (8 videos)"))
S.append(Spacer(1, 8))
S.append(tabla([
    [Paragraph("<b>#</b>", CELLB), Paragraph("<b>Tema</b>", CELLB), Paragraph("<b>Formato</b>", CELLB),
     Paragraph("<b>Estado</b>", CELLB)],
    [Paragraph("1", CELLB), Paragraph("Recursos para tu pentatónica menor (sin hablar, toca)", CELL),
     Paragraph("A", CELL), chip("✓ Filmado")],
    [Paragraph("2", CELLB), Paragraph("\"5 acordes de la pentatónica para funkear tus solos\"", CELL),
     Paragraph("A", CELL), chip("✓ Filmado")],
    [Paragraph("3", CELLB), Paragraph("\"¿Hay que tocar rápido para sonar rockero?\"", CELL),
     Paragraph("C", CELL), chip("✓ Filmado")],
    [Paragraph("4", CELLB), Paragraph("\"¿Cuántas escalas necesitás?\"", CELL),
     Paragraph("C", CELL), chip("✓ Filmado + editado")],
    [Paragraph("5", CELLB), Paragraph("\"¿La pentatónica es de principiantes?\"", CELL),
     Paragraph("C", CELL), chip("✓ Filmado")],
    [Paragraph("6", CELLB), Paragraph("\"Tus solos no respiran\" (espacio)", CELL),
     Paragraph("C", CELL), chip("✓ Filmado")],
    [Paragraph("7", CELLB), Paragraph("\"¿El equipo arregla tu solo?\" (plugin vs ampli barato)", CELL),
     Paragraph("C", CELL), chip("~ 6.5 — falta grabar guitarras", False)],
    [Paragraph("8", CELLB), Paragraph("\"No tengo oído\" (cantá primero, tocá después)", CELL),
     Paragraph("C+conexión", CELL), chip("✓ Filmado, en edición")],
], [1.0 * cm, W - 6.7 * cm, 2.2 * cm, 3.5 * cm]))
S.append(Paragraph(
    "Formato A = Autoridad (alcance) · Formato C = Creencia atacada (conversión, el motor del embudo).", SMALL))

S.append(Paragraph("PRÓXIMOS A FILMAR — orden ya decidido (4 sesiones)", H2))
S.append(tabla([
    [Paragraph("<b>Orden</b>", CELLB), Paragraph("<b>Video</b>", CELLB), Paragraph("<b>Formato</b>", CELLB),
     Paragraph("<b>Nota</b>", CELLB)],
    [Paragraph("1º", CELLB), Paragraph("#7 — terminar (solo faltan las guitarras)", CELL), Paragraph("C", CELL),
     Paragraph("A medias hace rondas — se prioriza para no perder la continuidad del plano hablado ya "
               "filmado.", CELL)],
    [Paragraph("2º", CELLB), Paragraph("\"3 formas de romper las cajas\"", CELL), Paragraph("A", CELL),
     Paragraph("Blindado: cero decisiones abiertas, cero fact-check pendiente. Alimenta lead magnet "
               "PENTA.", CELL)],
    [Paragraph("3º", CELLB), Paragraph("REEL FIJADO", CELL), Paragraph("A (Autoridad)", CELL),
     Paragraph("No es hablado — \"partitura emocional\" de 30 seg. Va después de calentar la mano en la "
               "sesión anterior.", CELL)],
    [Paragraph("4º", CELLB), Paragraph("TU HISTORIA + VENDEDOR \"Como que desaparece\"", CELL),
     Paragraph("P + Conversión", CELL),
     Paragraph("Mismo setup (cara a cámara, sin tocar), se filman juntos. El vendedor se publica recién "
               "con autoridad ya construida (5-6 Formato C en el feed).", CELL)],
], [1.4 * cm, 5.6 * cm, 2.4 * cm, W - 9.4 * cm]))
S.append(Paragraph(
    "El vendedor \"Dejá de mirar tutoriales\" queda AFUERA de esta ronda: promete un lead magnet de \"3 "
    "licks con el cómo\" que todavía no existe como PDF. \"Cómo es una clase\" se sacó del stock público "
    "hace rondas: ese contenido corresponde a la llamada de descubrimiento, mano a mano — publicarlo le "
    "sacaría a la llamada su motivo de existir.", SMALL))

# ============================================================ MATERIAL DE CLASE
S.append(PageBreak())
S.append(seccion_roja("5 · MATERIAL DE CLASE (cuadernillos de ejercicios)"))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "El programa entero está respaldado por <b>53 ejercicios con numeración corrida</b> (más 2 anexos de "
    "ritmo, uno en paralelo a cada hito), "
    "cada uno con partitura real y tablatura hechas con LilyPond, diagramas de mástil verificados traste "
    "por traste, criterios claros de \"ya lo tenés\", y un entregable grabable por hito. No es un curso "
    "improvisado sobre la marcha: el contenido pedagógico de los 3 meses ya existe.", BODY))
S.append(tabla([
    [Paragraph("<b>Cuadernillo</b>", CELLB), Paragraph("<b>Contenido</b>", CELLB),
     Paragraph("<b>Ejerc.</b>", CELLB), Paragraph("<b>Pág.</b>", CELLB)],
    [Paragraph("Hito 1 — El Mapa", CELLB),
     Paragraph("Las 5 cajas conectadas por sus puentes. Cierra con un solo de 8 compases.", CELL),
     Paragraph("1-16", CELL), Paragraph("12", CELL)],
    [Paragraph("Hito 2 — El Sabor", CELLB),
     Paragraph("Ligados/slides → bending → vibrato → espacio y dinámica. Sale a la caja 2 en la "
               "semana 6 (bend a la tónica + blue note).", CELL),
     Paragraph("17-34", CELL), Paragraph("16", CELL)],
    [Paragraph("↳ Anexo — El Ritmo", CELLB),
     Paragraph("En paralelo al Hito 2 (no reemplaza semanas). Enseña a LEER ritmo — 10 células, "
               "basado en Pozzoli, entregable de 1 min. Vive en la máquina de Feli, no en este repo.", CELL),
     Paragraph("10 células", CELL), Paragraph("19", CELL)],
    [Paragraph("Hito 3 — El Vocabulario", CELLB),
     Paragraph("Escuela británica vs. americana, el color de cada grado, las notas de afuera, dos "
               "licks en las cajas 3 y 5, arquitectura del solo. Cierra con el solo final de 12 "
               "compases que recorre el mástil.", CELL),
     Paragraph("35-53", CELL), Paragraph("25", CELL)],
    [Paragraph("↳ Anexo — Ritmo y Construcción de Frases", CELLB),
     Paragraph("En paralelo al Hito 3. Enseña a APLICAR el ritmo (el árbol de las figuras, tresillo y "
               "swing, síncopa, el push, frases largas con cita real). Sí está en este repo.", CELL),
     Paragraph("A-J", CELL), Paragraph("13", CELL)],
    [Paragraph("Bonus post-programa", CELLB),
     Paragraph("6 licks más, fuera de las cajas 1 y 2 (cajas 3, 4, 5 y mástil completo). No es parte "
               "de las 12 semanas.", CELL),
     Paragraph("54-59", CELL), Paragraph("8", CELL)],
], [3.6 * cm, W - 3.6 * cm - 3.0 * cm, 1.6 * cm, 1.4 * cm]))
S.append(Paragraph(
    "<i>Los 2 anexos de ritmo son material EN PARALELO, no semanas nuevas — cierran el hueco de ritmo "
    "documentado como pendiente. El de Hito 2 vive solo en la carpeta de Feli; el de Hito 3 está en el "
    "repo (`Anexo-Ritmo-y-Construccion-de-Frases.pdf`).</i>", SMALL))
S.append(Paragraph(
    "<i>Pág. = páginas de la fuente que genera este repo. La versión maquetada que arma Claude Design "
    "para el alumno es más larga y agrega citas reales de discos (\"-bis\") a varios de estos "
    "ejercicios — no compite con la fuente, la expande.</i>", SMALL))
S.append(Spacer(1, 6))
S.append(tabla([
    [chip("✓ FIRME", True),
     Paragraph("Los 3 hitos + bonus ya pasaron <b>múltiples rondas de auditoría</b> (escala, distribución "
               "por caja, coherencia entre ejercicios, checklist vs. contenido real) — no es la primera "
               "revisión. Pedagógicamente está sólido y listo para dar clase con esto. Lo único que sigue "
               "puliéndose es la <b>estética de las tablaturas</b> en la maquetación de Design, un tema "
               "visual, no de contenido.", CELL)],
], [2.4 * cm, W - 2.4 * cm]))

S.append(Paragraph("LEAD MAGNETS (regalo por DM)", H3))
S.append(tabla([
    [Paragraph("<b>Archivo</b>", CELLB), Paragraph("<b>Keyword</b>", CELLB), Paragraph("<b>Va con</b>", CELLB)],
    [Paragraph("Mapa de las 5 cajas conectadas", CELL), Paragraph("PENTA", CELL),
     Paragraph("Video #5 y \"3 formas de romper las cajas\"", CELL)],
    [Paragraph("Rutina \"tocá 2, callate 2\"", CELL), Paragraph("SOLO", CELL),
     Paragraph("Video #6", CELL)],
    [Paragraph("Ejercicio \"destapar el oído\"", CELL), Paragraph("SOLO", CELL),
     Paragraph("Video #8", CELL)],
], [6.0 * cm, 2.4 * cm, W - 8.4 * cm]))

S.append(Paragraph("OTRO CONTENIDO LISTO", H3))
S.append(Paragraph(
    "4 carruseles diseñables (5 guitarristas/1 escala · los 4 ingredientes del sabor · 5 mentiras que "
    "te tienen trabado · anatomía de un solo que emociona) · glosario de edición CapCut · copy maestro "
    "adaptado del formato de personas que trabajaron con Nico.", BODY))

# ============================================================ EMBUDO Y PUBLICACIÓN
S.append(PageBreak())
S.append(seccion_roja("6 · EMBUDO Y ORDEN DE PUBLICACIÓN"))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "<i>Contenido orgánico IG (reels Formato C) → Perfil magnético (bio + reel fijado + destacadas) → "
    "DM (keyword) → Llamada de descubrimiento (15-20 min, por voz) → Venta.</i>", BODY))
S.append(Paragraph("Regla de oro: NO se vende en el DM. El DM solo agenda la llamada.", SMALL))

S.append(Paragraph("LAS 2 REGLAS DE SECUENCIA", H3))
S.append(tabla([
    [Paragraph("<b>1</b>", CELLB), Paragraph("Nunca dos videos de \"creencia atacada\" seguidos — cansa y "
                                              "suena a reto. Alternar Autoridad → Creencia → Personal.", CELL)],
    [Paragraph("<b>2</b>", CELLB), Paragraph("Los VENDEDORES se publican recién con autoridad ya construida "
                                              "(5-6 Formato C publicados) — nunca como primer contenido.", CELL)],
], [0.9 * cm, W - 0.9 * cm]))

S.append(Paragraph("REGLA 97/3 Y REGLA 70/30", H3))
S.append(tabla([
    [Paragraph("<b>97/3</b>", CELLB),
     Paragraph("El 97% del público se nutre con contenido (Formato A/C); solo el 3% está listo para "
               "comprar ya. Los vendedores apuntan a ese 3%.", CELL)],
    [Paragraph("<b>70/30</b>", CELLB),
     Paragraph("70% de los reels con Feli tocando bien (Formato C, convierte) · 30% análisis de solos "
               "ajenos (Formato A, construye alcance).", CELL)],
], [1.6 * cm, W - 1.6 * cm]))

# ============================================================ SISTEMA DE VENTA (NUEVO)
S.append(PageBreak())
S.append(seccion_roja("7 · SISTEMA DE VENTA — recién armado, sin probar en una llamada real"))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "Es exactamente lo que Nico cubre en el mes 3 de la mentoría (\"Conversión y Delivery\"). Se armó "
    "un borrador de los 4 documentos que faltaban, con la salvedad honesta de que <b>Feli nunca vendió "
    "high-ticket por voz</b> — esto necesita la mirada de Nico antes de una llamada real, no está "
    "pensado para reemplazarla.", BODY))
S.append(tabla([
    [Paragraph("<b>Documento</b>", CELLB), Paragraph("<b>Qué resuelve</b>", CELLB)],
    [Paragraph("Manejo de objeciones", CELLB),
     Paragraph("\"Es caro\", \"no tengo tiempo\", \"lo pienso\", \"¿y si no me sale?\" — guionado palabra "
               "por palabra, con la pregunta que se hace ANTES de responder cada una.", CELL)],
    [Paragraph("El momento del cierre", CELLB),
     Paragraph("La transición de \"te cuento el programa\" a decir el precio, los 3 finales posibles de "
               "la llamada guionados, y el seguimiento después de un \"lo pienso\".", CELL)],
    [Paragraph("Plantilla de DM", CELLB),
     Paragraph("Del comentario con keyword a la llamada agendada. Regla de oro: NO se vende en el DM, "
               "solo se agenda la llamada.", CELL)],
    [Paragraph("Precio, garantía y fecha", CELLB),
     Paragraph("Recomendación decidida (no un menú de opciones) para las 3 decisiones abiertas de la "
               "sección 1.", CELL)],
], [3.8 * cm, W - 3.8 * cm]))
S.append(Paragraph(
    "El precio de USD 600 (ver sección 1) salió de este ejercicio, cruzado con el rango original del "
    "propio método FLOW — no es un número inventado aparte.", SMALL))

# ============================================================ LO QUE FALTA CERRAR
S.append(PageBreak())
S.append(Paragraph("LO QUE QUEDA PARA LA MENTORÍA CON NICO", H1))
S.append(Paragraph(
    "Esta es la lista corta. Todo lo anterior ya está resuelto o producido — esto es lo que realmente "
    "necesita la mirada de Nico.", BODY))
S.append(tabla([
    [Paragraph("<b>#</b>", CELLB), Paragraph("<b>Decisión</b>", CELLB), Paragraph("<b>Qué se necesita</b>", CELLB)],
    [Paragraph("1", CELLB), Paragraph("Fecha de arranque de la 1ª cohorte", CELL),
     Paragraph("Es la que más urge: desbloquea el precio final, la keyword y el ritmo de publicación.", CELL)],
    [Paragraph("2", CELLB), Paragraph("Validar el precio de USD 600", CELL),
     Paragraph("Ya no es el placeholder de 400 — es una recomendación con análisis detrás (sección 7). "
               "Falta el visto bueno de Nico, no una decisión desde cero.", CELL)],
    [Paragraph("3", CELLB), Paragraph("Garantía", CELL),
     Paragraph("Elegir entre las 2 propuestas ya redactadas (30 días fuerte / 1ª clase suave).", CELL)],
    [Paragraph("4", CELLB), Paragraph("Revisar el sistema de venta antes de la 1ª llamada real", CELL),
     Paragraph("Objeciones, cierre y DM (sección 7) son un borrador — Feli nunca vendió high-ticket por "
               "voz. Practicarlo con Nico antes de usarlo con un prospecto real.", CELL)],
    [Paragraph("5", CELLB), Paragraph("Nombre del programa", CELL),
     Paragraph("\"Solo con Sabor\" no convence del todo a Feli. No bloquea el lanzamiento.", CELL)],
    [Paragraph("6", CELLB), Paragraph("Confirmar usuario de Instagram", CELL),
     Paragraph("@felibayamenor — validar formato exacto antes de imprimirlo en todo el material.", CELL)],
    [Paragraph("7", CELLB), Paragraph("Módulo 2 (futuro)", CELL),
     Paragraph("Ritmo y cambios de acorde quedaron fuera de las 12 semanas a propósito — es contenido "
               "post-programa, no un hueco a tapar ahora.", CELL)],
], [0.9 * cm, 4.4 * cm, W - 5.3 * cm]))

S.append(Spacer(1, 10))
S.append(caja_oscura(
    '<font color="white" size="10.5"><b>El estado real del proyecto</b></font><br/>'
    '<font color="#f7d7d2" size="9">7 videos completos + 1 a medias (falta terminar el #7) + 4 más con '
    'orden de filmación ya decidido. El programa pedagógico completo (53 ejercicios + anexo de ritmo), '
    'firme tras múltiples rondas de auditoría — pedagógicamente sólido, falta pulir estética de '
    'tablatura nomás. 3 lead magnets, 4 carruseles, el embudo diseñado, y ahora también un primer '
    'borrador del sistema de venta (objeciones, cierre, DM, precio). Lo que falta son decisiones y '
    'practicar la venta con Nico, no producción de contenido. · %s</font>' % IG, W))

doc.build(S)
print("OK Resumen-Ejecutivo-para-Nico.pdf")
