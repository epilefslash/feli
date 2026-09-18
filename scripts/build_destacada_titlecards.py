# -*- coding: utf-8 -*-
"""Genera las 6 placas de la destacada METODO (formato historia de Instagram, 1080x1920).

POR QUE EXISTE ESTE SCRIPT (memoria/05 SS55): el plan original era pedirle las 6 imagenes a
Claude Design con un prompt de texto. Se probo (18/9) y salio mal: una IA de imagen no puede
redibujar con precision un diagrama de mastil a partir de una descripcion -- invento uno
incorrecto y mal compuesto. Feli lo rechazo ("nada que ver").

La solucion: no se describe el grafico, se DIBUJA, con los datos ya verificados del repo
(PENTA/TONICAS/CAJAS, auditados por auditar_cajas.py) y en el estilo visual del cuadernillo
REAL que Feli entrega -- ver `destacada_graficos.py` para por que ese estilo y no el de
`cuadernillo_comun.py`.

Cada placa lleva el grafico insignia de su pilar, sacado del cuadernillo correspondiente:

    1 Gancho          mapa de las 5 cajas          Hito 1, "El mapa completo"
    2 EL MAPA         cajas 1 y 2 solapadas        Hito 1 -- donde se tocan entre si
    3 EL SABOR        los 3 bendings de 1 tono     Hito 2, "Bending - cantar con la cuerda"
    4 EL VOCABULARIO  las dos escuelas             Hito 3, "Las dos escuelas"
    5 EL PULSO        las celulas con su palabra   El Pulso, "Las 12 celulas del modulo"
    6 EL VUELO        los 4 micro-pasos            memoria/02 SS28-QUINQUIES (sin grafico
                                                   propio en la fuente -- ver nota abajo)

Dos reglas de composicion que se aprendieron del intento fallido:
1. El bloque de contenido se CENTRA en la zona segura, no se ancla arriba -- si no queda
   media placa vacia abajo, que es justo lo que se veia mal.
2. El tamano de cada linea de titulo se autoajusta para no tocar nunca los margenes.

Salida: entregables/destacadas/destacada-N-*.pdf + .png (1080x1920 px a 72 dpi). El PNG es
lo que Feli sube a Instagram; el PDF queda como fuente vectorial por si hay que reimprimir.

Uso:
    python3 scripts/build_destacada_titlecards.py
"""
import os
import shutil
import subprocess

from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas as canvaslib

import destacada_graficos as G

W, H = 1080.0, 1920.0
MARGEN = 96.0                    # margen lateral minimo del texto

# Fondo oscuro calido (el mismo del posteo de 2 pasos ya publicado) + tarjeta blanca adentro,
# donde el grafico se ve igual que en el cuadernillo impreso.
BG = colors.HexColor("#16120f")
CARD = colors.white
TXT = colors.white
SUB = colors.HexColor("#c9bdb5")
FOOT = colors.HexColor("#6e625b")

# Zona segura de Instagram Stories: arriba se come ~250px (usuario, X) y abajo ~280px
# (barra de responder).
SAFE_TOP = 1620.0
SAFE_BOT = 340.0

IG = "@feli.baya.menor"

SALIDA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                      "entregables", "destacadas")


# ---------------------------------------------------------------- bloques
class Texto(object):
    """Lineas de texto centradas. El cuerpo baja solo si alguna linea no entra a lo ancho."""

    def __init__(self, lineas, font, size, leading, color, gap=0):
        self.lineas, self.font, self.color, self.gap = lineas, font, color, gap
        ancho_max = W - 2 * MARGEN
        original = size
        for l in lineas:
            while size > 10 and pdfmetrics.stringWidth(l, font, size) > ancho_max:
                size -= 1
        self.size = size
        self.leading = leading * size / float(original)
        self.height = self.leading * len(lineas) + gap

    def draw(self, c, y):
        c.setFont(self.font, self.size)
        c.setFillColor(self.color)
        yy = y - self.size
        for l in self.lineas:
            c.drawCentredString(W / 2, yy, l)
            yy -= self.leading
        return y - self.height


class Vinetas(object):
    """Lista con vinetas naranjas, alineada a la izquierda pero centrada como bloque."""

    def __init__(self, lineas, size=40, leading=92, gap=0):
        self.lineas, self.size, self.leading, self.gap = lineas, size, leading, gap
        self.ancho = max(pdfmetrics.stringWidth(l, "Helvetica", size) for l in lineas)
        self.height = leading * len(lineas) + gap

    def draw(self, c, y):
        x = (W - (self.ancho + 46)) / 2
        yy = y - self.size
        for l in self.lineas:
            c.setFillColor(G.NARANJA)
            c.circle(x + 9, yy + self.size * 0.33, 9, fill=1, stroke=0)
            c.setFillColor(TXT)
            c.setFont("Helvetica", self.size)
            c.drawString(x + 46, yy, l)
            yy -= self.leading
        return y - self.height


class Boton(object):
    """Bloque naranja lleno, con el CTA adentro.

    Lo usa SOLO la placa de cierre, a proposito: es la unica historia de la destacada que
    pide algo, y el bloque de color la separa del resto de un vistazo.
    """

    def __init__(self, lineas, size=40, leading=54, pad=40, gap=0):
        self.lineas, self.size, self.leading, self.pad, self.gap = lineas, size, leading, pad, gap
        ancho_max = W - 2 * 88
        while size > 12 and max(pdfmetrics.stringWidth(l, "Helvetica-Bold", size)
                                for l in lineas) > ancho_max:
            size -= 1
        self.size = size
        self.leading = leading * size / float(self.size if self.size else 1)
        self.ch = leading * len(lineas) + 2 * pad
        self.height = self.ch + gap

    def draw(self, c, y):
        cw = W - 2 * 44
        x = (W - cw) / 2
        c.setFillColor(G.NARANJA)
        c.roundRect(x, y - self.ch, cw, self.ch, 26, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", self.size)
        yy = y - self.pad - self.size
        for l in self.lineas:
            c.drawCentredString(W / 2, yy, l)
            yy -= self.leading
        return y - self.height


class Tarjeta(object):
    """Tarjeta blanca redondeada con un grafico del cuadernillo adentro.

    `dibujar(c, x, y_base, w)` recibe el ancho util y la linea de base que le corresponde;
    `alto` y `base` los declara cada grafico porque cada uno cuelga cosas distintas por
    debajo (numeros de traste, leyenda) y por encima (corchetes de caja).
    """

    def __init__(self, dibujar, alto, base, pad=48, gap=0, titulo=None, pie=None):
        self.dibujar, self.pad, self.gap = dibujar, pad, gap
        self.titulo, self.pie = titulo, pie
        self.interno = alto + (44 if titulo else 0) + (40 if pie else 0)
        self.base = base + (40 if pie else 0)
        self.cw = W - 2 * 44
        self.ch = self.interno + 2 * pad
        self.height = self.ch + gap

    def draw(self, c, y):
        x = (W - self.cw) / 2
        c.setFillColor(CARD)
        c.roundRect(x, y - self.ch, self.cw, self.ch, 30, fill=1, stroke=0)
        xi, wi = x + self.pad, self.cw - 2 * self.pad

        if self.titulo:
            c.setFillColor(G.NARANJA)
            c.setFont("Helvetica-Bold", 23)
            c.drawString(xi, y - self.pad - 23, self.titulo)
        if self.pie:
            c.setFillColor(G.NARANJA)
            c.setFont("Helvetica-Bold", 20)
            c.drawString(xi, y - self.ch + self.pad, self.pie)

        self.dibujar(c, xi, y - self.ch + self.pad + self.base, wi)
        return y - self.height


def placa(nombre, bloques, ruta=None, png=True):
    """Centra verticalmente la pila de bloques en la zona segura y la dibuja.

    `ruta` y `png=False` los usa el animador (`build_destacada_animaciones.py`), que necesita
    escribir estados intermedios en otro lado y rasterizarlos el mismo a mas resolucion.
    """
    ruta = ruta or os.path.join(SALIDA, nombre)
    c = canvaslib.Canvas(ruta, pagesize=(W, H))

    c.setFillColor(BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(G.NARANJA)
    c.rect(0, H - 14, W, 14, fill=1, stroke=0)

    total = sum(b.height for b in bloques)
    y = min(SAFE_BOT + (SAFE_TOP - SAFE_BOT + total) / 2, SAFE_TOP)
    for b in bloques:
        y = b.draw(c, y)

    c.setFont("Helvetica", 26)
    c.setFillColor(FOOT)
    c.drawCentredString(W / 2, SAFE_BOT - 52, IG)

    c.showPage()
    c.save()
    if png:
        _png(ruta)
        print("OK", nombre)
    return ruta


def _png(ruta_pdf):
    """Rasteriza a 72 dpi -> 1080x1920 px exactos, que es lo que se sube a Instagram."""
    if not shutil.which("pdftoppm"):
        print("   (sin pdftoppm: queda solo el PDF)")
        return
    subprocess.run(["pdftoppm", "-png", "-r", "72", "-singlefile",
                    ruta_pdf, ruta_pdf[:-4]], check=True)


def eyebrow(t):
    return Texto([t], "Helvetica-Bold", 30, 30, G.NARANJA, gap=46)


def titulo(lineas):
    return Texto(lineas, "Helvetica-Bold", 86, 100, TXT, gap=30)


def titulo_pilar(t):
    """Los nombres de pilar son una o dos palabras: entran mucho mas grandes que un gancho."""
    return Texto([t], "Helvetica-Bold", 124, 124, TXT, gap=48)


def bajada(t):
    return Texto([t], "Helvetica", 42, 42, SUB, gap=54)


def pie(lineas, gap=0):
    return Texto(lineas, "Helvetica-Bold", 38, 54, SUB, gap=gap)


# ---------------------------------------------------------------- las 6 placas
def tarjetas():
    """Las 7 placas, como (nombre, bloques).

    Se expone aparte de main() porque `build_destacada_animaciones.py` arma los
    videos con estas mismas definiciones -- si se duplicaran, la version fija y la
    animada se irian separando con cada cambio de texto.
    """
    placas = []

    mapa = lambda c, x, y, w: G.mapa_completo(c, x, y, w, hs=40)
    puentes = G.notas_compartidas(1, 2)
    puente = lambda c, x, y, w: G.mapa_completo(c, x, y, w, hs=40, f0=4, f1=11,
                                                cajas=(1, 2), leyenda=False,
                                                anillos=puentes)
    bend = lambda c, x, y, w: G.bendings(c, x, y, w, hs=40)

    # 1 -- GANCHO. El mastil entero: el mismo grafico del lead magnet y del Hito 1.
    placas.append(("destacada-1-gancho.pdf", [
        eyebrow("// EL MÉTODO, EN 2 MINUTOS"),
        titulo(["Cómo paso de tocar", "siempre lo mismo…", "a un solo que es tuyo."]),
        Tarjeta(mapa, 470, 125, gap=58),
        pie(["Mirá las siguientes historias"]),
    ]))

    # 2 -- PILAR 1. Las cajas 1 y 2 solapadas: el contenido real del pilar no son las cajas,
    #      son los puentes -- donde una se toca con la siguiente.
    placas.append(("destacada-2-pilar1-mapa.pdf", [
        eyebrow("// PILAR 1"),
        titulo_pilar("EL MAPA"),
        bajada("dominar el mástil"),
        Tarjeta(puente, 386, 45, gap=54,
                titulo="DONDE LA CAJA 1 SE TOCA CON LA 2",
                pie="Las marcadas son de las dos cajas. Ahí se cruza."),
        pie(["5 cajas sueltas pasan a ser", "un solo mástil."]),
    ]))

    # 3 -- PILAR 2. Los 3 bendings de un tono del Hito 2, tal cual el cuadernillo.
    placas.append(("destacada-3-pilar2-sabor.pdf", [
        eyebrow("// PILAR 2"),
        titulo_pilar("EL SABOR"),
        bajada("bending, vibrato, expresión"),
        Tarjeta(bend, 368, 125, gap=54,
                titulo="BENDING — CANTAR CON LA CUERDA",
                pie="3ª cuerda, traste 7: el más usado del rock."),
        pie(["Ya sabés las notas.", "Acá aprendés a que suenen a música."]),
    ]))

    # 4 -- PILAR 3. La tabla de las dos escuelas: la idea central del Hito 3.
    placas.append(("destacada-4-pilar3-vocabulario.pdf", [
        eyebrow("// PILAR 3"),
        titulo_pilar("EL VOCABULARIO"),
        bajada("licks propios, estilo"),
        Tarjeta(lambda c, x, y, w: G.dos_escuelas(c, x, y + 270, w), 270, 0, gap=54,
                titulo="LAS DOS ESCUELAS DEL ROCK",
                pie="Una por semana. En el solo final usás las dos."),
        pie(["No copiás a Page y a Slash.", "Te apropiás de lo que hacen."]),
    ]))

    # 5 -- PILAR 4. Las celulas con su palabra: se dicen antes de tocarse.
    placas.append(("destacada-5-pilar4-pulso.pdf", [
        eyebrow("// PILAR 4"),
        titulo_pilar("EL PULSO"),
        bajada("ritmo y tiempo"),
        Tarjeta(lambda c, x, y, w: G.celulas(c, x, y + 330, w), 330, 0, gap=54,
                titulo="UN PULSO, VARIAS FORMAS DE PARTIRLO",
                pie="Si podés decirla, ya la podés tocar."),
        pie(["Las notas justas en el momento", "equivocado no suenan."]),
    ]))

    # 6 -- PILAR 5. Sin grafico propio a proposito: el pilar no ensena nada nuevo, integra.
    #      Los 4 micro-pasos son los reales (memoria/02 SS28-QUINQUIES).
    placas.append(("destacada-6-pilar5-vuelo.pdf", [
        eyebrow("// PILAR 5"),
        titulo_pilar("EL VUELO"),
        bajada("improvisando y soltándote en vivo"),
        Vinetas(["Te movés por las 5 cajas sin pensarlas",
                 "El sabor aparece solo",
                 "Tus licks entran sin anunciarse",
                 "Tocás con otros: entrás, salís, volvés"], gap=70),
        pie(["Acá no aprendés nada nuevo.", "Soltás todo lo anterior, en vivo."]),
    ]))

    # 7 -- CIERRE + CTA. PLAN B: la historia 12 se filma a camara (memoria/05 SS49). Esta
    #      placa existe solo por si hay que cerrar la destacada antes de poder filmarla.
    #      El CTA pasa la regla del mantra (memoria/04, "Menu de CTAs"): nombra la dolencia
    #      del alumno, no el metodo -- ni "mi programa" ni "te cuento como trabajo".
    placas.append(("destacada-7-cierre-cta.pdf", [
        eyebrow("// LO QUE TE LLEVÁS"),
        titulo(["Grabás tu propio", "solo de 1 minuto."]),
        bajada("Ese es tu antes y después."),
        pie(["Y no es el único: cada pilar", "cierra con un video tuyo."], gap=54),
        Boton(["Si sabés la caja 1 y seguís", "sonando igual, escribime SOLO"], gap=0),
    ]))

    return placas


def main():
    os.makedirs(SALIDA, exist_ok=True)
    for nombre, bloques in tarjetas():
        placa(nombre, bloques)


if __name__ == "__main__":
    main()
