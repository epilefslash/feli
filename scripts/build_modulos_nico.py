# -*- coding: utf-8 -*-
"""Arma el PDF en primera persona, para entregarle a Nico, contestando punto por punto todo lo
que piden los Modulos 1 y 2 (Identificar Estudiante Ideal / Estructurar Programa de Alto Valor).

Distinto de Lo-Que-Tengo-Resuelto.pdf (ese es para que Feli lo internalice antes de la reunion,
con lenguaje de auditoria interna). Este es el documento que se le entrega A Nico: mismo contenido
de fondo, pero escrito como la tarea contestada, sin "gaps"/checkmarks de auditoria interna.

Fuente: entregables/contenido/MODULOS-1-2-PARA-NICO.md
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Modulos-1-y-2-Para-Nico.pdf",
                "MÓDULOS 1 Y 2 — MI RESPUESTA",
                "Identificar Estudiante Ideal · Estructurar Programa de Alto Valor",
                "Solo con Sabor · Para Nico",
                "Modulos 1 y 2 para Nico - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("MÓDULOS 1 Y 2 — MI RESPUESTA", MOBILE_H1))
S.append(Paragraph(
    "Todo lo que piden los Módulos 1 y 2, contestado punto por punto.",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>Cómo leer esto</b></font><br/>'
    '<font color="#f7d7d2" size="9">Es mi tarea contestada, no una auditoria -- donde ya tengo '
    'la respuesta la escribo directo, y donde me falta algo lo digo tal cual. Las 5 preguntas '
    'que quiero resolver con vos, no solo, quedan al final.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/MODULOS-1-2-PARA-NICO.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Modulos-1-y-2-Para-Nico.pdf")
