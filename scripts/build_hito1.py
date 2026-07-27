# -*- coding: utf-8 -*-
"""Cuadernillo HITO 1 — EL MAPA (ejercicios con tablatura y partitura)."""
import struct
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, Image, PageBreak,
                                Flowable, KeepTogether)

LY = "/tmp/claude-0/-home-user-feli/d22a8506-1d7e-5c6f-914f-42d1d90cdfde/scratchpad/ly"
OUT = "/home/user/feli/Cuadernillo-Hito1-El-Mapa-EJERCICIOS.pdf"
IG = "@felibayamenor"

# Fuente auxiliar solo para simbolos que Helvetica no tiene (negra, flecha, casilla)
pdfmetrics.registerFont(TTFont('Sym', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
NEGRA = '<font name="Sym">♩</font>'
FLECHA = '<font name="Sym">→</font>'
CAJ = '<font name="Sym" size="11">☐</font>'

RED = colors.HexColor("#c0392b")
DARK = colors.HexColor("#2c3e50")
GREY = colors.HexColor("#777777")
LIGHT = colors.HexColor("#f5f0ec")
LIGHT2 = colors.HexColor("#fdf6f5")
BORDER = colors.HexColor("#ddcfc9")
WOOD = colors.HexColor("#e8ded6")

H1 = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=15.5, leading=19,
                    textColor=RED, spaceBefore=2, spaceAfter=6)
H2 = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=12, leading=15.5,
                    textColor=RED, spaceBefore=10, spaceAfter=4)
H3 = ParagraphStyle('H3', fontName='Helvetica-Bold', fontSize=10.5, leading=13.5,
                    textColor=DARK, spaceBefore=8, spaceAfter=2)
BODY = ParagraphStyle('BODY', fontName='Helvetica', fontSize=9.5, leading=13.2,
                      textColor=DARK, spaceAfter=4)
SMALL = ParagraphStyle('SMALL', fontName='Helvetica-Oblique', fontSize=8.5, leading=11.5,
                       textColor=GREY, spaceAfter=3)
CELL = ParagraphStyle('CELL', fontName='Helvetica', fontSize=9, leading=12, textColor=DARK)
CELLB = ParagraphStyle('CELLB', fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=RED)

# ---------------------------------------------------------------- datos del mastil
PENTA = {
    1: [0, 3, 5, 8, 10, 12, 15, 17],
    2: [1, 3, 5, 8, 10, 13, 15, 17],
    3: [2, 5, 7, 9, 12, 14, 17],
    4: [0, 2, 5, 7, 10, 12, 14, 17],
    5: [0, 3, 5, 7, 10, 12, 15, 17],
    6: [0, 3, 5, 8, 10, 12, 15, 17],
}
TONICAS = {1: [5, 17], 2: [10], 3: [14], 4: [7], 5: [12], 6: [5, 17]}
CUERDAS = ["Mi", "La", "Re", "Sol", "Si", "Mi"]      # de la 6a (abajo) a la 1a (arriba)

CAJAS = {
    1: {"rango": (4, 9),  "notas": {6: [5, 8], 5: [5, 7], 4: [5, 7], 3: [5, 7], 2: [5, 8], 1: [5, 8]}},
    2: {"rango": (6, 11), "notas": {6: [8, 10], 5: [7, 10], 4: [7, 10], 3: [7, 9], 2: [8, 10], 1: [8, 10]}},
    3: {"rango": (8, 14), "notas": {6: [10, 12], 5: [10, 12], 4: [10, 12], 3: [9, 12], 2: [10, 13], 1: [10, 12]}},
    4: {"rango": (11, 16), "notas": {6: [12, 15], 5: [12, 15], 4: [12, 14], 3: [12, 14], 2: [13, 15], 1: [12, 15]}},
    5: {"rango": (1, 6),  "notas": {6: [3, 5], 5: [3, 5], 4: [2, 5], 3: [2, 5], 2: [3, 5], 1: [3, 5]}},
}
CAJA_RANGO_REAL = {1: (5, 8), 2: (7, 10), 3: (9, 13), 4: (12, 15), 5: (2, 5)}


def _mastil(c, x0, y0, w, hs, f0, nf, nut=False):
    """Dibuja el fondo, trastes, cuerdas. Devuelve el ancho de traste."""
    fw = w / nf
    top = y0 + hs * 5
    c.setFillColor(WOOD)
    c.rect(x0, y0, w, hs * 5, fill=1, stroke=0)
    c.setStrokeColor(colors.HexColor("#b3a79e"))
    c.setLineWidth(0.7)
    for i in range(nf + 1):
        c.line(x0 + i * fw, y0, x0 + i * fw, top)
    if nut:
        c.setLineWidth(3.2)
        c.setStrokeColor(DARK)
        c.line(x0, y0, x0, top)
    c.setStrokeColor(colors.HexColor("#8d8078"))
    for s in range(6):
        c.setLineWidth(0.4 + s * 0.13)
        c.line(x0, y0 + s * hs, x0 + w, y0 + s * hs)
    return fw


def _nota(c, x, y, es_tonica, r=4.3):
    if es_tonica:
        c.setFillColor(RED)
        c.circle(x, y, r, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 5.4)
        c.drawCentredString(x, y - 1.9, "A")
    else:
        c.setFillColor(DARK)
        c.circle(x, y, r - 0.5, fill=1, stroke=0)


class Diagrama(Flowable):
    """Diagrama de una caja: cuerdas = filas, trastes = columnas."""

    PAD_L, PAD_R, PAD_B, PAD_T = 24, 6, 14, 15

    def __init__(self, caja, width, hs=11.0):
        Flowable.__init__(self)
        self.caja, self.width, self.hs = caja, width, hs
        self.f0, f1 = CAJAS[caja]["rango"]
        self.nf = f1 - self.f0
        self.height = hs * 5 + self.PAD_B + self.PAD_T

    def draw(self):
        c = self.canv
        x0, y0 = self.PAD_L, self.PAD_B
        w = self.width - self.PAD_L - self.PAD_R
        fw = _mastil(c, x0, y0, w, self.hs, self.f0, self.nf, nut=(self.f0 == 0))
        top = y0 + self.hs * 5

        c.setFillColor(GREY)
        c.setFont("Helvetica", 6.5)
        for i in range(self.nf):
            c.drawCentredString(x0 + (i + 0.5) * fw, y0 - 9, str(self.f0 + i + 1))
        c.setFont("Helvetica-Bold", 6.5)
        for s, nombre in enumerate(CUERDAS):
            c.drawRightString(x0 - 4, y0 + s * self.hs - 2.2, nombre)

        for cuerda, trastes in CAJAS[self.caja]["notas"].items():
            y = y0 + (6 - cuerda) * self.hs
            for t in trastes:
                if self.f0 < t <= self.f0 + self.nf:
                    _nota(c, x0 + (t - self.f0 - 0.5) * fw, y, t in TONICAS.get(cuerda, []))

        a, b = CAJA_RANGO_REAL[self.caja]
        c.setFillColor(RED)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(x0, top + 4, "CAJA %d  ·  trastes %d a %d" % (self.caja, a, b))


class MapaCompleto(Flowable):
    """Mastil entero (trastes 0 a 17) con las 5 cajas marcadas arriba."""

    PAD_L, PAD_R, PAD_B, PAD_T = 32, 8, 15, 34

    def __init__(self, width, hs=12.0):
        Flowable.__init__(self)
        self.width, self.hs = width, hs
        self.height = hs * 5 + self.PAD_B + self.PAD_T

    def draw(self):
        c = self.canv
        nf = 17
        x0, y0 = self.PAD_L, self.PAD_B
        w = self.width - self.PAD_L - self.PAD_R
        fw = _mastil(c, x0, y0, w, self.hs, 0, nf, nut=True)
        top = y0 + self.hs * 5

        c.setFillColor(GREY)
        c.setFont("Helvetica", 6.5)
        for t in (3, 5, 7, 9, 12, 15, 17):
            c.drawCentredString(x0 + (t - 0.5) * fw, y0 - 9, str(t))
        c.setFont("Helvetica-Bold", 6.5)
        for s, nombre in enumerate(CUERDAS):
            c.drawRightString(x0 - 13, y0 + s * self.hs - 2.2, nombre)

        for cuerda, trastes in PENTA.items():
            y = y0 + (6 - cuerda) * self.hs
            for t in trastes:
                if t > nf:
                    continue
                x = x0 + (t - 0.5) * fw if t > 0 else x0 - 7
                _nota(c, x, y, t in TONICAS.get(cuerda, []), r=4.0)

        # llaves de las cajas, en dos niveles para que no se pisen
        c.setFont("Helvetica-Bold", 7)
        for i, (caja, a, b) in enumerate([(5, 2, 5), (1, 5, 8), (2, 7, 10), (3, 9, 13), (4, 12, 15)]):
            xa, xb = x0 + (a - 1) * fw, x0 + b * fw
            yy = top + 7 + (i % 2) * 14
            c.setStrokeColor(RED)
            c.setLineWidth(1)
            c.line(xa, yy, xb, yy)
            c.line(xa, yy, xa, yy - 3.5)
            c.line(xb, yy, xb, yy - 3.5)
            c.setFillColor(RED)
            c.drawCentredString((xa + xb) / 2, yy + 3, "caja %d" % caja)


# ---------------------------------------------------------------- helpers
def png_size(path):
    return struct.unpack('>II', open(path, 'rb').read(26)[16:24])


def score(name, width):
    p = "%s/%s.cropped.png" % (LY, name)
    w, h = png_size(p)
    return Image(p, width=width, height=width * h / w)


def ejercicio(num, titulo, bajada, name, width, meta=None):
    els = [Paragraph("EJERCICIO %d — %s" % (num, titulo), H3),
           Paragraph(bajada, BODY)]
    if meta:
        els.append(Paragraph(meta, SMALL))
    els += [Spacer(1, 2), score(name, width), Spacer(1, 6)]
    return KeepTogether(els)


def tabla(rows, colWidths, header=True):
    t = Table(rows, colWidths=colWidths)
    st = [('ROWBACKGROUNDS', (0, 1 if header else 0), (-1, -1), [colors.white, LIGHT2]),
          ('GRID', (0, 0), (-1, -1), 0.5, BORDER),
          ('VALIGN', (0, 0), (-1, -1), 'TOP'),
          ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
          ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5)]
    if header:
        st.append(('BACKGROUND', (0, 0), (-1, 0), LIGHT))
    t.setStyle(TableStyle(st))
    return t


def banner(n, titulo, subtitulo, width):
    t = Table([[Paragraph('<font color="white" size="13"><b>SEMANA %d</b></font><br/>'
                          '<font color="white" size="10.5"><b>%s</b></font><br/>'
                          '<font color="#f7d7d2" size="8.5">%s</font>' % (n, titulo, subtitulo),
                          ParagraphStyle('b', fontName='Helvetica', fontSize=10, leading=14))]],
              colWidths=[width])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), RED),
                           ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                           ('TOPPADDING', (0, 0), (-1, -1), 7), ('BOTTOMPADDING', (0, 0), (-1, -1), 7)]))
    return t


def par(flowables, widths):
    t = Table([flowables], colWidths=widths)
    t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'),
                           ('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                           ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
    return t


# ---------------------------------------------------------------- documento
def on_page(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setFillColor(RED)
    canvas.rect(0, h - 62, w, 62, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 17)
    canvas.drawString(2 * cm, h - 34, "HITO 1 — EL MAPA")
    canvas.setFont("Helvetica", 9.5)
    canvas.drawString(2 * cm, h - 49,
                      "Las 5 cajas de la pentatónica menor, conectadas · ejercicios con TAB y partitura")
    canvas.setFont("Helvetica-Bold", 9)
    canvas.drawRightString(w - 2 * cm, h - 42, IG)
    canvas.setFillColor(GREY)
    canvas.setFont("Helvetica", 7.5)
    canvas.drawString(2 * cm, 1.15 * cm, "Solo con Sabor · Hito 1 — El Mapa")
    canvas.drawRightString(w - 2 * cm, 1.15 * cm, "pág. %d" % doc.page)
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(2 * cm, 1.5 * cm, w - 2 * cm, 1.5 * cm)
    canvas.restoreState()


doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm,
                      topMargin=2.85 * cm, bottomMargin=1.85 * cm,
                      title="Hito 1 - El Mapa (ejercicios)", author="Feli")
doc.addPageTemplates([PageTemplate(id='p', frames=[
    Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='f')], onPage=on_page)])
W = doc.width
S = []

# ============================================================ 1. INTRO
S.append(Paragraph("QUÉ VAS A LOGRAR EN ESTOS 30 DÍAS", H2))
S.append(Paragraph(
    "Hoy vivís en la caja 1. La conocés, la repetís, y cuando querés salir de ahí te perdés. "
    "En 4 semanas vas a recorrer el mástil entero con la pentatónica menor <b>sin pensar dónde estás "
    "parado</b>: las 5 cajas dejan de ser 5 dibujos sueltos y pasan a ser <b>un solo mapa</b>. "
    "<b>Entregable del hito:</b> un video tuyo recorriendo las 5 cajas sin pausa y el solo del Ejercicio 16.", BODY))

S.append(Paragraph("LAS 5 REGLAS DEL MES", H2))
S.append(tabla([
    [Paragraph("<b>Regla</b>", CELLB), Paragraph("<b>Por qué</b>", CELLB)],
    [Paragraph("Todo en <b>La menor</b>", CELL),
     Paragraph("Una sola tonalidad los 30 días. Lo que entrenás es el MAPA, no la tonalidad; cambiar de tono ahora te distrae. En el mes 2 lo movés.", CELL)],
    [Paragraph("<b>Metrónomo siempre</b>", CELL),
     Paragraph("Arrancás a 60 BPM en corcheas. Subís de a 5 BPM SOLO cuando te sale 3 veces seguidas sin error.", CELL)],
    [Paragraph("<b>Lento y limpio gana</b>", CELL),
     Paragraph("Si tenés que apurar para llegar, está muy rápido. Tocar rápido con errores entrena los errores.", CELL)],
    [Paragraph("<b>20 minutos por día</b>", CELL),
     Paragraph("Todos los días le gana a 3 horas el domingo. El mástil se fija por repetición espaciada, no por maratón.", CELL)],
    [Paragraph("<b>Decí las tónicas</b>", CELL),
     Paragraph("Cada vez que toques un LA (los puntos rojos), decilo en voz alta. Suena tonto y funciona: fija el mapa.", CELL)],
], [3.4 * cm, W - 3.4 * cm]))

S.append(Paragraph("CÓMO LEER LOS EJERCICIOS", H2))
S.append(Paragraph(
    "Cada ejercicio viene con <b>partitura arriba</b> y <b>tablatura abajo</b>: son lo mismo escrito de dos formas. "
    "En la TAB, las 6 líneas son las 6 cuerdas (la de arriba es la 1ª, el Mi agudo) y los números son los trastes. "
    "Si no leés partitura usá la TAB, y dejá que el pentagrama te enseñe de a poco: mirá solo si la nota sube o baja. "
    "Eso ya te ordena el oído.", BODY))
S.append(tabla([
    [Paragraph("<b>Símbolo</b>", CELLB), Paragraph("<b>Qué es</b>", CELLB), Paragraph("<b>Cómo se toca</b>", CELLB)],
    [Paragraph("línea entre dos números", CELL), Paragraph("Slide", CELL),
     Paragraph("Tocás la primera y te deslizás a la segunda sin levantar el dedo ni volver a puntear.", CELL)],
    [Paragraph('"bend 1 tono"', CELL), Paragraph("Bending", CELL),
     Paragraph("Empujás la cuerda hasta que suene DOS trastes más arriba. Afinado, o no cuenta.", CELL)],
    [Paragraph('"vibrato"', CELL), Paragraph("Vibrato", CELL),
     Paragraph("Movés la cuerda arriba y abajo, parejo. Es tu firma: sin vibrato la nota queda muerta.", CELL)],
    [Paragraph("punto rojo con A", CELL), Paragraph("Tónica (La)", CELL),
     Paragraph("Tu casa. Empezar y terminar frases ahí es lo que hace que suene resuelto.", CELL)],
], [3.2 * cm, 2.4 * cm, W - 5.6 * cm]))

S.append(Paragraph("LA RUTINA DIARIA (20 minutos)", H2))
S.append(tabla([
    [Paragraph("<b>Min</b>", CELLB), Paragraph("<b>Qué</b>", CELLB), Paragraph("<b>Foco</b>", CELLB)],
    [Paragraph("0–5", CELLB), Paragraph("La caja de la semana, ida y vuelta con metrónomo", CELL),
     Paragraph("Limpieza: que suene cada nota, sin cuerdas zumbando.", CELL)],
    [Paragraph("5–10", CELLB), Paragraph("Secuencias / tónicas", CELL),
     Paragraph("Que la mano deje de ir en línea recta y el oído ubique el LA.", CELL)],
    [Paragraph("10–15", CELLB), Paragraph("El lick o el puente de la semana", CELL),
     Paragraph("Acá aparece el sabor: bending, vibrato, slide.", CELL)],
    [Paragraph("15–20", CELLB), Paragraph("<b>Improvisás</b> sobre backing en Lam", CELL),
     Paragraph("Sin papel. Usás SOLO lo de esta semana. Es la parte más importante.", CELL)],
], [1.5 * cm, 6.4 * cm, W - 7.9 * cm]))
S.append(Paragraph(
    "Backing para todo el hito: buscá en YouTube <b>\"slow blues backing track A minor 60 bpm\"</b> o "
    "<b>\"A minor rock backing track\"</b>. Elegí uno con espacio, no uno lleno de notas.", SMALL))

# ============================================================ 2. EL MAPA
S.append(PageBreak())
S.append(Paragraph("EL MAPA COMPLETO (a dónde vamos)", H1))
S.append(Paragraph(
    "Esto es todo el terreno: la pentatónica de La menor en el mástil entero. Los puntos rojos son los LA "
    "(tu casa). Las llaves de arriba marcan las 5 cajas. Fijate en algo: <b>las cajas se pisan entre sí</b> — "
    "comparten notas. Esas notas compartidas son los puentes que vas a usar para cruzar de una a otra.", BODY))
S.append(Spacer(1, 4))
S.append(MapaCompleto(W))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "No intentes memorizar esto hoy. Lo vas a armar de a una caja por semana, y en la semana 4 vas a mirar "
    "este dibujo y te va a resultar obvio.", SMALL))

S.append(Paragraph("EL ORDEN DE LAS 4 SEMANAS", H2))
S.append(tabla([
    [Paragraph("<b>Semana</b>", CELLB), Paragraph("<b>Territorio</b>", CELLB),
     Paragraph("<b>Lo que se suma</b>", CELLB), Paragraph("<b>Ejerc.</b>", CELLB)],
    [Paragraph("1", CELLB), Paragraph("Caja 1 (trastes 5–8)", CELL),
     Paragraph("Tu casa. Las tónicas y el primer lick con sabor.", CELL), Paragraph("1 a 4", CELL)],
    [Paragraph("2", CELLB), Paragraph("Caja 2 (7–10) + puente", CELL),
     Paragraph("El primer cruce. Slide de una caja a la otra.", CELL), Paragraph("5 a 8", CELL)],
    [Paragraph("3", CELLB), Paragraph("Cajas 3 y 4 (9–15)", CELL),
     Paragraph("La zona aguda. Dos cruces más, encadenados.", CELL), Paragraph("9 a 12", CELL)],
    [Paragraph("4", CELLB), Paragraph("Caja 5 (2–5) + todo", CELL),
     Paragraph("Se cierra el círculo. El mástil entero, arriba y abajo.", CELL), Paragraph("13 a 16", CELL)],
], [1.7 * cm, 4.0 * cm, W - 7.6 * cm, 1.9 * cm]))

S.append(Paragraph("LOS 3 ERRORES QUE FRENAN ESTE HITO", H2))
S.append(Paragraph(
    "<b>1. Correr antes de tenerlo limpio.</b> Si a 60 BPM se te escapa una nota, subir el tempo no lo arregla: lo tapa. "
    "Bajá el metrónomo hasta que salga perfecto y desde ahí subí.<br/>"
    "<b>2. Estudiar las cajas como dibujos sueltos.</b> Una caja sola no sirve de nada. Lo que vale son los PUENTES "
    "(ejercicios 7, 11, 12 y 14). Si te salteás esos, vas a saber 5 cajas y vas a seguir sin poder moverte.<br/>"
    "<b>3. No improvisar.</b> Los últimos 5 minutos de la rutina no son opcionales. Si solo repetís ejercicios "
    "entrenás los dedos, pero no la cabeza. La improvisación es donde el mapa se vuelve tuyo.", BODY))

# ============================================================ SEMANA 1
S.append(PageBreak())
S.append(banner(1, "CAJA 1 — tu casa (trastes 5 a 8)",
                "Objetivo: que la caja 1 te salga sin mirar el mástil, y que sepas dónde está el LA.", W))
S.append(Spacer(1, 8))
S.append(par([Diagrama(1, W * 0.52),
              Paragraph("Los tres LA de la caja 1: <b>6ª cuerda traste 5</b>, <b>4ª cuerda traste 7</b> y "
                        "<b>1ª cuerda traste 5</b>. Son las tres puertas de tu casa. Si te perdés en cualquier "
                        "momento del mes, volvés a una de esas tres.<br/><br/>"
                        "Digitación: <b>un dedo por traste</b>. Índice en el 5, anular en el 7, meñique en el 8.", BODY)],
             [W * 0.52, W * 0.48]))
S.append(Spacer(1, 4))

S.append(ejercicio(1, "La caja 1, ida y vuelta", (
    "El motor de todo. Subís las 12 notas y bajás. Púa alternada (abajo–arriba) desde el primer día, "
    "aunque te salga lento. Si una nota suena apagada, pará y arreglá el dedo antes de seguir."),
    "e01", W, "Metrónomo 60 BPM en corcheas. Meta de la semana: 80 BPM limpio, 3 veces seguidas sin error."))

S.append(ejercicio(2, "Las tónicas (dónde está tu casa)", (
    "Tocás cada LA solo, dejándolo sonar los 2 tiempos, y lo decís en voz alta: <i>\"la\"</i>. "
    "En el último compás bajás una frase y <b>resolvés</b> en el LA de la 4ª cuerda. Escuchá cómo esa "
    "nota hace que todo suene terminado: ese es el efecto que vas a buscar toda tu vida."),
    "e02", W, "Con backing en Lam. Sin metrónomo: acá lo que se entrena es el OÍDO, no la mano."))

S.append(ejercicio(3, "Secuencia de a 4 (romper la línea recta)", (
    "Mismo territorio, pero en vez de subir derecho vas y volvés en grupos de cuatro notas. Esto es lo que hace "
    "que tu escala deje de sonar a escala: la mano aprende a cambiar de dirección. Es el ejercicio más aburrido "
    "del cuadernillo y el que más se te va a notar."),
    "e03", W, "60 BPM, meta 75. Si te trabás, hacé solo el primer compás 20 veces antes de seguir."))

S.append(ejercicio(4, "Tu primer lick con sabor", (
    "Cuatro tiempos de música de verdad. El <b>bending de 1 tono</b> va en la 3ª cuerda traste 7: empujás hasta "
    "que suene igual que el traste 9. Compará: tocá el 9, escuchalo, después bendeá el 7 hasta que suene "
    "idéntico. El <b>vibrato</b> del final es lo que separa a un alumno de un guitarrista: movelo parejo, sin apuro."),
    "e04", W, "Repetilo 10 veces por día toda la semana. Grabate el viernes y escuchá si el bending llega afinado."))

# ============================================================ SEMANA 2
S.append(PageBreak())
S.append(banner(2, "CAJA 2 + EL PRIMER PUENTE (trastes 7 a 10)",
                "Objetivo: sumar territorio nuevo y cruzar de la caja 1 a la 2 sin frenar.", W))
S.append(Spacer(1, 8))
S.append(par([Diagrama(2, W * 0.52),
              Paragraph("La caja 2 arranca donde termina la 1: <b>comparten los trastes 7 y 8</b>. No es un dibujo "
                        "nuevo que aprendés de cero, es la continuación del mismo mapa.<br/><br/>"
                        "Sus tónicas son la <b>4ª cuerda traste 7</b> (la misma de la caja 1 — ese es el puente) "
                        "y la <b>2ª cuerda traste 10</b>.", BODY)],
             [W * 0.52, W * 0.48]))
S.append(Spacer(1, 4))

S.append(ejercicio(5, "La caja 2, ida y vuelta", (
    "Mismo trabajo que el ejercicio 1, territorio nuevo. Ojo con la 3ª cuerda: acá los trastes son 7 y 9 "
    "(no 7 y 10). Es la irregularidad de la escala en esa cuerda, y es donde todos se equivocan."),
    "e05", W, "60 BPM, meta 80. Antes de arrancar tocá el ejercicio 1 una vez, para sentir de dónde venís."))

S.append(ejercicio(6, "Las tónicas de la caja 2", (
    "Dos LA nuevos que ubicar. El de la 4ª cuerda traste 7 ya lo conocías de la caja 1: <b>ese es el puente</b>. "
    "Una misma nota que pertenece a las dos cajas. Ahí es donde vas a cruzar."),
    "e06", W, "Con backing. Decí \"la\" en voz alta cada vez, igual que en la semana 1."))

S.append(ejercicio(7, "EL PUENTE — de la caja 1 a la caja 2", (
    "El ejercicio más importante del mes. Subís por la caja 1 y al llegar a la 1ª cuerda hacés un "
    "<b>slide del traste 8 al 10</b>: ya estás en la caja 2, y bajás por ahí. Un solo movimiento, sin frenar, "
    "sin mirar. El slide no es un adorno: es el vehículo que te lleva de una zona a la otra."),
    "e07", W, "60 BPM. Cuando salga, probá el mismo cruce en la 2ª cuerda (8 a 10) y en la 3ª (7 a 9): es la misma idea."))

S.append(ejercicio(8, "Un lick que cruza las dos cajas", (
    "Acá se junta todo: bending en la caja 1, slide al medio, y el vibrato final ya en la caja 2. "
    "Cuando puedas tocar esto sin pensarlo dejaste de tener dos cajas: tenés una sola zona de 6 trastes."),
    "e08", W, "Repetilo 10 veces por día. Después improvisá 5 minutos usando SOLO estas dos cajas."))

# ============================================================ SEMANA 3
S.append(PageBreak())
S.append(banner(3, "CAJAS 3 Y 4 — la zona aguda (trastes 9 a 15)",
                "Objetivo: dos cajas nuevas y dos puentes más. Acá se abre el mástil de verdad.", W))
S.append(Spacer(1, 8))
S.append(par([Diagrama(3, W * 0.49), Diagrama(4, W * 0.49)], [W * 0.505, W * 0.495]))
S.append(Spacer(1, 4))
S.append(Paragraph(
    "Es la semana más cargada y también la más divertida: es la zona donde viven los solos que te gustan. "
    "Si te sentís desbordado, priorizá el <b>ejercicio 12</b> por encima de todo — es el que junta las piezas.", BODY))

S.append(ejercicio(9, "La caja 3, ida y vuelta", (
    "Trastes 9 a 13. Es la más cómoda de las cinco: casi todo cae en el 10 y el 12, así que la mano trabaja poco. "
    "La trampa es justamente esa — como es fácil, medio mundo se queda a vivir acá."),
    "e09", W, "60 BPM, meta 80."))

S.append(ejercicio(10, "La caja 4, ida y vuelta", (
    "Trastes 12 a 15. Los trastes son más angostos: apretá cerca del metal y con menos fuerza. "
    "Si sentís que tenés que hacer fuerza, estás poniendo el dedo demasiado atrás."),
    "e10", W, "60 BPM, meta 75. Si te duele la mano, parás. No se entrena con dolor."))

S.append(ejercicio(11, "Dos puentes encadenados (2 a 3 a 4)", (
    "Dos slides seguidos: del 10 al 12 en la 1ª cuerda (entrás a la caja 3) y del 10 al 13 en la 2ª "
    "(entrás a la caja 4). Terminás con un vibrato largo en la 3ª cuerda traste 14: esa nota es un LA, "
    "por eso suena a llegada."),
    "e11", W, "Lento, 55 BPM si hace falta. La prolijidad de los slides importa más que la velocidad."))

S.append(ejercicio(12, "EL RECORRIDO DIAGONAL (el ejercicio clave del hito)", (
    "Acá dejás de pensar en cajas. En vez de subir y bajar dentro de una zona, <b>atravesás el mástil en "
    "diagonal</b>: subís de a poco por cada cuerda y vas cruzando las cuatro cajas de una. Es exactamente lo que "
    "hacen Page o Slash cuando parece que van a cualquier lado y nunca se pierden."),
    "e12", W, "55 BPM y con paciencia. Este ejercicio solo, hecho todos los días, ya justifica el mes."))

# ============================================================ SEMANA 4
S.append(PageBreak())
S.append(banner(4, "CAJA 5 Y EL MÁSTIL COMPLETO (se cierra el círculo)",
                "Objetivo: la última caja, la vuelta completa, y tu solo de evaluación.", W))
S.append(Spacer(1, 8))
S.append(par([Diagrama(5, W * 0.52),
              Paragraph("La caja 5 vive <b>debajo</b> de la caja 1 (trastes 2 a 5). Es la que menos se usa y la que "
                        "más te va a servir: es la zona grave, la de los riffs.<br/><br/>"
                        "Sus tónicas son la <b>6ª cuerda traste 5</b> y la <b>1ª cuerda traste 5</b> — las mismas "
                        "de la caja 1. Por eso el círculo cierra ahí.", BODY)],
             [W * 0.52, W * 0.48]))
S.append(Spacer(1, 4))

S.append(ejercicio(13, "La caja 5, ida y vuelta", (
    "Trastes 2 a 5. Ojo: en la 4ª y la 3ª cuerda las notas son 2 y 5, un estirón de tres trastes. "
    "Es la caja más incómoda de las cinco — es normal, no la estás haciendo mal."),
    "e13", W, "60 BPM, meta 75."))

S.append(ejercicio(14, "El círculo: de la caja 5 a la caja 1", (
    "Subís por la caja 5 y al llegar a la 1ª cuerda traste 5… <b>ya estás en la caja 1</b>. No hay slide ni "
    "salto: es la misma nota. Ahí entendés que las 5 cajas son un círculo, no una fila. Después de la 5 viene "
    "la 1 otra vez, una octava más arriba."),
    "e14", W, "60 BPM. Tocalo mirando el mapa de la página 2 mientras lo hacés."))

S.append(ejercicio(15, "Bajar el mástil en diagonal", (
    "El movimiento contrario al ejercicio 12: desde la caja 4 hasta la caja 5, bajando en diagonal. Cuesta más que "
    "subir — casi todos saben subir y no saben volver. Y un solo que sube y no baja se queda sin final."),
    "e15", W, "55 BPM. Fijate en los carteles: en 2 compases pasás por las 5 cajas."))

S.append(Paragraph("EJERCICIO 16 — EL SOLO DE EVALUACIÓN (tu entregable)", H2))
S.append(Paragraph(
    "Ocho compases que recorren las cinco cajas y usan todo lo del mes: espacio, bending, vibrato, slides y un cierre "
    "en la tónica. No es un examen de velocidad: <b>es un examen de mapa</b>. Aprendetelo, tocalo sobre el backing, "
    "grabalo y mandámelo. Ese video es tu Hito 1 cerrado.", BODY))
S.append(Spacer(1, 2))
S.append(score("e16", W))
S.append(Spacer(1, 4))
S.append(Paragraph(
    "Fijate en el compás 4: una sola nota larga y después <b>silencio</b>. Ese silencio está escrito a propósito — "
    "es lo que hace que el clímax del compás 5 pegue. Si lo llenás de notas, se muere.", SMALL))

# ============================================================ CIERRE
S.append(PageBreak())
S.append(Paragraph("¿CERRASTE EL HITO 1? (checklist honesto)", H1))
S.append(Paragraph(
    "Marcá solo lo que sea verdad. Si algo no está no pasa nada: repetís esa semana. "
    "El hito no se cierra por calendario, se cierra por resultado.", BODY))
S.append(tabla([
    [Paragraph("", CELLB), Paragraph("<b>Lo puedo hacer</b>", CELLB), Paragraph("<b>Cómo lo compruebo</b>", CELLB)],
    [Paragraph(CAJ, CELL), Paragraph("Toco las 5 cajas de memoria, sin mirar el papel", CELL),
     Paragraph("Alguien me dice un número del 1 al 5 y arranco esa caja en menos de 2 segundos.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Sé dónde está el LA en cualquier parte del mástil", CELL),
     Paragraph("Improvisando freno cuando quiero y caigo en un LA sin buscarlo.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Cruzo de una caja a la otra sin frenar", CELL),
     Paragraph("Toco el ejercicio 12 entero, a tempo, sin cortes ni dudas.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Bajo el mástil, no solo lo subo", CELL),
     Paragraph("Toco el ejercicio 15 con la misma soltura que el 12.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Mi bending llega afinado", CELL),
     Paragraph("Grabo el ejercicio 4 y al escucharlo el bending suena igual que el traste de destino.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("Tengo vibrato, no temblor", CELL),
     Paragraph("En la grabación el vibrato es parejo y controlado, no un tembleque nervioso.", CELL)],
    [Paragraph(CAJ, CELL), Paragraph("<b>Grabé el ejercicio 16 y lo mandé</b>", CELL),
     Paragraph("El video existe. Es el entregable del hito.", CELL)],
], [0.9 * cm, 6.3 * cm, W - 7.2 * cm]))

S.append(Paragraph("PLANILLA DE PRÁCTICA (marcá cada día que tocaste)", H2))
dias = ["L", "M", "X", "J", "V", "S", "D"]
rows = [[Paragraph("<b>Semana</b>", CELLB)] + [Paragraph("<b>%s</b>" % d, CELLB) for d in dias] +
        [Paragraph("<b>BPM al que llegué</b>", CELLB)]]
for nombre in ["1 · Caja 1", "2 · Caja 2", "3 · Cajas 3-4", "4 · Caja 5 + todo"]:
    rows.append([Paragraph(nombre, CELL)] + [Paragraph(CAJ, CELL) for _ in dias] + [Paragraph("", CELL)])
t = tabla(rows, [3.0 * cm] + [0.85 * cm] * 7 + [W - 3.0 * cm - 0.85 * cm * 7])
t.setStyle(TableStyle([('ALIGN', (1, 0), (7, -1), 'CENTER')]))
S.append(t)
S.append(Paragraph(
    "Regla: 5 días por semana o más. Si una semana marcaste menos de 4, no avances de caja: repetila. "
    "No es castigo — es que el mapa necesita repetición para fijarse.", SMALL))

S.append(Paragraph("Y DESPUÉS DE ESTO, ¿QUÉ?", H2))
S.append(Paragraph(
    "El Hito 1 te da el <b>territorio</b>: ya sabés dónde están las notas y podés moverte sin perderte. "
    "Pero saber dónde están las notas no alcanza para emocionar a nadie — por eso el Hito 2 es <b>EL SABOR</b>: "
    "ligados, slides, adornos, bending y vibrato trabajados en serio, que es lo que hace que la misma escala suene "
    "a Gary Moore y no a ejercicio. Y el Hito 3 es <b>EL VOCABULARIO</b>: tus propios licks, robados honestamente "
    "a los grandes, y tu solo final.", BODY))
S.append(Paragraph(
    "Pero eso es después. Este mes tenés un solo trabajo: <b>que el mástil deje de ser un misterio</b>.", BODY))

S.append(Spacer(1, 10))
cierre = Table([[Paragraph(
    '<font color="white" size="10.5"><b>¿Dudas con algún ejercicio?</b></font><br/>'
    '<font color="#f7d7d2" size="9">Traelas a la clase de los lunes, o escribime por DM. No te quedes trabado una '
    'semana entera por algo que se resuelve en dos minutos. · %s</font>' % IG,
    ParagraphStyle('c', fontName='Helvetica', fontSize=9, leading=13))]], colWidths=[W])
cierre.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), DARK),
                            ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                            ('TOPPADDING', (0, 0), (-1, -1), 8), ('BOTTOMPADDING', (0, 0), (-1, -1), 8)]))
S.append(cierre)

doc.build(S)
print("OK", OUT)
