# -*- coding: utf-8 -*-
"""Arma el PDF del ANEXO DE RITMO — el árbol, las 3 velocidades y la síncopa.

Requiere que antes se haya corrido `gen_scores_ritmo.py` (genera ./partituras/r01..r10).

Este anexo NO es un hito nuevo: corre en paralelo al Hito 3. Por eso sus ejercicios
se numeran con letras (A a J) y no tocan la numeración corrida 1-59.

VA EN EL MES 3, NO EN EL 2, y el motivo no es de carga sino de dependencias:
  · su operación es "agarrá un lick que ya sabés y movelo", y los primeros licks del
    programa aparecen recién en la semana 6 (ej. 25-26). Al mes 3 el alumno llega con
    un banco; al mes 2, con dos.
  · cita el ej. 44 y el ej. 46, los dos del Hito 3. En el mes 2 serían referencias a
    material que el alumno todavía no vio.
  · el ej. 44 ("mismas notas, tres ritmos") es justamente lo que este anexo desarrolla:
    el 44 muestra tres ritmos terminados, el anexo entrega la palanca que los produce.
El módulo de ritmo basado en Pozzoli (que Feli produce aparte) se queda en el mes 2:
ése enseña a LEER ritmo, éste a APLICARLO. Un documento de ritmo por mes, en ese orden.

El dato que justifica que exista, contado expandiendo las duraciones heredadas de
LilyPond (en `c''8 a' g' e'` hay cuatro corcheas y un solo "8" escrito — contar los
tokens da 395 y es el error que tuvo la primera versión de esta tabla): son **995
notas**, corcheas 74% · negras 17% · blancas 5% · redondas 3% · **2 semicorcheas** ·
cero fusas. El alumno termina el programa con un vocabulario rítmico de dos figuras.

Y de los 217 compases, 165 arrancan justo en el 1 y solo 16 a contratiempo (7%); los
5 puntillos del programa son todos notas finales sostenidas, ninguno una figura
rítmica adentro de una frase. Ese segundo dato es el que justifica el bloque de síncopa.
"""
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Spacer, KeepTogether

from cuadernillo_comun import (H1, H2, H3, BODY, SMALL, CELL, CELLB, CAJ,
                               ArbolFiguras, GrillaDelCompas, documento, tabla,
                               caja_oscura, score)

doc = documento("Anexo-Ritmo-El-Arbol-y-las-3-Velocidades.pdf",
                "ANEXO DE RITMO",
                "El árbol de las figuras · el mismo lick en 4, 2 o 1 pulso · tresillo, swing,\n                 síncopa, desplazamiento y llamada-respuesta",
                "Solo con Sabor · Anexo de ritmo (va con el Hito 3)",
                "Anexo de ritmo - El arbol y las 3 velocidades")
W = doc.width
S = []


def ej(letra, titulo, bajada, name, meta=None):
    els = [Paragraph("EJERCICIO %s — %s" % (letra, titulo), H3),
           Paragraph(bajada, BODY)]
    if meta:
        els.append(Paragraph(meta, SMALL))
    els += [Spacer(1, 2), score(name, W), Spacer(1, 6)]
    return KeepTogether(els)


# ============================================================ 1. POR QUÉ EXISTE
S.append(Paragraph("POR QUÉ ESTE ANEXO EXISTE", H2))
S.append(Paragraph(
    "Conté todas las notas de los tres hitos y del bonus. Son <b>995</b>, y se reparten así:", BODY))
S.append(tabla([
    [Paragraph("<b>Figura</b>", CELLB), Paragraph("<b>Corchea</b>", CELLB), Paragraph("<b>Negra</b>", CELLB),
     Paragraph("<b>Blanca</b>", CELLB), Paragraph("<b>Redonda</b>", CELLB), Paragraph("<b>Semicorchea</b>", CELLB),
     Paragraph("<b>Fusa</b>", CELLB)],
    [Paragraph("<b>Cuánto</b>", CELLB), Paragraph("74%", CELL), Paragraph("17%", CELL),
     Paragraph("5%", CELL), Paragraph("3%", CELL),
     Paragraph("<b>2 en total</b>", CELL), Paragraph("<b>ninguna</b>", CELL)],
], [W * 0.16] + [W * 0.14] * 6))
S.append(Spacer(1, 7))
S.append(Paragraph(
    "O sea: aprendiste <b>dónde</b> están las notas (Hito 1) y <b>cómo</b> atacarlas (Hito 2), pero durante "
    "todo el programa las tocaste con dos figuras: tres de cada cuatro notas son corcheas. Dos "
    "semicorcheas en casi mil notas. Eso no está mal — se "
    "hizo a propósito, porque meter ritmo nuevo mientras aprendés a afinar un bending es pedirte dos cosas a "
    "la vez. Pero si no lo cerramos, te queda un solo que suena parejo: todas las frases con la misma "
    "densidad, como si hablaras siempre a la misma velocidad.", BODY))
S.append(Paragraph(
    "Este anexo no te da <b>ni una nota nueva</b>. Te da lo que hacés con las que ya tenés.", BODY))

# ============================================================ 2. EL ÁRBOL
S.append(Spacer(1, 6))
S.append(Paragraph("EL ÁRBOL DE LAS FIGURAS", H2))
S.append(Paragraph(
    "Todas las figuras salen de partir la de arriba por la mitad. No hay que memorizar cuánto dura cada una: "
    "hay que ver de dónde sale.", BODY))
S.append(Spacer(1, 4))
S.append(ArbolFiguras(W))
S.append(Spacer(1, 4))
S.append(caja_oscura(
    '<font color="white"><b>Lo único que hay que sacar de este dibujo:</b> las cinco filas duran '
    '<b>exactamente lo mismo</b>. Un compás entero, las cinco. Lo que cambia no es cuánto tiempo ocupan — '
    'es en cuántos pedazos lo partís. Bajar un escalón no es "tocar más rápido": es partir la figura al '
    'medio.</font>', W))
S.append(Spacer(1, 7))
S.append(Paragraph(
    "<b>Y una que sigue para abajo:</b> si partís la semicorchea al medio te da la <b>fusa</b> (32 por compás, "
    "un octavo de pulso). No la vas a necesitar para tocar rock — está acá para que veas que el árbol no se "
    "termina, sigue el mismo patrón todo lo que quieras.", BODY))

# ============================================================ 3. LAS 3 VELOCIDADES
S.append(Spacer(1, 10))
S.append(Paragraph("EL MISMO LICK EN 4, EN 2 Y EN 1 PULSO", H2))
S.append(Paragraph(
    "Acá está la parte que de verdad te cambia el solo. Agarrás un lick que ya sabés y lo metés en menos "
    "espacio. Esto tiene nombre — se llama <b>diminución</b> — y no es un ejercicio de velocidad. Es un "
    "ejercicio de <b>función</b>:", BODY))
S.append(Spacer(1, 3))
S.append(tabla([
    [Paragraph("<b>La misma idea, en…</b>", CELLB), Paragraph("<b>Qué es dentro del solo</b>", CELLB),
     Paragraph("<b>Cuándo la usás</b>", CELLB)],
    [Paragraph("<b>Negras</b> (4 pulsos)", CELLB),
     Paragraph("Una <b>frase</b>. Una afirmación. Se escucha entera y se entiende.", CELL),
     Paragraph("Cuando estás diciendo algo y querés que se entienda. Apertura y cierre del solo.", CELL)],
    [Paragraph("<b>Corcheas</b> (2 pulsos)", CELLB),
     Paragraph("Un <b>comentario</b>. Ya no es la idea principal: es algo que agregás.", CELL),
     Paragraph("En el medio, cuando el solo está creciendo y todavía no llegaste al clímax.", CELL)],
    [Paragraph("<b>Semicorcheas</b> (1 pulso)", CELLB),
     Paragraph("Un <b>adorno</b>. Un gesto. Pasa tan rápido que el oído lo siente, no lo analiza.", CELL),
     Paragraph("De remate, o para llenar un hueco sin cambiar de idea.", CELL)],
], [W * 0.24, W * 0.40, W * 0.36]))
S.append(Spacer(1, 7))
S.append(Paragraph(
    "Fijate que <b>no dice \"más rápido\" en ninguna fila</b>. Son tres cosas distintas, no la misma cosa a "
    "tres velocidades. Elegir cuál de las tres tocás en cada momento es, literalmente, componer.", BODY))
S.append(Spacer(1, 5))

S.append(ej("A", "Las 3 velocidades de la misma celda",
            "Mirá la tablatura: los cuatro números son <b>los mismos</b> en los tres compases (8-5-8-5, caja 1). "
            "Lo único que cambia es la figura. Tocalos seguidos, con metrónomo, sin parar entre compás y "
            "compás — el efecto está en escuchar los tres pegados.<br/><br/>"
            "<b>Los silencios están escritos a propósito.</b> No son relleno: son el ejercicio.",
            "r01",
            "Es el mismo truco del ejercicio 46 que ya hiciste este mes (un lick en las 5 cajas), pero en el "
            "otro eje. Aquel probaba que un lick no es un lugar. Éste prueba que tampoco es una velocidad."))

S.append(caja_oscura(
    '<font color="white"><b>LA REGLA QUE HACE QUE ESTO NO TE ARRUINE EL HITO 2</b><br/><br/>'
    'Comprimir un lick <b>no te ahorra tiempo: te regala silencio</b>. Si la frase entraba en 4 pulsos y '
    'ahora entra en 1, no ganaste velocidad — ganaste <b>3 pulsos de silencio</b> que antes no tenías.<br/><br/>'
    'Todo el Hito 2 te enseñó que el espacio es parte de la frase. Este anexo es la máquina de fabricar '
    'espacio. Si usás la compresión para meter <i>más</i> notas en el mismo lugar, te comiste el regalo y '
    'volviste a sonar atropellado. <b>Lo que hacés con esos 3 pulsos que quedaron libres es lo que decide '
    'si sonás a músico.</b></font>', W))

S.append(Spacer(1, 8))
S.append(Paragraph("Y ALGO QUE NADIE TE AVISA: AL COMPRIMIR, LA MANO DERECHA TIENE QUE CAMBIAR", H2))
S.append(Paragraph(
    "Tocá el ejercicio A tres veces y prestá atención a la mano de la púa, no a la izquierda. En negras "
    "picás las cuatro notas cómodo. En corcheas todavía llegás. En semicorcheas, si intentás picar las "
    "cuatro con la misma fuerza, <b>se te endurece la frase</b>: suena a máquina y se te tensa el "
    "antebrazo.", BODY))
S.append(Paragraph(
    "La salida no es tocar más rápido: es <b>picar menos</b>. A medida que la figura se achica, cada vez "
    "más notas se resuelven con los ligados que aprendiste en el Hito 2 — hammer-on, pull-off y slide — y "
    "la púa se reserva para la primera de cada grupo. Por eso los solos rápidos de verdad tienen "
    "<b>menos</b> ataques de púa que los lentos, no más.", BODY))
S.append(Paragraph(
    "Esto es también una tercera variable expresiva, además de la altura y la velocidad: <b>a medida que "
    "el solo crece, el ataque se vuelve más ligado</b>. No es sólo un recurso técnico para poder llegar — "
    "es parte de por qué un clímax suena a que se desborda en vez de sonar a que se apura. Volvé al "
    "ejercicio 19 del Hito 2 (una púa cada tres notas) con esto en la cabeza: ese ejercicio no era de "
    "velocidad, era de <b>economía de púa</b>, y recién ahora se entiende para qué era.", BODY))

# ============================================================ 4. EL TRESILLO
S.append(Spacer(1, 10))
S.append(Paragraph("EL TRESILLO — EL QUE NO ENTRA EN EL ÁRBOL", H2))
S.append(Paragraph(
    "El árbol parte todo <b>en dos</b>. El tresillo parte <b>en tres</b>, y por eso suena distinto a "
    "cualquier cosa del árbol: no es una figura más rápida, es otra forma de repartir el pulso. Tres notas "
    "donde el oído espera dos. Eso solo ya te cambia el color de la frase, sin tocar ni una nota nueva.", BODY))
S.append(Paragraph(
    "Ya lo usaste sin que te lo nombraran así: el <b>ejercicio 19 del Hito 2</b> (\"una púa cada 3 notas\") "
    "es esto mismo.", SMALL))
S.append(Spacer(1, 5))
S.append(ej("B", "Las mismas 6 notas, binario y atresillado",
            "Compás 1: seis corcheas, ocupan <b>3 pulsos</b>. Compás 2: las mismas seis notas en dos "
            "tresillos, ocupan <b>2 pulsos</b>. La tablatura es idéntica — 8-5-8-5-7-5.<br/><br/>"
            "Contá en voz alta mientras tocás: en el compás 1, <b>UN-o-DOS-o-TRES-o</b>. En el compás 2, "
            "<b>UN-o-a-DOS-o-a</b>. Si te cuesta, es la señal de que estaba faltando.",
            "r02"))

# ============================================================ 5. SWING
S.append(Spacer(1, 4))
S.append(Paragraph("RECTO Y SWING — ESTO ES OTRO EJE, NO OTRA FIGURA", H2))
S.append(Paragraph(
    "Acá viene la confusión más común, así que va separado del árbol a propósito. <b>El swing no es una "
    "figura.</b> Son las mismas corcheas de siempre; lo que cambia es <b>dónde cae la segunda</b>. En recto, "
    "las dos corcheas del pulso duran igual. En swing, la primera se estira y la segunda llega tarde: "
    "larga-corta, larga-corta.", BODY))
S.append(Paragraph(
    "El árbol te dice <b>qué figura</b> usás. El swing te dice <b>dónde cae dentro del pulso</b>. Son dos "
    "preguntas distintas y se pueden combinar: podés tocar corcheas rectas o corcheas con swing, y las dos "
    "siguen siendo corcheas.", BODY))
S.append(Spacer(1, 5))
S.append(ej("C", "La misma frase, recta y con swing",
            "En la partitura el swing está <b>escrito</b> (negra + corchea dentro de un tresillo) para que "
            "veas de dónde sale, pero en un chart de blues normalmente no se escribe: dice \"shuffle\" arriba "
            "y se toca así. Compás 1 recto, compás 2 swing, mismas notas.<br/><br/>"
            "<b>Prueba de oído:</b> grabate los dos compases y escuchalos sin mirar. Si no distinguís cuál "
            "es cuál, exagerá más el swing — casi siempre se hace de menos.",
            "r03",
            "Buena parte del blues-rock que te gusta está en swing, no en recto. Es una de las razones por "
            "las que un lick tuyo bien tocado igual no termina de sonar al disco."))

# ============================================================ 5-BIS. SÍNCOPA
S.append(Spacer(1, 10))
S.append(Paragraph("DÓNDE CAE — CONTRATIEMPO, SÍNCOPA Y ANTICIPACIÓN", H2))
S.append(Paragraph(
    "Hasta acá el anexo contestó dos preguntas: <b>qué figura</b> usás (el árbol) y <b>en cuántos pedazos</b> "
    "se parte el pulso (tresillo y swing). Falta la tercera, y es la que más cambia el carácter de un lick: "
    "<b>dónde empieza la nota respecto del pulso</b>.", BODY))
S.append(Paragraph(
    "Un compás de 4/4 tiene <b>ocho</b> lugares donde puede caer una nota, no cuatro. Cuatro son los números "
    "— UNO, DOS, TRES, CUATRO — y cuatro son los huecos del medio, que se cuentan <b>\"y\"</b>. Decilo en voz "
    "alta ahora mismo, sin la guitarra:", BODY))
S.append(GrillaDelCompas(W))
S.append(Paragraph(
    "Conté los compases de los tres hitos y del bonus: son <b>217</b>, y solo <b>16 arrancan a contratiempo</b> "
    "— el 7%. De los otros, <b>165 arrancan justo en el 1</b>, con el pie, y el resto arranca en algún otro "
    "número (casi siempre en el 2). Y hay <b>5 puntillos en todo el programa</b>: los cinco son la última "
    "nota de una frase, aguantada hasta que se acaba el compás. Ninguno es una figura rítmica adentro de "
    "una frase.", BODY))
S.append(Paragraph(
    "En el <b>ejercicio 44</b>, hace un par de semanas, te dije que <b>el ritmo es el 70% de la identidad "
    "de una frase</b> — y ahí te mostré tres ritmos ya terminados, sin decirte de qué están hechos. Este "
    "bloque es esa deuda: la palanca que los produce.", BODY))
S.append(Spacer(1, 6))

S.append(tabla([
    [Paragraph("<b>Las tres palabras, que no son sinónimos</b>", CELLB), Paragraph("<b>Qué es</b>", CELLB)],
    [Paragraph("<b>CONTRATIEMPO</b>", CELLB),
     Paragraph("La nota cae en un <b>\"y\"</b>, en el hueco entre dos números. Nada más que eso: es un lugar.", CELL)],
    [Paragraph("<b>SÍNCOPA</b>", CELLB),
     Paragraph("La nota entra en el \"y\" <b>y se estira por encima del número que sigue</b>, que queda sin "
               "ataque. El contratiempo es el lugar; la síncopa es el lugar <i>más</i> la duración.", CELL)],
    [Paragraph("<b>ANTICIPACIÓN</b><br/>(el <i>push</i>)", CELLB),
     Paragraph("Una síncopa que cruza la <b>barra de compás</b>: entrás en el \"y\" del 4 y el 1 del compás "
               "siguiente ya te encuentra sonando. Es el gesto más rockero de los tres.", CELL)],
], [W * 0.26, W * 0.74]))
S.append(Spacer(1, 6))

S.append(ej("D", "El número y el \"y\" (una sola nota)",
            "Antes de leer nada, hacé esto <b>sin la guitarra</b>, 30 segundos: marcá el pulso con el pie y "
            "contá en voz alta <b>UN y DOS y TRES y CUA y</b>. El pie <b>baja</b> en el número y <b>sube</b> "
            "en el \"y\". Cuando el pie sube solo, sin que lo pienses, recién ahí agarrá la viola.<br/><br/>"
            "Una sola nota las ocho veces — DO, primera cuerda traste 8. No hay nada que digitar: toda tu "
            "atención tiene que estar en el <b>lugar</b>, no en los dedos. En el compás 2, cada vez que tocás, "
            "<b>tu pie está arriba</b>. Esa incomodidad es el ejercicio.",
            "r04"))

S.append(ej("E", "Mover una nota, no agregarla",
            "Las mismas cuatro notas de siempre (8-5-8-5). Lo único que se mueve es el LA.<br/><br/>"
            "<b>Compás 1:</b> todo a tiempo, el LA cae justo en el 2. Es tu punto de comparación.<br/>"
            "<b>Compás 2:</b> el LA entra medio tiempo antes… y lo volvés a pegar en el 2. "
            "<b>Está mal a propósito.</b> No suena sincopado: suena a que metiste una nota de más y tropezaste. "
            "Es el error que comete casi todo el mundo.<br/>"
            "<b>Compás 3:</b> entra medio tiempo antes y <b>no lo repetís</b> — hay una ligadura. El 2 queda "
            "sin ataque. <i>Eso</i> es una síncopa.<br/><br/>"
            "<b>Ahora contá los números de la tablatura.</b> El compás 2 tiene cinco. El compás 3 tiene cuatro, "
            "los mismos que el compás 1. El que sincopa toca <b>menos</b>, no más.",
            "r05"))

S.append(ej("F", "El push — cruzar la barra de compás",
            "La celda de siempre cayendo en la tónica, dos veces.<br/><br/>"
            "<b>Versión recta:</b> la llegada cae justo en el 1 del compás siguiente. Bien tocado, bien "
            "medido… y suena a alguien practicando.<br/>"
            "<b>Versión anticipada:</b> <b>las mismas siete notas y las mismas figuras</b>, corridas medio "
            "tiempo para atrás. La llegada entra en el \"y\" del 4 y se liga sobre la barra.<br/><br/>"
            "Mirá las dos tablaturas: <b>8-5-8-5-7-5-7 las dos veces</b>, no cambió ni un traste. Y ahora "
            "mirá el último compás: <b>está vacío</b>. Ahí es exactamente donde cae el 1 de la banda, y vos "
            "no tocás nada — ya venías sonando desde antes.",
            "r06",
            "Ojo con la tablatura: una nota ligada no lleva número, porque no se vuelve a puntear. Ese "
            "casillero en blanco justo en el tiempo fuerte no es un error de impresión — es la síncopa."))

S.append(ej("G", "El puntillo: la máquina de fabricar síncopas",
            "<b>Escuchá los compases 1 y 2 y decime cuál es cuál. No vas a poder:</b> son el mismo sonido "
            "escrito de dos maneras, el primero con ligaduras y el segundo con puntillos. Las dos tablaturas "
            "son <b>idénticas</b> (8-5-8). El puntillo no es una figura nueva que hay que aprender: es la "
            "forma corta de escribir una nota ligada a la mitad de sí misma.<br/><br/>"
            "Y fijate de dónde sale. El árbol parte todo <b>por la mitad</b>; el puntillo hace lo contrario: "
            "le <b>suma</b> la mitad. Por eso no entra en el árbol — y por eso sincopa: un tiempo y medio no "
            "encaja en una grilla de a un tiempo, así que corre todo lo que sigue al contratiempo.<br/><br/>"
            "<b>Compás 3:</b> el patrón <b>3+3+2</b> (tres corcheas, tres corcheas, dos). Es el reparto "
            "sincopado más usado del rock, y no tiene una sola nota nueva.",
            "r07"))

S.append(caja_oscura(
    '<font color="white"><b>LA REGLA (la misma de antes, en su otra cara)</b><br/><br/>'
    '<b>Sincopar no agrega notas: mueve una.</b> Si después de sincopar tenés más notas que antes, no '
    'sincopaste — rellenaste.<br/><br/>'
    'Y la síncopa <b>no se escucha en la nota que tocás: se escucha en el tiempo fuerte que dejaste vacío</b>. '
    'Si llenás ese 1 con otra nota para no dejar un hueco, la anticipación no suena mal — <b>desaparece</b>, '
    'porque ya no queda nada contra qué escucharla. El Hito 2 te enseñó que el silencio es parte de la frase; '
    'esto te dice <b>dónde</b> ponerlo: justo donde el oído más lo espera.<br/><br/>'
    'Comprobalo contando la tablatura: en todo este bloque no hay una sola semicorchea, y los tres '
    'compases del ejercicio G —los más sincopados de todos— se tocan con <b>tres</b> ataques cada uno, '
    '<b>uno menos</b> que el compás recto del ejercicio E. Acá no hay nada que ganar tocando más rápido.</font>', W))

S.append(Spacer(1, 10))
S.append(Paragraph("LA ESCALERA DE DESPLAZAMIENTO", H2))
S.append(Paragraph(
    "El ejercicio F te probó <b>una vez</b> que mover el arranque cambia todo. Este lo convierte en un "
    "procedimiento que podés aplicar a cualquier lick tuyo: la misma celda entrando en cinco lugares "
    "distintos del compás, uno detrás del otro. <b>Las notas no cambian nunca</b> — 8-5-8-5, las cinco "
    "veces. Lo único que se mueve es dónde empieza.", BODY))
S.append(Spacer(1, 4))
S.append(ej("H", "La misma celda entrando en cinco lugares",
            "Tocá los cinco compases seguidos, con metrónomo, sin parar entre uno y otro. Vas a escuchar "
            "que la celda es siempre la misma y aun así los cinco suenan distinto. <b>Ese es todo el "
            "recurso</b>: no necesitás cinco licks, necesitás uno y cinco lugares para meterlo.<br/><br/>"
            "<b>Y ahora la parte que casi nadie enseña</b>, que es la que te va a pasar a vos apenas lo "
            "intentes solo. Fijate en el compás 6: si corrés el arranque un poco más, la frase <b>ya no "
            "entra</b> — se te va del compás y tenés que ligar la última nota para que no quede colgando. "
            "El compás 7 muestra el arreglo de verdad: <b>sacar una nota</b>. Contá las tablaturas, tiene "
            "una menos.<br/><br/>"
            "Sacar una nota no es hacer trampa ni es que te salió mal: <b>es el ajuste que hace posible el "
            "desplazamiento</b>. Cuando movés el principio de una frase, casi siempre vas a tener que "
            "tocar el final. Si no sabés esto, probás, no te cierra el compás, y concluís que la síncopa "
            "no te sale.",
            "r08",
            "Regla práctica: si al desplazar te sobra frase, sacá del final, no del principio. El "
            "principio es lo que hace que el oído reconozca que es la misma idea."))

S.append(Spacer(1, 10))
S.append(Paragraph("LLAMADA Y RESPUESTA — el solo como conversación", H2))
S.append(Paragraph(
    "Hasta acá el anexo trabajó <b>una</b> frase. Esto es lo que pasa cuando hay dos y se hablan entre "
    "ellas. El ejercicio 49 del Hito 3 ya te dio una arquitectura de solo — presenta, desarrolla, clímax, "
    "cierra — pero esa es una arquitectura <b>narrativa</b>: una curva que sube y baja. Esta es otra, y "
    "es <b>conversacional</b>: una pregunta, una respuesta, la pregunta de nuevo, y la respuesta que "
    "cierra. No es la misma con otro nombre, y no compiten: son dos moldes distintos y te conviene "
    "tener los dos.", BODY))
S.append(Spacer(1, 4))
S.append(tabla([
    [Paragraph("<b>Frase</b>", CELLB), Paragraph("<b>Qué hace</b>", CELLB), Paragraph("<b>Cómo se reconoce</b>", CELLB)],
    [Paragraph("<b>1 · LLAMADA</b>", CELLB),
     Paragraph("Pregunta. Presenta la idea y la deja abierta.", CELL),
     Paragraph("Termina en una nota que <b>no</b> es la tónica (acá, la 5ª). El oído queda esperando.", CELL)],
    [Paragraph("<b>2 · RESPUESTA</b>", CELLB),
     Paragraph("Contesta. Baja y cierra lo que la llamada dejó abierto.", CELL),
     Paragraph("Termina en la <b>tónica</b>. Fijate que arranca igual que la llamada: está escuchando.", CELL)],
    [Paragraph("<b>1 · LLAMADA otra vez</b>", CELLB),
     Paragraph("Repite la pregunta — pero no idéntica.", CELL),
     Paragraph("<b>Mismo primer compás, otro final</b>, y mudada a la caja 2. Eso es \"repetir más arriba\".", CELL)],
    [Paragraph("<b>3 · RESPUESTA FINAL</b>", CELLB),
     Paragraph("Cierra la conversación entera, no sólo la última pregunta.", CELL),
     Paragraph("La misma tónica, pero <b>una octava abajo</b>. Bajar de octava es lo que la vuelve final.", CELL)],
], [W * 0.22, W * 0.34, W * 0.44]))
S.append(Spacer(1, 6))
S.append(ej("I", "Llamada y respuesta (el molde 1 · 2 · 1 · 3)",
            "Ocho compases, cuatro frases de dos. Tocalo con backing y prestá atención a una sola cosa: "
            "<b>las dos llamadas comparten el primer compás nota por nota</b>. Eso no es pereza — es lo "
            "único que hace que el oyente reconozca que volvió la misma pregunta. Si cambiás el principio, "
            "es otra frase; si cambiás sólo el final, es la misma frase contestada distinto.<br/><br/>"
            "<b>Por qué la segunda llamada está en la caja 2:</b> repetir una idea más arriba es la forma "
            "más barata de que suene desarrollada y no repetida. Es el mismo mecanismo del ejercicio 46 del "
            "Hito 3 (un lick en las 5 cajas), usado acá con un fin distinto: allá probaba que un lick no es "
            "un lugar, acá <b>usa</b> ese hecho para construir una conversación.",
            "r09",
            "El error típico: contestar más fuerte y más rápido de lo que preguntaste. Una respuesta que "
            "grita no está contestando — está interrumpiendo. Contestá al mismo volumen y en el mismo "
            "lugar del compás que la llamada."))

S.append(Spacer(1, 8))
S.append(Paragraph("EL PROBLEMA DE PRACTICAR ESTO SOLO (y los 3 correctores)", H2))
S.append(Paragraph(
    "Esto es lo primero del anexo que <b>no podés practicar sin metrónomo o backing</b>. Con las 3 velocidades "
    "o el tresillo podías controlarte solo; acá no, y la razón es incómoda: <b>una síncopa mal medida suena "
    "igual que llegar tarde</b>. Y hay un error que es invisible desde adentro — tocás la nota anticipada y "
    "tu pie se va con ella: el \"y\" se te vuelve el 1 nuevo, el compás entero rota, y terminás tocando algo "
    "perfectamente recto convencido de que sincopaste. Un profesor al lado te lo corrige en dos segundos; "
    "solo en tu casa lo podés practicar mal durante meses.", BODY))
S.append(Spacer(1, 3))
S.append(tabla([
    [Paragraph("<b>Corrector</b>", CELLB), Paragraph("<b>Cómo se hace</b>", CELLB), Paragraph("<b>Qué te delata</b>", CELLB)],
    [Paragraph("<b>El click flaco</b>", CELLB),
     Paragraph("Poné el metrónomo a la <b>mitad</b> del BPM, sonando solo en el 1 y el 3.", CELL),
     Paragraph("Si corriste el pulso, a los cuatro compases te desencontrás del click. Un click denso te tapa "
               "el error; uno flaco te lo canta.", CELL)],
    [Paragraph("<b>Contar en voz alta</b>", CELLB),
     Paragraph("<b>Mientras</b> tocás, no después: UN y DOS y TRES y CUA y.", CELL),
     Paragraph("Si no podés, el pulso está en tus manos y no en tu cabeza — y si está en tus manos, se te va "
               "a mudar cada vez que sincopes.", CELL)],
    [Paragraph("<b>Filmate el pie</b>", CELLB),
     Paragraph("20 segundos de celular apuntando al piso.", CELL),
     Paragraph("Tiene que haber al menos una nota que ataques con el pie <b>arriba</b>. Si pie y mano bajan "
               "siempre juntos, no sincopaste: moviste el 1.", CELL)],
], [W * 0.20, W * 0.38, W * 0.42]))
S.append(Spacer(1, 6))
S.append(Paragraph(
    "<b>Y una advertencia de dosis:</b> si anticipás todo, al tercer compás el oído del que escucha se "
    "reacomoda y toma la anticipación como el pulso nuevo. Ahí la síncopa deja de existir. Una síncopa vale "
    "por lo que la rodea — necesita notas que sí caigan en el tiempo para que se note.", BODY))

# ============================================================ 6. CÓMO PRACTICARLO
S.append(Spacer(1, 10))
S.append(Paragraph("CÓMO SE PRACTICA ESTO (10 MINUTOS, DENTRO DE TU RUTINA)", H2))
S.append(Paragraph(
    "No hace falta tiempo nuevo. Agarrás <b>un</b> lick que ya sabés — cualquiera de los que venís "
    "robando en el Hito 3, o del banco de licks — y le hacés esta escalera. Un lick por semana alcanza.", BODY))
S.append(Spacer(1, 3))
S.append(tabla([
    [Paragraph("<b>Paso</b>", CELLB), Paragraph("<b>Qué hacés</b>", CELLB), Paragraph("<b>Cuándo pasás al siguiente</b>", CELLB)],
    [Paragraph("1", CELLB),
     Paragraph("Tocá el lick en <b>negras</b>, con metrónomo lento (60-70 BPM).", CELL),
     Paragraph("Cuando cae parejo y sin acelerar. No antes.", CELL)],
    [Paragraph("2", CELLB),
     Paragraph("El mismo lick en <b>corcheas</b>, mismo BPM. Ahora te sobran 2 pulsos: <b>dejalos en silencio</b>.", CELL),
     Paragraph("Cuando aguantás el silencio sin llenarlo. Esto es lo difícil, no las notas.", CELL)],
    [Paragraph("3", CELLB),
     Paragraph("El mismo lick en <b>semicorcheas</b>. Te sobran 3 pulsos de silencio.", CELL),
     Paragraph("Cuando entra limpio y el silencio sigue ahí.", CELL)],
    [Paragraph("4", CELLB),
     Paragraph("Ahora <b>atresillalo</b>. Y después probalo con <b>swing</b>.", CELL),
     Paragraph("Cuando los dos suenan distintos entre sí de verdad.", CELL)],
    [Paragraph("5", CELLB),
     Paragraph("<b>Anticipalo</b>: el mismo lick entrando medio tiempo antes, ligando sobre la barra. "
               "Metrónomo solo en el 1 y el 3.", CELL),
     Paragraph("Cuando seguís enganchado al click a los ocho compases y el tiempo fuerte queda vacío.", CELL)],
    [Paragraph("6", CELLB),
     Paragraph("Poné un backing y <b>mezclá</b>: la misma idea en negras, después de adorno en semicorcheas, "
               "después anticipada.", CELL),
     Paragraph("Éste no se termina nunca. Es improvisar.", CELL)],
], [W * 0.08, W * 0.50, W * 0.42]))
S.append(Spacer(1, 8))

S.append(caja_oscura(
    '<font color="white"><b>El error que va a cometer todo el mundo</b> es tratar los pasos 2 y 3 como una '
    'carrera: subir el metrónomo hasta donde no sale. No es eso. <b>El BPM no se toca en toda la escalera.</b> '
    'Lo que cambia es cuánto del compás ocupa la frase — el pulso es siempre el mismo. Si estás subiendo el '
    'metrónomo, estás haciendo otro ejercicio.</font>', W))

S.append(Spacer(1, 10))
S.append(Paragraph("EL CIERRE — TODO ENCADENADO", H2))
S.append(Paragraph(
    "Cada hito del programa cierra tocando una pieza entera: el ejercicio 16, el 34, el 53. Este anexo "
    "también tiene el suyo. Nueve compases con <b>la misma celda de siempre</b> pasando, en orden, por "
    "todo lo que trabajaste acá: negras, corcheas, tresillo, contratiempo, puntillo y el push.", BODY))
S.append(Spacer(1, 4))
S.append(ej("J", "Los nueve compases que resumen el anexo",
            "No hay nada nuevo. Es literalmente 8-5-8-5 de punta a punta, y aun así los nueve compases "
            "suenan a nueve cosas distintas. Si podés tocarlo entero, a tempo y sin mirar, el anexo está "
            "aprendido.<br/><br/>"
            "<b>Mirá el último compás.</b> Vuelve el motivo del compás 1 — las mismas cuatro notas con las "
            "que arrancaste — pero en <b>blancas</b>: la mitad de velocidad. Eso hace dos cosas a la vez. "
            "Es el <b>leitmotiv</b> del ejercicio 52 del Hito 3 (la idea que vuelve al final y hace que el "
            "solo se sienta cerrado), y es la tesis de todo este anexo demostrada sobre sí misma: "
            "<b>mismas notas, otra figura, otra función</b>. Empezaste con una frase y terminás con una "
            "conclusión, sin haber cambiado una sola nota.",
            "r10",
            "Cuando lo tengas, hacé el paso siguiente: tocá los mismos nueve compases con un lick TUYO en "
            "lugar de la celda. Ahí el anexo deja de ser un ejercicio y pasa a ser una herramienta."))

S.append(Spacer(1, 10))
S.append(Paragraph("CHECKLIST DE CIERRE", H2))
S.append(tabla([
    [Paragraph(CAJ, CELL), Paragraph("Puedo dibujar el árbol de memoria y explicar por qué todas las filas duran lo mismo.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Agarro un lick mío y lo toco en negras, corcheas y semicorcheas sin cambiar el BPM.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Cuando comprimo, <b>dejo el silencio que queda</b> en vez de llenarlo con más notas.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Distingo de oído un tresillo de un par de corcheas.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Distingo de oído recto de swing, y puedo tocar la misma frase de las dos formas.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("En una improvisación uso <b>al menos dos densidades distintas</b> — no todo parejo.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Puedo contar <b>UN y DOS y TRES y CUA y</b> en voz alta mientras toco, sin trabarme.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Toco una frase anticipada con el metrónomo solo en el 1 y el 3, y sigo enganchado a los 8 compases.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Al menos una frase mía <b>entra antes del tiempo fuerte</b> — y ese tiempo fuerte queda vacío.", CELL)],
], [1.1 * cm, W - 1.1 * cm], header=False))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "<b>Entregable sugerido:</b> 1 minuto improvisando sobre un backing donde se escuche claramente una frase "
    "en negras y, más adelante, esa misma idea de adorno en semicorcheas. Que se reconozca que es la misma "
    "idea. Y que haya <b>exactamente tres frases que entren antes del tiempo fuerte</b> — tres, contadas. "
    "Si son más, dejó de ser un recurso y se volvió tu pulso nuevo. Eso es todo el anexo en una "
    "grabación.", BODY))
S.append(Paragraph(
    "Este anexo va en paralelo al Hito 3. Sus ejercicios se numeran con letras (A a J) justamente para que "
    "no se mezclen con los 59 del programa: no reemplazan ninguna semana. El módulo de ritmo del mes 2 "
    "(el de lectura) te enseñó a LEER las figuras; éste te enseña a usarlas en tus propias frases.<br/><br/>"
    "<b>Y una aclaración, porque te la vas a preguntar:</b> casi todo el anexo está en la caja 1 y eso es "
    "a propósito. Si además de cambiar la figura te cambiara la posición, no sabrías cuál de las dos cosas "
    "te cambió el sonido. Acá la geografía la dejamos quieta para poder escuchar el ritmo — ya la "
    "trabajaste los tres meses. La única excepción es el ejercicio I, donde mudarse de caja <i>es</i> el "
    "contenido.", SMALL))

doc.build(S)
print("OK  Anexo-Ritmo-El-Arbol-y-las-3-Velocidades.pdf")
