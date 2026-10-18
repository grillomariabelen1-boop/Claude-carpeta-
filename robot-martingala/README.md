# Robot Martingala (thinkorswim) — S&P 500 y Nasdaq

Estrategia en thinkScript con martingala en canasta, **solo compras**, **sin stop loss** y **sin límite de entradas**. Ajustada para el S&P 500 y el Nasdaq 100.

## Dónde usarlo

| Mercado | ETF | Futuro micro | Futuro grande | `mercado` |
|---|---|---|---|---|
| S&P 500 | SPY | /MES ($5 por punto) | /ES ($50 por punto) | `SP500` |
| Nasdaq 100 | QQQ | /MNQ ($2 por punto) | /NQ ($20 por punto) | `Nasdaq` |

Abrí el gráfico del símbolo, agregá la estrategia y elegí el `mercado` que corresponde. Con futuros, empezá por los **micro** (/MES, /MNQ): son 10 veces más chicos.

## Cómo funciona

1. Sin posición abierta: compra `cantidad_inicial` si el precio cierra arriba de la EMA.
2. Si el precio cae la **distancia** desde la última compra: vuelve a comprar la cantidad anterior × `multiplicador`.
3. Si el precio sube el **take profit** sobre el precio promedio de todas las compras: vende todo y vuelve a empezar.
4. No hay stop loss ni tope de compras.

Valores que usa cada mercado (el Nasdaq se mueve más, por eso tiene más distancia):

| `mercado` | Distancia | Take profit |
|---|---|---|
| `SP500` | 1,5 % | 0,75 % |
| `Nasdaq` | 2 % | 1 % |
| `Personalizado` | `distancia_pct` | `take_profit_pct` |

La línea amarilla del gráfico es el precio promedio de la canasta abierta.

## Parámetros

| Parámetro | Default | Qué hace |
|---|---|---|
| `mercado` | SP500 | Elige los valores de distancia y take profit |
| `cantidad_inicial` | 1 | Acciones (SPY/QQQ) o contratos (futuros) de la primera compra |
| `multiplicador` | 2.0 | Cuánto se multiplica la cantidad en cada nueva compra |
| `largo_ema` | 50 | EMA que habilita la primera compra |
| `distancia_pct` | 2.0 | Solo con `Personalizado` |
| `take_profit_pct` | 1.0 | Solo con `Personalizado` |

## Instalación

1. En thinkorswim, en un gráfico: **Studies → Edit studies → pestaña Strategies → Create**.
2. Pegá el contenido de `RobotMartingala.ts`, ponele nombre `RobotMartingala` y guardá.
3. Agregalo al gráfico y elegí el `mercado`.
4. **Importante:** en **Edit studies → Global strategy settings**, subí "Maximum entry orders in the same direction" al máximo que permita. Si queda en 1, thinkorswim ignora las compras de la martingala.
5. Para ver resultados: clic derecho en cualquier señal → **Show report**.

## Limitación de thinkorswim

Las estrategias de thinkorswim **solo simulan sobre el gráfico (backtest), no mandan órdenes reales**. Para que opere de verdad hay que usar la API de Schwab (por ejemplo con Python) corriendo en una computadora o servidor.

## ⚠️ Riesgo

Con `multiplicador = 2` y `cantidad_inicial = 1`:

| Compras | Caída S&P 500 | Caída Nasdaq | Cantidad total |
|---|---|---|---|
| 1 | 0 % | 0 % | 1 |
| 5 | 6 % | 8 % | 31 |
| 8 | 10 % | 13 % | 255 |
| 10 | 13 % | 17 % | 1.023 |
| 12 | 15 % | 20 % | 4.095 |

Caídas así pasan seguido: el S&P 500 cayó cerca de 34 % en 2020, 25 % en 2022 y 19 % en 2025; el Nasdaq más todavía. En futuros, 255 contratos de /MES son unas 255 × 5 × el valor del índice en exposición (más de USD 7 millones con el índice en 6.000), y en /ES diez veces eso. Sin stop loss, cuando se acaba el margen el broker liquida todo.
