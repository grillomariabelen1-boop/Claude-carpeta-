#!/bin/sh
# Genera la guia en A5 lista para anillar, a partir de guia.html
# Requiere: chromium (print-to-pdf) y python3 con pymupdf.
set -e
CHROME="${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}"
cd "$(dirname "$0")"

"$CHROME" --headless --disable-gpu --no-sandbox \
  --print-to-pdf=bruto.pdf --no-pdf-header-footer guia.html

python3 - <<'PY'
import pymupdf as fitz
MM = 72 / 25.4
d = fitz.open("bruto.pdf")

# total par, para imprimir a doble faz
if d.page_count % 2:
    d.new_page(width=148 * MM, height=210 * MM)

for i in range(d.page_count):
    p = d[i]
    if i == 0 or not p.get_text().strip():      # portada y hojas de guarda van sin folio
        continue
    n = i + 1
    txt = str(n)
    w = fitz.get_text_length(txt, fontname="times-roman", fontsize=8.5)
    # el folio va siempre en el margen exterior
    x = p.rect.width - 12 * MM - w if n % 2 else 12 * MM
    p.insert_text((x, p.rect.height - 11 * MM), txt,
                  fontname="times-roman", fontsize=8.5, color=(.35, .35, .35))

d.save("Cialdini-GUIA-A5.pdf", garbage=4, deflate=True)
print(f"Cialdini-GUIA-A5.pdf: {d.page_count} paginas")
PY
rm -f bruto.pdf
