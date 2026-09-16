# -*- coding: utf-8 -*-
"""Arma la HOJA DE RUTA para el alumno -- el documento de bienvenida/orientacion de "Solo con
Sabor", no un cuadernillo de ejercicios. Explica como esta armado el programa completo: los 5
pilares, el horario semanal en vivo, y como funciona una clase.

Fuente de las decisiones que resume (memoria/02 SS28-QUATER, SS51 de memoria/06):
- Los 5 pilares corren en PARALELO durante todo el programa (no en bloques de 4 semanas).
- Horario confirmado: Lunes El Mapa, Martes El Sabor, Miercoles El Vocabulario + El Pulso,
  Jueves El Vuelo, 18-19hs (Argentina).
- La regla de los 10 minutos, las consultas asincronicas y el canal de seguimiento son de Nico.

Misma familia visual que los demas documentos (cuadernillo_comun.py).
"""
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Spacer

from cuadernillo_comun import (H1, H2, H3, BODY, SMALL, CELL, CELLB, IG,
                               documento, tabla, caja_oscura, MapaCompleto)

doc = documento("Hoja-de-Ruta-Solo-con-Sabor.pdf",
                "HOJA DE RUTA",
                "Cómo funciona el programa, de punta a punta",
                "Solo con Sabor · Hoja de Ruta",
                "Hoja de Ruta - Solo con Sabor")
W = doc.width
S = []

# ============================================================ 1. BIENVENIDA
S.append(Paragraph("BIENVENIDO A SOLO CON SABOR", H1))
S.append(Paragraph(
    "Este documento es tu mapa del programa completo — para que sepas siempre dónde estás parado y "
    "qué sigue. No hace falta que te lo aprendas de memoria: guardalo, es al que volvés cada vez que "
    "tengas la duda de \"¿y ahora qué toca?\".", BODY))
S.append(Paragraph(
    "La promesa es simple: hoy sabés la caja 1 de la pentatónica menor y sonás escolar — siempre las "
    "mismas frases, sin moverte del mástil. Al final de este camino improvisás con sabor por las 5 "
    "cajas, con bending, vibrato y licks que son tuyos. Ese es el trato, y todo lo que sigue es cómo "
    "llegamos ahí.", BODY))

# ============================================================ 2. CÓMO ESTÁ ARMADO
S.append(Paragraph("CÓMO ESTÁ ARMADO EL PROGRAMA", H2))
S.append(Paragraph(
    "Grupal, online, un grupo chico (4 a 6 personas) — no sos un número, y vas a aprender también de "
    "lo que le corrijo a tus compañeros. Tres partes se combinan todas las semanas:", BODY))
S.append(tabla([
    [Paragraph("<b>Parte</b>", CELLB), Paragraph("<b>Para qué te sirve</b>", CELLB)],
    [Paragraph("Zona virtual", CELL), Paragraph(
        "Tus cuadernillos de ejercicios (partitura + tablatura), los backings para practicar, y las "
        "grabaciones de cada clase en vivo. Es lo que usás entre semana, a tu ritmo.", CELL)],
    [Paragraph("Encuentros en vivo", CELL), Paragraph(
        "5 clases semanales, una por pilar. Ahí tocás vos, te corrijo en el momento, y escuchás la "
        "corrección de tus compañeros — eso también es aprender.", CELL)],
    [Paragraph("Comunidad", CELL), Paragraph(
        "Un canal (WhatsApp/Discord) para avisos, consultas entre clases, y para que no estudies "
        "solo.", CELL)],
], [3.4 * cm, W - 3.4 * cm]))

S.append(Spacer(1, 4))
S.append(Paragraph(
    "Un aviso honesto sobre el tiempo: no hay una fecha fija de \"semana 6\" o \"mes 2\". El ritmo "
    "típico, si sostenés tu práctica semanal, ronda los 3 meses — pero cada pilar dura lo que tiene "
    "que durar para vos, no lo que diga un calendario. Avanzás cuando estás listo, no cuando lo dice "
    "una fecha.", SMALL))

# ============================================================ 3. LOS 5 PILARES
S.append(Paragraph("LOS 5 PILARES", H2))
S.append(Paragraph(
    "El orden no es arbitrario: cada uno se apoya en el anterior. Vos los recorrés en este orden, "
    "aunque las 5 clases existan todas, todas las semanas, para que cada alumno del grupo vaya a la "
    "que le toca según dónde esté.", BODY))

S.append(Spacer(1, 4))
S.append(MapaCompleto(W, hs=11.5))
S.append(Spacer(1, 6))

PILARES = [
    ("PILAR 1 · EL MAPA — dominar el mástil",
     "Hoy conocés la caja 1 y quizás alguna más, pero las tenés sueltas en la cabeza. Acá dejás de "
     "ver 5 cajas separadas y empezás a ver un solo mástil: vas a saber, en cualquier punto, qué caja "
     "pisás y cómo llegar a la de al lado.",
     "Video recorriendo las 5 cajas sin pausa."),
    ("PILAR 2 · EL SABOR — bending, vibrato, expresión",
     "Ya sabés las notas — acá aprendés a que suenen a música. Bending que llega afinado, vibrato que "
     "es tuyo, y el silencio, que también es parte de la frase. Es la diferencia entre ejecutar y "
     "sonar.",
     "El solo de cierre del pilar + tu antes/después grabado."),
    ("PILAR 3 · EL VOCABULARIO — licks propios, estilo",
     "Te enseño a robarle frases a Page, a Slash, a Hendrix — y a transformarlas hasta que suenen "
     "tuyas. No copiás: te apropiás.",
     "Tu solo propio de 1 minuto. Tu trofeo."),
    ("PILAR 4 · EL PULSO — ritmo y tiempo",
     "De nada sirve tocar las notas justas si entran en el momento equivocado. Acá aprendés dónde cae "
     "cada nota respecto del tiempo — el ritmo que nadie te enseñó.",
     "1 minuto improvisando con al menos 3 frases que entren antes del tiempo fuerte."),
    ("PILAR 5 · EL VUELO — improvisando y soltándote en vivo",
     "Acá no aprendés nada nuevo — soltás todo lo anterior, en vivo, improvisando de verdad, con otro "
     "músico al lado. Es la prueba de que el mapa, el sabor, el vocabulario y el pulso ya son un solo "
     "idioma.",
     "Tu solo final de 1 minuto grabado — el cierre del programa."),
]
for titulo, cuerpo, entregable in PILARES:
    S.append(Paragraph(titulo, H3))
    S.append(Paragraph(cuerpo, BODY))
    S.append(Paragraph("<b>Tu entregable:</b> %s" % entregable, SMALL))
    S.append(Spacer(1, 3))

# ============================================================ 4. TU SEMANA EN VIVO
S.append(Spacer(1, 6))
S.append(Paragraph("TU SEMANA EN VIVO", H2))
S.append(Paragraph(
    "5 clases de 1 hora, Lunes a Jueves, 18 a 19hs (horario Argentina) — una por pilar:", BODY))
S.append(tabla([
    [Paragraph("<b>Día</b>", CELLB), Paragraph("<b>Horario</b>", CELLB), Paragraph("<b>Pilar</b>", CELLB)],
    [Paragraph("Lunes", CELL), Paragraph("18 a 19hs", CELL), Paragraph("EL MAPA", CELL)],
    [Paragraph("Martes", CELL), Paragraph("18 a 19hs", CELL), Paragraph("EL SABOR", CELL)],
    [Paragraph("Miércoles", CELL), Paragraph("18 a 19hs", CELL), Paragraph("EL VOCABULARIO", CELL)],
    [Paragraph("Miércoles", CELL), Paragraph("19 a 20hs", CELL), Paragraph("EL PULSO", CELL)],
    [Paragraph("Jueves", CELL), Paragraph("18 a 19hs", CELL), Paragraph("EL VUELO", CELL)],
], [4 * cm, 3.5 * cm, W - 7.5 * cm]))
S.append(Spacer(1, 4))
S.append(Paragraph(
    "No hace falta que te conectes a las 5 todas las semanas: vas a la clase del pilar en el que "
    "estás. A medida que avanzás, vas sumando las siguientes.", BODY))

# ============================================================ 5. CÓMO ES UNA CLASE
S.append(Paragraph("CÓMO ES UNA CLASE", H2))
S.append(tabla([
    [Paragraph("<b>1</b>", CELLB), Paragraph(
        "Nos conectamos a la hora indicada. Si en 10 minutos no hay nadie en la sala, la clase de ese "
        "día no se dicta — por eso siempre avisamos antes, por el canal, qué clase hay hoy.", CELL)],
    [Paragraph("<b>2</b>", CELLB), Paragraph(
        "¿No llegás a un horario? Dejá tu consulta por el canal antes de esa clase. La respondo igual, "
        "en la próxima sesión de ese mismo pilar — nadie se queda sin resolver su duda por no llegar "
        "al horario en vivo.", CELL)],
    [Paragraph("<b>3</b>", CELLB), Paragraph(
        "Cada clase termina con una tarea concreta para la semana. Un paso a la vez, no una lista de "
        "cosas sueltas.", CELL)],
], [0.8 * cm, W - 0.8 * cm]))

# ============================================================ 6. EL CANAL
S.append(Paragraph("EL CANAL DE WHATSAPP / DISCORD", H2))
S.append(Paragraph(
    "Sirve para tres cosas: avisos de horario, dejar tus consultas si no llegás a una clase, y "
    "comunidad — que no estudies solo. Si en algún momento pasan varios días y no te conectaste a "
    "ninguna clase, te voy a escribir yo directamente. No es para presionarte: es porque el programa "
    "rinde según lo sigas, y prefiero enterarme a tiempo antes de que te frustres solo con esto.",
    BODY))

# ============================================================ CIERRE
S.append(Spacer(1, 10))
S.append(caja_oscura(
    '<font color="white" size="10.5"><b>Cualquier duda con este documento, escribime directo.</b></font><br/>'
    '<font color="#f7d7d2" size="9">Esta es la última vez que empezás una canción y no la terminás '
    'como querías. Bienvenido a Solo con Sabor. · %s</font>' % IG, W))

doc.build(S)
print("OK Hoja-de-Ruta-Solo-con-Sabor.pdf")
