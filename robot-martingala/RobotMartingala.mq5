//+------------------------------------------------------------------+
//|                                             RobotMartingala.mq5  |
//|  Martingala en canasta: sin stop loss y sin límite de operaciones |
//+------------------------------------------------------------------+
#property copyright "Robot Martingala"
#property version   "1.00"
#property strict

#include <Trade\Trade.mqh>

//--- Parámetros
input double LoteInicial      = 0.01;   // Lote de la primera operación
input double Multiplicador    = 2.0;    // Multiplicador de lote en cada nueva entrada
input int    DistanciaPips    = 20;     // Pips en contra para abrir la siguiente entrada
input int    TakeProfitPips   = 10;     // Ganancia en pips sobre el precio promedio para cerrar todo
input int    PeriodoEMA       = 50;     // EMA que decide la dirección de la primera entrada
input ENUM_TIMEFRAMES MarcoEMA = PERIOD_H1; // Marco temporal de la EMA
input ulong  NumeroMagico     = 777001; // Identificador de las operaciones del robot
input int    DeslizamientoPts = 30;     // Deslizamiento máximo en puntos

CTrade trade;
int    handleEMA = INVALID_HANDLE;
double pip;

//+------------------------------------------------------------------+
int OnInit()
  {
   trade.SetExpertMagicNumber(NumeroMagico);
   trade.SetDeviationInPoints(DeslizamientoPts);

   int digitos = (int)SymbolInfoInteger(_Symbol, SYMBOL_DIGITS);
   pip = (digitos == 3 || digitos == 5) ? _Point * 10 : _Point;

   handleEMA = iMA(_Symbol, MarcoEMA, PeriodoEMA, 0, MODE_EMA, PRICE_CLOSE);
   if(handleEMA == INVALID_HANDLE)
     {
      Print("No se pudo crear la EMA");
      return INIT_FAILED;
     }
   return INIT_SUCCEEDED;
  }

//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
   if(handleEMA != INVALID_HANDLE)
      IndicatorRelease(handleEMA);
  }

//+------------------------------------------------------------------+
//| Ajusta el lote al paso, mínimo y máximo que permite el broker     |
//+------------------------------------------------------------------+
double NormalizarLote(double lote)
  {
   double minimo = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_MIN);
   double maximo = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_MAX);
   double paso   = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_STEP);
   lote = MathFloor(lote / paso) * paso;
   return MathMax(minimo, MathMin(maximo, lote));
  }

//+------------------------------------------------------------------+
//| Abre una posición sin SL ni TP individual                         |
//+------------------------------------------------------------------+
bool Abrir(ENUM_POSITION_TYPE tipo, double lote)
  {
   lote = NormalizarLote(lote);
   bool ok = (tipo == POSITION_TYPE_BUY)
             ? trade.Buy(lote, _Symbol, 0, 0, 0, "Martingala")
             : trade.Sell(lote, _Symbol, 0, 0, 0, "Martingala");
   if(!ok)
      Print("Error al abrir ", lote, " lotes: ", trade.ResultRetcodeDescription());
   return ok;
  }

//+------------------------------------------------------------------+
void CerrarTodo()
  {
   for(int i = PositionsTotal() - 1; i >= 0; i--)
     {
      ulong ticket = PositionGetTicket(i);
      if(ticket == 0) continue;
      if(PositionGetString(POSITION_SYMBOL) != _Symbol) continue;
      if(PositionGetInteger(POSITION_MAGIC) != (long)NumeroMagico) continue;
      if(!trade.PositionClose(ticket))
         Print("Error al cerrar ", ticket, ": ", trade.ResultRetcodeDescription());
     }
  }

//+------------------------------------------------------------------+
void OnTick()
  {
   int    cantidad      = 0;
   double volumenTotal  = 0;
   double sumaPrecioVol = 0;
   double ultimoPrecio  = 0;
   double ultimoLote    = 0;
   long   ultimaHora    = 0;
   ENUM_POSITION_TYPE tipo = POSITION_TYPE_BUY;

   //--- Relevar la canasta abierta
   for(int i = PositionsTotal() - 1; i >= 0; i--)
     {
      ulong ticket = PositionGetTicket(i);
      if(ticket == 0) continue;
      if(PositionGetString(POSITION_SYMBOL) != _Symbol) continue;
      if(PositionGetInteger(POSITION_MAGIC) != (long)NumeroMagico) continue;

      double vol    = PositionGetDouble(POSITION_VOLUME);
      double precio = PositionGetDouble(POSITION_PRICE_OPEN);
      long   hora   = PositionGetInteger(POSITION_TIME_MSC);

      cantidad++;
      volumenTotal  += vol;
      sumaPrecioVol += precio * vol;
      tipo = (ENUM_POSITION_TYPE)PositionGetInteger(POSITION_TYPE);

      if(hora > ultimaHora)
        {
         ultimaHora   = hora;
         ultimoPrecio = precio;
         ultimoLote   = vol;
        }
     }

   double bid = SymbolInfoDouble(_Symbol, SYMBOL_BID);
   double ask = SymbolInfoDouble(_Symbol, SYMBOL_ASK);

   //--- Sin posiciones: primera entrada según la EMA
   if(cantidad == 0)
     {
      double ema[1];
      if(CopyBuffer(handleEMA, 0, 0, 1, ema) != 1)
         return;
      Abrir(bid > ema[0] ? POSITION_TYPE_BUY : POSITION_TYPE_SELL, LoteInicial);
      return;
     }

   double promedio = sumaPrecioVol / volumenTotal;

   if(tipo == POSITION_TYPE_BUY)
     {
      //--- Toda la canasta llegó al objetivo: cerrar y reiniciar
      if(bid >= promedio + TakeProfitPips * pip)
        {
         CerrarTodo();
         return;
        }
      //--- El precio fue en contra: nueva entrada con lote multiplicado
      if(ask <= ultimoPrecio - DistanciaPips * pip)
         Abrir(POSITION_TYPE_BUY, ultimoLote * Multiplicador);
     }
   else
     {
      if(ask <= promedio - TakeProfitPips * pip)
        {
         CerrarTodo();
         return;
        }
      if(bid >= ultimoPrecio + DistanciaPips * pip)
         Abrir(POSITION_TYPE_SELL, ultimoLote * Multiplicador);
     }
  }
//+------------------------------------------------------------------+
