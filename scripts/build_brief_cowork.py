# -*- coding: utf-8 -*-
"""Arma el PDF del BRIEF PARA COWORK -- el documento autosuficiente que Feli pega como primer
mensaje en su sesion de Claude Cowork dedicada a contenido.

Fuente: entregables/contenido/BRIEF-PARA-COWORK.md
Decisiones que resume: memoria/05 SS53 (los 38 ganchos + la maquina de reciclado) y SS54 (el
sistema de produccion por lotes).
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Brief-para-Cowork.pdf",
                "BRIEF DE CONTENIDO",
                "Para pegar en la sesión de Cowork · autosuficiente",
                "Solo con Sabor · Brief para Cowork",
                "Brief para Cowork - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("EL BRIEF, DE UNA SOLA VEZ", MOBILE_H1))
S.append(Paragraph(
    "Todo lo que una sesión nueva necesita saber para producir contenido sin volver a preguntar: "
    "quién sos, a quién le hablás, las 6 reglas de copy que no se negocian, la estructura de cada "
    "formato, las 38 fórmulas de gancho y el sistema de trabajo por lotes.",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>La regla que sostiene todo el sistema</b></font><br/>'
    '<font color="#f7d7d2" size="9">Nunca publiques lo que filmaste esta semana. Publicás de lo que '
    'ya está editado del ciclo anterior — eso te da 2 semanas de aire, y es lo que hace que una '
    'semana mala no corte la racha.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/BRIEF-PARA-COWORK.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Brief-para-Cowork.pdf")
