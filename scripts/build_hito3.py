# -*- coding: utf-8 -*-
"""Arma el PDF del Cuadernillo HITO 3 — EL VOCABULARIO.

Requiere que antes se haya corrido `gen_scores_h3.py` (genera ./partituras/e35..e51).
"""
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Spacer, PageBreak, TableStyle, KeepTogether

from cuadernillo_comun import (H1, H2, BODY, SMALL, CELL, CELLB, CAJ, IG, BLUE,
                               Diagrama, MapaBlueNotes, documento, tabla, banner, par, caja_oscura,
                               ejercicio, score, TablaturaEnBlanco)

doc = documento("Cuadernillo-Hito3-El-Vocabulario-EJERCICIOS.pdf",
                "HITO 3 — EL VOCABULARIO",
                "Robar licks con honestidad, armar tu solo · ejercicios con TAB y partitura",
                "Solo con Sabor · Hito 3 — El Vocabulario",
                "Hito 3 - El Vocabulario (ejercicios)")
W = doc.width
SOS = '<font name="Sym">♯</font>'   # sostenido: Helvetica no lo tiene
S = []

# ============================================================ INTRO
S.append(Paragraph("LO QUE TE FALTA NO SON NOTAS: ES QUÉ DECIR", H2))
S.append(Paragraph(
    "Con el Hito 1 conseguiste el <b>territorio</b> — sabés dónde están las notas. Con el Hito 2 conseguiste "
    "la <b>voz</b> — cada nota que tocás tiene algo tuyo. Y sin embargo, cuando improvisás, todavía sentís "
    "que no sabés qué tocar. Es lógico: te falta <b>vocabulario</b>.", BODY))
S.append(Paragraph(
    "Nadie improvisa de la nada. Page, Hendrix y Gary Moore no inventaban en el momento: tenían un banco de "
    "frases robadas, digeridas y transformadas durante años, y las combinaban. Improvisar no es crear de cero, "
    "<b>es hablar un idioma que ya tenés incorporado</b>. Este mes armás tu banco.", BODY))
S.append(Paragraph(
    "<b>Entregable del hito y del programa:</b> tu solo propio de 1 minuto, grabado. Ese video es tu trofeo.", BODY))

S.append(Paragraph("ROBAR CON HONESTIDAD: LOS 5 PASOS", H2))
S.append(Paragraph(
    "Copiar un lick nota por nota y pegarlo en tu solo no es robar: es fotocopiar, y se escucha. "
    "Robar de verdad es quedarte con el <b>mecanismo</b> — por qué esa frase funciona — y aplicarlo a lo tuyo. "
    "Estos son los 5 pasos, y ninguno se saltea.", BODY))
S.append(tabla([
    [Paragraph("<b>Paso</b>", CELLB), Paragraph("<b>Qué hacés</b>", CELLB),
     Paragraph("<b>Cómo sabés que terminaste</b>", CELLB)],
    [Paragraph("<b>1 · ESCUCHAR</b>", CELLB),
     Paragraph("Elegís UNA frase de 2 o 3 segundos que te haya erizado la piel. Una. La escuchás 20 veces.", CELL),
     Paragraph("Podés cantarla entera de memoria, sin la guitarra en la mano.", CELL)],
    [Paragraph("<b>2 · SACAR</b>", CELLB),
     Paragraph("La buscás en el mástil de oído. Sin TAB, sin YouTube, sin preguntar.", CELL),
     Paragraph("La tocás igual que en el disco, aunque sea lento y feo.", CELL)],
    [Paragraph("<b>3 · COPIAR</b>", CELLB),
     Paragraph("La imitás con todo: el fraseo, el vibrato, la fuerza, la mugre. Hasta la respiración.", CELL),
     Paragraph("Al grabarte, se parece — no solo las notas: el <i>gesto</i>.", CELL)],
    [Paragraph("<b>4 · VARIAR</b>", CELLB),
     Paragraph("Le cambiás el ritmo, el remate y la caja. Tres versiones distintas mínimo (ej. 44, 45 y 46).", CELL),
     Paragraph("Podés tocar 3 versiones sin pensar cuál era la original.", CELL)],
    [Paragraph("<b>5 · APROPIAR</b>", CELLB),
     Paragraph("La usás improvisando, mezclada con lo tuyo, sin anunciarla.", CELL),
     Paragraph("Te sale sola en una improvisación, sin que la hayas planeado. <b>Ahí ya es tuya.</b>", CELL)],
], [2.4 * cm, 6.4 * cm, W - 8.8 * cm]))
S.append(Paragraph(
    "El error de todos: quedarse en el paso 3. Por eso hay gente que sabe 200 licks y suena a nadie. "
    "Un lick que atravesó los 5 pasos vale más que cincuenta guardados en una carpeta.", SMALL))

S.append(Paragraph("UNA ACLARACIÓN SOBRE LAS PARTITURAS DE ESTE CUADERNILLO", H2))
S.append(Paragraph(
    "Acá vas a ver dos cosas distintas, y conviene que sepas cuál estás mirando en cada página.", BODY))
S.append(Paragraph(
    "<b>Los ejercicios numerados (del 35 al 53) NO son transcripciones</b> de solos de nadie: son frases "
    "originales escritas <i>en el estilo de</i> cada escuela. Es a propósito, y es exactamente el punto del "
    "hito. Lo que se enseña acá no son las notas de Page — es el <b>mecanismo</b> que hace que las frases de "
    "Page funcionen. Ese mecanismo no tiene dueño, y es lo único que te sirve para inventar lo tuyo.", BODY))
S.append(Paragraph(
    "<b>Las páginas marcadas como CITA son otra cosa:</b> ésas sí son transcripciones, y están para que veas "
    "el mecanismo en su hábitat — tocado por el que lo inventó, en un disco de verdad. <b>No se practican "
    "como los ejercicios.</b> Se escuchan, se miran, y se les busca el recurso adentro. Cada cita te dice "
    "exactamente qué mirar; si te ponés a sacarla nota por nota antes de tiempo, estás haciendo otra cosa.", BODY))

# ============================================================ LAS DOS ESCUELAS
S.append(PageBreak())
S.append(Paragraph("LAS DOS ESCUELAS (y qué robarle a cada una)", H1))
S.append(Paragraph(
    "Casi todo el rock sale de dos formas de pensar la misma pentatónica. No son mejores ni peores: son "
    "<b>dos maneras de hacer que una frase signifique algo</b>. Vas a estudiar una por semana, y en el solo "
    "final vas a usar las dos.", BODY))
S.append(tabla([
    [Paragraph("", CELLB), Paragraph("<b>BRITÁNICA</b> (semana 9)", CELLB),
     Paragraph("<b>AMERICANA</b> (semana 10)", CELLB)],
    [Paragraph("<b>La frase vale por…</b>", CELLB),
     Paragraph("la <b>insistencia</b>. Un motivo corto repetido hasta que se vuelve un riff.", CELL),
     Paragraph("la <b>melodía</b>. Una frase larga que respira como una voz que canta.", CELL)],
    [Paragraph("<b>Sensación</b>", CELLB),
     Paragraph("Agresiva, rítmica, te empuja hacia adelante.", CELL),
     Paragraph("Vocal, espaciosa, te deja caer.", CELL)],
    [Paragraph("<b>Recursos típicos</b>", CELLB),
     Paragraph("Motivo repetido · dobles cuerdas · unísonos · ataque de púa fuerte.", CELL),
     Paragraph("Bendings largos · legato · slides · silencios grandes.", CELL)],
    [Paragraph("<b>Referentes</b>", CELLB),
     Paragraph("Jimmy Page, Angus Young, Clapton.", CELL),
     Paragraph("Hendrix, Slash, Gary Moore, B.B. King.", CELL)],
    [Paragraph("<b>Qué robarle</b>", CELLB),
     Paragraph("Que <b>no hace falta una nota nueva</b> para sostener una frase: alcanza con repetir bien.", CELL),
     Paragraph("Que <b>una sola nota bien estirada</b> dice más que doce apuradas.", CELL)],
], [3.0 * cm, (W - 3.0 * cm) / 2, (W - 3.0 * cm) / 2]))
S.append(Paragraph(
    "<b>Los nombres son de estilo, no de pasaporte.</b> Gary Moore era de Belfast y Slash nació en "
    "Inglaterra, y los dos están en la columna \"americana\" — porque tocan así, no por dónde nacieron. "
    "Lo mismo al revés: lo \"británico\" es una forma de pensar la frase (insistir) que también usan "
    "guitarristas de cualquier otro lado. Quedate con el mecanismo, no con la etiqueta.", SMALL))

S.append(Paragraph("CÓMO SACAR UN LICK DE OÍDO (el paso que todos evitan)", H2))
S.append(Paragraph(
    "Sacar de oído es incómodo y por eso casi nadie lo hace — se va directo a buscar la TAB. Pero es "
    "justamente la incomodidad la que entrena: <b>buscar y errar es el ejercicio</b>. Si mirás la TAB, "
    "aprendés dónde poner los dedos y no aprendés nada más.", BODY))
S.append(tabla([
    [Paragraph("<b>Paso</b>", CELLB), Paragraph("<b>Cómo</b>", CELLB)],
    [Paragraph("Achicá el bocado", CELL),
     Paragraph("Dos segundos de música, no un solo entero. Una frase. Si te cuesta, media frase.", CELL)],
    [Paragraph("Bajá la velocidad", CELL),
     Paragraph("En YouTube: engranaje → velocidad → 0.5x o 0.25x (no cambia el tono). En el celular hay apps "
               "que loopean un fragmento: buscá \"slow downer\" o \"transcribe\".", CELL)],
    [Paragraph("Cantala primero", CELL),
     Paragraph("Antes de tocar nada. Si no la podés cantar, no la escuchaste bien todavía. "
               "(Es el mismo ejercicio del oído que ya venís haciendo.)", CELL)],
    [Paragraph("Buscá SOLO la primera nota", CELL),
     Paragraph("Es el 80% del trabajo. Cuando la clavás, el resto cae casi solo porque ya conocés la escala.", CELL)],
    [Paragraph("Anotala en el banco", CELL),
     Paragraph("En la hoja de tablatura en blanco del final. Y escribí <b>qué le robaste</b>, no solo las notas.", CELL)],
], [4.0 * cm, W - 4.0 * cm]))

S.append(Paragraph("LA RUTINA DIARIA (20 minutos)", H2))
S.append(tabla([
    [Paragraph("<b>Min</b>", CELLB), Paragraph("<b>Qué</b>", CELLB), Paragraph("<b>Foco</b>", CELLB)],
    [Paragraph("0–3", CELLB), Paragraph("Calentás con un ejercicio del Hito 1 o 2", CELL),
     Paragraph("No perder el mapa ni el sabor mientras sumás vocabulario.", CELL)],
    [Paragraph("3–8", CELLB), Paragraph("Los licks de la semana, prolijos", CELL),
     Paragraph("Que suenen como el ejemplo, no parecido.", CELL)],
    [Paragraph("8–13", CELLB), Paragraph("<b>Variaciones</b> del lick (ritmo, remate, caja)", CELL),
     Paragraph("Acá el lick deja de ser prestado.", CELL)],
    [Paragraph("13–20", CELLB), Paragraph("<b>Improvisás</b> metiendo el lick sin anunciarlo", CELL),
     Paragraph("Que entre y salga de tus frases sin que se note el pegote.", CELL)],
], [1.5 * cm, 6.9 * cm, W - 8.4 * cm]))

# ============================================================ SEMANA 9
S.append(PageBreak())
S.append(banner(9, "ESCUELA BRITÁNICA — la fuerza está en repetir",
                "Objetivo: entender que una frase corta, insistida con convicción, vale más que una larga y prolija.", W))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "La idea que hay que entender esta semana es contraintuitiva: <b>repetir no es falta de ideas</b>. "
    "Cuando escuchás un solo de Zeppelin o de AC/DC y te queda pegado, casi nunca es por una melodía "
    "elaborada — es porque una celda de tres notas se te metió en la cabeza a fuerza de insistencia. "
    "Es la misma lógica de un riff, aplicada al solo.", BODY))
S.append(Paragraph(
    "<b>Y una advertencia sobre dónde están escritos estos licks.</b> Cada uno vive en una caja distinta: "
    "el primero en la 1, el segundo en la 2, el tercero en la 3, y el cuarto los encadena a los tres "
    "atravesando el mástil. Está hecho a propósito y es la mitad de la lección: un recurso <b>no pertenece "
    "a una posición</b>. Si te cuesta ubicar el dibujo, volvé al mapa del Hito 1 — no es material nuevo, "
    "es territorio que ya recorriste.", SMALL))

S.append(ejercicio(35, "El motivo que se repite (caja 1)", (
    "Una celda de tres notas, machacada cinco veces, y recién en la sexta resolvés. Vas a sentir que "
    "<b>estás repitiendo demasiado</b> — esa sensación es la trampa: desde adentro siempre parece más "
    "repetido de lo que se escucha desde afuera. Grabate y vas a ver que suena convincente, no monótono.<br/><br/>"
    "Éste es el único de la semana que va en la caja 1, y es a propósito: es tu <b>punto de comparación</b>. "
    "En el ejercicio 47 vas a tocar esta misma celda tres cajas más arriba, y la diferencia solo se escucha "
    "si tenés ésta en el oído."),
    "e35", W, "60 BPM en tresillos. El pull-off va en la 1ª cuerda (8 al 5); el Sol de la 2ª se puntea."))

S.append(ejercicio("35-bis", "CITA — Angus Young / AC/DC, \"Highway to Hell\" (caja 1)", (
    "Los primeros compases del solo, tal como los toca Angus: exactamente el recurso del ej. 35, tocado "
    "por la escuela británica en un disco real. Ni bien arranca hace una repetición — bendeá y soltá, "
    "cuatro veces — antes de aflojar a medio tono y después a un cuarto."),
    "e35bis", W, "60 BPM. Todo en la 1ª cuerda, traste 5. El cuarto de tono es el más difícil: apenas movés "
    "la cuerda, no le pongas fuerza de bend entero."))

S.append(ejercicio(36, "Dobles cuerdas (caja 2)", (
    "Dos notas juntas, con la púa barriendo las dos cuerdas de una. Es el sonido de Chuck Berry y de medio "
    "AC/DC: suena más grande que una nota sola sin necesidad de tocar más rápido. Cuidá que las dos suenen "
    "parejas — si una se escucha más, estás inclinando la púa.<br/><br/>"
    "Va en la <b>caja 2</b> (trastes 7 a 10). Es el mismo mecanismo que harías en la caja 1: dos cuerdas "
    "agudas, dos formas que alternan. <b>Corriste la mano tres trastes, nada más.</b>"),
    "e36", W, "70 BPM. Apagá con la mano derecha las cuerdas que no usás: si zumba algo, se arruina."))

S.append(ejercicio("36-bis", "CITA — Angus Young, \"pentatónica + 6\" (caja 3-4)", (
    "El otro truco clásico de Angus, además de la celda repetida: agregarle a la pentatónica menor "
    "el <b>6º grado</b> (FA#), una nota que no es blue note ni la 2ª que ya conocés — es un color "
    "distinto, más dulce, casi mayor.<br/><br/>"
    "Subís por la 3ª cuerda pisando esa nota de paso, llegás arriba con medio tono de bending, y "
    "bajás por el mismo camino cerrando con un cuarto de tono. La misma pentatónica de siempre, "
    "con una sola nota prestada que le cambia el humor."),
    "e36bis", W, "El FA# es de paso, igual que el blue note del ej. 26: no te quedes parado en él, "
    "es el puente hacia el bending, no el destino."))

S.append(ejercicio(37, "El unísono (dos cuerdas, la misma nota) — caja 3", (
    "El recurso más impactante de la escuela británica. Tocás dos cuerdas juntas y <b>bendeás la de abajo "
    "hasta que suene exactamente igual que la de arriba</b>. Cuando están afinadas, las dos notas se pelean "
    "y producen un batido que suena enorme. Cuando no, suena horrible — no hay término medio, y por eso "
    "es el mejor test de afinación de bending que existe.<br/><br/>"
    "Acá va en la <b>caja 3</b>: bendeás el traste 12 de la 3ª cuerda hasta igualar el 10 de la 2ª. "
    "Es exactamente la misma relación que en la caja 1 (7ª contra 5ª) — la forma es idéntica, corrida."),
    "e37", W, "Lento, sin metrónomo. Escuchá el batido: cuando desaparece, llegaste."))

S.append(ejercicio("37-bis", "CITA — Angus Young, Lick 1, unísono con bending (compases 2 a 4)", (
    "El mismo mecanismo del ejercicio 37 — la nota fija arriba, y abajo una serie de bendings completos "
    "que van igualándola — pero tocado por Angus, bajando de posición cuatro veces: de la caja 4 a la "
    "caja 1.<br/><br/>"
    "Fijate que cada bending cuesta distinto según la posición — ya lo viste en el ej. 22 del Hito 2. "
    "Acá lo tenés cuatro veces seguidas, bajando: la mano tiene que reajustar la fuerza en cada uno."),
    "e37bis", W, "70 BPM. Cada bending es de un tono completo — no lo sueltes de golpe, dejalo sonar "
    "arriba antes de bajar al siguiente."))

S.append(ejercicio(38, "Los tres recursos encadenados (y el viaje)", (
    "Motivo repetido, dobles cuerdas y unísono en una sola frase. Fijate cuántas notas distintas usaste: "
    "casi ninguna. Toda la fuerza vino del <b>tratamiento</b>, no del material.<br/><br/>"
    "Y fijate en algo más: cada recurso está en la caja donde lo aprendiste — celda en la 1, dobles cuerdas "
    "en la 2, unísono en la 3. <b>La frase sube por el mástil sola</b>, porque el vocabulario que usás vive "
    "repartido. Así se arma un solo que se mueve sin que el movimiento parezca un ejercicio."),
    "e38", W, "Con backing. Tocalo como si estuvieras enojado: esta escuela pide convicción, no delicadeza."))

# ============================================================ SEMANA 10
S.append(PageBreak())
S.append(banner(10, "ESCUELA AMERICANA — la frase que canta",
                "Objetivo: frases largas, vocales, con espacio. Lo opuesto exacto de la semana pasada.", W))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "Si la escuela británica empuja, ésta <b>deja caer</b>. Las frases son más largas, más ligadas, y "
    "sobre todo: dejan lugar. El truco mental es simple — <b>imaginá que estás cantando</b>. Un cantante "
    "respira, sostiene, y no dice dos ideas al mismo tiempo. Si tu frase no la podés cantar, es porque "
    "la pensaste con los dedos.", BODY))

S.append(ejercicio(39, "La frase vocal (escuela Gary Moore) — caja 4", (
    "Tres compases y apenas un puñado de notas. La estructura es la de una frase hablada: una entrada que "
    "<b>hace esperar</b>, un bending largo que es el momento importante, y una bajada que resuelve. "
    "Lo difícil acá no es tocarlo: es aguantar los silencios sin rellenarlos.<br/><br/>"
    "Va arriba de todo, en la <b>caja 4</b> (trastes 12 a 15), porque ahí es donde esta escuela realmente "
    "vive: el registro agudo hace la mitad del trabajo emocional. La misma frase en la caja 1 suena "
    "correcta; acá arriba <b>suena a que alguien está diciendo algo</b>."),
    "e39", W, "Con backing lento. Cantala antes de tocarla, aunque desafines. Ojo: trastes angostos, menos fuerza."))

S.append(ejercicio("39-bis", "El slide previo y el double stop fantasma (Gary Moore) — caja 4", (
    "Dos trucos que separan un bending \"tocado\" de uno \"cantado\", los dos de la misma clase de Gary "
    "Moore. <b>Primero, el slide previo:</b> en vez de pisar la nota y estirar de una, deslizate hacia "
    "ella. El bend deja de sonar a golpe y empieza a sonar <i>slick</i> — fluido, con intención.<br/><br/>"
    "<b>Segundo, el double stop fantasma:</b> mientras sostenés el bend en la 1ª cuerda, la punta de ese "
    "mismo dedo roza la 2ª cuerda de al lado — <b>sin estirarla</b>. No es el bend a dos cuerdas del "
    "ejercicio 37 (ahí las dos se estiran juntas hasta empatar): acá una suena estirada y la otra suena "
    "fija, y esa fricción es lo que le agrega cuerpo al momento más intenso del solo. Es un gesto de mano "
    "derecha, así que no está dibujado en el pentagrama — practicalo directamente sobre la partitura del "
    "ejercicio 39, en el mismo compás del bending largo.<br/><br/>"
    "<i>Nota de transporte: la clase original está en Do menor, traste 18. Acá está pasada a La menor "
    "(3 trastes abajo, traste 15) para que caiga en la misma caja 4 que ya conocés del ejercicio 39.</i>"),
    "e39bis", W, "Practicá el slide solo, después el double stop solo, y recién ahí los dos juntos. "
    "El error típico es apurar el slide — dale el mismo tiempo que le darías a una palabra."))

S.append(ejercicio(40, "La línea fluida (escuela Slash) — de la caja 4 a la 1", (
    "Casi todo ligado: en dos compases puntéas tres o cuatro veces nada más. El resultado es una línea que "
    "<b>se derrama</b> por el mástil en vez de marcar cada nota. Empezá lento — si acelerás antes de tiempo, "
    "los ligados se apagan y queda un murmullo.<br/><br/>"
    "Y acá \"derramarse por el mástil\" es literal: <b>arranca en la caja 4 y termina en la 1</b>, bajando "
    "en diagonal. Es el mismo movimiento del ejercicio 15 del Hito 1, ahora con vocabulario encima."),
    "e40", W, "60 BPM y subís. Que las notas ligadas suenen igual de fuerte que las punteadas."))

S.append(ejercicio(41, "Dobles cuerdas con ligado (remate estilo Hendrix) — caja 2", (
    "Dobles cuerdas otra vez, pero acá el hammer-on va <b>en la cuerda de abajo mientras la de arriba se "
    "sostiene</b>. Ese movimiento es la marca registrada de Hendrix y de todo el R&B. Es más difícil de lo "
    "que parece: el dedo que golpea tiene que ser preciso para no apagar la otra cuerda.<br/><br/>"
    "En la <b>caja 2</b>: el hammer va del traste 7 al 9 en la 3ª cuerda, mientras la 2ª sostiene el 8. "
    "Compará con el ejercicio 36, que también es de dobles cuerdas y está en la misma caja: "
    "<b>mismo barrio, dos mecanismos distintos</b>."),
    "e41", W, "Lento. Si la nota de arriba se corta cuando hacés el hammer, tocás con demasiada fuerza."))

S.append(ejercicio(42, "Los tres recursos encadenados (y el viaje de vuelta)", (
    "La línea fluida, la doble cuerda con ligado y el bending largo en una sola frase. Compará esta página "
    "con el ejercicio 38: <b>la misma escala, el mismo mástil, dos idiomas distintos</b>.<br/><br/>"
    "Fijate también en la dirección. El 38 (británico) <b>sube</b> de la caja 1 a la 3; éste <b>baja</b> "
    "de la 4 a la 1. No es casualidad: la escuela británica empuja hacia adelante y la americana deja caer, "
    "y eso también se escribe en el mástil."),
    "e42", W, "Con backing. Tocalo relajado, casi perezoso. Esta escuela pide calma, no convicción."))

# ============================================================ SEMANA 11
S.append(PageBreak())
S.append(banner(11, "HACERLO TUYO — las 3 variaciones y la arquitectura",
                "Objetivo: que un lick prestado deje de sonar prestado, y entender cómo se arma un solo entero.", W))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "Esta es la semana que separa a quien colecciona licks de quien improvisa. La operación es siempre la "
    "misma: agarrás una frase y le cambiás <b>una sola cosa por vez</b> — el ritmo, el remate, o el lugar "
    "del mástil. Con tres variaciones, un lick robado ya es material tuyo: nadie puede señalar de dónde salió.", BODY))

S.append(Paragraph(
    "Pero antes de tocar una variación hay que entender algo que venimos usando sin nombrar: "
    "<b>cada nota de la escala tiene un carácter propio</b>. Ya sabés que cerrar en la tónica suena a "
    "conclusión. Lo que casi nadie te cuenta es que las otras cuatro también dicen algo, y elegir bien "
    "en cuál caés es lo que hace que un remate funcione o no.", BODY))
S.append(Spacer(1, 2))
S.append(par([Diagrama(1, W * 0.5, grados=True,
                       titulo="CAJA 1 — el grado de cada nota"),
              Paragraph("Mirá el mismo dibujo de siempre con otra información: en vez de las notas, "
                        "<b>los grados</b>. La pentatónica menor tiene cinco: <b>1 · 3ª menor · 4ª · 5ª · 7ª menor</b>."
                        "<br/><br/>"
                        "Y fijate lo que <b>no</b> tiene: 2ª, 3ª mayor, 6ª ni 7ª mayor. Justo los grados que "
                        "pueden chocar contra el acorde. <b>Por eso la pentatónica \"no tiene notas "
                        "equivocadas\"</b> — no es magia, es que le sacaron las conflictivas.", BODY)],
             [W * 0.5, W * 0.5]))
S.append(Spacer(1, 6))
S.append(tabla([
    [Paragraph("<b>Grado</b>", CELLB), Paragraph("<b>Nota en Lam</b>", CELLB),
     Paragraph("<b>Qué sensación deja si caés ahí</b>", CELLB), Paragraph("<b>Para qué la usás</b>", CELLB)],
    [Paragraph("<b>1ª · tónica</b>", CELLB), Paragraph("LA", CELL),
     Paragraph("<b>Reposo total.</b> Llegaste, no falta nada. Es el punto final de la oración.", CELL),
     Paragraph("Cerrar el solo. Terminar una respuesta.", CELL)],
    [Paragraph("<b>3ª menor</b>", CELLB), Paragraph("DO", CELL),
     Paragraph("Descanso, pero <b>triste</b>. Es la nota que hace que todo suene menor.", CELL),
     Paragraph("Terminar sin cerrar del todo. Darle color melancólico.", CELL)],
    [Paragraph("<b>4ª</b>", CELLB), Paragraph("RE", CELL),
     Paragraph("<b>Suspenso.</b> Queda pidiendo moverse: el oído espera que sigas.", CELL),
     Paragraph("Dejar una pregunta abierta. Empujar hacia la frase siguiente.", CELL)],
    [Paragraph("<b>5ª</b>", CELLB), Paragraph("MI", CELL),
     Paragraph("<b>Firme y abierta.</b> Sólida, pero no cerrada — suena a \"sigo\".", CELL),
     Paragraph("Sostener el medio de un solo. Frenar sin terminar.", CELL)],
    [Paragraph("<b>7ª menor</b>", CELLB), Paragraph("SOL", CELL),
     Paragraph("<b>Flotando.</b> La más inestable y la más bluesera de todas.", CELL),
     Paragraph("Tensión, mugre, momentos de clímax. Nunca para cerrar.", CELL)],
    [Paragraph("<b>8ª · tónica</b>", CELLB), Paragraph("LA (arriba)", CELL),
     Paragraph("Reposo otra vez, pero <b>más brillante</b>: cierra con energía, no con calma.", CELL),
     Paragraph("Cerrar un solo hacia arriba, triunfal.", CELL)],
], [2.2 * cm, 2.0 * cm, (W - 4.2 * cm) * 0.56, (W - 4.2 * cm) * 0.44]))

S.append(ejercicio(43, "El color de cada grado (la prueba del reposo)", (
    "Seis notas largas, una por compás, subiendo de la tónica a la octava — todas dentro de la caja 1. "
    "<b>Tocá cada una con el backing sonando y quedate ahí cuatro tiempos enteros</b>, escuchando qué te "
    "produce. No es un ejercicio de manos: es de oído. Vas a sentir físicamente que la 4ª te pide moverte "
    "y que la tónica te deja tranquilo."),
    "e43", W,
    "Con backing, obligatorio: solo, no hay contra qué medir la sensación. Hacelo con los ojos cerrados."))

S.append(Paragraph(
    "Cuando esto se te vuelve automático dejás de improvisar a ciegas: <b>ya no elegís notas, elegís "
    "sensaciones</b>. Los tres ejercicios que siguen son exactamente eso aplicado.", SMALL))

# ============================================================ LAS NOTAS DE AFUERA
S.append(PageBreak())
S.append(Paragraph("LAS NOTAS DE AFUERA (las que no están en la tabla de arriba)", H1))
S.append(Paragraph(
    "La tabla anterior tiene cinco filas porque la pentatónica tiene cinco notas. Y ya sabés por qué no "
    "tiene notas equivocadas: le faltan justo la 2ª, la 3ª mayor, la 6ª y la 7ª mayor — las que pueden "
    "chocar. Ahora que ya tenés el mapa (Hito 1), la voz (Hito 2) y entendés el color de cada grado, "
    "es el momento de agregar <b>tres notas de afuera</b>. Ojo con cómo lo leés: <b>no son escalas nuevas "
    "y no vas a tener que aprender cinco cajas más</b>. Son tres notas que se meten en el mapa que ya "
    "tenés, cada una con una regla. Eso es literalmente lo único que separa tu pentatónica de la de "
    "Gilmour o la de Frusciante.", BODY))
S.append(Spacer(1, 4))
S.append(tabla([
    [Paragraph("<b>Nota</b>", CELLB), Paragraph("<b>En Lam</b>", CELLB),
     Paragraph("<b>Qué le hace a la frase</b>", CELLB), Paragraph("<b>La regla</b>", CELLB)],
    [Paragraph("<b>blue note</b><br/>(entre 4ª y 5ª)", CELLB), Paragraph("MI bemol", CELL),
     Paragraph("<b>Ensucia.</b> Le mete la mugre del blues, tensión que pide resolver.", CELL),
     Paragraph("De <b>paso</b>, nunca de llegada. Cruzala rápido, sin vibrato.", CELL)],
    [Paragraph("<b>2ª / 9ª</b>", CELLB), Paragraph("SI", CELL),
     Paragraph("<b>Da aire.</b> Abre la frase, la vuelve más melódica y menos blusera. "
               "Es el color de Californication y de Gilmour — y no es casualidad: Clapton y John Mayer "
               "la usan tanto que en algunos círculos ya la llaman \"la novena de los prolijos\".", CELL),
     Paragraph("Se puede <b>sostener</b> y vibrar. La más segura de las tres.", CELL)],
    [Paragraph("<b>6ª</b>", CELLB), Paragraph("FA  /  FA" + SOS, CELL),
     Paragraph("<b>Endulza o entristece, según cuál.</b> Tiene dos versiones y son casi "
               "opuestas — mirá el recuadro de abajo.", CELL),
     Paragraph("Se puede sostener, pero <b>elegí la correcta</b> según el acorde.", CELL)],
], [2.6 * cm, 1.9 * cm, (W - 4.5 * cm) * 0.53, (W - 4.5 * cm) * 0.47]))

S.append(Paragraph("LAS DOS SEXTAS (la única que tiene trampa)", H2))
S.append(Paragraph(
    "Es la única de las tres que exige una decisión, y por eso se explica aparte. La <b>6ª menor</b> "
    "(FA) es la de la escala menor natural: oscura, dramática, de balada — es la que usa Frusciante en "
    "Californication, que está en Fa" + SOS + " menor, y la que hace que un solo suene triste en vez de "
    "bluesero. La <b>6ª mayor</b> (FA" + SOS + ") es la contraria: dulce, brillante, la nota del "
    "\"BB box\", la firma de B.B. King.", BODY))
S.append(Paragraph(
    "<b>Cómo elegís:</b> escuchá el acompañamiento. Si la base es un vamp menor tipo Lam–Fa–Sol "
    "(o cualquier balada menor), va la <b>6ª menor</b>. Si la base es un blues o un vamp con séptimas, "
    "va la <b>6ª mayor</b>. Metida al revés, cualquiera de las dos suena mal — y no es tu oído fallando, "
    "es la nota chocando de verdad contra el acorde. La <b>6ª mayor</b> —el \"BB box\"— es territorio "
    "para después del programa: por ahora te alcanza con saber que existe y por qué suena distinta.", SMALL))

S.append(PageBreak())
S.append(Paragraph("EL BLUE NOTE EN TODO EL MÁSTIL", H2))
S.append(Paragraph(
    "De las tres, el blue note es el que ya probaste: en el Hito 2 (ej. 26) lo tocaste en un solo lugar "
    "— caja 2, 3ª cuerda, traste 8. Ahora que tenés el mapa completo podés ver la foto entera: "
    "<b>hay un blue note por cuerda y por octava en todo el mástil</b>. No era una excepción de la "
    "caja 2, es parte del mapa.", BODY))
S.append(Spacer(1, 4))
S.append(MapaBlueNotes(W))
S.append(Spacer(1, 4))
S.append(Paragraph(
    "<font color=\"#%s\"><b>●</b></font> el blue note en cada cuerda y octava dentro del mástil. Fijate que "
    "caen en las costuras entre cajas — es otra prueba de que las costuras no son frontera, son "
    "territorio compartido. <b>La regla no cambia por tener más lugares donde usarla:</b> es una nota de "
    "PASO, nunca de llegada. Cruzala rápido entre la 4ª y la 5ª, en cualquier dirección, y nunca la "
    "sostengas ni le hagas vibrato — ahí es donde deja de sonar a blues y empieza a sonar a error."
    % BLUE.hexval()[2:], SMALL))
S.append(caja_oscura(
    '<font color="#f7d7d2" size="9">Estas tres notas son el techo del programa, no el piso de otro. '
    'No hay que "estudiar la escala menor natural": si ya te movés por las cinco cajas, agregar la 2ª '
    'y la 6ª es correr un dedo. <font color="white"><b>Lo difícil nunca fue saber más notas — fue '
    'saber cuándo usarlas.</b></font></font>', W))

S.append(ejercicio(44, "Mismas notas, tres ritmos distintos (cajas 2 y 3)", (
    "Las mismas seis notas escritas tres veces, con tres ritmos: parejo, acelerando, y a contratiempo. "
    "Escuchá los tres seguidos: <b>suenan a tres licks distintos</b>, y no cambiaste ni una nota. "
    "El ritmo es el 70% de la identidad de una frase, y es lo primero que hay que tocar.<br/><br/>"
    "La frase está escrita entre las <b>cajas 2 y 3</b>, no en la 1. Y fijate que las tres versiones están "
    "en la MISMA posición: es a propósito. Si cambiara de caja entre una y otra, no sabrías si lo que cambió "
    "el sonido fue el ritmo o el registro. Acá la única variable es el ritmo.<br/><br/>"
    "Si este juego de <b>mover el ritmo sin cambiar las notas</b> te enganchó, en el Anexo de Ritmo del "
    "Hito 2 (ej. A, Las 3 velocidades) hay la otra cara de la moneda: la MISMA idea metida en menos espacio, "
    "recorriendo las cinco cajas. Ahí es donde el ritmo deja de ser una variante y se convierte en una "
    "decisión compositiva."),
    "e44", W, "70 BPM. El tercero (a contratiempo) es el más difícil: contá en voz alta si hace falta."))

S.append(ejercicio(45, "Mismo arranque, tres remates (cajas 2 y 3)", (
    "Acá se aplica lo del ejercicio anterior. La frase entra igual las tres veces y cambia solo la última nota: "
    "primero cae en la <b>4ª</b> (queda colgada, es una pregunta), después en la <b>tónica</b> (cierra, es la "
    "respuesta), y por último en la <b>3ª menor</b> (resuelve para arriba, con color triste). "
    "El remate es lo que el oído se lleva: <b>cambiar el final cambia el significado de todo lo anterior</b>, "
    "igual que en una oración.<br/><br/>"
    "Mismo criterio que el 44: la frase vive entre las cajas 2 y 3, y las tres versiones comparten posición "
    "para que la única variable sea <b>dónde caés</b>."),
    "e45", W, "Con backing. Antes de tocar cada versión, adiviná qué va a pasar. Después comprobá."))

S.append(ejercicio(46, "EL MISMO LICK EN LAS CINCO CAJAS", (
    "<b>El ejercicio que demuestra la tesis del programa entero.</b> Una sola frase, escrita cinco veces: "
    "en la caja 5, la 1, la 2, la 3 y la 4 — en ese orden, o sea recorriendo el mástil de abajo hacia arriba. "
    "Mismas notas, mismo ritmo, mismo dibujo. <b>Lo único que cambia es dónde ponés la mano.</b><br/><br/>"
    "Mirá la partitura sin leer la tablatura: las cinco líneas son <i>idénticas</i>. Ahora mirá la tablatura: "
    "no se parecen en nada. Eso es todo lo que hay que entender — <b>un lick no es un lugar del mástil, es un "
    "patrón</b>. Si lo tenés en una caja lo tenés en las cinco, y acá se paga entero el trabajo del Hito 1.<br/><br/>"
    "Y ahora lo fino, que es lo que hace que este ejercicio valga la pena. Las cinco versiones no suenan "
    "<i>parecido</i>: son <b>literalmente las mismas seis alturas</b> — el mismo LA, el mismo SOL, el mismo MI. "
    "No hay una más aguda que otra. Lo único que cambia es <b>en qué cuerdas las tocás</b>, y eso cambia el "
    "color:<br/><br/>"
    "· La versión de la <b>caja 5</b> vive en las cuerdas <b>1ª, 2ª y 3ª</b>, abajo en el mástil (trastes 2-5). "
    "Cuerda fina + traste bajo = sonido <b>abierto y brillante</b>, con más ataque. Casi suena a que estuvieras "
    "usando cuerdas al aire.<br/>"
    "· La versión de la <b>caja 4</b> vive en las cuerdas <b>3ª, 4ª y 5ª</b>, arriba (trastes 12-15). "
    "Cuerda gruesa + traste alto = sonido <b>gordo y redondo</b>, con más sustain y más cuerpo. Es la zona "
    "donde la guitarra más se parece a una voz — y de paso, donde el bending sale más fácil, porque la cuerda "
    "está más floja (acordate del ejercicio 22).<br/><br/>"
    "Ninguna de las dos es mejor. Son dos <b>timbres</b> distintos para decir exactamente lo mismo. Por eso "
    "mudarse de caja no es un requisito de checklist: es una <b>decisión expresiva</b>, y a partir de acá la "
    "tomás vos.<br/><br/>"
    "<i>Ojo con una confusión fácil: la caja 5 de ESTE ejercicio no es la caja 5 del ejercicio 48. Acá está "
    "tocada en las cuerdas finas y suena brillante; allá está tocada una octava más abajo, en la 5ª y la 6ª, "
    "y por eso suena a riff. Misma caja, dos registros distintos — la caja te dice dónde poner la mano, no "
    "qué tan grave va a sonar.</i>"),
    "e46", W,
    "Lento, una caja por día si hace falta. Cuando las cinco te salgan, hacé esto: poné el backing, "
    "improvisá, y cada vez que uses esta frase elegí una caja distinta según lo que quieras que suene."))

S.append(Paragraph("DOS LICKS MÁS, EN LOS DOS EXTREMOS DEL MÁSTIL", H2))
S.append(Paragraph(
    "Venís tocando vocabulario repartido por las cajas 1, 2, 3 y 4 desde la semana 9. Estos dos cierran el "
    "mapa: uno vuelve a la <b>caja 3</b> — y es a propósito la misma celda del ejercicio 35, para que la "
    "comparación sea directa — y el otro baja a la <b>caja 5</b>, la única zona que todavía no habías "
    "pisado en este hito.", BODY))

S.append(ejercicio(47, "La celda repetida, tres cajas más arriba (caja 3)", (
    "Es <b>exactamente el mecanismo del ejercicio 35</b> — la celda de tres notas machacada hasta que se "
    "vuelve un gancho — pero en la caja 3, entre los trastes 10 y 13. Tocá el 35 y después éste, seguidos: "
    "vas a escuchar que es la misma idea y que <b>suena a otra cosa</b>. Más brillante, más urgente, más "
    "cerca de un solo de Cream que de uno de AC/DC. La frase no cambió: cambió el barrio."),
    "e47", W,
    "Escuchá: Clapton en Cream — casi todo su vocabulario vive en esta zona. "
    "70 BPM. La tónica de llegada es la 2ª cuerda traste 10."))

S.append(ejercicio("47-ter", "En el estilo de Clapton — el bend largo, en la misma caja", (
    "Misma caja 3 que el 47, pero con otra firma: en vez de insistir con una celda, Clapton se queda "
    "en <b>una sola nota estirada, sostenida con vibrato ancho</b>. Es la tercera cara de la escuela "
    "británica — Page repite motivos, Angus también, Clapton canta con un bending que no se apura.<br/><br/>"
    "<i>Nota: éste es compuesto en el estilo de Clapton, no una transcripción — a diferencia del "
    "35-bis y el 47-bis, todavía no hay una cita real verificada de él en el cuadernillo.</i>"),
    "e47ter", W,
    "El bending dura lo que dure tu aire si lo cantaras: no lo cortes antes de tiempo."))

S.append(ejercicio(48, "La zona grave: la caja 5 (trastes 2 a 5)", (
    "El otro extremo del mástil, y el que casi nadie usa. Acá abajo la pentatónica <b>deja de sonar a solo "
    "y empieza a sonar a riff</b>: es la zona de Angus y de Chuck Berry. Fijate el peso de cada nota — la "
    "misma escala, tocada en las cuerdas gruesas, pega distinto: no susurra, empuja. Cerrás en el LA de la "
    "6ª cuerda traste 5, la tónica más grave que tenés en el mástil."),
    "e48", W,
    "60 BPM, con los ligados marcados. Después improvisá 5 minutos SOLO acá abajo: "
    "es incómodo al principio y es justamente lo que hay que entrenar."))

S.append(ejercicio(49, "La arquitectura: las 4 frases de un solo", (
    "Un solo no es una lista de licks: es una <b>curva</b>. Presenta (grave y simple, en la caja 1), "
    "desarrolla (la misma idea <b>mudada a la caja 2</b>), clímax (subís a la caja 3, lo más agudo y lo más "
    "fuerte), cierra (bajás por el mástil y resolvés abajo). Ocho compases que son el molde de casi cualquier "
    "solo que te haya gustado en tu vida. <b>Fijate que cada frase vive en una caja distinta:</b> no es "
    "decoración, es lo que hace que la curva se escuche. Aprendételo de memoria: es el plano.<br/><br/>"
    "<b>La regla de Brian May, que acá se aplica sin nombrarla:</b> el crecimiento tiene que ser en DOS "
    "variables a la vez, no solo una. <b>Altura</b> — empezás en un registro medio y subís — y <b>velocidad</b> "
    "— arrancás lento y melódico, y te guardás las notas rápidas para el clímax. Si solo subís de altura pero "
    "tocás siempre al mismo ritmo, la curva se nota menos. Las dos variables juntas son las que hacen que un "
    "solo se sienta que va a algún lado.<br/><br/>"
    "<b>Y hay una tercera, que casi nadie cuenta: el silencio.</b> No sólo crecen la altura y la velocidad — "
    "también <b>baja la cantidad de aire</b>. Presentá con mucho espacio entre frase y frase (dos, tres "
    "tiempos de silencio, sin miedo), acortá esos huecos en el desarrollo, y para el clímax que casi no "
    "queden. El oyente no escucha el silencio que sacaste, pero <b>siente que el solo se está apretando</b>. "
    "Es la variable más barata de las tres —no requiere tocar mejor, requiere tocar menos al principio— y es "
    "la que más separa un solo que crece de uno que simplemente sube."),
    "e49", W, "Con backing. Fijate en las dinámicas escritas: la curva es tanto de VOLUMEN como de altura."))

# ============================================================ SEMANA 12
S.append(PageBreak())
S.append(banner(12, "TU SOLO — el trofeo",
                "Objetivo: dejar de tocar ejercicios y grabar una pieza de música que sea tuya.", W))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "Última semana. No hay técnica nueva: hay una decisión. Vas a armar <b>un solo propio</b> sobre el molde "
    "de cuatro frases, con tu vocabulario, y lo vas a grabar. No tiene que ser difícil — tiene que ser "
    "<b>tuyo y estar terminado</b>. Un solo simple y bien cerrado le gana a uno ambicioso y a medio hacer.", BODY))

S.append(ejercicio(50, "El esqueleto (completalo vos)", (
    "Están escritas las <b>llegadas</b> de cada frase y el lugar del bending; falta lo que va en el medio. "
    "Eso lo ponés vos, con tu vocabulario. Es un ejercicio de escritura, no de lectura: agarrá lápiz y "
    "anotá tus frases en los compases vacíos.<br/><br/>"
    "<b>Mirá dónde caen las cuatro llegadas:</b> caja 1 (traste 7), caja 2 (traste 10), caja 3 (traste 12) "
    "y caja 5 (bajás al traste 3 y cerrás en el 5). Está hecho a propósito y "
    "no es negociable — <b>no vas a poder conectarlas sin recorrer el mástil</b>. Ese recorrido es el solo. "
    "Si te sale escribir las cuatro frases sin moverte de la caja 1, volvé al ejercicio 46: algo del mapa "
    "todavía no está."),
    "e50", W, "Empezá tarareando el solo entero antes de tocar una nota. Si lo podés cantar, lo podés tocar."))

S.append(ejercicio(51, "Los tres finales posibles", (
    "Tres formas de terminar: a la tónica suave (el más seguro y el que casi siempre funciona), un bending "
    "largo que se apaga (el más dramático), o una doble cuerda que queda sonando (el más rockero). "
    "Fijate que <b>cada uno está escrito en una caja distinta</b> — caja 1 (trastes 5-7), caja 3 (traste 12) "
    "y caja 4 (traste 15): un final no "
    "depende de la posición, depende del gesto. Podés cerrar donde te agarre el último compás. "
    "Probá los tres con tu solo y elegí uno. <b>Un solo sin final decidido suena a que te quedaste sin ideas.</b>"),
    "e51", W, "Con backing. El final se ensaya tanto como el principio."))

S.append(ejercicio(52, "El motivo que vuelve (esto tiene nombre: leitmotiv)", (
    "El truco que hace que un solo suene <b>compuesto</b> y no improvisado a la deriva: presentás una idea al "
    "principio, la dejás ir, y la traés de vuelta al final. El oído la reconoce y siente que el solo cerró — "
    "aunque no sepa por qué. Es gratis y casi nadie lo usa.<br/><br/>"
    "No es un truco casero: es un recurso con nombre — <b>leitmotiv</b> — prestado de la música clásica y "
    "del cine, donde un personaje tiene su melodía y vuelve cada vez que aparece. En la guitarra funciona "
    "igual: Frusciante lo usa todo el tiempo, y es buena parte de por qué sus solos se te quedan pegados "
    "aunque no sepas por qué. Empieza con una idea simple, cantable, y la repite o la varía. Es exactamente "
    "lo que hiciste vos en este ejercicio. <i>(Éste sí va en la misma caja las dos veces, y es la única vez "
    "que te lo voy a pedir: el motivo tiene que sonar IGUAL para que se reconozca.)</i><br/><br/>"
    "Fijate <b>cuál</b> caja: la 3, y el motivo es la misma celda del ejercicio 47. Que tenga que repetirse "
    "idéntico no significa que tenga que vivir en la caja 1 — significa que las dos veces caiga en el mismo "
    "lugar. Elegí el que quieras: lo único que no se negocia es que la vuelta suene igual que la ida."),
    "e52", W, "Metelo en tu solo: que la frase 1 y la frase 4 compartan algo."))

# el solo final va entero en una pagina: el encabezado no se separa de la partitura
S.append(KeepTogether([
    Paragraph("EJERCICIO 53 — EL SOLO FINAL (el trofeo del programa)", H2),
    Paragraph(
        "Doce compases que usan <b>los tres hitos</b>: se mueve por las cajas (Hito 1), cada nota tiene bending, "
        "vibrato, ligados y dinámica (Hito 2), y está armado con vocabulario de las dos escuelas sobre el molde "
        "de cuatro frases, con el motivo que vuelve al final (Hito 3).", BODY),
    Paragraph(
        "<b>El recorrido:</b> presenta en la <b>caja 5</b> — la zona grave, abajo de todo —, desarrolla subiendo "
        "a la caja 2, mete el motivo británico en la 3, trepa a la 4 en el clímax, bendea de vuelta en la 3 y "
        "cierra bajando otra vez a la 5. Seis cambios de zona en doce compases, y ninguno es gratuito: "
        "cada uno cae donde la frase lo pide.", BODY),
    Paragraph(
        "<b>Y fijate que no arranca en la caja 1.</b> Es a propósito, y es la decisión más importante de toda "
        "la página: éste es el video que vas a mostrar como prueba de tres meses de trabajo. La frase de "
        "apertura tiene que ser grave y simple — pero grave no quiere decir caja 1, quiere decir <i>abajo</i>, "
        "y la caja 5 está más abajo todavía. Abrir ahí prueba la promesa del programa en el primer segundo, "
        "en vez de contradecirla. Además el solo abre y cierra en la misma zona: <b>vuelve a casa</b>. "
        "Los ejercicios 49 y 50 abren en la caja 1 y éste en la 5 — no es un error: es la prueba de que "
        "la arquitectura es <b>portátil</b>. El molde es \"grave, desarrollo, clímax, cierre\"; dónde "
        "apoyás cada escalón lo elegís vos.", BODY),
    Paragraph(
        "Estudialo, tocalo, y después <b>usalo como modelo para el tuyo</b>. La consigna del entregable no es "
        "tocar éste: es que grabes uno propio con esta misma arquitectura.", BODY),
    Spacer(1, 2),
    score("e53", W),
    Spacer(1, 4),
    Paragraph(
        "Compás 10: silencio completo, justo después del bending más importante. Es el aire antes del cierre — "
        "sin ese compás vacío, la vuelta del motivo no emocionaría.", SMALL),
]))

# ============================================================ BANCO DE LICKS
S.append(PageBreak())
S.append(Paragraph("TU BANCO DE LICKS", H1))
S.append(Paragraph(
    "Acá vas anotando lo que te robás. La regla es la que importa: <b>no anotes solo las notas — anotá qué "
    "le robaste</b>. \"Bending que espera dos tiempos antes de subir\", \"motivo de 3 notas repetido\", "
    "\"termina en la tónica pero una octava abajo\". Las notas se olvidan; los mecanismos se usan toda la vida.", BODY))
S.append(Paragraph(
    "Meta del mes: <b>8 licks</b> que hayan pasado los 5 pasos. No 50 guardados: 8 apropiados. "
    "Imprimí esta página las veces que necesites.", SMALL))
S.append(Spacer(1, 6))
S.append(TablaturaEnBlanco(W, sistemas=7, compases=2))

# ============================================================ CIERRE
S.append(PageBreak())
S.append(Paragraph("¿CERRASTE EL HITO 3? (checklist honesto)", H1))
S.append(tabla([
    [Paragraph("", CELLB), Paragraph("<b>Lo puedo hacer</b>", CELLB), Paragraph("<b>Cómo lo compruebo</b>", CELLB)],
    [Paragraph(CAJ, CELL), Paragraph("Saqué al menos un lick de oído, sin TAB", CELL),
     Paragraph("Lo toco igual que el disco y puedo decir de qué tema salió.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Toco los licks de las dos escuelas", CELL),
     Paragraph("Hago el ejercicio 38 y el 42 y se escuchan claramente distintos.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Reconozco de oído en qué grado caí", CELL),
     Paragraph("Improvisando freno en una nota y sé si es tónica, 4ª o 7ª sin buscarla en el mástil.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Sé variar un lick de 3 formas", CELL),
     Paragraph("Agarro cualquier frase y le cambio ritmo, remate y caja sin pensarlo.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Muevo un lick a otra caja sin perderme", CELL),
     Paragraph("Toco el ejercicio 46 entero, las 5 cajas seguidas, sin frenar entre una y otra.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("<b>Toco licks reales fuera de la caja 1</b>", CELL),
     Paragraph("Los ejercicios 47 (caja 3) y 48 (caja 5) me salen de memoria, sin buscar los trastes.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Entiendo la curva de un solo", CELL),
     Paragraph("Escucho un solo y puedo señalar dónde presenta, desarrolla, climax y cierra.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("<b>Mi solo recorre el mástil</b>", CELL),
     Paragraph("Puedo decir en qué caja está cada una de mis 4 frases, y no son todas la misma.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Mi solo tiene un final decidido", CELL),
     Paragraph("Elegí uno de los tres finales del ejercicio 51 y lo ensayé aparte.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Tengo 8 licks en el banco, apropiados", CELL),
     Paragraph("Los 8 pasaron los 5 pasos, y al menos uno me salió solo improvisando.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("<b>Grabé mi solo de 1 minuto</b>", CELL),
     Paragraph("El video existe. Es el entregable del programa entero.", CELL)],
], [0.9 * cm, 6.3 * cm, W - 7.2 * cm]))

S.append(Paragraph("EL SOLO FINAL: LA CONSIGNA COMPLETA", H2))
S.append(tabla([
    [Paragraph("<b>Requisito</b>", CELLB), Paragraph("<b>Detalle</b>", CELLB)],
    [Paragraph("Duración", CELL), Paragraph("1 minuto aproximado, sobre el backing en La menor.", CELL)],
    [Paragraph("Arquitectura", CELL), Paragraph("Las 4 frases: presenta, desarrolla, clímax, cierra.", CELL)],
    [Paragraph("Territorio", CELL), Paragraph("Que se mueva por al menos 3 cajas. No puede vivir en la caja 1.", CELL)],
    [Paragraph("Sabor", CELL), Paragraph("Mínimo: 2 bendings afinados, vibrato en las notas largas, un silencio de "
                                         "más de 2 tiempos.", CELL)],
    [Paragraph("Vocabulario", CELL), Paragraph("Al menos 2 licks de tu banco, variados (no calcados).", CELL)],
    [Paragraph("Final", CELL), Paragraph("Decidido y ensayado, y sabiendo en qué grado cerrás. Nada de apagarse porque se acabó el backing.", CELL)],
    [Paragraph("Bonus", CELL), Paragraph("Que el motivo del principio vuelva sobre el final.", CELL)],
], [3.0 * cm, W - 3.0 * cm]))
S.append(Paragraph(
    "<b>Una aclaración que parece obvia y no lo es:</b> tu entregable NO es el ejercicio 53 tocado de "
    "memoria. Podés compartir su arquitectura (las 4 frases, dónde cae cada una) porque para eso está "
    "como modelo — pero las notas, los licks y el remate tienen que ser los tuyos, los que armaste en "
    "el ejercicio 50 y variaste después. Si tu solo se puede confundir nota por nota con el 53, no está "
    "terminado: copiaste el mapa, no hiciste el viaje.", SMALL))

S.append(Paragraph("PLANILLA DE PRÁCTICA", H2))
dias = ["L", "M", "X", "J", "V", "S", "D"]
rows = [[Paragraph("<b>Semana</b>", CELLB)] + [Paragraph("<b>%s</b>" % d, CELLB) for d in dias] +
        [Paragraph("<b>Licks al banco</b>", CELLB)]]
for nombre in ["9 · Escuela británica", "10 · Escuela americana", "11 · Variaciones", "12 · Tu solo"]:
    rows.append([Paragraph(nombre, CELL)] + [Paragraph(CAJ, CELL) for _ in dias] + [Paragraph("", CELL)])
t = tabla(rows, [3.8 * cm] + [0.85 * cm] * 7 + [W - 3.8 * cm - 0.85 * cm * 7])
t.setStyle(TableStyle([('ALIGN', (1, 0), (7, -1), 'CENTER')]))
S.append(t)

# ============================================================ PÁGINA DE CIERRE
S.append(PageBreak())
S.append(Paragraph("TERMINASTE EL PROGRAMA", H1))
S.append(Paragraph(
    "Hace tres meses vivías en la caja 1, repetías los mismos cuatro licks y tus solos sonaban a escala. "
    "Mirá lo que juntaste:", BODY))
S.append(Spacer(1, 2))
S.append(tabla([
    [Paragraph("<b>Hito</b>", CELLB), Paragraph("<b>Lo que te dio</b>", CELLB),
     Paragraph("<b>Cómo se nota cuando tocás</b>", CELLB)],
    [Paragraph("<b>1 · EL MAPA</b>", CELLB),
     Paragraph("El territorio: las 5 cajas conectadas.", CELL),
     Paragraph("Te movés por todo el mástil sin frenar ni pensar dónde estás parado.", CELL)],
    [Paragraph("<b>2 · EL SABOR</b>", CELLB),
     Paragraph("La voz: ligados, bending, vibrato, espacio y dinámica.", CELL),
     Paragraph("Cada nota tiene algo tuyo. Una sola nota tuya ya se reconoce.", CELL)],
    [Paragraph("<b>3 · EL VOCABULARIO</b>", CELLB),
     Paragraph("Qué decir: tu banco de licks y la arquitectura del solo.", CELL),
     Paragraph("Improvisás con ideas, no con dedos. Tus solos tienen principio y final.", CELL)],
], [3.2 * cm, 5.4 * cm, W - 8.6 * cm]))

S.append(Paragraph("GUARDÁ EL VIDEO", H2))
S.append(Paragraph(
    "Ese solo de un minuto es la prueba de tres meses de trabajo. Guardalo bien: dentro de un año va a ser "
    "el <b>\"antes\"</b> de la próxima etapa, igual que el audio del día 1 del Hito 2 fue el antes de éste. "
    "Es la única forma honesta de medir el progreso en música — el oído propio siempre miente.", BODY))

S.append(Paragraph("Y AHORA, ¿QUÉ?", H2))
S.append(Paragraph(
    "Lo que sigue no es más información: es <b>kilometraje</b>. Tres cosas, en orden de importancia:", BODY))
S.append(tabla([
    [Paragraph("<b>1</b>", CELLB), Paragraph("<b>Tocá con gente</b>", CELL),
     Paragraph("Nada de lo que aprendiste termina de asentarse hasta que lo usás con una banda atrás. "
               "Zapadas, jams, un amigo con un bajo. Lo que sea, pero con otro.", CELL)],
    [Paragraph("<b>2</b>", CELLB), Paragraph("<b>Seguí sacando de oído</b>", CELL),
     Paragraph("El hábito del Hito 3 no vence: un lick por semana, sacado sin TAB, y tu vocabulario "
               "no para de crecer solo.", CELL)],
    [Paragraph("<b>3</b>", CELLB), Paragraph("<b>Mudá la pentatónica</b>", CELL),
     Paragraph("Todo el programa fue en La menor a propósito. Ahora movelo: Mi, Sol, Re. Es el mismo mapa "
               "corrido de lugar — vas a tardar mucho menos de lo que pensás.", CELL)],
], [0.8 * cm, 4.0 * cm, W - 4.8 * cm]))

S.append(Paragraph("LO QUE ESTE PROGRAMA NO TE DIO (y lo digo de frente)", H2))
S.append(Paragraph(
    "Doce semanas alcanzan para el mapa, el sabor y el vocabulario. No alcanzan para todo, y preferimos "
    "que lo sepas por acá antes de que lo descubras tocando con gente. Faltan dos cosas, a propósito:", BODY))
S.append(tabla([
    [Paragraph("<b>EL RITMO</b>", CELLB),
     Paragraph("Trabajamos <b>qué</b> notas tocás y <b>cómo</b> las tocás, pero casi no trabajamos "
               "<b>cuándo</b> entran respecto del pulso. Buena parte de lo que hace que un lick suene a "
               "Page es dónde cae, no qué notas tiene. Subdivisión, shuffle contra recto, entrar a "
               "contratiempo: eso es un módulo aparte.", CELL)],
    [Paragraph("<b>LOS CAMBIOS DE ACORDE</b>", CELLB),
     Paragraph("Los tres hitos improvisan sobre un vamp fijo en La menor. Eso es a propósito: aísla la "
               "variable para que puedas concentrarte en el mástil y en el sabor. Pero un blues de 12 "
               "compases se mueve, y ahí hay que saber qué hacer cuando el acorde cambia debajo tuyo.", CELL)],
], [4.2 * cm, W - 4.2 * cm]))
S.append(Paragraph(
    "Nada de esto invalida lo que hiciste: son el escalón siguiente, no un agujero. Si al tocar con gente "
    "sentís que \"algo no encaja\" aunque las notas estén bien, casi seguro es una de estas dos.", SMALL))

S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10.5"><b>Mandame tu solo final.</b></font><br/>'
    '<font color="#f7d7d2" size="9">Lo escucho entero y te mando una devolución grabada, no un "está muy bueno". '
    'Y si te copás, lo subimos: tu antes/después es la mejor prueba de que esto funciona. · %s</font>' % IG, W))

doc.build(S)
print("OK Cuadernillo-Hito3-El-Vocabulario-EJERCICIOS.pdf")
