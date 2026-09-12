# -*- coding: utf-8 -*-
"""Arma el PDF con el pineado completo: 3 slides + copy, listo para Canva, y los 2 guiones de
entrenamiento (DM para hoy + video opcional para despues).

Fuente: entregables/contenido/EL-PINEADO-ARMADO.md
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("El-Pineado-Armado.pdf",
                "EL PINEADO",
                "Armado completo: 3 slides + copy + los 2 entrenamientos",
                "Solo con Sabor · 12/9",
                "El Pineado Armado - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("EL PINEADO — ARMADO COMPLETO", MOBILE_H1))
S.append(Paragraph(
    "Las 3 slides y el copy, listos para pasar a Canva. Más el guion de entrenamiento que usás "
    "hoy (DM, sin filmar nada) y uno de video opcional para más adelante.",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>Para hoy</b></font><br/>'
    '<font color="#f7d7d2" size="9">Diseñás las 3 slides, publicás, pineás. El entrenamiento de '
    'hoy es texto para el DM -- no hace falta filmar nada.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/EL-PINEADO-ARMADO.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK El-Pineado-Armado.pdf")
