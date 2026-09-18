"""Genera la secuencia de superposiciones (PNG con transparencia) del demo."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS, DUR = 1080, 1920, 30, 8.0
N = int(FPS * DUR)
FD = "fonts/"


def F(n, s, w=None):
    f = ImageFont.truetype(FD + n, s)
    if w:
        try:
            f.set_variation_by_axes([w])
        except Exception:
            pass
    return f


fo = {
    "titulo": F("Anton.ttf", 104),
    "swatch": F("InstrumentSerif.ttf", 66),
    "lower": F("PlayfairDisplay.ttf", 60, 600),
    "sub": F("Inter.ttf", 52, 700),
    "cierre": F("BebasNeue.ttf", 92),
}


def ease(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def win(t, a, b, fin=0.35, fout=0.3):
    if t < a or t > b:
        return 0.0, 0.0
    ein = ease((t - a) / fin) if t < a + fin else 1.0
    eout = 1.0 if t < b - fout else 1 - ease((t - (b - fout)) / fout)
    return ein, eout


def texto(d, img, xy, s, font, alpha=255, sombra=True, anchor="la"):
    if alpha <= 2:
        return
    if sombra:
        capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(capa).text(
            (xy[0], xy[1] + 4), s, font=font, fill=(0, 0, 0, int(120 * alpha / 255)), anchor=anchor
        )
        img.alpha_composite(capa.filter(ImageFilter.GaussianBlur(10)))
    d.text(xy, s, font=font, fill=(255, 255, 255, alpha), anchor=anchor)


for i in range(N):
    t = i / FPS
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # 1) TITULO — franja negra semitransparente + Anton
    ein, eout = win(t, 0.5, 3.4)
    a = ein * eout
    if a > 0:
        dy = int(50 * (1 - ein))
        banda = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(banda).rectangle([0, 286 + dy, W, 596 + dy], fill=(0, 0, 0, int(115 * a)))
        img.alpha_composite(banda)
        texto(d, img, (60, 318 + dy), "POR QUÉ TU ROPA", fo["titulo"], int(255 * a), False)
        texto(d, img, (60, 440 + dy), "SE VE DE OTRO COLOR", fo["titulo"], int(255 * a), False)
        d = ImageDraw.Draw(img)

    # 2) CHIP DE COLOR
    ein, eout = win(t, 2.2, 6.2)
    a = ein * eout
    if a > 0:
        x = int(60 - 260 * (1 - ein))
        chip = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        dc = ImageDraw.Draw(chip)
        dc.rounded_rectangle([x, 900, x + 560, 1030], radius=65, fill=(0, 0, 0, int(140 * a)))
        dc.ellipse(
            [x + 22, 922, x + 108, 1008],
            fill=(107, 122, 79, int(255 * a)),
            outline=(255, 255, 255, int(210 * a)),
            width=4,
        )
        img.alpha_composite(chip)
        d = ImageDraw.Draw(img)
        texto(d, img, (x + 136, 928), "verde oliva", fo["swatch"], int(255 * a), False)

    # 3) ZOCALO editorial
    ein, eout = win(t, 3.8, 6.2)
    a = ein * eout
    if a > 0:
        texto(d, img, (60, 1100 + int(24 * (1 - ein))), "lo que ve la cámara", fo["lower"], int(235 * a))

    # 4) SUBTITULO
    ein, eout = win(t, 4.6, 7.2, 0.15, 0.2)
    a = ein * eout
    if a > 0:
        texto(d, img, (W // 2, 1560), "no es el color, es el balance de blancos", fo["sub"], int(255 * a), True, "ma")

    # 5) CIERRE
    ein, eout = win(t, 6.6, 8.0, 0.3, 0.25)
    a = ein * eout
    if a > 0:
        texto(d, img, (W // 2, 760), "TE MUESTRO CÓMO", fo["cierre"], int(255 * a), True, "ma")
        texto(d, img, (W // 2, 860), "SE ARREGLA", fo["cierre"], int(255 * a), True, "ma")

    img.save(f"seq/f{i:04d}.png")

print("frames:", N)
