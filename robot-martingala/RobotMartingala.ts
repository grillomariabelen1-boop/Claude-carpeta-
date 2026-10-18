# Robot Martingala para thinkorswim (thinkScript - Strategy)
# Ajustado para S&P 500 (SPY, /ES, /MES) y Nasdaq 100 (QQQ, /NQ, /MNQ).
# Solo compras. Sin stop loss y sin límite de entradas.
# 1) Sin posición: compra si el precio está arriba de la EMA.
# 2) Si cae "distancia" % desde la última compra: compra de nuevo multiplicando la cantidad.
# 3) Si sube "take profit" % sobre el precio promedio de la canasta: vende todo y reinicia.

input mercado = {default SP500, Nasdaq, Personalizado};
input cantidad_inicial = 1;      # Acciones (SPY/QQQ) o contratos (/ES, /MES, /NQ, /MNQ)
input multiplicador = 2.0;       # Multiplicador de cantidad en cada nueva compra
input largo_ema = 50;            # EMA que habilita la primera compra
input distancia_pct = 2.0;       # Solo se usa con mercado = Personalizado
input take_profit_pct = 1.0;     # Solo se usa con mercado = Personalizado

# S&P 500 se mueve menos que el Nasdaq: entradas más juntas y objetivo más chico
def distancia = if mercado == mercado.SP500 then 1.5
                else if mercado == mercado.Nasdaq then 2.0
                else distancia_pct;
def objetivo  = if mercado == mercado.SP500 then 0.75
                else if mercado == mercado.Nasdaq then 1.0
                else take_profit_pct;

def ema = ExpAverage(close, largo_ema);

def totalCant;
def costoTotal;
def ultPrecio;
def ultCant;

def hayPos = totalCant[1] > 0;
def promedio = if hayPos then costoTotal[1] / totalCant[1] else 0;

def cerrar = hayPos and close >= promedio * (1 + objetivo / 100);
def primera = !hayPos and close > ema;
def promediar = hayPos and !cerrar and close <= ultPrecio[1] * (1 - distancia / 100);

def cantNueva = if primera then cantidad_inicial
                else if promediar then Max(1, Round(ultCant[1] * multiplicador, 0))
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
