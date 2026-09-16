#!/usr/bin/env python3
"""
Adapta un PDF de libro a un tamano imprimible y anillable.

Que hace:
  1. Detecta el area real de contenido de cada pagina (descarta margenes muertos).
  2. Reencuadra ese contenido en el tamano de libro elegido, con margenes
     espejados: el margen interior (del lado del anillado) mas ancho que el
     exterior, alternando en paginas pares e impares.
  3. Opcionalmente inserta paginas en blanco para que cada capitulo (nivel 1
     del indice del PDF) arranque en pagina impar, como un libro de verdad.
  4. Opcionalmente impone 2 paginas A5 por hoja A4 apaisada, en orden
     "cortar y apilar", para imprimir a doble faz y cortar al medio.

Uso tipico (A5, para llevar a la imprenta):
    python3 herramientas/libro_imprimible.py libro.pdf -o libro-A5.pdf

Uso para imprimir en casa en A4 y cortar al medio:
    python3 herramientas/libro_imprimible.py libro.pdf -o libro-2up.pdf --modo 2up-a4
"""

import argparse
import os
import sys

try:
    import pymupdf as fitz
except ImportError:  # versiones viejas
    import fitz

MM = 72.0 / 25.4

# ancho x alto en milimetros
TAMANOS = {
    "a5": (148.0, 210.0),
    "b5": (176.0, 250.0),
    "6x9": (152.4, 228.6),
    "15x21": (150.0, 210.0),
    "5.5x8.5": (139.7, 215.9),
    "a4": (210.0, 297.0),
}


def bbox_contenido(page, margen_seguridad=2.0):
    """Union de todo lo dibujado en la pagina, con un colchon de seguridad."""
    r = fitz.Rect()
    for b in page.get_text("blocks"):
        r |= fitz.Rect(b[:4])
    for img in page.get_images(full=True):
        try:
            for ir in page.get_image_rects(img[0]):
                r |= ir
        except Exception:
            pass
    try:
        for d in page.get_drawings():
            r |= d["rect"]
    except Exception:
        pass

    if r.is_empty or r.is_infinite:
        return None

    r += (-margen_seguridad, -margen_seguridad, margen_seguridad, margen_seguridad)
    r &= page.rect
    return r if not r.is_empty else None


def plan_paginas(doc, capitulos_impar):
    """Lista de entradas: indice de pagina origen, o None para hoja en blanco."""
    inicios = set()
    if capitulos_impar:
        for nivel, _titulo, pag in doc.get_toc():
            if nivel == 1 and pag >= 1:
                inicios.add(pag - 1)

    plan = []
    for i in range(doc.page_count):
        # len(plan) es la cantidad ya colocada -> la proxima seria la impar
        # numero len(plan)+1. Si el capitulo caeria en par, metemos una blanca.
        if i in inicios and (len(plan) + 1) % 2 == 0:
            plan.append(None)
        plan.append(i)
    return plan


def construir_interior(doc, cfg):
    ancho_mm, alto_mm = TAMANOS[cfg.tamano]
    W, H = ancho_mm * MM, alto_mm * MM

    plan = plan_paginas(doc, cfg.capitulos_impar)
    if cfg.prueba:
        plan = plan[: cfg.prueba]

    multiplo = 4 if cfg.modo == "2up-a4" else 2
    while len(plan) % multiplo:
        plan.append(None)

    out = fitz.open()
    for n, origen in enumerate(plan, start=1):
        pagina = out.new_page(width=W, height=H)
        if origen is None:
            continue

        impar = n % 2 == 1  # recto: anillado a la izquierda
        izq = (cfg.interior if impar else cfg.exterior) * MM
        der = (cfg.exterior if impar else cfg.interior) * MM
        marco = fitz.Rect(izq, cfg.superior * MM, W - der, H - cfg.inferior * MM)

        src = doc[origen]
        clip = bbox_contenido(src) if cfg.recortar else None
        pagina.show_pdf_page(marco, doc, origen, clip=clip)

    return out, plan


def imponer_2up(interior, dorso):
    """2 paginas por hoja A4 apaisada, orden cortar-y-apilar, doble faz."""
    W, H = 297.0 * MM, 210.0 * MM
    mitad_izq = fitz.Rect(0, 0, W / 2, H)
    mitad_der = fitz.Rect(W / 2, 0, W, H)

    total = interior.page_count
    mitad = total // 2

    out = fitz.open()
    for j in range(total // 4):
        frente = out.new_page(width=W, height=H)
        frente.show_pdf_page(mitad_izq, interior, 2 * j)
        frente.show_pdf_page(mitad_der, interior, 2 * j + mitad)

        reverso = out.new_page(width=W, height=H)
        a, b = 2 * j + 1, 2 * j + 1 + mitad
        if dorso == "espejado":
            a, b = b, a
        reverso.show_pdf_page(mitad_izq, interior, a)
        reverso.show_pdf_page(mitad_der, interior, b)

    return out


def main():
    p = argparse.ArgumentParser(
        description="Adapta un PDF a tamano libro para imprimir y anillar.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("entrada", help="PDF de origen")
    p.add_argument("-o", "--salida", required=True, help="PDF de salida")
    p.add_argument(
        "--tamano", default="a5", choices=sorted(TAMANOS),
        help="tamano final del libro (default: a5)",
    )
    p.add_argument(
        "--modo", default="directo", choices=["directo", "2up-a4"],
        help="directo = una pagina por hoja; 2up-a4 = dos A5 por hoja A4 para cortar",
    )
    p.add_argument("--interior", type=float, default=20.0, help="margen del lomo en mm (default: 20)")
    p.add_argument("--exterior", type=float, default=12.0, help="margen exterior en mm (default: 12)")
    p.add_argument("--superior", type=float, default=15.0, help="margen superior en mm (default: 15)")
    p.add_argument("--inferior", type=float, default=15.0, help="margen inferior en mm (default: 15)")
    p.add_argument(
        "--sin-recorte", dest="recortar", action="store_false",
        help="no recortar los margenes originales (usa la hoja entera del origen)",
    )
    p.add_argument(
        "--capitulos-impar", action="store_true",
        help="insertar blancas para que cada capitulo arranque en pagina derecha",
    )
    p.add_argument(
        "--dorso", default="espejado", choices=["espejado", "directo"],
        help="solo en 2up-a4: como ordena el dorso segun como da vuelta la hoja tu impresora",
    )
    p.add_argument("--prueba", type=int, default=0, help="procesar solo las primeras N paginas")
    p.add_argument(
        "--separar-portada", action="store_true",
        help="guardar la pagina 1 en un PDF aparte (para imprimir en cartulina)",
    )
    cfg = p.parse_args()

    if cfg.modo == "2up-a4" and cfg.tamano != "a5":
        p.error("--modo 2up-a4 solo funciona con --tamano a5 (es la unica medida que entra justo 2 veces en A4)")

    doc = fitz.open(cfg.entrada)
    if doc.needs_pass:
        p.error("el PDF esta protegido con contrasena")

    interior, plan = construir_interior(doc, cfg)
    resultado = imponer_2up(interior, cfg.dorso) if cfg.modo == "2up-a4" else interior

    if cfg.separar_portada and resultado.page_count > 1:
        base, ext = os.path.splitext(cfg.salida)
        portada = fitz.open()
        portada.insert_pdf(resultado, from_page=0, to_page=0)
        portada.save(base + "-portada" + ext)
        resultado.delete_page(0)
        print(f"portada  -> {base}-portada{ext}")

    resultado.save(cfg.salida, garbage=4, deflate=True)

    blancas = sum(1 for x in plan if x is None)
    ancho_mm, alto_mm = TAMANOS[cfg.tamano]
    print(f"origen   : {doc.page_count} pag ({doc[0].rect.width/MM:.0f} x {doc[0].rect.height/MM:.0f} mm)")
    print(f"libro    : {len(plan)} pag de {ancho_mm:.0f} x {alto_mm:.0f} mm ({blancas} en blanco agregadas)")
    if cfg.modo == "2up-a4":
        print(f"impresion: {resultado.page_count} hojas A4 apaisadas, doble faz, cortar al medio")
    else:
        print(f"impresion: {resultado.page_count} paginas, doble faz")
    print(f"salida   -> {cfg.salida}")


if __name__ == "__main__":
    sys.exit(main())
