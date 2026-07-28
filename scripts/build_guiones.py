# -*- coding: utf-8 -*-
"""Arma el PDF de los 3 guiones pendientes: Historia, Reel Fijado, Cómo es una clase.

Cada guion tiene su línea de tiempo en tabla (tiempo | qué pasa | qué decís o tocás),
más tono, copy de post, hashtags y notas de edición. Mismo estilo visual que los
cuadernillos de ejercicios.
"""
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether

from cuadernillo_comun import (H1, H2, H3, BODY, SMALL, CELL, CELLB, RED, DARK, LIGHT, LIGHT2, BORDER,
                               IG, documento, tabla, caja_oscura)

doc = documento("Guiones-Historia-Fijado-Vendedores.pdf",
                "GUIONES PENDIENTES",
                "Historia · Reel fijado · 2 guiones vendedores — con línea de tiempo",
                "Solo con Sabor · Guiones — Historia, Fijado, Vendedores",
                "Guiones - Historia, Fijado, Vendedores")
W = doc.width
S = []


def linea_tiempo(filas, colw=None):
    """Tabla de timeline: [tiempo, qué se ve/hace, qué decís (o vacío)]."""
    header = [Paragraph("<b>Tiempo</b>", CELLB), Paragraph("<b>Qué se ve / hacés</b>", CELLB),
              Paragraph("<b>Qué decís</b>", CELLB)]
    rows = [header]
    for t, ve, dice in filas:
        rows.append([Paragraph("<b>%s</b>" % t, CELLB), Paragraph(ve, CELL),
                     Paragraph(dice, CELL) if dice else Paragraph("<i>(sin diálogo)</i>", SMALL)])
    cw = colw or [2.1 * cm, W * 0.34, W - 2.1 * cm - W * 0.34]
    t = Table(rows, colWidths=cw)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), LIGHT),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LIGHT2]),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    return t


def ficha_tecnica(filas):
    rows = [[Paragraph("<b>%s</b>" % k, CELLB), Paragraph(v, CELL)] for k, v in filas]
    t = Table(rows, colWidths=[2.6 * cm, W - 2.6 * cm])
    t.setStyle(TableStyle([
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, LIGHT2]),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    return t


def banner_video(numero, titulo, subtitulo):
    etiqueta = "VIDEO #%s" % numero if numero.isdigit() else "GUION %s" % numero
    t = Table([[Paragraph('<font color="white" size="14"><b>%s</b></font><br/>'
                          '<font color="white" size="12"><b>%s</b></font><br/>'
                          '<font color="#f7d7d2" size="9">%s</font>' % (etiqueta, titulo, subtitulo),
                          BODY)]], colWidths=[W])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), RED),
                           ('LEFTPADDING', (0, 0), (-1, -1), 12), ('RIGHTPADDING', (0, 0), (-1, -1), 12),
                           ('TOPPADDING', (0, 0), (-1, -1), 9), ('BOTTOMPADDING', (0, 0), (-1, -1), 9)]))
    return t


# ============================================================ PORTADA
S.append(Paragraph("LOS GUIONES QUE FALTAN PARA COMPLETAR EL STOCK", H1))
S.append(Paragraph(
    "De los 8 videos filmados, 6 son creencias atacadas. Ninguno responde <b>\"¿por qué vos?\"</b> "
    "— la objeción que más frena una venta de USD 400-900 a un desconocido de Instagram. Historia y "
    "Fijado cierran esa grieta. Y para el 3% que ya está listo para comprar (regla 97/3), van los dos "
    "guiones vendedores: conversión pura, sin regalar en público lo que la llamada de descubrimiento "
    "tiene que vender.", BODY))
S.append(tabla([
    [Paragraph("<b>#</b>", CELLB), Paragraph("<b>Video</b>", CELLB), Paragraph("<b>Función</b>", CELLB),
     Paragraph("<b>Duración</b>", CELLB)],
    [Paragraph("11", CELLB), Paragraph("TU HISTORIA", CELL),
     Paragraph("Responde \"¿por qué vos?\" — te humaniza, te vuelve la opción elegida.", CELL),
     Paragraph("55-65 seg", CELL)],
    [Paragraph("12", CELLB), Paragraph("REEL FIJADO", CELL),
     Paragraph("La carta de presentación del perfil. Prueba de que sabés tocar.", CELL),
     Paragraph("25-35 seg", CELL)],
    [Paragraph("V1", CELLB), Paragraph("VENDEDOR — \"Como que desaparece\"", CELL),
     Paragraph("Conversión pura, a cámara sin tocar. Para el 3% listo para comprar.", CELL),
     Paragraph("30-35 seg", CELL)],
    [Paragraph("V2", CELLB), Paragraph("VENDEDOR — \"Dejá de mirar tutoriales\"", CELL),
     Paragraph("Mismo objetivo, con guitarra sonando y el espejo del \"yo era ese tipo\".", CELL),
     Paragraph("40-45 seg", CELL)],
], [1.1 * cm, 5.2 * cm, W - 8.2 * cm, 1.9 * cm]))

S.append(Paragraph("¿QUÉ PASÓ CON \"CÓMO ES UNA CLASE\"?", H2))
S.append(Paragraph(
    "Se sacó del stock público. Es contenido que corresponde a la <b>llamada de descubrimiento</b>, "
    "mano a mano con el potencial cliente — publicarlo le regala al visitante la información que "
    "debería generar esa conversación privada. Sí vale la pena grabarlo una vez, sin subir, como "
    "ensayo de cómo lo vas a explicar en la llamada real.", BODY))

S.append(Paragraph("ORDEN DE FILMACIÓN SUGERIDO", H2))
S.append(Paragraph(
    "<b>1º Historia</b> — es el que necesita más tranquilidad emocional y el que más ensayo pide, "
    "conviene sacarlo de encima primero. <b>2º Fijado</b> — el más simple: solo tocar bien, sin hablar, "
    "buen día para relajar después del esfuerzo del anterior. <b>3º un vendedor</b> — elegí \"Dejá de "
    "mirar tutoriales\" si preferís tener guitarra sonando, o \"Como que desaparece\" si preferís un "
    "video todo a cámara, sin tocar. <b>Recordá:</b> los vendedores se publican recién cuando ya haya "
    "autoridad construida (después de varios Formato C) — filmalos ahora, pero no los subas todavía.", BODY))

S.append(Paragraph("CÓMO LEER LA LÍNEA DE TIEMPO", H2))
S.append(Paragraph(
    "Cada guion tiene una tabla con tres columnas: <b>cuándo</b> (minuto:segundo), <b>qué se ve o hacés</b> "
    "en cámara, y <b>qué decís</b> en ese tramo. Grabá mirando la tabla al lado de la cámara — no hace falta "
    "memorizar palabra por palabra, alcanza con tener clara la idea de cada bloque.", BODY))

# ============================================================ VIDEO 11 — HISTORIA
S.append(PageBreak())
S.append(banner_video("11", "TU HISTORIA", "Formato P (Personal) · humaniza · hace que te elijan a VOS"))
S.append(Spacer(1, 8))

S.append(ficha_tecnica([
    ("Duración", "55-65 segundos"),
    ("Backing", "Ninguno, o un clima muy suave de fondo — casi inaudible bajo la voz"),
    ("Tono", "Bajá un cambio, hablale a un amigo, no a una cámara"),
    ("Por qué existe", "Es el único video del stock que responde \"¿por qué vos?\" — la objeción "
                       "principal de un producto de USD 400-900 comprado a un desconocido"),
]))
S.append(Spacer(1, 6))

S.append(Paragraph("LOS 6 DATOS REALES (la base de este guion)", H2))
S.append(Paragraph(
    "Empezaste a los <b>once años</b>. Aprendiste de todas las formas posibles: TAB de internet, "
    "videos, profesor particular, y hasta la <b>facultad de música en Rosario (UNR)</b> — no te "
    "recibiste, pero aprendiste muchísimo ahí. Tu Punto A fue años tocando siempre las mismas frases, "
    "<b>a pesar</b> de todo ese estudio formal. El quiebre fue un profesor puntual que te enseñó a "
    "<b>conectar el mástil en vez de memorizar cajas sueltas</b> — el germen exacto del Hito 1, "
    "\"El Mapa\", de tu propio método. Y lo que cambió fue que empezaste a <b>improvisar con libertad, "
    "sin depender de licks memorizados</b>.", BODY))
S.append(Paragraph(
    "El dato de la facultad es un activo, no un detalle menor: \"estudié formalmente y AUN ASÍ me "
    "pasaba esto\" es un argumento de autoridad mucho más fuerte que \"no estudié nada\". No lo "
    "minimices ni te disculpes por no haberte recibido — contalo tal cual, con naturalidad.", SMALL))

S.append(Spacer(1, 8))
S.append(Paragraph("LÍNEA DE TIEMPO", H2))
S.append(linea_tiempo([
    ("0:00–0:06", "A cámara, sin guitarra colgada o con ella quieta. Plano cerrado, mirada directa.",
     "\"Empecé a tocar la guitarra a los once años. Y durante mucho tiempo pensé que el problema era "
     "que me faltaba talento.\""),
    ("0:06–0:22", "Seguís a cámara, tono neutro — es un repaso rápido, no dramático.",
     "\"Pasé por todo lo que puede pasar un guitarrista: aprendí con tablaturas de internet, con "
     "videos, tuve profesores particulares, y hasta estudié en la facultad de música en Rosario. No "
     "me recibí, pero aprendí un montón ahí. Y aun así — con todo eso encima — durante años seguí "
     "tocando las mismas frases de siempre. Sabía un montón de teoría. Pero cuando improvisaba, "
     "sonaba siempre igual.\""),
    ("0:22–0:38", "Podés mostrar la guitarra brevemente acá, sin tocar todavía.",
     "\"Lo que cambió todo fue un profesor que, en vez de enseñarme una caja más, me enseñó a "
     "conectar el mástil entero. Ahí entendí que el problema nunca fueron las notas que me faltaban "
     "— era que tenía cinco cajas separadas en la cabeza, en vez de un solo mapa.\""),
    ("0:38–0:50", "A cámara, tono más liviano — ya pasaste la parte difícil del relato.",
     "\"Desde ese día empecé a improvisar con libertad de verdad — sin depender de licks memorizados, "
     "moviéndome por donde se me ocurriera en el momento. Eso es lo que antes no podía hacer.\""),
    ("0:50–0:60", "A cámara, tranquilo, casi charlando.",
     "\"Por eso armé este método así, empezando siempre por el mapa completo del mástil — es lo que "
     "a mí me cambió la cabeza, y quiero ahorrarte los años que me llevó a mí entenderlo. Si estás en "
     "el mismo lugar donde yo estaba, escribime SOLO y te cuento cómo trabajamos.\""),
], colw=[2.0 * cm, W * 0.30, W - 2.0 * cm - W * 0.30]))

S.append(Spacer(1, 6))
S.append(Paragraph("GUÍA DE TONO", H2))
S.append(Paragraph(
    "Ensayalo contándoselo a una persona real (pareja, amigo guitarrista) antes de prender la cámara: "
    "si a esa persona le genera algo, funciona. Si te queda \"de guion\", volvé a contarlo con tus "
    "palabras — la línea de tiempo te da la idea de cada bloque, no hace falta decirla textual. "
    "No necesitás tocar la guitarra en este video — si tocás algo, que sea al final, breve, sin ser el foco.", BODY))

S.append(Paragraph("COPY DEL POST", H2))
S.append(Paragraph(
    "<i>\"Empecé a tocar a los once años. Pasé por tablaturas de internet, videos, profesores "
    "particulares, y hasta la facultad de música — no me recibí, pero aprendí muchísimo ahí. Y con "
    "todo eso encima, durante años seguí tocando las mismas frases de siempre. Lo que me cambió la "
    "cabeza fue un profesor que me enseñó a conectar el mástil entero, en vez de memorizar cajas "
    "sueltas. Ahí empecé a improvisar de verdad, con libertad. Por eso armé mi método empezando "
    "siempre por ahí: el mapa completo. Quiero ahorrarte los años que a mí me llevó entenderlo. "
    "Si te sentís identificado, escribime SOLO.\"</i>", BODY))

S.append(Paragraph("HASHTAGS", H3))
S.append(Paragraph("#guitarra #guitarraelectrica #aprenderguitarra #historiapersonal #rock #bluesrock #guitarristas", SMALL))

S.append(Paragraph("NOTA DE EDICIÓN", H3))
S.append(Paragraph(
    "Subtítulos SIEMPRE (es el video que más se comparte a pantalla apagada). Sin efectos, sin memes, "
    "sin zooms bruscos — cualquier adorno visual le resta verdad a este video.", SMALL))

# ============================================================ VIDEO 12 — FIJADO
S.append(PageBreak())
S.append(banner_video("12", "REEL FIJADO", "Formato A (Autoridad) · sin hablar · la carta de presentación del perfil"))
S.append(Spacer(1, 8))

S.append(ficha_tecnica([
    ("Duración", "25-35 segundos"),
    ("Backing", "El mejor que tengas armado — vale grabarlo especial para esto, no reciclar otro"),
    ("Tono", "Ninguno: no hablás, solo tocás"),
    ("Por qué existe", "Es el primer video que ve cualquiera que entra al perfil por curiosidad. "
                       "Su único trabajo: que piensen \"éste sabe\" y se queden a mirar el resto"),
]))
S.append(Spacer(1, 6))

S.append(Paragraph(
    "No es un guion hablado — es una <b>partitura emocional</b>. Misma estructura de 4 frases que ya "
    "usás en el ejercicio 16 del Hito 1 y el ejercicio 45 del Hito 3: <b>presenta → desarrolla → clímax "
    "→ cierra</b>.", BODY))

S.append(Paragraph("LÍNEA DE TIEMPO", H2))
S.append(linea_tiempo([
    ("0:00–0:06", "PRESENTA. Plano cerrado en tus manos. Arrancás tocando — sin hook de texto, sin cara.",
     "Frase grave y simple, en caja 1 o caja 5. Pocas notas, con espacio. No se busca enganchar con "
     "velocidad: se busca que desde el segundo 1 se escuche control e intención."),
    ("0:06–0:14", "DESARROLLA. La cámara puede abrirse a un plano más amplio (cara + manos).",
     "La misma idea, un escalón más arriba (caja 2 o 3). Acá entra el primer bending con vibrato "
     "sostenido: el momento que separa \"sabe tocar\" de \"solo sabe las notas\"."),
    ("0:14–0:24", "CLÍMAX. El punto más agudo e intenso de todo el reel.",
     "Subís con un slide a caja 4, aumentás la dinámica (más fuerte, más densidad de notas) durante "
     "3-4 segundos MÁXIMO — más que eso cansa — y después bajás."),
    ("0:24–0:30", "CIERRA. Bajás, aflojás, cerrás en la tónica con vibrato. Plano final: tu cara "
                  "relajada, sin decir nada.",
     "Silencio de 1 segundo después de la última nota antes de cortar — es parte del reel, no cortes "
     "en seco."),
], colw=[2.0 * cm, W * 0.40, W - 2.0 * cm - W * 0.40]))

S.append(Spacer(1, 6))
S.append(Paragraph("ELEMENTOS NO NEGOCIABLES", H2))
S.append(tabla([
    [Paragraph("<b>Regla</b>", CELLB), Paragraph("<b>Por qué</b>", CELLB)],
    [Paragraph("Cero texto en pantalla", CELL),
     Paragraph("Ningún hook, ningún CTA, ninguna palabra. Solo tu usuario de Instagram, chico y discreto "
               "en una esquina — por si alguien lo repostea sin el contexto del perfil.", CELL)],
    [Paragraph("Sonido limpio", CELL),
     Paragraph("Es el video donde el AUDIO importa más que en cualquier otro. Invertí el tiempo que "
               "haga falta en que la guitarra se escuche bien grabada, sin compresión agresiva.", CELL)],
    [Paragraph("Se re-graba cada 3-6 meses", CELL),
     Paragraph("A diferencia de los demás, tiene sentido actualizarlo: es tu carta de presentación en "
               "tiempo presente, no un archivo histórico.", CELL)],
], [3.6 * cm, W - 3.6 * cm]))

S.append(Paragraph("COPY DEL POST (mínimo, casi no hace falta)", H3))
S.append(Paragraph("<i>[Nombre del programa] · @felibayamenor</i>", SMALL))

S.append(Paragraph("NOTA DE EDICIÓN", H3))
S.append(Paragraph(
    "Sin transiciones, sin efectos de sonido, sin música de fondo que compita con la guitarra. Es el "
    "único video de todo el stock donde \"menos producción\" ES la producción correcta.", SMALL))

# ============================================================ VENDEDOR 1 — "COMO QUE DESAPARECE"
S.append(PageBreak())
S.append(banner_video("V1", "VENDEDOR — \"COMO QUE DESAPARECE\"",
                      "Conversión pura · a cámara, sin tocar · keyword: SABOR"))
S.append(Spacer(1, 8))

S.append(ficha_tecnica([
    ("Duración", "30-35 segundos"),
    ("Backing", "Ninguno, o mínimo — el poder está en la mirada, no en la música"),
    ("Tono", "El viewer se tiene que sentir LEÍDO. Cualquier adorno lo diluye"),
    ("Cuándo publicarlo", "Recién cuando ya haya autoridad construida — después de 5-6 Formato C, "
                         "NUNCA como primer contenido (regla de la sección 9)"),
    ("Origen", "Adaptado de un guion de venta directa de jazz que identificaste como el que más "
              "convierte. Mecánica: espejo del dolor → sacar la culpa → nombrar la solución sin "
              "regalarla → puerta con keyword"),
]))
S.append(Spacer(1, 6))

S.append(Paragraph("LÍNEA DE TIEMPO", H2))
S.append(linea_tiempo([
    ("0:00–0:10", "A cámara todo el tiempo. Sin guitarra, o con la viola colgada sin tocar. "
                  "Subtítulos grandes.",
     "\"Mirás tutoriales, guardás licks, sacás los solos de tus ídolos… pero cuando improvisás, "
     "nada de eso aparece.\""),
    ("0:10–0:20", "Seguís a cámara, tono de espejo — no acusador.",
     "\"Le dedicaste un montón de horas — y en el momento de tocar, terminás metido en la misma "
     "caja de siempre, con las mismas frases de siempre. Como si todo lo que estudiaste no "
     "existiera. Como que desaparece.\""),
    ("0:20–0:30", "A cámara, ahora ofreciendo, no señalando.",
     "\"Y mirá: no necesitás más licks. Tampoco estudiar más horas. Necesitás un sistema que "
     "convierta eso que estudiás en TU forma de tocar — que cuando improvises, salga solo, con "
     "sabor, sin pensarlo.\""),
    ("0:30–0:35", "A cámara, cierre tranquilo, sin apuro.",
     "\"Si querés trabajar en serio, en un proceso paso a paso, para improvisar solos de rock con "
     "la libertad que buscás, mandame SABOR y te cuento cómo trabajamos.\""),
], colw=[2.0 * cm, W * 0.32, W - 2.0 * cm - W * 0.32]))

S.append(Spacer(1, 6))
S.append(Paragraph("DECISIONES DE ADAPTACIÓN (por qué funciona)", H2))
S.append(tabla([
    [Paragraph("<b>Elemento</b>", CELLB), Paragraph("<b>Por qué</b>", CELLB)],
    [Paragraph("\"La misma caja de siempre\"", CELL),
     Paragraph("Reemplaza \"los mismos recursos\" del original. La caja 1 es la cárcel CON NOMBRE "
               "del avatar — una imagen física que reconoce al instante.", CELL)],
    [Paragraph("\"Como que desaparece\"", CELL),
     Paragraph("Se roba casi textual del guion original: es la frase más potente, describe la "
               "experiencia exacta de improvisar y quedarse en blanco.", CELL)],
    [Paragraph("La CTA no regala nada", CELL),
     Paragraph("No es un lead magnet: abre conversación de método directo. Por eso es el que "
               "vende — atrae al 3% listo para comprar (regla 97/3), no a curiosos.", CELL)],
], [3.6 * cm, W - 3.6 * cm]))

S.append(Paragraph("VERSIÓN CORTA (para story o pie de otro reel)", H3))
S.append(Paragraph(
    "<i>\"Guardás licks que después nunca aparecen cuando improvisás. El problema no es cuánto "
    "estudiás — es que nada lo conecta. No necesitás más material: necesitás un sistema. Mandame "
    "SABOR y te cuento cómo trabajamos.\"</i>", BODY))

S.append(Paragraph("NOTA DE EDICIÓN", H3))
S.append(Paragraph(
    "Sin música o backing mínimo. Sin memes, sin zooms. La fuerza está en la mirada sostenida a "
    "cámara — cualquier corte o efecto rompe la sensación de que te está hablando a VOS.", SMALL))

# ============================================================ VENDEDOR 2 — "DEJÁ DE MIRAR TUTORIALES"
S.append(PageBreak())
S.append(banner_video("V2", "VENDEDOR — \"DEJÁ DE MIRAR TUTORIALES\"",
                      "Espejo, no reto · vos FUISTE ese tipo · keyword: ROCK"))
S.append(Spacer(1, 8))

S.append(ficha_tecnica([
    ("Duración", "40-45 segundos"),
    ("Backing", "Blues en La"),
    ("Tono", "Empático — vos FUISTE ese tipo. Es un espejo, no un reto"),
    ("Particularidad", "El \"mal\" acá no es tocar mal: es el scroll infinito de tutoriales"),
    ("Cuándo publicarlo", "Mismo criterio que el anterior: después de tener autoridad construida"),
]))
S.append(Spacer(1, 6))

S.append(Paragraph("LÍNEA DE TIEMPO", H2))
S.append(linea_tiempo([
    ("0:00–0:04", "HOOK, a cámara.",
     "\"¿Cuántos tutoriales de guitarra miraste este mes? ¿Veinte? ¿Cincuenta? ¿Y tu improvisación "
     "mejoró algo? Sé honesto.\""),
    ("0:04–0:12", "EL \"MAL\" — el espejo, no tocás: mostrás. Visual: feed lleno de tutoriales o "
                  "carpeta de guardados, scrolleando. Labels: \"200 licks guardados\" · \"0 solos "
                  "propios\". Sin guitarra sonando: backing tenso bajito o silencio con clicks de scroll.",
     "\"Yo era ese tipo. Guardaba licks, miraba análisis de solos, cursos, más licks… Sabía un "
     "montón. Y cuando agarraba la viola para improvisar… seguía sonando igual que hace dos años.\""),
    ("0:12–0:18", "REVELACIÓN, a cámara.",
     "\"El problema no es que te falte información. Es que te SOBRA. Acumulás 'qués' sin un "
     "'cómo'. Mirá lo que hacen 20 minutos bien diseñados.\""),
    ("0:18–0:32", "EL \"BIEN\" — tocás, poco hablado encima. Improvisás 12-14 seg sobre el backing, "
                  "con sabor. Labels secuenciales: \"20 min por día\" · \"una sola cosa por semana\" "
                  "· \"con un orden\".",
     "\"Esto no salió de mirar videos. Salió de practicar UNA cosa por vez, con un orden.\""),
    ("0:32–0:40", "CIERRE, a cámara.",
     "\"No necesitás más tutoriales. Necesitás menos información y más dirección. Veinte minutos "
     "por día con un plan le ganan a cuatro horas de scroll. Siempre.\""),
    ("0:40–0:45", "CTA.",
     "\"Comentá ROCK y te mando tres licks con sabor — pero con el CÓMO practicarlos, no el lick "
     "pelado.\""),
], colw=[2.0 * cm, W * 0.38, W - 2.0 * cm - W * 0.38]))

S.append(Spacer(1, 6))
S.append(Paragraph("GUÍA DE TONO", H2))
S.append(Paragraph(
    "Este video es un ESPEJO, no un reto. El viewer se tiene que sentir <b>entendido</b>, no "
    "acusado. Por eso arrancás con \"yo era ese tipo\" — te ponés adentro del problema antes de "
    "señalarlo. El copy del post podés reusar el COPY MAESTRO de la sección 12 del documento "
    "(fue escrito exactamente para esta creencia), cambiando solo el CTA final a ROCK.", BODY))

S.append(Paragraph("NOTA DE EDICIÓN", H3))
S.append(Paragraph(
    "En el \"mal\" no hay guitarra sonando — meté un backing tenso bajito o silencio incómodo con "
    "el sonido del scroll (clicks). El contraste acá es scroll muerto vs guitarra viva.", SMALL))

S.append(Paragraph("HASHTAGS", H3))
S.append(Paragraph("#guitarra #guitarraelectrica #aprenderguitarra #tutorialguitarra #solodeguitarra #rock #bluesrock #pentatonica #guitarristas #practicarguitarra", SMALL))

# ============================================================ CIERRE
S.append(PageBreak())
S.append(Paragraph("CHECKLIST ANTES DE FILMAR", H1))
S.append(tabla([
    [Paragraph("<b>Video</b>", CELLB), Paragraph("<b>Lo tengo listo cuando…</b>", CELLB)],
    [Paragraph("11 · Historia", CELLB),
     Paragraph("Ensayé el relato en voz alta con otra persona al menos una vez, con los 6 datos reales.", CELL)],
    [Paragraph("12 · Fijado", CELLB),
     Paragraph("Tengo la frase de las 4 partes ensayada y sé exactamente qué toco en cada tramo, sin dudar.", CELL)],
    [Paragraph("V1 · Como que desaparece", CELLB),
     Paragraph("Puedo sostener la mirada a cámara los 30 segundos sin cortar ni desviar la vista.", CELL)],
    [Paragraph("V2 · Dejá de mirar tutoriales", CELLB),
     Paragraph("Tengo el backing de blues en La listo y practiqué la frase del \"bien\" (12-14 seg con sabor).", CELL)],
], [3.8 * cm, W - 3.8 * cm]))

S.append(Spacer(1, 10))
S.append(caja_oscura(
    '<font color="white" size="10.5"><b>Recordá el orden y la regla de los vendedores</b></font><br/>'
    '<font color="#f7d7d2" size="9">Historia primero (más ensayo, más carga emocional) → Fijado segundo '
    '(el más simple, para descomprimir) → un vendedor al final. Los vendedores se FILMAN ahora pero se '
    'PUBLICAN recién después de 5-6 Formato C — nunca como primer contenido. · %s</font>' % IG, W))

doc.build(S)
print("OK Guiones-Historia-Fijado-Vendedores.pdf")
