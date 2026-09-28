# -*- coding: utf-8 -*-
"""Arma los 3 PDF de bienvenida para el alumno, uno por hito -- van en la carpeta de cada
hito junto al cuadernillo. Explican por donde empezar y que es cada subcarpeta, sin repetir
la rutina diaria / reglas que ya estan adentro de cada cuadernillo principal.

Fuente: entregables/contenido/ONBOARDING-HITO{1,2,3}.md
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

HITOS = [
    ("1", "El Mapa", "Onboarding-Hito1-El-Mapa.pdf", "ONBOARDING-HITO1.md"),
    ("2", "El Sabor", "Onboarding-Hito2-El-Sabor.pdf", "ONBOARDING-HITO2.md"),
    ("3", "El Vocabulario", "Onboarding-Hito3-El-Vocabulario.pdf", "ONBOARDING-HITO3.md"),
]

for num, nombre, out, fuente in HITOS:
    doc = documento(out,
                    f"HITO {num} — {nombre.upper()}",
                    "Cómo aprovechar esta carpeta al máximo",
                    "Solo con Sabor · Guía de la carpeta",
                    f"Onboarding Hito {num} - Solo con Sabor")
    W = doc.width
    S = []
    S.append(Paragraph(f"HITO {num} — {nombre.upper()}", MOBILE_H1))
    S.append(Paragraph(
        "Antes de tocar nada: 2 minutos para saber por dónde arrancar y qué es cada carpeta.",
        MOBILE_BODY))
    S.append(Spacer(1, 8))
    S.append(PageBreak())
    with open(f"entregables/contenido/{fuente}", encoding="utf-8") as f:
        render_markdown(f.read(), S, W)
    doc.build(S)
    print(f"OK {out}")
