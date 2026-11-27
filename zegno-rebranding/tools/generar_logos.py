"""Genera los SVG del rebranding de Zegno Studio con el texto convertido a curvas.

Uso: python3 generar_logos.py <carpeta_fuentes> <carpeta_salida>
La carpeta de fuentes tiene que tener fraunces-it.ttf (Fraunces Italic 600, SOFT 100)
y dmmono.ttf (DM Mono 500), descargadas de Google Fonts.
"""
import sys, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONTS = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "fonts")

COL = {
    "espresso": "#2A1D17",
    "hueso": "#EFE8DD",
    "tungsteno": "#D4892F",
    "rec": "#E0442C",
}

def text_path(fontfile, text, size, x=0, y=0, tracking=0.0):
    """Devuelve (d, ancho) del texto como path SVG. y = línea de base."""
    f = TTFont(fontfile)
    gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f["head"].unitsPerEm
    s = size / upm
    hmtx = f["hmtx"]
    ds = []; cx = 0.0
    for ch in text:
        g = cmap[ord(ch)]
        pen = SVGPathPen(gs)
        tp = TransformPen(pen, (s, 0, 0, -s, x + cx, y))
        gs[g].draw(tp)
        ds.append(pen.getCommands())
        cx += hmtx[g][0] * s + tracking * size
    return " ".join(ds), cx - tracking * size

def isotipo(fg, rec, x=0, y=0, size=100):
    """Z de encuadre: esquina sup-izq + diagonal + esquina inf-der, con punto REC."""
    k = size / 100
    sw = 11 * k
    def P(a, b): return f"{x + a*k:.2f} {y + b*k:.2f}"
    return (f'<path d="M{P(16,40)} V{y+16*k:.2f} H{x+84*k:.2f} L{P(16,84)} H{x+84*k:.2f} V{y+60*k:.2f}" '
            f'fill="none" stroke="{fg}" stroke-width="{sw:.2f}" stroke-linejoin="miter" stroke-miterlimit="10" stroke-linecap="butt"/>'
            f'<circle cx="{x+79*k:.2f}" cy="{y+44*k:.2f}" r="{6.5*k:.2f}" fill="{rec}"/>')

FR = os.path.join(FONTS, "fraunces-it.ttf")
MO = os.path.join(FONTS, "dmmono.ttf")

def svg(w, h, body, bg=None):
    bgr = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}">{bgr}{body}</svg>\n'

def horizontal(fg, rec, accent):
    # isotipo 120 alto, wordmark a la derecha
    iso = isotipo(fg, rec, 0, 0, 120)
    d, wz = text_path(FR, "zegno", 112, 150, 92)
    dm, wm = text_path(MO, "STUDIO", 17, 150 + wz + 12, 49, tracking=0.28)
    w = 150 + wz + 12 + wm + 4
    body = iso + f'<path d="{d}" fill="{fg}"/>' + f'<path d="{dm}" fill="{accent}"/>'
    return w, 126, body

def vertical(fg, rec, accent):
    d, wz = text_path(FR, "zegno", 112, 0, 0)
    W = wz + 4
    iso = isotipo(fg, rec, (W - 120) / 2, 0, 120)
    d, wz = text_path(FR, "zegno", 112, 0, 226)
    dm, wm = text_path(MO, "STUDIO", 20, 0, 0, tracking=0.9)
    dm, wm = text_path(MO, "STUDIO", 20, (W - wm) / 2, 280, tracking=0.9)
    body = iso + f'<path d="{d}" fill="{fg}"/>' + f'<path d="{dm}" fill="{accent}"/>'
    return W, 286, body

def wordmark(fg, accent):
    d, wz = text_path(FR, "zegno", 112, 0, 92)
    dm, wm = text_path(MO, "STUDIO", 17, wz + 12, 49, tracking=0.28)
    return wz + 12 + wm + 4, 126, f'<path d="{d}" fill="{fg}"/><path d="{dm}" fill="{accent}"/>'

def avatar(bg, fg, rec):
    # 1080x1080, isotipo centrado con aire para el recorte circular
    return 1080, 1080, f'<rect width="1080" height="1080" fill="{bg}"/>' + isotipo(fg, rec, 330, 330, 420)

def main(OUT):
  os.makedirs(OUT, exist_ok=True)
  variants = {
      "positivo": (COL["espresso"], COL["rec"], COL["tungsteno"], None),
      "negativo": (COL["hueso"], COL["rec"], COL["tungsteno"], COL["espresso"]),
      "mono-espresso": (COL["espresso"], COL["espresso"], COL["espresso"], None),
      "mono-hueso": (COL["hueso"], COL["hueso"], COL["hueso"], None),
  }
  pad = 24
  for name, (fg, rec, acc, bg) in variants.items():
      for kind, fn in (("horizontal", horizontal), ("vertical", vertical)):
          w, h, body = fn(fg, rec, acc)
          W, H = w + 2 * pad, h + 2 * pad
          open(f"{OUT}/zegno-{kind}-{name}.svg", "w").write(
              svg(W, H, f'<g transform="translate({pad} {pad})">{body}</g>', bg))
      w, h, body = wordmark(fg, acc)
      open(f"{OUT}/zegno-wordmark-{name}.svg", "w").write(
          svg(w + 2*pad, h + 2*pad, f'<g transform="translate({pad} {pad})">{body}</g>', bg))
      open(f"{OUT}/zegno-isotipo-{name}.svg", "w").write(svg(100, 100, isotipo(fg, rec), bg))

  open(f"{OUT}/zegno-avatar-instagram.svg", "w").write(svg(*avatar(COL["espresso"], COL["hueso"], COL["rec"])))
  open(f"{OUT}/zegno-avatar-instagram-claro.svg", "w").write(svg(*avatar(COL["hueso"], COL["espresso"], COL["rec"])))
  print("ok", len(os.listdir(OUT)))

if __name__ == "__main__":
    main(sys.argv[2])
