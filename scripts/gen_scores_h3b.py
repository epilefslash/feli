# -*- coding: utf-8 -*-
"""Partituras del Cuadernillo HITO 3 · PARTE 2 — 8 licks POST-PROGRAMA, fuera de las cajas 1 y 2 (ej. 52 a 59).

Los licks de caja 2 (bend a la tónica + blue note) se movieron al Hito 2, semana 6,
para que el alumno pise la caja 2 DURANTE el programa y no recién al final.

Salida: ./partituras/eNN.cropped.png

IMPORTANTE — igual que en la parte 1: los licks son ORIGINALES, escritos con el
MECANISMO característico de cada guitarrista y en la caja donde ese guitarrista
realmente vive. No son transcripciones. Cada lick lleva en el cuadernillo una
referencia de qué escuchar para reconocer el recurso en su contexto original.

Regla del cuadernillo: NINGUNO usa la caja 1 (trastes 5 a 8) como territorio.

Notas fuera de la pentatónica que se usan (adornos permitidos):
  · Mib (b5, blue note)  -> 3a cuerda traste 8   = ees'
  · Fa# (6a mayor)       -> 3a cuerda traste 11  = fis'   (la nota del "BB box")

Alturas LilyPond por caja (La menor):
  CAJA 2 (7-10):  6a 8=c 10=d · 5a 7=e 10=g · 4a 7=a 10=c' · 3a 7=d' 9=e' · 2a 8=g' 10=a' · 1a 8=c'' 10=d''
  CAJA 3 (9-13):  6a 10=d 12=e · 5a 10=g 12=a · 4a 10=c' 12=d' · 3a 9=e' 12=g' · 2a 10=a' 13=c'' · 1a 10=d'' 12=e''
  CAJA 4 (12-15): 6a 12=e 15=g · 5a 12=a 15=c' · 4a 12=d' 14=e' · 3a 12=g' 14=a' · 2a 13=c'' 15=d'' · 1a 12=e'' 15=g''
  CAJA 5 (2-5):   6a 3=g, 5=a, · 5a 3=c 5=d · 4a 2=e 5=g · 3a 2=a 5=c' · 2a 3=d' 5=e' · 1a 3=g' 5=a'
"""
from gen_scores import render

EJ = {}

# ==================================================== CAJA 3 (trastes 9 a 13)
# 52: Clapton / Cream — el motivo agudo repetido hasta que se vuelve un gancho
EJ["e52"] = r"""
  \tuplet 3/2 { e''8\1^\markup{\bold "la celda, bien arriba"}( d''\1) c''\2 }
  \tuplet 3/2 { e''8\1( d''\1) c''\2 }
  \tuplet 3/2 { e''8\1( d''\1) c''\2 }
  \tuplet 3/2 { e''8\1( d''\1) c''\2 } |
  \tuplet 3/2 { e''8\1( d''\1) c''\2 }
  \tuplet 3/2 { e''8\1( d''\1) c''\2 }
  a'2\2^\markup{\bold "vibrato · la tónica está acá"} |
"""

# 53: B.B. King — la 6a mayor en lugar de la 7a menor (la nota que endulza)
EJ["e53"] = r"""
  r8 e''8\1 d''\1 a'\2 fis'8\3^\markup{\bold "6ª MAYOR · la nota dulce"} a'\2 fis'\3 a'\2 |
  a'2\2^\markup{\bold "vibrato rápido y angosto"} e'8\3 d'\4 a4\5 |
"""

# ==================================================== CAJA 4 (trastes 12 a 15)
# 54: Gilmour — una sola nota, estirada y sostenida una eternidad
EJ["e54"] = r"""
  r2 a'8\3 c''8\2 ~ c''4 |
  c''1\2^\markup{\bold "bend 1 tono · y lo sostenés"} |
  c''2\2^\markup{\bold "vibrato lento y ancho"} a'8\3 g'\3 e'4\4 |
  a1\5^\markup{\bold "a casa"} |
"""

# 55: Hendrix — dobles cuerdas en el registro agudo
EJ["e55"] = r"""
  <c''\2 e''\1>8^\markup{\bold "dos cuerdas juntas, bien arriba"} <c''\2 e''\1>8
  <d''\2 g''\1>4 <c''\2 e''\1>4 <d''\2 g''\1>4 |
  <d''\2 g''\1>8 <c''\2 e''\1>8 a'4\3 g'8\3 e'\4 d'4\4 |
  a1\5^\markup{\bold "vibrato"} |
"""

# ==================================================== CAJA 5 (trastes 2 a 5)
# 56: Angus / Chuck Berry — la zona grave suena a riff, no a solo
EJ["e56"] = r"""
  g,8\6^\markup{\bold "acá abajo pesa más"}( a,\6) c\5( d\5) e\4( g\4) a8\3 c'\3 |
  c'8\3 a\3 g\4 e\4 d\5 c\5 a,4\6^\markup{\bold "a casa"} |
"""

# 57: la caja 5 también canta — frase melódica con espacio en la zona grave
EJ["e57"] = r"""
  r4 c'8\3 d'8\2 ~ d'2 |
  e'4\2^\markup{\bold "vibrato"} ~ e'4 c'8\3 a\3 g4\4 |
  a,1\6^\markup{\bold "la tónica más grave que tenés"} |
"""

# ==================================================== TODO EL MÁSTIL
# 58: la subida rodante — caja 5 a caja 3 usando la 1a cuerda como escalera
EJ["e58"] = r"""
  g,8\6^\markup{\bold "caja 5"} a,\6 c\5 d\5 e\4 g\4 a\3 c'\3 |
  d'8\2 e'\2 g'\1 a'\1 \glissando c''4\1^\markup{\bold "caja 1"} r4 |
  c''8\1 \glissando d''4\1^\markup{\bold "caja 2"} \glissando e''4\1^\markup{\bold "caja 3"} r4. |
  e''1\1^\markup{\bold "vibrato · llegaste al traste 12"} |
"""

# 59: Slash — la bajada diagonal, casi todo ligado
EJ["e59"] = r"""
  a''8\1 \glissando g''8\1^\markup{\bold "caja 4"}( e''\1) c''\2( a'\2) e'\3( d'\3) a8\4 |
  g8\4^\markup{\bold "caja 1"} e\5 d\5 c\5^\markup{\bold "caja 5"} a,4\6 g,4\6 |
  a,1\6^\markup{\bold "vibrato · cerrás en la tónica grave"} |
"""


if __name__ == "__main__":
    fails = [k for k in sorted(EJ) if not render(k, EJ[k])]
    print("\nFallaron:", fails if fails else "ninguno")
