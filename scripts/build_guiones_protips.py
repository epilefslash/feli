# -*- coding: utf-8 -*-
"""Arma el PDF de los 3 guiones para filmar hoy (Fijado, Epifania, Vendedor) con protips de
coach / director / linguistica / sonido en cada uno -- para tener a mano mientras se filma.

Fuente: entregables/contenido/GUIONES-SABADO-PROTIPS.md
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Guiones-Protips.pdf",
                "GUIONES + PROTIPS",
                "Fijado, Epifanía y Vendedor — con notas de coach, director y lingüística",
                "Solo con Sabor · Para filmar hoy",
                "Guiones con Protips - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("GUIONES + PROTIPS", MOBILE_H1))
S.append(Paragraph(
    "Los 3 guiones para filmar hoy, palabra por palabra, con notas de coach de actuación, "
    "director y lingüística en cada uno.",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>Orden sugerido</b></font><br/>'
    '<font color="#f7d7d2" size="9">Fijado (sin texto, entras en calor) &#8594; '
    'Epifania &#8594; Vendedor (el mas cargado, dejalo para el final).</font>', W))
S.append(PageBreak())

with open("entregables/contenido/GUIONES-SABADO-PROTIPS.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Guiones-Protips.pdf")
