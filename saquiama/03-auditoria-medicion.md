# Por qué el panel de Meta puede mostrar más ventas de las reales

> **Es la preocupación principal del cliente.** Este documento junta lo que ya
> se sabe revisando la web y lo que falta confirmar con los datos.

*Relevado el 25/9/2026.*

## Lo que ya revisé en la web

| Qué | Resultado |
|---|---|
| ¿Cuántos píxeles hay en el código de la web? | **Uno solo** (`868160216021939`), cargado por PixelYourSite. No hay píxeles pegados a mano |
| ¿Se manda también por servidor (API de conversiones)? | **Sí**, desde el mismo plugin |
| ¿Tiene ID de evento para no contar doble entre el navegador y el servidor? | **Sí** (`sendEventId: true`) |
| ¿Tiene activada la "coincidencia avanzada"? | **No.** Meta recibe menos datos para reconocer a quien compró. Eso no infla las ventas, pero baja la calidad de la medición |
| ¿Hay algo más que pueda mandar compras a Meta? | **No.** El Google Tag Manager (`GTM-KM9JWL46`) solo tiene Google Analytics 4 |

## Las 4 causas posibles, de más a menos probable

### 1 · Meta se atribuye ventas sin clic
Desde 2026, Meta cuenta por defecto la compra de alguien que **solo vio** el
anuncio (1 día) o que **solo interactuó** con él, sin hacer clic (1 día). Con
120.000 seguidoras, que ven los anuncios y además compran por el orgánico, esto
suma muchas ventas que igual iban a pasar.

**Cómo se confirma:** en la exportación con "Comparar ventanas de atribución",
comparar las compras con "solo 7 días de clic" contra el total.

### 2 · Se cuentan pedidos por transferencia que nunca se pagaron
El 15% de descuento empuja a pagar por transferencia. En ese caso, **el pedido
se crea y la página de "gracias" aparece antes de que llegue la plata**. El
plugin manda la compra a Meta en ese momento. Si la clienta después no
transfiere, **para Meta fue una venta y para la caja no**.

**Cómo se confirma:** en WooCommerce, contar los pedidos "En espera" y
"Cancelados" de los últimos 90 días. Si son muchos, esta es una causa fuerte.

**Cómo se arregla:** en PixelYourSite, revisar en qué estados del pedido se
dispara la compra. Si el plugin no lo permite, hay que evaluarlo con el
desarrollador.

### 3 · ~~El Tag Manager manda una segunda compra~~ → descartada (25/9)
Revisé el contenedor público del Tag Manager (`GTM-KM9JWL46`). **No tiene
ningún píxel ni etiqueta de Meta.** Solo tiene Google Analytics 4
(`G-H4KJMMQZV1`), con los eventos ver producto, agregar al carrito, iniciar
checkout y **compra**.

**Dato útil:** como Google Analytics también registra las compras, hay una
**segunda fuente, independiente de Meta**, para contar las ventas web.
Cualquiera que tenga acceso a Google Analytics (o a Site Kit, adentro del
WordPress) puede ver cuántas compras hubo del 1 al 25 de septiembre. Si Google
Analytics cuenta menos de 37 compras **en total, de todos los canales**, Meta
está contando de más con seguridad.

### 4 · Los pedidos de Mercado Pago rechazados o pendientes
Con Mercado Pago pasa algo parecido a la transferencia: si el pago queda
pendiente o se rechaza, la clienta igual puede volver a la página de "gracias".

**Cómo se confirma:** igual que la 2, mirando los pedidos cancelados y fallidos.

## Qué le decimos al cliente

1. **"Tenían razón."** Hay al menos dos motivos técnicos por los que el panel
   cuenta de más, y no dependen de quién manejaba la pauta.
2. **"Lo vamos a medir con su caja."** El número oficial pasa a ser el MER:
   ventas cobradas de la web dividido la inversión en pauta. El ROAS de Meta
   queda solo para comparar anuncios entre sí.
3. **"Y lo vamos a corregir en origen":** que la compra se registre recién
   cuando se paga, revisar el Tag Manager y activar la coincidencia avanzada.

## Lo que necesito para cerrarlo

- [ ] Pedidos de WooCommerce de los últimos 90 días **con su estado** (pagado,
      en espera, cancelado, fallido) y el **medio de pago**. Sin datos
      personales.
- [ ] La exportación de Meta con "Comparar ventanas de atribución".
- [ ] Una captura del evento Purchase en el Administrador de eventos (de dónde
      llega).
- [x] ~~Etiquetas del Tag Manager~~: revisadas, no hay nada de Meta.
- [ ] Compras y facturación del 1 al 25/9 según **Google Analytics** (o Site Kit en el WordPress).
- [ ] Una captura de la configuración del evento Purchase en PixelYourSite.
