# -*- coding: utf-8 -*-
"""Arma el PDF que resuelve la duda del Fijado (es el posteo de 2 pasos, pineado), los 3 posts
de hoy, el reacomodo de lo que se corre, y la correccion del "entrenamiento" del lead magnet.

Fuente: entregables/contenido/FIJADO-Y-2-PASOS-RESUELTO.md
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Fijado-y-2-Pasos-Resuelto.pdf",
                "FIJADO Y 2 PASOS",
                "Resuelto: qué es el Fijado, los 3 de hoy, y la corrección del entrenamiento",
                "Solo con Sabor · 12/9",
                "Fijado y 2 Pasos Resuelto - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("FIJADO Y 2 PASOS — RESUELTO", MOBILE_H1))
S.append(Paragraph(
    "El Fijado es el posteo de 2 pasos, pineado. Los 3 de hoy, qué se reacomoda, la corrección "
    "del entrenamiento del lead magnet, y la Epifanía verificada contra el prompt completo de Nico.",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>Para hoy, en 3 líneas</b></font><br/>'
    '<font color="#f7d7d2" size="9">1) Subís 3: 2 pasos (pineado) + #1 (recursos) + Epifanía '
    '(filmás hoy). 2) El reel mudo viejo y #9 no se pierden, se reacomodan. 3) El entrenamiento '
    'del lead magnet va en el DM, no en el posteo.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/FIJADO-Y-2-PASOS-RESUELTO.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Fijado-y-2-Pasos-Resuelto.pdf")
