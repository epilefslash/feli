# -*- coding: utf-8 -*-
"""Arma el PDF del plan de los 15 primeros posteos + los 4 guiones de contenido nuevos.

Fuente: entregables/contenido/PLAN-15-POSTEOS.md

Sale de auditar la Hoja de Ruta de Metodo Flow Music (1/9) contra el stock real de contenido:
Nico pide una composicion exacta para los primeros 15 posteos y faltaban 4 categorias enteras
(Epifania, StoryTelling en foto, posteo de 2 pasos, 2 testimonios). El documento trae los
guiones nuevos, el orden de publicacion y la lista de lo que hay que producir.
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Plan-15-Posteos-y-Guiones-Nuevos.pdf",
                "LOS 15 PRIMEROS POSTEOS",
                "Guiones nuevos - orden de publicacion - que falta producir",
                "Solo con Sabor - Plan de contenido",
                "Plan de contenido - Metodo Flow")
W = doc.width
S = []

S.append(Paragraph("LOS 15 PRIMEROS POSTEOS", MOBILE_H1))
S.append(Paragraph(
    "La Hoja de Ruta de Metodo Flow Music pide una composicion exacta para los primeros 15 posteos "
    "del perfil. Auditada contra el stock real de contenido, aparecieron cuatro categorias que no "
    "existian en nuestro marco de trabajo. Este documento trae los guiones de esas cuatro, el orden "
    "de publicacion de los 15, y la lista de lo que falta producir.", MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>Como usar esto</b></font><br/>'
    '<font color="#f7d7d2" size="9">Los bloques en recuadro son texto para decir o publicar tal cual. '
    'El guion de la Epifania tiene 4 blancos entre corchetes: hay que llenarlos con datos reales '
    'antes de grabar, y la seccion que sigue al guion explica como. El orden de los 15 esta en la '
    'seccion 5 y lo que hay que producir, priorizado, en la 6.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/PLAN-15-POSTEOS.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Plan-15-Posteos-y-Guiones-Nuevos.pdf")
