"""Genera PDF con el análisis armónico de 'Isabel' (Ratones Paranoicos)."""
from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("DejaVu", "I", 9)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, "Análisis armónico — Isabel (Ratones Paranoicos)",
                 align="R", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def footer(self):
        self.set_y(-12)
        self.set_font("DejaVu", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, f"Página {self.page_no()}", align="C")


NAVY = (20, 40, 80)
ACCENT = (150, 30, 30)
GREY = (90, 90, 90)
LIGHT = (235, 235, 240)
LIGHT2 = (245, 240, 230)


def h1(pdf, text):
    pdf.set_font("DejaVu", "B", 20)
    pdf.set_text_color(*NAVY)
    pdf.multi_cell(0, 9, text, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)


def h2(pdf, text):
    pdf.set_font("DejaVu", "B", 14)
    pdf.set_text_color(*ACCENT)
    pdf.ln(2)
    pdf.multi_cell(0, 7, text, new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(*ACCENT)
    pdf.set_line_width(0.4)
    y = pdf.get_y()
    pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
    pdf.ln(2)


def h3(pdf, text):
    pdf.set_font("DejaVu", "B", 11)
    pdf.set_text_color(*NAVY)
    pdf.ln(1)
    pdf.multi_cell(0, 6, text, new_x="LMARGIN", new_y="NEXT")


def body(pdf, text):
    pdf.set_font("DejaVu", "", 10.5)
    pdf.set_text_color(30, 30, 30)
    pdf.multi_cell(0, 5.5, text, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)


def bullet(pdf, text):
    pdf.set_font("DejaVu", "", 10.5)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(5)
    pdf.cell(4, 5.5, "•")
    pdf.multi_cell(0, 5.5, text, new_x="LMARGIN", new_y="NEXT")


def info_box(pdf, title, body_text, accent=(150, 30, 30)):
    # calcular altura del cuerpo
    pdf.set_font("DejaVu", "", 10)
    left_pad = 4
    usable_w = pdf.w - pdf.l_margin - pdf.r_margin - 2 * left_pad
    lines = pdf.multi_cell(usable_w, 5.2, body_text,
                          dry_run=True, output="LINES")
    body_h = len(lines) * 5.2
    total_h = 8 + body_h + 4  # título + cuerpo + padding
    x0 = pdf.l_margin
    y0 = pdf.get_y()
    # fondo
    pdf.set_fill_color(250, 247, 240)
    pdf.rect(x0, y0, pdf.w - pdf.l_margin - pdf.r_margin, total_h,
            style="F")
    # barra lateral
    pdf.set_fill_color(*accent)
    pdf.rect(x0, y0, 2, total_h, style="F")
    # título
    pdf.set_xy(x0 + left_pad, y0 + 2)
    pdf.set_font("DejaVu", "B", 11)
    pdf.set_text_color(*accent)
    pdf.cell(0, 6, title, new_x="LMARGIN", new_y="NEXT")
    # cuerpo
    pdf.set_x(x0 + left_pad)
    pdf.set_font("DejaVu", "", 10)
    pdf.set_text_color(30, 30, 30)
    pdf.multi_cell(usable_w, 5.2, body_text,
                  new_x="LMARGIN", new_y="NEXT")
    pdf.set_y(y0 + total_h + 3)


def table(pdf, headers, rows, col_widths, header_fill=NAVY, zebra=LIGHT):
    pdf.set_font("DejaVu", "B", 10)
    pdf.set_fill_color(*header_fill)
    pdf.set_text_color(255, 255, 255)
    pdf.set_draw_color(200, 200, 200)
    for i, h in enumerate(headers):
        pdf.cell(col_widths[i], 8, h, border=1, align="C", fill=True)
    pdf.ln(8)
    pdf.set_font("DejaVu", "", 10)
    pdf.set_text_color(30, 30, 30)
    for idx, row in enumerate(rows):
        fill = idx % 2 == 0
        if fill:
            pdf.set_fill_color(*zebra)
        for i, val in enumerate(row):
            pdf.cell(col_widths[i], 7, val, border=1, align="C", fill=fill)
        pdf.ln(7)
    pdf.ln(2)


def table_wrap(pdf, headers, rows, col_widths, header_fill=NAVY, zebra=LIGHT):
    """Tabla con celdas que pueden tener texto largo (wrap)."""
    pdf.set_font("DejaVu", "B", 10)
    pdf.set_fill_color(*header_fill)
    pdf.set_text_color(255, 255, 255)
    pdf.set_draw_color(200, 200, 200)
    for i, h in enumerate(headers):
        pdf.cell(col_widths[i], 8, h, border=1, align="C", fill=True)
    pdf.ln(8)
    pdf.set_font("DejaVu", "", 9.5)
    pdf.set_text_color(30, 30, 30)
    line_h = 5
    for idx, row in enumerate(rows):
        # calcular alto necesario
        max_lines = 1
        for i, val in enumerate(row):
            w = col_widths[i]
            lines = pdf.multi_cell(w, line_h, val, split_only=True)
            if len(lines) > max_lines:
                max_lines = len(lines)
        h = max_lines * line_h + 1
        fill = idx % 2 == 0
        if fill:
            pdf.set_fill_color(*zebra)
        x0, y0 = pdf.get_x(), pdf.get_y()
        for i, val in enumerate(row):
            x, y = pdf.get_x(), pdf.get_y()
            pdf.multi_cell(col_widths[i], line_h, val, border=1,
                          align="C" if i < 2 else "L", fill=fill,
                          max_line_height=line_h)
            pdf.set_xy(x + col_widths[i], y)
        pdf.set_xy(x0, y0 + h)
    pdf.ln(2)


pdf = PDF(format="A4")
pdf.set_margins(18, 15, 18)
pdf.set_auto_page_break(auto=True, margin=18)

# Unicode fonts
DJ = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
DJB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
DJI = "/usr/share/fonts/truetype/freefont/FreeSansOblique.ttf"
DJBI = "/usr/share/fonts/truetype/freefont/FreeSansBoldOblique.ttf"
pdf.add_font("DejaVu", "", DJ)
pdf.add_font("DejaVu", "B", DJB)
pdf.add_font("DejaVu", "I", DJI)
pdf.add_font("DejaVu", "BI", DJBI)

pdf.add_page()

# ---------- PORTADA / TÍTULO ----------
pdf.set_font("DejaVu", "B", 26)
pdf.set_text_color(*NAVY)
pdf.ln(4)
pdf.multi_cell(0, 11, "Análisis armónico", new_x="LMARGIN", new_y="NEXT",
              align="C")
pdf.set_font("DejaVu", "B", 20)
pdf.set_text_color(*ACCENT)
pdf.multi_cell(0, 9, "«Isabel» — Ratones Paranoicos",
              new_x="LMARGIN", new_y="NEXT", align="C")
pdf.set_font("DejaVu", "I", 11)
pdf.set_text_color(*GREY)
pdf.multi_cell(0, 6, "Álbum: Fieras Lunáticas (1991) · Autor: Juanse",
              new_x="LMARGIN", new_y="NEXT", align="C")
pdf.ln(6)

# ---------- TONALIDAD ----------
h2(pdf, "1. Tonalidad")
body(pdf,
     "La canción está en LA MAYOR (A). El centro tonal es inequívoco: el "
     "riff de intro es un A5 repetido y todas las frases resuelven sobre A. "
     "Sin embargo, la paleta de acordes se enriquece con una dominante "
     "secundaria y con préstamos del modo menor paralelo, que son los que "
     "le dan a «Isabel» su color característico.")

# ---------- CUADRO 1: GRADOS DE LA MAYOR + PARALELA ----------
h2(pdf, "2. Grados de la escala — La mayor y su paralela La menor")
body(pdf,
     "Abajo, los siete grados de la escala de La mayor con su acorde "
     "diatónico, y debajo los grados de su paralela, La menor natural. "
     "El acorde del menor paralelo que usa el tema como préstamo "
     "modal es bVII = G.")

# Cabecera común: I - II - III - IV - V - VI - VII
col_widths = [28, 22, 22, 22, 22, 22, 22, 22]  # primera col = etiqueta

# Tabla LA MAYOR
pdf.set_font("DejaVu", "B", 11)
pdf.set_text_color(*NAVY)
pdf.cell(0, 7, "LA MAYOR (modo jónico)", new_x="LMARGIN", new_y="NEXT")
pdf.ln(1)

headers_maj = ["", "I", "ii", "iii", "IV", "V", "vi", "vii°"]
rows_maj = [
    ["Nota",     "A",   "B",   "C#",  "D",   "E",   "F#",  "G#"],
    ["Acorde",   "A",   "Bm",  "C#m", "D",   "E",   "F#m", "G#°"],
    ["Función",  "T",   "SD",  "T",   "SD",  "D",   "T",   "D"],
]
table(pdf, headers_maj, rows_maj, col_widths, header_fill=NAVY, zebra=LIGHT)

# Tabla LA MENOR (paralela)
pdf.set_font("DejaVu", "B", 11)
pdf.set_text_color(*ACCENT)
pdf.cell(0, 7, "LA MENOR NATURAL (modo eólico) — paralela",
        new_x="LMARGIN", new_y="NEXT")
pdf.ln(1)

headers_min = ["", "i", "ii°", "bIII", "iv", "v", "bVI", "bVII"]
rows_min = [
    ["Nota",     "A",   "B",   "C",   "D",   "E",   "F",   "G"],
    ["Acorde",   "Am",  "B°",  "C",   "Dm",  "Em",  "F",   "G"],
    ["Función",  "T",   "SD",  "T",   "SD",  "D",   "T",   "SD/D"],
]
table(pdf, headers_min, rows_min, col_widths,
     header_fill=ACCENT, zebra=LIGHT2)

body(pdf,
     "T = tónica · SD = subdominante · D = dominante. "
     "El acorde de La menor que aparece en «Isabel» es G (bVII): "
     "préstamo modal del paralelo menor / mixolidio.")

# ---------- ACORDES USADOS EN EL TEMA ----------
pdf.add_page()
h2(pdf, "3. Acordes que usa el tema y su función")

headers_f = ["Acorde", "Grado", "Explicación"]
rows_f = [
    ["A",     "I",
     "Tónica. Reposo absoluto. El riff de intro es A5."],
    ["F#",    "V/ii",
     "Dominante secundaria de Bm. La tercera mayor (A#) es la "
     "nota ajena al tono; crea tensión hacia Bm."],
    ["Bm7",   "ii7",
     "Subdominante menor. Destino natural del F#. Color suspendido."],
    ["F#m7",  "vi7",
     "Relativa menor. Función de tónica «triste»."],
    ["G",     "bVII",
     "Préstamo del menor paralelo / mixolidio. Sonido rockero-modal. "
     "Es el acorde más característico del tema junto al F#."],
    ["E",     "V",
     "Dominante principal. Resuelve a A (I)."],
]
table_wrap(pdf, headers_f, rows_f, [22, 22, 132], header_fill=NAVY)

# ---------- ESTRUCTURA ----------
h2(pdf, "4. Estructura de la canción")

headers_s = ["#", "Sección", "Armonía", "Lectura"]
rows_s = [
    ["1", "Intro",
     "A5 (x4)",
     "Riff sobre power chord. Establece tónica y pulso."],
    ["2", "Verso",
     "A — F#",
     "I — V/ii. Dominante secundaria «suspendida»: tensión sin "
     "resolver de inmediato."],
    ["3", "Estribillo",
     "Bm7 — F#m7",
     "ii7 — vi7. Resolución del F# al Bm y deslizamiento cromático "
     "al F#m. Flota lejos de la tónica."],
    ["4", "Giro / cadencia",
     "G — E — A",
     "bVII — V — I. Cadencia rockera clásica: el bVII (préstamo "
     "modal) baja al V y resuelve a la tónica. Mezcla sonoridad "
     "modal (mixolidia) con cadencia auténtica."],
    ["5", "Solo",
     "Verso + estribillo",
     "Pentatónica/blues de La con guiños al mixolidio sobre el G."],
    ["6", "Final",
     "A — G (vamp)",
     "I — bVII. Cadencia modal de cierre, sello stone."],
]
table_wrap(pdf, headers_s, rows_s, [10, 36, 40, 90], header_fill=NAVY)

# ---------- RECURSOS ARMÓNICOS ----------
h2(pdf, "5. Recursos armónicos clave")
bullet(pdf, "Dominante secundaria V/ii (F# → Bm): motor armónico "
           "del verso; aporta «mordida» y evita el diatonismo puro.")
bullet(pdf, "Préstamo del menor paralelo: G (bVII), tomado de "
           "La menor / mixolidio. Sello del rock stone.")
bullet(pdf, "Cadencia bVII — V — I (G — E — A): híbrido entre "
           "cadencia modal mixolidia (bVII → I) y cadencia "
           "auténtica (V → I). Muy usada en rock clásico — "
           "aparece, por ejemplo, en «Hey Joe» (Jimi Hendrix), "
           "«With A Little Help From My Friends» (The Beatles) "
           "y «Sympathy for the Devil» (Rolling Stones).")
bullet(pdf, "Séptimas en el estribillo (Bm7, F#m7): enriquecen "
           "el color y hacen más cantábile la sección.")
bullet(pdf, "Power chord A5 en el riff: sin tercera, para que la "
           "melodía vocal y los acordes de relleno definan el "
           "carácter mayor/menor.")
bullet(pdf, "Modal mixture: conviven el diatonismo de La mayor "
           "(I-ii-IV-V-vi) con el préstamo del paralelo menor "
           "(bVII). Esta mezcla es parte de la identidad armónica "
           "del tema.")

# ---------- GLOSARIO ----------
h2(pdf, "6. Glosario armónico")
body(pdf,
     "Dos conceptos que aparecen a lo largo del análisis, explicados "
     "brevemente:")

info_box(pdf, "Diatónico",
     "Un acorde o nota es «diatónico» cuando pertenece a la escala de "
     "la tonalidad. En La mayor, los siete acordes diatónicos son "
     "A, Bm, C#m, D, E, F#m y G#°. Todo lo que suene fuera de ese "
     "conjunto es «no diatónico» o cromático. En «Isabel» los acordes "
     "diatónicos son A, Bm7, F#m7 y E; los no diatónicos son F# "
     "(con A# ajena al tono) y G (con G natural ajena al tono).",
     accent=NAVY)

info_box(pdf, "Dominante secundaria",
     "Un «dominante secundario» es un acorde mayor con séptima "
     "(V7) que no resuelve al I del tono, sino a otro grado de la "
     "escala. Se lo nota V/ii, V/iii, V/IV, V/V, V/vi. Su función es "
     "crear tensión-resolución hacia un grado secundario, enriqueciendo "
     "la armonía sin cambiar de tonalidad. En «Isabel», el F# mayor "
     "funciona como V/ii: es el dominante de Bm (ii), que es su "
     "destino natural en el estribillo.",
     accent=ACCENT)

# ---------- CONCLUSIÓN ----------
h2(pdf, "7. Conclusión")
body(pdf,
     "«Isabel» es un ejemplo de libro del rock stone/argentino: "
     "tonalidad mayor clara (La), pero coloreada con una dominante "
     "secundaria (F# → Bm) y un préstamo modal (G, bVII). Esa "
     "combinación —diatonismo mayor + modal mixture + V/ii + "
     "cadencia bVII-V-I— es lo que le da ese carácter «dulce y "
     "amargo» a la vez, tan ligado a la estética de los Rolling "
     "Stones que Juanse lleva como bandera.")

# ---------- FUENTES ----------
pdf.ln(2)
pdf.set_font("DejaVu", "B", 10)
pdf.set_text_color(*GREY)
pdf.cell(0, 6, "Fuentes consultadas:", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("DejaVu", "", 9)
for src in [
    "Cifra Club — cifraclub.com/ratones-paranoicos/isabel/",
    "La Cuerda — chords.lacuerda.net/ratones/isabel",
    "Acordes D Canciones — acordesdcanciones.com (2017)",
    "E-Chords — e-chords.com/chords/los-ratones-paranoicos/isabel",
]:
    pdf.cell(0, 5, "  • " + src, new_x="LMARGIN", new_y="NEXT")

pdf.output("/home/user/feli/isabel_analisis_armonico.pdf")
print("OK")
