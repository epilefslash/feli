# -*- coding: utf-8 -*-
"""Arma el PDF del Cuadernillo HITO 2 — EL SABOR.

Requiere que antes se haya corrido `gen_scores_h2.py` (genera ./partituras/e17..e34).
"""
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import (H1, H2, BODY, SMALL, CELL, CELLB, CAJ, IG,
                               Diagrama, DiagramaFlechas, MapaCompleto, documento,
                               tabla, banner, par, caja_oscura, ejercicio, score)

doc = documento("Cuadernillo-Hito2-El-Sabor-EJERCICIOS.pdf",
                "HITO 2 — EL SABOR",
                "Ligados, slides, bending, vibrato, espacio y dinámica · ejercicios con TAB y partitura",
                "Solo con Sabor · Hito 2 — El Sabor",
                "Hito 2 - El Sabor (ejercicios)")
W = doc.width
S = []

# ============================================================ 1. INTRO
S.append(Paragraph("DE DÓNDE VENÍS Y A DÓNDE VAS", H2))
S.append(Paragraph(
    "En el Hito 1 conseguiste el <b>territorio</b>: sabés dónde están las notas y te movés por las 5 cajas "
    "sin perderte. Pero saber dónde están las notas no emociona a nadie. Un GPS conoce todas las calles "
    "de la ciudad y no sabe contar una historia.", BODY))
S.append(Paragraph(
    "Este mes no vas a aprender ni una nota nueva. Vas a trabajar el <b>CÓMO</b>: las mismas cinco notas de "
    "siempre, pero atacadas de forma que suenen a música. Esto es lo único que separa tu pentatónica de la de "
    "Gary Moore — no son notas distintas, es <b>tratamiento distinto</b>.", BODY))
S.append(Paragraph(
    "<b>Entregable del hito:</b> el solo del Ejercicio 34 grabado, y un antes/después: el mismo minuto de "
    "improvisación grabado el día 1 y el día 30.", BODY))

S.append(Paragraph("LOS 4 BLOQUES DEL MES, EN ESTE ORDEN Y POR ESTA RAZÓN", H2))
S.append(tabla([
    [Paragraph("<b>Sem.</b>", CELLB), Paragraph("<b>Recurso</b>", CELLB),
     Paragraph("<b>Qué resuelve</b>", CELLB), Paragraph("<b>Por qué va acá</b>", CELLB)],
    [Paragraph("5", CELLB), Paragraph("<b>Ligados y slides</b>", CELL),
     Paragraph("Que no puntees todas las notas. Las frases se pegan, dejan de sonar a ejercicio.", CELL),
     Paragraph("Es lo más mecánico y lo menos dependiente del oído: se aprende rápido y ya te cambia el sonido.", CELL)],
    [Paragraph("6", CELLB), Paragraph("<b>Bending</b>", CELL),
     Paragraph("Cantar con la cuerda. Es el recurso más expresivo de la guitarra.", CELL),
     Paragraph("Es el más difícil de afinar: necesita las 4 semanas. Y se practica en tres zonas del "
               "mástil, porque la fuerza que pide cambia según dónde estés.", CELL)],
    [Paragraph("7", CELLB), Paragraph("<b>Vibrato</b>", CELL),
     Paragraph("Que la nota larga no se muera. Es tu firma personal.", CELL),
     Paragraph("Va después del bending porque lo mejor de todo es bendear Y vibrar la misma nota.", CELL)],
    [Paragraph("8", CELLB), Paragraph("<b>Espacio y dinámica</b>", CELL),
     Paragraph("Que la frase respire y tenga volumen variable. Deja de ser una ametralladora.", CELL),
     Paragraph("Es lo más difícil de todo, porque no se hace con los dedos: se hace con la cabeza.", CELL)],
], [1.2 * cm, 3.0 * cm, 5.4 * cm, W - 9.6 * cm]))

S.append(Paragraph("LAS 4 REGLAS DEL MES", H2))
S.append(tabla([
    [Paragraph("<b>Regla</b>", CELLB), Paragraph("<b>Por qué</b>", CELLB)],
    [Paragraph("<b>Menos notas</b>", CELL),
     Paragraph("Los ejercicios de este mes tienen la mitad de notas que los del Hito 1. No es que falte material: "
               "es que si tocás muchas notas no podés cuidar ninguna. El sabor se trabaja nota por nota.", CELL)],
    [Paragraph("<b>Grabate</b>", CELL),
     Paragraph("Es el mes donde el oído miente más. Tu bending te parece afinado mientras tocás y no lo está. "
               "El celular no miente. Grabá una vez por semana, mínimo.", CELL)],
    [Paragraph("<b>Aprender quieto,<br/>aplicar moviéndose</b>", CELL),
     Paragraph("Cada semana arranca con el recurso solo, en un lugar fijo del mástil, aburrido y sin contexto. "
               "Y <b>termina lejos de ahí</b>: el último ejercicio de cada bloque se va a otra caja. La razón "
               "no es variedad — es que un bending en el traste 7 y uno en el 12 no son el mismo gesto, y si "
               "sólo practicás uno, el otro te sale desafinado.", CELL)],
    [Paragraph("<b>Todo con backing</b>", CELL),
     Paragraph("La expresividad es relativa a algo. Un bending afinado se escucha afinado CONTRA un acorde. "
               "Solo, no tenés referencia.", CELL)],
], [3.6 * cm, W - 3.6 * cm]))

S.append(Paragraph("LA RUTINA DIARIA (20 minutos)", H2))
S.append(tabla([
    [Paragraph("<b>Min</b>", CELLB), Paragraph("<b>Qué</b>", CELLB), Paragraph("<b>Foco</b>", CELLB)],
    [Paragraph("0–3", CELLB), Paragraph("Repaso del mapa: una caja del Hito 1, ida y vuelta", CELL),
     Paragraph("Calentar y no perder lo ganado. Rápido, sin drama.", CELL)],
    [Paragraph("3–10", CELLB), Paragraph("El recurso de la semana, AISLADO", CELL),
     Paragraph("Lento y feo. Acá se construye el control.", CELL)],
    [Paragraph("10–15", CELLB), Paragraph("El recurso dentro de una frase", CELL),
     Paragraph("Que empiece a sonar a música y no a ejercicio.", CELL)],
    [Paragraph("15–20", CELLB), Paragraph("<b>Improvisás</b> obligándote a usarlo", CELL),
     Paragraph("Regla: no puede pasar una frase sin el recurso de la semana.", CELL)],
], [1.5 * cm, 6.6 * cm, W - 8.1 * cm]))

# ============================================================ SEMANA 5
S.append(PageBreak())
S.append(banner(5, "LIGADOS Y SLIDES — que la púa deje de tocar todo",
                "Objetivo: que las notas se peguen entre sí. Es el cambio de sonido más rápido de todo el mes.", W))
S.append(Spacer(1, 8))
S.append(par([Diagrama(1, W * 0.5, titulo="DONDE SE APRENDE: CAJA 1 (trastes 5 a 8)"),
              Paragraph("<b>Hammer-on:</b> puntéas la nota baja y golpeás la alta con el dedo, sin puntear.<br/>"
                        "<b>Pull-off:</b> al revés — desde la nota alta, tirás el dedo hacia abajo y suena la baja."
                        "<br/><br/>"
                        "Los tres primeros ejercicios se hacen acá, en la caja 1, y es a propósito: mientras "
                        "aprendés un movimiento nuevo de la mano no conviene estar además buscando dónde "
                        "estás parado. <b>Pero el cuarto se va de la caja</b> — y bastante lejos. "
                        "Un recurso que sólo te sale en un lugar del mástil todavía no lo tenés.", BODY)],
             [W * 0.5, W * 0.5]))
S.append(Spacer(1, 4))

S.append(ejercicio(17, "Hammer-on aislado (subiendo)", (
    "Puntéas SOLO la primera nota de cada par; la segunda tiene que sonar por el golpe del dedo. "
    "Si la segunda suena más flojita, no estás golpeando: estás apoyando. El dedo cae desde arriba, "
    "con decisión, cerca del traste."),
    "e17", W, "60 BPM. Test: si tapás la púa con la otra mano y la nota igual suena, está bien hecho."))

S.append(ejercicio(18, "Pull-off aislado (bajando)", (
    "El más difícil de los dos, y el que casi todos hacen mal: <b>no se levanta el dedo, se tira</b>. "
    "El dedo de arriba engancha la cuerda hacia abajo, como si pellizcara. Si solo lo levantás, la nota "
    "de abajo suena muerta."),
    "e18", W, "60 BPM. Ojo: el dedo de la nota baja tiene que estar apoyado ANTES de tirar el de arriba."))

S.append(ejercicio(19, "El tresillo de rock (una púa cada 3 notas)", (
    "Púa, martillo, tirón: tres notas, un solo golpe de púa. Este patrón es la mitad del vocabulario del "
    "rock — Page, Angus y Slash lo usan hasta el cansancio. Cuando te sale fluido, tu velocidad aparente "
    "se duplica sin que hayas ganado nada de velocidad real."),
    "e19", W, "50 BPM en tresillos, y subís de a poco. Que las 3 notas suenen con el mismo volumen."))

S.append(ejercicio(20, "Toda la pentatónica en UNA sola cuerda", (
    "<b>Mirá la tablatura antes de tocar nada.</b> Todo el primer compás está en una sola línea: 3ª cuerda, "
    "trastes 2 · 5 · 7 · 9 · 12 · 14. Eso es la pentatónica de La menor entera, una octava completa, sin "
    "mover el dedo de una cuerda. <b>Ninguna caja tiene esta forma, porque esto no es una caja</b> — es el "
    "mástil mirado de costado.<br/><br/>"
    "Cómo se sube: los saltos de <b>dos trastes</b> se hacen con <i>hammer-on</i> (5→7, 7→9, 12→14) y los de "
    "<b>tres</b> con <i>slide</i> (2→5, 9→12), porque a tres trastes el hammer ya no suena parejo. Bajando es "
    "lo mismo al revés: <i>pull-off</i> de a dos, <i>slide</i> de a tres.<br/><br/>"
    "<b>El compás 2 es el premio.</b> Llegaste al traste 14 (la tónica aguda). Ahí saltás a la 2ª cuerda, "
    "traste 13, y lo estirás <b>medio tono</b>: esa es una nota que no está en la pentatónica, y es la que "
    "hace que el blues suene a blues. Después volvés a caer en el 14 con vibrato.<br/><br/>"
    "<b>Fijate en las figuras, porque ahí está el efecto:</b> el 13 y el 14 son dos <b>semicorcheas "
    "pegadas</b> — un gesto rápido, casi un latigazo — y recién después viene la nota larga con vibrato. "
    "Si tocás el bending lento y la resolución lenta se te va el chiste: no son dos notas, es <b>un solo "
    "movimiento</b> que termina en una nota sostenida.<br/><br/>"
    "Y mirá cómo empieza y cómo termina: arranca en el <b>tiempo 2</b>, y la bajada cierra dejando un "
    "silencio de un tiempo. Es un <b>espejo</b> — el aire que había al principio queda al final. No es "
    "decorado: es lo que hace que suene a frase cerrada y no a escala que se cortó.<br/><br/>"
    "<b>Para qué sirve de verdad:</b> cuando sepas hacer esto, dejás de estar atado a las posiciones. Todas "
    "las cuerdas tienen su recorrido horizontal — probalo en la 2ª y en la 6ª cuando esto te salga."),
    "e20", W,
    "Con backing, 70 BPM. Primero sin ligados, cada nota picada, para ubicar los trastes. Recién cuando los "
    "tengas de memoria metés los hammer y los slides. <b>Ojo con el ½ del compás 2:</b> es medio tono, no un "
    "tono — chequealo contra el traste 14 de la 3ª cuerda, tiene que quedar apenas abajo."))

# ============================================================ SEMANA 6
S.append(PageBreak())
S.append(banner(6, "BENDING — cantar con la cuerda",
                "Objetivo: que llegue AFINADO y a una nota que exista. Un bending que no llega, no cuenta.", W))
S.append(Spacer(1, 8))
S.append(DiagramaFlechas(1, [(3, 7, 9, "1 tono  ·  EL MÁS USADO DEL ROCK"),
                             (2, 8, 10, "1 tono"),
                             (1, 8, 10, "1 tono")], W, rango=(4, 12),
                         titulo="LOS BENDINGS DE LA CAJA 1 — de dónde salís (rojo) y a dónde tenés que llegar (negro)"))
S.append(Spacer(1, 6))
S.append(Paragraph(
    "Un bending no es \"estirar la cuerda\": es <b>ir a una nota concreta</b>. Cada flecha de arriba tiene un "
    "destino que existe en la escala. Si te quedás corto suena desafinado y triste; si te pasás, suena a gato. "
    "El de la <b>3ª cuerda traste 7</b> es el más usado del rock: aprendé ese antes que ninguno.", BODY))
S.append(Paragraph(
    "Técnica: bendeás con <b>tres dedos</b> apoyados (anular al frente, medio e índice atrás ayudando), girando "
    "la muñeca — no con la fuerza del dedo solo. Y el pulgar por encima del mástil, agarrando: es lo que te da "
    "la palanca. Si te duele, estás empujando con el dedo en vez de girar la muñeca.", BODY))

S.append(ejercicio(21, "Escuchá el destino, después bendeá", (
    "El ejercicio que arregla los bendings desafinados. Primero tocás la nota de destino y la escuchás bien "
    "(traste 9). Después bendeás desde el 7 hasta que suene <b>exactamente igual</b>. No parecido: igual. "
    "Tu oído es el que corrige la mano, no al revés."),
    "e21", W, "Sin metrónomo, con backing. Hacelo 5 minutos por día toda la semana: es el que más rinde."))

S.append(ejercicio(22, "El mismo bending en tres zonas del mástil", (
    "El mismo bending de 1 tono, tres veces — pero en el traste <b>7</b>, en el <b>12</b> y en el <b>15</b>. "
    "Tocá los tres seguidos y prestá atención a una sola cosa: <b>cuánta fuerza tenés que hacer en cada uno</b>."
    "<br/><br/>"
    "No es el mismo gesto y no es tu imaginación. Cuanto más arriba del mástil, <b>más corta es la parte de "
    "la cuerda que vibra</b>, así que el mismo empujón produce más cambio de altura — y además la cuerda se "
    "siente más blanda. Abajo pasa al revés: en el traste 7 hay que empujar bastante más para llegar al mismo "
    "tono.<br/><br/>"
    "<b>Por qué esto importa más de lo que parece.</b> Si practicás el bending siempre en la misma zona, no "
    "aprendés a bendear: aprendés a bendear <i>ahí</i>. El día que tu solo llegue al clímax arriba del mástil "
    "—cosa que va a pasar, es el ej. 53— vas a estirar con la fuerza de abajo y te vas a pasar de largo. "
    "Suena desafinado y no vas a saber por qué.<br/><br/>"
    "La 3ª cuerda es gruesa y cuesta, la 1ª es finita y se pasa sola: <b>la cuerda y la posición son dos "
    "variables distintas</b>, y las dos te cambian la fuerza. Este ejercicio mueve las dos a propósito."),
    "e22", W,
    "70 BPM con backing. Chequeá cada bending contra la nota de destino pisada, como en el ej. 21 — pero "
    "hacelo en las tres zonas. Arriba vas a frenar antes de lo que creías; abajo vas a tener que empujar más."))

S.append(ejercicio(23, "Bending y vuelta (el release)", (
    "La mitad del bending que nadie practica: <b>la bajada</b>. Subís, sostenés, y volvés despacio y controlado — "
    "no soltando de golpe. Si soltás de golpe, todas las notas intermedias suenan como un resbalón.<br/><br/>"
    "Es a propósito el <b>mismo traste del ejercicio 21</b> — no es que te quedaste sin ideas de dónde ponerlo. "
    "Cuando compares los dos vas a escuchar solamente lo nuevo (la vuelta controlada), sin el ruido de una "
    "posición distinta metiéndose en el medio. El ejercicio 29 sigue esta misma cadena un escalón más."),
    "e23", W, "Lento, 60 BPM. La bajada tiene que durar lo mismo que la subida."))

S.append(ejercicio(24, "Lick de bending (escuela Gary Moore)", (
    "Cómo se usa de verdad: primero una frase que <b>hace esperar</b>, después el bending como el momento "
    "importante, y recién ahí la resolución. El bending pega porque llega tarde. Si bendeás todo el tiempo, "
    "no bendeás nada."),
    "e24", W, "Con backing lento. Grabate y escuchá si el bending llega a la nota o se queda a mitad de camino."))

S.append(Paragraph("Y AHORA SÍ: SALÍS DE LA CAJA 1", H2))
S.append(Paragraph(
    "Hasta acá te moviste por el mástil cuando el ejercicio lo pedía (el 20 recorre una cuerda entera, el 22 "
    "bendea en tres zonas), pero siempre <b>de paso</b>: la casa seguía siendo la caja 1. Ahora te mudás de "
    "verdad — y no es casualidad que sea a la caja 2: es <b>la caja del bending</b>. Ahí la tónica de la 2ª "
    "cuerda (traste 10) tiene la 7ª menor justo un tono abajo, o sea exactamente a distancia de estirón.", BODY))
S.append(Spacer(1, 2))
S.append(par([Diagrama(2, W * 0.5),
              Paragraph("Ya la conocés del Hito 1 y comparte los trastes 7 y 8 con la caja 1, así que no estás "
                        "aprendiendo un dibujo nuevo: estás corriendo la mano tres trastes.<br/><br/>"
                        "Los dos ejercicios que siguen son los primeros <b>licks</b> del programa — frases "
                        "de verdad, con el mecanismo de un guitarrista concreto detrás.", BODY)],
             [W * 0.5, W * 0.5]))
S.append(Spacer(1, 4))

S.append(ejercicio(25, "El bend que aterriza en la tónica (Albert King / SRV)", (
    "Un bending no es un adorno: es una <b>llegada</b>. Estirás la 2ª cuerda traste 8 un tono entero y caés "
    "justo en el LA — la tónica de la caja 2. Por eso suena a que llegaste a algún lado, y no a que estiraste "
    "una cuerda porque quedaba bien. Albert King hizo una carrera con este movimiento y SRV lo heredó completo."),
    "e25", W,
    "Escuchá: Albert King, «Born Under a Bad Sign» · Stevie Ray Vaughan, «Texas Flood». "
    "70 BPM con backing. Comprobá el bending contra el traste 10 antes de tocarlo."))

S.append(ejercicio(26, "El blue note, de paso — y las dos formas de llegar", (
    "La primera nota del programa que <b>no pertenece a la pentatónica</b>: el MI bemol (3ª cuerda traste 8), "
    "el famoso <i>blue note</i>. Le pone la mugre al blues, pero con una regla estricta — "
    "<b>es una nota de paso, nunca de llegada</b>. Va metida entre el RE (traste 7) y el MI (traste 9), "
    "cruzándola sin frenar. Si te quedás parado en ella suena desafinado, porque lo está.<br/><br/>"
    "<b>Los compases 3 y 4 son la misma frase, y ahí está lo importante de este ejercicio.</b> En vez de "
    "pisar el traste 8, pisás el <b>7</b> y lo estirás <b>medio tono</b> — mirá la flecha, dice <b>½</b> y no "
    "<i>full</i>. Llegás a la misma altura por otro camino. Es el <b>único bending de medio tono de todo el "
    "programa</b>, y no es un capricho que sea justo éste: en el blues, al blue note casi nunca se llega "
    "pisándolo. Se llega estirando.<br/><br/>"
    "¿Por qué suena distinto si la nota es la misma? Porque el dedo <b>pasa por el medio</b>. Pisado, el MI "
    "bemol aparece de golpe, afinado y limpio. Estirado, la cuerda recorre todo lo que hay entre el RE y el "
    "MI bemol, y ese recorrido — que dura una fracción de segundo — es literalmente el quejido del blues. "
    "Eso es lo que hace B.B. King en <i>The Thrill Is Gone</i>, que es el solo de referencia de este mes."),
    "e26", W,
    "Escuchá: cualquier shuffle de Clapton o de Page — está en todos. "
    "70 BPM. Tocá el compás 1 sin el MI bemol y después con él: esa diferencia es el sabor. "
    "Después tocá el 1 y el 3 seguidos: misma nota, distinta emoción. "
    "<b>Ojo con el medio tono:</b> tu mano viene entrenada del ej. 21 para estirar un tono entero, así que "
    "lo más probable es que te pases. Chequealo contra el traste 8 pisado hasta que coincidan."))

# ============================================================ SEMANA 7
S.append(PageBreak())
S.append(banner(7, "VIBRATO — tu firma",
                "Objetivo: un vibrato parejo y elegido, no un tembleque nervioso. Es lo primero que te delata.", W))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "El vibrato es lo único de la guitarra que es <b>tuyo</b>: el de B.B. King, el de Clapton y el de Gary Moore "
    "se reconocen en una nota. Y también es lo que delata al amateur en una nota — porque el vibrato del amateur "
    "es involuntario: aparece del nervio, no de una decisión.", BODY))
S.append(Spacer(1, 2))
S.append(par([Diagrama(2, W * 0.5, titulo="TERRITORIO DE ESTA SEMANA: CAJA 2"),
              Paragraph("Esta semana te quedás en la caja 2 — la misma zona donde ya bendeaste en la semana "
                        "pasada. No sumás posición nueva justo cuando estás por sumar una técnica nueva.<br/><br/>"
                        "Tónica: 2ª cuerda, traste 10.", BODY)],
             [W * 0.5, W * 0.5]))
S.append(Spacer(1, 4))

S.append(Paragraph("EL AGARRE (esto es lo que nadie te corrige)", H2))
S.append(tabla([
    [Paragraph("<b>Punto</b>", CELLB), Paragraph("<b>Cómo va</b>", CELLB)],
    [Paragraph("Pulgar", CELL),
     Paragraph("<b>Por encima del diapasón</b>, apoyado suave — no escondido atrás del mástil. Para este "
               "vibrato en particular, necesitás ese apoyo.", CELL)],
    [Paragraph("Base del índice", CELL),
     Paragraph("Hace contacto por abajo con la base de la mano. Es el segundo punto de apoyo, junto con "
               "el pulgar — entre los dos sostienen el movimiento.", CELL)],
    [Paragraph("Dedos de apoyo", CELL),
     Paragraph("Apoyá los dedos <b>anteriores</b> al que estás usando (si vibrás con el anular, apoyá "
               "índice y medio también). Te da fuerza y estabilidad — si el esfuerzo cae solo en la "
               "falange del dedo que vibra, se cansa y pierde control.", CELL)],
], [3.2 * cm, W - 3.2 * cm]))

S.append(tabla([
    [Paragraph("<b>Los errores más comunes</b>", CELLB), Paragraph("<b>Cómo se arregla</b>", CELLB)],
    [Paragraph("Tembleque descontrolado", CELL),
     Paragraph("Medilo con metrónomo (ejercicio 27). Si no podés contar las ondas, no lo estás controlando: "
               "te está saliendo solo.", CELL)],
    [Paragraph("Vibrato con el dedo (\"vibrato de falange\")", CELL),
     Paragraph("Se hace con la <b>muñeca</b>, girándola como si abrieras el pomo de una puerta — no doblando "
               "la última falange. El dedo solo no tiene fuerza ni regularidad.", CELL)],
    [Paragraph("Alternar la dirección", CELL),
     Paragraph("Vibrar <b>siempre para el mismo lado</b> (siempre para arriba, o siempre para abajo) es mucho "
               "más fácil que alternar. Elegí un sentido y quedate ahí — alternar es un truco avanzado, "
               "no el punto de partida.", CELL)],
    [Paragraph("Mover el mástil de la guitarra", CELL),
     Paragraph("Si además de la cuerda se mueve el mástil, estás regalando energía al instrumento en vez de "
               "ponerla toda en la cuerda. El resultado es un vibrato menos preciso y más cansador.", CELL)],
    [Paragraph("Empezar a vibrar de inmediato", CELL),
     Paragraph("Dejá sonar la nota derecha medio segundo y <b>después</b> entrás con el vibrato. Ese retardo "
               "es lo que suena caro.", CELL)],
], [4.4 * cm, W - 4.4 * cm]))
S.append(Paragraph(
    "<b>Tensión y relajación:</b> un vibrato tiene dos momentos, no uno. Tensás (estirás la cuerda) y "
    "<b>relajás</b> (soltás para que vuelva sola a su lugar). El error más común es no volver del todo — "
    "la cuerda se queda un poquito estirada y la nota queda permanentemente desafinada, aunque sea poco.", SMALL))

S.append(ejercicio(27, "Vibrato medido (con metrónomo) — caja 2", (
    "La misma nota tres veces, con el vibrato contado: 2, 3 y 4 ondas por tiempo (en términos de subdivisión: "
    "corcheas, tresillos y semicorcheas). Suena a ejercicio militar y esa es la idea — <b>vibrato que podés "
    "contar es vibrato que controlás</b>. Después vas a elegir la velocidad según la frase, pero primero "
    "tenés que poder elegirla. Si no podés hacer esto medido, es muy probable que todavía no puedas hacerlo "
    "libre — el ejercicio libre solo se nota bien cuando el medido ya está.<br/><br/>"
    "Va en la <b>caja 2</b> (tónica: 2ª cuerda, traste 10), no en la 1. Ya bendeaste ahí en la semana pasada — "
    "esto sigue en el mismo territorio en vez de volver para atrás."),
    "e27", W,
    "60 BPM. Empezá por el lento: es el más difícil, porque el nervio te empuja a acelerar. Repetilo variando "
    "la <b>amplitud</b> (cuánto estirás) sin cambiar la velocidad — son dos controles distintos, no uno. Y "
    "hacelo con cada dedo, no solo el índice: el meñique en particular te va a costar el doble."))

S.append(ejercicio(28, "El mismo vibrato en tres registros (y un cuarto, en caja 4)", (
    "Una frase corta que termina en una nota larga, resuelta en grave, medio y agudo. Vas a descubrir que "
    "<b>en los graves el vibrato tiene que ser angosto</b> (si no, suena desafinado) y <b>en los agudos ancho</b> "
    "(si no, ni se escucha). No es un solo vibrato: son tres — y agregamos un cuarto compás que te muda a la "
    "<b>caja 4</b>, para que el vibrato no quede asociado solo a la caja 1."),
    "e28", W, "Con backing. Escuchá la diferencia, no la mires. El último compás usa la tónica de la caja 4 (3ª cuerda, traste 14)."))

S.append(ejercicio(29, "Bending + vibrato (la combinación pro)", (
    "Acá está el sonido que buscabas desde que empezaste a tocar. Bendeás, <b>sostenés arriba</b>, y ahí le metés "
    "vibrato sin soltar el bending. Es difícil porque la mano ya está haciendo fuerza — el vibrato se hace "
    "<b>desde arriba</b>, con la muñeca, sin dejar caer la nota."),
    "e29", W, "Lento. Si el bending se cae mientras vibrás, es que no tenías el bending firme. Volvé al ejercicio 21."))

S.append(ejercicio(30, "El vibrato como remate — caja 2", (
    "Una frase entera donde la última nota se sostiene con vibrato. Regla de oro: <b>la nota final de una frase "
    "nunca se deja sola</b>. Si termina seca, la frase suena a que te olvidaste de algo.<br/><br/>"
    "También en <b>caja 2</b>, resolviendo en su propia tónica (2ª cuerda, traste 10) — misma idea que en la "
    "caja 1, otro lugar del mástil."),
    "e30", W, "Con backing. Grabate: si el vibrato de la última nota no se escucha, no existió."))

# ============================================================ SEMANA 8
S.append(PageBreak())
S.append(banner(8, "ESPACIO Y DINÁMICA — la parte que no se toca con los dedos",
                "Objetivo: que tu solo respire y tenga volumen variable. Es la semana más difícil del hito.", W))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "Todo lo anterior se practica con las manos. Esto no. El espacio y la dinámica se practican con la "
    "<b>cabeza</b>, y por eso casi nadie los trabaja: no se sienten como \"estudiar guitarra\". "
    "Pero son la diferencia entre un solo que emociona y uno que impresiona un rato y cansa.", BODY))
S.append(Paragraph(
    "B.B. King construyó una carrera entera con esto: tocaba menos notas que cualquiera de su generación y "
    "no hay una sola que sobre. El silencio no es la ausencia de música — es lo que hace que la nota "
    "siguiente signifique algo.", BODY))

S.append(ejercicio(31, "La regla de las 3 notas (y de nuevo, en caja 5)", (
    "Tocás tres notas y <b>te callás un compás entero</b>. Vas a sentir una incomodidad física, unas ganas "
    "enormes de llenar el silencio: esa incomodidad es exactamente lo que estás entrenando a tolerar. "
    "El silencio escrito acá no es una pausa entre ejercicios — es parte de la música. El último par repite "
    "la misma idea en la <b>caja 5</b>: abajo el silencio pesa distinto, y también hay que aprender a tolerarlo ahí."
    "<br/><br/>"
    "<b>Si contar no te alcanza, hacelo con el cuerpo.</b> Ponete una taza de café al lado. Tocás tus tres "
    "notas, <b>soltás la mano derecha y agarrás la taza</b>, tomás un sorbo, la apoyás, y recién ahí volvés a "
    "tocar. Suena a chiste y no lo es: contar es una operación mental que podés hacer <i>mientras</i> seguís "
    "tocando — o sea que podés hacer trampa sin darte cuenta. Con la taza en la mano no podés. El silencio "
    "deja de ser una decisión y pasa a ser un hecho físico, y de paso descubrís que dura mucho menos de lo "
    "que te parecía desde adentro."),
    "e31", W, "Con backing, obligatorio. Contá los tiempos del silencio en voz alta si hace falta."))

S.append(ejercicio(32, "Pregunta abajo, respuesta arriba", (
    "Dos frases con el <b>mismo ritmo</b> y distinto final: la primera termina en una nota que queda colgada "
    "(pregunta), la segunda en la tónica (respuesta). Así habla la gente, y así hablan los buenos solos. "
    "Es la estructura más vieja y más efectiva que existe.<br/><br/>"
    "<b>Y acá le sumamos la otra mitad:</b> la pregunta vive en la <b>caja 5</b>, abajo de todo (trastes 2 a "
    "5), y la respuesta en la <b>caja 4</b>, arriba de todo (trastes 12 a 15). No es capricho — cambia el "
    "<i>humor</i> de cada frase. Abajo la guitarra suena gorda, oscura, casi como un bajo: la pregunta pesa. "
    "Arriba suena finita y brillante, y ahí la respuesta se escucha como que <b>llegó</b>.<br/><br/>"
    "La misma pregunta hecha arriba y la misma respuesta hecha abajo funcionarían igual de bien "
    "gramaticalmente — y sonarían a otra cosa. <b>Dónde tocás una frase es parte de lo que la frase dice.</b> "
    "Eso no se puede escribir en el papel: hay que escucharlo."),
    "e32", W,
    "Con backing. Después hacelo al revés — pregunta arriba, respuesta abajo — y decidí cuál te gusta más. "
    "No hay una correcta: hay una que te suena a vos."))

S.append(ejercicio(33, "La misma frase en tres volúmenes — caja 2", (
    "Idéntica frase, tocada suave, normal y fuerte. La dinámica no se hace con la perilla: se hace con "
    "<b>cuánta púa le das a la cuerda</b>. Susurrar, hablar, gritar. Si tocás todo al mismo volumen, tu solo "
    "es un tipo que habla monótono durante un minuto.<br/><br/>"
    "La misma frase de los ejercicios 27 y 30 (caja 2), para no sumar una posición nueva justo cuando la "
    "cabeza está ocupada con la dinámica."),
    "e33", W, "Sin tocar el ampli ni el pedal. Todo con la mano derecha."))

S.append(PageBreak())
S.append(Paragraph("ANTES DEL SOLO: ESTO YA TE SIRVE EN LAS 5 CAJAS", H2))
S.append(Paragraph(
    "Este mes <b>aprendiste</b> cada recurso en un lugar fijo y lo <b>aplicaste</b> moviéndote: el bending "
    "salió a los trastes 12 y 15, el vibrato a la caja 4, la pregunta y la respuesta del ejercicio 32 a las "
    "cajas 5 y 4. Pero eso pasó cuando el ejercicio te lo pedía. Lo que falta es que lo hagas <b>vos</b>, sin "
    "que esté escrito — porque la <b>técnica</b> no vive en una caja: bendear un tono es el mismo movimiento "
    "en la caja 3 que en la caja 1, y un vibrato de muñeca es el mismo gesto arriba que abajo. Lo que cambia "
    "es la digitación, no el mecanismo — y esa digitación ya la tenés, viene del Hito 1.", BODY))
S.append(Spacer(1, 4))
S.append(MapaCompleto(W))
S.append(Spacer(1, 4))
S.append(Paragraph(
    "<b>Antes de pasar al solo de evaluación, agarrá 10 minutos y probá esto:</b> elegí un bending de la "
    "semana 6 y hacelo en las cajas 3, 4 y 5 sin que esté escrito — buscá la nota destino de oído, como en el "
    "ejercicio 21, y practicá también la bajada controlada del 23 ahí arriba. Después agarrá el vibrato medido "
    "del ejercicio 27 y repetilo parado en cada una de las cinco. No hace falta que te salga prolijo la "
    "primera vez: lo que estás comprobando es que <b>no hay una caja \"para el sabor\" y otras \"para el "
    "mapa\"</b> — hay un mástil, y el sabor va donde vayas vos. "
    "El solo que sigue ya te va a pedir esto mismo, sin avisar.", SMALL))
S.append(Spacer(1, 8))

S.append(Paragraph("EJERCICIO 34 — EL SOLO DE EVALUACIÓN (tu entregable)", H2))
S.append(Paragraph(
    "Diez compases que usan <b>todo el mes</b>: entra suave y con espacio, vibra una nota larga, mete ligados, "
    "bendea y vibra arriba del bending, se calla un compás entero, sube con un slide, llega al clímax en forte, "
    "baja con ligados y cierra en la tónica, suave, con vibrato.", BODY))
S.append(Paragraph(
    "Fijate el compás 6: el slide te lleva de caja 1 a caja 2, y las notas repetidas que siguen ya caen en "
    "<b>caja 3</b>. El compás 7 arranca directo en <b>caja 4</b> y baja. Es la misma lógica del Hito 1 — "
    "el clímax de un solo casi nunca se queda en un solo lugar del mástil.", BODY))
S.append(Paragraph(
    "Fijate que <b>casi no hay notas rápidas</b>. Ese es el punto del hito: lo que emociona no es la cantidad "
    "de notas, es lo que le hacés a cada una.", BODY))
S.append(Spacer(1, 2))
S.append(score("e34", W))
S.append(Spacer(1, 4))
S.append(Paragraph(
    "El compás 5 es un silencio completo, en el medio del solo. Es la nota más valiente de la partitura.", SMALL))

S.append(PageBreak())
S.append(Paragraph("LA APOYATURA — la nota que prepara a la otra", H2))
S.append(Paragraph(
    "Ya la usaste sin nombrarla: es esa nota corta que entra <b>justo antes</b> de la nota importante, "
    "y que hace que la llegada suene menos \"pisada\" y más \"cantada\". No es un ligado — se puntea con "
    "la púa, igual que la nota a la que apunta — y no es un bending: son dos notas distintas, una de paso "
    "y otra de destino.<br/><br/>"
    "Compará el primer compás con el segundo: misma nota de llegada, pero el segundo la anuncia. Ese "
    "medio segundo de aviso es lo que separa una frase mecánica de una que respira.", BODY))
S.append(Spacer(1, 2))
S.append(score("e34bis", W))
S.append(Spacer(1, 4))
S.append(Paragraph(
    "70 BPM. La apoyatura entra corta y sin acento — el peso va en la nota de llegada, no en la de paso. "
    "Si las dos suenan igual de fuerte, todavía no es apoyatura: es dos notas sueltas.", SMALL))

# ============================================================ CIERRE
S.append(PageBreak())
S.append(Paragraph("¿CERRASTE EL HITO 2? (checklist honesto)", H1))
S.append(Paragraph(
    "Este hito no se comprueba mirando el papel: se comprueba <b>escuchando la grabación</b>. "
    "Marcá solo lo que se escuche, no lo que te parezca que hacés.", BODY))
S.append(tabla([
    [Paragraph("", CELLB), Paragraph("<b>Lo puedo hacer</b>", CELLB), Paragraph("<b>Cómo lo compruebo</b>", CELLB)],
    [Paragraph(CAJ, CELL), Paragraph("Mis ligados suenan tan fuerte como las notas punteadas", CELL),
     Paragraph("En la grabación no se distingue cuál punteé y cuál ligué.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("El tresillo de rock me sale fluido", CELL),
     Paragraph("Toco el ejercicio 19 a tempo, con las 3 notas parejas.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Puedo recorrer la pentatónica entera en una sola cuerda", CELL),
     Paragraph("Toco el ejercicio 20 en la 3ª cuerda de memoria, sin mirar el dibujo de ninguna caja.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Mis bendings llegan afinados", CELL),
     Paragraph("Grabo el ejercicio 21 y el bending suena idéntico a la nota de destino.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("<b>…y también llegan afinados arriba del mástil</b>", CELL),
     Paragraph("Grabo el ejercicio 22: los bendings de los trastes 7, 12 y 15 llegan los tres. "
               "Si arriba me paso de largo, todavía estoy empujando con la fuerza de abajo.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Controlo la vuelta del bending", CELL),
     Paragraph("En el ejercicio 23 la bajada es gradual, no un resbalón.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Puedo elegir la velocidad de mi vibrato", CELL),
     Paragraph("Hago el ejercicio 27 y las tres velocidades son distintas y parejas.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Puedo bendear y vibrar la misma nota", CELL),
     Paragraph("El ejercicio 29 sale sin que se caiga la afinación del bending.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Tolero el silencio cuando improviso", CELL),
     Paragraph("En un minuto de improvisación hay al menos 4 silencios de más de 2 tiempos.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Mi solo tiene volumen variable", CELL),
     Paragraph("En la grabación se escucha claramente una parte suave y una fuerte.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Mi apoyatura suena a apoyatura, no a dos notas sueltas", CELL),
     Paragraph("En el ejercicio 34-bis la nota de paso se escucha más floja que la de llegada.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("<b>Grabé el ejercicio 34 y el antes/después</b>", CELL),
     Paragraph("Los dos videos existen. Son el entregable del hito.", CELL)],
], [0.9 * cm, 6.3 * cm, W - 7.2 * cm]))

S.append(Paragraph("EL ANTES/DESPUÉS (no te lo saltees)", H2))
S.append(Paragraph(
    "El día 1 de este mes grabate <b>un minuto improvisando</b> sobre el backing, sin preparar nada. Guardalo y "
    "no lo escuches. El día 30, grabá otro minuto sobre el mismo backing. Recién ahí escuchá los dos seguidos.", BODY))
S.append(Paragraph(
    "Durante el mes vas a sentir que no avanzás: el progreso en expresividad es invisible desde adentro, porque "
    "tu oído mejora al mismo tiempo que tus manos. Los dos audios seguidos son la única prueba objetiva.", BODY))

S.append(Paragraph("PLANILLA DE PRÁCTICA", H2))
dias = ["L", "M", "X", "J", "V", "S", "D"]
rows = [[Paragraph("<b>Semana</b>", CELLB)] + [Paragraph("<b>%s</b>" % d, CELLB) for d in dias] +
        [Paragraph("<b>¿Me grabé esta semana?</b>", CELLB)]]
for nombre in ["5 · Ligados y slides", "6 · Bending", "7 · Vibrato", "8 · Espacio y dinámica"]:
    rows.append([Paragraph(nombre, CELL)] + [Paragraph(CAJ, CELL) for _ in dias] + [Paragraph(CAJ, CELL)])
from reportlab.platypus import TableStyle
t = tabla(rows, [3.6 * cm] + [0.85 * cm] * 7 + [W - 3.6 * cm - 0.85 * cm * 7])
t.setStyle(TableStyle([('ALIGN', (1, 0), (7, -1), 'CENTER'), ('ALIGN', (8, 1), (8, -1), 'CENTER')]))
S.append(t)

S.append(Paragraph("Y DESPUÉS DE ESTO, ¿QUÉ?", H2))
S.append(Paragraph(
    "Con el Hito 1 conseguiste el territorio y con el Hito 2 la voz. Lo que te falta es <b>qué decir</b>: "
    "el Hito 3 es <b>EL VOCABULARIO</b> — robarles licks a los grandes de forma honesta (escuchar, sacar, copiar, "
    "variar, apropiar), entender cómo se arma un solo con principio y final, y grabar tu solo de un minuto.", BODY))
S.append(Paragraph(
    "Pero eso es después. Este mes tenés un solo trabajo: <b>que cada nota que toques tenga algo que la haga tuya</b>.", BODY))

S.append(Spacer(1, 4))
S.append(caja_oscura(
    '<font color="white" size="10.5"><b>¿Tu bending no llega o tu vibrato sale nervioso?</b></font><br/>'
    '<font color="#f7d7d2" size="9">Mandame un video de 20 segundos por DM y te lo corrijo. La expresividad '
    'es lo más difícil de autoevaluar: desde adentro siempre suena mejor de lo que es. · %s</font>' % IG, W))

doc.build(S)
print("OK Cuadernillo-Hito2-El-Sabor-EJERCICIOS.pdf")
