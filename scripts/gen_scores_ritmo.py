# -*- coding: utf-8 -*-
"""Genera las partituras del ANEXO DE RITMO (ejercicios A a G).

Salida: ./partituras/rNN.cropped.png

El anexo corre en paralelo al Hito 2, junto con el módulo de ritmo basado en
Pozzoli. Por eso los ejercicios se numeran con LETRAS y no con números: la
numeración corrida 1-59 de los cuadernillos no se toca.

  A, B, C -> el árbol de figuras, el tresillo y el swing.
  D a G   -> síncopa, anticipación (el push) y el puntillo.

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

# ------------------------------------------------------- D) el número y el "y"
# UNA sola nota, a propósito: si hay que digitar algo, la atención se va a los
# dedos y no al lugar del pulso, que es lo único que se está enseñando acá.
EJ["r04"] = r"""
  c''4\1^\markup{\bold "EN EL NÚMERO · mano y pie bajan juntos"} c''\1 c''\1 c''\1 |
  r8 c''8\1^\markup{\bold "EN EL 'Y' · tocás con el pie ARRIBA"} r8 c''\1 r8 c''\1 r8 c''\1 |
"""

# ------------------------------------------------------- E) mover, no agregar
# El compás 2 está MAL a propósito: es el error que comete casi todo el mundo
# —anticipar la nota y volver a pegarla en el tiempo fuerte—, y se detecta
# contando los números de la tablatura (5 contra 4). El rótulo "MAL" vive dentro
# de la partitura, no sólo en el texto: si Design lo redibuja, se nota.
EJ["r05"] = r"""
  c''4\1^\markup{\bold "1 · A TIEMPO · el LA cae en el 2"} a'\1 g'\2 e'\2 |
  c''8\1^\markup{\bold "2 · MAL · entra antes y la REPITE"} a'\1 a'4\1 g'\2 e'\2 |
  c''8\1^\markup{\bold "3 · SÍNCOPA · entra antes y NO la repite"} a'\1 ~ a'4\1 g'\2 e'\2 |
"""

# ------------------------------------------------------- F) el push
# Las MISMAS 7 notas y las MISMAS figuras las dos veces (8-5-8-5-7-5-7). Lo único
# que cambia es que la segunda arranca medio tiempo antes, y por eso la llegada
# se liga sobre la barra. Es la primera ligadura de todo el repo que cruza un
# compás. El último compás queda con la tablatura VACÍA: ahí cae el 1.
EJ["r06"] = r"""
  r4 c''8\1^\markup{\bold "RECTA · la llegada cae justo en el 1"} a'\1 g'\2 e'\2 d'\3 c'\3 |
  a1\4 |
  r8 c''8\1^\markup{\bold "ANTICIPADA · todo medio tiempo antes"} a'\1 g'\2 e'\2 d'\3 c'\3 a8\4 ~ |
  a1\4^\markup{\bold "el 1 no se toca: ya venías sonando"} |
"""

# ------------------------------------------------------- G) el puntillo
# Compases 1 y 2 suenan idéntico y sus tablaturas son idénticas (8-5-8): el
# puntillo no es una figura nueva, es la forma corta de escribir una ligadura.
# Y como suma la mitad en vez de partirla, corre todo lo que sigue al contratiempo.
#
# OJO con el 3+3+2: es el compás 2 (1,5 + 1,5 + 1 = 3+3+2 corcheas), NO otro.
# Una versión anterior rotulaba como "3+3+2" un compás que era 3+3+1+1 y encima
# tenía 4 ataques, lo que desmentía la frase de la caja ("el más sincopado es el
# que tiene menos notas"). El compás 3 ahora es el MISMO 3+3+2 bajando: prueba
# que es un patrón transportable y mantiene los 3 ataques.
EJ["r07"] = r"""
  c''4\1^\markup{\bold "1 · escrito con ligaduras"} ~ c''8\1 a'4\1 ~ a'8\1 g'4\2 |
  c''4.\1^\markup{\bold "2 · lo MISMO con puntillos = el 3+3+2"} a'4.\1 g'4\2 |
  g'4.\2^\markup{\bold "3 · el mismo 3+3+2, bajando"} e'4.\2 d'4\3 |
"""

if __name__ == "__main__":
    fails = [k for k in sorted(EJ) if not render(k, EJ[k])]
    print("\nFallaron:", fails if fails else "ninguno")
