# -*- coding: utf-8 -*-
"""Convierte un MusicXML de Guitar Pro al dialecto LilyPond de este repo.

    python3 scripts/importar_musicxml.py archivo.xml [--nombre r08]

Existe por un motivo puntual y vale la pena dejarlo escrito: **re-tipear una
tablatura mirándola es exactamente el error que venimos cazando hace tres rondas**
(Design redibujó el ej. 47 y metió un FA fuera de escala 6 veces; aplastó las 4
llegadas del ej. 50 en una sola caja). Si Feli transcribe algo en Guitar Pro y yo
lo copio a ojo, reproduzco el mismo bug. Con el MusicXML no hay lectura humana en
el medio: se parsea la altura y el número de cuerda, y de ahí sale la nota.

Qué lee (del pentagrama de TABLATURA, staff 2, que es el único que trae
<string>/<fret>):
    pitch + string      -> nota LilyPond + \\N
    type + dots         -> figura
    tie                 -> ~
    slur                -> ( )
    hammer-on/pull-off  -> ^"H" / ^"P"
    slide               -> \\glissando + ^"sl."
    bend                -> \\tabSym \\bendFull  (1 tono)  ·  \\bendHalf (medio)
    <words>             -> ^\\markup{\\bold "..."}  (las cuentas "1 and 2 and")
    grace               -> \\grace

Los tresillos SI se traducen (<time-modification> -> \\tuplet A/N). Se agregaron
despues de que el ej. I fallara el barcheck: la "Frase larga 1" tiene uno y sin
soportarlo el compas daba 18/16 en vez de 16/16. Moraleja: **el barcheck de
LilyPond es el que valida la importacion**, no la vista.

Lo que NO traduce y hay que revisar a mano: dinamicas, y los <rehearsal> (EX1,
EX2...), que conviene reescribir como texto del ejercicio en vez de meterlos en
la partitura.
"""
import sys
import xml.etree.ElementTree as ET

TIPO = {"whole": "1", "half": "2", "quarter": "4", "eighth": "8",
        "16th": "16", "32nd": "32", "64th": "64"}


def lily_pitch(step, alter, octave):
    """C4 (do central) = c' en LilyPond. Los alter salen como is/es."""
    n = step.lower()
    if alter == 1:
        n += "is"
    elif alter == -1:
        n += "es"
    elif alter == 2:
        n += "isis"
    elif alter == -2:
        n += "eses"
    if octave >= 3:
        n += "'" * (octave - 3)
    else:
        n += "," * (3 - octave)
    return n


def texto(el, path, default=None):
    x = el.find(path)
    return x.text if x is not None else default


def convertir(ruta):
    root = ET.parse(ruta).getroot()
    salida, compas_n = [], 0

    for measure in root.iter("measure"):
        compas_n += 1
        linea, pendientes, ya_puestos = [], [], set()

        for hijo in measure:
            # los <words> traen las cuentas ("1 and 2 and") — se guardan para
            # colgarlas de la nota o silencio que viene justo despues
            if hijo.tag == "direction":
                w = hijo.find(".//words")
                if w is not None and w.text and w.text.strip():
                    t = w.text.strip()
                    # el XML repite cada cartel una vez por pentagrama; con uno alcanza
                    if t not in pendientes and t not in ya_puestos:
                        pendientes.append(t)
                continue
            if hijo.tag != "note":
                continue
            # SOLO el pentagrama de tablatura: es el que trae string/fret
            if texto(hijo, "staff") != "2":
                continue

            tec = hijo.find(".//technical")
            nots = hijo.find("notations")
            es_gracia = hijo.find("grace") is not None
            tipo = texto(hijo, "type", "quarter")
            dur = TIPO.get(tipo, "4") + "." * len(hijo.findall("dot"))

            if hijo.find("rest") is not None:
                tok = "r" + dur
            else:
                p = hijo.find("pitch")
                alter = int(texto(p, "alter", "0"))
                tok = lily_pitch(texto(p, "step"), alter, int(texto(p, "octave")))
                tok += dur
                cuerda = texto(tec, "string") if tec is not None else None
                if cuerda:
                    tok += "\\" + cuerda

            if es_gracia:
                tok = "\\grace " + tok

            # --- articulaciones ---
            marcas = []
            if tec is not None:
                b = tec.find("bend")
                if b is not None and b.find("release") is None:
                    alt = float(texto(b, "bend-alter", "0"))
                    tok += " \\tabSym " + ("\\bendFull" if abs(alt) >= 2 else "\\bendHalf")
                elif b is not None:
                    tok += " \\tabSym \\bendRel"
                if tec.find("hammer-on") is not None and \
                        tec.find("hammer-on").get("type") == "start":
                    marcas.append("H")
                if tec.find("pull-off") is not None and \
                        tec.find("pull-off").get("type") == "start":
                    marcas.append("P")

            if nots is not None:
                for sl in nots.findall("slide"):
                    if sl.get("type") == "start":
                        tok += " \\glissando"
                        marcas.append("sl.")

            for m in marcas:
                tok += '^\\markup{\\bold\\small "%s"}' % m
            for w in pendientes:
                tok += '^\\markup{\\bold "%s"}' % w.replace('"', "'")
                ya_puestos.add(w)
            pendientes = []

            # ligaduras de expresion (slur) y de prolongacion (tie)
            if nots is not None:
                tipos = [x.get("type") for x in nots.findall("slur")]
                if "stop" in tipos:              # primero cierra la anterior,
                    tok += ")"                   # despues abre la siguiente:
                if "start" in tipos:             # "()" seria una ligadura vacia
                    tok += "("
                if nots.find("tied[@type='start']") is not None:
                    tok += " ~"

            # --- tresillos: <time-modification> + <tuplet start/stop> ---
            tm = hijo.find("time-modification")
            abre = cierra = None
            if nots is not None:
                for t in nots.findall("tuplet"):
                    if t.get("type") == "start" and tm is not None:
                        abre = "\\tuplet %s/%s {" % (texto(tm, "actual-notes"),
                                                    texto(tm, "normal-notes"))
                    elif t.get("type") == "stop":
                        cierra = "}"
            if abre:
                linea.append(abre)
            linea.append(tok)
            if cierra:
                linea.append(cierra)

        if linea:
            salida.append("  " + " ".join(linea) + " |")

    return salida, compas_n


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    nombre = "impNN"
    if "--nombre" in sys.argv:
        nombre = sys.argv[sys.argv.index("--nombre") + 1]
    lineas, n = convertir(args[0])
    print('EJ["%s"] = r"""' % nombre)
    print("\n".join(lineas))
    print('"""')
    print("\n# %d compases importados de %s" % (n, args[0].split("/")[-1]), file=sys.stderr)
