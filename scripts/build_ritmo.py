# -*- coding: utf-8 -*-
"""Arma el PDF del ANEXO DE RITMO — el árbol de las figuras y las 3 velocidades.

Requiere que antes se haya corrido `gen_scores_ritmo.py` (genera ./partituras/r01..r03).

Este anexo NO es un hito nuevo: corre en paralelo al Hito 2, al lado del módulo de
ritmo basado en Pozzoli que Feli produce aparte. Por eso sus ejercicios se numeran
con letras (A, B, C) y no tocan la numeración corrida 1-59 de los cuadernillos.

El dato que justifica que exista, contado con `auditar_cajas.py` sobre las 395 notas
de los 4 cuadernillos: corcheas 50% · negras 28% · blancas 13% · redondas 8% · UNA
sola semicorchea, cero fusas. El alumno termina el programa con un vocabulario
rítmico de dos figuras.
"""
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Spacer, KeepTogether

from cuadernillo_comun import (H1, H2, H3, BODY, SMALL, CELL, CELLB, CAJ,
                               ArbolFiguras, documento, tabla, caja_oscura, score)

doc = documento("Anexo-Ritmo-El-Arbol-y-las-3-Velocidades.pdf",
                "ANEXO DE RITMO",
                "El árbol de las figuras · el mismo lick en 4, 2 o 1 pulso · tresillo y swing",
                "Solo con Sabor · Anexo de ritmo (va con el Hito 2)",
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
    "Conté todas las notas de los tres hitos y del bonus. Son <b>395</b>, y se reparten así:", BODY))
S.append(tabla([
    [Paragraph("<b>Figura</b>", CELLB), Paragraph("<b>Corchea</b>", CELLB), Paragraph("<b>Negra</b>", CELLB),
     Paragraph("<b>Blanca</b>", CELLB), Paragraph("<b>Redonda</b>", CELLB), Paragraph("<b>Semicorchea</b>", CELLB),
     Paragraph("<b>Fusa</b>", CELLB)],
    [Paragraph("<b>Cuánto</b>", CELLB), Paragraph("50%", CELL), Paragraph("28%", CELL),
     Paragraph("13%", CELL), Paragraph("8%", CELL),
     Paragraph("<b>1 sola</b>", CELL), Paragraph("<b>ninguna</b>", CELL)],
], [W * 0.16] + [W * 0.14] * 6))
S.append(Spacer(1, 7))
S.append(Paragraph(
    "O sea: aprendiste <b>dónde</b> están las notas (Hito 1) y <b>cómo</b> atacarlas (Hito 2), pero durante "
    "todo el programa las tocaste con dos figuras. Una sola semicorchea en 395 notas. Eso no está mal — se "
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
            "Es el mismo truco del ejercicio 46 del Hito 3 (un lick en las 5 cajas), pero en el otro eje. "
            "Aquel probaba que un lick no es un lugar. Éste prueba que tampoco es una velocidad."))

S.append(caja_oscura(
    '<font color="white"><b>LA REGLA QUE HACE QUE ESTO NO TE ARRUINE EL HITO 2</b><br/><br/>'
    'Comprimir un lick <b>no te ahorra tiempo: te regala silencio</b>. Si la frase entraba en 4 pulsos y '
    'ahora entra en 1, no ganaste velocidad — ganaste <b>3 pulsos de silencio</b> que antes no tenías.<br/><br/>'
    'Todo el Hito 2 te enseñó que el espacio es parte de la frase. Este anexo es la máquina de fabricar '
    'espacio. Si usás la compresión para meter <i>más</i> notas en el mismo lugar, te comiste el regalo y '
    'volviste a sonar atropellado. <b>Lo que hacés con esos 3 pulsos que quedaron libres es lo que decide '
    'si sonás a músico.</b></font>', W))

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

# ============================================================ 6. CÓMO PRACTICARLO
S.append(Spacer(1, 10))
S.append(Paragraph("CÓMO SE PRACTICA ESTO (10 MINUTOS, DENTRO DE TU RUTINA)", H2))
S.append(Paragraph(
    "No hace falta tiempo nuevo. Agarrás <b>un</b> lick que ya sabés — cualquiera del Hito 1 o del Hito 2 — "
    "y le hacés esta escalera. Un lick por semana alcanza.", BODY))
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
     Paragraph("Poné un backing y <b>mezclá</b>: la misma idea en negras, después de adorno en semicorcheas.", CELL),
     Paragraph("Éste no se termina nunca. Es improvisar.", CELL)],
], [W * 0.08, W * 0.50, W * 0.42]))
S.append(Spacer(1, 8))

S.append(caja_oscura(
    '<font color="white"><b>El error que va a cometer todo el mundo</b> es tratar los pasos 2 y 3 como una '
    'carrera: subir el metrónomo hasta donde no sale. No es eso. <b>El BPM no se toca en toda la escalera.</b> '
    'Lo que cambia es cuánto del compás ocupa la frase — el pulso es siempre el mismo. Si estás subiendo el '
    'metrónomo, estás haciendo otro ejercicio.</font>', W))

S.append(Spacer(1, 10))
S.append(Paragraph("CHECKLIST DE CIERRE", H2))
S.append(tabla([
    [Paragraph(CAJ, CELL), Paragraph("Puedo dibujar el árbol de memoria y explicar por qué todas las filas duran lo mismo.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Agarro un lick mío y lo toco en negras, corcheas y semicorcheas sin cambiar el BPM.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Cuando comprimo, <b>dejo el silencio que queda</b> en vez de llenarlo con más notas.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Distingo de oído un tresillo de un par de corcheas.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Distingo de oído recto de swing, y puedo tocar la misma frase de las dos formas.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("En una improvisación uso <b>al menos dos densidades distintas</b> — no todo parejo.", CELL)],
], [1.1 * cm, W - 1.1 * cm], header=False))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "<b>Entregable sugerido:</b> 1 minuto improvisando sobre un backing donde se escuche claramente una frase "
    "en negras y, más adelante, esa misma idea de adorno en semicorcheas. Que se reconozca que es la misma "
    "idea. Eso es todo el anexo en una grabación.", BODY))
S.append(Paragraph(
    "Este anexo va en paralelo al Hito 2, junto con el módulo de ritmo. Sus ejercicios se numeran con letras "
    "(A, B, C) justamente para que no se mezclen con los 59 del programa: no reemplazan ninguna semana.", SMALL))

doc.build(S)
print("OK  Anexo-Ritmo-El-Arbol-y-las-3-Velocidades.pdf")
