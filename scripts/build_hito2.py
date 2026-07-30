# -*- coding: utf-8 -*-
"""Arma el PDF del Cuadernillo HITO 2 — EL SABOR.

Requiere que antes se haya corrido `gen_scores_h2.py` (genera ./partituras/e17..e34).
"""
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import (H1, H2, BODY, SMALL, CELL, CELLB, CAJ, IG,
                               Diagrama, DiagramaFlechas, documento,
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

S.append(Paragraph("LOS 5 RECURSOS, EN ESTE ORDEN Y POR ESTA RAZÓN", H2))
S.append(tabla([
    [Paragraph("<b>Sem.</b>", CELLB), Paragraph("<b>Recurso</b>", CELLB),
     Paragraph("<b>Qué resuelve</b>", CELLB), Paragraph("<b>Por qué va acá</b>", CELLB)],
    [Paragraph("5", CELLB), Paragraph("<b>Ligados y slides</b>", CELL),
     Paragraph("Que no puntees todas las notas. Las frases se pegan, dejan de sonar a ejercicio.", CELL),
     Paragraph("Es lo más mecánico y lo menos dependiente del oído: se aprende rápido y ya te cambia el sonido.", CELL)],
    [Paragraph("6", CELLB), Paragraph("<b>Bending</b>", CELL),
     Paragraph("Cantar con la cuerda. Es el recurso más expresivo de la guitarra.", CELL),
     Paragraph("Es el más difícil de afinar: necesita las 4 semanas. Cierra mudándose a la caja 2.", CELL)],
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
    [Paragraph("<b>Aislar, después integrar</b>", CELL),
     Paragraph("Cada semana arranca con el recurso solo, aburrido, sin contexto — y termina metiéndolo en una "
               "frase. Si te salteás la parte aburrida, el recurso no te sale cuando improvisás.", CELL)],
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
S.append(par([Diagrama(1, W * 0.5, titulo="TERRITORIO: CAJA 1 (trastes 5 a 8)"),
              Paragraph("Todo el mes se toca en la <b>caja 1</b> y algo de la <b>caja 2</b>. Ya las conocés: "
                        "es a propósito. Si tenés que pensar dónde estás parado, no te queda cabeza para "
                        "pensar cómo suena.<br/><br/>"
                        "<b>Hammer-on:</b> puntéas la nota baja y golpeás la alta con el dedo, sin puntear.<br/>"
                        "<b>Pull-off:</b> al revés — desde la nota alta, tirás el dedo hacia abajo y suena la baja.", BODY)],
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

S.append(ejercicio(20, "Ligados y slide dentro de una frase", (
    "Acá se junta: hammer, pull, un slide para cambiar de zona y un vibrato de cierre. Fijate en lo que pasó — "
    "es la misma pentatónica del Hito 1, pero ya no suena a escala. Y todavía no tocaste ni un bending."),
    "e20", W, "Con backing, 70 BPM. Repetilo hasta que salga sin pensar en la técnica."))

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

S.append(ejercicio(22, "Bending con destino, en tres cuerdas", (
    "El mismo bending de 1 tono en la 3ª, la 2ª y la 1ª cuerda. Vas a notar que <b>cada cuerda pide fuerza "
    "distinta</b>: la 3ª es gruesa y cuesta, la 1ª es finita y se pasa sola. Por eso hay que practicarlo en cada una."),
    "e22", W, "70 BPM con backing. En las cuerdas finas, frená antes de lo que te parece."))

S.append(ejercicio(23, "Bending y vuelta (el release)", (
    "La mitad del bending que nadie practica: <b>la bajada</b>. Subís, sostenés, y volvés despacio y controlado — "
    "no soltando de golpe. Si soltás de golpe, todas las notas intermedias suenan como un resbalón."),
    "e23", W, "Lento, 60 BPM. La bajada tiene que durar lo mismo que la subida."))

S.append(ejercicio(24, "Lick de bending (escuela Gary Moore)", (
    "Cómo se usa de verdad: primero una frase que <b>hace esperar</b>, después el bending como el momento "
    "importante, y recién ahí la resolución. El bending pega porque llega tarde. Si bendeás todo el tiempo, "
    "no bendeás nada."),
    "e24", W, "Con backing lento. Grabate y escuchá si el bending llega a la nota o se queda a mitad de camino."))

S.append(Paragraph("Y AHORA SÍ: SALÍS DE LA CAJA 1", H2))
S.append(Paragraph(
    "Hasta este ejercicio todo el Hito 2 vivió en la caja 1, a propósito: no tenía sentido pelearte con "
    "la ubicación mientras aprendías a bendear. Pero ya sabés bendear, así que <b>es el momento de mudarte</b> — "
    "y no es casualidad que sea a la caja 2: es <b>la caja del bending</b>. Ahí la tónica de la 2ª cuerda "
    "(traste 10) tiene la 7ª menor justo un tono abajo, o sea exactamente a distancia de estirón.", BODY))
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

S.append(ejercicio(26, "El blue note, de paso", (
    "La primera nota del programa que <b>no pertenece a la pentatónica</b>: el MI bemol (3ª cuerda traste 8), "
    "el famoso <i>blue note</i>. Le pone la mugre al blues, pero con una regla estricta — "
    "<b>es una nota de paso, nunca de llegada</b>. Va metida entre el RE (traste 7) y el MI (traste 9), "
    "cruzándola sin frenar. Si te quedás parado en ella suena desafinado, porque lo está."),
    "e26", W,
    "Escuchá: cualquier shuffle de Clapton o de Page — está en todos. "
    "70 BPM. Tocá el compás 1 sin el MI bemol y después con él: esa diferencia es el sabor."))

# ============================================================ SEMANA 7
S.append(PageBreak())
S.append(banner(7, "VIBRATO — tu firma",
                "Objetivo: un vibrato parejo y elegido, no un tembleque nervioso. Es lo primero que te delata.", W))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "El vibrato es lo único de la guitarra que es <b>tuyo</b>: el de B.B. King, el de Clapton y el de Gary Moore "
    "se reconocen en una nota. Y también es lo que delata al amateur en una nota — porque el vibrato del amateur "
    "es involuntario: aparece del nervio, no de una decisión.", BODY))
S.append(tabla([
    [Paragraph("<b>Los 3 errores</b>", CELLB), Paragraph("<b>Cómo se arregla</b>", CELLB)],
    [Paragraph("Tembleque descontrolado", CELL),
     Paragraph("Medilo con metrónomo (ejercicio 25). Si no podés contar las ondas, no lo estás controlando: "
               "te está saliendo solo.", CELL)],
    [Paragraph("Vibrato con el dedo", CELL),
     Paragraph("Se hace con la <b>muñeca</b>, moviendo la mano entera como si girases un picaporte. El dedo "
               "solo no tiene fuerza ni regularidad.", CELL)],
    [Paragraph("Empezar a vibrar de inmediato", CELL),
     Paragraph("Dejá sonar la nota derecha medio segundo y <b>después</b> entrás con el vibrato. Ese retardo "
               "es lo que suena caro.", CELL)],
], [4.4 * cm, W - 4.4 * cm]))

S.append(ejercicio(27, "Vibrato medido (con metrónomo) — caja 2", (
    "La misma nota tres veces, con el vibrato contado: 2, 3 y 4 ondas por tiempo. Suena a ejercicio militar y "
    "esa es la idea — <b>vibrato que podés contar es vibrato que controlás</b>. Después vas a elegir la velocidad "
    "según la frase, pero primero tenés que poder elegirla.<br/><br/>"
    "Va en la <b>caja 2</b> (tónica: 2ª cuerda, traste 10), no en la 1. Ya bendeaste ahí en la semana pasada — "
    "esto sigue en el mismo territorio en vez de volver para atrás."),
    "e27", W, "60 BPM. Empezá por el lento: es el más difícil, porque el nervio te empuja a acelerar."))

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
    "la misma idea en la <b>caja 5</b>: abajo el silencio pesa distinto, y también hay que aprender a tolerarlo ahí."),
    "e31", W, "Con backing, obligatorio. Contá los tiempos del silencio en voz alta si hace falta."))

S.append(ejercicio(32, "Pregunta y respuesta — caja 2", (
    "Dos frases con el <b>mismo ritmo</b> y distinto final: la primera termina en una nota que queda colgada "
    "(pregunta), la segunda en la tónica (respuesta). Así habla la gente, y así hablan los buenos solos. "
    "Es la estructura más vieja y más efectiva que existe.<br/><br/>"
    "Otra vez en <b>caja 2</b>: la pregunta queda en el traste 8 (no resuelve), la respuesta cae en el "
    "traste 10 (la tónica). Practicalo acá antes de probarlo en la caja 1 de memoria."),
    "e32", W, "Con backing. Cuando salga, improvisá pregunta/respuesta con frases tuyas."))

S.append(ejercicio(33, "La misma frase en tres volúmenes — caja 2", (
    "Idéntica frase, tocada suave, normal y fuerte. La dinámica no se hace con la perilla: se hace con "
    "<b>cuánta púa le das a la cuerda</b>. Susurrar, hablar, gritar. Si tocás todo al mismo volumen, tu solo "
    "es un tipo que habla monótono durante un minuto.<br/><br/>"
    "La misma frase de los ejercicios 27 y 30 (caja 2), para no sumar una posición nueva justo cuando la "
    "cabeza está ocupada con la dinámica."),
    "e33", W, "Sin tocar el ampli ni el pedal. Todo con la mano derecha."))

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
    [Paragraph(CAJ, CELL), Paragraph("Mis bendings llegan afinados", CELL),
     Paragraph("Grabo el ejercicio 21 y el bending suena idéntico a la nota de destino.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Controlo la vuelta del bending", CELL),
     Paragraph("En el ejercicio 23 la bajada es gradual, no un resbalón.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Puedo elegir la velocidad de mi vibrato", CELL),
     Paragraph("Hago el ejercicio 25 y las tres velocidades son distintas y parejas.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Puedo bendear y vibrar la misma nota", CELL),
     Paragraph("El ejercicio 27 sale sin que se caiga la afinación del bending.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Tolero el silencio cuando improviso", CELL),
     Paragraph("En un minuto de improvisación hay al menos 4 silencios de más de 2 tiempos.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Mi solo tiene volumen variable", CELL),
     Paragraph("En la grabación se escucha claramente una parte suave y una fuerte.", CELL)],
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
