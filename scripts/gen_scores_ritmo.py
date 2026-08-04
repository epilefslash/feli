# -*- coding: utf-8 -*-
"""Genera las partituras del ANEXO DE RITMO (ejercicios A, B, C).

Salida: ./partituras/rNN.cropped.png

El anexo corre en paralelo al Hito 2, junto con el módulo de ritmo basado en
Pozzoli. Por eso los ejercicios se numeran con LETRAS y no con números: la
numeración corrida 1-59 de los cuadernillos no se toca.

La consigna de todo el anexo: **las notas no cambian nunca**. En cada ejercicio
la tablatura repite los mismos trastes y lo único que se mueve es la figura. Es
el mismo truco del ejercicio 46 del Hito 3 (un lick en las 5 cajas) pero en el
otro eje: si aquel probaba que un lick no es un lugar, éste prueba que tampoco
es una velocidad.

La celda usada en todos: DO-LA-SOL-MI descendente en la caja 1
  (1a cuerda 8 y 5, 2a cuerda 8 y 5) = c'' a' g' e'
"""
from gen_scores import render

EJ = {}

# ------------------------------------------------------- A) las 3 velocidades
# Los mismos 4 trastes, tres veces. Lo que cambia es cuánto compás ocupan — y por
# lo tanto cuánto silencio queda después. Los silencios están escritos a propósito:
# son el contenido del ejercicio, no un relleno.
EJ["r01"] = r"""
  c''4\1^\markup{\bold "NEGRAS · 4 pulsos"} a'\1 g'\2 e'\2 |
  c''8\1^\markup{\bold "CORCHEAS · 2 + 2 de silencio"} a'\1 g'\2 e'\2 r2 |
  c''16\1^\markup{\bold "SEMIS · 1 + 3 de silencio"} a'\1 g'\2 e'\2 r4 r2 |
"""

# ------------------------------------------------------- B) el tresillo
# El árbol parte en 2. El tresillo parte en 3, y por eso no entra en el árbol.
# Las mismas 6 notas: en corcheas ocupan 3 pulsos, atresilladas ocupan 2.
EJ["r02"] = r"""
  c''8\1^\markup{\bold "6 corcheas = 3 pulsos"} a'\1 g'\2 e'\2 d'\3 c'\3 r4 |
  \tuplet 3/2 { c''8\1^\markup{\bold "las MISMAS 6 notas en tresillos = 2 pulsos"} a'\1 g'\2 }
  \tuplet 3/2 { e'8\2 d'\3 c'\3 } r2 |
"""

# ------------------------------------------------------- C) recto vs swing
# El swing no es una figura distinta: es la MISMA corchea corrida de lugar. Se
# escribe como negra + corchea dentro de un tresillo (larga-corta). Por eso va
# aparte del árbol: el árbol dice qué figura usás, el swing dice dónde cae.
EJ["r03"] = r"""
  c''8\1^\markup{\bold "RECTO · las dos corcheas duran igual"} a'\1 g'\2 e'\2 d'\3 c'\3 a4\4 |
  \tuplet 3/2 { c''4\1^\markup{\bold "SWING · larga-corta, mismas notas"} a'8\1 }
  \tuplet 3/2 { g'4\2 e'8\2 }
  \tuplet 3/2 { d'4\3 c'8\3 } a4\4 |
"""

if __name__ == "__main__":
    fails = [k for k in sorted(EJ) if not render(k, EJ[k])]
    print("\nFallaron:", fails if fails else "ninguno")
