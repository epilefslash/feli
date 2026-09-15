# -*- coding: utf-8 -*-
"""Arma el PDF de la auditoria del Modulo 2 (Programa de Alto Valor) contra la memoria del proyecto.

Fuente: entregables/contenido/MODULO-2-RESPONDIDO.md

Cruza la plantilla de Programa de Alto Valor, la Ecuacion de Valor, los elementos que hacen pagar
mas, el mindset de precio y la estructuracion (infierno/cielo, modulos/lecciones) contra lo que ya
esta resuelto en la memoria. El hallazgo principal: una posible simplificacion del plan de delivery
(memoria/02 sec.28-BIS) si Nico confirma que los cuadernillos ya escritos alcanzan como guion de
clase en vivo para la primera cohorte, sin necesidad de pregrabar antes de vender.
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Modulo-2-Programa-Alto-Valor-Respondido.pdf",
                "MÓDULO 2 — RESPONDIDO",
                "Programa de Alto Valor: plantilla, ecuación de valor y estructuración, vs la memoria",
                "Solo con Sabor · Módulo 2",
                "Modulo 2 respondido - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("MÓDULO 2 — RESPONDIDO", MOBILE_H1))
S.append(Paragraph(
    "La Plantilla de Programa de Alto Valor, la Ecuación de Valor, los elementos que hacen pagar "
    "más, el mindset de precio y la Estructuración (infierno/cielo, módulos/lecciones) — el "
    "Módulo 2 de Método Flow, cruzado contra lo que ya está escrito en la memoria del proyecto. "
    "Para la reunión del lunes 8/9 con Nico.", MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>El hallazgo principal</b></font><br/>'
    '<font color="#f7d7d2" size="9">No es un gap, es una simplificacion posible: el material sugiere '
    'entregar en vivo semana a semana con la primera cohorte, usando los cuadernillos ya escritos '
    'como guion, y recien grabar el pregrabado definitivo despues, con feedback real. Eso sacaria de '
    'encima toda la tarea de grabar antes de vender. Detalle al principio del documento.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/MODULO-2-RESPONDIDO.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Modulo-2-Programa-Alto-Valor-Respondido.pdf")
