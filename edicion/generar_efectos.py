"""Genera los efectos de sonido del kit, sintetizados desde cero.

No se descarga nada: cada efecto se construye onda por onda, así que no tienen
dueño y se pueden usar en contenido monetizado y en trabajo pago sin riesgo.

Uso: python3 generar_efectos.py [carpeta-salida]   (por defecto: ./sfx)
"""
import math
import sys
import wave
from pathlib import Path

import numpy as np

SR = 48000


def env(n, ataque=0.005, caida=0.2, curva=3.0):
    """Envolvente de amplitud: cuánto tarda en entrar y en apagarse."""
    t = np.linspace(0, 1, n)
    atk = np.clip(t / ataque, 0, 1)
    rel = np.exp(-curva * np.clip((t - ataque) / (1 - ataque), 0, 1) * (1 / max(caida, 1e-3)) * 0.35)
    return atk * rel


def biquad_bp(x, fc_arr, Q=2.0):
    """Pasabanda con la frecuencia central variando en el tiempo (el barrido)."""
    y = np.zeros_like(x)
    x1 = x2 = y1 = y2 = 0.0
    for i in range(len(x)):
        w0 = 2 * math.pi * fc_arr[i] / SR
        al = math.sin(w0) / (2 * Q)
        cw = math.cos(w0)
        b0, b1, b2 = al, 0.0, -al
        a0, a1, a2 = 1 + al, -2 * cw, 1 - al
        xi = x[i]
        yi = (b0 / a0) * xi + (b1 / a0) * x1 + (b2 / a0) * x2 - (a1 / a0) * y1 - (a2 / a0) * y2
        x2, x1 = x1, xi
        y2, y1 = y1, yi
        y[i] = yi
    return y


def guardar(carpeta, nombre, x, pico=0.85):
    m = np.max(np.abs(x)) or 1.0
    x = x / m * pico
    f = int(SR * 0.003)  # 3 ms de fundido en los bordes para que no cliquee
    if len(x) > 2 * f:
        x[:f] *= np.linspace(0, 1, f)
        x[-f:] *= np.linspace(1, 0, f)
    destino = carpeta / f"{nombre}.wav"
    with wave.open(str(destino), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((x * 32767).astype("<i2").tobytes())
    print(f"  {destino}  {len(x)/SR:.2f}s")


def main(salida="sfx"):
    carpeta = Path(salida)
    carpeta.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(7)  # semilla fija: los efectos salen siempre iguales

    # whoosh — transición entre dos planos
    n = int(SR * 0.55)
    t = np.linspace(0, 1, n)
    fc = 300 + 3600 * np.sin(np.pi * t) ** 1.5
    guardar(carpeta, "whoosh", biquad_bp(rng.normal(0, 1, n), fc, Q=1.4) * env(n, 0.18, 0.55, 2.2))

    # riser — sube la tensión antes de revelar algo
    n = int(SR * 0.9)
    t = np.linspace(0, 1, n)
    fc = 250 * np.exp(np.log(6000 / 250) * t)
    guardar(carpeta, "riser", biquad_bp(rng.normal(0, 1, n), fc, Q=3.0) * (t ** 1.6))

    # click — para que entre un texto
    n = int(SR * 0.05)
    guardar(carpeta, "click", biquad_bp(rng.normal(0, 1, n), np.full(n, 3400.0), Q=1.0) * env(n, 0.002, 0.05, 6))

    # pop — para una placa chica o un chip de color
    n = int(SR * 0.09)
    f = np.linspace(900, 180, n)
    guardar(carpeta, "pop", np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.004, 0.09, 5))

    # ding — remate de un dato
    n = int(SR * 0.7)
    t = np.linspace(0, 1, n)
    guardar(carpeta, "ding", (np.sin(2 * np.pi * 2093 * t) + 0.5 * np.sin(2 * np.pi * 3136 * t)
                              + 0.25 * np.sin(2 * np.pi * 4186 * t)) * np.exp(-5 * t))

    # thud — cierre, peso
    n = int(SR * 0.4)
    t = np.linspace(0, 1, n)
    f = np.linspace(110, 45, n)
    guardar(carpeta, "thud", np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-6 * t))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "sfx")
