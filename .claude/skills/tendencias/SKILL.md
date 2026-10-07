---
name: tendencias
description: Busca tendencias virales actuales (colores, prendas, estéticas, formatos, búsquedas y audios) en TikTok, Instagram, Pinterest y Google, las filtra según la estrategia de @belengrillo_ y las convierte en ideas de video listas para grabar. Usala cuando pida "tendencias", "qué está viral", "trends", "qué se está buscando", "color de moda", "ideas con lo que está pegando" o "qué está funcionando esta semana".
---

# Búsqueda de tendencias virales

Encontrás lo que tiene momento **ahora** y lo traducís a videos que encajen en
la cuenta. Una tendencia que no pasa el filtro no se entrega, por más viral
que sea.

## 1. Antes de buscar, leé

- `estrategia/00-contexto.md` → nicho, audiencia (mujeres argentinas 20-35,
  centro en 28), límites.
- `estrategia/07-pilares-y-voz.md` → carriles y voz.
- `estrategia/10-datos-reales.md` → qué ya funcionó. La vía comprobada es
  **"color de tendencia con nombre propio"** (butter yellow → 17K).
- El archivo más reciente en `tendencias/`, si existe, para no repetir lo que
  ya se reportó y marcar qué sigue subiendo y qué se cayó.

## 2. Dónde buscar

Usá WebSearch (y WebFetch cuando una página lo permita). Hacé las búsquedas en
paralelo, en español y en inglés, con el mes y año actuales.

| Fuente | Qué sacar |
|---|---|
| TikTok Creative Center (Trends: hashtags, canciones, creadores) | Hashtags y audios en subida, filtrando por Argentina si se puede |
| Pinterest Trends / Pinterest Predicts | Colores, estéticas y prendas en subida |
| Google Trends (Argentina) | Búsquedas de moda, colores, prendas, "cómo combinar…" |
| Medios de moda (Vogue, Harper's Bazaar, Elle, revistas argentinas) | Color de la temporada, prendas del momento, pasarelas |
| Notas sobre "TikTok trends" de la semana / el mes | Formatos y memes de video en circulación |
| Retail argentino (Zara AR, vidrieras, lanzamientos locales) | Qué está entrando efectivamente a las tiendas acá |

**Temporada:** acordate de que Argentina está en el hemisferio sur. Una
tendencia de "otoño" del norte llega acá con desfase o hay que adaptarla.

**Honestidad sobre las fuentes:** no tenés acceso al feed ni a las métricas
internas de TikTok. Si un dato viene de una nota y no de una fuente primaria,
decilo. No inventes números de views ni de crecimiento.

## 3. Qué buscar (en este orden de prioridad)

1. **Colores con nombre propio** ("butter yellow", "mocha mousse", "cherry
   red"…). Es la vía comprobada de la cuenta.
2. **Prendas y estéticas** en subida (una prenda puntual, un estilo con
   nombre).
3. **Búsquedas con intención**: "cómo combinar X", "qué ponerse para Y",
   "colores que favorecen…".
4. **Formatos de video** (estructuras, memes, plantillas) que se puedan hacer
   hablando, sin bailar.
5. **Audios** en subida que sirvan de fondo para combinaciones o series.
6. **Publicidad pública del momento** (campañas, lanzamientos, polémicas de
   marca) que alimenten el carril "cómo te venden".

## 4. Filtro: entra sólo si pasa todo

- [ ] Encaja en un carril de `07` (vida con ropa · guía de compra · autoridad ·
      edición · cómo te venden).
- [ ] Se puede hacer en la voz de "la amiga que te avisa".
- [ ] **No es un trend de baile.** Límite duro, sin excepciones.
- [ ] Le habla a una mujer argentina de ~28 con trabajo, no a una de 20.
- [ ] Se consigue o se ve en Argentina (o el ángulo es justamente que no).
- [ ] No obliga a comprar mucho: se resuelve con lo que hay en el placard,
      con un producto puntual o con SHEIN.
- [ ] No toca clientes ni campañas internas de la agencia.

Si una tendencia es enorme pero no pasa, ponela en "Descartadas" con el motivo
en una línea. Sirve para no volver a evaluarla.

## 5. Entregá esto

Guardá el informe en `tendencias/AAAA-MM-DD.md` (fecha de hoy) y mostrale un
resumen en el chat.

```markdown
# Tendencias — DD/MM/AAAA

## Para grabar esta semana (máx. 3)
La que tiene más momento y mejor encaje primero.

### 1. [Nombre de la tendencia]
- **Qué es:** una línea.
- **Por qué ahora:** la señal concreta + fuente (link).
- **Ventana:** subiendo · pico · bajando.
- **Carril / formato:** …
- **Título-gancho:** "…" (usá la fórmula de `10-datos-reales.md` cuando sea
  un color: "Combinaciones con [color] que no fallan", "Si tenés [color]…")
- **Primer frame:** qué se ve en el segundo 0.
- **Búsqueda a capturar:** la frase que la gente tipea → va en la primera
  línea del caption.

## En el radar (subiendo, todavía no)
- [Tendencia] — señal — cuándo volver a mirarla.

## Descartadas
- [Tendencia] — motivo (ej.: trend de baile; público de 18-22; no llega a AR).

## Fuentes
- …
```

## 6. Después

- Preguntá si quiere sumar las ideas elegidas al banco: agregalas al archivo
  del carril en `banco-de-ideas/` y como filas nuevas `estado=idea` en
  `banco-de-ideas/estado.csv` (siguiente `id` libre).
- Ofrecé pasar la #1 directo a caption con la skill `caption`, usando la
  "búsqueda a capturar" como primera línea.
- Recordá la regla 9 del plan de recuperación: **un cambio por vez**. Una
  tendencia nueva entra cambiando el tema, no el formato y el horario a la vez.
