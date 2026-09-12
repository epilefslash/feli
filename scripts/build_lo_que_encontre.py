# -*- coding: utf-8 -*-
"""Arma el PDF de "Lo que encontre cuando fui a chequear" -- version en primera persona (de Feli
para un tercero curioso) del respaldo academico del metodo. Mismo contenido verificado que
Respaldo-Academico-Metodo.pdf, pero contado como carta/historia, con ejemplos del programa y venta
sutil -- pensado para compartir por DM, historia o carta de ventas, no para uso interno.

No es un reemplazo de Respaldo-Academico-Metodo.pdf (ese sigue siendo la version auditora, con
citas completas y veredictos, para uso interno / con Nico). Este es la version de cara al publico.

Fuente: entregables/contenido/Lo-Que-Encontre-Cuando-Fui-A-Chequear.md
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak

from cuadernillo_comun import documento, caja_oscura
from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY

doc = documento("Lo-Que-Encontre-Cuando-Fui-A-Chequear.pdf",
                "LO QUE ENCONTRÉ",
                "Por qué el método está armado así — contado por mí, con lo que fui a chequear",
                "Solo con Sabor · Feli",
                "Lo Que Encontre - Solo con Sabor")
W = doc.width
S = []

S.append(Paragraph("LO QUE ENCONTRÉ CUANDO FUI A CHEQUEAR", MOBILE_H1))
S.append(Paragraph(
    "Por qué el método está armado así — contado en primera persona, con lo que encontré cuando "
    "fui a ver si mi intuición tenía compañía.",
    MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>Qué es esto</b></font><br/>'
    '<font color="#f7d7d2" size="9">Es la carta que le mandaria a alguien curioso que me pregunta '
    'si el metodo tiene sustento o es puro carisma. Mismo contenido verificado que el documento '
    'interno, pero en mi voz, con ejemplos del programa, y honesto sobre lo que todavia no tiene '
    'respaldo solido.</font>', W))
S.append(PageBreak())

with open("entregables/contenido/Lo-Que-Encontre-Cuando-Fui-A-Chequear.md", encoding="utf-8") as f:
    render_markdown(f.read(), S, W)

doc.build(S)
print("OK Lo-Que-Encontre-Cuando-Fui-A-Chequear.pdf")
