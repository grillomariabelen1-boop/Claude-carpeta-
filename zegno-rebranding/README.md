# Zegno Studio — Identidad v2 (pulido del logo original)

Manual de marca publicado: https://claude.ai/artifact/VH2F9pCNX59dg7RqKd6oJM
(copia local: `manual-de-marca.html`).

## Qué hay acá

| Carpeta / archivo | Contenido |
|---|---|
| `logos/` | Sello, logotipo y monograma "zs" en SVG, con el texto pasado a curvas, en variantes crema, café y arena. |
| `logos/zegno-avatar-instagram.svg` | Foto de perfil de 1080 × 1080. |
| `logos/destacadas/` | Las cinco portadas de destacadas: servicios, casos, proceso, tips y contacto. |
| `manual/manual.src.html` | Fuente del manual (los SVG se insertan al armarlo). |
| `tools/` | Scripts que generan los logos y arman el manual. |

## Sistema en una línea

Logo original pulido: "zegno" en Instrument Serif Italic + "studio" en Inter Tight ExtraBold, sobre el círculo crema.
Colores: Lino `#F4EFE8`, Crema `#E8DFD3`, Arena `#CDBFAE`, Taupe `#9A8775`, Cacao `#5C4636`, Café `#3B2A20`.

## Regenerar

```bash
pip install fonttools brotli
# instrument-it.ttf, intertight-800.ttf e intertight-600.ttf (Google Fonts) en una carpeta
python3 tools/armar_manual.py <carpeta_fuentes>
```
