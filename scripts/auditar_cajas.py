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
# Traste 0 = cuerda al aire. Dato que vale la pena saber: de las 6 cuerdas al aire,
# CINCO son notas de la pentatonica de La menor (MI, LA, RE, SOL, MI). La unica que
# no pertenece es la 2a (SI). O sea que la guitarra en afinacion estandar ya es casi
# una pentatonica de Lam sonando. Por eso estan en el mapa: si un ejercicio usa una
# cuerda al aire, es escala valida y no tiene que fallar la validacion.
# OJO: el traste 0 no cae dentro de ninguna de las 5 cajas (la mas baja, la 5, arranca
# en el 2). cajas_de(0) devuelve [] a proposito: la posicion abierta esta afuera del
# sistema de cajas, y eso es correcto, no un bug.
MAPA = {
    6: {"e,": 0, "g,": 3, "a,": 5, "c": 8, "d": 10, "e": 12, "g": 15},
    5: {"a,": 0, "c": 3, "d": 5, "e": 7, "g": 10, "a": 12, "c'": 15, "d'": 17},
    4: {"d": 0, "e": 2, "g": 5, "a": 7, "c'": 10, "d'": 12, "e'": 14, "g'": 17},
    3: {"g": 0, "a": 2, "c'": 5, "d'": 7, "e'": 9, "g'": 12, "a'": 14, "c''": 17},
    2: {"d'": 3, "e'": 5, "g'": 8, "a'": 10, "c''": 13, "d''": 15},
    1: {"e'": 0, "g'": 3, "a'": 5, "c''": 8, "d''": 10, "e''": 12, "g''": 15, "a''": 17},
}

# CROMATICAS PERMITIDAS — notas que NO son de la pentatonica de La menor y que
# entran igual, a proposito y documentadas. Decision de Feli (5/8/2026) al importar
# sus transcripciones. Van aparte del MAPA para que se vean: cualquier nota alterada
# que no este aca sigue haciendo fallar la validacion.
#
#   MIb / RE# -> el BLUE NOTE (b5). El alumno ya lo conoce del ej. 26 del Hito 2.
#   SI        -> la 2a (o 9a). Color melodico, no de blues. Aparece en el ej. I,
#                y en el ej. 37-bis (cita de Angus Young, Lick 1) en la 1a cuerda.
#   FA#       -> la 6a mayor del "BB box". Ya estaba en el ej. 54 del bonus desde
#                siempre, pero el regex viejo no la veia: la caza este arreglo.
#                Tambien es "el 6 agregado" del ej. 36-bis (Am pentatonica + 6).
#
# Si se agrega una tercera, escribir aca POR QUE. Una lista de excepciones sin
# motivo escrito deja de ser una excepcion y pasa a ser un agujero.
CROMATICAS = {
    4: {"ees'": 13, "dis'": 13},
    3: {"ees'": 8, "dis'": 8, "b": 4, "fis'": 11},
    2: {"b'": 12},
    1: {"ees''": 11, "dis''": 11, "b'": 7},
}

CAJAS = {1: (5, 8), 2: (7, 10), 3: (9, 13), 4: (12, 15), 5: (2, 5)}

# OJO con este regex: la version anterior era r"([a-g][,']*)\d*\.*\\(\d)" y NO
# contemplaba alteraciones, asi que "ees'" (el blue note del ej. 26) y "dis'" no
# matcheaban nunca. El validador informaba "escala OK" sin haber mirado una sola
# nota alterada — justo las que mas probable es que esten mal. Si se toca este
# regex, probarlo contra ees' / dis' / b antes de dar nada por bueno.
NOTA = re.compile(r"([a-g](?:isis|eses|is|es)?[,']*)\d*\.*\\(\d)")


def frets(src):
    out, fallos = [], []
    for pitch, cuerda in NOTA.findall(src):
        c = int(cuerda)
        if pitch in MAPA.get(c, {}):
            out.append(MAPA[c][pitch])
        elif pitch in CROMATICAS.get(c, {}):
            out.append(CROMATICAS[c][pitch])
            CROMATICAS_USADAS.append((pitch, c))
        else:
            fallos.append((pitch, c))
    return out, fallos


def cajas_de(f):
    return [c for c, (a, b) in CAJAS.items() if a <= f <= b]


def cajas_exclusivas(fs):
    """Cajas que el ejercicio pisa SIN AMBIGÜEDAD.

    Las ventanas se solapan: el traste 5 es caja 1 y caja 5 a la vez, el 12 y el
    13 son caja 3 y caja 4. Una nota en un traste compartido no prueba que el
    ejercicio haya llegado a la caja que promete el texto. Esta lista sólo cuenta
    los trastes que pertenecen a una única caja.

    OJO al leer esto: las cajas 2 y 3 nunca pueden aparecer acá, y no es un error.
    Sus trastes exclusivos (6 y 11) no tienen ninguna nota de la pentatónica de La
    menor, así que toda nota de la caja 2 o 3 comparte ventana con una vecina. La
    columna sirve para las cajas 1, 4 y 5: si el texto promete una de esas tres y
    no aparece acá, la promesa no se está cumpliendo.
    """
    return sorted({cs[0] for f in fs for cs in [cajas_de(f)] if len(cs) == 1})


FUERA_DE_ESCALA = []
CROMATICAS_USADAS = []


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
        print("  %-5s notas=%3d  trastes %2d-%2d  fuera de 5-8: %3d (%4.0f%%)  cajas: %-15s exclusivas: %s"
              % (k, len(fs), min(fs), max(fs), len(fuera),
                 100 * len(fuera) / len(fs), usadas, cajas_exclusivas(fs)))
    print("-" * 78)
    print("  TOTAL: %d notas · %d fuera de la ventana 5-8 (%.1f%%)"
          % (tot_notas, tot_fuera, 100 * tot_fuera / tot_notas))
    print("  Ejercicios que NO salen de la ventana 5-8: %d/%d  -> %s"
          % (len(solo_c1), len(EJ), ", ".join(solo_c1)))
    print()


def tabla_de_trastes():
    """Imprime, cuerda por cuerda, qué trastes son de la pentatónica y de qué caja.

    Existe porque esta tabla se escribió a mano en un briefing para otra sesión y
    salió mal: se listó el traste 7 de la 6ª cuerda como nota válida, cuando ahí
    hay un SI, que no pertenece a la escala. El traste 7 es LA — pero en la 4ª
    cuerda, no en la 6ª. Cada cuerda tiene sus propios trastes y no se pueden
    mezclar de memoria.

        python scripts/auditar_cajas.py --tabla
    """
    nombre = {"a": "LA", "c": "DO", "d": "RE", "e": "MI", "g": "SOL"}
    print("=" * 78)
    print("TRASTES DE LA PENTATÓNICA DE LA MENOR, POR CUERDA")
    print("Entre corchetes, las cajas a las que pertenece cada traste.")
    print("Un traste que no figura acá es una nota fuera de la escala.")
    print("=" * 78)
    for cuerda in range(1, 7):
        celdas = []
        for pitch, f in sorted(MAPA[cuerda].items(), key=lambda kv: kv[1]):
            celdas.append("%2d=%-3s%s" % (f, nombre[pitch[0]], cajas_de(f)))
        print("  cuerda %d:  %s" % (cuerda, "  ".join(celdas)))
    print()
    print("  Trastes exclusivos de una sola caja: 2 y 3 -> caja 5 · 14 y 15 -> caja 4.")
    print("  Las cajas 2 y 3 no tienen ninguno (sus trastes propios, 6 y 11, están")
    print("  fuera de la escala). Por eso nunca aparecen en la columna 'exclusivas'.")
    print("=" * 78)
    print()


def valida_compases():
    """Compila cada partitura y reporta los compases que no suman 4 negras.

    Existe porque el ej. 7 del Hito 1 llegó al alumno con un compás de 4/4 que
    tenía 4 tiempos y medio adentro (`g8 e d c2.` = 4,5): si lo tocaba con
    metrónomo, no cerraba. LilyPond lo venía avisando en cada build con un
    "barcheck failed", pero el aviso se perdía entre el resto de la salida y
    nadie lo miraba. Ahora falla ruidoso, como la validación de escala.

    No se puede reemplazar por aritmética en Python: hay que resolver duraciones
    heredadas, tresillos y ligaduras, y el markup mete letras a-g que parecen
    notas. LilyPond ya sabe hacer todo eso — se le pregunta a él.
    """
    import glob
    import subprocess
    malos = []
    for ly in sorted(glob.glob(os.path.join(PARTITURAS, "*.ly"))):
        nombre = os.path.basename(ly)[:-3]
        r = subprocess.run(["lilypond", "-dcrop", "-o", "/tmp/_bc_" + nombre, ly],
                           capture_output=True, text=True)
        fallos = [l for l in r.stderr.splitlines() if "barcheck failed" in l]
        if fallos:
            malos.append((nombre, fallos[0].split("at:")[-1].strip()))
    return malos


PARTITURAS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "partituras")

if "--compases" in sys.argv:
    print("=" * 78)
    print("VALIDACIÓN DE COMPASES (barcheck de LilyPond sobre cada partitura)")
    print("=" * 78)
    malos = valida_compases()
    for nombre, exceso in malos:
        print("  !! %s — un compás no suma 4 negras (sobra/falta %s)" % (nombre, exceso))
    if malos:
        print("\nUn compás mal medido no se ve leyendo la tablatura, pero el alumno lo choca")
        print("apenas pone el metrónomo. Arreglar antes de exportar el PDF.")
        sys.exit(1)
    print("OK — los compases de todas las partituras suman 4 negras.")
    print("=" * 78)
    sys.exit(0)

if "--tabla" in sys.argv:
    tabla_de_trastes()
    sys.exit(0)


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
