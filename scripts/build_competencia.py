# -*- coding: utf-8 -*-
"""Arma el PDF del analisis de competencia real (Modulo 1, pregunta 12).

Fuente: entregables/contenido/ANALISIS-COMPETENCIA.md

Investigacion real hecha con 4 busquedas independientes en paralelo (workflow), 53 items crudos
consolidados a 5 referentes + 5 programas similares + benchmark de precio. Ningun dato inventado:
donde no se encontro precio/info real en la busqueda, el documento dice "no encontrado" en vez de
una cifra fabricada.
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Analisis-de-Competencia.pdf",
                "ANÁLISIS DE COMPETENCIA",
                "5 referentes + 5 programas similares, con precio real donde se encontró",
                "Solo con Sabor · Módulo 1, pregunta 12",
                "Analisis de competencia - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("ANÁLISIS DE COMPETENCIA", MOBILE_H1))
S.append(Paragraph(
    "El ítem que más veces pidió el material de Nico (pregunta 12 del Módulo 1, y otra vez en la "
    "Estructuración del Módulo 2). Investigación real: 4 búsquedas independientes en paralelo, "
    "53 items crudos consolidados acá.", MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>El hallazgo que mas importa</b></font><br/>'
    '<font color="#f7d7d2" size="9">Andy Kligman -- la cuenta que ya tenias anotada como '
    'INSPIRACION de formato de Instagram -- aparecio en la busqueda como COMPETIDOR real: '
    'mismo pais, mismo idioma, vende clases de improvisacion por DM. Y sobre precio: USD 600 '
    'no tiene un comparable directo en el mercado -- cae entre los cursos grabados baratos y '
    'la mentoria boutique carisima, sin nadie en el medio con tu mismo formato.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/ANALISIS-COMPETENCIA.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Analisis-de-Competencia.pdf")
