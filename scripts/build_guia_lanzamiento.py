# -*- coding: utf-8 -*-
"""Arma el PDF de la guia de lanzamiento de @felibayamenor.

Fuente: entregables/contenido/GUIA-LANZAMIENTO.md

Todo lo que tiene que existir (perfil, destacadas, los 3 primeros posteos) antes de abrir el
Instagram al publico, en orden, con el texto listo para copiar en cada paso.
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Guia-de-Lanzamiento-felibayamenor.pdf",
                "GUÍA DE LANZAMIENTO",
                "Todo lo que tiene que estar listo antes de abrir @felibayamenor",
                "@felibayamenor · Guía de lanzamiento",
                "Guia de lanzamiento - felibayamenor")
W = doc.width
S = []

S.append(Paragraph("@felibayamenor", MOBILE_H1))
S.append(Paragraph(
    "La checklist completa, en orden, de todo lo que tiene que existir antes de que el perfil "
    "sea público: el perfil (bio, foto, usuario), las destacadas con el texto ya escrito, y los "
    "3 primeros videos con sus guiones. Se lee de arriba hacia abajo y se va tildando.",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>Los 2 niveles</b></font><br/>'
    '<font color="#f7d7d2" size="9">🔴 NO NEGOCIABLE — sin esto no se abre el perfil. '
    '🟡 PUEDE ESPERAR — se completa en las semanas siguientes, no bloquea el día 1. '
    'El Paso 0 tiene el estado real de hoy, y el checklist final está al cierre del documento.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/GUIA-LANZAMIENTO.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Guia-de-Lanzamiento-felibayamenor.pdf")
