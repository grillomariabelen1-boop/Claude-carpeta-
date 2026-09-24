# Web: base para la propuesta de mejoras

> **Pendiente:** conseguir la URL para auditarla. Esta es la checklist con la
> que se va a revisar. Todavía no son recomendaciones.

**Por qué importa para la pauta:** la pauta trae la visita y la web la
convierte. Si la conversión sube de 1% a 1,5%, el mismo presupuesto vende 50%
más. Con USD 300 al mes, mejorar la web es la palanca más barata que hay.

## Qué revisar, en orden de impacto

### 1 · Celular y velocidad
- [ ] ¿Carga en menos de 3 segundos en 4G? Revisar con PageSpeed Insights, versión móvil.
- [ ] ¿Las fotos están comprimidas (WebP) y cargan a medida que se baja?
- [ ] ¿El botón de comprar se ve sin bajar, en la ficha de producto?

### 2 · Ficha de producto (para una clienta de 30 a 50)
- [ ] ¿Hay tabla de talles **en centímetros**, con cómo medirse?
- [ ] ¿Dice qué talle usa la modelo y cuánto mide?
- [ ] ¿Hay video de la prenda puesta? Los mismos videos que ya funcionan en pauta.
- [ ] ¿La composición de la tela y el cuidado están visibles?
- [ ] ¿El precio, las cuotas sin interés y el precio por transferencia están arriba?
- [ ] ¿Hay reseñas o fotos de clientas?

### 3 · Confianza y fricción
- [ ] ¿La política de cambios está clara y a la vista? Es la duda número uno en ropa online.
- [ ] ¿El costo de envío se ve **antes** del checkout?
- [ ] ¿Hay botón de WhatsApp para dudas de talle?
- [ ] ¿Muestra el showroom (dirección, horarios, fotos)? Da confianza aunque no vayan.

### 4 · Checkout
- [ ] ¿Se puede comprar sin crear cuenta?
- [ ] ¿Cuántos pasos tiene? Lo ideal es 1 o 2 pantallas.
- [ ] ¿Qué medios de pago acepta? Mercado Pago, tarjetas en cuotas, transferencia con descuento.
- [ ] ¿Pide solo los datos necesarios?

### 5 · Ticket promedio
- [ ] ¿Hay envío gratis desde un monto? Con un ticket de $80.000, un umbral un poco más alto (por ejemplo $100.000–$110.000) empuja a agregar una prenda.
- [ ] ¿Hay "completá el look" o productos relacionados en la ficha?

### 6 · Medición (lo técnico que afecta la pauta)
- [ ] ¿Los eventos ViewContent, AddToCart, InitiateCheckout y Purchase se disparan todos, con valor y moneda?
- [ ] ¿El píxel y la API de conversiones deduplican (el mismo `event_id`)?
- [ ] ¿Hay catálogo de productos conectado a Meta? Permite anuncios de catálogo y etiquetas de compra en Instagram.
- [ ] ¿Existe Google Analytics 4 para cruzar los datos con Meta?

## Formato de la propuesta final

Una tabla por mejora: **qué pasa hoy → qué cambiar → impacto esperado →
esfuerzo para el desarrollador (bajo, medio o alto)**. Se ordena por impacto
dividido por esfuerzo, para que la marca apruebe primero lo barato que más
mueve.
