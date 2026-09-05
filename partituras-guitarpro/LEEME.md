# Partituras originales de Feli (Guitar Pro)

Los fuentes de las tres partituras que Feli transcribió en Guitar Pro, guardados
acá para que no dependan de su máquina ni de un chat.

| Archivo | Dónde se usa |
|---|---|
| `reto-de-construccion-de-frases.pdf` / `.xml` | **Anexo, ej. H** (compases 1-18) y **H-bis** (19-34) |
| `llamada-y-respuesta.pdf` / `.xml` | **Anexo, ej. I** (los 14 compases) |
| `subdivisiones.pdf` / `.xml` | **No se usa.** Decisión de Feli: lo ubica en otro lado |

## Cómo se generan las imágenes del cuadernillo

Las imágenes que van al anexo son **recortes del PDF**, no renders de LilyPond —
la tipografía de Guitar Pro se ve mejor para estas piezas densas:

    pdftoppm -r 300 -png reto-de-construccion-de-frases.pdf /tmp/gpreto
    # y después recortar los sistemas con Pillow a
    # scripts/partituras/r08.cropped.png · r08b · r09

⚠️ **Las notas de estas tres viven igual en `scripts/gen_scores_ritmo.py`**, con
claves que empiezan con `_` (`_ref_h`, `_ref_hbis`, `_ref_i`). No se renderizan —
si se les saca el guion bajo, el generador **pisa** las imágenes de Feli. Están
ahí para que `auditar_cajas.py` las mida y para que el barcheck de LilyPond
verifique que los compases cierran. Así se encontró el compás de 18/16 de la
Frase larga 1, que en la partitura renderizada no se veía.

## Si Feli cambia una transcripción

1. Exporta de Guitar Pro el **PDF** y el **MusicXML**
2. Los reemplaza acá
3. `python3 scripts/importar_musicxml.py <archivo>.xml --nombre _ref_h` y pega el
   resultado en `gen_scores_ritmo.py` (para que la auditoría siga midiendo bien)
4. Recorta el PDF nuevo a `scripts/partituras/`
5. `python3 scripts/build_ritmo.py`
