# -*- coding: utf-8 -*-
"""Genera la partitura del ejercicio nuevo del MÓDULO DE RITMO (mes 2, Pozzoli).

Salida: ./partituras/rit_celula_viaja.cropped.png

ORIGEN. Feli trajo un PDF de ejercicios "al estilo de Tony Iommi" (créditos "Words &
Music by Sukko" — NO es una transcripción real) y señaló lo que valía adentro: una
sola celda de la pentatónica en la caja 1, repetida en subdivisiones crecientes, con
ligados y apoyaturas, incluyendo el TRESILLO DE SEMICORCHEAS (6 por pulso) — la figura
del trino de Hendrix/Clapton/Page, y la única de la escalera binaria que no está en
ningún cuadernillo del programa.

La primera lectura de ese PDF lo descartó como shred por los "sextillizos a ♩=120".
Ese diagnóstico estaba mal y conviene dejarlo escrito para no repetirlo: los compases
5-6 del original no son una escala corrida, son DOS NOTAS alternadas con H y P — o sea
UNA púa cada seis notas. Es una textura (un trino), no una carrera. Medir esa figura en
notas-por-segundo es el error; lo que hay que mirar es cuántos ATAQUES DE PÚA tiene.

QUÉ SE TOMÓ Y QUÉ NO
  ✓ La escalera de subdivisiones sobre una celda fija.
  ✓ El tresillo de semicorcheas (la figura que faltaba).
  ✓ Los ligados como parte del contenido: al comprimir, la derecha hace MENOS.
  ✗ Las repeticiones "5x" (drill mecánico) y el recorrido descendente por 5 cuerdas:
    alargan sin agregar. Acá la celda es de dos notas y no se mueve.
  ✗ Tony Iommi como referente nombrado — no está en el panel del programa
    (metal/doom, no rock/blues pentatónico). El ejercicio no cita a nadie.

LA CELDA: 1ª cuerda, trastes 5 y 8 (LA y DO) = a' y c''. Es la misma celda de la
caja 1 que usa el anexo del mes 3, a propósito.

EL BPM NO SE TOCA. Es la regla que protege al Hito 2: la figura se comprime, el pulso
no. Si el alumno sube el metrónomo, el ejercicio se convierte en lo que el reel #3
denuncia.

LA TAREA (idea de Feli, y es lo que convierte el drill en ejercicio del programa):
repetir la escalera entera en las cajas 2, 3, 4 y 5. El compás 6 muestra la caja 2
como modelo; las otras tres las saca el alumno. Es el mismo movimiento del ej. 46 del
Hito 3 (un lick en las 5 cajas) aplicado al eje rítmico.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_scores import render

EJ = {}

EJ["rit_celula_viaja"] = r"""
  a'4\1^\markup{\bold "1 · NEGRAS — 1 por pulso · 4 púas"} c''\1 a'\1 c''\1 |
  a'8\1^\markup{\bold "2 · CORCHEAS — 2 por pulso · 8 púas"} c''\1 a'\1 c''\1 a'\1 c''\1 a'\1 c''\1 |
  \tuplet 3/2 { a'8\1^\markup{\bold "3 · TRESILLO DE CORCHEAS — 3 por pulso · 4 púas"} c''\1( a'\1) }
  \tuplet 3/2 { c''8\1 a'\1( c''\1) }
  \tuplet 3/2 { a'8\1 c''\1( a'\1) }
  \tuplet 3/2 { c''8\1 a'\1( c''\1) } |
  \tuplet 3/2 { a'16\1^\markup{\bold "4 · TRESILLO DE SEMICORCHEAS — 6 por pulso · SIGUEN 4 púas"} c''\1( a'\1 c''\1 a'\1 c''\1) }
  \tuplet 3/2 { a'16\1 c''\1( a'\1 c''\1 a'\1 c''\1) }
  \tuplet 3/2 { a'16\1 c''\1( a'\1 c''\1 a'\1 c''\1) }
  \tuplet 3/2 { a'16\1 c''\1( a'\1 c''\1 a'\1 c''\1) } |
  \tuplet 3/2 { a'16\1^\markup{\bold "5 · la misma, con el pulso 2 en silencio"} c''\1( a'\1 c''\1 a'\1 c''\1) }
  r4
  \tuplet 3/2 { a'16\1 c''\1( a'\1 c''\1 a'\1 c''\1) }
  r4 |
  \tuplet 3/2 { c''16\1^\markup{\bold "6 · LA TAREA — la misma escalera en caja 2, y después 3, 4 y 5"} d''\1( c''\1 d''\1 c''\1 d''\1) }
  \tuplet 3/2 { c''16\1 d''\1( c''\1 d''\1 c''\1 d''\1) }
  \tuplet 3/2 { c''16\1 d''\1( c''\1 d''\1 c''\1 d''\1) }
  \tuplet 3/2 { c''16\1 d''\1( c''\1 d''\1 c''\1 d''\1) } |
"""

if __name__ == "__main__":
    fails = [k for k in sorted(EJ) if not render(k, EJ[k])]
    print("\nFallaron:", fails if fails else "ninguno")
