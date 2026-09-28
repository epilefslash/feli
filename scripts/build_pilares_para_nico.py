# -*- coding: utf-8 -*-
"""Version de Pilares-y-Micropasos-Solo-con-Sabor.pdf para compartir directamente con Nico --
sin las notas de proceso interno (donde vive cada archivo, que esta auditado, etc).

Fuente: entregables/contenido/PILARES-Y-MICROPASOS-PARA-NICO.md
"""
from reportlab.platypus import Paragraph, Spacer

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Pilares-y-Micropasos-Para-Nico.pdf",
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
    '<font color="#f7d7d2" size="9">El contenido pedagogico tiene una primera version terminada: '
    '5 documentos con partitura y tablatura reales, 59 ejercicios de numeracion corrida, mas dos '
    'modulos de ritmo. Falta produccion y distribucion, y sigue abierto a que el equipo aporte o '
    'ajuste el diseno. La pregunta abierta esta al final.</font>', W))
S.append(Spacer(1, 10))

with open("entregables/contenido/PILARES-Y-MICROPASOS-PARA-NICO.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Pilares-y-Micropasos-Para-Nico.pdf")
