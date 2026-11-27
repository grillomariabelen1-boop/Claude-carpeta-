"""Genera las portadas de destacadas y arma manual-de-marca.html con los SVG embebidos.

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

def brackets(x0, y0, x1, y1, L, sw, color):
    return (f'<path d="M{x0} {y0+L} V{y0} H{x0+L} M{x1} {y1-L} V{y1} H{x1-L}" fill="none" '
            f'stroke="{color}" stroke-width="{sw}"/>')

# ---------- Portadas de destacadas (texto en curvas) ----------
generated = {}
for key, glyph in (("servicios", "s"), ("casos", "c"), ("proceso", "p"), ("tips", "t"), ("contacto", "@")):
    font = g.FR if glyph != "@" else g.MO
    size = 46 if glyph != "@" else 40
    d, w = g.text_path(font, glyph, size, 0, 0)
    d, w = g.text_path(font, glyph, size, 50 - w / 2 - (1.5 if glyph != "@" else 0), 63 if glyph not in "pt" else 60)
    body = (f'<rect width="100" height="100" fill="{C["espresso"]}"/>'
            + brackets(24, 24, 76, 76, 12, 3.2, C["tungsteno"])
            + f'<path d="{d}" fill="{C["hueso"]}"/>')
    s = g.svg(100, 100, body)
    open(os.path.join(HL, f"destacada-{key}.svg"), "w").write(s)
    generated[f"hl-{key}"] = s

# ---------- Plantillas de posteo (maqueta, usa las fuentes web del manual) ----------
FD = "font-family=\"Fraunces, Georgia, serif\" font-style=\"italic\" font-weight=\"600\""
FS = "font-family=\"DM Sans, Arial, sans-serif\""
FM = "font-family=\"DM Mono, monospace\" font-weight=\"500\" letter-spacing=\"3\""

def iso_small(x, y, size, fg, rec):
    return g.isotipo(fg, rec, x, y, size)

generated["post-portada"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1350" preserveAspectRatio="xMidYMid slice">
<rect width="1080" height="1350" fill="{C['espresso']}"/>
{brackets(60, 60, 1020, 1290, 96, 6, C['tungsteno'])}
<circle cx="132" cy="160" r="12" fill="{C['rec']}"/>
<text x="160" y="170" {FM} font-size="30" fill="#B9AC9C">REC 00:00:01</text>
<g {FD} font-size="112" fill="{C['hueso']}">
<text x="110" y="640">3 errores</text><text x="110" y="760">que hacen que</text><text x="110" y="880">tu reel <tspan fill="{C['tungsteno']}">no retenga</tspan></text>
</g>
{iso_small(110, 1130, 90, C['hueso'], C['rec'])}
<text x="970" y="1192" text-anchor="end" {FM} font-size="30" fill="#B9AC9C">DESLIZÁ →</text>
</svg>'''

generated["post-tip"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1350" preserveAspectRatio="xMidYMid slice">
<rect width="1080" height="1350" fill="{C['hueso']}"/>
<text x="110" y="190" {FM} font-size="32" fill="{C['tungsteno']}">TIP 03/05</text>
<g {FD} font-size="96" fill="{C['espresso']}"><text x="110" y="420">Grabá el final</text><text x="110" y="530"><tspan fill="{C['tungsteno']}">primero.</tspan></text></g>
<g {FS} font-size="40" fill="#6E5E52"><text x="110" y="700">Si sabés cómo termina el video,</text><text x="110" y="760">sabés qué tiene que prometer</text><text x="110" y="820">el segundo uno.</text></g>
<line x1="110" y1="1180" x2="970" y2="1180" stroke="#D8CEC0" stroke-width="3"/>
<text x="110" y="1250" {FM} font-size="28" fill="#6E5E52">ZEGNO STUDIO</text>
<text x="970" y="1250" text-anchor="end" {FM} font-size="28" fill="#6E5E52">GUARDALO</text>
</svg>'''

generated["post-caso"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1350" preserveAspectRatio="xMidYMid slice">
<defs><linearGradient id="ph" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8A6A4F"/><stop offset="1" stop-color="#3A2A22"/></linearGradient></defs>
<rect width="1080" height="1350" fill="{C['espresso']}"/>
<rect x="110" y="150" width="860" height="700" fill="url(#ph)"/>
{brackets(80, 120, 1000, 880, 80, 6, C['tungsteno'])}
<text x="540" y="510" text-anchor="middle" {FM} font-size="28" fill="#D8CEC0">FOTO O FRAME DEL CLIENTE</text>
<text x="110" y="980" {FM} font-size="30" fill="{C['tungsteno']}">CASO · VILLAGE POLO CLUB</text>
<g {FD} font-size="80" fill="{C['hueso']}"><text x="110" y="1090">Del feed improvisado</text><text x="110" y="1185">a una grilla con dirección.</text></g>
</svg>'''

generated["post-foto"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1440" preserveAspectRatio="xMidYMid slice">
<defs><linearGradient id="pf" x1="0" y1="0" x2="0.4" y2="1"><stop offset="0" stop-color="#D4892F"/><stop offset=".55" stop-color="#7A4E2C"/><stop offset="1" stop-color="#2A1D17"/></linearGradient></defs>
<rect width="1080" height="1440" fill="url(#pf)"/>
{brackets(90, 90, 990, 1350, 110, 8, C['hueso'])}
<circle cx="170" cy="190" r="16" fill="{C['rec']}"/>
<text x="204" y="202" {FM} font-size="36" fill="{C['hueso']}">00:00:15</text>
<g {FD} font-size="104" fill="{C['hueso']}"><text x="150" y="1180">Detrás de</text><text x="150" y="1290">cámara</text></g>
</svg>'''

generated["reel-portada"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1920">
<defs><linearGradient id="rp" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3A2A22"/><stop offset="1" stop-color="#2A1D17"/></linearGradient></defs>
<rect width="1080" height="1920" fill="url(#rp)"/>
<rect x="0" y="420" width="1080" height="1080" fill="none" stroke="#5A463A" stroke-width="3" stroke-dasharray="14 14"/>
<text x="540" y="400" text-anchor="middle" {FM} font-size="26" fill="#8C7B6C">ZONA VISIBLE EN LA GRILLA</text>
{brackets(140, 640, 940, 1280, 80, 6, C['tungsteno'])}
<circle cx="200" cy="720" r="12" fill="{C['rec']}"/>
<text x="226" y="730" {FM} font-size="28" fill="#B9AC9C">REC</text>
<g {FD} font-size="104" fill="{C['hueso']}" text-anchor="middle"><text x="540" y="960">Cuánto cobrar</text><text x="540" y="1075">por un <tspan fill="{C['tungsteno']}">UGC</tspan></text></g>
</svg>'''

# ---------- Armado del HTML ----------
def load(name):
    if name in generated:
        return generated[name]
    return open(os.path.join(LOGOS, name + ".svg")).read()

def strip_size(s):
    return re.sub(r'(<svg[^>]*?)\s(width|height)="[^"]*"', r"\1", re.sub(r'(<svg[^>]*?)\s(width|height)="[^"]*"', r"\1", s), count=1)

def inner(s):
    return re.sub(r"^.*?<svg[^>]*>|</svg>\s*$", "", s.strip(), flags=re.S)

src = open(os.path.join(ROOT, "manual", "manual.src.html")).read()
html = re.sub(r"<!--svg:([\w-]+)-->", lambda m: strip_size(load(m.group(1))).strip(), src)
html = re.sub(r"<!--svg-inner:([\w-]+)-->", lambda m: inner(load(m.group(1))), html)
out = os.path.join(ROOT, "manual-de-marca.html")
open(out, "w").write(html)
print("manual:", out, f"{len(html)/1024:.0f} KB")
