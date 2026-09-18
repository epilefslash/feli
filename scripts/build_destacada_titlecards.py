# -*- coding: utf-8 -*-
"""Genera las 6 placas de la destacada METODO (formato historia de Instagram, 1080x1920).

POR QUE EXISTE ESTE SCRIPT (memoria/05 SS55): el plan original era pedirle las 6 imagenes a
Claude Design con un prompt de texto. Se probo (18/9) y salio mal: una IA de imagen no puede
redibujar con precision "las 5 cajas de la pentatonica" a partir de una descripcion -- invento
un mastil incorrecto y mal compuesto. Feli lo rechazo ("nada que ver").

La solucion: no se describe el diagrama, se DIBUJA con los mismos componentes que ya generan
los cuadernillos reales y aprobados (MapaCompleto, DiagramaFlechas, ArbolFiguras,
TablaturaEnBlanco de cuadernillo_comun.py). Cero improvisacion: el mastil que sale aca es
nota por nota el mismo que el del PDF que el alumno ya tiene en la mano.

Dos reglas de composicion que se aprendieron del intento fallido:
1. El bloque de contenido se CENTRA en la zona segura, no se ancla arriba -- si no queda
   media placa vacia abajo, que es justo lo que se veia mal.
2. El tamano de cada linea de titulo se autoajusta para no tocar nunca los margenes.

Salida: scratchpad/titlecards/destacada-N-*.pdf + .png (1080x1920 px a 72 dpi).

Uso:
    python3 scripts/build_destacada_titlecards.py
"""
import os

from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas as canvaslib

from cuadernillo_comun import (RED, IG, MapaCompleto, DiagramaFlechas,
                               ArbolFiguras, TablaturaEnBlanco)

W, H = 1080.0, 1920.0
MARGEN = 96.0                    # margen lateral minimo del texto

# Paleta de la placa -- fondo calido casi negro, igual que el posteo de 2 pasos ya publicado.
BG = colors.HexColor("#16120f")
CARD = colors.HexColor("#fdf6f5")
TXT = colors.white
SUB = colors.HexColor("#c9bdb5")
FOOT = colors.HexColor("#6e625b")

# Zona segura de Instagram Stories: arriba se come ~250px (usuario, X) y abajo ~280px
# (barra de responder). Todo el contenido vive entre estas dos lineas.
SAFE_TOP = 1620.0
SAFE_BOT = 340.0

SALIDA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                      "scratchpad", "titlecards")


# ---------------------------------------------------------------- bloques
class Texto(object):
    """Lineas de texto centradas. El size baja solo si alguna linea no entra a lo ancho."""

    def __init__(self, lineas, font, size, leading, color, gap=0):
        self.lineas, self.font, self.color, self.gap = lineas, font, color, gap
        ancho_max = W - 2 * MARGEN
        original = size
        for l in lineas:
            while size > 10 and pdfmetrics.stringWidth(l, font, size) > ancho_max:
                size -= 1
        self.size = size
        # si el texto tuvo que achicarse, el interlineado se achica en la misma proporcion
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
    """Lista con vinetas rojas, alineada a la izquierda pero centrada como bloque."""

    def __init__(self, lineas, size=40, leading=92, gap=0):
        self.lineas, self.size, self.leading, self.gap = lineas, size, leading, gap
        self.ancho = max(pdfmetrics.stringWidth(l, "Helvetica", size) for l in lineas)
        self.height = leading * len(lineas) + gap

    def draw(self, c, y):
        x = (W - (self.ancho + 46)) / 2
        yy = y - self.size
        for l in self.lineas:
            c.setFillColor(RED)
            c.circle(x + 9, yy + self.size * 0.33, 9, fill=1, stroke=0)
            c.setFillColor(TXT)
            c.setFont("Helvetica", self.size)
            c.drawString(x + 46, yy, l)
            yy -= self.leading
        return y - self.height


class Tarjeta(object):
    """Un Flowable del cuadernillo adentro de una tarjeta blanca redondeada.

    El flowable se instancia a su tamano natural de impresion (donde sus fuentes de 6.5pt
    tienen sentido) y se escala entero -- asi los numeros de traste crecen con el dibujo en
    vez de quedar ilegibles.
    """

    def __init__(self, flow, ancho, escala, pad=44, gap=0):
        self.flow, self.ancho, self.escala, self.pad, self.gap = flow, ancho, escala, pad, gap
        self.cw = ancho * escala + 2 * pad
        self.ch = flow.height * escala + 2 * pad
        self.height = self.ch + gap

    def draw(self, c, y):
        x = (W - self.cw) / 2
        c.setFillColor(CARD)
        c.roundRect(x, y - self.ch, self.cw, self.ch, 28, fill=1, stroke=0)
        c.saveState()
        c.translate(x + self.pad, y - self.ch + self.pad)
        c.scale(self.escala, self.escala)
        self.flow.drawOn(c, 0, 0)
        c.restoreState()
        return y - self.height


def placa(nombre, bloques):
    """Centra verticalmente la pila de bloques en la zona segura y la dibuja."""
    ruta = os.path.join(SALIDA, nombre)
    c = canvaslib.Canvas(ruta, pagesize=(W, H))

    c.setFillColor(BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(RED)
    c.rect(0, H - 14, W, 14, fill=1, stroke=0)

    total = sum(b.height for b in bloques)
    y = SAFE_BOT + (SAFE_TOP - SAFE_BOT + total) / 2
    y = min(y, SAFE_TOP)
    for b in bloques:
        y = b.draw(c, y)

    c.setFont("Helvetica", 26)
    c.setFillColor(FOOT)
    c.drawCentredString(W / 2, SAFE_BOT - 52, IG)

    c.showPage()
    c.save()
    print("OK", nombre)


def eyebrow(t):
    return Texto([t], "Helvetica-Bold", 30, 30, RED, gap=46)


def titulo(lineas):
    return Texto(lineas, "Helvetica-Bold", 86, 100, TXT, gap=30)


def titulo_pilar(t):
    """Los nombres de pilar son una o dos palabras: entran mucho mas grandes que un gancho."""
    return Texto([t], "Helvetica-Bold", 124, 124, TXT, gap=48)


def bajada(t):
    return Texto([t], "Helvetica", 42, 42, SUB, gap=54)


def pie(lineas, gap=0):
    return Texto(lineas, "Helvetica-Bold", 38, 54, SUB, gap=gap)


def main():
    os.makedirs(SALIDA, exist_ok=True)

    # 1 -- GANCHO. El mastil completo con las 5 cajas: el mismo asset del lead magnet.
    placa("destacada-1-gancho.pdf", [
        eyebrow("// EL MÉTODO, EN 2 MINUTOS"),
        titulo(["Cómo paso de tocar", "siempre lo mismo…", "a un solo que es tuyo."]),
        Tarjeta(MapaCompleto(440, hs=17), 440, 1.95, gap=60),
        pie(["Mirá las siguientes historias"]),
    ])

    # 2 -- PILAR 1. Mismo mapa: es literalmente el contenido del pilar.
    placa("destacada-2-pilar1-mapa.pdf", [
        eyebrow("// PILAR 1"),
        titulo_pilar("EL MAPA"),
        bajada("dominar el mástil"),
        Tarjeta(MapaCompleto(440, hs=17), 440, 1.95, gap=56),
        pie(["5 cajas sueltas pasan a ser", "un solo mástil."]),
    ])

    # 3 -- PILAR 2. El bending del ejercicio 21 del Hito 2, tal cual: 3a cuerda, 7 -> 9.
    placa("destacada-3-pilar2-sabor.pdf", [
        eyebrow("// PILAR 2"),
        titulo_pilar("EL SABOR"),
        bajada("bending, vibrato, expresión"),
        Tarjeta(DiagramaFlechas(1, [(3, 7, 9, "")], 420, hs=19,
                                titulo="BENDING DE 1 TONO  ·  3ª CUERDA, TRASTE 7 AL 9",
                                rango=(4, 10)), 420, 2.05, gap=56),
        pie(["Ya sabés las notas.", "Acá aprendés a que suenen a música."]),
    ])

    # 4 -- PILAR 3. El banco de licks del Hito 3: no se coleccionan notas, se anota el mecanismo.
    placa("destacada-4-pilar3-vocabulario.pdf", [
        eyebrow("// PILAR 3"),
        titulo_pilar("EL VOCABULARIO"),
        bajada("licks propios, estilo"),
        Tarjeta(TablaturaEnBlanco(440, sistemas=2, compases=4), 440, 1.95, gap=56),
        pie(["No copiás a Page y a Slash.", "Te apropiás de lo que hacen."]),
    ])

    # 5 -- PILAR 4. El arbol de figuras del Pulso, sin cambiar un trazo.
    placa("destacada-5-pilar4-pulso.pdf", [
        eyebrow("// PILAR 4"),
        titulo_pilar("EL PULSO"),
        bajada("ritmo y tiempo"),
        Tarjeta(ArbolFiguras(430), 430, 1.8, gap=52),
        pie(["Las notas justas en el momento", "equivocado no suenan."]),
    ])

    # 6 -- PILAR 5. Sin diagrama a proposito: El Vuelo no ensena nada nuevo, integra.
    #      La lista son los 4 micro-pasos reales (memoria/02 SS28-QUINQUIES).
    placa("destacada-6-pilar5-vuelo.pdf", [
        eyebrow("// PILAR 5"),
        titulo_pilar("EL VUELO"),
        bajada("improvisando y soltándote en vivo"),
        Vinetas(["Te movés por las 5 cajas sin pensarlas",
                 "El sabor aparece solo",
                 "Tus licks entran sin anunciarse",
                 "Tocás con otros: entrás, salís, volvés"], gap=70),
        pie(["Acá no aprendés nada nuevo.", "Soltás todo lo anterior, en vivo."]),
    ])


if __name__ == "__main__":
    main()
