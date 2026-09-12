# -*- coding: utf-8 -*-
"""Arma el PDF de las 12 semanas completas (los 3 hitos + el ritmo transversal en una sola tabla),
para que Feli tenga el mapa entero antes de arrancar a grabar el pregrabado.

Fuente: entregables/contenido/Programa-12-Semanas-Con-Ritmo.md
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Programa-12-Semanas-Con-Ritmo.pdf",
                "LAS 12 SEMANAS",
                "Tema, cuadernillo, repertorio, improvisacion y ritmo -- todo junto",
                "Solo con Sabor",
                "Programa 12 Semanas con Ritmo")
W = doc.width
S = []

S.append(Paragraph("LAS 12 SEMANAS, COMPLETAS", MOBILE_H1))
S.append(Paragraph(
    "El mapa semana a semana de los 3 hitos, con que ejercicios del cuadernillo usa cada una, el "
    "solo de referencia, la consigna de improvisacion en vivo, y donde entra el ritmo transversal.",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>Antes de usar esto para grabar</b></font><br/>'
    '<font color="#f7d7d2" size="9">La columna de ritmo es una PROPUESTA, no algo ya decidido -- '
    'nunca se fijo semana por semana en el proyecto. El Mes 3 se reordeno (11/9): las escuelas '
    'britanica/americana se agrupan por lo que SON, no por el numero de ejercicio, porque rondas '
    'de correccion posteriores esparcieron las citas reales mas adelante en la numeracion. Queda '
    'UNA sola cosa pendiente de resolver antes de grabar todo (el solo de la semana 5) -- esta al '
    'final del documento, no la pases por alto.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/Programa-12-Semanas-Con-Ritmo.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Programa-12-Semanas-Con-Ritmo.pdf")
