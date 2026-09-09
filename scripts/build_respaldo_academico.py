# -*- coding: utf-8 -*-
"""Arma el PDF del respaldo academico del metodo -- que principios pedagogicos de "Solo con Sabor"
tienen fuente academica real y verificable, y cuales no. Para citar con autoridad en reels, carta
de ventas, y con Nico.

Investigado con WebSearch real (no inventado) en una sesion aparte -- ver
memoria/10-notas-tecnicas-asistente.md si se documenta ahi, y el propio documento trae su nota
metodologica arriba.

Fuente: entregables/contenido/RESPALDO-ACADEMICO-METODO.md
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Respaldo-Academico-Metodo.pdf",
                "RESPALDO ACADÉMICO",
                "Qué principios del método están estudiados, y qué no — con fuentes reales",
                "Solo con Sabor · Investigación verificada",
                "Respaldo Academico - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("RESPALDO ACADÉMICO DEL MÉTODO", MOBILE_H1))
S.append(Paragraph(
    "Qué principios pedagógicos de \"Solo con Sabor\" tienen fuente académica real y verificable "
    "— y cuáles no. Para citar con autoridad, del mismo modo que se citaría a Berklee.",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>Antes de citar algo de acá en un reel</b></font><br/>'
    '<font color="#f7d7d2" size="9">Cada cita salio de una busqueda real, verificada. Las marcadas '
    '"FUERTE Y DIRECTA" se pueden citar tal cual. Las "RAZONABLE PERO INDIRECTA" dan contexto, pero '
    'no digas que el estudio prueba la tecnica puntual del programa. Nada de esto midio "Solo con '
    'Sabor" -- son estudios que el programa aplica sin saberlo, por experiencia propia de Feli. Contalo '
    'asi, no al reves.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/RESPALDO-ACADEMICO-METODO.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Respaldo-Academico-Metodo.pdf")
