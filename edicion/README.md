# Edición — herramientas

Tres scripts para el pilar de edición (`banco-de-ideas/06-edicion.md`). Todo lo
que producen es reproducible: se corre el script y sale siempre igual.

## Instalación

```bash
pip install -r edicion/requisitos.txt
```

`imageio-ffmpeg` trae su propio ffmpeg, así que no hace falta instalarlo aparte.

## `generar_efectos.py` — los sonidos

```bash
python3 edicion/generar_efectos.py sfx
```

Sintetiza seis efectos desde cero. **No se descarga nada de ningún lado**: cada
sonido se construye onda por onda, así que no tienen dueño y se pueden usar en
contenido monetizado y en trabajo de marca sin riesgo de reclamo.

| Efecto | Para qué |
|---|---|
| `whoosh` | Transición entre dos planos |
| `riser` | Sube la tensión antes de revelar algo |
| `click` | Para que entre un texto |
| `pop` | Para una placa chica o un chip de color |
| `ding` | Remate de un dato |
| `thud` | Cierre, peso |

La semilla del ruido está fija, así que los archivos salen idénticos cada vez.

## `generar_superposiciones.py` — los gráficos

```bash
mkdir -p seq && python3 edicion/generar_superposiciones.py
```

Genera la secuencia de PNG con transparencia que después se superpone al video.
Cuatro tipos de superposición:

- **Franja + título** — el gancho. La franja negra al 45% está para que el texto
  blanco no desaparezca cuando el fondo es claro.
- **Chip de color** — círculo con el color real + el nombre. Es la superposición
  propia de la cuenta: el pilar de color hecho gráfico.
- **Zócalo editorial** — texto sin caja, tipografía fina, para un comentario al paso.
- **Subtítulo** — abajo, centrado, siempre en el mismo lugar.

Todo entra con una curva de desaceleración de ~350 ms. Nada aparece de golpe.

Los tiempos están escritos a mano dentro del script (`win(t, entra, sale)`) — en
un video real salen del guion.

Necesita las tipografías en `fonts/`. Todas las del kit tienen licencia SIL Open
Font License: uso comercial permitido.

### Componer con el video

```bash
ffmpeg -i plano.mp4 -framerate 30 -i "seq/f%04d.png" \
  -filter_complex "[0:v][1:v]overlay=0:0:format=auto" \
  -c:v libx264 -crf 20 -pix_fmt yuv420p salida.mp4
```

## `analizar_referencia.py` — leerle la edición a un video

El resultado de correrlo sobre dos videos propios está en [`estilo.md`](estilo.md).

```bash
python3 edicion/analizar_referencia.py referencia.mp4 analisis/
```

Convierte "me gusta cómo está editado" en números:

- cada corte y cuánto dura cada plano
- ritmo: plano promedio, mediana, el más corto, cortes por segundo
- picos de audio — dónde metieron los efectos
- paleta dominante de cada plano
- `planos.jpg`: plancha de contactos con el primer frame de cada plano
- `analisis.json`: todo lo anterior en crudo

## Lo que no hacen estos scripts

- **Música**: no se genera ni se descarga. Y el sonido de tendencia de TikTok se
  agrega adentro de TikTok — si se quema en el mp4 se pierde la asociación al
  sonido, que es un carril de distribución.
- **Transcripción automática**: todavía no. Los subtítulos se sincronizan a mano
  contra el guion de `plantillas/`.
