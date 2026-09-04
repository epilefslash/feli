# -*- coding: utf-8 -*-
"""Arma el PDF de repaso final para el lunes con Nico: donde quedamos + Modulo 1 y 2 punto por
punto (que pide Nico, cual es nuestra respuesta) + el analisis del techo de edad.

Fuente: entregables/contenido/RESUMEN-LUNES-NICO.md
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Resumen-para-el-Lunes.pdf",
                "RESUMEN PARA EL LUNES",
                "Donde quedamos + Modulo 1 y 2 punto por punto, con nuestra respuesta a cada cosa",
                "Solo con Sabor · Repaso final antes de Nico",
                "Resumen para el Lunes - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("RESUMEN PARA EL LUNES", MOBILE_H1))
S.append(Paragraph(
    "Todo junto: el estado real hoy, el plan de filmación del sábado, y un cuadro punto por "
    "punto de todo lo que piden los Módulos 1 y 2 de Nico con nuestra respuesta a cada cosa — "
    "para repasar y ajustar con tus palabras donde quieras.",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>Estado en una línea</b></font><br/>'
    '<font color="#f7d7d2" size="9">Módulos 1 y 2 cerrados. Solo quedan 4 preguntas para '
    'resolver CON Nico el lunes. Contenido: video #9 filmado, sábado se filma Fijado + '
    'Epifanía, bio final lista.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/RESUMEN-LUNES-NICO.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Resumen-para-el-Lunes.pdf")
