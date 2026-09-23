# -*- coding: utf-8 -*-
"""Arma el PDF del plan de accion del sabado 12/9: los 4 prompts de carruseles, que filmar al
mediodia (con guion/shot-list adentro), que hace falta para abrir el Instagram a la tarde, y el
estado completo de los 15 posteos.

Fuente: entregables/contenido/PLAN-DE-ACCION-12-9.md
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Plan-de-Accion-12-9.pdf",
                "PLAN DE ACCIÓN 12/9",
                "Prompts de carruseles + qué filmar hoy + qué falta para abrir el Instagram",
                "Solo con Sabor · Plan del día",
                "Plan de Accion 12-9 - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("PLAN DE ACCIÓN — SÁBADO 12/9", MOBILE_H1))
S.append(Paragraph(
    "Todo lo de hoy en un solo lugar: los 4 prompts de carruseles, que filmar al mediodia (con "
    "el guion adentro), que hace falta para abrir el Instagram a la tarde, y el estado completo "
    "de los 15 posteos con lo de hoy ya incorporado.",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>Orden sugerido del dia</b></font><br/>'
    '<font color="#f7d7d2" size="9">1) Filmar Fijado y Epifania (seccion 2) · 2) Editarlos junto '
    'con el #9 · 3) Mientras tanto, mandar los 4 prompts de carruseles (seccion 1) a Canva/Design '
    '· 4) A la tarde, abrir el Instagram con la seccion 3.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/PLAN-DE-ACCION-12-9.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Plan-de-Accion-12-9.pdf")
