# -*- coding: utf-8 -*-
"""Arma el PDF de la auditoria del Modulo 1 (Estudiante Ideal) contra la memoria del proyecto.

Fuente: entregables/contenido/MODULO-1-RESPONDIDO.md

Cruza las 12 preguntas de la Guia de Estudiante Ideal de Metodo Flow + las 4 variables del
negocio contra lo que ya esta resuelto en la memoria, para llegar a la reunion del 8/9 con Nico
sabiendo que esta cerrado y que faltan (4 gaps reales, ninguno musical).
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Modulo-1-Estudiante-Ideal-Respondido.pdf",
                "MÓDULO 1 — RESPONDIDO",
                "Las 12 preguntas del Estudiante Ideal, cruzadas contra la memoria del proyecto",
                "Solo con Sabor · Módulo 1",
                "Modulo 1 respondido - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("MÓDULO 1 — RESPONDIDO", MOBILE_H1))
S.append(Paragraph(
    "Las 4 variables del negocio y las 12 preguntas de la Guía del Estudiante Ideal de Método "
    "Flow, cruzadas una por una contra lo que ya está escrito en la memoria del proyecto. Para "
    "la reunión del lunes con Nico.", MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>El resultado corto</b></font><br/>'
    '<font color="#f7d7d2" size="9">9 de las 12 preguntas ya tienen respuesta real en la memoria '
    'del proyecto, mas las 4 variables del negocio. Quedan 4 gaps genuinos (ninguno musical, el '
    'mas grande es el analisis de competencia). El detalle de cada uno esta al final.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/MODULO-1-RESPONDIDO.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Modulo-1-Estudiante-Ideal-Respondido.pdf")
