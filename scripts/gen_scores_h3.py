# -*- coding: utf-8 -*-
"""Genera las partituras del Cuadernillo Hito 3 — EL VOCABULARIO (ejercicios 35 a 51).

Salida: ./partituras/eNN.cropped.png
Reutiliza la plantilla y el renderizador de `gen_scores.py`.

IMPORTANTE — los licks son ORIGINALES, escritos *en el estilo de* cada escuela.
No son transcripciones de solos ajenos. Es a propósito y es el punto pedagógico
del hito: lo que se roba es el MECANISMO (el motivo que se repite, la doble
cuerda, el bending que espera), no las notas de otro.

Tonalidad: La menor pentatónica. Cajas 1 y 2 sobre todo, con subidas a la 3 y 4.

Alturas LilyPond (sonido real, clave treble_8):
  6a: 3=g, 5=a, 8=c 10=d 12=e 15=g
  5a: 3=c 5=d 7=e 10=g 12=a 15=c'
  4a: 2=e 5=g 7=a 10=c' 12=d' 14=e'
  3a: 2=a 5=c' 7=d' 9=e' 12=g' 14=a'
  2a: 3=d' 5=e' 8=g' 10=a' 13=c'' 15=d''
  1a: 3=g' 5=a' 8=c'' 10=d'' 12=e'' 15=g'' 17=a''

Notación: ( ) ligado · \glissando slide · <a\2 b\1> doble cuerda ·
          ^\markup cartel · \p \mf \f dinámica · \tuplet 3/2 tresillo
"""
from gen_scores import render

EJ = {}

# ============================================ SEMANA 9 — ESCUELA BRITÁNICA
# Lo que define a la escuela: motivos cortos que se repiten, dobles cuerdas,
# ataque rítmico. La frase vale por la INSISTENCIA, no por la melodía.

# 35: el motivo que se repite (celda de 3 notas, machacada)
EJ["e35"] = r"""
  \tuplet 3/2 { c''8\1^\markup{\bold "una celda de 3 notas"}( a'\1) g'\2 }
  \tuplet 3/2 { c''8\1( a'\1) g'\2 }
  \tuplet 3/2 { c''8\1( a'\1) g'\2 }
  \tuplet 3/2 { c''8\1( a'\1) g'\2 } |
  \tuplet 3/2 { c''8\1( a'\1) g'\2 }
  \tuplet 3/2 { c''8\1( a'\1) g'\2 }
  e'4\2 a4\4^\markup{\bold "y recién ahí resolvés"} |
"""

# 36: dobles cuerdas (la marca de Angus / Chuck Berry)
EJ["e36"] = r"""
  <e'\2 a'\1>8^\markup{\bold "dos cuerdas juntas"} <e'\2 a'\1>8 <g'\2 c''\1>4 <e'\2 a'\1>4 <g'\2 c''\1>4 |
  <g'\2 c''\1>8 <e'\2 a'\1>8 d'4\3 c'8\3 a\4 g4\4 |
  a1\4^\markup{\bold "vibrato"} |
"""

# 37: el unísono (bendeás una cuerda hasta igualar la de al lado)
EJ["e37"] = r"""
  <d'\3 e'\2>2^\markup{\bold "bendeá la 3ª hasta que suene IGUAL que la 2ª"} <d'\3 e'\2>2 |
  <d'\3 e'\2>4 r4 c'8\3 a\4 g\4 e\5 |
  a1\4^\markup{\bold "vibrato"} |
"""

# 38: los tres recursos británicos encadenados
EJ["e38"] = r"""
  \tuplet 3/2 { c''8\1( a'\1) g'\2 } \tuplet 3/2 { c''8\1( a'\1) g'\2 }
  <e'\2 a'\1>4 <g'\2 c''\1>4 |
  <d'\3 e'\2>2^\markup{\bold "unísono"} d'8\3 c'\3 a4\4 |
  a1\4^\markup{\bold "vibrato"} |
"""

# ============================================ SEMANA 10 — ESCUELA AMERICANA
# Lo que la define: frases que respiran como una voz, legato, bendings largos,
# espacio. La frase vale por la MELODÍA, no por la insistencia.

# 39: la frase vocal (escuela Gary Moore) — espera, estira, resuelve
EJ["e39"] = r"""
  r4 a'8\1 c''8\1 ~ c''2 |
  d'4\3^\markup{\bold "bend 1 tono + vibrato"} ~ d'2. |
  c'8\3 a\4 g\4 e\5 a2\4^\markup{\bold "vibrato largo"} |
"""

# 40: la línea fluida (escuela Slash) — casi todo ligado, casi nada punteado
EJ["e40"] = r"""
  r8 d''8\1 \glissando c''8\1^\markup{\bold "slide"}( a'\1) g'\2( e'\2) d'\3( c'\3) |
  a8\4( g\4) e\5( d\5) c8\6 a,4.\6^\markup{\bold "vibrato"} |
"""

# 41: dobles cuerdas con ligado (el remate estilo Hendrix)
EJ["e41"] = r"""
  <c'\3 e'\2>8^\markup{\bold "el hammer va en la cuerda de abajo"}( <d'\3 e'\2>8) <c'\3 e'\2>4
  <c'\3 e'\2>8( <d'\3 e'\2>8) <c'\3 e'\2>4 |
  g'8\2 e'\2 d'\3 c'\3 a2\4^\markup{\bold "vibrato"} |
"""

# 42: los tres recursos americanos encadenados
EJ["e42"] = r"""
  r8 d''8\1 \glissando c''8\1( a'\1) g'\2( e'\2) d'\3( c'\3) |
  <c'\3 e'\2>8( <d'\3 e'\2>8) <c'\3 e'\2>4 a4\4 r4 |
  d'2\3^\markup{\bold "bend 1 tono"} d'2\3^\markup{\bold "vibrato"} |
  c'8\3 a\4 g\4 e\5 a2\4^\markup{\bold "vibrato"} |
"""

# ============================================ SEMANA 11 — HACERLO TUYO
# Las 3 variaciones que convierten un lick robado en un lick propio,
# precedidas por el color de cada grado: es lo que explica POR QUE un remate funciona.

# 43: el color de cada grado — la misma escala, seis sensaciones distintas
EJ["e43"] = r"""
  a1\4^\markup{\bold "1ª · la tónica"} |
  c'1\3^\markup{\bold "3ª menor"} |
  d'1\3^\markup{\bold "4ª"} |
  e'1\2^\markup{\bold "5ª"} |
  g'1\2^\markup{\bold "7ª menor"} |
  a'1\1^\markup{\bold "8ª · tónica arriba"} |
"""

# Las 3 variaciones que convierten un lick robado en un lick propio.

# 44: mismas notas, tres ritmos distintos
EJ["e44"] = r"""
  a'8\1^\markup{\bold "1 · todo parejo"} g'\2 e'\2 d'\3 c'\3 a\4 r4 |
  a'4\1^\markup{\bold "2 · arranca lento y acelera"} g'8\2 e'\2 d'16\3 c'\3 a8\4 ~ a4\4 |
  r8 a'8\1^\markup{\bold "3 · a contratiempo"} g'\2 e'\2 ~ e'8 d'\3 c'\3 a\4 |
"""

# 45: mismo arranque, tres remates distintos
EJ["e45"] = r"""
  r4 a'8\1 g'\2 e'4\2 d'4\3^\markup{\bold "remate 1 · queda colgado (pregunta)"} |
  r4 a'8\1 g'\2 e'4\2 a4\4^\markup{\bold "remate 2 · cae en la tónica (respuesta)"} |
  r4 a'8\1 g'\2 e'4\2 c''4\1^\markup{\bold "remate 3 · sube y queda vibrando"} |
"""

# 46: el mismo lick, mudado de caja
EJ["e46"] = r"""
  r8 a'8\1^\markup{\bold "en la caja 1"} g'\2 e'\2 d'\3 c'\3 a4\4 |
  r8 d''8\1^\markup{\bold "el mismo, en la caja 2"} c''\1 a'\2 g'\2 e'\3 d'4\3 |
  r8 e''8\1^\markup{\bold "y en la caja 3"} d''\1 c''\2 a'\2 g'\3 e'4\3 |
"""

# 47: la arquitectura de un solo — las 4 frases
EJ["e47"] = r"""
  r4 a8\4^\markup{\bold "1 · PRESENTA — grave y simple"} c'\3 d'4\3 c'4\3 |
  a1\4^\markup{\bold "vibrato"} |
  r4 e'8\2^\markup{\bold "2 · DESARROLLA — la misma idea, más arriba"} g'\2 a'4\1 g'4\2 |
  e'1\2^\markup{\bold "vibrato"} |
  c''8\1\f^\markup{\bold "3 · CLÍMAX — lo más agudo y lo más fuerte"} d''\1 e''\1 d''\1 c''4\1 a'4\2 |
  d'2\3^\markup{\bold "bend 1 tono + vibrato"} d'2\3 |
  c'8\3\p^\markup{\bold "4 · CIERRA — bajás y resolvés"} a\4 g\4 e\5 d\5 c\6 a,4\6 |
  a,1\6^\markup{\bold "vibrato"} |
"""

# ============================================ SEMANA 12 — TU SOLO
# 48: el esqueleto para completar — están las llegadas, faltan tus frases
EJ["e48"] = r"""
  r1^\markup{\bold "TU frase 1 — grave, 3 o 4 notas, tranquila"} |
  a1\4^\markup{\bold "caé acá (tónica) + vibrato"} |
  r1^\markup{\bold "TU frase 2 — la misma idea, una caja más arriba"} |
  e'1\2^\markup{\bold "caé acá + vibrato"} |
  r1^\markup{\bold "TU frase 3 — el clímax: agudo, fuerte, más notas"} |
  d'2\3^\markup{\bold "el bending va acá"} d'2\3^\markup{\bold "vibrato"} |
  r1^\markup{\bold "TU frase 4 — bajás, aflojás"} |
  a,1\6^\markup{\bold "cerrás en la tónica"} |
"""

# 49: tres finales posibles (elegí uno para tu solo)
EJ["e49"] = r"""
  c'8\3 a\4 g\4 e\5 a2\4^\markup{\bold "1 · a la tónica, suave — el más seguro"} |
  d'4\3^\markup{\bold "2 · un bending largo que se va apagando"} ~ d'2. |
  <e'\2 a'\1>2^\markup{\bold "3 · doble cuerda que queda sonando"} <e'\2 a'\1>2 |
"""

# 50: el motivo que vuelve (el truco que hace que un solo suene "armado")
EJ["e50"] = r"""
  \tuplet 3/2 { c''8\1( a'\1) g'\2 } e'4\2^\markup{\bold "el motivo, al principio"} r2 |
  r1 |
  \tuplet 3/2 { c''8\1( a'\1) g'\2 } e'4\2^\markup{\bold "…y vuelve al final: el oído lo reconoce"} a4\4 r4 |
"""

# 51: EL SOLO FINAL — 12 compases, el trofeo del programa
EJ["e51"] = r"""
  r4 a8\4\p^\markup{\bold "PRESENTA"} c'\3 d'4\3 c'4\3 |
  a2\4^\markup{\bold "vibrato"} r2 |
  r4 e'8\2^\markup{\bold "DESARROLLA"} g'\2 a'4\1 g'4\2 |
  e'2\2^\markup{\bold "vibrato"} r2 |
  \tuplet 3/2 { c''8\1\mf^\markup{\bold "el motivo británico"}( a'\1) g'\2 }
  \tuplet 3/2 { c''8\1( a'\1) g'\2 }
  \tuplet 3/2 { c''8\1( a'\1) g'\2 } e'4\2 |
  <e'\2 a'\1>8 <e'\2 a'\1>8 <g'\2 c''\1>4 <e'\2 a'\1>4 <g'\2 c''\1>4 |
  r8 c''8\1\f \glissando d''4\1^\markup{\bold "CLÍMAX"} e''4\1 g''4\1 |
  g''2\1^\markup{\bold "vibrato ancho"} e''8\1 d''\2 c''\2 a'\2 |
  d'2\3^\markup{\bold "bend 1 tono"} d'2\3^\markup{\bold "vibrato"} |
  r1 |
  \tuplet 3/2 { c''8\1\p^\markup{\bold "vuelve el motivo · CIERRA"}( a'\1) g'\2 } e'4\2 c'8\3 a\4 g4\4 |
  a,1\6^\markup{\bold "vibrato · se apaga"} |
"""


if __name__ == "__main__":
    fails = [k for k in sorted(EJ) if not render(k, EJ[k])]
    print("\nFallaron:", fails if fails else "ninguno")
