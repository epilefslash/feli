# -*- coding: utf-8 -*-
"""Las 5 portadas de las destacadas del perfil (los circulitos de arriba de la grilla).

POR QUE EXISTEN (pedido de Feli, 18/9): sin portada propia, Instagram usa una captura de la
primera historia de la destacada — y una captura recortada en circulo queda mal. Textual:
*"ya que podemos elegir y crear las portadas de los reel, no nos vamos a descuidar con las
portadas de las destacadas."*

Las 5 destacadas planificadas (`memoria/05` SS11):
    METODO · FORMACION · ALUMNOS · YO TOCO · TESTIMONIOS

DECISIONES DE DISENO, y por que:

1. **Icono solo, sin texto.** Instagram ya escribe el nombre de la destacada debajo del
   circulo. Meter la palabra adentro es repetirla, y ademas queda ilegible a ese tamano.
2. **Todo el contenido vive en el centro.** Instagram recorta un CIRCULO del centro de la
   imagen, asi que el icono entra en una circunferencia de 640 px de diametro sobre el lienzo
   de 1080x1920 — con margen de sobra para que ningun recorte se coma un borde.
3. **Misma paleta que las placas y los cuadernillos:** fondo #16120f, icono naranja #e4572e.
   Se ven como familia con el resto del perfil, no como iconos pegados de un banco.
4. **Cada icono se DIBUJA con primitivas** (no es tipografia de iconos ni una imagen bajada),
   asi que no depende de ninguna fuente instalada ni de ninguna licencia.

Salida: entregables/destacadas/portadas/portada-*.png (1080x1920).

Uso:
    python3 scripts/build_destacada_portadas.py
"""
import os
import shutil
import subprocess

from reportlab.lib import colors
from reportlab.pdfgen import canvas as canvaslib

import destacada_graficos as G

W, H = 1080.0, 1920.0
CX, CY = W / 2, H / 2
SEGURO = 640.0                  # diametro del circulo que Instagram deja ver

BG = colors.HexColor("#16120f")
ICONO = G.NARANJA
TENUE = colors.HexColor("#5a4c44")   # la grilla del mastil, que no compite con los puntos

SALIDA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                      "entregables", "destacadas", "portadas")


# ---------------------------------------------------------------- iconos
def metodo(c):
    """El mastil con la caja 1 marcada: el mismo mapa, reducido a icono.

    La caja va con su FORMA REAL (los trastes de `CAJAS[1]`, escalonados), no con dos columnas
    parejas -- es la silueta que el alumno reconoce del cuadernillo. La ventana va de 4 a 9 para
    que la caja (5 a 8) quede con aire a los dos lados en vez de pegada al borde.
    """
    f0, f1 = 4, 9
    w, hs = 430.0, 56.0
    x, y = CX - w / 2, CY - hs * 2.5
    fw = w / (f1 - f0 + 1)

    c.setStrokeColor(TENUE)
    c.setLineWidth(4)
    for i in range(6):                                  # cuerdas
        c.line(x, y + i * hs, x + w, y + i * hs)
    for k in range(f1 - f0 + 2):                        # trastes
        c.line(x + k * fw, y, x + k * fw, y + 5 * hs)

    c.setFillColor(ICONO)
    for cuerda, trastes in G.CAJAS[1]["notas"].items():
        yy = y + (6 - cuerda) * hs
        for t in trastes:
            c.circle(x + (t - f0 + 0.5) * fw, yy, 19, fill=1, stroke=0)


def formacion(c):
    """Birrete: el paso por la facultad de musica es el dato que sostiene esta destacada."""
    dx, dy = 210.0, 92.0
    y = CY + 78
    p = c.beginPath()                                   # la tabla de arriba, en rombo
    p.moveTo(CX, y + dy)
    p.lineTo(CX + dx, y)
    p.lineTo(CX, y - dy)
    p.lineTo(CX - dx, y)
    p.close()
    c.setFillColor(ICONO)
    c.drawPath(p, fill=1, stroke=0)

    b = c.beginPath()                                   # el cuerpo, un trapecio
    b.moveTo(CX - 118, y - 44)
    b.lineTo(CX + 118, y - 44)
    b.lineTo(CX + 96, y - 196)
    b.curveTo(CX + 50, y - 236, CX - 50, y - 236, CX - 96, y - 196)
    b.close()
    c.drawPath(b, fill=1, stroke=0)

    c.setStrokeColor(ICONO)                             # la borla
    c.setLineWidth(11)
    c.line(CX + dx - 16, y - 6, CX + dx - 16, y - 168)
    c.circle(CX + dx - 16, y - 188, 26, fill=1, stroke=0)


def alumnos(c):
    """Dos siluetas: la destacada es de ellos, no de Feli."""
    def figura(x, y, r, borde=0):
        """Si `borde` > 0 se dibuja primero en color de fondo y mas gordo: eso abre el hueco
        que separa una silueta de la otra, sin tener que tapar con rectangulos a mano."""
        for color, extra in ((BG, borde), (ICONO, 0)):
            if extra == 0 and borde and color is BG:
                continue
            c.setFillColor(color)
            c.circle(x, y + r * 1.75, r + extra, fill=1, stroke=0)
            c.wedge(x - r * 1.85 - extra, y - r * 1.5 - extra,
                    x + r * 1.85 + extra, y + r * 1.5 + extra, 0, 180, fill=1, stroke=0)

    figura(CX + 104, CY - 26, 60)                       # el de atras, mas chico
    figura(CX - 74, CY - 52, 74, borde=17)              # el de adelante, con su hueco


def yo_toco(c):
    """Una pua. Es el objeto mas reconocible de un guitarrista y no se confunde con nada."""
    w2, h2 = 168.0, 200.0
    y = CY - 20
    p = c.beginPath()
    p.moveTo(CX - w2, y + h2 * 0.35)
    p.curveTo(CX - w2, y + h2 * 1.05, CX + w2, y + h2 * 1.05, CX + w2, y + h2 * 0.35)
    p.curveTo(CX + w2 * 0.92, y - h2 * 0.35, CX + w2 * 0.40, y - h2 * 0.86, CX, y - h2)
    p.curveTo(CX - w2 * 0.40, y - h2 * 0.86, CX - w2 * 0.92, y - h2 * 0.35,
              CX - w2, y + h2 * 0.35)
    p.close()
    c.setFillColor(ICONO)
    c.drawPath(p, fill=1, stroke=0)


def testimonios(c):
    """Comillas: lo que hace un testimonio es prestar la voz de otro."""
    # Se usa el glifo tipografico en vez de dibujar la coma a mano: la comilla de Helvetica
    # ya tiene la curva bien resuelta, y a mano quedaba una colita despegada de la bola.
    # El glifo se dibuja desde la linea de base y su tinta vive muy por encima de ella, asi
    # que la base va bien abajo del centro para que la comilla quede centrada en el recorte.
    cuerpo = 600
    c.setFillColor(ICONO)
    c.setFont("Helvetica-Bold", cuerpo)
    c.drawCentredString(CX, CY - cuerpo * 0.585, u"\u201d")


PORTADAS = [("metodo", metodo), ("formacion", formacion), ("alumnos", alumnos),
            ("yo-toco", yo_toco), ("testimonios", testimonios)]


def main():
    os.makedirs(SALIDA, exist_ok=True)
    for nombre, dibujar in PORTADAS:
        ruta = os.path.join(SALIDA, "portada-%s.pdf" % nombre)
        c = canvaslib.Canvas(ruta, pagesize=(W, H))
        c.setFillColor(BG)
        c.rect(0, 0, W, H, fill=1, stroke=0)
        dibujar(c)
        c.showPage()
        c.save()
        if shutil.which("pdftoppm"):
            subprocess.run(["pdftoppm", "-png", "-r", "72", "-singlefile",
                            ruta, ruta[:-4]], check=True)
        print("OK portada-%s" % nombre)


if __name__ == "__main__":
    main()
