# -*- coding: utf-8 -*-
"""Arma el PDF consolidado final: todo lo pendiente de Modulos 1 y 2, clasificado y con tiempos.

Fuente: entregables/contenido/CIERRE-MODULOS-1-Y-2.md

Junta los checklists de MODULO-1-RESPONDIDO.md y MODULO-2-RESPONDIDO.md + lo que sumaron los
ultimos 2 documentos (Vehiculo, prompts ChatGPT), clasificado en 5 categorias (pensar solo /
investigar / campo-depende-de-otros / depende-de-campo / preguntas para la reunion) y repartido
en el calendario real de Feli: jueves a la noche, viernes AM, sabado-domingo, lunes AM antes de
la reunion con Nico a las 12:30.
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Cierre-Modulos-1-y-2.pdf",
                "CIERRE MÓDULOS 1 Y 2",
                "Todo lo pendiente, clasificado, con tiempos y repartido en tu calendario real",
                "Solo con Sabor · Para el lunes con Nico",
                "Cierre Modulos 1 y 2 - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("CIERRE MÓDULOS 1 Y 2", MOBILE_H1))
S.append(Paragraph(
    "El consolidado final: todo lo que salió de los Módulos 1 y 2, clasificado por tipo de "
    "tarea, con tiempo estimado, y repartido en tu calendario real hasta el lunes 12:30.",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>El golazo, resumido</b></font><br/>'
    '<font color="#f7d7d2" size="9">Todo lo que depende solo de vos entra en un bloque de '
    '2 a 2.5 horas -- cabe entero en la manana del viernes. El resto (las encuestas a alumnos) '
    'tiene reloj propio: mandala cuanto antes, no el domingo a la noche. El detalle categoria '
    'por categoria y el reparto dia por dia estan mas abajo.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/CIERRE-MODULOS-1-Y-2.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Cierre-Modulos-1-y-2.pdf")
