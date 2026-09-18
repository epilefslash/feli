# -*- coding: utf-8 -*-
"""Graficos de las placas de historias, dibujados en el estilo del cuadernillo REAL.

POR QUE NO SE REUSA `cuadernillo_comun.py`: sus diagramas tienen fondo de madera, puntos
chicos y tipografia de 6.5pt -- estan pensados para una pagina A4 impresa. Los cuadernillos
que Feli entrega de verdad (los que pasa por Design) usan otro estilo, mas limpio y mas
grande: fondo blanco, puntos gordos, todos los trastes numerados, leyenda al pie. Feli lo
dijo textual (18/9): "el del cuadernillo es un poco mas amable a la vista".

Lo que SI se reusa de `cuadernillo_comun.py` son los DATOS (PENTA, TONICAS, CAJAS), que
estan verificados por `auditar_cajas.py`. Aca solo cambia como se dibujan.

Paleta muestreada del cuadernillo real, no inventada:
    naranja #e4572e · tinta #191512 · gris #8a8886 · crema #f5f0ec
"""
from reportlab.lib import colors

from cuadernillo_comun import PENTA, TONICAS, CAJAS, CAJA_RANGO_REAL

NARANJA = colors.HexColor("#e4572e")
TINTA = colors.HexColor("#191512")
GRIS = colors.HexColor("#8a8886")
GRIS_CLARO = colors.HexColor("#c7c5c2")
CREMA = colors.HexColor("#f5f0ec")
NOTA_APAGADA = colors.HexColor("#d8d0c6")

# Trastes que contienen alguna nota de la pentatonica -- se numeran en negro; el resto,
# en gris claro. Es lo que hace el cuadernillo real y lo que le da el aire "amable".
TRASTES_CON_NOTA = {t for ts in PENTA.values() for t in ts if t > 0}


def _cuerdas(c, x, y, w, hs):
    """6 lineas horizontales; la 6a (abajo) un poco mas gruesa, como una cuerda de verdad."""
    c.setStrokeColor(GRIS)
    for i in range(6):                      # i=0 arriba (1a cuerda) ... i=5 abajo (6a)
        c.setLineWidth(1.1 + i * 0.35)
        yy = y + (5 - i) * hs
        c.line(x, yy, x + w, yy)


def _trastes(c, x, y, w, hs, n):
    c.setStrokeColor(GRIS_CLARO)
    c.setLineWidth(1.0)
    fw = w / float(n)
    for k in range(n + 1):
        c.line(x + k * fw, y, x + k * fw, y + 5 * hs)
    return fw


def _cejuela(c, x, y, hs):
    c.setStrokeColor(TINTA)
    c.setLineWidth(7)
    c.line(x, y - 4, x, y + 5 * hs + 4)


def _numeros(c, x, y, fw, f0, f1, size):
    for f in range(f0, f1 + 1):
        tiene = f in TRASTES_CON_NOTA
        c.setFillColor(TINTA if tiene else GRIS_CLARO)
        c.setFont("Helvetica-Bold" if tiene else "Helvetica", size)
        c.drawCentredString(x + (f - f0 + 0.5) * fw, y - size - 12, str(f))


def _punto(c, cx, cy, r, relleno, texto=None, color_texto=colors.white, borde=None):
    if borde is not None:
        c.setFillColor(colors.white)
        c.setStrokeColor(borde)
        c.setLineWidth(2.6)
        c.circle(cx, cy, r, fill=1, stroke=1)
    else:
        c.setFillColor(relleno)
        c.circle(cx, cy, r, fill=1, stroke=0)
    if texto:
        c.setFillColor(color_texto)
        c.setFont("Helvetica-Bold", r * 1.05)
        c.drawCentredString(cx, cy - r * 0.37, texto)


def _corchetes_cajas(c, x, y_top, fw, f0, cajas, size):
    """Los corchetes rojos de las cajas, escalonados en dos alturas para que no se pisen."""
    for i, caja in enumerate(cajas):
        a, b = CAJA_RANGO_REAL[caja]
        xa = x + (a - f0) * fw + fw * 0.08
        xb = x + (b - f0 + 1) * fw - fw * 0.08
        yy = y_top + 26 + ((i + 1) % 2) * (size + 30)
        c.setStrokeColor(NARANJA)
        c.setLineWidth(3)
        c.line(xa, yy, xb, yy)
        c.line(xa, yy, xa, yy - 11)
        c.line(xb, yy, xb, yy - 11)
        c.setFillColor(NARANJA)
        c.setFont("Helvetica-Bold", size)
        c.drawCentredString((xa + xb) / 2, yy + 11, "CAJA %d" % caja)


# ---------------------------------------------------------------- EL MAPA
def notas_compartidas(caja_a, caja_b):
    """Las notas que pertenecen a las dos cajas a la vez -- los puentes entre una y otra.

    Es el contenido real del Hito 1: el alumno no se traba porque le falten cajas, se traba
    porque no sabe por donde se pasa de una a la siguiente.
    """
    na, nb = CAJAS[caja_a]["notas"], CAJAS[caja_b]["notas"]
    return {(cu, t) for cu in na for t in na[cu] if t in nb.get(cu, [])}


def mapa_completo(c, x, y, w, hs=34, f0=1, f1=17, cajas=(5, 1, 2, 3, 4), leyenda=True,
                  anillos=()):
    """El mastil entero con las 5 cajas marcadas -- el grafico insignia del Hito 1.

    Replica el del cuadernillo entregado: sin cuerdas al aire, trastes 1 a 17 numerados,
    los que no tienen nota en gris claro, corchetes de caja escalonados y leyenda al pie.
    Devuelve (alto_total, y_base) para poder apilar debajo.
    """
    n = f1 - f0 + 1
    fw = _trastes(c, x, y, w, hs, n)
    _cuerdas(c, x, y, w, hs)
    if f0 == 1:
        _cejuela(c, x, y, hs)

    r = hs * 0.33
    for cuerda, trastes in PENTA.items():
        yy = y + (6 - cuerda) * hs
        for t in trastes:
            if not (f0 <= t <= f1):
                continue
            cx = x + (t - f0 + 0.5) * fw
            if (cuerda, t) in anillos:
                c.setStrokeColor(NARANJA)
                c.setLineWidth(4)
                c.circle(cx, yy, r * 1.75, fill=0, stroke=1)
            if t in TONICAS.get(cuerda, []):
                _punto(c, cx, yy, r, NARANJA, "A")
            else:
                _punto(c, cx, yy, r, TINTA)

    _numeros(c, x, y, fw, f0, f1, 24)
    if cajas:
        _corchetes_cajas(c, x, y + 5 * hs, fw, f0, cajas, 22)

    if leyenda:
        ly = y - 100
        _punto(c, x + 14, ly, 15, NARANJA)
        c.setFillColor(TINTA)
        c.setFont("Helvetica-Bold", 21)
        c.drawString(x + 40, ly - 7, "LA — TU CASA")
        x2 = x + w * 0.46
        _punto(c, x2 + 14, ly, 15, TINTA)
        c.drawString(x2 + 40, ly - 7, "RESTO DE LA PENTATÓNICA")


# ---------------------------------------------------------------- EL SABOR
def bendings(c, x, y, w, hs=34, f0=5, f1=12):
    """El diagrama de bendings del Hito 2, pagina 'Bending — cantar con la cuerda'.

    Los 3 bendings son los del cuadernillo, verificados nota por nota: 1a cuerda 8->10
    (DO a RE), 2a cuerda 8->10 (SOL a LA) y 3a cuerda 7->9 (RE a MI). Los tres son de un
    tono entero y los tres caen en una nota de la pentatonica.
    """
    FLECHAS = [(1, 8, 10), (2, 8, 10), (3, 7, 9)]
    destinos = {(cu, d) for cu, _o, d in FLECHAS}
    origenes = {(cu, o) for cu, o, _d in FLECHAS}

    n = f1 - f0 + 1
    fw = _trastes(c, x, y, w, hs, n)
    _cuerdas(c, x, y, w, hs)

    r = hs * 0.33
    for cuerda, trastes in PENTA.items():
        yy = y + (6 - cuerda) * hs
        for t in trastes:
            if not (f0 <= t <= f1):
                continue
            cx = x + (t - f0 + 0.5) * fw
            if (cuerda, t) in origenes:
                _punto(c, cx, yy, r, NARANJA, "B")
            elif (cuerda, t) in destinos:
                _punto(c, cx, yy, r, None, borde=TINTA)
            elif t in TONICAS.get(cuerda, []):
                _punto(c, cx, yy, r, NOTA_APAGADA, "A", color_texto=TINTA)
            else:
                _punto(c, cx, yy, r, NOTA_APAGADA)

    _numeros(c, x, y, fw, f0, f1, 24)

    ly = y - 100
    _punto(c, x + 14, ly, 15, NARANJA)
    c.setFillColor(TINTA)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(x + 40, ly - 7, "DESDE ACÁ BENDEÁS")
    x2 = x + w * 0.48
    _punto(c, x2 + 14, ly, 15, None, borde=TINTA)
    c.setFillColor(TINTA)          # _punto con borde deja el relleno en blanco
    c.drawString(x2 + 40, ly - 7, "HASTA ACÁ — 1 TONO")


# ---------------------------------------------------------------- EL PULSO
def _figura(c, x, y, w, partes, barras):
    """Un compas-celula sobre un pentagrama chico: `partes` cabezas con `barras` corchetes."""
    c.setStrokeColor(GRIS_CLARO)
    c.setLineWidth(1.0)
    sep = 11
    for i in range(5):
        c.line(x, y + i * sep, x + w, y + i * sep)

    y_cabeza = y + sep * 0.5
    plica = 46.0
    xs = [x + w * 0.16 + i * (w * 0.62 / max(partes, 1)) for i in range(partes)]

    for cx in xs:                                   # cabezas
        c.saveState()
        c.translate(cx, y_cabeza)
        c.rotate(-20)
        c.setFillColor(TINTA)
        c.ellipse(-8, -5.6, 8, 5.6, fill=1, stroke=0)
        c.restoreState()

    c.setStrokeColor(TINTA)
    c.setLineWidth(2.4)
    for cx in xs:                                   # plicas
        c.line(cx + 7.4, y_cabeza + 1, cx + 7.4, y_cabeza + plica)

    if barras and partes > 1:                       # corchetes que unen las plicas
        c.setLineWidth(6)
        a, b = xs[0] + 7.4, xs[-1] + 7.4
        for k in range(barras):
            yy = y_cabeza + plica - k * 11
            c.line(a, yy, b, yy)

    # barra de compas al final, como en el cuadernillo
    c.setStrokeColor(GRIS_CLARO)
    c.setLineWidth(1.6)
    c.line(x + w, y, x + w, y + sep * 4)


def celulas(c, x, y, w, filas=None):
    """Las primeras celulas de 'Las 12 celulas del modulo' (El Pulso, pag. 4).

    La columna de la palabra es la que importa: cada celula se dice antes de tocarse.
    """
    if filas is None:
        filas = [("NEGRA", "el pulso entero", 1, 0, "PEZ"),
                 ("CORCHEA + CORCHEA", "la división recta", 2, 1, "PA-TO"),
                 ("CUATRO SEMICORCHEAS", "el pulso partido en cuatro", 4, 2, "CHO-CO-LA-TE")]
    alto = 118
    for i, (nombre, sub, partes, barras, palabra) in enumerate(filas):
        fy = y - 74 - i * alto          # `y` es el BORDE SUPERIOR del bloque
        c.setFillColor(TINTA)
        c.setFont("Helvetica-Bold", 22)
        c.drawString(x, fy + 52, nombre)
        c.setFillColor(GRIS)
        c.setFont("Helvetica", 19)
        c.drawString(x, fy + 26, sub)

        _figura(c, x + w * 0.46, fy + 16, w * 0.24, partes, barras)

        c.setFillColor(NARANJA)
        c.setFont("Helvetica-Bold", 26)
        c.drawRightString(x + w, fy + 44, palabra)

        if i + 1 < len(filas):
            c.setStrokeColor(GRIS_CLARO)
            c.setLineWidth(1)
            c.line(x, fy - 14, x + w, fy - 14)


# ---------------------------------------------------------------- EL VOCABULARIO
def dos_escuelas(c, x, y, w, filas=None):
    """La tabla 'Las dos escuelas' del Hito 3 (pag. 3), recortada a lo esencial."""
    if filas is None:
        filas = [("La frase vale por…", "la insistencia", "la melodía"),
                 ("Sensación", "agresiva, rítmica", "vocal, espaciosa"),
                 ("Referentes", "Page, Angus, Clapton", "Hendrix, Slash, Gary Moore")]
    col = w * 0.30
    x1, x2 = x + col, x + col + (w - col) / 2
    y -= 28                             # `y` es el BORDE SUPERIOR del bloque

    c.setFillColor(NARANJA)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(x1, y, "BRITÁNICA")
    c.drawString(x2, y, "AMERICANA")
    c.setStrokeColor(TINTA)
    c.setLineWidth(2.4)
    c.line(x, y - 20, x + w, y - 20)

    fy = y - 62
    for etiqueta, a, b in filas:
        c.setFillColor(TINTA)
        c.setFont("Helvetica-Bold", 21)
        c.drawString(x, fy, etiqueta)
        c.setFont("Helvetica", 21)
        for xx, txt in ((x1, a), (x2, b)):
            c.drawString(xx, fy, txt)
        fy -= 40
        c.setStrokeColor(GRIS_CLARO)
        c.setLineWidth(1)
        c.line(x, fy + 22, x + w, fy + 22)
        fy -= 18
