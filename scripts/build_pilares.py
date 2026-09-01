# -*- coding: utf-8 -*-
"""Arma el PDF de pilares y micro pasos, en el formato que pide la Hoja de Ruta de Metodo Flow.

Fuente: entregables/contenido/PILARES-Y-MICROPASOS.md

Es el entregable del bloque "Estructurar Programa de Alto Valor" para llevar al Onboarding. No
crea nada nuevo: traduce el programa que ya existe (3 hitos, 53 ejercicios, 4 cuadernillos) al
vocabulario del metodo, para no gastar en rehacer las 2 semanas que el calendario le asigna.
"""
from reportlab.platypus import Paragraph, Spacer

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Pilares-y-Micropasos-Solo-con-Sabor.pdf",
                "PROGRAMA DE ALTO VALOR",
                "Pilares, micro pasos y vehiculo - Solo con Sabor",
                "Felipe Baya - Solo con Sabor",
                "Pilares y micropasos - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("SOLO CON SABOR", MOBILE_H1))
S.append(Paragraph(
    "Programa grupal de improvisacion en rock sobre la pentatonica menor. 12 semanas, "
    "cohortes de 4 a 6 alumnos. Este documento es el bloque <b>Estructurar Programa de Alto Valor</b> "
    "de la hoja de ruta: estudiante ideal, transformacion, pilares, micro pasos y vehiculo.",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>Estado</b></font><br/>'
    '<font color="#f7d7d2" size="9">El contenido pedagogico tiene una primera version terminada y '
    'auditada: 4 cuadernillos con partitura y tablatura reales, 59 ejercicios de numeracion corrida, '
    'mas un anexo de ritmo. Falta produccion y distribucion, y sigue abierto a que el equipo aporte '
    'o ajuste el diseno. La pregunta abierta esta al final.</font>', W))
S.append(Spacer(1, 10))

with open("entregables/contenido/PILARES-Y-MICROPASOS.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Pilares-y-Micropasos-Solo-con-Sabor.pdf")
