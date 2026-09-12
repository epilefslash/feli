# -*- coding: utf-8 -*-
"""Arma el PDF de la devolucion de sesion del 11/9: resumen de lo procesado (feedback de Nico +
M3 completo + trabajo de campo de tonalidad para El Vuelo), checklist de pendientes, y el guion
actualizado para filmar el fin de semana (Fijado sin cambios + Epifania en su formato nuevo).

Fuente: entregables/contenido/DEVOLUCION-SESION-11-9.md
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Devolucion-Sesion-11-9.pdf",
                "DEVOLUCIÓN 11/9",
                "Feedback de Nico + M3 completo + tonalidad en El Vuelo — resumen, checklist y guion del finde",
                "Solo con Sabor · Devolución",
                "Devolucion Sesion 11-9 - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("DEVOLUCIÓN DE LA SESIÓN (11/9)", MOBILE_H1))
S.append(Paragraph(
    "Lo que se proceso hoy: la devolucion de Nico sobre el contenido, el M3 completo que subiste, "
    "y el cierre de tonalidad para El Vuelo. El detalle completo de cada punto vive en la memoria "
    "del repo — esto es el resumen para tener a mano.",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>Cómo usar este documento</b></font><br/>'
    '<font color="#f7d7d2" size="9">Arriba, qué se cerró hoy y el checklist de lo que falta. '
    'Abajo del todo, el guion actualizado para filmar el fin de semana.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/DEVOLUCION-SESION-11-9.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Devolucion-Sesion-11-9.pdf")
