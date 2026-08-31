# Diagnóstico del estancamiento

> **Actualizado el 30/8 con datos reales.** Dos cosas cambiaron:
> **(a)** la cuenta **no está penalizada** — un video de abril 2025 hizo 24.000
> views en los últimos 60 días, o sea mientras los nuevos hacen 180-350, así que
> TikTok sigue distribuyendo y el problema está en el contenido reciente;
> **(b)** la causa 3 (deriva de formato) queda **confirmada**: los hauls, que
> eran el 50-60% del plan, rinden 4× menos que los videos de color.
> Ver [`10-datos-reales.md`](10-datos-reales.md).

## Lo primero: la ventana de 4-6 semanas ya se cumplió

Promote se cortó el **10/7**. Al **30/8** pasaron **~7 semanas**.

La estimación de recuperación era de 4-6 semanas. Ya estamos afuera de esa
ventana y las views siguen en 180-350. Eso cambia el diagnóstico:

> **El resto de Promote ya no alcanza como explicación principal.**

Sigue siendo un factor de fondo, pero si fuera el único, a esta altura ya
habría un rebote parcial. Hay algo más sosteniendo el techo. Este documento
separa las dos cosas.

## Qué significa la banda 180-350

No es un número al azar: es el **pool inicial de distribución** de TikTok.
Todo video entra a una audiencia fría de unos cientos de cuentas. Pasa al
siguiente pool sólo si las señales de ese primer lote superan un umbral.

Señales que deciden el pase, ordenadas por peso real:

1. **Tasa de finalización** (¿lo vieron entero?)
2. **Watch time promedio** y rewatches
3. **Shares** y **saves**
4. Comentarios
5. Likes ← el que menos pesa

Quedarse clavada en 180-350 significa una sola cosa: **los videos entran al
pool y no lo superan**. No es un problema de cantidad de posteos ni de
hashtags ni de horario. Es un problema de **retención**.

Corolario importante: **postear más no rompe el techo**. Diez videos que no
pasan el pool son diez veces el mismo resultado.

## Por qué Promote dejó un hueco

Promote compra impresiones de una audiencia que no es la del grafo orgánico.
Ese público mira peor: menos finalización, menos rewatch, casi cero
seguimiento. El modelo igual registra esas señales flojas y ensucia su
estimación de "a quién le gusta esta cuenta".

Al cortar Promote, la distribución vuelve a ser orgánica, pero el historial
reciente que el modelo usa como referencia todavía está contaminado. La salida
es acumular videos orgánicos con buena retención hasta que el historial
reciente esté dominado por señales limpias.

Eso es lo que hace el plan color-first: **el color es el formato con mejor
rendimiento comprobado de la cuenta** (4× un haul), así que es la herramienta
más rápida para limpiar el historial. El plan original apostaba a los hauls por
un supuesto que los datos desmintieron.

## Las cuatro causas candidatas del techo actual

Con Promote ya descartado como causa única, quedan cuatro. No son excluyentes.

### 1. Retención en los primeros 3 segundos
La más probable. Si el primer frame no muestra ya el objeto de deseo (la ropa,
el color, el peinado terminado), se pierde entre 40% y 60% de la audiencia
antes del segundo 3. Con esa caída ningún video pasa el pool.

**Test:** mirar la curva de retención de los últimos 10 videos. Si la caída a
3s es mayor al 50%, el problema es el gancho y nada más.

### 2. Ambigüedad de tema a nivel cuenta
Muchos formatos distintos rotando **sin jerarquía** le dificultan al modelo
definir a qué audiencia servir la cuenta. Una cuenta legible se distribuye
mejor que una cuenta variada. El problema nunca fue la cantidad de formatos
sino que ninguno mandaba: desde el 30/8 hay jerarquía —color, guía de compra y
bajitas sostienen la semana ([`03-formatos.md`](03-formatos.md))— y el resto
rota alrededor.

**Test:** mirar los últimos 15 videos en la grilla. ¿Se lee "esto es una
cuenta de color y estilo" en dos segundos? Si no, hay ambigüedad.

### 3. Deriva de formato
Si en los últimos meses bajó la proporción de hauls y combinaciones de color
—los dos formatos que mejor performan— y subió la de formatos más lentos, la
retención promedio de la cuenta bajó por composición, no por calidad.

**Confirmado por los datos:** los hauls rinden 4× menos que los videos de
color. Si en los últimos meses subió la proporción de hauls, la retención
promedio de la cuenta bajó por composición.

**Test:** contar cuántos de los últimos 20 videos son de color o colorimetría.
Si son menos de 8, hay deriva.

### 4. Inconsistencia de cadencia
Huecos de varios días seguidos de tandas de tres videos. El modelo penaliza
la irregularidad más que el volumen bajo.

**Test:** mirar el calendario de los últimos 30 días.

## Cómo el plan ataca las cuatro

| Causa | Qué la ataca |
|---|---|
| Retención a 3s | Reglas de gancho y duración corta ([`02`](02-plan-recuperacion.md), [`03`](03-formatos.md)) |
| Ambigüedad de tema | Identidad única color + estilo en todos los videos ([`02`](02-plan-recuperacion.md)) |
| Deriva de formato | Ratio 40% color-first ([`02`](02-plan-recuperacion.md)) |
| Inconsistencia | Cadencia fija 5-6 por semana ([`04`](04-calendario-6-semanas.md)) |

## Antes de arrancar: hacer los cuatro tests

Los cuatro tests de arriba son 20 minutos de trabajo y definen dónde poner el
esfuerzo. Anotar los resultados en [`05-metricas.md`](05-metricas.md), sección
"Línea de base".

Sin línea de base no se puede saber si el plan funcionó.
