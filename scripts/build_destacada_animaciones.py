# -*- coding: utf-8 -*-
"""Convierte las 7 placas de la destacada METODO en videos verticales de 5 segundos.

POR QUE POR CODIGO Y NO CON UNA IA DE VIDEO (pedido de Feli, 18/9): las IA de imagen-a-video
generan el movimiento alucinando pixeles cuadro a cuadro, y un diagrama de mastil —puntos
alineados en una grilla, numeros de traste— es exactamente lo que peor les sale. Deformarian
el mastil igual que Claude Design lo redibujo mal (`memoria/05` SS55). Aca cada cuadro se
DIBUJA con los mismos datos verificados del repo: el traste 7 sigue siendo el traste 7 en los
125 cuadros.

Dos animaciones, las dos deliberadamente sobrias -- esto acompana al texto, no compite:

1. **Zoom lento** (Ken Burns) en las 7: 100% -> 106% a lo largo del video. Se rasteriza a
   1.5x y se recorta hacia adentro, asi que el zoom NO pixela: siempre hay mas resolucion
   de la que se muestra.
2. **Las cajas encendiendose**, solo en las 2 placas de mastil. El mastil arranca todo en
   gris y cada caja se prende por turno, hasta que al final se prende el mastil entero. Es
   literalmente la tesis del Pilar 1 contada en 5 segundos: 5 cajas sueltas -> un solo mapa.

Salida: entregables/destacadas/animadas/*.mp4 (1080x1920, H.264, sin audio).

Uso:
    python3 scripts/build_destacada_animaciones.py
"""
import os
import shutil
import subprocess
import tempfile

from PIL import Image

import destacada_graficos as G
import build_destacada_titlecards as T

FPS = 25
SEGUNDOS = 5.0
ZOOM_FINAL = 1.06          # cuanto se acerca al final. Mas que esto ya marea.
SUPER = 1.5                # se rasteriza a 1.5x para que el zoom no pixele
FUNDIDO = 4                # cuadros de mezcla al cambiar de estado

W, H = 1080, 1920
SALIDA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                      "entregables", "destacadas", "animadas")


def _estados_mapa():
    """Placa 1: el mastil entero, prendiendo una caja por vez y cerrando con todo prendido."""
    orden = [(5,), (5, 1), (5, 1, 2), (5, 1, 2, 3), (5, 1, 2, 3, 4)]
    estados = []
    for prendidas in orden:
        estados.append([
            T.eyebrow("// EL MÉTODO, EN 2 MINUTOS"),
            T.titulo(["Cómo paso de tocar", "siempre lo mismo…", "a un solo que es tuyo."]),
            T.Tarjeta(_mapa(prendidas), 470, 125, gap=58),
            T.pie(["Mirá las siguientes historias"]),
        ])
    estados.append([                                    # cierre: el mastil completo
        T.eyebrow("// EL MÉTODO, EN 2 MINUTOS"),
        T.titulo(["Cómo paso de tocar", "siempre lo mismo…", "a un solo que es tuyo."]),
        T.Tarjeta(_mapa(None), 470, 125, gap=58),
        T.pie(["Mirá las siguientes historias"]),
    ])
    return estados


def _mapa(prendidas):
    cajas = (5, 1, 2, 3, 4) if prendidas is None else tuple(prendidas)
    return lambda c, x, y, w: G.mapa_completo(c, x, y, w, hs=40, cajas=cajas,
                                              encendidas=prendidas)


def _estados_puente():
    """Placa 2: primero la caja 1, despues la 2, y al final los puentes entre las dos."""
    puentes = G.notas_compartidas(1, 2)
    base = lambda cajas, anillos: T.Tarjeta(
        lambda c, x, y, w: G.mapa_completo(c, x, y, w, hs=40, f0=4, f1=11, cajas=cajas,
                                           leyenda=False, anillos=anillos,
                                           encendidas=cajas),
        386, 45, gap=54,
        titulo="DONDE LA CAJA 1 SE TOCA CON LA 2",
        pie="Las marcadas son de las dos cajas. Ahí se cruza.")
    return [[T.eyebrow("// PILAR 1"), T.titulo_pilar("EL MAPA"),
             T.bajada("dominar el mástil"), base(cajas, anillos),
             T.pie(["5 cajas sueltas pasan a ser", "un solo mástil."])]
            for cajas, anillos in [((1,), ()), ((1, 2), ()), ((1, 2), puentes)]]


def render_estados(bloques_por_estado, tmp):
    """Cada estado -> un PNG a 1.5x. Devuelve las imagenes ya abiertas, en orden."""
    imgs = []
    for i, bloques in enumerate(bloques_por_estado):
        pdf = os.path.join(tmp, "estado%02d.pdf" % i)
        T.placa(None, bloques, ruta=pdf, png=False)
        subprocess.run(["pdftoppm", "-png", "-r", str(int(72 * SUPER)), "-singlefile",
                        pdf, pdf[:-4]], check=True)
        imgs.append(Image.open(pdf[:-4] + ".png").convert("RGB"))
    return imgs


def animar(nombre, bloques_por_estado, hasta=0.62):
    """Arma el mp4. `hasta` = en que fraccion del video termina de cambiar de estado."""
    total = int(FPS * SEGUNDOS)
    with tempfile.TemporaryDirectory() as tmp:
        imgs = render_estados(bloques_por_estado, tmp)
        bw, bh = imgs[0].size
        n = len(imgs)
        # cuadro en el que entra cada estado; el ultimo se sostiene hasta el final
        cortes = [0] if n == 1 else [round(i * total * hasta / (n - 1)) for i in range(n)]

        cuadros = os.path.join(tmp, "f")
        os.makedirs(cuadros)
        for f in range(total):
            idx = max(i for i, c in enumerate(cortes) if c <= f)
            base = imgs[idx]
            # mezcla corta al entrar un estado nuevo, para que no sea un salto seco
            if idx > 0 and f - cortes[idx] < FUNDIDO:
                base = Image.blend(imgs[idx - 1], base, (f - cortes[idx] + 1.0) / FUNDIDO)

            z = 1.0 + (ZOOM_FINAL - 1.0) * (f / float(total - 1))
            cw, ch = bw / z, bh / z
            x0, y0 = (bw - cw) / 2, (bh - ch) / 2
            (base.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch)))
                 .resize((W, H), Image.LANCZOS)
                 .save(os.path.join(cuadros, "%04d.png" % f)))

        destino = os.path.join(SALIDA, nombre)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS),
                        "-i", os.path.join(cuadros, "%04d.png"),
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18",
                        destino], check=True)
    print("OK", nombre, "· %d estados" % len(bloques_por_estado))


def main():
    if not shutil.which("ffmpeg"):
        raise SystemExit("Falta ffmpeg: apt-get install -y ffmpeg")
    os.makedirs(SALIDA, exist_ok=True)

    animar("destacada-1-gancho.mp4", _estados_mapa())
    animar("destacada-2-pilar1-mapa.mp4", _estados_puente())

    # Las otras 5 no tienen nada que "encender": van con el zoom solo.
    for nombre, bloques in T.tarjetas()[2:]:
        animar(nombre.replace(".pdf", ".mp4"), [bloques])


if __name__ == "__main__":
    main()
