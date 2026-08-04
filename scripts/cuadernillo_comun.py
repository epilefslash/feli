# -*- coding: utf-8 -*-
"""Piezas compartidas por los cuadernillos: paleta, estilos, diagramas de mástil y helpers.

Lo usan `build_hito1.py` y `build_hito2.py`. Si querés cambiar los colores, la tipografía
o cómo se dibujan los diagramas, se toca acá y cambia en todos los cuadernillos a la vez.
"""
import os
import struct

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, Image, Flowable, KeepTogether)

AQUI = os.path.dirname(os.path.abspath(__file__))
PARTITURAS = os.path.join(AQUI, "partituras")
RAIZ = os.path.dirname(AQUI)
IG = "@felibayamenor"

# Fuente auxiliar solo para simbolos que Helvetica no tiene (casilla, flecha, negra)
for _ruta in ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
              "C:/Windows/Fonts/DejaVuSans.ttf", "C:/Windows/Fonts/seguisym.ttf"):
    if os.path.exists(_ruta):
        pdfmetrics.registerFont(TTFont('Sym', _ruta))
        break
CAJ = '<font name="Sym" size="11">☐</font>'

# ---------------------------------------------------------------- paleta
RED = colors.HexColor("#c0392b")
DARK = colors.HexColor("#2c3e50")
GREY = colors.HexColor("#777777")
LIGHT = colors.HexColor("#f5f0ec")
LIGHT2 = colors.HexColor("#fdf6f5")
BORDER = colors.HexColor("#ddcfc9")
WOOD = colors.HexColor("#e8ded6")
BLUE = colors.HexColor("#2f6fed")   # el blue note — distinto del rojo (tónica) y el gris oscuro (nota común)

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
# Trastes de la pentatonica de La menor por cuerda (1 = Mi agudo ... 6 = Mi grave)
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
    1: {"rango": (4, 9),   "notas": {6: [5, 8], 5: [5, 7], 4: [5, 7], 3: [5, 7], 2: [5, 8], 1: [5, 8]}},
    2: {"rango": (6, 11),  "notas": {6: [8, 10], 5: [7, 10], 4: [7, 10], 3: [7, 9], 2: [8, 10], 1: [8, 10]}},
    3: {"rango": (8, 14),  "notas": {6: [10, 12], 5: [10, 12], 4: [10, 12], 3: [9, 12], 2: [10, 13], 1: [10, 12]}},
    4: {"rango": (11, 16), "notas": {6: [12, 15], 5: [12, 15], 4: [12, 14], 3: [12, 14], 2: [13, 15], 1: [12, 15]}},
    5: {"rango": (1, 6),   "notas": {6: [3, 5], 5: [3, 5], 4: [2, 5], 3: [2, 5], 2: [3, 5], 1: [3, 5]}},
}
CAJA_RANGO_REAL = {1: (5, 8), 2: (7, 10), 3: (9, 13), 4: (12, 15), 5: (2, 5)}

# Grados de la pentatonica menor: 1 - 3menor - 4 - 5 - 7menor (no hay 2a, 3aM, 6a ni 7aM).
# La clave es la distancia en semitonos desde la tonica.
GRADOS = {0: "1", 3: "3", 5: "4", 7: "5", 10: "7"}
AL_AIRE = [4, 11, 7, 2, 9, 4]   # altura de cada cuerda al aire (1a a 6a), Do = 0
TONICA_PC = 9                    # La


def grado(cuerda, traste):
    """Devuelve el grado ('1', '3', '4', '5', '7') de una nota en La menor pentatónica."""
    pc = (AL_AIRE[cuerda - 1] + traste) % 12
    return GRADOS.get((pc - TONICA_PC) % 12)


# ---------------------------------------------------------------- dibujo
def _mastil(c, x0, y0, w, hs, nf, nut=False):
    """Fondo, trastes y cuerdas. Devuelve el ancho de un traste."""
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


def _nota(c, x, y, es_tonica, r=4.3, texto=None, color=None):
    if color is not None:
        c.setFillColor(color)
        c.circle(x, y, r, fill=1, stroke=0)
    elif es_tonica:
        c.setFillColor(RED)
        c.circle(x, y, r, fill=1, stroke=0)
        texto = texto or "A"
    else:
        c.setFillColor(DARK)
        c.circle(x, y, r - 0.5, fill=1, stroke=0)
    if texto:
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 5.4)
        c.drawCentredString(x, y - 1.9, texto)


class Diagrama(Flowable):
    """Diagrama de una caja de la pentatónica: cuerdas = filas, trastes = columnas."""

    PAD_L, PAD_R, PAD_B, PAD_T = 24, 6, 14, 15

    def __init__(self, caja, width, hs=11.0, titulo=None, grados=False):
        Flowable.__init__(self)
        self.caja, self.width, self.hs = caja, width, hs
        self.f0, f1 = CAJAS[caja]["rango"]
        self.nf = f1 - self.f0
        self.titulo = titulo
        self.grados = grados     # escribe el grado dentro de cada punto, no solo en las tónicas
        self.height = hs * 5 + self.PAD_B + self.PAD_T

    def draw(self):
        c = self.canv
        x0, y0 = self.PAD_L, self.PAD_B
        w = self.width - self.PAD_L - self.PAD_R
        fw = _mastil(c, x0, y0, w, self.hs, self.nf, nut=(self.f0 == 0))
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
                    es_tonica = t in TONICAS.get(cuerda, [])
                    _nota(c, x0 + (t - self.f0 - 0.5) * fw, y, es_tonica,
                          texto=grado(cuerda, t) if self.grados else None)

        a, b = CAJA_RANGO_REAL[self.caja]
        c.setFillColor(RED)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(x0, top + 4, self.titulo or "CAJA %d  ·  trastes %d a %d" % (self.caja, a, b))


class DiagramaFlechas(Flowable):
    """Caja de la pentatónica con flechas de origen → destino (bendings, slides).

    `flechas` = lista de (cuerda, traste_origen, traste_destino, etiqueta).
    `rango` sobreescribe el de la caja: hace falta porque los bendings terminan
    en trastes que quedan FUERA de la caja, y si no se extiende, la flecha se
    dibuja afuera del diagrama.
    """

    PAD_L, PAD_R, PAD_B, PAD_T = 24, 10, 14, 21

    def __init__(self, caja, flechas, width, hs=13.0, titulo=None, rango=None):
        Flowable.__init__(self)
        self.caja, self.flechas, self.width, self.hs = caja, flechas, width, hs
        self.f0, f1 = rango or CAJAS[caja]["rango"]
        self.nf = f1 - self.f0
        self.titulo = titulo
        self.height = hs * 5 + self.PAD_B + self.PAD_T

    def draw(self):
        c = self.canv
        x0, y0 = self.PAD_L, self.PAD_B
        w = self.width - self.PAD_L - self.PAD_R
        fw = _mastil(c, x0, y0, w, self.hs, self.nf)
        top = y0 + self.hs * 5

        c.setFillColor(GREY)
        c.setFont("Helvetica", 6.5)
        for i in range(self.nf):
            c.drawCentredString(x0 + (i + 0.5) * fw, y0 - 9, str(self.f0 + i + 1))
        c.setFont("Helvetica-Bold", 6.5)
        for s, nombre in enumerate(CUERDAS):
            c.drawRightString(x0 - 4, y0 + s * self.hs - 2.2, nombre)

        # notas de la caja, apagadas
        for cuerda, trastes in CAJAS[self.caja]["notas"].items():
            y = y0 + (6 - cuerda) * self.hs
            for t in trastes:
                if self.f0 < t <= self.f0 + self.nf:
                    _nota(c, x0 + (t - self.f0 - 0.5) * fw, y, False, r=3.4,
                          color=colors.HexColor("#b9aca3"))

        # flechas origen -> destino
        for cuerda, o, d, etiqueta in self.flechas:
            y = y0 + (6 - cuerda) * self.hs
            xo = x0 + (o - self.f0 - 0.5) * fw
            xd = x0 + (d - self.f0 - 0.5) * fw
            c.setStrokeColor(RED)
            c.setLineWidth(1.3)
            c.line(xo + 5, y, xd - 5, y)
            c.setFillColor(RED)
            p = c.beginPath()
            p.moveTo(xd - 4.5, y)
            p.lineTo(xd - 9, y + 3)
            p.lineTo(xd - 9, y - 3)
            p.close()
            c.drawPath(p, fill=1, stroke=0)
            _nota(c, xo, y, False, r=4.6, color=RED, texto=str(o))
            _nota(c, xd, y, False, r=4.6, color=DARK, texto=str(d))
            if etiqueta:
                c.setFillColor(GREY)
                c.setFont("Helvetica-Bold", 6)
                c.drawString(xd + 8, y - 2, etiqueta)

        if self.titulo:
            c.setFillColor(RED)
            c.setFont("Helvetica-Bold", 8.5)
            c.drawString(x0, top + 10, self.titulo)


class TablaturaEnBlanco(Flowable):
    """Pentagramas de tablatura vacíos, para que el alumno escriba los licks que saca.

    Cada sistema lleva arriba una línea de datos (de quién es, qué le robó) — el
    punto del hito no es juntar licks, es saber QUÉ mecanismo tiene cada uno.
    """

    SEP_CUERDA = 9.0
    ALTO_SISTEMA = 9.0 * 5 + 32      # 5 espacios entre 6 cuerdas + el encabezado
    PAD_L = 20

    def __init__(self, width, sistemas=4, compases=4, encabezado=True):
        Flowable.__init__(self)
        self.width, self.sistemas, self.compases = width, sistemas, compases
        self.encabezado = encabezado
        self.height = self.ALTO_SISTEMA * sistemas

    def draw(self):
        c = self.canv
        w = self.width - self.PAD_L
        for s in range(self.sistemas):
            base = self.height - (s + 1) * self.ALTO_SISTEMA + 22

            if self.encabezado:
                c.setFillColor(GREY)
                c.setFont("Helvetica", 7)
                c.drawString(self.PAD_L, base + self.SEP_CUERDA * 5 + 9,
                             "lick nº ______   ·   ¿de quién?  ____________________   "
                             "·   ¿qué le robo?  ________________________________")

            c.setStrokeColor(colors.HexColor("#9c8f86"))
            c.setLineWidth(0.5)
            for i in range(6):
                y = base + i * self.SEP_CUERDA
                c.line(self.PAD_L, y, self.PAD_L + w, y)

            # barras de compás
            c.setLineWidth(0.7)
            for m in range(self.compases + 1):
                x = self.PAD_L + m * w / self.compases
                c.line(x, base, x, base + self.SEP_CUERDA * 5)

            c.setFillColor(GREY)
            c.setFont("Helvetica-Bold", 7)
            c.drawRightString(self.PAD_L - 4, base + self.SEP_CUERDA * 2 - 2, "TAB")


class MapaCompleto(Flowable):
    """Mástil entero (trastes 0 a 17) con las 5 cajas marcadas arriba."""

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
        fw = _mastil(c, x0, y0, w, self.hs, nf, nut=True)
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


# Blue note = paso cromático entre la 4ª y la 5ª (el único "hueco" de un tono entero
# de la pentatónica menor). Una posición por cuerda y por octava dentro del mástil.
BLUE_NOTES = {1: [11], 2: [4, 16], 3: [8], 4: [1, 13], 5: [6], 6: [11]}


class MapaBlueNotes(MapaCompleto):
    """El mástil completo (igual que MapaCompleto) con el blue note marcado en cada cuerda.

    Es la misma nota "de paso" que ya se probó en el Hito 2 (ej. 26, caja 2, 3ª cuerda,
    traste 8) — acá se muestra que existe UNA sola por cuerda y por octava en todo el
    mástil, no una por caja. Confirma la idea central del programa: no son 5 cajas
    sueltas, es un solo mapa.
    """

    def draw(self):
        super().draw()
        c = self.canv
        x0, y0 = self.PAD_L, self.PAD_B
        w = self.width - self.PAD_L - self.PAD_R
        fw = w / 17
        for cuerda, trastes in BLUE_NOTES.items():
            y = y0 + (6 - cuerda) * self.hs
            for t in trastes:
                _nota(c, x0 + (t - 0.5) * fw, y, False, r=4.3, texto="b5", color=BLUE)


class ArbolFiguras(Flowable):
    """El árbol de las figuras: redonda -> 2 blancas -> 4 negras -> 8 corcheas -> 16 semis.

    Cada fila vale exactamente lo mismo (un compás de 4/4). Las líneas que bajan de
    cada figura a las dos de abajo son el punto del dibujo: bajar un escalón no es
    "ir más rápido", es partir la figura al medio. Por eso se dibuja como árbol y no
    como una lista de figuras con su duración al lado.

    Las plicas van para arriba y los conectores salen de abajo de la cabeza, así el
    árbol se lee de arriba hacia abajo sin que las líneas crucen las plicas.
    """

    FILAS = [
        (1, "REDONDA", "4 pulsos"),
        (2, "BLANCAS", "2 pulsos cada una"),
        (4, "NEGRAS", "1 pulso cada una"),
        (8, "CORCHEAS", "medio pulso"),
        (16, "SEMICORCHEAS", "un cuarto de pulso"),
    ]
    PAD_L, PAD_R, PAD_T, PAD_B = 96, 4, 12, 10
    FILA_H = 40.0
    RX, RY = 4.2, 3.1       # radios de la cabeza de la nota
    PLICA = 21.0

    def __init__(self, width):
        Flowable.__init__(self)
        self.width = width
        self.height = self.FILA_H * len(self.FILAS) + self.PAD_T + self.PAD_B

    def _centros(self, n):
        w = self.width - self.PAD_L - self.PAD_R
        return [self.PAD_L + (j + 0.5) * w / n for j in range(n)]

    def _cabeza(self, c, x, y, hueca):
        c.saveState()
        c.translate(x, y)
        c.rotate(-20)
        c.setLineWidth(1.1)
        c.setStrokeColor(DARK)
        if hueca:
            c.setFillColor(colors.white)
            c.ellipse(-self.RX, -self.RY, self.RX, self.RY, fill=1, stroke=1)
        else:
            c.setFillColor(DARK)
            c.ellipse(-self.RX, -self.RY, self.RX, self.RY, fill=1, stroke=0)
        c.restoreState()

    def draw(self):
        c = self.canv
        top = self.height - self.PAD_T

        for i, (n, nombre, dur) in enumerate(self.FILAS):
            y = top - i * self.FILA_H - self.FILA_H / 2
            xs = self._centros(n)

            # conectores hacia la fila de abajo: cada figura se parte en dos
            if i + 1 < len(self.FILAS):
                y_hijo = y - self.FILA_H
                hijos = self._centros(self.FILAS[i + 1][0])
                c.setStrokeColor(BORDER)
                c.setLineWidth(0.7)
                for j, x in enumerate(xs):
                    for xh in (hijos[2 * j], hijos[2 * j + 1]):
                        c.line(x, y - self.RY - 1.5, xh, y_hijo + self.PLICA * 0 + self.RY + 5)

            # plicas y barras de corchete (unen a los hermanos de la misma negra)
            if n > 1:
                c.setStrokeColor(DARK)
                c.setLineWidth(1.1)
                for x in xs:
                    c.line(x + self.RX - 0.4, y + 1, x + self.RX - 0.4, y + self.PLICA)
            if n >= 8:
                grupo = n // 4          # corcheas de a 2, semicorcheas de a 4
                c.setLineWidth(2.0)
                for g in range(0, n, grupo):
                    a, b = xs[g] + self.RX - 0.4, xs[g + grupo - 1] + self.RX - 0.4
                    c.line(a, y + self.PLICA, b, y + self.PLICA)
                    if n == 16:         # doble barra
                        c.line(a, y + self.PLICA - 4, b, y + self.PLICA - 4)

            for x in xs:
                self._cabeza(c, x, y, hueca=(n <= 2))

            c.setFillColor(RED)
            c.setFont("Helvetica-Bold", 8)
            c.drawString(4, y + 2, nombre)
            c.setFillColor(GREY)
            c.setFont("Helvetica", 7)
            c.drawString(4, y - 7.5, dur)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(DARK)
            c.drawRightString(self.PAD_L - 8, y - 2.5, u"× %d" % n)


class GrillaDelCompas(Flowable):
    """Los 8 lugares donde puede caer una nota en un compás de 4/4.

    Los cuatro números (tiempos fuertes, pie abajo) van llenos; los cuatro "y"
    (contratiempo, pie arriba) van huecos. Es el andamio que le falta a alguien
    que nunca contó un compás en voz alta: antes de leer una síncopa en la
    partitura tiene que poder ver que el compás no tiene cuatro lugares, tiene
    ocho.
    """

    PAD_T, PAD_B = 26, 30
    H = 34.0

    def __init__(self, width):
        Flowable.__init__(self)
        self.width = width
        self.height = self.H + self.PAD_T + self.PAD_B

    def draw(self):
        c = self.canv
        etiquetas = ["1", "y", "2", "y", "3", "y", "4", "y"]
        w = self.width / 8
        y = self.PAD_B

        for i, et in enumerate(etiquetas):
            x = i * w
            fuerte = (i % 2 == 0)
            c.setStrokeColor(BORDER)
            c.setLineWidth(0.8)
            c.setFillColor(DARK if fuerte else colors.white)
            c.rect(x + 2, y, w - 4, self.H, fill=1, stroke=1)

            c.setFillColor(colors.white if fuerte else GREY)
            c.setFont("Helvetica-Bold", 15 if fuerte else 12)
            c.drawCentredString(x + w / 2, y + self.H / 2 - 5, et)

            c.setFillColor(RED if not fuerte else GREY)
            c.setFont("Helvetica-Bold", 6.5)
            c.drawCentredString(x + w / 2, y - 11, "PIE ARRIBA" if not fuerte else "pie abajo")

        c.setFillColor(DARK)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(0, y + self.H + 11, "UN  y  DOS  y  TRES  y  CUA  y")
        c.setFillColor(GREY)
        c.setFont("Helvetica-Oblique", 7.5)
        c.drawRightString(self.width, y + self.H + 11,
                          "los oscuros son los tiempos fuertes · los blancos son el contratiempo")
        c.setFillColor(RED)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawCentredString(self.width / 2, y - 25,
                            "Casi todo lo que tocaste en los 3 hitos empieza en un casillero oscuro.")


# ---------------------------------------------------------------- helpers de armado
def score(name, width):
    """Inserta una partitura ya renderizada por los scripts gen_scores*.py."""
    p = os.path.join(PARTITURAS, name + ".cropped.png")
    w, h = struct.unpack('>II', open(p, 'rb').read(26)[16:24])
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
    t = Table([[Paragraph('<font color="white" size="13"><b>SEMANA %s</b></font><br/>'
                          '<font color="white" size="10.5"><b>%s</b></font><br/>'
                          '<font color="#f7d7d2" size="8.5">%s</font>' % (n, titulo, subtitulo),
                          ParagraphStyle('b', fontName='Helvetica', fontSize=10, leading=14))]],
              colWidths=[width])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), RED),
                           ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                           ('TOPPADDING', (0, 0), (-1, -1), 7), ('BOTTOMPADDING', (0, 0), (-1, -1), 7)]))
    return t


def par(flowables, widths):
    """Pone flowables uno al lado del otro."""
    t = Table([flowables], colWidths=widths)
    t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'),
                           ('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                           ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
    return t


def caja_oscura(texto, width):
    t = Table([[Paragraph(texto, ParagraphStyle('c', fontName='Helvetica', fontSize=9, leading=13))]],
              colWidths=[width])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), DARK),
                           ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                           ('TOPPADDING', (0, 0), (-1, -1), 8), ('BOTTOMPADDING', (0, 0), (-1, -1), 8)]))
    return t


def documento(archivo, titulo_cabecera, subtitulo_cabecera, pie, meta_titulo):
    """Crea el BaseDocTemplate con la cabecera roja y el pie de página."""

    def on_page(canvas, doc):
        canvas.saveState()
        w, h = A4
        canvas.setFillColor(RED)
        canvas.rect(0, h - 62, w, 62, fill=1, stroke=0)
        canvas.setFillColor(colors.white)
        canvas.setFont("Helvetica-Bold", 17)
        canvas.drawString(2 * cm, h - 34, titulo_cabecera)
        canvas.setFont("Helvetica", 9.5)
        canvas.drawString(2 * cm, h - 49, subtitulo_cabecera)
        canvas.setFont("Helvetica-Bold", 9)
        canvas.drawRightString(w - 2 * cm, h - 42, IG)
        canvas.setFillColor(GREY)
        canvas.setFont("Helvetica", 7.5)
        canvas.drawString(2 * cm, 1.15 * cm, pie)
        canvas.drawRightString(w - 2 * cm, 1.15 * cm, "pág. %d" % doc.page)
        canvas.setStrokeColor(BORDER)
        canvas.setLineWidth(0.5)
        canvas.line(2 * cm, 1.5 * cm, w - 2 * cm, 1.5 * cm)
        canvas.restoreState()

    doc = BaseDocTemplate(os.path.join(RAIZ, archivo), pagesize=A4,
                          leftMargin=2 * cm, rightMargin=2 * cm,
                          topMargin=2.85 * cm, bottomMargin=1.85 * cm,
                          title=meta_titulo, author="Feli")
    doc.addPageTemplates([PageTemplate(id='p', frames=[
        Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='f')], onPage=on_page)])
    return doc
