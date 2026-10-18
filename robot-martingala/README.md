# Robot Martingala (MetaTrader 5)

Expert Advisor en MQL5 que opera con martingala en canasta, **sin stop loss** y **sin límite de operaciones**.

## Cómo funciona

1. Si no hay posiciones abiertas, abre una con `LoteInicial`. La dirección la decide una EMA: precio arriba de la EMA → compra; abajo → venta.
2. Si el precio va en contra `DistanciaPips` desde la última entrada, abre otra en la misma dirección con el lote anterior × `Multiplicador`.
3. Cuando el precio supera el **precio promedio ponderado** de toda la canasta por `TakeProfitPips`, cierra todo y vuelve a empezar.
4. No hay stop loss ni tope de entradas: sigue promediando mientras el broker le dé margen.

## Parámetros

| Parámetro | Default | Qué hace |
|---|---|---|
| `LoteInicial` | 0.01 | Lote de la primera operación |
| `Multiplicador` | 2.0 | Cuánto se multiplica el lote en cada nueva entrada |
| `DistanciaPips` | 20 | Pips en contra para abrir la siguiente |
| `TakeProfitPips` | 10 | Ganancia sobre el promedio para cerrar la canasta |
| `PeriodoEMA` / `MarcoEMA` | 50 / H1 | Filtro de dirección de la primera entrada |
| `NumeroMagico` | 777001 | Identifica las operaciones del robot |
| `DeslizamientoPts` | 30 | Deslizamiento máximo |

## Instalación

1. En MetaTrader 5: **Archivo → Abrir carpeta de datos → MQL5 → Experts**.
2. Copiá `RobotMartingala.mq5` ahí.
3. Abrilo con MetaEditor y compilá (F7).
4. Arrastralo al gráfico y activá **Trading algorítmico**.

## ⚠️ Riesgo — leelo antes de usarlo en real

Sin stop loss y sin límite, la martingala gana seguido montos chicos y, cuando el precio va en contra sin retroceder, **puede vaciar la cuenta entera**. Con `Multiplicador = 2` y `DistanciaPips = 20`, el lote se duplica cada 20 pips en contra:

| Entradas | Pips en contra | Lote de la última | Volumen total |
|---|---|---|---|
| 1 | 0 | 0.01 | 0.01 |
| 5 | 80 | 0.16 | 0.31 |
| 8 | 140 | 1.28 | 2.55 |
| 10 | 180 | 5.12 | 10.23 |
| 12 | 220 | 20.48 | 40.95 |

Un movimiento de 200 pips sin retroceso es normal en pares como EURUSD en unos días. Cuando se acaba el margen, el broker cierra todo por *stop out* y la pérdida es la de la canasta completa.

Recomendación: probalo primero en el **Probador de estrategias** y en una **cuenta demo** durante varias semanas, incluyendo periodos de tendencia fuerte.
