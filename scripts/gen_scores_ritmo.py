# -*- coding: utf-8 -*-
"""Genera las partituras del ANEXO DE RITMO (ejercicios A a J).

Salida: ./partituras/rNN.cropped.png

El anexo corre en paralelo al Hito 3 (el módulo de ritmo basado en Pozzoli, que
Feli produce aparte, se queda en el mes 2). Por eso los ejercicios se numeran con
LETRAS y no con números: la numeración corrida 1-59 de los cuadernillos no se toca.

  A, B, C -> el árbol de figuras, el tresillo (de corchea y de negra) y el swing.
  D a G   -> síncopa, anticipación (el push) y el puntillo.
  H       -> la escalera de desplazamiento (la celda entrando en 5 lugares).
  I       -> llamada y respuesta, el molde 1-2-1-3.
  J       -> el cierre: los nueve compases que encadenan todo el anexo.

La consigna de todo el anexo: **las notas no cambian nunca**. En cada ejercicio
la tablatura repite los mismos trastes y lo único que se mueve es la figura. Es
el mismo truco del ejercicio 46 del Hito 3 (un lick en las 5 cajas) pero en el
otro eje: si aquel probaba que un lick no es un lugar, éste prueba que tampoco
es una velocidad.

⚠️ LOS EJERCICIOS A-G VIVEN CASI ENTEROS EN LA CAJA 1, Y NO ES UN DESCUIDO. Es la
única forma de aislar la variable: si además de cambiar la figura cambiara la
posición, el alumno no sabría qué produjo el cambio de sonido. Mismo criterio que
mantiene juntas las tres versiones de los ej. 44 y 45 del Hito 3. No "arreglarlo"
subiendo esos ejercicios de caja: rompe el diseño.

Los ejercicios H, H-bis e I son otra cosa: son TRANSCRIPCIONES DE FELI importadas
del MusicXML (ver importar_musicxml.py), recorren de la cuerda al aire al traste 17
y traen notas cromáticas. Ahí la geografía es parte del contenido, no una variable
suelta. Con ellos el anexo quedó en 46% fuera de la caja 1 (era 98% adentro).

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
# Las mismas 6 notas, tres veces: en corcheas ocupan 3 pulsos, en tresillos de corchea
# 2, y en tresillos de NEGRA los 4 del compás.
#
# El tresillo de negra es el que más flota de los tres, porque es el único cuyas notas
# no coinciden con ningún número del compás salvo el 1. Es también la única figura del
# anexo que no estaba en ninguna de las 995 notas del programa.
EJ["r02"] = r"""
  c''8\1^\markup{\bold "6 corcheas = 3 pulsos"} a'\1 g'\2 e'\2 d'\3 c'\3 r4 |
  \tuplet 3/2 { c''8\1^\markup{\bold "las MISMAS 6 en tresillos de corchea = 2 pulsos"} a'\1 g'\2 }
  \tuplet 3/2 { e'8\2 d'\3 c'\3 } r2 |
  \tuplet 3/2 { c''4\1^\markup{\bold "y en tresillos de NEGRA = los 4 pulsos"} a'\1 g'\2 }
  \tuplet 3/2 { e'4\2 d'\3 c'\3 } |
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

# ----------------------------------- H) el reto de construccion de frases
# TRANSCRIPCION DE FELI (Guitar Pro -> MusicXML -> importar_musicxml.py).
# NO se re-tipeo a mano: se parseo el XML, asi que las alturas y las cuerdas son
# exactamente las que el escribio. Cinco ejercicios: la misma frase entrando en el
# 1, en el "y" del 1, en el 2, en el "y" del 2 y en el 3, mas un encadenado final.
# Las cuentas ("1 and 2 and") vienen del propio XML y se imprimen sobre el compas:
# el alumno LEE donde entrar en vez de contar silencios.
EJ["r08"] = r"""
  e8\5^\markup{\bold "1"} g8\4 a8\4 c'8\3 \grace d'32\3 e'8\3 g'8\2 a'8\2 c''8\2 |
  a'1\2 |
  r8^\markup{\bold "1"}^\markup{\bold "and"} e8\5 g8\4 a8\4 c'8\3 \grace d'32\3 e'8\3 g'8\2 a'8\2 |
  c''16\2 a'16\2 ~ a'8\2 ~ a'4\2 ~ a'2\2 |
  r4^\markup{\bold "1 and"}^\markup{\bold "2"} d'4\4 \tabSym \bendFull a'8\3 g'8\3 d'8\4 \tabSym \bendFull d'8\4 |
  c'4\4 a16\5^\markup{\bold\small "H"}( g16\5) e8\6 r2 |
  r4^\markup{\bold "1 and"}^\markup{\bold "2"}^\markup{\bold "and"} r8 d'8\4 \tabSym \bendFull a'8\3 g'8\3 d'8\4 \tabSym \bendFull d'8\4 |
  c'4\4 a16\5^\markup{\bold\small "H"}( g16\5) e8\6 r2 |
  r2^\markup{\bold "1 and 2 and"}^\markup{\bold "3"} g'8\2 \tabSym \bendFull a'8\2 dis'32\3 \glissando^\markup{\bold\small "sl."}( d'32\3^\markup{\bold\small "H"})( c'16\3) a8\4 |
  d'8\3 c'8\3 a16\4^\markup{\bold\small "H"}( g16\4) e8\5 g8\4 a8\4 ~ a4\4 |
  r2^\markup{\bold "1 and 2 and"}^\markup{\bold "3"}^\markup{\bold "and"} r8 g'8\2 \tabSym \bendFull a'8\2 g'8\2 |
  dis'32\3 \glissando^\markup{\bold\small "sl."}( d'32\3^\markup{\bold\small "H"})( c'16\3) a8\4 d'8\3 c'8\3 a16\4^\markup{\bold\small "H"}( g16\4) e8\5 g8\4 a8\4 |
  r2^\markup{\bold "1 and 2 and"}^\markup{\bold "3 and"}^\markup{\bold "4"} r4 e'8\3 g'8\2 |
  a'8\2 e'8\3 a'8\2 c''8\1 a'2\2 |
  r2^\markup{\bold "1 and 2 and"}^\markup{\bold "3 and"}^\markup{\bold "4"}^\markup{\bold "and"} r4 r8 e'8\3 |
  a'8\2 e'8\3 a'8\2 c''8\1 a'2\2 |
  r4 r2. |
  r4 r2. |
"""

# El encadenado final (EX5 del original de Feli): los cuatro puntos de entrada
# seguidos, sin parar. Va como partitura aparte porque los 34 compases juntos no
# entran en una pagina — y de paso queda mejor: primero se practican los cinco
# sueltos y recien despues se tocan de corrido.
EJ["r08b"] = r"""
  e8\5^\markup{\bold "1"} g8\4 a8\4 c'8\3 \grace d'32\3 e'8\3 g'8\2 a'8\2 c''8\2 |
  a'1\2 |
  r8^\markup{\bold "1"}^\markup{\bold "and"} e8\5 g8\4 a8\4 c'8\3 \grace d'32\3 e'8\3 g'8\2 a'8\2 |
  c''16\2 a'16\2 ~ a'8\2 ~ a'4\2 ~ a'2\2 |
  r4^\markup{\bold "1 and"}^\markup{\bold "2"} d'4\5 \tabSym \bendFull a'8\3 g'8\4 d'8\5 \tabSym \bendFull d'8\5 |
  c'4\5 a16\5^\markup{\bold\small "H"}( g16\5) e8\6 r2 |
  r4^\markup{\bold "1 and"}^\markup{\bold "2"}^\markup{\bold "and"} r8 d'8\5 \tabSym \bendFull a'8\3 g'8\4 d'8\5 \tabSym \bendFull d'8\5 |
  c'4\5 a16\5^\markup{\bold\small "H"}( g16\5) e8\6 r2 |
  r2^\markup{\bold "1 and 2 and"}^\markup{\bold "3"} g'8\3 \tabSym \bendFull a'8\2 dis'32\4 \glissando^\markup{\bold\small "sl."}( d'32\4^\markup{\bold\small "H"})( c'16\4) a8\5 |
  d'8\4 c'8\4 a16\5^\markup{\bold\small "H"}( g16\5) e8\6 g8\5 a8\5 ~ a4\5 |
  r2^\markup{\bold "1 and 2 and"}^\markup{\bold "3"}^\markup{\bold "and"} r8 g'8\3 \tabSym \bendFull a'8\2 g'8\3 |
  dis'32\4 \glissando^\markup{\bold\small "sl."}( d'32\4^\markup{\bold\small "H"})( c'16\4) a8\5 d'8\4 c'8\4 a16\5^\markup{\bold\small "H"}( g16\5) e8\6 g8\5 a8\5 |
  r2^\markup{\bold "1 and 2 and"}^\markup{\bold "3 and"}^\markup{\bold "4"} r4 e'8\3 g'8\2 |
  a'8\2 e'8\3 a'8\2 c''8\1 a'2\2 |
  r2^\markup{\bold "1 and 2 and"}^\markup{\bold "3 and"}^\markup{\bold "4"}^\markup{\bold "and"} r4 r8 e'8\4 |
  a'8\3 e'8\4 a'8\3 c''8\3 a'2\3 |
"""

# ----------------------------------- I) llamada y respuesta
# TRANSCRIPCION DE FELI, importada del MusicXML igual que la H.
# Llamada y respuesta dos veces, cada par en un registro distinto, y despues dos
# frases largas que recorren el mastil entero. Trae notas cromaticas (el MIb, que
# es el blue note que el alumno ya conoce del ej. 26, y el SI, que es la 2a) —
# estan a proposito y se explican en el texto del ejercicio.
EJ["r09"] = r"""
  r8^\markup{\bold "LLAMADA"} d'8\4 \tabSym \bendFull ~ d'8\4 e'8\3 a'8\2 e'8\3 g'8\3 \glissando^\markup{\bold\small "sl."}( a'8\3) |
  c''16\2 a'8.\3 a'4\3 r2 |
  r8^\markup{\bold "RESPUESTA"} g'8\3 \tabSym \bendFull ~ g'8\3 a'8\2 dis'32\4 \glissando^\markup{\bold\small "sl."}( d'32\4^\markup{\bold\small "H"})( c'16\4) a8\5 d'8\4 c'8\4 |
  a2\5 r2 |
  r8^\markup{\bold "LLAMADA"} d'8\4 \tabSym \bendFull ~ d'8\4 e'8\3 a'8\2 e'8\3 g'8\3 \glissando^\markup{\bold\small "sl."}( a'8\3) |
  c''16\2 a'8.\3 ~ a'8\3 c''8\2 ~ c''16\2 a'32\3^\markup{\bold\small "H"}( g'32\3 \glissando^\markup{\bold\small "sl."})( e'16\3) r4 r16 |
  r8^\markup{\bold "RESPUESTA"} c''8\2 \tabSym \bendFull ~ c''8\2 \tabSym \bendRel ~ c''8\2 a'16\2 e'16\3 d'32\4 \glissando^\markup{\bold\small "sl."}( dis'32\4 \glissando^\markup{\bold\small "sl."})( d'16\4^\markup{\bold\small "H"})( c'16\4) a16\5 d'16\4^\markup{\bold\small "H"}( c'16\4) |
  a2\5 r2 |
  \grace c''32.\1^\markup{\bold\small "H"}( d''8.\1) c''16\1 a'8.\2 g'16\2 \grace e'32\3 \glissando^\markup{\bold\small "sl."}( d'16\3^\markup{\bold\small "H"})( c'16\3) d'16\3 a16\4 \tuplet 3/2 { c'8\3 d'8\3 e'8\3 |
  \grace c'32\3^\markup{\bold\small "H"}( d'8.\3) c'16\3 a8.\4 g16\4 \grace e32\5 \glissando^\markup{\bold\small "sl."}( d16\5) c16\5 d16\5 a,16\6 \tuplet 3/2 { c8\5 d8\5 e8\5 |
  \grace c32\5^\markup{\bold\small "H"}( d8.\5) c16\5 a,4\5 r2 |
  b8.\3 \tabSym \bendHalf b16\3 a8.\4 g16\4 a16\4 e16\5 g16\4 a16\4 \glissando^\markup{\bold\small "sl."}( c'16\4) d'16\3 e'16\3 \glissando^\markup{\bold\small "sl."}( g'16\3) |
  b'8.\2 \tabSym \bendHalf b'16\2 a'8.\2 g'16\3 \glissando^\markup{\bold\small "sl."}( a'16\3) c''16\2 d''16\2 a'16\3 c''16\2^\markup{\bold\small "H"}( d''16\2) e''16\1 g''16\1 \tabSym \bendFull ~ |
  g''2\1 r2 |
"""

# ------------------------------------------------- J) el cierre: todo encadenado
# El anexo terminaba en el ej. G y se cortaba. Los hitos cierran con un solo (ej. 16,
# 34, 53); éste no tenía su equivalente. Son nueve compases con la MISMA célula de
# siempre pasando por todo lo que enseña el anexo, en orden.
#
# El último compás es el motivo del compás 1 devuelto en BLANCAS — o sea aumentado, no
# repetido igual. Es el leitmotiv del ej. 52 del Hito 3 y, al mismo tiempo, la tesis del
# anexo demostrada sobre sí misma: mismas notas, otra figura, otra función.
EJ["r10"] = r"""
  c''4\1^\markup{\bold "NEGRAS · la frase"} a'\1 g'\2 e'\2 |
  d'2\3 r2 |
  c''8\1^\markup{\bold "CORCHEAS · el comentario"} a'\1 g'\2 e'\2 d'\3 c'\3 a4\4 |
  \tuplet 3/2 { c''8\1^\markup{\bold "TRESILLO"} a'\1 g'\2 } \tuplet 3/2 { e'8\2 d'\3 c'\3 } a4\4 r4 |
  r8 c''8\1^\markup{\bold "A CONTRATIEMPO"} a'\1 g'\2 e'4\2 r4 |
  c''4.\1^\markup{\bold "PUNTILLO · 3+3+2"} a'4.\1 g'4\2 |
  r8 c''8\1^\markup{\bold "EL PUSH · cruza la barra"} a'\1 g'\2 e'\2 d'\3 c'\3 a8\4 ~ |
  a4\4 r4 c''4\1^\markup{\bold "vuelve el motivo…"} a'\1 |
  g'2\2^\markup{\bold "…pero en blancas: mismas notas, otra función"} e'2\2 |
"""

if __name__ == "__main__":
    fails = [k for k in sorted(EJ) if not render(k, EJ[k])]
    print("\nFallaron:", fails if fails else "ninguno")
