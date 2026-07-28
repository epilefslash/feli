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

doc = documento("Guiones-Historia-Fijado-Clase.pdf",
                "3 GUIONES PENDIENTES",
                "Tu historia · Reel fijado · Cómo es una clase — con línea de tiempo",
                "Solo con Sabor · Guiones — Historia, Fijado, Clase",
                "Guiones - Historia, Fijado, Clase")
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
    t = Table([[Paragraph('<font color="white" size="14"><b>VIDEO #%s</b></font><br/>'
                          '<font color="white" size="12"><b>%s</b></font><br/>'
                          '<font color="#f7d7d2" size="9">%s</font>' % (numero, titulo, subtitulo),
                          BODY)]], colWidths=[W])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), RED),
                           ('LEFTPADDING', (0, 0), (-1, -1), 12), ('RIGHTPADDING', (0, 0), (-1, -1), 12),
                           ('TOPPADDING', (0, 0), (-1, -1), 9), ('BOTTOMPADDING', (0, 0), (-1, -1), 9)]))
    return t


# ============================================================ PORTADA
S.append(Paragraph("LOS 3 VIDEOS QUE FALTAN PARA COMPLETAR EL STOCK", H1))
S.append(Paragraph(
    "De los 8 videos filmados, 6 son creencias atacadas. Ninguno responde <b>\"¿por qué vos?\"</b> "
    "ni <b>\"¿qué compro exactamente?\"</b> — las dos objeciones que más frenan una venta de "
    "USD 400-900 a un desconocido de Instagram. Estos tres videos cierran esas dos grietas.", BODY))
S.append(tabla([
    [Paragraph("<b>#</b>", CELLB), Paragraph("<b>Video</b>", CELLB), Paragraph("<b>Función</b>", CELLB),
     Paragraph("<b>Duración</b>", CELLB)],
    [Paragraph("11", CELLB), Paragraph("TU HISTORIA", CELL),
     Paragraph("Responde \"¿por qué vos?\" — te humaniza, te vuelve la opción elegida.", CELL),
     Paragraph("55-65 seg", CELL)],
    [Paragraph("12", CELLB), Paragraph("REEL FIJADO", CELL),
     Paragraph("La carta de presentación del perfil. Prueba de que sabés tocar.", CELL),
     Paragraph("25-35 seg", CELL)],
    [Paragraph("13", CELLB), Paragraph("CÓMO ES UNA CLASE", CELL),
     Paragraph("Responde \"¿qué compro?\" — muestra el producto real, no la promesa.", CELL),
     Paragraph("40-50 seg", CELL)],
], [1.1 * cm, 3.6 * cm, W - 6.6 * cm, 1.9 * cm]))

S.append(Paragraph("ORDEN DE FILMACIÓN SUGERIDO", H2))
S.append(Paragraph(
    "<b>1º Historia</b> — es el que necesita más tranquilidad emocional y el que más ensayo pide, "
    "conviene sacarlo de encima primero. <b>2º Fijado</b> — el más simple: solo tocar bien, sin hablar, "
    "buen día para relajar después del esfuerzo del anterior. <b>3º Clase</b> — se beneficia de grabarse "
    "el mismo día que Historia, con el mismo ánimo genuino ya activado, y necesita tener a mano el "
    "cuadernillo impreso o en pantalla.", BODY))

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
    ("Tono", "El más importante de los 3. Bajá un cambio, hablale a un amigo, no a una cámara"),
    ("Por qué existe", "Es el único video del stock que responde \"¿por qué vos?\" — la objeción "
                       "principal de un producto de USD 400-900 comprado a un desconocido"),
]))
S.append(Spacer(1, 6))

S.append(Paragraph("ANTES DE GRABAR: completá estos 6 blancos con TU historia real", H2))
S.append(Paragraph(
    "La estructura y el arco emocional ya están resueltos abajo — eso no cambia. Pero los hechos son "
    "tuyos: no los inventé porque no los conozco, y no tendría sentido que lo haga. Contestá cada uno "
    "en voz alta, grabándote sin cámara, antes de armar la versión final del guion.", BODY))
S.append(tabla([
    [Paragraph("<b>#</b>", CELLB), Paragraph("<b>Pregunta</b>", CELLB)],
    [Paragraph("1", CELLB), Paragraph("¿A qué edad / hace cuántos años empezaste a tocar?", CELL)],
    [Paragraph("2", CELLB), Paragraph("¿Cómo aprendiste — solo, con profesor, mirando videos?", CELL)],
    [Paragraph("3", CELLB), Paragraph("¿Cuál es TU versión de \"vivir en la caja 1\"? (años tocando lo mismo, "
                                       "un show que salió mal, comparación con otro guitarrista que te frenó)", CELL)],
    [Paragraph("4", CELLB), Paragraph("¿Cuál fue el quiebre — un profesor, un video, una frase, una devolución?", CELL)],
    [Paragraph("5", CELLB), Paragraph("¿Qué cambió en tu forma de tocar (y de sentir la guitarra) después de eso?", CELL)],
    [Paragraph("6", CELLB), Paragraph("¿Por qué enseñás esto ahora? ¿Qué te gustaría que alguien te hubiera "
                                       "dicho a vos hace años?", CELL)],
], [1.0 * cm, W - 1.0 * cm]))

S.append(Spacer(1, 8))
S.append(Paragraph("LÍNEA DE TIEMPO", H2))
S.append(linea_tiempo([
    ("0:00–0:06", "A cámara, sin guitarra colgada o con ella quieta. Plano cerrado, mirada directa.",
     "\"Hace [BLANCO 1] años yo tocaba exactamente como vos tocás ahora. Y durante mucho tiempo pensé "
     "que el problema era que me faltaba talento.\""),
    ("0:06–0:20", "Seguís a cámara, tono más bajo, como confesando algo.",
     "[BLANCO 3 — contá tu versión concreta: un lugar, una fecha, una sensación física. Cuanto más "
     "concreto, más se identifica el que mira.] \"Sabía las notas. Sabía las escalas. Pero cuando tenía "
     "que improvisar de verdad, sonaba a alumno, no a músico. Y no entendía por qué.\""),
    ("0:20–0:35", "Podés mostrar la guitarra brevemente acá, sin tocar todavía.",
     "\"Lo que cambió fue [BLANCO 4]. Ahí entendí algo que nadie me había dicho antes: no me faltaban "
     "notas. Me faltaba [espacio / sabor / orden — elegí el término que resuene con tu historia].\""),
    ("0:35–0:48", "A cámara, tono más liviano — ya pasaste la parte difícil del relato.",
     "[BLANCO 5 — qué cambió realmente, simple y creíble. No hace falta que sea espectacular: "
     "\"empecé a tocar cosas que antes ni intentaba\" alcanza y suena honesto.]"),
    ("0:48–0:60", "A cámara, tranquilo, casi charlando.",
     "\"Por eso armé este método: para ahorrarte los años que yo tardé en darme cuenta. [BLANCO 6, en "
     "una frase corta.] Si estás en el mismo lugar donde yo estaba, escribime SOLO y te cuento cómo "
     "trabajamos.\""),
], colw=[2.0 * cm, W * 0.32, W - 2.0 * cm - W * 0.32]))

S.append(Spacer(1, 6))
S.append(Paragraph("GUÍA DE TONO", H2))
S.append(Paragraph(
    "Se graba UNA VEZ que tengas los 6 blancos escritos en un papel, no memorizados palabra por palabra — "
    "leer de memoria sin naturalidad arruina justo lo que este video necesita transmitir. Ensayá "
    "contándoselo a una persona real (pareja, amigo guitarrista) antes de prender la cámara: si a esa "
    "persona le genera algo, funciona. Si te queda \"de guion\", volvé a contarlo con tus palabras. "
    "No necesitás tocar la guitarra en este video — si tocás algo, que sea al final, breve, sin ser el foco.", BODY))

S.append(Paragraph("COPY DEL POST", H2))
S.append(Paragraph(
    "<i>\"No arranqué sabiendo esto. Arranqué exactamente donde estás vos ahora — [resumen de 1 línea "
    "de tu Punto A]. Tardé [BLANCO 1] años en entender lo que te puedo enseñar en 90 días. Esa es la "
    "única razón por la que armé este método: no quiero que nadie tarde lo que tardé yo. Si te sentís "
    "identificado, escribime SOLO.\"</i>", BODY))

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

# ============================================================ VIDEO 13 — CLASE
S.append(PageBreak())
S.append(banner_video("13", "CÓMO ES UNA CLASE", "Formato A/P mixto · resuelve \"¿qué compro?\" · keyword nueva: CLASE"))
S.append(Spacer(1, 8))

S.append(ficha_tecnica([
    ("Duración", "40-50 segundos"),
    ("Backing", "No hace falta — es un video hablado con apoyo visual del cuadernillo"),
    ("Tono", "Orgullo genuino por lo que armaste, sin venta dura"),
    ("Por qué existe", "No estaba en el plan original. Surgió en la auditoría de marketing: nadie que "
                       "ve tus reels sabe qué compra en concreto. Este es el único video que muestra el "
                       "PRODUCTO, no la promesa"),
]))
S.append(Spacer(1, 6))

S.append(Paragraph("LÍNEA DE TIEMPO", H2))
S.append(linea_tiempo([
    ("0:00–0:05", "HOOK, a cámara.",
     "\"¿Cómo es una clase de guitarra en grupo? Te muestro exactamente cómo lo armé.\""),
    ("0:05–0:20", "Cámara en mano o en trípode, mostrás el cuadernillo físico o la pantalla. Podés "
                  "tocar 2 segundos recorriendo las cajas mientras hablás del Hito 1.",
     "\"Son 3 meses, 3 etapas. El mes uno es EL MAPA: te vas de vivir en una sola caja de la pentatónica "
     "a moverte por las cinco, conectadas. El mes dos es EL SABOR: bending, vibrato, el silencio — lo "
     "que hace que la misma escala suene a Gary Moore y no a ejercicio. Y el mes tres es EL VOCABULARIO: "
     "armás tu propio banco de licks y cerrás grabando tu solo.\""),
    ("0:20–0:35", "Ritmo más rápido, casi un listado hablado. A cámara.",
     "\"Cada semana tenés cuatro encuentros en vivo: teoría los lunes, técnica los martes, un solo "
     "icónico los jueves, y el sábado — la que más me gusta — cada uno improvisa y le doy una devolución "
     "personal. Grupo chico: 4 a 6 personas. No sos un número.\""),
    ("0:35–0:45", "Mostrás una página del cuadernillo a cámara, 2-3 segundos — con TAB y partitura "
                  "bien visibles.",
     "\"Y no es solo teoría suelta: tenés cuadernillos con partitura y tablatura de cada ejercicio, con "
     "criterios claros de cuándo ya lo tenés y cuándo seguís practicando. No es una playlist de videos. "
     "Es un método con orden.\""),
    ("0:45–0:50", "A cámara, cierre tranquilo.",
     "\"Si querés ver si encajás en la próxima camada, escribime CLASE y charlamos 15 minutos, sin costo.\""),
], colw=[2.0 * cm, W * 0.36, W - 2.0 * cm - W * 0.36]))

S.append(Spacer(1, 6))
S.append(Paragraph("GUÍA DE TONO", H2))
S.append(Paragraph(
    "Es el único video donde SÍ mostrás material físico o de pantalla — la aplicación directa de la "
    "idea de \"usar el cuadernillo como prueba de método\". No hace falta mostrarlo entero: 2-3 segundos "
    "de una página con TAB y partitura real alcanzan para que se entienda que esto no es contenido "
    "genérico. No hables de precio acá — eso se dice en la llamada, no en el reel. Este video solo tiene "
    "que lograr que alguien quiera agendar esos 15 minutos.", BODY))
S.append(Paragraph(
    "<b>Keyword nueva y distinta de las demás: CLASE</b> (no PENTA, no SOLO, no SABOR) — porque el que "
    "comenta acá ya está más cerca de comprar que el que comenta en un reel de creencia. Sirve para medir "
    "esa diferencia de intención en tus DMs.", BODY))

S.append(Paragraph("COPY DEL POST", H2))
S.append(Paragraph(
    "<i>\"¿Cómo es por dentro un curso de guitarra en grupo?<br/><br/>"
    "3 meses. 3 etapas: el mapa, el sabor, el vocabulario. 4 encuentros en vivo por semana, grupo de "
    "4 a 6 personas, devolución personal cada sábado.<br/><br/>"
    "Y no es solo \\\"clases\\\": tenés material propio, con partitura y tablatura, hecho específicamente "
    "para este método — no reciclado de otro lado.<br/><br/>"
    "Si querés ver si es para vos, escribime <b>CLASE</b> y charlamos 15 minutos, sin costo ni "
    "compromiso.\"</i>", BODY))

S.append(Paragraph("HASHTAGS", H3))
S.append(Paragraph("#guitarra #guitarraelectrica #clasesdeguitarra #aprenderguitarra #metododeguitarra #rock #bluesrock", SMALL))

S.append(Paragraph("NOTA DE EDICIÓN", H3))
S.append(Paragraph(
    "Este es el único video del stock donde vale la pena un plano de \"pantalla\" (mostrando el PDF o "
    "la tablatura) en vez de solo cámara — usalo, es tu diferencial visual más fuerte y hasta ahora no "
    "aparece en ningún reel filmado.", SMALL))

# ============================================================ CIERRE
S.append(PageBreak())
S.append(Paragraph("CHECKLIST ANTES DE FILMAR", H1))
S.append(tabla([
    [Paragraph("<b>Video</b>", CELLB), Paragraph("<b>Lo tengo listo cuando…</b>", CELLB)],
    [Paragraph("11 · Historia", CELLB),
     Paragraph("Completé los 6 blancos por escrito y me lo conté a otra persona en voz alta al menos una vez.", CELL)],
    [Paragraph("12 · Fijado", CELLB),
     Paragraph("Tengo la frase de las 4 partes ensayada y sé exactamente qué toco en cada tramo, sin dudar.", CELL)],
    [Paragraph("13 · Clase", CELLB),
     Paragraph("Tengo el cuadernillo impreso o abierto en pantalla, listo para mostrar en el segundo 0:35.", CELL)],
], [3.4 * cm, W - 3.4 * cm]))

S.append(Spacer(1, 10))
S.append(caja_oscura(
    '<font color="white" size="10.5"><b>Recordá el orden</b></font><br/>'
    '<font color="#f7d7d2" size="9">Historia primero (más ensayo, más carga emocional) → Fijado segundo '
    '(el más simple, para descomprimir) → Clase al final, aprovechando el mismo ánimo genuino del primero. '
    'Los tres juntos cierran el stock completo de contenido. · %s</font>' % IG, W))

doc.build(S)
print("OK Guiones-Historia-Fijado-Clase.pdf")
