# -*- coding: utf-8 -*-
"""Arma el PDF en primera persona de todo lo que Feli ya tiene resuelto de los Modulos 1 y 2 -
para internalizar, no para revisar contra Nico (eso es Resumen-para-el-Lunes.pdf).

Fuente: entregables/contenido/RESUELTO-PRIMERA-PERSONA.md
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Lo-Que-Tengo-Resuelto.pdf",
                "LO QUE YA TENGO RESUELTO",
                "Módulos 1 y 2, en primera persona, punto por punto — para internalizarlo",
                "Solo con Sabor · Para leer antes del lunes",
                "Lo Que Tengo Resuelto - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("LO QUE YA TENGO RESUELTO", MOBILE_H1))
S.append(Paragraph(
    "Todo lo que está cerrado de los Módulos 1 y 2, escrito en primera persona, punto por punto — "
    "para leerlo y sentirlo mío antes de la reunión con Nico.",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>Esto es solo lo cerrado</b></font><br/>'
    '<font color="#f7d7d2" size="9">Lo que todavia esta abierto (las 4 preguntas para Nico) '
    'no esta aca -- eso vive en Resumen-para-el-Lunes.pdf. Esto es unicamente lo que ya '
    'resolvi, para leerlo antes de entrar a la reunion.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/RESUELTO-PRIMERA-PERSONA.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Lo-Que-Tengo-Resuelto.pdf")
