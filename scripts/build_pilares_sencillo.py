# -*- coding: utf-8 -*-
"""Version compacta de Pilares-y-Micropasos-Solo-con-Sabor.pdf -- sin las tablas de micro pasos
detalladas ni el texto explicativo largo. Pensada para tener a mano en pantalla durante la llamada
con Nico, no para leer con calma. El detalle completo sigue en Pilares-y-Micropasos-Solo-con-Sabor.pdf.

Fuente: entregables/contenido/PILARES-VERSION-SENCILLA.md
"""
from reportlab.platypus import Paragraph, Spacer

from cuadernillo_comun import documento
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Pilares-Version-Sencilla.pdf",
                "PROGRAMA DE ALTO VALOR",
                "Version sencilla -- Solo con Sabor",
                "Felipe Baya - Solo con Sabor",
                "Pilares - Version Sencilla")
W = doc.width
S = []

S.append(Paragraph("SOLO CON SABOR — RESUMEN", MOBILE_H1))
S.append(Spacer(1, 6))

with open("entregables/contenido/PILARES-VERSION-SENCILLA.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Pilares-Version-Sencilla.pdf")
