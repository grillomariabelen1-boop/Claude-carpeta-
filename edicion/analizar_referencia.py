"""Le saca la gramática de edición a un video de referencia.

Uso: python3 analizar_referencia.py <video.mp4> <carpeta-salida>

Devuelve: cortes, duración de cada plano, ritmo, picos de audio (candidatos a
efecto de sonido), paleta por plano, y una plancha de contactos con el primer
frame de cada plano.
"""
import json
import re
import subprocess
import sys
import wave
from pathlib import Path

import imageio_ffmpeg
import numpy as np
from PIL import Image

FF = imageio_ffmpeg.get_ffmpeg_exe()
FFPROBE = FF.replace("ffmpeg-", "ffprobe-") if Path(FF.replace("ffmpeg-", "ffprobe-")).exists() else None


def ficha(v):
    """Duración, resolución, fps, bitrate — leídos del propio ffmpeg."""
    p = subprocess.run([FF, "-hide_banner", "-i", str(v)], capture_output=True, text=True)
    txt = p.stderr
    out = {}
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", txt)
    if m:
        out["duracion_s"] = int(m[1]) * 3600 + int(m[2]) * 60 + float(m[3])
    m = re.search(r"Video:.*?, (\d+)x(\d+)", txt)
    if m:
        out["ancho"], out["alto"] = int(m[1]), int(m[2])
    m = re.search(r"([\d.]+) fps", txt)
    if m:
        out["fps"] = float(m[1])
    m = re.search(r"bitrate: (\d+) kb/s", txt)
    if m:
        out["bitrate_kbps"] = int(m[1])
    out["tiene_audio"] = "Audio:" in txt
    return out


def cortes(v, umbral=0.30):
    """Detecta los cambios de plano."""
    p = subprocess.run(
        [FF, "-hide_banner", "-i", str(v), "-filter:v", f"select='gt(scene,{umbral})',showinfo",
         "-f", "null", "-"],
        capture_output=True, text=True,
    )
    return sorted(float(m) for m in re.findall(r"pts_time:([\d.]+)", p.stderr))


def envolvente_audio(v, out_dir, ventana=0.02):
    """RMS del audio en ventanas cortas: sirve para ubicar golpes y efectos."""
    wav = out_dir / "_audio.wav"
    subprocess.run(
        [FF, "-hide_banner", "-loglevel", "error", "-y", "-i", str(v),
         "-ac", "1", "-ar", "24000", str(wav)], check=True,
    )
    with wave.open(str(wav), "rb") as w:
        sr = w.getframerate()
        x = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").astype(np.float32) / 32768
    n = int(sr * ventana)
    if n < 1 or len(x) < n:
        return sr, np.array([]), np.array([])
    recorte = x[: len(x) // n * n].reshape(-1, n)
    rms = np.sqrt((recorte ** 2).mean(axis=1))
    t = np.arange(len(rms)) * ventana
    wav.unlink(missing_ok=True)
    return sr, t, rms


def transitorios(t, rms, factor=2.6, sep=0.25):
    """Picos bruscos de volumen = candidatos a whoosh / click / golpe."""
    if len(rms) == 0:
        return []
    suave = np.convolve(rms, np.ones(25) / 25, mode="same")
    picos, ultimo = [], -9
    for i in range(1, len(rms) - 1):
        if rms[i] > factor * max(suave[i], 1e-4) and rms[i] >= rms[i - 1] and rms[i] > rms[i + 1]:
            if t[i] - ultimo > sep:
                picos.append(round(float(t[i]), 2))
                ultimo = t[i]
    return picos


def frame(v, seg, destino, ancho=360):
    subprocess.run(
        [FF, "-hide_banner", "-loglevel", "error", "-y", "-ss", str(seg), "-i", str(v),
         "-vframes", "1", "-vf", f"scale={ancho}:-1", str(destino)], check=True,
    )


def paleta(img_path, k=5):
    im = Image.open(img_path).convert("RGB").resize((120, 120))
    q = im.quantize(colors=k, method=Image.Quantize.FASTOCTREE)
    pal = q.getpalette()[: k * 3]
    cuenta = sorted(q.getcolors(), reverse=True)
    return ["#%02X%02X%02X" % tuple(pal[i * 3:i * 3 + 3]) for _, i in cuenta]


def plancha(frames, destino, cols=5):
    ims = [Image.open(f) for f in frames]
    if not ims:
        return
    w, h = ims[0].size
    filas = (len(ims) + cols - 1) // cols
    hoja = Image.new("RGB", (cols * w, filas * h), (18, 18, 18))
    for i, im in enumerate(ims):
        hoja.paste(im.resize((w, h)), ((i % cols) * w, (i // cols) * h))
    hoja.save(destino, quality=92)


def main(video, salida):
    v, out = Path(video), Path(salida)
    out.mkdir(parents=True, exist_ok=True)
    (out / "frames").mkdir(exist_ok=True)

    info = ficha(v)
    cs = cortes(v)
    dur = info.get("duracion_s", 0)

    # planos: desde cada corte hasta el siguiente
    limites = [0.0] + cs + [dur]
    planos = []
    for i in range(len(limites) - 1):
        ini, fin = limites[i], limites[i + 1]
        if fin - ini < 0.08:
            continue
        f = out / "frames" / f"plano{i:02d}.jpg"
        frame(v, ini + min(0.15, (fin - ini) / 3), f)
        planos.append({
            "n": len(planos) + 1,
            "entra_s": round(ini, 2),
            "sale_s": round(fin, 2),
            "dura_s": round(fin - ini, 2),
            "paleta": paleta(f),
            "frame": str(f.relative_to(out)),
        })

    sr, t, rms = envolvente_audio(v, out)
    picos = transitorios(t, rms)
    duraciones = [p["dura_s"] for p in planos]

    resumen = {
        "archivo": v.name,
        "ficha": info,
        "cortes_detectados": len(cs),
        "planos": len(planos),
        "plano_mas_corto_s": round(min(duraciones), 2) if duraciones else None,
        "plano_mas_largo_s": round(max(duraciones), 2) if duraciones else None,
        "plano_promedio_s": round(float(np.mean(duraciones)), 2) if duraciones else None,
        "plano_mediana_s": round(float(np.median(duraciones)), 2) if duraciones else None,
        "cortes_por_segundo": round(len(cs) / dur, 2) if dur else None,
        "picos_de_audio_s": picos,
        "detalle_planos": planos,
    }
    (out / "analisis.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=2))
    plancha([out / p["frame"] for p in planos], out / "planos.jpg")

    print(f"\n=== {v.name} ===")
    print(f"  {info.get('ancho')}x{info.get('alto')} · {info.get('fps')} fps · {dur:.1f}s")
    print(f"  {len(planos)} planos · promedio {resumen['plano_promedio_s']}s · "
          f"mediana {resumen['plano_mediana_s']}s · {resumen['cortes_por_segundo']} cortes/s")
    print(f"  cortes en: {[round(c,2) for c in cs]}")
    print(f"  picos de audio en: {picos}")
    return resumen


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
