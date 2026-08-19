# -*- coding: utf-8 -*-
"""Genera las partituras (pentagrama + TAB) del Cuadernillo Hito 1 con LilyPond.

Salida: ./partituras/eNN.cropped.png

Tonalidad: La menor pentatónica (A C D E G).
Alturas LilyPond (sonido real, clave treble_8):
  6a: 3=g, 5=a, 8=c 10=d 12=e 15=g   -> g, a, c d e g
  5a: 3=c 5=d 7=e 10=g 12=a 15=c'
  4a: 2=e 5=g 7=a 10=c' 12=d' 14=e'
  3a: 2=a 5=c' 7=d' 9=e' 12=g' 14=a'
  2a: 3=d' 5=e' 8=g' 10=a' 13=c'' 15=d''
  1a: 3=g' 5=a' 8=c'' 10=d'' 12=e'' 15=g'' 17=a''
"""
import os
import subprocess

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "partituras")
os.makedirs(OUT, exist_ok=True)

TEMPLATE = r"""\version "2.24.0"
\header { tagline = ##f }
\paper {
  indent = 0
  ragged-right = ##f
  line-width = %(width)s\mm
  oddFooterMarkup = ##f
  oddHeaderMarkup = ##f
  evenFooterMarkup = ##f
  evenHeaderMarkup = ##f
}

%% --- notacion estandar de guitarra (el vocabulario que lee cualquier guitarrista) ---
%% Los slides (\glissando) y los ligados (slur + ^"H" / ^"P") ya salen nativos y se
%% dibujan solos en la tablatura. El bending no: LilyPond 2.24 no le pone flecha al
%% numero de traste, asi que se arma con markup.
%%
%% \tabSym marca UN markup para que aparezca tambien sobre la TABLATURA (el template
%% apaga los TextScript ahi para que los carteles didacticos no se dupliquen). Va
%% DESPUES de la nota, y afecta solo al markup que lo sigue — por eso en la misma nota
%% pueden convivir el simbolo (que va a los dos pentagramas) y un cartel en prosa (que
%% va solo al de arriba). Se hace con \tweak y no con \once \override justamente por
%% eso: el override alcanzaba a los dos markups y duplicaba el texto en la tablatura.
%%
%%   d'2\3 \tabSym \bendFull            bending de un tono  (full + flecha arriba)
%%   d'2\3 \tabSym \bendHalf            bending de medio tono
%%   d'2\3 \tabSym \bendQuarter          bending de cuarto de tono (micro-bend, color)
%%   d'2\3 \tabSym \bendRel             soltar el bending   (rel. + flecha abajo)
%%   a1\4  \tabSym \vib                 vibrato             (la linea ondulada)
%%   a1\4  \tabSym \vib ^\markup{...}   simbolo en las dos, prosa solo arriba
%%
%% La regla al escribir un ejercicio: si la notacion ya lo dice, el texto no lo repite.
%% "bend 1 tono", "vibrato", "slide", "traste 9" salen; "escucha el destino", "blue
%% note", "caes en la tonica de la caja 2" se quedan, porque eso la notacion no lo dice.
tabSym = #(define-music-function (mk) (markup?)
  #{ -\tweak stencil #ly:text-interface::print -\tweak padding #0.4 ^#mk #})
bendFull = \markup \override #'(baseline-skip . 1.3) \center-column {
  \bold \small "full" \arrow-head #Y #UP ##t }
bendHalf = \markup \override #'(baseline-skip . 1.3) \center-column {
  \bold \small "½" \arrow-head #Y #UP ##t }
bendQuarter = \markup \override #'(baseline-skip . 1.3) \center-column {
  \bold \small "¼" \arrow-head #Y #UP ##t }
bendRel = \markup \override #'(baseline-skip . 1.3) \center-column {
  \bold \small "rel." \arrow-head #Y #DOWN ##t }
vib = \markup \raise #0.4 \draw-squiggle-line #0.3 #'(4 . 0) ##t

musica = {
  \key a \minor
  \time 4/4
  \override Voice.StringNumber.stencil = ##f
%(music)s
}

\score {
  <<
    \new Staff {
      \clef "treble_8"
      \musica
    }
    \new TabStaff {
      \override TextScript.stencil = ##f
      \musica
    }
  >>
  \layout {
    \context { \Score \override SpacingSpanner.common-shortest-duration = #(ly:make-moment 1/8) }
  }
}
"""

# ---------------------------------------------------------------- ejercicios
EJ = {}

# ===== SEMANA 1 — CAJA 1 (trastes 5-8) =====
EJ["e01"] = r"""
  a,8\6 c\6 d\5 e\5 g\4 a\4 c'\3 d'\3 |
  e'8\2 g'\2 a'\1 c''\1 a'\1 g'\2 e'\2 d'\3 |
  c'8\3 a\4 g\4 e\5 d\5 c\6 a,4\6 |
"""

EJ["e02"] = r"""
  a,2\6^\markup{\bold "tónica"} r2 |
  a2\4^\markup{\bold "tónica"} r2 |
  a'2\1^\markup{\bold "tónica"} r2 |
  c''8\1 a'\1 g'\2 e'\2 d'\3 c'\3 a4\4^\markup{\bold "a casa"} |
"""

EJ["e03"] = r"""
  a,8\6 c\6 d\5 e\5 c\6 d\5 e\5 g\4 |
  d8\5 e\5 g\4 a\4 e\5 g\4 a\4 c'\3 |
  g8\4 a\4 c'\3 d'\3 a\4 c'\3 d'\3 e'\2 |
  c'8\3 d'\3 e'\2 g'\2 d'\3 e'\2 g'\2 a'\1 |
"""

EJ["e04"] = r"""
  r4 g'8\2 e'\2 d'4\3 \tabSym \bendFull ~ d'4 |
  c'8\3 a\4 g\4 e\5 a2\4 \tabSym \vib |
"""

# ===== SEMANA 2 — CAJA 2 (trastes 7-10) =====
EJ["e05"] = r"""
  c8\6 d\6 e\5 g\5 a\4 c'\4 d'\3 e'\3 |
  g'8\2 a'\2 c''\1 d''\1 c''\1 a'\2 g'\2 e'\3 |
  d'8\3 c'\4 a\4 g\5 e\5 d\6 c4\6 |
"""

EJ["e06"] = r"""
  a2\4^\markup{\bold "tónica"} r2 |
  a'2\2^\markup{\bold "tónica"} r2 |
  d''8\1 c''\1 a'\2 g'\2 e'\3 d'\3 a4\4^\markup{\bold "a casa"} |
"""

EJ["e07"] = r"""
  a,8\6 c\6 d\5 e\5 g\4 a\4 c'\3 d'\3 |
  e'8\2 g'\2 a'\1 c''\1 \glissando d''4\1^\markup{\bold "sl. → caja 2"} r4 |
  d''8\1 c''\1 a'\2 g'\2 e'\3 d'\3 c'\4 a\4 |
  g8\5 e\5 d\6 c\6 ~ c2\6 |
"""

EJ["e08"] = r"""
  r8 a'8\1 g'\2 e'\2 d'4\3 \tabSym \bendFull c'4\3 |
  d'8\3 \glissando e'\3^\markup{\bold "ya estás en caja 2"} g'4\2 a'2\2 \tabSym \vib |
"""

# ===== SEMANA 3 — CAJAS 3 y 4 =====
EJ["e09"] = r"""
  d8\6 e\6 g\5 a\5 c'\4 d'\4 e'\3 g'\3 |
  a'8\2 c''\2 d''\1 e''\1 d''\1 c''\2 a'\2 g'\3 |
  e'8\3 d'\4 c'\4 a\5 g\5 e\6 d4\6 |
"""

EJ["e10"] = r"""
  e8\6 g\6 a\5 c'\5 d'\4 e'\4 g'\3 a'\3 |
  c''8\2 d''\2 e''\1 g''\1 e''\1 d''\2 c''\2 a'\3 |
  g'8\3 e'\4 d'\4 c'\5 a\5 g\6 e4\6 |
"""

EJ["e11"] = r"""
  g'8\2 a'\2 c''\1 d''\1 \glissando e''4\1^\markup{\bold "sl. → caja 3"} r4 |
  e''8\1 c''\2 a'\2 g'\3 e'\3 d'\4 c'\4 a\5 |
  a8\5 c'\4 d'\4 g'\3 a'\2 \glissando c''4.\2^\markup{\bold "sl. → caja 4"} |
  d''8\2 e''\1 g''\1 e''\1 d''4\2 c''4\2 |
  a'1\3 \tabSym \vib |
"""

EJ["e12"] = r"""
  a,8\6^\markup{\bold "caja 1"} c\6 d\6 e\5^\markup{\bold "caja 2"} g\5 a\5 c'\4^\markup{\bold "caja 3"} d'\4 |
  e'8\4 g'\3^\markup{\bold "caja 4"} a'\3 c''\2 d''\2 e''\1 g''\1 a''\1 |
  a''8\1 g''\1 e''\1 d''\2 c''\2 a'\3 g'\3 e'\4 |
  d'8\4 c'\4 a\5 g\5 e\5 d\6 c4\6 |
  a,1\6^\markup{\bold "a casa"} |
"""

# ===== SEMANA 4 — CAJA 5 + MÁSTIL COMPLETO =====
EJ["e13"] = r"""
  g,8\6 a,\6 c\5 d\5 e\4 g\4 a\3 c'\3 |
  d'8\2 e'\2 g'\1 a'\1 g'\1 e'\2 d'\2 c'\3 |
  a8\3 g\4 e\4 d\5 c\5 a,\6 g,4\6 |
"""

EJ["e14"] = r"""
  g,8\6 a,\6 c\5 d\5 e\4 g\4 a\3 c'\3 |
  d'8\2 e'\2 g'\1 a'\1^\markup{\bold "acá empieza la caja 1"} c''4\1 r4 |
  c''8\1 a'\1 g'\2 e'\2 d'\3 c'\3 a\4 g\4 |
  e8\5 d\5 c\6 a,\6 ~ a,2\6 |
"""

EJ["e15"] = r"""
  g''8\1^\markup{\bold "caja 4"} e''\1 c''\2^\markup{\bold "caja 3"} a'\2 e'\3^\markup{\bold "caja 2"} d'\3 a\4 g\4 |
  e8\5^\markup{\bold "caja 1"} d\5 c\5^\markup{\bold "caja 5"} a,\6 g,2\6 |
"""

EJ["e16"] = r"""
  r4 g'8\2 a'\1 c''4\1 ~ c''4 |
  a'8\1 g'\2 e'2.\2 \tabSym \vib ^\markup{\bold "dejá respirar"} |
  d'8\3 e'\3 g'\2 a'\2 c''4\1 d''4\1 |
  e''2\1 \tabSym \vib ^\markup{\bold "nota larga"} r2 |
  g''8\1 e''\1 d''\2 c''\2 a'4\3 g'4\3 |
  e'8\3 d'\4 c'\4 a\5 g4\5 e4\5 |
  a,8\6 c\6 d\5 e\5 g\4 a\4 c'\3 d'\3 |
  a'1\1 \tabSym \vib ^\markup{\bold "cerrás en casa"} |
"""


def render(name, music, width=160):
    ly_path = os.path.join(OUT, name + ".ly")
    with open(ly_path, "w") as f:
        f.write(TEMPLATE % {"music": music, "width": width})
    r = subprocess.run(
        ["lilypond", "-dcrop", "-dresolution=300", "-o", name, name + ".ly"],
        cwd=OUT, capture_output=True, text=True)
    png = os.path.join(OUT, name + ".cropped.png")
    ok = os.path.exists(png)
    print(("OK  " if ok else "FAIL") + f" {name}")
    if not ok:
        print(r.stderr[-1500:])
    return ok


if __name__ == "__main__":
    fails = [k for k in sorted(EJ) if not render(k, EJ[k])]
    print("\nFallaron:", fails if fails else "ninguno")
