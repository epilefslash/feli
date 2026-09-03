# -*- coding: utf-8 -*-
"""Arma el PDF de la auditoria del Modulo 1 (Estudiante Ideal) contra la memoria del proyecto.

Fuente: entregables/contenido/MODULO-1-RESPONDIDO.md

Cruza las 4 variables del negocio + las 4 partes del autoanalisis + las 12 preguntas de la Guia
de Estudiante Ideal + las etapas de Estudio de Campo y Analizar de Metodo Flow, contra lo que ya
esta resuelto en la memoria, para llegar a la reunion del 8/9 con Nico sabiendo que esta cerrado
y que falta -- un checklist de campo (encuestas, competencia, valores), no contenido nuevo.
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Modulo-1-Estudiante-Ideal-Respondido.pdf",
                "MÓDULO 1 — RESPONDIDO",
                "Autoanálisis, Estudio de Campo y Analizar, cruzados contra la memoria del proyecto",
                "Solo con Sabor · Módulo 1",
                "Modulo 1 respondido - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("MÓDULO 1 — RESPONDIDO", MOBILE_H1))
S.append(Paragraph(
    "Las 4 variables del negocio, las 4 partes del Autoanálisis, las 12 preguntas de la Guía del "
    "Estudiante Ideal, y las etapas de Estudio de Campo y Analizar — todo el Módulo 1 de Método "
    "Flow, cruzado contra lo que ya está escrito en la memoria del proyecto. Para la reunión del "
    "lunes 8/9 con Nico.", MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>El resultado corto</b></font><br/>'
    '<font color="#f7d7d2" size="9">La mayor parte del Modulo 1 ya tiene respuesta real en la '
    'memoria del proyecto. Lo que falta es trabajo de campo -- encuestar 5-10 alumnos, mapear la '
    'competencia -- e introspeccion corta sobre valores propios. Cero contenido nuevo que inventar. '
    'El checklist completo, en orden, esta al final.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/MODULO-1-RESPONDIDO.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Modulo-1-Estudiante-Ideal-Respondido.pdf")
