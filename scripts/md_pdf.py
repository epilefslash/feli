# -*- coding: utf-8 -*-
"""Renderer markdown -> flowables de ReportLab, reusable por cualquier build_*.py del repo.

Sale de `build_venta_pdf.py`, que fue el primero en necesitarlo. Se extrajo acá para que los
documentos nuevos (planes, briefings, guiones que no llevan partitura) no tengan que volver a
copiar 150 lineas de parser. `build_venta_pdf.py` sigue con su copia propia a proposito: es un
entregable que ya funciona y no vale la pena tocarlo por una refactorizacion cosmetica.

Soporta: headers h1-h4, **negrita**, *cursiva*, `codigo`, listas, tablas con header, blockquotes
(y la linea ">" sola como salto de parrafo adentro de una cita, que es como se marcan las pausas
de los guiones hablados). Los emoji se sacan: la fuente del documento no los tiene y salen como
cuadraditos.

Uso:
    from md_pdf import render_markdown, MOBILE_H1, MOBILE_BODY
    render_markdown(open('doc.md').read(), story, doc.width)
"""
import re

from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle

from cuadernillo_comun import H1, H2, H3, BODY, RED, DARK, LIGHT, BORDER

# Cuerpo un poco mas grande y con mas leading que el BODY del cuadernillo: estos documentos se
# leen en el celular, no impresos.
MOBILE_BODY = ParagraphStyle('MD_BODY', parent=BODY, fontSize=10.5, leading=15)
MOBILE_QUOTE = ParagraphStyle('MD_QUOTE', parent=MOBILE_BODY, leftIndent=12,
                              textColor=DARK, borderColor=BORDER, borderWidth=0,
                              backColor=LIGHT, spaceBefore=2, spaceAfter=2,
                              borderPadding=6)
MOBILE_H1 = ParagraphStyle('MD_H1', parent=H1, fontSize=16, leading=20, spaceBefore=4, spaceAfter=8)
MOBILE_H2 = ParagraphStyle('MD_H2', parent=H2, fontSize=13, leading=16.5, spaceBefore=10, spaceAfter=6)
MOBILE_H3 = ParagraphStyle('MD_H3', parent=H3, fontSize=11.5, leading=14.5, spaceBefore=8, spaceAfter=4)
BULLET = ParagraphStyle('MD_BULLET', parent=MOBILE_BODY, leftIndent=10)
CODE_BLOCK = ParagraphStyle('MD_CODE', parent=MOBILE_BODY, fontName='Courier-Bold', fontSize=10,
                            leading=14, textColor=DARK, backColor=LIGHT, borderColor=BORDER,
                            borderWidth=0.5, borderPadding=8, leftIndent=2)
TABLE_CELL = ParagraphStyle('MD_CELL', parent=MOBILE_BODY, fontSize=9, leading=12)
TABLE_HEAD_CELL = ParagraphStyle('MD_HEAD', parent=TABLE_CELL, fontName='Helvetica-Bold', textColor=RED)

EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF️]+"
)


def inline(txt):
    """**negrita**, *cursiva* y `codigo` de markdown a tags de reportlab. Escapa lo basico."""
    txt = EMOJI_RE.sub('', txt).strip()
    txt = txt.replace('&', '&amp;')
    txt = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', txt)
    txt = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<i>\1</i>', txt)
    txt = re.sub(r'`([^`]+?)`', r'<font face="Helvetica-Bold" color="#8a3a1f">\1</font>', txt)
    return txt


def merge_continuations(raw_lines):
    """Une lineas fisicas que continuan el mismo parrafo o item de lista.

    El markdown del repo viene con wrap manual a ~100 caracteres. Sin esto, cada linea fisica
    se renderiza como un Paragraph aparte y el espaciado queda roto.
    """
    def is_locked(s):
        # Un heading, un separador, una fila de tabla o una cita nunca reciben la linea de
        # abajo como continuacion, tengan o no una linea en blanco que los separe del texto
        # que sigue -- si no, "## Titulo\nprosa sin blanco" se fusiona en el titulo entero.
        if re.match(r'^#{1,4}\s', s) or s.startswith('>'):
            return True
        if s.startswith('|') and s.endswith('|'):
            return True
        if s in ('---', '***', '___'):
            return True
        return False

    def is_block_start(s):
        if not s:
            return True
        if is_locked(s):
            return True
        if re.match(r'^[-*]\s', s) or re.match(r'^\d+\.\s', s):
            return True
        return False

    merged = []
    locked = []  # paralelo a merged: True si esa linea no debe recibir continuaciones
    in_fence = False
    for raw in raw_lines:
        s = raw.strip()
        if s.startswith('```'):
            # Los fences de codigo nunca se unen con nada, ni entre si ni con lo de afuera:
            # cada linea de adentro tiene que sobrevivir intacta (es texto para copiar y pegar).
            in_fence = not in_fence
            merged.append(s)
            locked.append(True)
            continue
        if in_fence:
            merged.append(s)
            locked.append(True)
            continue
        if not s:
            merged.append('')
            locked.append(True)
            continue
        prev_locked = locked[-1] if locked else True
        if not merged or merged[-1] == '' or prev_locked or is_block_start(s):
            merged.append(s)
            locked.append(is_locked(s))
        else:
            merged[-1] = merged[-1] + ' ' + s
    return merged


def _col_widths(raw_cells, ncols, width):
    """Reparte el ancho segun cuanto texto tiene cada columna, en vez de partir en partes iguales.

    Con columnas iguales, una columna "#" de un digito se come el mismo ancho que una de prosa y
    la tabla queda con la prosa toda partida. Se mide el texto mas largo de cada columna y se
    reparte proporcional, con un piso del 6% para que ninguna quede impracticable.
    """
    largos = []
    for c in range(ncols):
        largo = max((len(row[c]) for row in raw_cells if c < len(row)), default=1)
        largos.append(max(largo, 1))
    total = float(sum(largos))
    crudos = [width * (l / total) for l in largos]
    # 6% alcanzaba para una columna de un digito pero no para una palabra corta ("Bloquea",
    # "Espera"): a ese ancho el texto se corta en dos lineas apretadas. 10% da lugar a ~7-8
    # caracteres sin partir, y con hasta 8 columnas en una fila todavia no se come el 100%.
    piso = width * 0.10
    # Lo que haga falta para levantar las columnas flacas al piso se le saca a las que sobran.
    faltante = sum(piso - w for w in crudos if w < piso)
    sobrante = sum(w - piso for w in crudos if w > piso)
    if sobrante <= 0:
        return [width / ncols] * ncols
    ajuste = min(faltante / sobrante, 1.0)
    return [piso if w < piso else w - (w - piso) * ajuste for w in crudos]


def render_markdown(md_text, story, width):
    lines = merge_continuations(md_text.split('\n'))
    i = 0
    quote_buf = []

    def flush_quote():
        if quote_buf:
            # quote_buf puede traer '' como marcador de salto de parrafo (linea ">" sola), que es
            # como se separan las pausas adentro de un mismo bloque hablado.
            paragraphs, current = [], []
            for item in quote_buf:
                if item == '':
                    if current:
                        paragraphs.append(' '.join(current))
                        current = []
                else:
                    current.append(item)
            if current:
                paragraphs.append(' '.join(current))
            story.append(Paragraph(inline('<br/><br/>'.join(paragraphs)), MOBILE_QUOTE))
            story.append(Spacer(1, 4))
            quote_buf.clear()

    def is_table_row(s):
        return s.startswith('|') and s.endswith('|') and s.count('|') >= 2

    def is_separator_row(s):
        cells = [c.strip() for c in s.strip('|').split('|')]
        return all(re.match(r'^:?-{2,}:?$', c) for c in cells)

    def parse_table(start):
        rows, raw_cells = [], []
        j = start
        while j < len(lines) and is_table_row(lines[j].strip()):
            j += 1
        raw_rows = [lines[k].strip() for k in range(start, j)]
        for r_idx, raw in enumerate(raw_rows):
            if r_idx == 1 and is_separator_row(raw):
                continue
            cells = [c.strip() for c in raw.strip('|').split('|')]
            style = TABLE_HEAD_CELL if r_idx == 0 else TABLE_CELL
            rows.append([Paragraph(inline(c), style) for c in cells])
            raw_cells.append(cells)
        return rows, raw_cells, j

    def render_code_block(start):
        """Lineas entre ```: se muestran tal cual, sin negrita/cursiva/emoji, para copiar y pegar."""
        j = start + 1
        code_lines = []
        while j < len(lines) and not lines[j].strip().startswith('```'):
            code_lines.append(lines[j].rstrip())
            j += 1
        text = '<br/>'.join(l.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;') or '&nbsp;'
                             for l in code_lines)
        story.append(Paragraph(text, CODE_BLOCK))
        story.append(Spacer(1, 6))
        return j + 1  # salta el ``` de cierre

    while i < len(lines):
        stripped = lines[i].rstrip().strip()

        if stripped.startswith('```'):
            flush_quote()
            i = render_code_block(i)
            continue

        if not stripped:
            flush_quote()
            i += 1
            continue

        if is_table_row(stripped):
            flush_quote()
            rows, raw_cells, next_i = parse_table(i)
            if rows:
                ncols = max(len(r) for r in rows)
                # Las filas de seccion (una sola celda con contenido y el resto vacias) se dejan
                # como estan: reportlab exige que todas las filas tengan la misma cantidad de celdas.
                for r in rows:
                    while len(r) < ncols:
                        r.append(Paragraph('', TABLE_CELL))
                t = Table(rows, colWidths=_col_widths(raw_cells, ncols, width), repeatRows=1)
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), LIGHT),
                    ('GRID', (0, 0), (-1, -1), 0.5, BORDER),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ('LEFTPADDING', (0, 0), (-1, -1), 5),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 5),
                    ('TOPPADDING', (0, 0), (-1, -1), 4),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                ]))
                story.append(t)
                story.append(Spacer(1, 6))
            i = next_i
            continue

        if stripped == '>':
            quote_buf.append('')
            i += 1
            continue

        if stripped.startswith('> '):
            quote_buf.append(stripped[2:])
            i += 1
            continue
        flush_quote()

        if stripped.startswith('# '):
            story.append(Paragraph(inline(stripped[2:]), MOBILE_H1))
        elif stripped.startswith('## '):
            story.append(Paragraph(inline(stripped[3:]), MOBILE_H2))
        elif stripped.startswith('### '):
            story.append(Paragraph(inline(stripped[4:]), MOBILE_H3))
        elif stripped.startswith('#### '):
            story.append(Paragraph(inline(stripped[5:]), MOBILE_H3))
        elif stripped in ('---', '***', '___'):
            story.append(Spacer(1, 6))
        elif re.match(r'^[-*] ', stripped):
            story.append(Paragraph('&#8226;&nbsp;&nbsp;' + inline(stripped[2:]), BULLET))
        elif re.match(r'^\d+\.\s', stripped):
            story.append(Paragraph(inline(stripped), BULLET))
        else:
            story.append(Paragraph(inline(stripped), MOBILE_BODY))
            story.append(Spacer(1, 3))
        i += 1

    flush_quote()
