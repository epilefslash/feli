# -*- coding: utf-8 -*-
"""Arma el PDF del sistema de venta (síntesis + 4 documentos) para leer cómodo desde el celu.

Convierte el markdown de entregables/venta/*.md a PDF con el mismo estilo visual que el
resto de los documentos del proyecto (cuadernillo_comun). Parser de markdown liviano:
headers, negrita, listas, blockquotes, y comillas de guion (líneas que arrancan con >).
"""
import os
import re
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, PageBreak, ListFlowable, ListItem, Table, TableStyle

from cuadernillo_comun import (H1, H2, H3, BODY, SMALL, RED, DARK, GREY,
                               LIGHT, BORDER, IG, documento, caja_oscura)

doc = documento("Sistema-de-Venta-Completo.pdf",
                "SISTEMA DE VENTA",
                "Objeciones · Cierre · DM · Precio — para leer en el celu",
                "Solo con Sabor · Sistema de venta",
                "Sistema de venta - Metodo Flow")
W = doc.width
S = []

# Estilos extra, pensados para lectura en pantalla chica: más leading, cuerpo un poco más grande.
MOBILE_BODY = ParagraphStyle('MOBILE_BODY', parent=BODY, fontSize=10.5, leading=15)
MOBILE_QUOTE = ParagraphStyle('MOBILE_QUOTE', parent=MOBILE_BODY, leftIndent=12,
                               textColor=DARK, borderColor=BORDER, borderWidth=0,
                               backColor=LIGHT, spaceBefore=2, spaceAfter=2,
                               borderPadding=6)
MOBILE_H1 = ParagraphStyle('MOBILE_H1', parent=H1, fontSize=16, leading=20, spaceBefore=4, spaceAfter=8)
TABLE_CELL = ParagraphStyle('TABLE_CELL', parent=MOBILE_BODY, fontSize=9, leading=12)
TABLE_HEAD_CELL = ParagraphStyle('TABLE_HEAD_CELL', parent=TABLE_CELL, fontName='Helvetica-Bold', textColor=RED)
MOBILE_H2 = ParagraphStyle('MOBILE_H2', parent=H2, fontSize=13, leading=16.5, spaceBefore=10, spaceAfter=6)
MOBILE_H3 = ParagraphStyle('MOBILE_H3', parent=H3, fontSize=11.5, leading=14.5, spaceBefore=8, spaceAfter=4)
BULLET = ParagraphStyle('BULLET', parent=MOBILE_BODY, leftIndent=10)


EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF️]+"
)


def inline(txt):
    """Convierte **negrita** y *cursiva* de markdown a tags de reportlab, y escapa lo básico."""
    txt = EMOJI_RE.sub('', txt).strip()
    txt = txt.replace('&', '&amp;')
    txt = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', txt)
    txt = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<i>\1</i>', txt)
    txt = re.sub(r'`([^`]+?)`', r'<font face="Helvetica-Bold" color="#8a3a1f">\1</font>', txt)
    return txt


def render_markdown(md_text, story):
    lines = md_text.split('\n')
    i = 0
    quote_buf = []

    def flush_quote():
        if quote_buf:
            joined = ' '.join(quote_buf)
            story.append(Paragraph(inline(joined), MOBILE_QUOTE))
            story.append(Spacer(1, 4))
            quote_buf.clear()

    def is_table_row(s):
        return s.startswith('|') and s.endswith('|') and s.count('|') >= 2

    def is_separator_row(s):
        cells = [c.strip() for c in s.strip('|').split('|')]
        return all(re.match(r'^:?-{2,}:?$', c) for c in cells)

    def parse_table(start):
        rows = []
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
        return rows, j

    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        if not stripped:
            flush_quote()
            i += 1
            continue

        if is_table_row(stripped):
            flush_quote()
            rows, next_i = parse_table(i)
            if rows:
                ncols = max(len(r) for r in rows)
                colw = W / ncols
                t = Table(rows, colWidths=[colw] * ncols, repeatRows=1)
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

        if stripped.startswith('> '):
            quote_buf.append(stripped[2:])
            i += 1
            continue
        else:
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
            story.append(Paragraph('•&nbsp;&nbsp;' + inline(stripped[2:]), BULLET))
        elif re.match(r'^\d+\.\s', stripped):
            story.append(Paragraph(inline(stripped), BULLET))
        else:
            story.append(Paragraph(inline(stripped), MOBILE_BODY))
            story.append(Spacer(1, 3))
        i += 1

    flush_quote()


BASE = "entregables/venta"
DOCS = [
    ("00-SINTESIS.md", "SÍNTESIS", "Lo que más importa, de las 5 piezas juntas"),
    ("04-precio-garantia.md", "PRECIO, GARANTÍA Y FECHA", None),
    ("01-objeciones.md", "MANEJO DE OBJECIONES", None),
    ("02-cierre.md", "EL MOMENTO DEL CIERRE", None),
    ("03-dm.md", "LA PLANTILLA DE DM", None),
]

# ============================================================ PORTADA
S.append(Paragraph("SISTEMA DE VENTA — SOLO CON SABOR", MOBILE_H1))
S.append(Paragraph(
    "Los 4 documentos de venta que faltaban (objeciones, cierre, DM, precio) más la síntesis "
    "que los cruza. Armado para revisar con Nico en el mes 3 de la mentoría (\"Conversión y "
    "Delivery\") — es un borrador para practicar, no para usar en piloto automático: Feli nunca "
    "vendió high-ticket por voz.", MOBILE_BODY))
S.append(Spacer(1, 8))
S.append(caja_oscura(
    '<font color="white" size="10"><b>Cómo leer esto</b></font><br/>'
    '<font color="#f7d7d2" size="9">Arranca con la SÍNTESIS (las 5 cosas que más importan). '
    'Después PRECIO/GARANTÍA/FECHA, porque esas 3 decisiones habilitan todo lo demás. '
    'Los guiones de diálogo van en recuadro — son para decir tal cual, no para parafrasear.</font>', W))
S.append(PageBreak())

for idx, (fname, title, subtitle) in enumerate(DOCS):
    path = os.path.join(BASE, fname)
    with open(path, encoding='utf-8') as f:
        content = f.read()
    S.append(Paragraph(title, MOBILE_H1))
    if subtitle:
        S.append(Paragraph(subtitle, SMALL))
        S.append(Spacer(1, 6))
    render_markdown(content, S)
    if idx < len(DOCS) - 1:
        S.append(PageBreak())

doc.build(S)
print("OK Sistema-de-Venta-Completo.pdf")
