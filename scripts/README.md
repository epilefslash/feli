# Scripts de los cuadernillos de ejercicios

Generan los PDFs con partitura + tablatura de los 3 hitos (53 ejercicios, numeración corrida 1-53) + el
bonus post-programa (6 licks más, 54-59).

> **Antes de exportar cualquier PDF, corré `python3 auditar_cajas.py`.** Además de reportar el % de
> notas fuera de la caja 1, valida que ninguna nota se salga de la pentatónica de La menor y termina con
> código 1 si algo falla.

| Archivo | Qué hace |
|---|---|
| `gen_scores.py` | Partituras del **Hito 1** (ejercicios 1 a 16) |
| `gen_scores_h2.py` | Partituras del **Hito 2** (ejercicios 17 a 34) |
| `gen_scores_h3.py` | Partituras del **Hito 3** (ejercicios 35 a 53) |
| `gen_scores_h3b.py` | Partituras del **bonus post-programa** — 6 licks fuera de la caja 1 (54 a 59) |
| `gen_scores_ritmo.py` | Partituras del **anexo de ritmo** (ejercicios A a G — no tocan la numeración 1-59) |
| `auditar_cajas.py` | Audita en qué cajas vive cada ejercicio + valida que todo caiga en la escala |
| `build_hito1.py` | Arma `Cuadernillo-Hito1-El-Mapa-EJERCICIOS.pdf` |
| `build_hito2.py` | Arma `Cuadernillo-Hito2-El-Sabor-EJERCICIOS.pdf` |
| `build_hito3.py` | Arma `Cuadernillo-Hito3-El-Vocabulario-EJERCICIOS.pdf` |
| `build_hito3b.py` | Arma `Cuadernillo-BONUS-Licks-Fuera-de-la-Caja1.pdf` |
| `build_ritmo.py` | Arma `Anexo-Ritmo-El-Arbol-y-las-3-Velocidades.pdf` — árbol, diminución, tresillo, swing y síncopa (va en paralelo al Hito 3) |
| `cuadernillo_comun.py` | Estética, diagramas de mástil, tablatura en blanco y tablas que comparten los tres |

- ¿Querés **cambiar un ejercicio**? Se edita el bloque `EJ["eNN"]` en el `gen_scores*.py` que corresponda.
- ¿Querés **cambiar un texto o una consigna**? Se edita el `build_hito*.py`.
- ¿Querés **cambiar colores o tipografía**? Se edita `cuadernillo_comun.py` (cambia en los dos hitos).

## Cómo se corre

```bash
apt-get install -y lilypond          # una sola vez
pip install reportlab                # una sola vez

python3 gen_scores.py                # partituras del hito 1  -> ./partituras/
python3 gen_scores_h2.py             # partituras del hito 2
python3 gen_scores_h3.py             # partituras del hito 3
python3 gen_scores_h3b.py            # partituras del bonus post-programa
python3 gen_scores_ritmo.py          # partituras del anexo de ritmo
python3 build_hito1.py               # PDF del hito 1  (queda en la carpeta de arriba)
python3 build_hito2.py               # PDF del hito 2
python3 build_hito3.py               # PDF del hito 3
python3 build_hito3b.py              # PDF del bonus post-programa
python3 build_ritmo.py               # PDF del anexo de ritmo
```

Si tocaste una partitura, corré el `gen_scores*.py` **antes** del `build_hito*.py`.

## Cómo se escribe una nota en LilyPond

Las alturas se escriben como suenan, y la cuerda se indica con `\1` … `\6`.
Referencia en La menor pentatónica:

| Cuerda | Trastes de la escala | Cómo se escribe |
|---|---|---|
| 6ª (Mi grave) | 3, 5, 8, 10, 12, 15 | `g,` `a,` `c` `d` `e` `g` |
| 5ª (La) | 3, 5, 7, 10, 12, 15 | `c` `d` `e` `g` `a` `c'` |
| 4ª (Re) | 2, 5, 7, 10, 12, 14 | `e` `g` `a` `c'` `d'` `e'` |
| 3ª (Sol) | 2, 5, 7, 9, 12, 14 | `a` `c'` `d'` `e'` `g'` `a'` |
| 2ª (Si) | 3, 5, 8, 10, 13, 15 | `d'` `e'` `g'` `a'` `c''` `d''` |
| 1ª (Mi agudo) | 3, 5, 8, 10, 12, 15, 17 | `g'` `a'` `c''` `d''` `e''` `g''` `a''` |

Duraciones: `4` negra · `8` corchea · `16` semicorchea · `2` blanca · `1` redonda · `4.` negra con puntito.
`|` cierra el compás. `r4` es un silencio de negra.

> **Ojo con el reparto de figuras.** Las 4 cuadernillos suman **995 notas**: corcheas 74% · negras 17% ·
> blancas 5% · redondas 3% · **2 semicorcheas** y ninguna fusa. Eso es a propósito (el ritmo se trabaja en
> el anexo, no dentro de los hitos), pero si agregás ejercicios conviene saberlo para no desbalancearlo más.
>
> ⚠️ **Al recontar, acordate de que la duración se HEREDA:** en `c''8\1 a'\1 g'\2 e'\2` hay cuatro corcheas
> y un solo `8` escrito. Contar los tokens con duración explícita da 395 y es un número inventado — ya se
> publicó una vez así. Hay que arrastrar la última duración vista.

Ejemplo — La (6ª cuerda traste 5) y Do (6ª traste 8) en corcheas:

```lilypond
a,8\6 c\6
```

Otros símbolos:

| Se escribe | Sale como |
|---|---|
| `a,8\6( c\6)` | ligado (hammer-on subiendo, pull-off bajando) |
| `\glissando` entre dos notas | slide |
| `^\markup{\bold "bend 1 tono"}` | cartel arriba de la nota |
| `~` | ligadura de prolongación (la nota sigue sonando; si cruza la barra de compás, la 2ª mitad **no lleva número en la TAB** — es correcto, no se vuelve a puntear) |
| `c''4.` | figura con puntillo (dura una vez y media) |
| `\p` `\mf` `\f` | dinámica (suave, medio, fuerte) |
| `\tuplet 3/2 { ... }` | tresillo |
| `<e'\2 a'\1>4` | doble cuerda (dos notas juntas) |

> **Antes de exportar, corré también `python3 auditar_cajas.py --compases`:** compila cada partitura y
> falla si algún compás no suma 4 negras. Existe porque el ej. 7 del Hito 1 llegó al alumno con un compás
> de 4 tiempos y medio — LilyPond lo venía avisando en cada build y el aviso se perdía entre el resto de
> la salida.

> LilyPond 2.24 no dibuja flechas de bending en la tablatura, por eso los bendings van
> anotados con `\markup`. Si algún día se actualiza a 2.25+, existe `\bendOn`.
