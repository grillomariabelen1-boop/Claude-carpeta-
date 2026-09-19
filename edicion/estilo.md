# El estilo de edición, medido

No es una descripción a ojo: son números sacados de dos videos propios con
`analizar_referencia.py`. Sirve para que cualquier video nuevo salga igual sin
tener que acordarse de nada.

Las dos referencias:

| | Referencia A (color lavanda) | Referencia B (habladito) |
|---|---|---|
| Duración | 49,0 s | 40,9 s |
| Planos | 9 | 2 |
| Plano promedio | 5,44 s | 20,5 s |
| Plano mediana | 4,27 s | 20,5 s |
| Cortes por segundo | 0,16 | 0,02 |
| Resolución del archivo | 576×1024 | 576×1024 |

La resolución es la de la copia bajada de TikTok, no la del original. Todo lo
de color de abajo está medido **después** de que TikTok lo comprimió, así que
el original era un poco más saturado.

## Los subtítulos

Es lo más característico y lo más fácil de replicar.

- **Una palabra por vez**, centrada. Nunca una frase entera.
- **Arriba, no abajo**: la banda de texto va entre el **19% y el 24%** de la
  altura del cuadro. En un export de 1080×1920 eso es entre y=365 y y=480.
  Está medido en 11 frames de los dos videos y no se mueve.
  Es una decisión buena: abajo está la interfaz de TikTok, que tapa.
- **Altura de la letra**: ~4-5% del alto del cuadro. En 1080×1920, cuerpo de
  **85 a 100 px**.
- **Dos colores y nada más:**
  - blanco `#FEFDFB`
  - lavanda `#C6C0E4` ← medido en tres palabras distintas, da siempre igual
- **El color de acento es el color del que habla el video.** En la referencia A
  el tema es el lavanda, y las palabras acentuadas son lavanda. O sea: el acento
  no es fijo, cambia con el video. Eso es un sistema, no un capricho: liga el
  texto al pilar de color.
- Las palabras acentuadas son las que cargan el dato (`color`, `segurísima`,
  `ya`); el resto va en blanco.
- Tienen una sombra oscura suave atrás para que se lean sobre fondo claro.
- **Tipografía**: palo seco redondeada, pesada, en minúscula. No se puede
  identificar con certeza desde una copia de 576 px recomprimida, y lo más
  probable es que sea una fuente interna de CapCut, que no se puede distribuir.
  Las dos más parecidas con licencia abierta son **Fredoka SemiBold** y
  **Nunito Black**.
- Aparece además una **cursiva manuscrita** que se escribe sola, con cursor
  tipo máquina de escribir. Equivalente con licencia abierta: **Caveat** o
  **Dancing Script**.

## El sonido va pegado al corte

Es el hallazgo menos obvio y el que más cambia el resultado.

De los 9 cortes de las dos referencias, **7 tienen un golpe de audio encima**,
con un desfase de entre 0 y 70 ms:

```
corte  2,93 s -> golpe a  2,98 s  (+50 ms)
corte 15,73 s -> golpe a 15,74 s  (+10 ms)
corte 34,80 s -> golpe a 34,78 s  (−20 ms)
corte 36,20 s -> golpe a 36,24 s  (+40 ms)
corte 37,93 s -> golpe a 37,96 s  (+30 ms)
corte 40,53 s -> golpe a 40,60 s  (+70 ms)
corte  7,60 s -> golpe a  7,60 s  (  0 ms)   [referencia B]
```

Regla para copiarlo: **efecto sobre el corte, nunca después**. Un `whoosh` del
kit, adelantado unos 30 ms respecto del frame del corte.

Aclaración honesta: el detector marca cualquier transitorio fuerte, y algunos
podrían ser el arranque de una palabra. Pero 7 de 9 —y uno clavado en 0 ms— es
demasiado para ser casualidad.

## La composición

Dos modos, y el video alterna entre ellos:

**Modo collage** — cuatro fotos de referencia llenando el cuadro, una o dos
fichas Pantone superpuestas en el centro con el nombre del color, y la cara
recortada abajo al centro, chica. Es el modo de autoridad: se muestra evidencia.

**Modo cara limpia** — plano entero, sin ningún gráfico encima. Es el modo de
confianza: sólo la cara hablando.

## La estructura de la referencia A

```
 0,0 – 2,9 s    collage          gancho: entra mostrando, no hablando
 2,9 – 34,8 s   cara limpia      con cortes de salto en 11,5 / 15,7 / 21,4
34,8 – 49,0 s   collage x4       ráfaga final: 1,4 s · 1,7 s · 2,6 s · 8,5 s
```

Abre con evidencia, desarrolla a cara limpia y cierra con una ráfaga de
collages que acelera el ritmo justo antes del final.

Un dato para mirar con cuidado: dentro del tramo hablado hay un plano de
**13,4 segundos sin un solo corte** (21,4 → 34,8). Es el punto más probable de
abandono del video, y conecta directo con el diagnóstico de retención de
`estrategia/01-diagnostico.md`.

## Receta corta

Para que un video nuevo salga con este estilo:

1. Subtítulo de a una palabra, centrado, al 21% de altura, cuerpo 90 px.
2. Blanco, y el color del video en las palabras que cargan el dato.
3. Un `whoosh` sobre cada corte, 30 ms antes del frame.
4. Cortes de salto cada 4-6 s en los tramos hablados. Ninguno más largo de 8 s.
5. Abrir con collage, desarrollar a cara limpia, cerrar con ráfaga de collage.
