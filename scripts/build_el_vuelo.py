# -*- coding: utf-8 -*-
"""Arma el PDF de "EL VUELO" -- la guia del Pilar 5 (memoria/02 SS28-QUINQUIES).

No es un cuadernillo de ejercicios como los de los Hitos 1-3: el Pilar 5 no ensena tecnica nueva,
es la integracion de todo lo anterior. Por eso este documento no tiene partituras nuevas -- es
checklist, consigna de la sesion en vivo, y el brief del solo final, reusando lo que ya existe
(la arquitectura del ej. 49-53 del Hito 3).

Misma familia visual que los 4 cuadernillos (cuadernillo_comun.py), para que entre parejo al
mismo flujo de Design.
"""
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Spacer

from cuadernillo_comun import (H1, H2, BODY, SMALL, CELL, CELLB, CAJ, IG,
                               documento, tabla, caja_oscura)

doc = documento("Guia-El-Vuelo-Pilar5.pdf",
                "EL VUELO",
                "Pilar 5 · donde todo lo que aprendiste deja de ser tecnica y se convierte en vos tocando",
                "Solo con Sabor · El Vuelo",
                "El Vuelo - Pilar 5 - Solo con Sabor")
W = doc.width
S = []

# ============================================================ 1. QUÉ ES ESTO
S.append(Paragraph("ANTES DE ARRANCAR: QUÉ ES ESTO (Y QUÉ NO)", H2))
S.append(Paragraph(
    "Este pilar no tiene ejercicios nuevos. No hay un traste nuevo que aprender, ni una técnica que "
    "todavía no viste. Si llegaste hasta acá, ya sabés todo lo que hace falta — El Mapa, El Sabor, "
    "El Vocabulario y El Pulso ya están en tus manos.", BODY))
S.append(Paragraph(
    "El Vuelo es otra cosa: es el momento en el que dejás de juntar piezas y empezás a "
    "<b>soltarlas</b>. No se trata de sumar más — se trata de que lo que ya tenés deje de pedirte "
    "pensar.", BODY))

# ============================================================ 2. QUÉ VA A PASAR
S.append(Paragraph("QUÉ VA A PASAR ACÁ (Y QUÉ VAS A LOGRAR)", H2))
S.append(Paragraph("Durante esta etapa vas a:", BODY))
S.append(tabla([
    [Paragraph("<b>Vas a...</b>", CELLB), Paragraph("<b>Qué significa en la práctica</b>", CELLB)],
    [Paragraph("Improvisar sin acordarte de las cajas", CELL),
     Paragraph("El mástil ya no es un mapa que consultás — es un lugar donde estás parado.", CELL)],
    [Paragraph("Sonar con sabor sin planearlo", CELL),
     Paragraph("El bending, el vibrato, el espacio aparecen solos, en el momento que los necesita "
               "la frase — no porque te acordaste de meterlos.", CELL)],
    [Paragraph("Meter tus propios licks sin anunciarlos", CELL),
     Paragraph("Entran y salen de tu improvisación como una palabra más, no como una cita.", CELL)],
    [Paragraph("Tocar con otra persona en vivo", CELL),
     Paragraph("Por primera vez en el programa con esa exigencia real: entrar, ceder el "
               "protagonismo, retomarlo, escuchar mientras tocás.", CELL)],
    [Paragraph("Grabar tu solo final", CELL),
     Paragraph("Un minuto tuyo, de punta a punta — al mismo tiempo tu examen y tu trofeo.", CELL)],
], [4.6 * cm, W - 4.6 * cm]))
S.append(Spacer(1, 6))
S.append(Paragraph(
    "El resultado de este pilar no es una habilidad nueva. Es la certeza de que lo que veníamos "
    "construyendo ya es <b>un solo idioma — el tuyo.</b>", BODY))

# ============================================================ 3. CHECKLIST
S.append(Paragraph("EL CHECKLIST — ANTES DE VENIR A ESTA SESIÓN", H2))
S.append(Paragraph(
    "No es un examen escrito. Es una lista honesta que te hacés vos, en soledad, con la guitarra "
    "en la mano.", BODY))
S.append(tabla([
    [Paragraph(CAJ, CELL), Paragraph(
        "Puedo improvisar 30 segundos moviéndome por lo menos por 3 cajas, sin pausas para pensar "
        "dónde estoy parado.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph(
        "Metí un bending, un vibrato o un silencio real sin decidirlo antes — apareció solo, en "
        "el momento.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph(
        "Uso al menos un lick que robé y transformé, y no se nota como una cita pegada.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph(
        "Cuando pruebo tocar sobre un backing que cambia de acorde, no me pierdo — sigo, aunque no "
        "\"sepa\" conscientemente por qué funciona.", CELL)],
], [1.0 * cm, W - 1.0 * cm], header=False))
S.append(Spacer(1, 4))
S.append(Paragraph(
    "Si tildaste los cuatro, estás listo para EL VUELO. Si te falta alguno, no es un problema — es "
    "una señal de a cuál de los pilares anteriores volver una semana más.", SMALL))

# ============================================================ 4. LA SESIÓN EN VIVO
S.append(Paragraph("LA SESIÓN EN VIVO: TOCAR CON OTRO", H2))
S.append(Paragraph(
    "Esta es la parte del programa que no se puede pregrabar. Necesita que estés ahí, en tiempo "
    "real, con otra persona tocando al lado.", BODY))
S.append(Paragraph("<b>La consigna:</b>", BODY))
S.append(tabla([
    [Paragraph("<b>1</b>", CELLB), Paragraph("Arrancás vos, 20-30 segundos, solo.", CELL)],
    [Paragraph("<b>2</b>", CELLB), Paragraph(
        "En algún momento, sin avisar, le cedés el lugar a quien esté tocando con vos — un "
        "silencio, una nota larga que se apaga, cualquier gesto que diga \"seguí vos\".", CELL)],
    [Paragraph("<b>3</b>", CELLB), Paragraph(
        "Esa persona toma la posta. Vos la escuchás — no rellenás el silencio, no compites.", CELL)],
    [Paragraph("<b>4</b>", CELLB), Paragraph(
        "Volvés a entrar cuando sientas que hay algo que agregar, no porque \"te toca\".", CELL)],
], [0.8 * cm, W - 0.8 * cm]))
S.append(Spacer(1, 4))
S.append(Paragraph(
    "No hay una forma correcta de hacerlo. Lo único que se evalúa es si escuchaste, no si tocaste "
    "bien.", SMALL))
S.append(Spacer(1, 4))
S.append(Paragraph(
    "<i>Optativo, solo si el grupo lo pide o sobra tiempo:</i> repetir la misma consigna una vuelta "
    "en Sol menor o Si menor. No es parte de la consigna evaluada — es una forma de estirar, en vivo, "
    "la idea de \"Cambiar de tonalidad\" del cierre de este documento, si el momento se presta.", SMALL))

# ============================================================ 5. EL EXAMEN
S.append(Paragraph("EL EXAMEN: TU SOLO FINAL", H2))
S.append(Paragraph(
    "Un minuto, grabado, de punta a punta. Las reglas son las mismas que ya conocés del cierre "
    "del Vocabulario — ahora te las repetimos como lo que son: el examen de todo el programa.", BODY))
S.append(tabla([
    [Paragraph("<b>Territorio</b>", CELLB), Paragraph(
        "Tiene que moverse por al menos 3 cajas. No puede vivir en la caja 1.", CELL)],
    [Paragraph("<b>Final</b>", CELLB), Paragraph(
        "Decidido y ensayado — sabés en qué nota cerrás. Nada de apagarse porque se acabó el "
        "backing.", CELL)],
    [Paragraph("<b>Con sabor</b>", CELLB), Paragraph(
        "Si sacamos las notas y dejamos solo el bending, el vibrato y el espacio, tiene que "
        "seguir sonando a vos.", CELL)],
], [3.2 * cm, W - 3.2 * cm]))
S.append(Spacer(1, 6))
S.append(Paragraph(
    "Esto no es un ejercicio más. Es tu trofeo — el video que mostrás cuando alguien te pregunta "
    "qué aprendiste en tres meses.", BODY))

S.append(Spacer(1, 10))
S.append(caja_oscura(
    '<font color="white" size="10.5"><b>Mandame tu solo final.</b></font><br/>'
    '<font color="#f7d7d2" size="9">Lo escucho entero y te mando una devolución grabada, no un '
    '"está muy bueno". Este solo es la prueba de que dejaste de repetir lo mismo de siempre — y '
    'ese es el punto de partida de todo lo que sigue. · %s</font>' % IG, W))

# ============================================================ 6. UNA COSA MÁS (optativo, no se evalúa)
S.append(Spacer(1, 14))
S.append(Paragraph("UNA COSA MÁS: CAMBIAR DE TONALIDAD", H2))
S.append(Paragraph(
    "Los tres hitos, El Pulso, El Vuelo — el programa entero lo recorriste en La menor. Es a propósito: "
    "aprender una técnica nueva y cambiar de tonalidad al mismo tiempo es aprender dos cosas a la vez, y "
    "por eso el programa nunca te lo pidió. Pero si llegaste hasta acá con el mapa bien puesto, esto no "
    "es tan difícil como suena — son dos pasos, y el primero ni siquiera mueve la mano.", BODY))

S.append(Paragraph("PASO 1 — LA MISMA CAJA YA ES DOS ESCALAS", H2))
S.append(Paragraph(
    "La pentatónica menor de La (La · Do · Re · Mi · Sol) y la pentatónica mayor de Do (Do · Re · Mi · "
    "Sol · La) son las mismas cinco notas. Exactamente las mismas. Lo único que cambia es dónde "
    "resolvés: si tus frases terminan en La, suena a menor — el peso que ya conocés. Si esas mismas "
    "frases, en la misma caja 1, sin mover un dedo, terminan en Do, suena mayor: más abierta, más "
    "resuelta.", BODY))
S.append(Paragraph(
    "No es una escala nueva. Es la misma escala, mirada con otro final. Es el paso más barato de todo "
    "este documento — probalo antes que cualquier otra cosa.", SMALL))

S.append(Paragraph("PASO 2 — MOVER LA FORMA, NO INVENTAR UNA", H2))
S.append(Paragraph(
    "Para cambiar de tonalidad de verdad (no solo de final, sino de lugar en el mástil), lo que se "
    "mueve es la FORMA completa — mismos dedos, mismas distancias, otro punto de partida. Conviene "
    "arrancar por las tonalidades más cerca de La, no por las lejanas: un salto chico todavía se "
    "siente como la misma forma corrida un poco; uno grande empieza a sentirse como una escala "
    "distinta, y ahí se pierde el punto de todo esto.", BODY))
S.append(tabla([
    [Paragraph("<b>1</b>", CELLB), Paragraph(
        "Encontrá la tónica de la nueva tonalidad en la 6ª cuerda. Las dos más cerca de tu casa (La, "
        "traste 5) son Sol menor (2 trastes abajo, traste 3) y Si menor (2 trastes arriba, traste 7) "
        "— un salto chico, la mano lo reconoce enseguida como el mismo gesto.", CELL)],
    [Paragraph("<b>2</b>", CELLB), Paragraph(
        "Plantá ahí la caja 1 entera — las mismas distancias entre dedos, el mismo dibujo. Se mueve "
        "en bloque.", CELL)],
    [Paragraph("<b>3</b>", CELLB), Paragraph(
        "Elegí UN lick que ya sea tuyo (de El Vocabulario) y tocalo ahí, de oído. No hay tablatura "
        "nueva que leer — es la misma que ya sabés, parada en otro lugar.", CELL)],
], [0.8 * cm, W - 0.8 * cm]))
S.append(Spacer(1, 4))
S.append(Paragraph(
    "Si preferís la opción más cómoda para arrancar en vez de la más cercana: Mi menor (al aire, "
    "traste 0) tiene las cuerdas sueltas a favor y es, de lejos, la tonalidad menor más pisada de "
    "todo el rock — lo que toques ahí va a sonar familiar más rápido que en cualquier otro lado.", SMALL))
S.append(Spacer(1, 4))
S.append(Paragraph(
    "No hace falta que te salga perfecto, y no hace falta que sea hoy. Ninguno de los dos pasos es un "
    "ejercicio del programa ni se evalúa en el solo final — es la misma lógica de \"Y después de esto, "
    "explorá\" con la que cierra El Vocabulario, aplicada a moverte de tonalidad en vez de a otro "
    "recurso. Es la puerta que dejás entreabierta.", SMALL))

doc.build(S)
print("OK Guia-El-Vuelo-Pilar5.pdf")
