# -*- coding: utf-8 -*-
"""Arma el PDF del cuadernillo POST-PROGRAMA — 6 licks fuera de las cajas 1 y 2.

Requiere que antes se haya corrido `gen_scores_h3b.py` (genera ./partituras/e54..e59).
"""
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle

from cuadernillo_comun import (H1, H2, BODY, SMALL, CELL, CELLB, CAJ, IG, RED,
                               Diagrama, MapaCompleto, documento, tabla, par,
                               caja_oscura, ejercicio, TablaturaEnBlanco)

doc = documento("Cuadernillo-BONUS-Licks-Fuera-de-la-Caja1.pdf",
                "8 LICKS FUERA DE LA CAJA 1",
                "Bonus post-programa — vocabulario en las cajas 3, 4, 5 y por todo el mástil",
                "Solo con Sabor · Bonus — Licks fuera de la caja 1",
                "Bonus - Licks fuera de la caja 1")
W = doc.width
S = []

# Helvetica no trae los simbolos de alteracion; van con la fuente auxiliar.
BEM = '<font name="Sym">\u266d</font>'
SOS = '<font name="Sym">\u266f</font>'


def seccion(titulo, subtitulo):
    t = Table([[Paragraph('<font color="white" size="12.5"><b>%s</b></font><br/>'
                          '<font color="#f7d7d2" size="8.5">%s</font>' % (titulo, subtitulo),
                          ParagraphStyle('b', fontName='Helvetica', fontSize=10, leading=14))]],
              colWidths=[W])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), RED),
                           ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                           ('TOPPADDING', (0, 0), (-1, -1), 7), ('BOTTOMPADDING', (0, 0), (-1, -1), 7)]))
    return t


# ============================================================ INTRO
S.append(Paragraph("PARA CUÁNDO ES ESTE CUADERNILLO", H2))
S.append(Paragraph(
    "Este no es material del programa: es lo que sigue <b>después</b>. Terminaste los tres hitos, tenés el "
    "mapa, la voz y el vocabulario, y grabaste tu solo. Si querés seguir creciendo sin empezar otro método "
    "desde cero, el camino es éste — <b>llevar todo lo que ya sabés a las zonas del mástil que todavía no "
    "pisaste</b>.", BODY))
S.append(Paragraph(
    "En el programa ya pisaste las cinco cajas: el mapa entero en el Hito 1, y en el Hito 3 dos licks reales "
    "fuera de la caja 1 (el 47 en la caja 3 y el 48 en la caja 5) más un solo final que las recorre. "
    "Acá hay <b>seis licks y ninguno usa las cajas 1 ni 2 como territorio</b>: uno en la caja 3, dos en la 4, "
    "uno en la 5 y dos que recorren el mástil entero. La idea no es que sumes seis frases — es que termines "
    "de descubrir que <b>cada caja tiene un carácter propio</b>. Las mismas cinco notas suenan a riff en la "
    "zona grave y a grito en la aguda.", BODY))
S.append(Paragraph(
    "Ritmo recomendado: <b>un lick por semana</b>, sin apuro. Seis semanas de material.", SMALL))

S.append(Paragraph("LA NOTA NUEVA DE ESTE CUADERNILLO", H2))
S.append(Paragraph(
    "En el Hito 2 ya sumaste tu primera nota de fuera de la escala: el <b>MI" + BEM + "</b> "
    "(el <i>blue note</i>), usado siempre de paso. Acá se suma una sola más, y cambia el color de la frase "
    "en la dirección contraria:", BODY))
S.append(tabla([
    [Paragraph("<b>Nota</b>", CELLB), Paragraph("<b>Dónde</b>", CELLB), Paragraph("<b>Qué hace y cómo se usa</b>", CELLB)],
    [Paragraph("<b>FA" + SOS + "</b><br/>(6ª mayor)", CELLB), Paragraph("3ª cuerda,<br/>traste 11", CELL),
     Paragraph("Reemplaza a la 7ª menor y le saca la tristeza a la frase: suena dulce y elegante en vez de "
               "oscura. Es la nota del <b>\"BB box\"</b> y es la razón por la que B.B. King no suena como el "
               "resto de los bluseros. La usás en el lick 54.", CELL)],
], [3.2 * cm, 2.3 * cm, W - 5.5 * cm]))
S.append(Paragraph(
    "Fijate el contraste: el blue note <b>ensucia</b> y va de paso; la 6ª mayor <b>endulza</b> y se puede "
    "sostener. Son las dos direcciones en las que podés salirte de la pentatónica.", SMALL))

S.append(Paragraph("LOS 6 LICKS DE UN VISTAZO", H2))
S.append(tabla([
    [Paragraph("<b>#</b>", CELLB), Paragraph("<b>Caja</b>", CELLB), Paragraph("<b>Escuela</b>", CELLB),
     Paragraph("<b>Qué le robás</b>", CELLB)],
    [Paragraph("54", CELLB), Paragraph("3", CELL), Paragraph("B.B. King", CELL),
     Paragraph("Cambiar la 7ª menor por la <b>6ª mayor</b>. La nota dulce.", CELL)],
    [Paragraph("55", CELLB), Paragraph("4", CELL), Paragraph("David Gilmour", CELL),
     Paragraph("Siete notas en cuatro compases. Una sola, estirada, manda.", CELL)],
    [Paragraph("56", CELLB), Paragraph("4", CELL), Paragraph("Hendrix", CELL),
     Paragraph("Dobles cuerdas arriba: suena enorme sin tocar rápido.", CELL)],
    [Paragraph("57", CELLB), Paragraph("5", CELL), Paragraph("Gary Moore", CELL),
     Paragraph("Que la zona grave también cante, con espacio y vibrato.", CELL)],
    [Paragraph("58", CELLB), Paragraph("todas", CELL), Paragraph("Jimmy Page", CELL),
     Paragraph("La 1ª cuerda como ascensor: 4 cajas en 3 slides.", CELL)],
    [Paragraph("59", CELLB), Paragraph("todas", CELL), Paragraph("Slash", CELL),
     Paragraph("Bajar el mástil en diagonal, casi todo ligado.", CELL)],
], [1.0 * cm, 1.3 * cm, 3.6 * cm, W - 5.9 * cm]))

S.append(Paragraph(
    "<b>Sobre las partituras:</b> igual que en el Hito 3, estos licks son <b>originales</b>, escritos con el "
    "mecanismo característico de cada guitarrista y en la caja donde ese guitarrista realmente vive. No son "
    "transcripciones. En cada uno te digo qué escuchar para reconocer el recurso en su contexto original — "
    "porque el objetivo no es que toques como ellos, es que entiendas <b>por qué</b> lo que hacen funciona.", SMALL))

# ============================================================ CAJA 3
S.append(PageBreak())
S.append(seccion("CAJA 3 · trastes 9 a 13 — la caja cómoda (y su trampa)",
                 "Casi todo cae en el 10 y el 12. Es tan cómoda que medio mundo se queda a vivir acá."))
S.append(Spacer(1, 8))
S.append(par([Diagrama(3, W * 0.5),
              Paragraph("La zona más fácil de tocar y la más fácil de sobreexplotar. Su ventaja real es "
                        "el <b>registro</b>: acá arriba las mismas frases suenan más urgentes, más "
                        "desesperadas.<br/><br/>"
                        "Además es el barrio del <b>\"BB box\"</b>: la tónica de la 2ª cuerda traste 10, con "
                        "la 6ª mayor pegada en la 3ª cuerda traste 11.", BODY)],
             [W * 0.5, W * 0.5]))
S.append(Spacer(1, 4))

S.append(ejercicio(54, "El \"BB box\": la 6ª mayor", (
    "Acá está el secreto de por qué B.B. King no suena como el resto de los bluseros: <b>cambia la 7ª menor "
    "por la 6ª mayor</b> (FA" + SOS + ", 3ª cuerda traste 11). Esa nota no pertenece a la pentatónica menor, y le saca "
    "la tristeza a la frase — suena dulce, elegante, casi alegre. El movimiento de ir y venir entre la tónica "
    "(2ª cuerda, traste 10) y esa 6ª es la firma de la casa."),
    "e54", W,
    "Escuchá: B.B. King, «Sweet Little Angel» · «Every Day I Have the Blues». "
    "Con backing, lento. El vibrato de B.B. es rápido y angosto, casi un temblor controlado."))

# ============================================================ CAJA 4
S.append(PageBreak())
S.append(seccion("CAJA 4 · trastes 12 a 15 — el techo",
                 "El registro más agudo del mástil. Acá se va a los clímax, y no se vive."))
S.append(Spacer(1, 8))
S.append(par([Diagrama(4, W * 0.5),
              Paragraph("Es la zona más expresiva y la más peligrosa: si tocás mucho tiempo acá arriba, "
                        "cansás al oyente. La regla es simple — <b>la caja 4 es para el momento más alto "
                        "del solo, y después se baja</b>.<br/><br/>"
                        "Los trastes son angostos: apretá cerca del metal y con menos fuerza de la que "
                        "creés que hace falta.", BODY)],
             [W * 0.5, W * 0.5]))
S.append(Spacer(1, 4))

S.append(ejercicio(55, "Una nota, estirada una eternidad", (
    "Contá las notas: siete, en cuatro compases. El protagonista es un bending sostenido <b>cuatro tiempos "
    "enteros</b> con vibrato lento y ancho. Es lo contrario de todo lo que uno cree que hay que hacer en el "
    "registro agudo. Gilmour te hace llorar tocando menos notas que cualquiera de su generación."),
    "e55", W,
    "Escuchá: Pink Floyd, «Comfortably Numb» (segundo solo) · «Shine On You Crazy Diamond». "
    "Con backing lento. Si sentís que el compás 2 es demasiado largo, está bien: ése es el punto."))

S.append(ejercicio(56, "Dobles cuerdas arriba", (
    "Dos notas juntas en el registro agudo suenan <b>enormes sin tocar rápido</b>. Es la herencia del R&amp;B: "
    "Hendrix pensaba en acordes aunque estuviera soleando, y por eso sus solos suenan llenos incluso cuando "
    "está tocando poco. Cuidá que las dos cuerdas suenen parejas — si una se escucha más, estás inclinando la púa."),
    "e56", W,
    "Escuchá: Hendrix, «Little Wing» · «The Wind Cries Mary». "
    "70 BPM. Apagá con la mano derecha las cuerdas que no usás."))

# ============================================================ CAJA 5
S.append(PageBreak())
S.append(seccion("CAJA 5 · trastes 2 a 5 — el sótano",
                 "La menos usada de las cinco, y la que más carácter tiene. Acá las notas pesan."))
S.append(Spacer(1, 8))
S.append(par([Diagrama(5, W * 0.5),
              Paragraph("Nadie solea acá abajo, y es una lástima: es la zona con más personalidad del "
                        "mástil. Las mismas cinco notas, en este registro, <b>dejan de sonar a solo y "
                        "empiezan a sonar a riff</b>.<br/><br/>"
                        "Ojo con la digitación: en la 4ª y la 3ª cuerda las notas están en los trastes 2 y 5, "
                        "un estirón de tres trastes. Es incómoda — es normal.", BODY)],
             [W * 0.5, W * 0.5]))
S.append(Spacer(1, 4))

S.append(Paragraph(
    "El lick de riff de esta caja — el de Chuck Berry y AC/DC — <b>ya lo tenés: es el ejercicio 48 del "
    "Hito 3</b>. Lo que sigue es el otro lado de la misma zona.", SMALL))
S.append(Spacer(1, 4))

S.append(ejercicio(57, "Que la zona grave también cante", (
    "La caja 5 no es solo para riffs. Con espacio y vibrato, una frase grave suena <b>íntima</b>, como alguien "
    "hablando bajito. Y es el contraste perfecto: si presentás el solo acá abajo, cuando después subas a la "
    "caja 4 el salto va a emocionar el doble."),
    "e57", W,
    "Escuchá: Gary Moore en las partes tranquilas de «Parisienne Walkways». "
    "Con backing, muy lento. Dejá que la nota larga del compás 1 se estire de verdad."))

# ============================================================ TODO EL MÁSTIL
S.append(PageBreak())
S.append(seccion("TODO EL MÁSTIL — cuando las cajas dejan de existir",
                 "Los dos últimos licks no viven en ninguna caja: la atraviesan. Es a donde apunta todo."))
S.append(Spacer(1, 6))
S.append(MapaCompleto(W))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "El mapa completo otra vez, ahora con otro sentido: <b>la 1ª cuerda es un ascensor</b>. Los trastes 5, 8, "
    "10, 12 y 15 son notas de la escala, y cada uno pertenece a una caja distinta. Un slide entre dos de ellos "
    "te muda de zona sin que tengas que pensar en formas.", BODY))

S.append(ejercicio(58, "La subida rodante (caja 5 → caja 3)", (
    "Arrancás en el sótano y subís hasta el traste 12 con <b>tres slides en la 1ª cuerda: del 5 al 8, del 8 al 10 "
    "y del 10 al 12</b>. Cuatro zonas del mástil recorridas y en ningún momento pensaste en un dibujo. "
    "Así se mueven los que parecen que van a cualquier lado y nunca se pierden."),
    "e58", W,
    "Escuchá: Page en los finales de solo de Zeppelin. "
    "60 BPM. Los slides tienen que sonar continuos: no vuelvas a puntear la nota de llegada."))

S.append(ejercicio(59, "La bajada diagonal", (
    "Casi todos saben subir; muy pocos saben volver. Esta es la bajada completa, desde el traste 17 hasta el "
    "traste 3, <b>casi toda ligada</b> — en dos compases puntéas cuatro veces. Un solo que sube y no baja se "
    "queda sin final: la caída es lo que hace que el clímax haya valido la pena."),
    "e59", W,
    "Escuchá: Slash en el final del solo de «Sweet Child O' Mine». "
    "55 BPM y subí de a poco. Que las notas ligadas suenen igual de fuerte que las punteadas."))

# ============================================================ CÓMO USARLOS
S.append(PageBreak())
S.append(Paragraph("CÓMO METER ESTOS LICKS EN UN SOLO", H1))
S.append(Paragraph(
    "Seis licks sueltos no son un solo: son seis licks sueltos. Lo que los convierte en música es "
    "<b>usar cada caja para lo que sirve</b>. Acá está la síntesis de todo el programa — la arquitectura de "
    "cuatro frases que ya conocés, cruzada con el mástil (se suman los ejercicios 47 y 48 del Hito 3, "
    "que viven en las cajas 3 y 5):", BODY))
S.append(Spacer(1, 2))
S.append(tabla([
    [Paragraph("<b>Frase</b>", CELLB), Paragraph("<b>Dónde tocarla</b>", CELLB),
     Paragraph("<b>Por qué</b>", CELLB), Paragraph("<b>Licks que te sirven</b>", CELLB)],
    [Paragraph("<b>1 · PRESENTA</b>", CELLB), Paragraph("Caja 5 o caja 1<br/>(grave)", CELL),
     Paragraph("Arrancar abajo te deja lugar para crecer. Si empezás arriba, no tenés a dónde ir.", CELL),
     Paragraph("57 · 48*", CELL)],
    [Paragraph("<b>2 · DESARROLLA</b>", CELLB), Paragraph("Caja 2 o caja 3<br/>(medio)", CELL),
     Paragraph("Subís un escalón: la misma idea, más arriba. El oyente reconoce y a la vez avanza.", CELL),
     Paragraph("54 · 47*", CELL)],
    [Paragraph("<b>3 · CLÍMAX</b>", CELLB), Paragraph("Caja 4<br/>(agudo)", CELL),
     Paragraph("Lo más alto y lo más fuerte. Se llega con un slide (lick 58) y se sostiene poco.", CELL),
     Paragraph("55, 56", CELL)],
    [Paragraph("<b>4 · CIERRA</b>", CELLB), Paragraph("Bajás a caja 1 o 5", CELL),
     Paragraph("La bajada es el desenlace. Cerrás en la tónica y el oído descansa.", CELL),
     Paragraph("59, 57", CELL)],
], [2.6 * cm, 3.0 * cm, W - 8.1 * cm, 2.5 * cm]))
S.append(Paragraph(
    "* Los ejercicios 47 y 48 no son de este cuadernillo: son del Hito 3, y ya los tenés.", SMALL))

S.append(Paragraph("LAS 3 REGLAS PARA QUE NO SUENE A COLLAGE", H2))
S.append(tabla([
    [Paragraph("<b>1</b>", CELLB), Paragraph("<b>Nunca dos licks pegados</b>", CELL),
     Paragraph("Entre lick y lick tiene que haber algo tuyo: una nota larga, un silencio, tres notas "
               "improvisadas. Si los encadenás, se escucha el pegote.", CELL)],
    [Paragraph("<b>2</b>", CELLB), Paragraph("<b>Variá al menos uno</b>", CELL),
     Paragraph("Cambiale el ritmo, el remate o la caja (ejercicios 44, 45 y 46 del Hito 3). Un lick "
               "calcado es de su dueño; uno variado ya es tuyo.", CELL)],
    [Paragraph("<b>3</b>", CELLB), Paragraph("<b>Máximo dos por solo</b>", CELL),
     Paragraph("Un solo de un minuto aguanta dos frases prestadas, no diez. El resto lo tenés que "
               "improvisar vos — para eso venís entrenando tres meses.", CELL)],
], [0.8 * cm, 4.2 * cm, W - 5.0 * cm]))

S.append(Paragraph("EL EJERCICIO QUE CIERRA TODO", H2))
S.append(Paragraph(
    "Poné el backing en La menor y tocá <b>un solo de un minuto que atraviese las cuatro zonas en orden</b>: "
    "arrancás en la caja 5, desarrollás en la 2 o la 3, subís a la 4 con un slide, y bajás en diagonal a "
    "cerrar. Podés usar dos de estos licks, no más. Grabalo.", BODY))
S.append(Paragraph(
    "Si podés hacer eso, ya no tocás la pentatónica: <b>la usás</b>. Que es de lo que se trataba desde el "
    "primer día.", BODY))

# ============================================================ BANCO
S.append(PageBreak())
S.append(Paragraph("SEGUÍ EL BANCO — licks fuera de la caja 1", H1))
S.append(Paragraph(
    "Misma consigna que en el Hito 3, con una columna más: <b>anotá en qué caja vive cada lick que sacás</b>. "
    "Si al final del mes tenés diez licks y ocho son de la caja 1, ya sabés qué te falta practicar.", BODY))
S.append(Spacer(1, 6))
S.append(TablaturaEnBlanco(W, sistemas=7, compases=2))

# ============================================================ CIERRE
S.append(PageBreak())
S.append(Paragraph("CHECKLIST", H1))
S.append(tabla([
    [Paragraph("", CELLB), Paragraph("<b>Lo puedo hacer</b>", CELLB), Paragraph("<b>Cómo lo compruebo</b>", CELLB)],
    [Paragraph(CAJ, CELL), Paragraph("Toco los 6 licks en su caja, sin mirar el papel", CELL),
     Paragraph("Me dicen un número del 54 al 59 y arranco en menos de 5 segundos.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Mi vibrato cambia según el registro (angosto abajo, ancho arriba)", CELL),
     Paragraph("Toco el lick 57 y el 56 seguidos: el vibrato no es el mismo.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Uso el blue note de paso, no de llegada", CELL),
     Paragraph("Improvisando lo cruzo sin frenar. Nunca termino una frase ahí.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Escucho la diferencia entre la 7ª menor y la 6ª mayor", CELL),
     Paragraph("Toco el lick 54 con FA" + SOS + " y después con SOL: sé cuál es cuál con los ojos cerrados.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Puedo solear en la caja 5 sin sentirme perdido", CELL),
     Paragraph("Improviso 1 minuto entero abajo del traste 5 y suena a música.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Subo y bajo el mástil con slides, sin frenar", CELL),
     Paragraph("Los licks 58 y 59 me salen a tempo y sin cortes.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Sé qué caja usar para cada parte del solo", CELL),
     Paragraph("Sin mirar la tabla, digo dónde va el clímax y dónde el cierre.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("<b>Grabé el solo que atraviesa las 4 zonas</b>", CELL),
     Paragraph("El video existe, dura un minuto y no vive en la caja 1.", CELL)],
], [0.9 * cm, 6.6 * cm, W - 7.5 * cm]))

S.append(Paragraph("EL TEST HONESTO", H2))
S.append(Paragraph(
    "Grabate improvisando un minuto <b>sin permitirte usar la caja 1</b>. Ni una nota entre los trastes 5 y 8. "
    "Va a ser incómodo los primeros treinta segundos y después se te va a abrir el mástil. "
    "Ese ejercicio, hecho una vez por semana, hace más por tu libertad que cualquier escala nueva.", BODY))

S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10.5"><b>¿Te trabaste con alguno?</b></font><br/>'
    '<font color="#f7d7d2" size="9">El 53 (la 6ª mayor) y el 57 (la caja 5 cantando) son los que más cuestan, '
    'y no por técnica: por oído. Mandame un video de 20 segundos por DM y te digo qué ajustar. · %s</font>' % IG, W))

doc.build(S)
print("OK Cuadernillo-BONUS-Licks-Fuera-de-la-Caja1.pdf")
