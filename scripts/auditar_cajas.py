# -*- coding: utf-8 -*-
"""Audita en qué cajas viven realmente los ejercicios de los cuadernillos.

Decodifica cada nota de las partituras LilyPond (pitch + número de cuerda) a su
traste, y reporta qué porcentaje sale de la ventana de la caja 1 (trastes 5-8).

Existe porque el programa promete "moverte por las 5 cajas" y es fácil que los
cuadernillos se llenen de caja 1 sin que se note leyéndolos. Correlo cada vez que
se toque una partitura.

    python scripts/auditar_cajas.py

Referencia sana (después de la auditoría de cajas):
    Hito 1  47%  ·  Hito 2  21%  ·  Hito 3  47%  ·  Bonus  73%
Si el Hito 3 baja de ~30%, algo se volvió a centrar en la caja 1.

También valida la ESCALA: el mapa de abajo sólo contiene las notas de la
pentatónica de La menor (La-Do-Re-Mi-Sol). Cualquier nota que no esté ahí no se
puede mapear a un traste, y el script la reporta y termina con código de salida 1.
O sea: si una partitura se va de la escala, esto lo caza.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Traste de cada nota de la pentatónica de Lam, por cuerda (según la cabecera
# de gen_scores_h3.py). clave: (pitch_lilypond, cuerda) -> traste
MAPA = {
    6: {"g,": 3, "a,": 5, "c": 8, "d": 10, "e": 12, "g": 15},
    5: {"c": 3, "d": 5, "e": 7, "g": 10, "a": 12, "c'": 15},
    4: {"e": 2, "g": 5, "a": 7, "c'": 10, "d'": 12, "e'": 14},
    3: {"a": 2, "c'": 5, "d'": 7, "e'": 9, "g'": 12, "a'": 14},
    2: {"d'": 3, "e'": 5, "g'": 8, "a'": 10, "c''": 13, "d''": 15},
    1: {"g'": 3, "a'": 5, "c''": 8, "d''": 10, "e''": 12, "g''": 15, "a''": 17},
}

CAJAS = {1: (5, 8), 2: (7, 10), 3: (9, 13), 4: (12, 15), 5: (2, 5)}

NOTA = re.compile(r"([a-g][,']*)\d*\.*\\(\d)")


def frets(src):
    out, fallos = [], []
    for pitch, cuerda in NOTA.findall(src):
        c = int(cuerda)
        if pitch in MAPA.get(c, {}):
            out.append(MAPA[c][pitch])
        else:
            fallos.append((pitch, c))
    return out, fallos


def cajas_de(f):
    return [c for c, (a, b) in CAJAS.items() if a <= f <= b]


FUERA_DE_ESCALA = []


def audita(EJ, titulo):
    print("=" * 78)
    print(titulo)
    print("=" * 78)
    tot_notas = tot_fuera = 0
    solo_c1 = []
    for k in sorted(EJ):
        fs, fallos = frets(EJ[k])
        if fallos:
            FUERA_DE_ESCALA.append((titulo.split(" —")[0], k, sorted(set(fallos))))
            print("  !! FUERA DE LA PENTATÓNICA en %s: %s" % (k, sorted(set(fallos))))
        if not fs:
            continue
        fuera = [f for f in fs if not (5 <= f <= 8)]   # fuera de la ventana de caja 1
        tot_notas += len(fs)
        tot_fuera += len(fuera)
        usadas = sorted({c for f in fs for c in cajas_de(f)})
        if usadas == [1] or usadas == [1, 2] and max(fs) <= 8:
            solo_c1.append(k)
        print("  %-5s notas=%3d  trastes %2d-%2d  fuera de 5-8: %3d (%4.0f%%)  cajas: %s"
              % (k, len(fs), min(fs), max(fs), len(fuera),
                 100 * len(fuera) / len(fs), usadas))
    print("-" * 78)
    print("  TOTAL: %d notas · %d fuera de la ventana 5-8 (%.1f%%)"
          % (tot_notas, tot_fuera, 100 * tot_fuera / tot_notas))
    print("  Ejercicios que NO salen de la ventana 5-8: %d/%d  -> %s"
          % (len(solo_c1), len(EJ), ", ".join(solo_c1)))
    print()


import gen_scores
import gen_scores_h2
import gen_scores_h3
import gen_scores_h3b

audita(gen_scores.EJ, "HITO 1 — EL MAPA (ej. 1-16)")
audita(gen_scores_h2.EJ, "HITO 2 — EL SABOR (ej. 17-34)")
audita(gen_scores_h3.EJ, "HITO 3 — EL VOCABULARIO (ej. 35-53)")
audita(gen_scores_h3b.EJ, "BONUS — LICKS FUERA DE LA CAJA 1 (ej. 54-59)")

print("=" * 78)
if FUERA_DE_ESCALA:
    print("VALIDACIÓN DE ESCALA: FALLÓ")
    print("Estas notas no pertenecen a la pentatónica de La menor (La-Do-Re-Mi-Sol).")
    print("Una nota fuera de escala en un ejercicio de memorización es un error real:")
    print("el alumno la aprende mal. Arreglar la partitura antes de exportar el PDF.")
    for hito, ej, notas in FUERA_DE_ESCALA:
        for pitch, cuerda in notas:
            print("  · %s · %s · '%s' en la cuerda %s" % (hito, ej, pitch, cuerda))
    sys.exit(1)
print("VALIDACIÓN DE ESCALA: OK — todas las notas caen en la pentatónica de La menor.")
print("=" * 78)
