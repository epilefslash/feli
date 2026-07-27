# Scripts del cuadernillo de ejercicios (Hito 1)

Generan `Cuadernillo-Hito1-El-Mapa-EJERCICIOS.pdf`.

## Para qué sirve cada uno

- **`gen_scores.py`** — escribe las partituras. Cada ejercicio es un bloque de LilyPond
  (`EJ["e01"]`, `EJ["e02"]`, …) y se renderiza a PNG con pentagrama + tablatura.
  Si querés **cambiar un ejercicio**, editás ese bloque y volvés a correr el script.
- **`build_hito1.py`** — arma el PDF: diagramas de mástil, textos, tablas y las partituras.
  Si querés **cambiar un texto o una consigna**, se edita acá.

## Cómo se corre

```bash
apt-get install -y lilypond          # una sola vez
pip install reportlab                # una sola vez
python3 gen_scores.py                # 1) genera las partituras
python3 build_hito1.py               # 2) arma el PDF
```

## Cómo se escribe una nota en LilyPond

Las alturas están escritas como suenan, y la cuerda se indica con `\1` … `\6`.
Referencia rápida en La menor pentatónica:

| Cuerda | Trastes de la escala | Cómo se escribe |
|---|---|---|
| 6ª (Mi grave) | 3, 5, 8, 10, 12, 15 | `g,` `a,` `c` `d` `e` `g` |
| 5ª (La) | 3, 5, 7, 10, 12, 15 | `c` `d` `e` `g` `a` `c'` |
| 4ª (Re) | 2, 5, 7, 10, 12, 14 | `e` `g` `a` `c'` `d'` `e'` |
| 3ª (Sol) | 2, 5, 7, 9, 12, 14 | `a` `c'` `d'` `e'` `g'` `a'` |
| 2ª (Si) | 3, 5, 8, 10, 13, 15 | `d'` `e'` `g'` `a'` `c''` `d''` |
| 1ª (Mi agudo) | 3, 5, 8, 10, 12, 15, 17 | `g'` `a'` `c''` `d''` `e''` `g''` `a''` |

Duraciones: `4` = negra, `8` = corchea, `2` = blanca, `1` = redonda, `4.` = negra con puntito.
Un `|` cierra el compás. `r4` es un silencio de negra.

Ejemplo — La (6ª cuerda traste 5) y Do (6ª traste 8) en corcheas:

```lilypond
a,8\6 c\6
```

Otros símbolos:
- `\glissando` entre dos notas = slide.
- `^\markup{\bold "bend 1 tono"}` = cartel arriba de la nota.
- `~` = ligadura de prolongación (la nota sigue sonando).
