# -*- coding: utf-8 -*-
"""Guiones para filmar las clases PREGRABADAS del Hito 1 — El Mapa.

QUE ES: el guion palabra por palabra de los 4 videos que el alumno mira en la Zona Virtual,
uno por semana del cuadernillo. No son reels de Instagram: es el contenido de ensenanza del
programa, se graba UNA vez y sirve para todas las camadas.

POR QUE SE REESCRIBIO ENTERO (18/9, pedido de Feli para empezar a filmar los fines de semana).
La version anterior de este PDF (16/9) tenia dos problemas reales:

1. **Ensenaba bending y vibrato en el ejercicio 4.** Eso se saco del Hito 1 -- es tecnica del
   Hito 2, y el alumno todavia no la tiene (`memoria/10` SS35). El ej. 4 hoy se llama "Una frase,
   no una escala" y lo que cambia es el RITMO, no la mano. Si Feli filmaba con el guion viejo,
   grababa una clase que contradice el cuadernillo que el alumno tiene enfrente.
2. **Repartia los 16 ejercicios en 3 videos desparejos** (4 / 8 / 4). El del medio se comia media
   semana 2 y toda la 3.

Ahora son **4 videos, uno por semana del cuadernillo, 4 ejercicios cada uno**. El alumno mira el
video de la semana en la que esta: el video y el papel dicen lo mismo, en el mismo orden.

TODO EL CONTENIDO SALE DE `build_hito1.py` (la fuente del cuadernillo) y los datos de trastes de
`auditar_cajas.py`. Nada se escribio de memoria.

Salida: Guiones-Pregrabado-Hito1-El-Mapa.pdf

Uso:
    python3 scripts/build_guiones_pregrabado_h1.py
"""
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Spacer, PageBreak

from reportlab.platypus import Table, TableStyle

from cuadernillo_comun import (H1, H2, H3, BODY, SMALL, CELL, CELLB, RED, DARK, GREY,
                               documento, tabla, caja_oscura, score, par)

doc = documento("Guiones-Pregrabado-Hito1-El-Mapa.pdf",
                "CLASES PREGRABADAS — HITO 1: EL MAPA",
                "Guion palabra por palabra · 4 videos, uno por semana",
                "Solo con Sabor · Guiones pregrabado Hito 1",
                "Guiones pregrabado - Hito 1 El Mapa")
W = doc.width
S = []

# Estilos propios de este documento: el texto hablado tiene que distinguirse de un vistazo
# del texto que es instruccion de produccion. Filmando se lee de reojo.
DICE = ParagraphStyle('DICE', fontName='Helvetica', fontSize=10, leading=14.5,
                      textColor=DARK, leftIndent=12, spaceAfter=5,
                      borderPadding=0)
MUESTRA = ParagraphStyle('MUESTRA', fontName='Helvetica-Oblique', fontSize=9,
                         leading=12.5, textColor=GREY, leftIndent=12, spaceAfter=4)
TIEMPO = ParagraphStyle('TIEMPO', fontName='Helvetica-Bold', fontSize=9.5, leading=12,
                        textColor=RED, spaceBefore=9, spaceAfter=2)


def banner_video(n, titulo, subtitulo):
    """Como el `banner` de los cuadernillos, pero dice VIDEO en vez de SEMANA.

    No se toca el helper compartido: lo usan los 5 cuadernillos y ahi la palabra correcta
    es "semana". Aca el lector es Feli filmando, no el alumno practicando.
    """
    t = Table([[Paragraph('<font color="white" size="13"><b>VIDEO %s</b></font><br/>'
                          '<font color="white" size="10.5"><b>%s</b></font><br/>'
                          '<font color="#f7d7d2" size="8.5">%s</font>' % (n, titulo, subtitulo),
                          ParagraphStyle('bv', fontName='Helvetica', fontSize=10, leading=14))]],
              colWidths=[W])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), RED),
                           ('LEFTPADDING', (0, 0), (-1, -1), 10),
                           ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                           ('TOPPADDING', (0, 0), (-1, -1), 7),
                           ('BOTTOMPADDING', (0, 0), (-1, -1), 7)]))
    return t


def bloque(tiempo, titulo, muestra, dice, error=None, partitura=None):
    """Un tramo del guion: cuando, que se ve, que se dice, y el error que hay que nombrar."""
    S.append(Paragraph("%s &nbsp;·&nbsp; %s" % (tiempo, titulo.upper()), TIEMPO))
    if partitura:
        S.append(Spacer(1, 2))
        S.append(score(partitura, W * 0.97))
        S.append(Spacer(1, 3))
    if muestra:
        S.append(Paragraph("EN PANTALLA: %s" % muestra, MUESTRA))
    for parrafo in dice:
        S.append(Paragraph('"%s"' % parrafo, DICE))
    if error:
        S.append(Paragraph("<b>El error que tenés que nombrar:</b> %s" % error, SMALL))


def ficha(cubre, objetivo, pantalla, duracion):
    S.append(tabla([
        [Paragraph("<b>Cubre</b>", CELLB), Paragraph(cubre, CELL)],
        [Paragraph("<b>Objetivo</b>", CELLB), Paragraph(objetivo, CELL)],
        [Paragraph("<b>En pantalla</b>", CELLB), Paragraph(pantalla, CELL)],
        [Paragraph("<b>Duración</b>", CELLB), Paragraph(duracion, CELL)],
    ], [2.6 * cm, W - 2.6 * cm], header=False))
    S.append(Spacer(1, 4))


# ================================================================ PORTADA
S.append(Paragraph("LO QUE VAS A GRABAR", H1))
S.append(Paragraph(
    "Son <b>4 videos</b>, uno por cada semana del cuadernillo del Hito 1. El alumno mira el video de "
    "la semana en la que está y después practica con el papel: los dos dicen lo mismo, en el mismo "
    "orden. Se graban una sola vez y sirven para todas las camadas — es el contenido de la Zona "
    "Virtual, no un reel.", BODY))
S.append(Paragraph(
    "Cada guion de abajo tiene, para cada ejercicio: <b>la partitura</b> (para que no tengas que abrir "
    "el cuadernillo mientras filmás), <b>qué mostrás</b>, <b>qué decís</b> palabra por palabra, y "
    "<b>el error que tenés que nombrar</b> — ese último es el que convierte una demostración en una "
    "clase.", BODY))

S.append(Paragraph("EL PLAN DE GRABACIÓN", H2))
S.append(tabla([
    [Paragraph("<b>Video</b>", CELLB), Paragraph("<b>Título</b>", CELLB),
     Paragraph("<b>Cubre</b>", CELLB), Paragraph("<b>Dura</b>", CELLB)],
    [Paragraph("1", CELL), Paragraph("Tu casa: la caja 1", CELL),
     Paragraph("Semana 1 · ej. 1 a 4", CELL), Paragraph("~12 min", CELL)],
    [Paragraph("2", CELL), Paragraph("El primer puente", CELL),
     Paragraph("Semana 2 · ej. 5 a 8", CELL), Paragraph("~14 min", CELL)],
    [Paragraph("3", CELL), Paragraph("La zona aguda y la diagonal", CELL),
     Paragraph("Semana 3 · ej. 9 a 12", CELL), Paragraph("~16 min", CELL)],
    [Paragraph("4", CELL), Paragraph("Se cierra el círculo", CELL),
     Paragraph("Semana 4 · ej. 13 a 16", CELL), Paragraph("~16 min", CELL)],
], [1.4 * cm, 6.2 * cm, 5.2 * cm, W - 12.8 * cm]))
S.append(Spacer(1, 4))
S.append(Paragraph(
    "<b>Para filmar los fines de semana:</b> un video por sesión. Si te rinde el día, hacé dos — pero "
    "no arranques el 2 sin haber terminado el 1, porque los videos se referencian entre sí y filmarlos "
    "desordenados te obliga a acordarte de qué dijiste.", SMALL))

S.append(Paragraph("CÓMO SE FILMA (esto no cambia entre videos)", H2))
S.append(tabla([
    [Paragraph("<b>Encuadre</b>", CELLB), Paragraph(
        "<b>Cámara sobre el mástil, no sobre tu cara.</b> El alumno necesita ver los dedos. Tu cara "
        "aparece solo en la apertura y el cierre de cada video.", CELL)],
    [Paragraph("<b>Audio</b>", CELLB), Paragraph(
        "La guitarra grabada limpia y tu voz por encima. Si tenés que elegir, priorizá que se entienda "
        "la guitarra: es lo que el alumno va a copiar.", CELL)],
    [Paragraph("<b>Tono</b>", CELLB), Paragraph(
        "Profesor cerca de un alumno real, no locutor. Podés trabarte y seguir: esto no es un reel, es "
        "una clase. La energía pareja importa más que la edición perfecta.", CELL)],
    [Paragraph("<b>Tempo</b>", CELLB), Paragraph(
        "Todo lo que toques de demostración, tocalo <b>dos veces</b>: una muy lenta explicando, y una a "
        "tempo. El alumno necesita las dos.", CELL)],
    [Paragraph("<b>Metrónomo</b>", CELLB), Paragraph(
        "Cuando el ejercicio lo pide, que se ESCUCHE en el video. Practicar con metrónomo se aprende "
        "viéndolo, no leyéndolo.", CELL)],
], [2.6 * cm, W - 2.6 * cm], header=False))

S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white"><b>LA REGLA QUE SOSTIENE TODO EL HITO 1 — decila en los 4 videos</b><br/><br/>'
    'En este hito <b>no se enseña bending, ni vibrato, ni ninguna técnica de expresión.</b> Eso es el '
    'Hito 2. Acá se enseña GEOGRAFÍA: dónde están las notas y cómo se va de una zona a la otra.<br/><br/>'
    'Si mientras filmás te sale hacer un bending de puro reflejo, no pasa nada — pero <b>no lo '
    'expliques ni lo pidas</b>. El alumno todavía no tiene esa mano, y pedirle algo que no le enseñaste '
    'es la forma más rápida de que se sienta torpe y abandone.</font>', W))

# ================================================================ VIDEO 1
S.append(PageBreak())
S.append(banner_video(1, "TU CASA: LA CAJA 1",
                      "Semana 1 del cuadernillo · ejercicios 1 a 4"))
S.append(Spacer(1, 6))
ficha("Ejercicios 1, 2, 3 y 4",
      "Que la caja 1 le salga sin mirar el mástil, y que sepa dónde están sus tres LA.",
      "El diagrama de la caja 1 (trastes 5 a 8) fijo en una esquina, todo el video.",
      "~12 minutos")

bloque("0:00 - 1:00", "Apertura", "Tu cara. Guitarra en la mano, sin tocar todavía.", [
    "Bienvenido al Hito 1. Se llama El Mapa, y ya sé lo que estás pensando: 'la caja 1 me la sé de "
    "memoria'. Y es verdad, te la sabés. Pero mirá, te hago una pregunta incómoda: si te la sabés, "
    "¿por qué cuando improvisás seguís cayendo siempre en las mismas cuatro notas?",
    "Ese es el punto. No es que no sepas la caja. Es que la sabés como un dibujo, no como un lugar. "
    "En este mes eso se da vuelta. Y arrancamos hoy, acá, con la zona donde ya estás parado.",
    "Una cosa antes de empezar: en este hito no vamos a hacer bendings ni vibrato. Nada de eso. Eso "
    "viene después. Este mes es puro mapa — dónde están las notas y cómo se va de un lado al otro."])

bloque("1:00 - 3:30", "Ejercicio 1 — La caja 1, ida y vuelta",
       "Primero el diagrama, después las manos. Metrónomo audible a 60 BPM.", [
    "Un dedo por traste, y no negociamos esto: índice en el 5, anular en el 7, meñique en el 8. Si "
    "usás el dedo que te queda cómodo, en dos semanas no vas a poder tocar rápido y no vas a saber "
    "por qué.",
    "Subís las doce notas y bajás. Púa alternada desde el primer día — abajo, arriba, abajo, arriba — "
    "aunque te salga lentísimo. Te va a salir lento. Está bien que salga lento.",
    "Arrancamos a 60. La meta de la semana es 80 limpio, tres veces seguidas sin un error. Ojo con "
    "eso: tres veces SEGUIDAS. Una vez bien y dos mal no cuenta."],
    error="que una nota suene apagada y el alumno siga de largo. Decíselo con todas las letras: "
          "si una nota no suena, PARÁ ahí y arreglá el dedo. Seguir de largo es practicar el error.",
    partitura="e01")

bloque("3:30 - 6:00", "Ejercicio 2 — Las tónicas (dónde está tu casa)",
       "Señalás las tres tónicas en el diagrama antes de tocarlas.", [
    "Ahora las tres puertas de tu casa. Sexta cuerda traste 5. Cuarta cuerda traste 7. Primera cuerda "
    "traste 5. Las tres son la misma nota: LA.",
    "Vas a tocar cada una sola, dejándola sonar los dos tiempos, y vas a decir 'la' en voz alta. Sí, "
    "en voz alta, solo en tu cuarto, sintiéndote ridículo. Hacelo igual.",
    "Escuchá el último compás: bajo una frase y termino en el LA de la cuarta cuerda. ¿Escuchás cómo "
    "eso suena TERMINADO? Como cuando alguien termina una oración. Ese efecto lo vas a buscar toda tu "
    "vida como guitarrista, y empieza acá.",
    "Este ejercicio va con backing y SIN metrónomo. Acá no estamos entrenando la mano, estamos "
    "entrenando el oído."],
    error="creer que esto es teoría. No lo es: es para que sepas, sin mirar el mástil, cuándo "
          "llegaste a casa. Decíselo así.",
    partitura="e02")

bloque("6:00 - 8:30", "Ejercicio 3 — Secuencia de a 4",
       "Tocás primero la escala derecha, después la secuencia. El contraste es el contenido.", [
    "Te voy a ser honesto: este es el ejercicio más aburrido de todo el cuadernillo. Y es el que más "
    "se te va a notar. Te explico por qué.",
    "Escuchá esto: [tocás la escala derecha] — eso suena a alumno practicando. Ahora escuchá esto: "
    "[tocás la secuencia de a 4] — eso ya suena a música. Y son exactamente las mismas notas.",
    "La diferencia es que la mano aprendió a cambiar de dirección. Cuando tocás una escala de corrido, "
    "sonás a escala. Punto. No hay forma de que suene a otra cosa.",
    "60 BPM, meta 75. Y si te trabás: hacé solo el primer compás veinte veces antes de seguir. No "
    "veinte veces el ejercicio entero — veinte veces el compás que no te sale."],
    error="pasarlo rápido porque aburre. Justamente por eso hay que quedarse.",
    partitura="e03")

bloque("8:30 - 11:30", "Ejercicio 4 — Una frase, no una escala",
       "Tocalo con el backing puesto, para que se escuche el silencio del arranque.", [
    "Cuatro tiempos, y acá no hay ningún truco nuevo en la mano. Mismas notas, misma caja, mismos "
    "dedos. Lo único que cambia es el RITMO.",
    "Fijate: hay un silencio al principio, y una nota larga en el medio. Nada más que eso. Y eso solo "
    "ya alcanza para que suene a frase y no a ejercicio.",
    "Esto es importante que lo entiendas ahora, porque te va a acompañar todo el programa: lo que hace "
    "que algo suene a música no son las notas. Es cuándo entran y cuánto duran.",
    "Repetilo diez veces por día toda la semana. Tocalo con el backing y prestá atención a una sola "
    "cosa: que respetes el silencio del principio. Vas a querer entrar antes. No entres."],
    error="entrar antes de tiempo para llenar el silencio. Es el reflejo de todo el mundo. Nombralo "
          "antes de que le pase.",
    partitura="e04")

bloque("11:30 - 12:00", "Cierre", "Volvés a tu cara.", [
    "Eso es la semana 1. Cuatro ejercicios, una sola caja, y tres notas que ya sabés encontrar sin "
    "mirar.",
    "La semana que viene sumamos la caja 2 — pero más importante que la caja nueva es lo otro que "
    "vamos a hacer: aprender a CRUZAR de una a la otra sin frenar. Ahí empieza el mapa de verdad.",
    "Practicá esta semana. Nos vemos en el video 2."])

# ================================================================ VIDEO 2
S.append(PageBreak())
S.append(banner_video(2, "EL PRIMER PUENTE",
                      "Semana 2 del cuadernillo · ejercicios 5 a 8"))
S.append(Spacer(1, 6))
ficha("Ejercicios 5, 6, 7 y 8",
      "Sumar la caja 2 y cruzar de la 1 a la 2 sin frenar. Es la semana del PUENTE.",
      "Los diagramas de la caja 1 y la caja 2 juntos, con los trastes 7 y 8 marcados en los dos.",
      "~14 minutos")

bloque("0:00 - 1:30", "Apertura", "Tu cara.", [
    "Antes de arrancar, tocá conmigo el ejercicio 1 de la semana pasada. Una vez. [lo tocás]",
    "Listo. Eso es de dónde venimos. Hoy sumamos territorio nuevo, pero quiero que te quede clarísimo "
    "algo desde el principio: la caja 2 NO es un dibujo nuevo que tenés que aprender de cero.",
    "La caja 2 arranca donde termina la 1. Comparten los trastes 7 y 8. Son las mismas notas, en el "
    "mismo mástil — es la continuación del mismo mapa. Si la aprendés como un dibujo suelto, vas a "
    "terminar con dos cárceles en vez de una."])

bloque("1:30 - 4:00", "Ejercicio 5 — La caja 2, ida y vuelta",
       "Señalá la tercera cuerda ANTES de tocar. Ahí está la trampa.", [
    "Mismo trabajo que el ejercicio 1, territorio nuevo. Trastes 7 a 10.",
    "Y acá prestá atención a una cosa, porque es donde se equivoca todo el mundo: en la tercera cuerda "
    "los trastes son 7 y 9. No 7 y 10. Nueve.",
    "No es un error del cuadernillo ni una excepción rara: es cómo está afinada la guitarra. La tercera "
    "cuerda está afinada distinto que las demás, y la escala se corre un traste ahí. Te va a pasar en "
    "las cinco cajas, así que acostumbrate ahora.",
    "60 BPM, meta 80."],
    error="tocar el 10 en la tercera cuerda por inercia. Mostrá cómo suena mal, a propósito, para que "
          "el oído lo reconozca solo.",
    partitura="e05")

bloque("4:00 - 6:00", "Ejercicio 6 — Las tónicas de la caja 2",
       "Marcá la 4ª/7 en los DOS diagramas al mismo tiempo. Esa imagen es la clase entera.", [
    "Dos LA nuevos para ubicar: cuarta cuerda traste 7, y segunda cuerda traste 10.",
    "Pará un segundo en el primero. Cuarta cuerda, traste 7. ¿Te suena? Es el mismo que ya tenías en la "
    "caja 1. La misma nota, el mismo traste, el mismo dedo.",
    "Eso no es una casualidad: ESE es el puente. Una sola nota que pertenece a las dos cajas a la vez. "
    "Ahí es por donde vas a cruzar.",
    "Mismo trabajo que la semana pasada: con backing, y decís 'la' en voz alta cada vez."],
    partitura="e06")

bloque("6:00 - 9:30", "Ejercicio 7 — EL PUENTE",
       "Lentísimo primero, mostrando el dedo que se desliza. Después a tempo.", [
    "Este es el ejercicio más importante del mes. Si de todo el hito te llevás uno solo, que sea éste.",
    "Subís por la caja 1, normal, como venís haciendo. Y cuando llegás a la primera cuerda, hacés un "
    "slide del traste 8 al 10. Eso es todo. Ya estás en la caja 2, y bajás por ahí.",
    "Un solo movimiento. Sin frenar. Sin mirar el mástil. Sin pensar 'ahora cambio de caja'.",
    "Y escuchá bien esto: el slide no es un adorno. No lo estoy poniendo para que suene lindo. El slide "
    "es el VEHÍCULO — es lo que te lleva de una zona a la otra. Sacale el slide y te quedan dos cajas "
    "separadas otra vez.",
    "60 BPM. Y cuando te salga, probá el mismo cruce en la segunda cuerda, del 8 al 10, y en la tercera, "
    "del 7 al 9. Es exactamente la misma idea en otra cuerda."],
    error="frenar antes del slide para acomodar la mano. Ese micro-freno es lo que delata que "
          "todavía son dos cajas. Mostralo mal a propósito y después bien.",
    partitura="e07")

bloque("9:30 - 13:00", "Ejercicio 8 — Un lick que cruza las dos cajas",
       "Tocalo con backing. Que se escuche como música, no como ejercicio.", [
    "Ahora una frase completa: arranca en la caja 1 y termina en la caja 2, con el mismo slide del "
    "ejercicio anterior.",
    "Esto ya no es un ejercicio de digitación, es música. Tocalo con el backing.",
    "Y te marco a dónde vamos: cuando puedas tocar esto sin pensarlo, dejaste de tener dos cajas. "
    "Tenés una sola zona de seis trastes. Esa es la diferencia entre saberte las cajas y tener un mapa.",
    "Repetilo diez veces por día. Y después — esto es lo que más te va a servir — improvisá cinco "
    "minutos usando SOLO estas dos cajas. Sin partitura, lo que se te ocurra, pero sin salir de ahí."],
    partitura="e08")

bloque("13:00 - 13:30", "Cierre", "Tu cara.", [
    "Semana 2 lista. Dos cajas y un puente entre ellas.",
    "La semana que viene es la más cargada de todas, y también la más divertida: sumamos las cajas 3 y "
    "4, que es donde viven los solos que te gustan. Y hacemos el ejercicio que le da nombre a todo "
    "esto: el recorrido en diagonal.",
    "Practicá el puente. Nos vemos."])

# ================================================================ VIDEO 3
S.append(PageBreak())
S.append(banner_video(3, "LA ZONA AGUDA Y LA DIAGONAL",
                      "Semana 3 del cuadernillo · ejercicios 9 a 12"))
S.append(Spacer(1, 6))
ficha("Ejercicios 9, 10, 11 y 12",
      "Dos cajas nuevas, dos puentes más, y el recorrido diagonal — el ejercicio clave del hito.",
      "Los diagramas de la caja 3 y la 4. Para el ejercicio 12, el mapa del mástil completo.",
      "~16 minutos")

bloque("0:00 - 1:00", "Apertura", "Tu cara.", [
    "Esta es la semana más cargada del mes. Te lo digo de entrada para que no te asustes: son cuatro "
    "ejercicios y dos cajas nuevas.",
    "Y te doy permiso para algo: si llegás al viernes y sentís que no llegaste con todo, priorizá el "
    "ejercicio 12 por encima de cualquier otro. Es el que junta todas las piezas. Los demás son "
    "preparación para ése.",
    "También es la semana más divertida, porque es la zona del mástil donde viven los solos que te "
    "gustan."])

bloque("1:00 - 3:30", "Ejercicio 9 — La caja 3, ida y vuelta",
       "Trastes 9 a 13.", [
    "La caja 3 es la más cómoda de las cinco. Casi todo cae en el traste 10 y el 12, así que la mano "
    "casi no trabaja. Te va a salir en dos minutos.",
    "Y ahí está la trampa. Justamente porque es fácil, medio mundo se queda a vivir acá. Es la segunda "
    "cárcel más común después de la caja 1.",
    "Así que aprendela bien, pero no te enamores. 60 BPM, meta 80."],
    error="quedarse practicando esta caja de más porque es la que sale fácil.",
    partitura="e09")

bloque("3:30 - 6:00", "Ejercicio 10 — La caja 4, ida y vuelta",
       "Mostrá bien de cerca DÓNDE apoyás el dedo respecto del metal.", [
    "Trastes 12 a 15. Y acá cambia algo físico: los trastes son más angostos que abajo.",
    "Eso quiere decir que tenés que apretar cerca del metal y con MENOS fuerza, no con más. Mirá "
    "[mostrás]: acá, pegadito al traste. No en el medio del espacio.",
    "Regla práctica: si sentís que tenés que hacer fuerza, no es que te falta mano. Es que estás "
    "poniendo el dedo demasiado atrás. Movelo adelante y la nota sale sola.",
    "60 BPM, meta 75. Y algo que te pido en serio: si te duele la mano, parás. No se entrena con dolor. "
    "Nunca."],
    error="apretar fuerte en la zona aguda. Es la causa número uno de manos doloridas y de gente que "
          "abandona.",
    partitura="e10")

bloque("6:00 - 9:00", "Ejercicio 11 — Dos puentes encadenados",
       "Contá en voz alta los dos slides mientras los hacés.", [
    "Ahora dos slides seguidos, uno atrás del otro. Del 10 al 12 en la primera cuerda: entrás a la "
    "caja 3. Del 10 al 13 en la segunda: entrás a la caja 4.",
    "Terminás en una nota larga, tercera cuerda traste 14. Esa nota es un LA. Por eso suena a llegada, "
    "por eso el ejercicio 'cierra' — no es casualidad, es la tónica otra vez.",
    "Lento. 55 BPM si hace falta. Acá la prolijidad de los slides importa muchísimo más que la "
    "velocidad: un slide sucio suena a error, un slide limpio suena a intención."],
    partitura="e11")

bloque("9:00 - 14:30", "Ejercicio 12 — EL RECORRIDO DIAGONAL",
       "El mapa completo en pantalla. Tocalo TRES veces: lentísimo, medio, y a tempo.", [
    "Llegamos. Este es el ejercicio que le da sentido a todo el mes.",
    "Hasta ahora pensaste en cajas: subo dentro de una zona, bajo dentro de una zona, cruzo a la de al "
    "lado. Acá dejás de pensar en cajas.",
    "Lo que vas a hacer es atravesar el mástil en DIAGONAL: subís de a poco por cada cuerda, y mientras "
    "tanto vas cruzando cuatro cajas sin darte cuenta. No hay un momento donde 'cambiás de caja'. "
    "Simplemente te movés.",
    "Y esto es exactamente lo que hacen Page o Slash cuando parece que se van a cualquier lado del "
    "mástil y nunca se pierden. No tienen cinco dibujos en la cabeza. Tienen uno solo, largo.",
    "55 BPM y con paciencia. Te lo digo de verdad: este ejercicio solo, hecho todos los días, ya "
    "justifica el mes entero. Si hacés solo esto, ya ganaste."],
    error="tocarlo rápido antes de tenerlo limpio. Acá la velocidad no prueba nada — lo que se "
          "entrena es que la mano no dude en los cruces.",
    partitura="e12")

bloque("14:30 - 15:00", "Cierre", "Tu cara.", [
    "Eso es la semana 3. Cuatro cajas y el mástil empezando a ser uno solo.",
    "La semana que viene cerramos: falta una sola caja, la 5, que es la que casi nadie usa y la que más "
    "te va a servir. Y ahí vas a ver por qué todo esto es un círculo y no una fila.",
    "Y al final de esa semana grabás tu solo. Practicá la diagonal."])

# ================================================================ VIDEO 4
S.append(PageBreak())
S.append(banner_video(4, "SE CIERRA EL CÍRCULO",
                      "Semana 4 del cuadernillo · ejercicios 13 a 16"))
S.append(Spacer(1, 6))
ficha("Ejercicios 13, 14, 15 y 16",
      "La última caja, la vuelta completa al mástil, y el solo de evaluación que el alumno graba.",
      "El diagrama de la caja 5 y, sobre el final, el mapa del mástil completo.",
      "~16 minutos")

bloque("0:00 - 1:00", "Apertura", "Tu cara.", [
    "Última semana del Hito 1. Falta una sola caja, y es la que casi nadie usa: la caja 5.",
    "Vive DEBAJO de la caja 1, entre los trastes 2 y 5. Es la zona grave, la de los riffs. Y es la que "
    "más te va a servir justamente porque casi nadie baja hasta ahí.",
    "Al final de este video está tu entregable del mes, así que prestá atención hasta el final."])

bloque("1:00 - 3:30", "Ejercicio 13 — La caja 5, ida y vuelta",
       "Mostrá el estirón de la cuarta y la tercera cuerda bien de cerca.", [
    "Trastes 2 a 5. Y te aviso de entrada: esta es la caja más incómoda de las cinco.",
    "Mirá la cuarta cuerda y la tercera: las notas son el 2 y el 5. Eso es un estirón de tres trastes, "
    "y abajo del mástil los trastes son anchos. Se siente raro.",
    "Es normal. No la estás haciendo mal, no te falta mano, no tenés los dedos cortos. Es incómoda para "
    "todos. Tomátela con calma.",
    "60 BPM, meta 75."],
    error="pensar que la incomodidad es culpa suya. Decíselo explícitamente — es el momento del hito "
          "donde más gente se frustra.",
    partitura="e13")

bloque("3:30 - 6:00", "El regalo de las cuerdas al aire",
       "Tocá la caja 5 dejando sonar la sexta al aire. El contraste tiene que escucharse.", [
    "Antes de seguir, quiero mostrarte algo que tiene la guitarra y casi nadie aprovecha.",
    "La caja 5 llega hasta el traste 2. ¿Y abajo qué hay? Las cuerdas al aire. Y acá viene lo lindo: de "
    "las seis cuerdas al aire, CINCO son notas de la pentatónica de La menor. Sexta MI, quinta LA, "
    "cuarta RE, tercera SOL, primera MI. La única que se sale es la segunda, que es un SI.",
    "O sea que tu guitarra, sin que le pises absolutamente nada, ya está sonando casi entera en la "
    "escala que estás estudiando.",
    "Eso te da tres cosas gratis. Una: una nota que sigue sonando sola mientras tu mano se muda de "
    "posición. Dos: un pedal grave para dejar sonando abajo. Y tres: otro timbre — la cuerda al aire "
    "suena más abierta y más larga que la misma nota pisada. Escuchá [mostrás las dos].",
    "Esto no está escrito en ningún ejercicio del cuadernillo, y es a propósito. Es tuyo para explorar."])

bloque("6:00 - 8:30", "Ejercicio 14 — El círculo: de la caja 5 a la caja 1",
       "Este es el momento del mapa completo en pantalla.", [
    "Subís por la caja 5 y cuando llegás a la primera cuerda traste 5... ya estás en la caja 1.",
    "No hay slide. No hay salto. No hay nada que hacer. Es la misma nota.",
    "Y ahí está la idea que cierra el mes entero: las cinco cajas no son una fila que empieza en la 1 y "
    "termina en la 5. Son un CÍRCULO. Después de la 5 viene la 1 otra vez, una octava más arriba, y "
    "así para siempre.",
    "El mástil no se te va a terminar nunca. Siempre hay una caja más, y siempre es una que ya sabés.",
    "60 BPM, y tocalo mirando el mapa completo mientras lo hacés."],
    partitura="e14")

bloque("8:30 - 11:00", "Ejercicio 15 — Bajar el mástil en diagonal",
       "Mostrá el mapa y señalá las 5 cajas mientras pasás por ellas.", [
    "El movimiento contrario al ejercicio 12: desde la caja 4 hasta la caja 5, bajando en diagonal.",
    "Y cuesta más que subir. Te lo adelanto para que no te frustres: casi todo el mundo sabe subir por "
    "el mástil y no sabe volver.",
    "Pensá lo que significa eso en un solo. Un solo que sube y no baja se queda sin final — se termina "
    "arriba, gritando, y no resuelve nunca. Bajar es lo que te deja cerrar.",
    "55 BPM. Y fijate en los carteles del ejercicio: en dos compases pasás por las cinco cajas. Dos "
    "compases."],
    error="practicar solo el ejercicio 12 y saltear éste. Son la ida y la vuelta del mismo camino.",
    partitura="e15")

bloque("11:00 - 15:30", "Ejercicio 16 — EL SOLO DE EVALUACIÓN",
       "Tocalo entero con backing, sin hablar encima. Después explicalo por partes.", [
    "Y llegamos a tu entregable. Ocho compases que recorren las cinco cajas.",
    "Primero escuchalo entero, sin que yo hable encima. [lo tocás con el backing]",
    "Ahora te lo desarmo. Usa todo lo del mes: espacio, ritmo variado, slides para cruzar, y un cierre "
    "en la tónica. Nada que no hayas practicado estas cuatro semanas.",
    "Una aclaración importante: esto NO es un examen de velocidad. Es un examen de mapa. No me importa "
    "a qué tempo lo toques. Me importa que se escuche que sabés dónde estás parado en cada momento.",
    "Aprendételo, tocalo sobre el backing, grabalo y mandámelo. Ese video es tu Hito 1 cerrado."],
    error="correrlo para que suene impresionante. Repetí que el criterio es el territorio, no el "
          "tempo — si no, todos lo mandan rápido y sucio.",
    partitura="e16")

bloque("15:30 - 16:00", "Cierre del hito", "Tu cara. Este cierre es el más importante de los cuatro.", [
    "Eso es el Hito 1. Un mes.",
    "Y quiero que pares un segundo a mirar lo que cambió. Hace cuatro semanas tenías una caja y un "
    "montón de dudas. Hoy tenés cinco cajas, cuatro puentes, y sabés bajar el mástil en diagonal.",
    "Pero lo que de verdad cambió no son las cinco cajas. Es que dejaste de verlas como cinco cosas.",
    "En el Hito 2 empieza otra historia completamente distinta. Ya no vamos a hablar de dónde están las "
    "notas — eso ya lo sabés. Vamos a hablar de CÓMO las tocás. Bending, vibrato, el silencio. Todo lo "
    "que hace que las mismas notas suenen a vos y no a un ejercicio.",
    "Mandame tu solo. Nos vemos en El Sabor."])

# ================================================================ CHECKLIST
S.append(PageBreak())
S.append(Paragraph("CHECKLIST DE GRABACIÓN", H1))
S.append(Paragraph(
    "Para tener al lado el día que filmás. Los tres bloques son de momentos distintos: lo de "
    "\"antes\" se hace una sola vez por sesión, lo de \"durante\" se chequea por video.", BODY))

S.append(Paragraph("ANTES DE PRENDER LA CÁMARA", H3))
S.append(tabla([
    [Paragraph("<b>1</b>", CELLB), Paragraph(
        "Leé el guion del video entero una vez, en voz alta. No para memorizarlo — para que las frases "
        "no te suenen nuevas cuando estés grabando.", CELL)],
    [Paragraph("<b>2</b>", CELLB), Paragraph(
        "Tocá los 4 ejercicios del video, seguidos, a tempo. Si alguno no te sale redondo, ensayalo "
        "ahora: no hay nada peor que descubrirlo con la cámara prendida.", CELL)],
    [Paragraph("<b>3</b>", CELLB), Paragraph(
        "Backing track de La menor cargado y a mano. Los ejercicios 2, 4, 8 y 16 lo piden.", CELL)],
    [Paragraph("<b>4</b>", CELLB), Paragraph(
        "Metrónomo listo y que se escuche en la grabación, no solo en tus auriculares.", CELL)],
    [Paragraph("<b>5</b>", CELLB), Paragraph(
        "Los diagramas de las cajas del video, listos para poner en pantalla en la edición.", CELL)],
], [0.8 * cm, W - 0.8 * cm], header=False))

S.append(Paragraph("DURANTE", H3))
S.append(tabla([
    [Paragraph("<b>1</b>", CELLB), Paragraph(
        "La cámara mira el MÁSTIL. Tu cara solo en la apertura y el cierre.", CELL)],
    [Paragraph("<b>2</b>", CELLB), Paragraph(
        "Cada demostración, dos veces: lenta explicando, y a tempo.", CELL)],
    [Paragraph("<b>3</b>", CELLB), Paragraph(
        "Nombrá el error de cada ejercicio. Es lo que separa una clase de una demostración.", CELL)],
    [Paragraph("<b>4</b>", CELLB), Paragraph(
        "Cero bending, cero vibrato, cero técnica del Hito 2. Ni de ejemplo.", CELL)],
    [Paragraph("<b>5</b>", CELLB), Paragraph(
        "Si te trabás, no cortes: repetí la frase y seguí. Se arregla en la edición y la energía se "
        "mantiene.", CELL)],
], [0.8 * cm, W - 0.8 * cm], header=False))

S.append(Paragraph("DESPUÉS", H3))
S.append(tabla([
    [Paragraph("<b>1</b>", CELLB), Paragraph(
        "Mirá el video entero una vez antes de darlo por bueno. Buscá una sola cosa: que se vea CLARO "
        "qué dedo está en qué traste. Si eso no se ve, el video no sirve por más bien que hables.", CELL)],
    [Paragraph("<b>2</b>", CELLB), Paragraph(
        "Subtítulos. El alumno lo va a mirar con la guitarra en la mano y a veces sin sonido.", CELL)],
    [Paragraph("<b>3</b>", CELLB), Paragraph(
        "Guardá el proyecto de edición. Cuando cambie un ejercicio del cuadernillo vas a querer "
        "regrabar solo ese tramo, no el video entero.", CELL)],
], [0.8 * cm, W - 0.8 * cm], header=False))

S.append(Spacer(1, 10))
S.append(caja_oscura(
    '<font color="white"><b>SI TENÉS UN SOLO FIN DE SEMANA, GRABÁ EL VIDEO 1.</b><br/><br/>'
    '<font color="#f7d7d2">Es el único que un alumno nuevo necesita para arrancar: la caja 1 es el '
    'único pilar sin prerrequisitos. Los otros tres se graban mientras el primer alumno cursa la '
    'semana 1 — no hace falta tener el hito entero filmado para abrir la puerta.</font></font>', W))

doc.build(S)
print("OK Guiones-Pregrabado-Hito1-El-Mapa.pdf")
