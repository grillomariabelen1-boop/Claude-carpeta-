# Zegno Studio — Rebranding v1

Manual de marca publicado: https://claude.ai/artifact/VH2F9pCNX59dg7RqKd6oJM
(copia local: `manual-de-marca.html`).

## Qué hay acá

| Carpeta / archivo | Contenido |
|---|---|
| `logos/` | Logo horizontal, vertical, logotipo e isotipo en SVG, con el texto pasado a curvas. Variantes: `positivo`, `negativo`, `mono-espresso`, `mono-hueso`. |
| `logos/zegno-avatar-instagram.svg` | Foto de perfil de 1080 × 1080 (también la versión `-claro`). |
| `logos/destacadas/` | Las cinco portadas de destacadas: servicios, casos, proceso, tips y contacto. |
| `manual/manual.src.html` | Fuente del manual (los SVG se insertan al armarlo). |
| `tools/` | Scripts que generan los logos y arman el manual. |

## Sistema en una línea

Isotipo **Z de encuadre** (dos esquinas de visor unidas por una diagonal, más el punto REC).
Colores: Espresso `#2A1D17`, Hueso `#EFE8DD`, Niebla `#D8CEC0`, Tungsteno `#D4892F`, REC `#E0442C` (solo el punto).
Tipografías (Google Fonts): Fraunces Italic 600 para títulos, DM Sans para textos y DM Mono para etiquetas.

## Regenerar

```bash
pip install fonttools brotli
# descargar Fraunces Italic 600 (SOFT 100) y DM Mono 500 como TTF en una carpeta, con los nombres fraunces-it.ttf y dmmono.ttf
python3 tools/armar_manual.py <carpeta_fuentes>
```
