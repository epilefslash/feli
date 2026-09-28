# -*- coding: utf-8 -*-
"""Arma el PDF de la guia de Ads + comunicacion para el estudio de grabacion de Andres y Wopler.
No es parte del proyecto Solo con Sabor -- favor puntual de Feli para un amigo.

Fuente: entregables/otros/GUIA-ADS-ANDRES-WOPLER.md
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

import cuadernillo_comun
from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

# Este documento es para el estudio de Andres y Wopler, no para Solo con Sabor -- la plantilla
# compartida trae el handle de Feli hardcodeado en la esquina superior. Se pisa aca para que no
# se filtre en un PDF que va para otro negocio.
cuadernillo_comun.IG = "Rosario Centro"

doc = documento("Guia-Ads-Estudio-Andres-Wopler.pdf",
                "GUÍA DE ADS",
                "Cómo usar Promocionar de Instagram + cómo comunicar el servicio",
                "Estudio de Grabación · Rosario Centro",
                "Guia de Ads - Estudio Andres y Wopler")
W = doc.width
S = []

S.append(Paragraph("GUÍA RÁPIDA DE PUBLICIDAD", MOBILE_H1))
S.append(Paragraph(
    "Cómo usar el botón Promocionar de Instagram paso a paso, y 3 ideas simples de cómo "
    "comunicar el servicio para que la publicidad tenga algo bueno que empujar.",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>Lo esencial en una linea</b></font><br/>'
    '<font color="#f7d7d2" size="9">Objetivo "Mas mensajes" -- audiencia manual, Rosario centro, '
    '5-10 km -- USD 3-5/dia, minimo 5-7 dias -- y una sola promesa clara, repetida siempre '
    'igual.</font>', W))
S.append(PageBreak())

with open("entregables/otros/GUIA-ADS-ANDRES-WOPLER.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Guia-Ads-Estudio-Andres-Wopler.pdf")
