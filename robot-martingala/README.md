# Robot Martingala (thinkorswim)

Estrategia en thinkScript con martingala en canasta, **solo compras**, **sin stop loss** y **sin límite de entradas**. Pensada para acciones o ETFs.

## Cómo funciona

1. Sin posición abierta: compra `acciones_iniciales` si el precio cierra arriba de la EMA.
2. Si el precio cae `distancia_pct` % desde la última compra: vuelve a comprar la cantidad anterior × `multiplicador`.
3. Si el precio sube `take_profit_pct` % sobre el **precio promedio** de todas las compras: vende todo y vuelve a empezar.
4. No hay stop loss ni tope de compras.

La línea amarilla del gráfico es el precio promedio de la canasta abierta.

## Parámetros

| Parámetro | Default | Qué hace |
|---|---|---|
| `acciones_iniciales` | 10 | Acciones de la primera compra |
| `multiplicador` | 2.0 | Cuánto se multiplica la cantidad en cada nueva compra |
| `distancia_pct` | 2.0 | % de caída para volver a comprar |
| `take_profit_pct` | 1.0 | % sobre el promedio para cerrar todo |
| `largo_ema` | 50 | EMA que habilita la primera compra |

## Instalación

1. En thinkorswim, en un gráfico: **Studies → Edit studies → pestaña Strategies → Create**.
2. Pegá el contenido de `RobotMartingala.ts`, ponele nombre `RobotMartingala` y guardá.
3. Agregalo al gráfico.
4. **Importante:** en **Edit studies → Global strategy settings**, subí "Maximum entry orders in the same direction" al máximo que permita. Si queda en 1, thinkorswim ignora las compras de la martingala.
5. Para ver resultados: clic derecho en cualquier señal → **Show report**.

## Limitación de thinkorswim

Las estrategias de thinkorswim **solo simulan sobre el gráfico (backtest), no mandan órdenes reales**. thinkorswim no tiene forma de ejecutar sola una martingala en vivo. Para que opere de verdad hay que usar la API de Schwab (por ejemplo con Python) corriendo en una computadora o servidor.

## ⚠️ Riesgo

Con los valores por defecto la cantidad se duplica cada 2 % de caída:

| Compras | Caída aprox. | Última compra | Acciones totales |
|---|---|---|---|
| 1 | 0 % | 10 | 10 |
| 5 | 8 % | 160 | 310 |
| 8 | 13 % | 1.280 | 2.550 |
| 10 | 17 % | 5.120 | 10.230 |

En una acción de USD 100, a las 10 compras tenés más de USD 850.000 invertidos con una caída del 17 %, algo que pasa seguido en una corrección. Sin stop loss, si no hay plata o margen para seguir comprando, la pérdida queda abierta entera o el broker liquida por margin call.
