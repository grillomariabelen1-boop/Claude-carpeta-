"""Genera los SVG del logo de Zegno Studio (v2, pulido del original) con el texto en curvas.

Uso: python3 generar_logos.py <carpeta_fuentes> <carpeta_salida>
Fuentes (Google Fonts, convertidas a TTF): instrument-it.ttf (Instrument Serif Italic),
intertight-800.ttf (Inter Tight ExtraBold) e intertight-600.ttf (Inter Tight SemiBold).
"""
import sys, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

FONTS = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "fonts")
SERIF = os.path.join(FONTS, "instrument-it.ttf")
BOLD = os.path.join(FONTS, "intertight-800.ttf")
SEMI = os.path.join(FONTS, "intertight-600.ttf")

COL = {
    "lino": "#F4EFE8",
    "crema": "#E8DFD3",
    "arena": "#CDBFAE",
    "taupe": "#9A8775",
    "cacao": "#5C4636",
    "cafe": "#3B2A20",
}

_cache = {}
def _font(path):
    if path not in _cache:
        _cache[path] = TTFont(path)
    return _cache[path]

def text_path(fontfile, text, size, x=0, y=0, tracking=0.0):
    """(d, ancho) del texto como path SVG; y es la línea de base; tracking en em."""
    f = _font(fontfile)
    gs = f.getGlyphSet(); cmap = f.getBestCmap(); s = size / f["head"].unitsPerEm
    ds = []; cx = 0.0
    for ch in text:
        g = cmap[ord(ch)]
        pen = SVGPathPen(gs)
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x + cx, y)))
        ds.append(pen.getCommands())
        cx += f["hmtx"][g][0] * s + tracking * size
    return " ".join(ds), cx - tracking * size

def ink_bounds(fontfile, text, size, tracking=0.0):
    """Caja real de tinta (xmin, ymin, xmax, ymax) con base en y=0, coordenadas SVG."""
    f = _font(fontfile); gs = f.getGlyphSet(); cmap = f.getBestCmap(); s = size / f["head"].unitsPerEm
    xs, ys = [], []; cx = 0.0
    for ch in text:
        g = cmap[ord(ch)]; bp = BoundsPen(gs); gs[g].draw(bp)
        if bp.bounds:
            a, b, c, d = bp.bounds
            xs += [cx + a * s, cx + c * s]; ys += [-d * s, -b * s]
        cx += f["hmtx"][g][0] * s + tracking * size
    return min(xs), min(ys), max(xs), max(ys)

# Proporciones del logotipo: "zegno" serif itálica + "studio" palo seco negrita, pegados.
Z_SIZE, S_SIZE, S_TRACK, GAP = 128, 104, -0.045, 3

def wordmark_paths(fg, x, y, scale=1.0):
    dz, wz = text_path(SERIF, "zegno", Z_SIZE * scale, x, y)
    ds, ws = text_path(BOLD, "studio", S_SIZE * scale, x + wz + GAP * scale, y, tracking=S_TRACK)
    return f'<path d="{dz}" fill="{fg}"/><path d="{ds}" fill="{fg}"/>', wz + GAP * scale + ws

def wordmark_bounds(scale=1.0):
    a = ink_bounds(SERIF, "zegno", Z_SIZE * scale)
    _, wz = text_path(SERIF, "zegno", Z_SIZE * scale)
    b = ink_bounds(BOLD, "studio", S_SIZE * scale, tracking=S_TRACK)
    off = wz + GAP * scale
    return min(a[0], b[0] + off), min(a[1], b[1]), max(a[2], b[2] + off), max(a[3], b[3])

def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}">{body}</svg>\n'

def wordmark_svg(fg, bg=None, pad=28):
    x0, y0, x1, y1 = wordmark_bounds()
    W, H = (x1 - x0) + 2 * pad, (y1 - y0) + 2 * pad
    body, _ = wordmark_paths(fg, pad - x0, pad - y0)
    rect = f'<rect width="{W:.0f}" height="{H:.0f}" fill="{bg}"/>' if bg else ""
    return svg(W, H, rect + body)

def badge_body(size, circle, fg, sub=True, fill=0.74):
    """Sello circular, como el logo original: logotipo centrado y 'SINCE 2024' legible."""
    r = size / 2
    x0, y0, x1, y1 = wordmark_bounds()
    k = size * fill / (x1 - x0)
    bx0, by0, bx1, by1 = wordmark_bounds(k)
    cx = r - (bx0 + bx1) / 2
    cy = r - (by0 + by1) / 2 - (size * 0.03 if sub else 0)
    body = f'<circle cx="{r}" cy="{r}" r="{r}" fill="{circle}"/>'
    wm, _ = wordmark_paths(fg, cx, cy, k)
    body += wm
    if sub:
        ss = size * 0.032
        _, w = text_path(SEMI, "SINCE 2024", ss, tracking=0.32)
        d, _ = text_path(SEMI, "SINCE 2024", ss, r - w / 2, cy + by1 + size * 0.085, tracking=0.32)
        body += f'<path d="{d}" fill="{fg}" fill-opacity="0.72"/>'
    return body

def monogram_body(size, circle, fg):
    """Monograma 'zs': la z itálica y la s negrita del logotipo, juntas."""
    r = size / 2
    zs, ss = size * 0.62, size * 0.5
    _, wz = text_path(SERIF, "z", zs)
    _, ws = text_path(BOLD, "s", ss)
    gap = -size * 0.01
    total = wz + gap + ws
    a = ink_bounds(SERIF, "z", zs); b = ink_bounds(BOLD, "s", ss)
    top, bot = min(a[1], b[1]), max(a[3], b[3])
    y = r - (top + bot) / 2
    x = r - total / 2
    dz, _ = text_path(SERIF, "z", zs, x, y)
    ds, _ = text_path(BOLD, "s", ss, x + wz + gap, y)
    c = f'<circle cx="{r}" cy="{r}" r="{r}" fill="{circle}"/>' if circle else ""
    return c + f'<path d="{dz}" fill="{fg}"/><path d="{ds}" fill="{fg}"/>'

def main(OUT):
    os.makedirs(OUT, exist_ok=True)
    for name, fg, bg in (("cafe", COL["cafe"], None), ("crema", COL["crema"], None),
                         ("cafe-sobre-crema", COL["cafe"], COL["crema"]), ("crema-sobre-cafe", COL["crema"], COL["cafe"])):
        open(f"{OUT}/zegno-logotipo-{name}.svg", "w").write(wordmark_svg(fg, bg))
    for name, circle, fg in (("crema", COL["crema"], COL["cafe"]), ("cafe", COL["cafe"], COL["crema"]),
                             ("arena", COL["arena"], COL["cafe"])):
        open(f"{OUT}/zegno-sello-{name}.svg", "w").write(svg(600, 600, badge_body(600, circle, fg)))
        open(f"{OUT}/zegno-monograma-{name}.svg", "w").write(svg(600, 600, monogram_body(600, circle, fg)))
    # Foto de perfil: sello sin bajada y con el logotipo más grande, para que se lea a 110 px
    open(f"{OUT}/zegno-avatar-instagram.svg", "w").write(
        svg(1080, 1080, f'<rect width="1080" height="1080" fill="{COL["crema"]}"/>' + badge_body(1080, COL["crema"], COL["cafe"], sub=False, fill=0.82)))
    print("ok", len(os.listdir(OUT)))

if __name__ == "__main__":
    main(sys.argv[2])
