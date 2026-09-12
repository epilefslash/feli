# -*- coding: utf-8 -*-
"""Arma el PDF chico con los 2 guiones para filmar hoy (12/9): Fijado (sin cambios) y Epifania
(formato nuevo, B-roll + copy, armado sobre el documento real de Nico -- M3, hoja "Posteos de
Epifania" -- que Feli subio hoy).

Fuente: entregables/contenido/GUION-PARA-FILMAR-HOY.md
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Guion-Para-Filmar-Hoy.pdf",
                "PARA FILMAR HOY",
                "Fijado + Epifania -- los 2 guiones que faltan para el Dia 0",
                "Solo con Sabor · 12/9",
                "Guion Para Filmar Hoy - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("PARA FILMAR HOY", MOBILE_H1))
S.append(Paragraph(
    "Los 2 guiones que faltan para completar el Dia 0 (el tercero, #9, ya esta filmado, solo "
    "falta editarlo).",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>Que cambio y que no</b></font><br/>'
    '<font color="#f7d7d2" size="9">El Fijado no cambio nada -- es la primera vez que lo filmas, '
    'no un rehacer. La Epifania si es nueva: se reformulo hoy sobre el documento real de Nico '
    '(M3, hoja Posteos de Epifania) que subiste vos mismo.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/GUION-PARA-FILMAR-HOY.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Guion-Para-Filmar-Hoy.pdf")
