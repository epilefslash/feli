# -*- coding: utf-8 -*-
"""Arma el PDF con los 4 videos pendientes (guiones completos) + el checklist completo de huecos
del proyecto, organizado por bloque.

Fuente: entregables/contenido/CHECKLIST-VIDEOS-Y-HUECOS.md
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Checklist-Videos-y-Huecos.pdf",
                "VIDEOS Y HUECOS",
                "Los 4 videos que faltan filmar (con guion) + el checklist completo de huecos",
                "Solo con Sabor · 13/9",
                "Checklist Videos y Huecos - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("VIDEOS PENDIENTES Y HUECOS DEL PROYECTO", MOBILE_H1))
S.append(Paragraph(
    "Parte 1: los 4 videos que faltan filmar, con el guion completo listo para usar. "
    "Parte 2: el checklist completo de huecos, organizado en 4 bloques por urgencia.",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>4 videos + 4 bloques de huecos</b></font><br/>'
    '<font color="#f7d7d2" size="9">Fijado viejo, #7 equipo, Historia #11, Vendedor -- con '
    'guion completo. Despues: Instagram, pregrabado del programa, pedagogicos a proposito, '
    'y negocio/infraestructura.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/CHECKLIST-VIDEOS-Y-HUECOS.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Checklist-Videos-y-Huecos.pdf")
