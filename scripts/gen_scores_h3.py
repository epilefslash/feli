# -*- coding: utf-8 -*-
"""Genera las partituras del Cuadernillo Hito 3 — EL VOCABULARIO (ejercicios 35 a 53).

Salida: ./partituras/eNN.cropped.png
Reutiliza la plantilla y el renderizador de `gen_scores.py`.

IMPORTANTE — los licks son ORIGINALES, escritos *en el estilo de* cada escuela.
No son transcripciones de solos ajenos. Es a propósito y es el punto pedagógico
del hito: lo que se roba es el MECANISMO (el motivo que se repite, la doble
cuerda, el bending que espera), no las notas de otro.

Tonalidad: La menor pentatónica.
Territorio: los licks de escuela (35-42) viven en la caja 1 a propósito — se aísla
la variable: se aprende el MECANISMO, no una posición nueva. Desde el ej. 46 en
adelante el hito se abre: 46 muda un lick por tres cajas, 47 y 48 son licks reales
en las cajas 3 y 5, y 49/50/53 (arquitectura, esqueleto y solo final) tienen sus
llegadas repartidas por el mástil para que el alumno NO pueda quedarse en la caja 1.

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

# 47: el mismo mecanismo del ej. 35, pero en la CAJA 3 (repatriado del bonus)
# Escuela británica: la celda repetida. Idéntico recurso, tres cajas más arriba.
EJ["e47"] = r"""
  \tuplet 3/2 { e''8\1^\markup{\bold "la MISMA celda del ej. 35, tres cajas más arriba"}( d''\1) c''\2 }
  \tuplet 3/2 { e''8\1( d''\1) c''\2 }
  \tuplet 3/2 { e''8\1( d''\1) c''\2 }
  \tuplet 3/2 { e''8\1( d''\1) c''\2 } |
  \tuplet 3/2 { e''8\1( d''\1) c''\2 }
  \tuplet 3/2 { e''8\1( d''\1) c''\2 }
  a'2\2^\markup{\bold "vibrato · la tónica de la caja 3"} |
"""

# 48: la CAJA 5, la zona grave (repatriado del bonus) — Angus / Chuck Berry
EJ["e48"] = r"""
  g,8\6^\markup{\bold "la zona grave: acá abajo pesa más"}( a,\6) c\5( d\5) e\4( g\4) a8\3 c'\3 |
  c'8\3 a\3 g\4 e\4 d\5 c\5 a,4\6^\markup{\bold "a casa: la tónica más grave"} |
"""

# 49: la arquitectura de un solo — las 4 frases, cada una en su caja
EJ["e49"] = r"""
  r4 a8\4^\markup{\bold "1 · PRESENTA — grave y simple · CAJA 1"} c'\3 d'4\3 c'4\3 |
  a1\4^\markup{\bold "vibrato"} |
  r4 e'8\3^\markup{\bold "2 · DESARROLLA — la misma idea, MUDADA A LA CAJA 2"} g'\2 a'4\2 c''4\1 |
  a'1\2^\markup{\bold "vibrato · la tónica de la caja 2"} |
  c''8\1\f^\markup{\bold "3 · CLÍMAX — subís a la CAJA 3, agudo y fuerte"} d''\1 e''\1 d''\1 c''4\1 a'4\2 |
  g'2\3^\markup{\bold "bend 1 tono + vibrato · caja 3"} g'2\3 |
  c'8\3\p^\markup{\bold "4 · CIERRA — bajás por el mástil y resolvés"} a\4 g\4 e\5 d\5 c\6 a,4\6 |
  a,1\6^\markup{\bold "vibrato · caja 5"} |
"""

# ============================================ SEMANA 12 — TU SOLO
# 50: el esqueleto para completar. Las 4 llegadas están en 4 cajas distintas:
# el alumno no puede conectarlas sin recorrer el mástil. Ese es el punto.
EJ["e50"] = r"""
  r1^\markup{\bold "TU frase 1 — grave, 3 o 4 notas, tranquila · CAJA 1"} |
  a1\4^\markup{\bold "caé acá: la tónica de la caja 1 + vibrato"} |
  r1^\markup{\bold "TU frase 2 — la misma idea, MUDADA A LA CAJA 2"} |
  a'1\2^\markup{\bold "caé acá: la tónica de la caja 2 + vibrato"} |
  r1^\markup{\bold "TU frase 3 — el clímax, arriba de todo · CAJA 3"} |
  g'2\3^\markup{\bold "el bending va acá: 1 tono, llega a la tónica"} g'2\3^\markup{\bold "vibrato"} |
  r1^\markup{\bold "TU frase 4 — bajás por todo el mástil hasta la CAJA 5"} |
  a,1\6^\markup{\bold "cerrás en la tónica más grave"} |
"""

# 51: tres finales posibles — cada uno en una caja distinta, a propósito:
# un cierre no depende de la posición, depende del gesto.
EJ["e51"] = r"""
  c'8\3 a\4 g\4 e\5 a2\4^\markup{\bold "1 · a la tónica, suave · CAJA 1 — el más seguro"} |
  g'4\3^\markup{\bold "2 · bending largo que se apaga · CAJA 3"} ~ g'2. |
  <c''\2 e''\1>2^\markup{\bold "3 · doble cuerda que queda sonando · CAJA 4"} <c''\2 e''\1>2 |
"""

# 52: el motivo que vuelve (el truco que hace que un solo suene "armado")
EJ["e52"] = r"""
  \tuplet 3/2 { c''8\1( a'\1) g'\2 } e'4\2^\markup{\bold "el motivo, al principio"} r2 |
  r1 |
  \tuplet 3/2 { c''8\1( a'\1) g'\2 } e'4\2^\markup{\bold "…y vuelve al final: el oído lo reconoce"} a4\4 r4 |
"""

# 53: EL SOLO FINAL — 12 compases, el trofeo del programa.
# Recorre cajas 1 -> 2 -> 3 -> 4 -> 3 -> 1 -> 5. Es la prueba de la promesa.
EJ["e53"] = r"""
  r4 a8\4\p^\markup{\bold "PRESENTA · caja 1"} c'\3 d'4\3 c'4\3 |
  a2\4^\markup{\bold "vibrato"} r2 |
  r4 e'8\3^\markup{\bold "DESARROLLA · mudado a la CAJA 2"} g'\2 a'4\2 c''4\1 |
  a'2\2^\markup{\bold "vibrato · tónica de la caja 2"} r2 |
  \tuplet 3/2 { c''8\1\mf^\markup{\bold "vuelve a caja 1: el motivo británico"}( a'\1) g'\2 }
  \tuplet 3/2 { c''8\1( a'\1) g'\2 }
  \tuplet 3/2 { c''8\1( a'\1) g'\2 } e'4\2 |
  <e'\2 a'\1>8 <e'\2 a'\1>8 <g'\2 c''\1>4 <e'\2 a'\1>4 <g'\2 c''\1>4 |
  r8 c''8\1\f \glissando d''4\1^\markup{\bold "CLÍMAX · subís por las cajas 2, 3 y 4"} e''4\1 g''4\1 |
  g''2\1^\markup{\bold "vibrato ancho · caja 4"} e''8\1 d''\2 c''\2 a'\2 |
  g'2\3^\markup{\bold "bend 1 tono · caja 3"} g'2\3^\markup{\bold "vibrato"} |
  r1 |
  \tuplet 3/2 { c''8\1\p^\markup{\bold "vuelve el motivo · CIERRA"}( a'\1) g'\2 } e'4\2 c'8\3 a\4 g4\4 |
  a,1\6^\markup{\bold "vibrato · se apaga en la caja 5"} |
"""


if __name__ == "__main__":
    fails = [k for k in sorted(EJ) if not render(k, EJ[k])]
    print("\nFallaron:", fails if fails else "ninguno")
