# -*- coding: utf-8 -*-
"""Arma el PDF con el guion de las 8 historias de la destacada METODO -- para filmar de corrido
y separar en historias despues.

Fuente: entregables/contenido/DESTACADA-METODO-GUION.md
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Destacada-Metodo-Guion.pdf",
                "DESTACADA METODO",
                "Guion de las 8 historias -- filmalo de corrido, cortalo despues",
                "Solo con Sabor · 14/9",
                "Destacada Metodo - Guion - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("DESTACADA “MÉTODO” — 8 HISTORIAS", MOBILE_H1))
S.append(Paragraph(
    "Guion hablado historia por historia, con los 5 pilares actualizados (El Mapa, El Sabor, "
    "El Vocabulario, El Pulso, El Vuelo). Listo para filmar de corrido y separar en CapCut.",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>8 historias, ~12-18 seg cada una</b></font><br/>'
    '<font color="#f7d7d2" size="9">Guitarra a mano, sin tocar salvo donde dice "tocás". '
    'Subtítulos siempre. Las historias 1 y 8 son las que más pesan.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/DESTACADA-METODO-GUION.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Destacada-Metodo-Guion.pdf")
