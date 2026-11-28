"""Genera logos y portadas de destacadas, y arma manual-de-marca.html con los SVG embebidos.

Uso: python3 armar_manual.py <carpeta_fuentes>
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import generar_logos as g  # noqa: E402

C = g.COL
LOGOS = os.path.join(ROOT, "logos")
HL = os.path.join(LOGOS, "destacadas")
os.makedirs(HL, exist_ok=True)
g.main(LOGOS)

generated = {}

# ---------- Portadas de destacadas: inicial en itálica sobre crema (texto en curvas) ----------
for key, glyph in (("servicios", "s"), ("casos", "c"), ("proceso", "p"), ("tips", "t"), ("contacto", "@")):
    font = g.SERIF if glyph != "@" else g.BOLD
    size = 64 if glyph != "@" else 40
    x0, y0, x1, y1 = g.ink_bounds(font, glyph, size)
    d, _ = g.text_path(font, glyph, size, 50 - (x0 + x1) / 2, 50 - (y0 + y1) / 2)
    s = g.svg(100, 100, f'<rect width="100" height="100" fill="{C["crema"]}"/><path d="{d}" fill="{C["cafe"]}"/>')
    open(os.path.join(HL, f"destacada-{key}.svg"), "w").write(s)
    generated[f"hl-{key}"] = s

# ---------- Plantillas (maquetas con las fuentes web del manual) ----------
SERIF = 'font-family="Instrument Serif, Georgia, serif" font-style="italic"'
SANS = 'font-family="Inter Tight, Arial, sans-serif"'
LBL = 'font-family="Inter Tight, Arial, sans-serif" font-weight="600" letter-spacing="4"'

def mini_wordmark(fg, x, y, width):
    x0, y0, x1, y1 = g.wordmark_bounds()
    k = width / (x1 - x0)
    body, _ = g.wordmark_paths(fg, x - x0 * k, y, k)
    return body

generated["post-portada"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1350" preserveAspectRatio="xMidYMid slice">
<rect width="1080" height="1350" fill="{C['crema']}"/>
<text x="110" y="200" {LBL} font-size="26" fill="{C['taupe']}">PARA TU MARCA</text>
<g {SERIF} font-size="132" fill="{C['cafe']}"><text x="104" y="560">3 errores que</text><text x="104" y="690">hacen que tu reel</text><text x="104" y="820">no retenga</text></g>
<line x1="110" y1="1150" x2="970" y2="1150" stroke="{C['arena']}" stroke-width="2"/>
{mini_wordmark(C['cafe'], 110, 1240, 260)}
<text x="970" y="1234" text-anchor="end" {LBL} font-size="24" fill="{C['taupe']}">DESLIZÁ →</text>
</svg>'''

generated["post-tip"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1350" preserveAspectRatio="xMidYMid slice">
<rect width="1080" height="1350" fill="{C['lino']}"/>
<text x="100" y="390" {SANS} font-weight="800" letter-spacing="-12" font-size="300" fill="{C['arena']}">03</text>
<g {SERIF} font-size="96" fill="{C['cafe']}"><text x="110" y="580">Grabá el final</text><text x="110" y="680">primero.</text></g>
<g {SANS} font-size="40" fill="{C['cacao']}"><text x="110" y="820">Si sabés cómo termina el video,</text><text x="110" y="880">sabés qué tiene que prometer</text><text x="110" y="940">el segundo uno.</text></g>
{mini_wordmark(C['taupe'], 110, 1240, 200)}
<text x="970" y="1234" text-anchor="end" {LBL} font-size="24" fill="{C['taupe']}">GUARDALO</text>
</svg>'''

generated["post-caso"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1350" preserveAspectRatio="xMidYMid slice">
<defs><linearGradient id="ph" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#A8927C"/><stop offset="1" stop-color="#6B5442"/></linearGradient></defs>
<rect width="1080" height="1350" fill="{C['cafe']}"/>
<rect x="90" y="90" width="900" height="820" rx="6" fill="url(#ph)"/>
<text x="540" y="510" text-anchor="middle" {LBL} font-size="24" fill="{C['crema']}">FOTO DEL CLIENTE</text>
<text x="110" y="1020" {LBL} font-size="26" fill="{C['arena']}">CASO · VILLAGE POLO CLUB</text>
<g {SERIF} font-size="84" fill="{C['crema']}"><text x="106" y="1130">Del feed improvisado</text><text x="106" y="1220">a una grilla con dirección.</text></g>
</svg>'''

generated["post-foto"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1440" preserveAspectRatio="xMidYMid slice">
<defs><linearGradient id="pf" x1="0" y1="0" x2="0.3" y2="1"><stop offset="0" stop-color="#CDBFAE"/><stop offset="1" stop-color="#7D6655"/></linearGradient></defs>
<rect width="1080" height="1440" fill="url(#pf)"/>
<g {SERIF} font-size="120" fill="{C['lino']}" text-anchor="middle"><text x="540" y="1200">Detrás de</text><text x="540" y="1320">cámara</text></g>
</svg>'''

generated["reel-portada"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1920">
<rect width="1080" height="1920" fill="{C['arena']}"/>
<rect x="0" y="420" width="1080" height="1080" fill="none" stroke="{C['taupe']}" stroke-width="3" stroke-dasharray="14 14"/>
<text x="540" y="390" text-anchor="middle" {LBL} font-size="24" fill="{C['cacao']}">ZONA VISIBLE EN LA GRILLA</text>
<g {SERIF} font-size="124" fill="{C['cafe']}" text-anchor="middle"><text x="540" y="930">Cuánto cobrar</text><text x="540" y="1060">por un UGC</text></g>
</svg>'''

# ---------- Armado del HTML ----------
def load(name):
    return generated[name] if name in generated else open(os.path.join(LOGOS, name + ".svg")).read()

def strip_size(s):
    head, rest = s.split(">", 1)
    head = re.sub(r'\s(width|height)="[^"]*"', "", head)
    return (head + ">" + rest).strip()

src = open(os.path.join(ROOT, "manual", "manual.src.html")).read()
html = re.sub(r"<!--svg:([\w-]+)-->", lambda m: strip_size(load(m.group(1))), src)
out = os.path.join(ROOT, "manual-de-marca.html")
open(out, "w").write(html)
print("manual:", out, f"{len(html)/1024:.0f} KB")
