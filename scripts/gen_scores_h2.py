# -*- coding: utf-8 -*-
"""Genera las partituras del Cuadernillo Hito 2 — EL SABOR (ejercicios 17 a 34).

Salida: ./partituras/eNN.cropped.png
Reutiliza la plantilla y el renderizador de `gen_scores.py`.

Tonalidad: La menor pentatónica. Todo se toca en las cajas 1 y 2, que el alumno
ya domina del Hito 1 — acá lo nuevo es CÓMO suena, no DÓNDE está.

Alturas LilyPond (sonido real, clave treble_8):
  6a: 3=g, 5=a, 8=c 10=d 12=e 15=g
  5a: 3=c 5=d 7=e 10=g 12=a 15=c'
  4a: 2=e 5=g 7=a 10=c' 12=d' 14=e'
  3a: 2=a 5=c' 7=d' 9=e' 12=g' 14=a'
  2a: 3=d' 5=e' 8=g' 10=a' 13=c'' 15=d''
  1a: 3=g' 5=a' 8=c'' 10=d'' 12=e'' 15=g'' 17=a''

Notación usada acá:
  ( )          ligado (hammer-on subiendo / pull-off bajando)
  \glissando   slide
  \tabSym       manda ese simbolo tambien a la TABLATURA (ver gen_scores.py)
  ^\bendFull    bending de un tono · ^\bendRel soltarlo · ^\vib vibrato
  \p \mf \f    dinámica
"""
from gen_scores import render   # misma plantilla, mismo directorio de salida

EJ = {}

# ===================================================== SEMANA 5 — LIGADOS Y SLIDES
# 17: hammer-on aislado, par por par, subiendo por la caja 1.
# Todos los ligados son en la MISMA cuerda y subiendo: por eso son H y no P.
EJ["e17"] = r"""
  a,8\6^\markup{\bold "hammer-on"}( c\6) a,8\6( c\6) d8\5^\markup{\bold\small "H"}( e\5) d8\5( e\5) |
  g8\4^\markup{\bold\small "H"}( a\4) g8\4( a\4) c'8\3^\markup{\bold\small "H"}( d'\3) c'8\3( d'\3) |
  e'8\2^\markup{\bold\small "H"}( g'\2) e'8\2( g'\2) a'8\1^\markup{\bold\small "H"}( c''\1) a'8\1( c''\1) |
"""

# 18: pull-off aislado, bajando. Misma cuerda, bajando -> P.
EJ["e18"] = r"""
  c''8\1^\markup{\bold "pull-off"}( a'\1) c''8\1( a'\1) g'8\2^\markup{\bold\small "P"}( e'\2) g'8\2( e'\2) |
  d'8\3^\markup{\bold\small "P"}( c'\3) d'8\3( c'\3) a8\4^\markup{\bold\small "P"}( g\4) a8\4( g\4) |
  e8\5^\markup{\bold\small "P"}( d\5) e8\5( d\5) c8\6^\markup{\bold\small "P"}( a,\6) c8\6( a,\6) |
"""

# 19: el tresillo de rock — una sola pua cada tres notas. Cada tresillo es H y despues P.
EJ["e19"] = r"""
  \tuplet 3/2 { a,8\6^\markup{\bold "una púa cada 3 notas · H P"}( c\6 a,\6) }
  \tuplet 3/2 { d8\5( e\5 d\5) }
  \tuplet 3/2 { g8\4( a\4 g\4) }
  \tuplet 3/2 { c'8\3( d'\3 c'\3) } |
  \tuplet 3/2 { e'8\2^\markup{\bold\small "H P"}( g'\2 e'\2) }
  \tuplet 3/2 { a'8\1( c''\1 a'\1) }
  \tuplet 3/2 { a'8\1( c''\1 a'\1) }
  \tuplet 3/2 { e'8\2( g'\2 e'\2) } |
  \tuplet 3/2 { c'8\3^\markup{\bold\small "H P"}( d'\3 c'\3) }
  \tuplet 3/2 { g8\4( a\4 g\4) }
  \tuplet 3/2 { d8\5( e\5 d\5) }
  \tuplet 3/2 { a,8\6( c\6 a,\6) } |
"""

# 20: ligados + slide juntos, ya como frase
EJ["e20"] = r"""
  r4 e'8\2^\markup{\bold\small "H"}( g'\2) a'4\1 \glissando c''4\1^\markup{\bold\small "sl."} |
  c''8\1^\markup{\bold\small "P"}( a'\1) g'\2( e'\2) d'\3( c'\3) a4\4 \tabSym \vib |
"""

# ===================================================== SEMANA 6 — BENDING
# 21: el destino primero, despues el bending (afinar el oido).
# El texto ya no dice "traste 9" ni "bendea el 7": eso lo dice la tablatura.
EJ["e21"] = r"""
  e'2\3^\markup{\bold "1 · escuchá el destino"} r2 |
  d'1\3 \tabSym \bendFull |
  a'2\2^\markup{\bold "2 · escuchá el destino"} r2 |
  g'1\2 \tabSym \bendFull |
"""

# 22: bending con destino, en tres cuerdas, ya en contexto
EJ["e22"] = r"""
  d'4\3 \tabSym \bendFull ~ d'4 c'8\3 a\4 g4\4 |
  g'4\2 \tabSym \bendFull ~ g'4 e'8\2 d'\3 c'4\3 |
  c''4\1 \tabSym \bendFull ~ c''4 a'8\1 g'\2 e'4\2 |
"""

# 23: bending y vuelta (release) — controlar la bajada
EJ["e23"] = r"""
  d'2\3 \tabSym \bendFull d'2\3 \tabSym \bendRel |
  c'8\3 a\4 g\4 e\5 a2\4 \tabSym \vib |
"""

# 24: lick de bending (escuela Gary Moore): esperar, estirar, resolver
EJ["e24"] = r"""
  r8 e'8\2 g'\2 a'\1 c''4\1 ~ c''4 |
  d'4\3 \tabSym \bendFull ~ d'4 c'8\3 a\4 g4\4 |
  a1\4 \tabSym \vib^\markup{\bold "ancho · dejala morir"} |
"""

# 25: bend a la tonica de la caja 2 (Albert King / SRV) - primer contacto con caja 2
EJ["e25"] = r"""
  r8 d''8\1 c''\1 a'\2 g'4\2 \tabSym \bendFull^\markup{\bold "caés en la tónica de caja 2"} ~ g'4 |
  g'2\2 \tabSym \vib^\markup{\bold "ancho, sin soltar el bending"} e'8\3 d'\3 a4\4 |
"""

# 26: el blue note, de paso (todavia en caja 2)
EJ["e26"] = r"""
  r8 a'8\2 g'\2 e'\3 d'8\3 ees'\3^\markup{\bold "blue note · solo de paso"} e'\3 g'\2 |
  e'8\3 d'\3 c'\4 g\5 a2\4 \tabSym \vib |
"""

# ===================================================== SEMANA 7 — VIBRATO
# 27: vibrato medido con metronomo (3 velocidades sobre la misma nota)
# ahora en la caja 2 (tonica: 2a cuerda, traste 10) — no en la 1.
# Aca el texto SI se queda: la cantidad de ondas es el contenido, y el simbolo no la dice.
EJ["e27"] = r"""
  a'1\2 \tabSym \vib^\markup{\bold "lento: 2 ondas por tiempo · caja 2"} |
  a'1\2 \tabSym \vib^\markup{\bold "medio: 3 ondas por tiempo"} |
  a'1\2 \tabSym \vib^\markup{\bold "rápido: 4 ondas por tiempo"} |
"""

# 28: la misma frase resuelta con vibrato en tres registros
EJ["e28"] = r"""
  c8\6 d\5 e\5 g\4 a2\4 \tabSym \vib^\markup{\bold "registro grave"} |
  c'8\3 d'\3 e'\2 g'\2 a'2\1 \tabSym \vib^\markup{\bold "medio"} |
  c''8\1 d''\1 e''\1 g''\1 a''2\1 \tabSym \vib^\markup{\bold "agudo, más ancho"} |
  g'8\3 c''\2 d''\2 e''\1 a'2\3 \tabSym \vib^\markup{\bold "caja 4"} |
"""

# 29: bending + vibrato (la combinacion que suena "pro")
EJ["e29"] = r"""
  d'2\3 \tabSym \bendFull d'2\3 \tabSym \vib |
  c'8\3 a\4 g\4 e\5 a2\4 \tabSym \vib |
"""

# 30: frase entera donde el vibrato es el remate. Ahora en la caja 2.
# OJO: g'\2 -> e'\3 cruza de cuerda (traste 8 de la 2a al 9 de la 3a), asi que NO es
# un pull-off aunque baje de altura. Se deja como ligadura de fraseo, sin letra.
EJ["e30"] = r"""
  r4 g'8\2^\markup{\bold "caja 2"} c''\1 d''4\1 ~ d''4 |
  c''8\1 a'\2 g'\2( e'\3) a'2\2 \tabSym \vib^\markup{\bold "la tónica de la caja 2, que se note"} |
"""

# ===================================================== SEMANA 8 — ESPACIO Y DINAMICA
# 31: la regla de las 3 notas — tocas poco, te callas mucho
EJ["e31"] = r"""
  r4 a'8\1 g'\2 e'2\2^\markup{\bold "3 notas"} |
  r1^\markup{\bold "y ahora te callás"} |
  r4 c''8\1 a'\1 g'2\2 |
  r1 |
  r4 d'8\3 c'\3 a2\4 \tabSym \vib |
  r1 |
  r4 g,8\6 e\4 a,2\6^\markup{\bold "3 notas · caja 5, bien grave"} |
  r1^\markup{\bold "y te callás igual"} |
"""

# 32: pregunta y respuesta (mismo ritmo, distinto final), en la caja 2
EJ["e32"] = r"""
  r4 c''8\1^\markup{\bold "caja 2"} d''\1 a'4\2 g'4\2^\markup{\bold "pregunta: queda abierta"} |
  r1 |
  r4 d''8\1 c''\1 g'4\2 a'4\2^\markup{\bold "respuesta: cierra en la tónica"} |
  r1 |
"""

# 33: la misma frase en tres volumenes. Ahora en la caja 2.
EJ["e33"] = r"""
  r4 c''8\1\p^\markup{\bold "caja 2"} d''\1 a'4\2 g'4\2 |
  r4 c''8\1\mf d''\1 a'4\2 g'4\2 |
  r4 c''8\1\f d''\1 a'4\2 g'4\2 \tabSym \vib |
"""

# 34: SOLO DE EVALUACION del Hito 2 — los 4 bloques + espacio + dinamica.
# Las dos ligaduras del anteultimo compas cruzan de cuerda: son de fraseo, no H ni P.
EJ["e34"] = r"""
  r2 r8 e'8\2\p g'\2 a'\1 |
  c''1\1 \tabSym \vib |
  a'8\1^\markup{\bold\small "H"}( c''\1) a'\1 g'\2^\markup{\bold\small "P"}( e'\2) g'\2 a'4\1\mf |
  d'2\3 \tabSym \bendFull d'2\3 \tabSym \vib |
  r1 |
  r8 c''8\1 \glissando d''4\1^\markup{\bold "sl. · caja 2"} e''4\1^\markup{\bold "caja 3"} e''4\1 |
  g''8\1\f^\markup{\bold "caja 4"} e''\1 d''\2 c''\2 a'4\3 g'4\3 |
  e'8\3( d'\4) c'\4( a\5) g4\5 e4\5 |
  a,8\6\p c\6 d\5 e\5 g\4 a\4 c'4\3 |
  a1\4 \tabSym \vib^\markup{\bold "dejala morir"} |
"""

if __name__ == "__main__":
    fails = [k for k in sorted(EJ) if not render(k, EJ[k])]
    print("\nFallaron:", fails if fails else "ninguno")
