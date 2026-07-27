# -*- coding: utf-8 -*-
"""Arma el PDF del Cuadernillo HITO 3 — EL VOCABULARIO.

Requiere que antes se haya corrido `gen_scores_h3.py` (genera ./partituras/e33..e48).
"""
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Spacer, PageBreak, TableStyle, KeepTogether

from cuadernillo_comun import (H1, H2, BODY, SMALL, CELL, CELLB, CAJ, IG,
                               documento, tabla, banner, par, caja_oscura,
                               ejercicio, score, TablaturaEnBlanco)

doc = documento("Cuadernillo-Hito3-El-Vocabulario-EJERCICIOS.pdf",
                "HITO 3 — EL VOCABULARIO",
                "Robar licks con honestidad, armar tu solo · ejercicios con TAB y partitura",
                "Solo con Sabor · Hito 3 — El Vocabulario",
                "Hito 3 - El Vocabulario (ejercicios)")
W = doc.width
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
     Paragraph("Le cambiás el ritmo, el remate y la caja. Tres versiones distintas mínimo (ej. 41, 42, 43).", CELL),
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
    "Los licks que vas a encontrar acá <b>no son transcripciones</b> de solos de nadie: son frases originales "
    "escritas <i>en el estilo de</i> cada escuela. Es a propósito, y es exactamente el punto del hito. "
    "Lo que se enseña acá no son las notas de Page — es el <b>mecanismo</b> que hace que las frases de Page "
    "funcionen. Ese mecanismo no tiene dueño, y es lo único que te sirve para inventar lo tuyo.", BODY))

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

S.append(ejercicio(33, "El motivo que se repite", (
    "Una celda de tres notas, machacada cinco veces, y recién en la sexta resolvés. Vas a sentir que "
    "<b>estás repitiendo demasiado</b> — esa sensación es la trampa: desde adentro siempre parece más "
    "repetido de lo que se escucha desde afuera. Grabate y vas a ver que suena convincente, no monótono."),
    "e33", W, "60 BPM en tresillos. El pull-off va en la 1ª cuerda (8 al 5); el Sol de la 2ª se puntea."))

S.append(ejercicio(34, "Dobles cuerdas", (
    "Dos notas juntas, con la púa barriendo las dos cuerdas de una. Es el sonido de Chuck Berry y de medio "
    "AC/DC: suena más grande que una nota sola sin necesidad de tocar más rápido. Cuidá que las dos suenen "
    "parejas — si una se escucha más, estás inclinando la púa."),
    "e34", W, "70 BPM. Apagá con la mano derecha las cuerdas que no usás: si zumba algo, se arruina."))

S.append(ejercicio(35, "El unísono (dos cuerdas, la misma nota)", (
    "El recurso más impactante de la escuela británica. Tocás dos cuerdas juntas y <b>bendeás la de abajo "
    "hasta que suene exactamente igual que la de arriba</b>. Cuando están afinadas, las dos notas se pelean "
    "y producen un batido que suena enorme. Cuando no, suena horrible — no hay término medio, y por eso "
    "es el mejor test de afinación de bending que existe."),
    "e35", W, "Lento, sin metrónomo. Escuchá el batido: cuando desaparece, llegaste."))

S.append(ejercicio(36, "Los tres recursos encadenados", (
    "Motivo repetido, dobles cuerdas y unísono en una sola frase. Fijate cuántas notas distintas usaste: "
    "casi ninguna. Toda la fuerza vino del <b>tratamiento</b>, no del material."),
    "e36", W, "Con backing. Tocalo como si estuvieras enojado: esta escuela pide convicción, no delicadeza."))

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

S.append(ejercicio(37, "La frase vocal (escuela Gary Moore)", (
    "Tres compases y apenas un puñado de notas. La estructura es la de una frase hablada: una entrada que "
    "<b>hace esperar</b>, un bending largo que es el momento importante, y una bajada que resuelve. "
    "Lo difícil acá no es tocarlo: es aguantar los silencios sin rellenarlos."),
    "e37", W, "Con backing lento. Cantala antes de tocarla, aunque desafines."))

S.append(ejercicio(38, "La línea fluida (escuela Slash)", (
    "Casi todo ligado: en dos compases puntéas tres o cuatro veces nada más. El resultado es una línea que "
    "<b>se derrama</b> por el mástil en vez de marcar cada nota. Empezá lento — si acelerás antes de tiempo, "
    "los ligados se apagan y queda un murmullo."),
    "e38", W, "60 BPM y subís. Que las notas ligadas suenen igual de fuerte que las punteadas."))

S.append(ejercicio(39, "Dobles cuerdas con ligado (remate estilo Hendrix)", (
    "Dobles cuerdas otra vez, pero acá el hammer-on va <b>en la cuerda de abajo mientras la de arriba se "
    "sostiene</b>. Ese movimiento es la marca registrada de Hendrix y de todo el R&B. Es más difícil de lo "
    "que parece: el dedo que golpea tiene que ser preciso para no apagar la otra cuerda."),
    "e39", W, "Lento. Si la nota de arriba se corta cuando hacés el hammer, tocás con demasiada fuerza."))

S.append(ejercicio(40, "Los tres recursos encadenados", (
    "La línea fluida, la doble cuerda con ligado y el bending largo en una sola frase. Compará esta página "
    "con el ejercicio 36: <b>la misma escala, el mismo mástil, dos idiomas distintos</b>."),
    "e40", W, "Con backing. Tocalo relajado, casi perezoso. Esta escuela pide calma, no convicción."))

# ============================================================ SEMANA 11
S.append(PageBreak())
S.append(banner(11, "HACERLO TUYO — las 3 variaciones y la arquitectura",
                "Objetivo: que un lick prestado deje de sonar prestado, y entender cómo se arma un solo entero.", W))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "Esta es la semana que separa a quien colecciona licks de quien improvisa. La operación es siempre la "
    "misma: agarrás una frase y le cambiás <b>una sola cosa por vez</b> — el ritmo, el remate, o el lugar "
    "del mástil. Con tres variaciones, un lick robado ya es material tuyo: nadie puede señalar de dónde salió.", BODY))

S.append(ejercicio(41, "Mismas notas, tres ritmos distintos", (
    "Las mismas seis notas escritas tres veces, con tres ritmos: parejo, acelerando, y a contratiempo. "
    "Escuchá los tres seguidos: <b>suenan a tres licks distintos</b>, y no cambiaste ni una nota. "
    "El ritmo es el 70% de la identidad de una frase, y es lo primero que hay que tocar."),
    "e41", W, "70 BPM. El tercero (a contratiempo) es el más difícil: contá en voz alta si hace falta."))

S.append(ejercicio(42, "Mismo arranque, tres remates", (
    "La frase entra igual las tres veces y termina distinto: colgada, en la tónica, o para arriba. "
    "El remate es lo que el oído se lleva — <b>cambiar el final cambia el significado de todo lo anterior</b>, "
    "igual que en una oración."),
    "e42", W, "Con backing. Fijate cuál te pide seguir tocando y cuál te deja tranquilo."))

S.append(ejercicio(43, "El mismo lick, mudado de caja", (
    "Idéntica frase, tocada en las cajas 1, 2 y 3. Acá se paga el trabajo del Hito 1: si el mapa está, esto "
    "sale casi solo. En cada caja el lick <b>cambia de carácter</b> — más grave suena más pesado, más agudo "
    "suena más urgente — aunque sean las mismas notas."),
    "e43", W, "Lento. Después probalo en las cajas 4 y 5 sin que esté escrito: ése es el verdadero examen."))

S.append(ejercicio(44, "La arquitectura: las 4 frases de un solo", (
    "Un solo no es una lista de licks: es una <b>curva</b>. Presenta (grave y simple), desarrolla (la misma "
    "idea más arriba), clímax (lo más agudo y lo más fuerte), cierra (bajás y resolvés). Ocho compases que "
    "son el molde de casi cualquier solo que te haya gustado en tu vida. Aprendételo de memoria: es el plano."),
    "e44", W, "Con backing. Fijate en las dinámicas escritas: la curva es tanto de VOLUMEN como de altura."))

# ============================================================ SEMANA 12
S.append(PageBreak())
S.append(banner(12, "TU SOLO — el trofeo",
                "Objetivo: dejar de tocar ejercicios y grabar una pieza de música que sea tuya.", W))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "Última semana. No hay técnica nueva: hay una decisión. Vas a armar <b>un solo propio</b> sobre el molde "
    "de cuatro frases, con tu vocabulario, y lo vas a grabar. No tiene que ser difícil — tiene que ser "
    "<b>tuyo y estar terminado</b>. Un solo simple y bien cerrado le gana a uno ambicioso y a medio hacer.", BODY))

S.append(ejercicio(45, "El esqueleto (completalo vos)", (
    "Están escritas las <b>llegadas</b> de cada frase y el lugar del bending; falta lo que va en el medio. "
    "Eso lo ponés vos, con tu vocabulario. Es un ejercicio de escritura, no de lectura: agarrá lápiz y "
    "anotá tus frases en los compases vacíos."),
    "e45", W, "Empezá tarareando el solo entero antes de tocar una nota. Si lo podés cantar, lo podés tocar."))

S.append(ejercicio(46, "Los tres finales posibles", (
    "Tres formas de terminar: a la tónica suave (el más seguro y el que casi siempre funciona), un bending "
    "largo que se apaga (el más dramático), o una doble cuerda que queda sonando (el más rockero). "
    "Probá los tres con tu solo y elegí uno. <b>Un solo sin final decidido suena a que te quedaste sin ideas.</b>"),
    "e46", W, "Con backing. El final se ensaya tanto como el principio."))

S.append(ejercicio(47, "El motivo que vuelve", (
    "El truco que hace que un solo suene <b>compuesto</b> y no improvisado a la deriva: presentás una idea al "
    "principio, la dejás ir, y la traés de vuelta al final. El oído la reconoce y siente que el solo cerró — "
    "aunque no sepa por qué. Es gratis y casi nadie lo usa."),
    "e47", W, "Metelo en tu solo: que la frase 1 y la frase 4 compartan algo."))

# el solo final va entero en una pagina: el encabezado no se separa de la partitura
S.append(KeepTogether([
    Paragraph("EJERCICIO 48 — EL SOLO FINAL (el trofeo del programa)", H2),
    Paragraph(
        "Doce compases que usan <b>los tres hitos</b>: se mueve por las cajas (Hito 1), cada nota tiene bending, "
        "vibrato, ligados y dinámica (Hito 2), y está armado con vocabulario de las dos escuelas sobre el molde "
        "de cuatro frases, con el motivo que vuelve al final (Hito 3).", BODY),
    Paragraph(
        "Estudialo, tocalo, y después <b>usalo como modelo para el tuyo</b>. La consigna del entregable no es "
        "tocar éste: es que grabes uno propio con esta misma arquitectura.", BODY),
    Spacer(1, 2),
    score("e48", W),
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
     Paragraph("Hago el ejercicio 36 y el 40 y se escuchan claramente distintos.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Sé variar un lick de 3 formas", CELL),
     Paragraph("Agarro cualquier frase y le cambio ritmo, remate y caja sin pensarlo.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Muevo un lick a otra caja sin perderme", CELL),
     Paragraph("El ejercicio 43 me sale también en las cajas 4 y 5, que no están escritas.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Entiendo la curva de un solo", CELL),
     Paragraph("Escucho un solo y puedo señalar dónde presenta, desarrolla, climax y cierra.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Mi solo tiene un final decidido", CELL),
     Paragraph("Elegí uno de los tres finales del ejercicio 46 y lo ensayé aparte.", CELL)],
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
    [Paragraph("Final", CELL), Paragraph("Decidido y ensayado. Nada de apagarse porque se acabó el backing.", CELL)],
    [Paragraph("Bonus", CELL), Paragraph("Que el motivo del principio vuelva sobre el final.", CELL)],
], [3.0 * cm, W - 3.0 * cm]))

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

S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10.5"><b>Mandame tu solo final.</b></font><br/>'
    '<font color="#f7d7d2" size="9">Lo escucho entero y te mando una devolución grabada, no un "está muy bueno". '
    'Y si te copás, lo subimos: tu antes/después es la mejor prueba de que esto funciona. · %s</font>' % IG, W))

doc.build(S)
print("OK Cuadernillo-Hito3-El-Vocabulario-EJERCICIOS.pdf")
