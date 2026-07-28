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
    [Paragraph("Precio", CELL), chip("~ PROVISORIO", False),
     Paragraph("<b>USD 400</b> \"fundadores\" — por debajo del rango original (600-900). Probablemente "
               "Nico empuje para arriba. Revisar en mentoría.", CELL)],
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
     Paragraph("~4 hs de vivo por semana para 4-6 personas (las mismas horas que antes le dabas a 1 solo "
               "alumno).", CELL)],
    [Paragraph("<b>Precio</b>", CELLB),
     Paragraph("USD 400 fundadores (provisorio, ver sección 1). Rango original sugerido por Nico: 600-900, "
               "subir a 900 con 2 testimonios.", CELL)],
], [2.6 * cm, W - 2.6 * cm]))

S.append(Paragraph("LAS 4 SESIONES SEMANALES", H3))
S.append(tabla([
    [Paragraph("<b>Día</b>", CELLB), Paragraph("<b>Sesión</b>", CELLB), Paragraph("<b>Qué pasa</b>", CELLB)],
    [Paragraph("Lunes", CELLB), Paragraph("Teoría / Q&A grupal", CELL),
     Paragraph("Resolver dudas de la semana (el video ya está en la plataforma).", CELL)],
    [Paragraph("Martes", CELLB), Paragraph("Técnica", CELL),
     Paragraph("Rutina de práctica guiada, todos tocan, vos corregís.", CELL)],
    [Paragraph("Jueves", CELLB), Paragraph("Repertorio", CELL),
     Paragraph("Análisis de un solo icónico por semana.", CELL)],
    [Paragraph("Sábado", CELLB), Paragraph("Improvisación", CELL),
     Paragraph("Cada alumno toca, devolución personalizada — la sesión joya.", CELL)],
], [1.8 * cm, 3.0 * cm, W - 4.8 * cm]))

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
    "Bonus post-programa (no entra en las 12 semanas): 8 licks más fuera de las cajas 1 y 2, para "
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

S.append(Paragraph("GUIONES ESCRITOS, TODAVÍA SIN FILMAR", H2))
S.append(tabla([
    [Paragraph("<b>Video</b>", CELLB), Paragraph("<b>Formato</b>", CELLB), Paragraph("<b>Nota</b>", CELLB)],
    [Paragraph("\"3 formas de romper las cajas\"", CELL), Paragraph("A", CELL),
     Paragraph("Alcance + alimenta lead magnet PENTA. Guion listo.", CELL)],
    [Paragraph("TU HISTORIA", CELL), Paragraph("P (Personal)", CELL),
     Paragraph("Guion FINAL con los 6 datos reales de Feli ya cargados. Listo para filmar.", CELL)],
    [Paragraph("REEL FIJADO", CELL), Paragraph("A (Autoridad)", CELL),
     Paragraph("No es hablado — es una \"partitura emocional\" de 30 seg (presenta/desarrolla/clímax/cierra).", CELL)],
    [Paragraph("VENDEDOR — \"Como que desaparece\"", CELL), Paragraph("Conversión", CELL),
     Paragraph("Filmar ya, publicar recién con autoridad construida (después de 5-6 Formato C).", CELL)],
    [Paragraph("VENDEDOR — \"Dejá de mirar tutoriales\"", CELL), Paragraph("Conversión", CELL),
     Paragraph("Mismo criterio de publicación que el anterior.", CELL)],
], [5.4 * cm, 2.8 * cm, W - 8.2 * cm]))
S.append(Paragraph(
    "\"Cómo es una clase\" se sacó del stock público: ese contenido corresponde a la llamada de "
    "descubrimiento, mano a mano — publicarlo le sacaría a la llamada su motivo de existir.", SMALL))

# ============================================================ MATERIAL DE CLASE
S.append(PageBreak())
S.append(seccion_roja("5 · MATERIAL DE CLASE (cuadernillos de ejercicios)"))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "El programa entero está respaldado por <b>51 ejercicios con numeración corrida</b> (más 8 de bonus), "
    "cada uno con partitura real y tablatura hechas con LilyPond, diagramas de mástil verificados traste "
    "por traste, criterios claros de \"ya lo tenés\", y un entregable grabable por hito. No es un curso "
    "improvisado sobre la marcha: el contenido pedagógico de los 3 meses ya existe.", BODY))
S.append(tabla([
    [Paragraph("<b>Cuadernillo</b>", CELLB), Paragraph("<b>Contenido</b>", CELLB),
     Paragraph("<b>Ejerc.</b>", CELLB), Paragraph("<b>Pág.</b>", CELLB)],
    [Paragraph("Hito 1 — El Mapa", CELLB),
     Paragraph("Las 5 cajas conectadas por sus puentes. Cierra con un solo de 8 compases.", CELL),
     Paragraph("1-16", CELL), Paragraph("11", CELL)],
    [Paragraph("Hito 2 — El Sabor", CELLB),
     Paragraph("Ligados/slides → bending → vibrato → espacio y dinámica. Sale a la caja 2 en la "
               "semana 6 (bend a la tónica + blue note).", CELL),
     Paragraph("17-34", CELL), Paragraph("11", CELL)],
    [Paragraph("Hito 3 — El Vocabulario", CELLB),
     Paragraph("Escuela británica vs. americana, el color de cada grado, arquitectura del solo. "
               "Cierra con el solo final de 12 compases.", CELL),
     Paragraph("35-51", CELL), Paragraph("16", CELL)],
    [Paragraph("Bonus post-programa", CELLB),
     Paragraph("8 licks más, fuera de las cajas 1 y 2 (cajas 3, 4, 5 y mástil completo). No es parte "
               "de las 12 semanas.", CELL),
     Paragraph("52-59", CELL), Paragraph("8", CELL)],
], [3.6 * cm, W - 3.6 * cm - 3.0 * cm, 1.6 * cm, 1.4 * cm]))

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
    [Paragraph("2", CELLB), Paragraph("Precio definitivo", CELL),
     Paragraph("USD 400 (provisorio) vs. el rango 600-900 que sugiere el propio método FLOW.", CELL)],
    [Paragraph("3", CELLB), Paragraph("Garantía", CELL),
     Paragraph("Elegir entre las 2 propuestas ya redactadas (30 días fuerte / 1ª clase suave).", CELL)],
    [Paragraph("4", CELLB), Paragraph("Nombre del programa", CELL),
     Paragraph("\"Solo con Sabor\" no convence del todo a Feli. No bloquea el lanzamiento.", CELL)],
    [Paragraph("5", CELLB), Paragraph("Confirmar usuario de Instagram", CELL),
     Paragraph("@felibayamenor — validar formato exacto antes de imprimirlo en todo el material.", CELL)],
    [Paragraph("6", CELLB), Paragraph("Módulo 2 (futuro)", CELL),
     Paragraph("Ritmo y cambios de acorde quedaron fuera de las 12 semanas a propósito — es contenido "
               "post-programa, no un hueco a tapar ahora.", CELL)],
], [0.9 * cm, 4.4 * cm, W - 5.3 * cm]))

S.append(Spacer(1, 10))
S.append(caja_oscura(
    '<font color="white" size="10.5"><b>El estado real del proyecto</b></font><br/>'
    '<font color="#f7d7d2" size="9">8 videos filmados + 5 guiones listos para filmar, el programa '
    'pedagógico completo (51 ejercicios + 8 de bonus), 3 lead magnets, 4 carruseles, y el embudo '
    'completamente diseñado. Lo que falta son decisiones de 5 minutos, no producción. · %s</font>' % IG, W))

doc.build(S)
print("OK Resumen-Ejecutivo-para-Nico.pdf")
