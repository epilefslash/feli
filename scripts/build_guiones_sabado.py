# -*- coding: utf-8 -*-
"""Arma el PDF con los 3 guiones para filmar el sabado 13/9: Reel Fijado, Epifania, Vendedor
"Como que desaparece" - para tenerlos a mano en un solo documento.

Fuente: entregables/contenido/GUIONES-SABADO.md (extraido de memoria/04, secciones 26, 35, 23)
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Guiones-Sabado.pdf",
                "GUIONES DEL SÁBADO",
                "Reel Fijado + Epifanía + Vendedor “Como que desaparece”, listos para filmar",
                "Solo con Sabor · Para el 13/9",
                "Guiones Sabado - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("GUIONES DEL SÁBADO", MOBILE_H1))
S.append(Paragraph(
    "Los 3 guiones para la filmación del 13/9, palabra por palabra, con ficha técnica, guía de "
    "tono, copy del post y hashtags — todo en un solo documento para tener a mano.",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>Orden de filmación</b></font><br/>'
    '<font color="#f7d7d2" size="9">1. Reel Fijado (el mas simple, para entrar en calor) '
    '&#8594; 2. Epifania (ensayala en voz alta antes de prender la camara) '
    '&#8594; 3. Vendedor, si sobra tiempo (no es urgente para el Dia 0).</font>', W))
S.append(PageBreak())

with open("entregables/contenido/GUIONES-SABADO.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Guiones-Sabado.pdf")
