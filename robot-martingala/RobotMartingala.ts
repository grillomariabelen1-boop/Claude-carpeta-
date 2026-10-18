# Robot Martingala para thinkorswim (thinkScript - Strategy)
# Solo compras. Sin stop loss y sin límite de entradas.
# 1) Sin posición: compra si el precio está arriba de la EMA.
# 2) Si cae "distancia_pct" desde la última compra: compra de nuevo multiplicando la cantidad.
# 3) Si sube "take_profit_pct" sobre el precio promedio de la canasta: vende todo y reinicia.

input acciones_iniciales = 10;   # Cantidad de la primera compra
input multiplicador = 2.0;       # Multiplicador de cantidad en cada nueva compra
input distancia_pct = 2.0;       # % de caída desde la última compra para volver a comprar
input take_profit_pct = 1.0;     # % de ganancia sobre el promedio para cerrar todo
input largo_ema = 50;            # EMA que habilita la primera compra

def ema = ExpAverage(close, largo_ema);

def totalCant;
def costoTotal;
def ultPrecio;
def ultCant;

def hayPos = totalCant[1] > 0;
def promedio = if hayPos then costoTotal[1] / totalCant[1] else 0;

def cerrar = hayPos and close >= promedio * (1 + take_profit_pct / 100);
def primera = !hayPos and close > ema;
def promediar = hayPos and !cerrar and close <= ultPrecio[1] * (1 - distancia_pct / 100);

def cantNueva = if primera then acciones_iniciales
                else if promediar then Round(ultCant[1] * multiplicador, 0)
                else 0;

totalCant  = CompoundValue(1, if cerrar then 0 else totalCant[1] + cantNueva, 0);
costoTotal = CompoundValue(1, if cerrar then 0 else costoTotal[1] + cantNueva * close, 0);
ultPrecio  = CompoundValue(1, if cantNueva > 0 then close else ultPrecio[1], 0);
ultCant    = CompoundValue(1, if cantNueva > 0 then cantNueva else ultCant[1], 0);

AddOrder(OrderType.BUY_TO_OPEN, cantNueva > 0, close, cantNueva, Color.GREEN, Color.GREEN, "Martingala");
AddOrder(OrderType.SELL_TO_CLOSE, cerrar, close, totalCant[1], Color.RED, Color.RED, "TP canasta");

plot PrecioPromedio = if totalCant > 0 then costoTotal / totalCant else Double.NaN;
PrecioPromedio.SetDefaultColor(Color.YELLOW);
PrecioPromedio.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
