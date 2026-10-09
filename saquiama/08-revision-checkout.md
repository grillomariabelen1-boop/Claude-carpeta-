# Revisión del checkout (9/10/2026)

Prueba en celular simulado (iPhone 13), con Camisero Anita. **No se hizo ninguna compra.** Puede haber generado 2 o 3 eventos de prueba (AddToCart / InitiateCheckout) del lado del servidor.

## Problemas encontrados (por prioridad)

1. **El envío gratis no se elige solo.** Con $196.000 en el carrito aparece "Envío gratuito", pero queda marcado "Envío a domicilio en CABA: $7.000" y el total lo suma. La clienta paga envío aunque el anuncio dice "envío gratis desde $140.000".
2. **El descuento por transferencia sigue aplicado al elegir tarjeta.** Con tarjeta seleccionada el resumen sigue mostrando "Descuento por transferencia (15%)". Si después Mercado Pago cobra otro monto, genera desconfianza o reclamos. Hay que probar el pago con tarjeta de punta a punta.
3. **El checkout tarda unos 10 segundos en cargar**, y las opciones de envío aparecen varios segundos después de completar la dirección. Mientras tanto el total se ve sin envío y después cambia.
4. **Zona de envío:** con una dirección de Avellaneda (provincia de Buenos Aires) aparece y queda elegido "Envío a domicilio en CABA". Revisar zonas.
5. **País sin elegir:** dice "Selecciona un país/región…" (250 países). Para una tienda que vende en Argentina, debería venir en Argentina o no mostrarse.
6. **Teléfono opcional:** sin teléfono no se puede recuperar por WhatsApp a quien no terminó la compra. Conviene que sea obligatorio.
7. **Textos de España y en inglés:** "Apellidos", "Población", "Código postal / ZIP", "Región / Provincia"; títulos "Cart" y "Checkout"; el aviso de privacidad está en inglés.
8. **No se mencionan las 3 cuotas sin interés** en el checkout (ni al elegir tarjeta).
9. **Encabezado muy alto en celular** (banner + logo + buscador ≈ 365 px) y el botón "Buscar" queda cortado a la derecha.

## Lo que está bien
- Medios de pago: transferencia (con 15% OFF aplicado), Débito Mercado Pago y tarjeta.
- Opción "Retirar en Showroom GRATIS".
- Cupón y tarjeta regalo disponibles.
