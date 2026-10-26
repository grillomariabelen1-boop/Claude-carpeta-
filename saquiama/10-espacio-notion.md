# Prompt para Claude in Chrome · Espacio de trabajo Saquiama en Notion

Armá en Notion, dentro de la página **"👗 Saquiama — Pauta"**, el espacio de trabajo de abajo. Si alguna base o página ya existe con el mismo nombre, no la dupliques: completá lo que falte. No borres nada de lo que ya está en la página. No agregues nombres, mails ni teléfonos de clientas.

---

## 1. Base de datos "✅ Tareas"

Propiedades:
- **Tarea** (título)
- **Estado** (estado): Pendiente · Esperando respuesta · En curso · Hecho
- **Responsable** (selección): Belén · Marce · Desarrollador
- **Área** (selección): Pauta · Creativos · Web y checkout · Medición · Datos
- **Prioridad** (selección): Alta · Media · Baja
- **Fecha** (fecha)
- **Notas** (texto)

Vistas: tablero por Estado, y una tabla por Responsable.

Filas:

| Tarea | Responsable | Área | Prioridad | Estado | Notas |
|---|---|---|---|---|---|
| Confirmar fechas de Saquiama Days | Marce | Pauta | Alta | Esperando respuesta | Mismas fechas que el Cyber, mismos beneficios de siempre. |
| Lista de otras prendas que más se venden | Marce | Creativos | Alta | Esperando respuesta | Para sumar guiones del video "¿Te quedaste pensando?" y placas nuevas. |
| Grabar videos de Saquiama Days (guiones 1 a 5) | Marce | Creativos | Alta | Pendiente | Ver página Guiones Saquiama Days. El Anny solo necesita grabar las 2 frases de comienzo. |
| Cambiar placa 12 a "En Saquiama Days, es ahora" | Belén | Creativos | Media | Pendiente | Hoy dice "En Cyber, es ahora". No usar la palabra Cyber. |
| Armar placas aprobadas: Camisero Anita A/B/C, Saco Amanda "¿Lo estás pensando?", Retiro "¿No querés esperar el envío?" | Belén | Creativos | Media | Pendiente | Siempre con fondo detrás del texto y márgenes de 120 px. |
| Placa "¿Dudás con el talle?" (Anny) | Marce | Creativos | Media | Esperando respuesta | Falta confirmar si se asesora talle por WhatsApp. |
| Mandar reseñas de clientas para placa | Belén | Creativos | Media | Pendiente | Sacar nombres antes de usarlas. |
| Confirmar datos para textos: política de cambios, tiempo de despacho, altura y talle de Marce, tela y colores del Anny | Marce | Creativos | Media | Esperando respuesta | |
| Export de pedidos WooCommerce julio a octubre (sin datos de clientas) | Marce | Datos | Alta | Pendiente | Para comparar ventas cobradas mes a mes. Sin nombres, mails ni teléfonos. |
| Checkout: mostrar "3 cuotas sin interés" (hoy escondidas en "Débito Mercado Pago") | Desarrollador | Web y checkout | Alta | Pendiente | Cambiar el nombre de la opción y mostrar cuotas en producto y carrito. |
| Checkout: carga lenta (~10 s) | Desarrollador | Web y checkout | Alta | Pendiente | Medido desde fuera de Argentina, es aproximado. |
| Checkout: Argentina como país por defecto | Desarrollador | Web y checkout | Media | Pendiente | |
| Checkout: teléfono obligatorio | Desarrollador | Web y checkout | Media | Pendiente | Para escribir por WhatsApp a quien no terminó la compra. |
| Checkout: textos de España y en inglés | Desarrollador | Web y checkout | Baja | Pendiente | Apellidos, Población, Código postal / ZIP, Cart, Checkout, aviso de privacidad. |
| Verificar a mano: dirección de Avellaneda muestra envío CABA | Belén | Web y checkout | Baja | Pendiente | |
| Medición: Purchase al marcar Completado (PixelYourSite) | Desarrollador | Medición | Alta | Hecho | Purchase solo por CAPI, calidad de coincidencia 9.3. |
| Desactivar redirección "?v=" (geolocalización) | Desarrollador | Web y checkout | Media | Hecho | |

---

## 2. Base de datos "🎨 Creativos"

Propiedades:
- **Pieza** (título)
- **Tipo** (selección): Placa · Video · Catálogo
- **Campaña** (selección): Retargeting · Prospecting · Día de la Madre · Saquiama Days
- **Estado** (estado): Idea · Texto aprobado · Para grabar · Lista · Activa · Pausada · Descartada
- **Producto** (texto)
- **Ángulo** (texto)
- **Formatos** (selección múltiple): 9:16 · 4:5
- **Gasto** (número, moneda)
- **Compras** (número)
- **CPA** (fórmula): `if(prop("Compras") > 0, round(prop("Gasto") / prop("Compras")), 0)`
- **Resultado** (selección): Ganador · Bien · Flojo · Perdedor · Sin datos
- **Notas** (texto)

Vistas: tablero por Estado, y una galería o tabla por Campaña.

Filas (los números son de Meta, del 1 al 23/10):

| Pieza | Tipo | Campaña | Estado | Producto | Ángulo | Compras | Resultado | Notas |
|---|---|---|---|---|---|---|---|---|
| Anny ocasiones | Video | Día de la Madre | Activa | Vestido Anny | Un vestido para distintas ocasiones | 7 | Ganador | CPA ~$10.000. Se reusa en Saquiama Days con comienzos nuevos. |
| Urgencia gift card | Video | Día de la Madre | Activa | Gift card | Urgencia + beneficios | | Bien | Mejor CTR de la campaña. |
| Elegidos de Marce | Video | Día de la Madre | Activa | | Marce recomienda prendas | | Flojo | |
| Regalos por 60mil | Video | Día de la Madre | Activa | | Opciones de regalo hasta $60.000 | | Perdedor | Candidato a pausar. |
| Placa 1 · 15% OFF | Placa | Retargeting | Activa | | Descuento por transferencia | | Sin datos | |
| Placa 2 · ¿Te quedaste pensando? | Placa | Retargeting | Activa | | Duda / volver al carrito | 13 | Ganador | Ángulo a repetir con otras prendas. |
| Placa 3 · Volvé por lo que te gustó | Placa | Retargeting | Activa | | Recordatorio | | Bien | |
| Placa · Envío gratis | Placa | Retargeting | Activa | | Envío gratis desde $140.000 | | Perdedor | La mayoría de las prendas cuesta menos de $140.000. |
| 5 · Saco Amanda 3 cuotas | Placa | Retargeting | Lista | Saco Amanda | 3 cuotas de $20.000 | | | Rehacer con fondo detrás del texto. |
| 6 · Vestido Anny | Placa | Retargeting | Lista | Vestido Anny | | | | Rehacer con fondo detrás del texto. |
| 7 · Retiro en showroom | Placa | Retargeting | Lista | | Retiro gratis en Avellaneda | | | Rehacer con fondo detrás del texto. |
| 8 · ¿Negro o azul? | Placa | Retargeting | Descartada | Camisero Anita | | | | |
| 9 · ¿Seguís pensándolo? | Placa | Retargeting | Lista | Camisero Anita | | | | |
| 10 · Lo viste, te gustó | Placa | Retargeting | Lista | Vestido Paris | | | | |
| 11 · Te estaba esperando | Placa | Retargeting | Lista | Vestido Anny | | | | |
| 12 · Saquiama Days, es ahora | Placa | Saquiama Days | Lista | Saco Amanda | | | | Hoy dice "En Cyber, es ahora": cambiar. |
| Camisero Anita A/B/C | Placa | Retargeting | Texto aprobado | Camisero Anita | | | | |
| ¿Lo estás pensando? (Saco Amanda) | Placa | Retargeting | Texto aprobado | Saco Amanda | | | | |
| ¿No querés esperar el envío? | Placa | Retargeting | Texto aprobado | | Retiro en showroom | | | |
| ¿Dudás con el talle? (Anny) | Placa | Retargeting | Idea | Vestido Anny | | | | Espera confirmación de WhatsApp. |
| Video 1 · ¿Te quedaste pensando? (3 prendas) | Video | Saquiama Days | Para grabar | | | | | |
| Video 2 · Anny comienzos nuevos (A y B) | Video | Saquiama Days | Para grabar | Vestido Anny | El que más me piden | | | Solo grabar la frase de comienzo. |
| Video 3 · Me pruebo 3 cosas | Video | Saquiama Days | Para grabar | | | | | |
| Video 4 · El look completo | Video | Saquiama Days | Para grabar | | | | | |
| Video 5 · Últimas horas | Video | Saquiama Days | Para grabar | | | | | Solo para el último día. |

---

## 3. Página "📋 Brief: beneficios, productos y estilo"

**Beneficios que se pueden comunicar**
- 15% OFF pagando por transferencia
- 3 cuotas sin interés (con Mercado Pago)
- Envío gratis desde $140.000
- Retiro gratis en el showroom: Beguerestain 2105, Avellaneda
- Gift card

Aviso: la mayoría de las prendas cuesta menos de $140.000, así que el envío gratis no es buen gancho solo.

**Envíos:** CABA $7.000 · Precio fijo $10.000 · Retiro en showroom gratis · Gratis desde $140.000.

**Precios en la web (octubre):**
- Camisero Anita (azul o negro, talles 1 a 3): $98.000
- Vestido Anny: $86.000
- Vestido Paris: $80.000
- Twinset Capri: $79.000
- Mono Alegra: $79.000
- India Liso: $71.000
- Pantalón Vito: $69.000
- Cinturón Santorini: $65.000
- Vestido India: $65.000
- Saco Amanda (3 x $20.000): $60.000
- Capita Ursula: $52.000

**Estilo de las placas (aprobado):**
- Texto blanco. Título en Instrument Serif, con acento en cursiva. "15% OFF" en Inter. Beneficios en Jost, en mayúsculas.
- Siempre un fondo oscuro semitransparente detrás del texto.
- Márgenes de 120 px a los costados. En 9:16, nada en el 14% de arriba ni en el 35% de abajo.
- El texto va sobre la pared o el espejo, nunca tapando la prenda. No cortar la cabeza.
- Un solo bloque de texto, no repartido a izquierda y derecha.
- Sin logo, sin dirección web, sin "Comprá online".
- Evitar fotos de la web que parecen hechas con IA o con otra modelo.

**Cómo trabajamos los textos:**
- En retargeting, resolver dudas y cerrar la venta.
- Proponer los textos y aprobarlos antes de armar las piezas.
- Variar los textos: no repetir siempre lo mismo.

---

## 4. Página "🎬 Guiones Saquiama Days"

Copiar el contenido completo de `saquiama/09-guiones-videos-cyber.md`, sin la sección "Pendiente".

---

## 5. Página "📏 Medición y públicos"

**Medición**
- Purchase se manda a Meta cuando el pedido pasa a Completado (PixelYourSite, por CAPI). La calidad de coincidencia es 9.3.
- Las transferencias cuentan cuando se marcan Completado.
- Los números de Meta no se comparan con septiembre, porque cambió la forma de medir.
- Para comparar meses, usar las ventas cobradas de WooCommerce.
- Atribución: 7 días clic / 1 día vista.
- UTM: `utm_source={{site_source_name}}&utm_medium=paid&utm_campaign={{campaign.name}}&utm_content={{ad.name}}`

**Prospecting excluye:**
- Visitantes web 30 días
- AddToCart 30 días
- InitiateCheckout 30 días
- Purchase 180 días
- Lista de clientas

**Retargeting incluye:**
- Visitantes web 30 días
- Vieron el 50% de un video, 60 días
- Interactuaron con Instagram, 365 días
- Lista de clientas
- No incluye Purchase.

**Día de la Madre:** público abierto, $15.000 por día.

**Catálogo:** el conjunto de productos es primavera verano. Meta puede mostrar otros productos en stock aunque se elija un conjunto.

**Reglas:** la lista de clientas la sube Marce directo a Meta. Nunca pasar nombres, mails ni teléfonos.

---

## 6. Página "📊 Resultados y aprendizajes"

Nota: datos de Meta, con atribución 7 días clic / 1 día vista.

**1 al 23 de octubre:**
- Siempre activa: 25 compras, ROAS 6,3
- Día de la Madre: 17 compras, ROAS 7,5

**Embudo del 6 al 9 de octubre (Meta):**
- 3.200 vieron un producto
- 117 agregaron al carrito
- 99 iniciaron el pago
- 6 compraron

**Qué aprendimos:**
- Funciona: Marce probándose las prendas, el vestido Anny y los looks completos.
- "¿Te quedaste pensando?" es la placa ganadora de retargeting, con 13 compras. Conviene repetir el ángulo con otras prendas.
- El envío gratis no sirve como gancho.
- "Regalos por 60mil" fue el peor anuncio del Día de la Madre.
- Mucha gente llega al pago y no compra. Las 3 cuotas no se ven hasta Mercado Pago y el checkout carga lento.

---

## 7. Arriba de la página principal

Agregar al principio una sección **"🧭 Accesos"** con links a las 2 bases y a las 4 páginas. Mover las secciones viejas de septiembre (Hecho, Antes de presentar, Preguntarle a Marce, Para el desarrollador, Pauta, Primeros 30 días) a una subpágina llamada **"🗄️ Archivo septiembre"**, sin borrar su contenido. Dejar en la principal "Cómo trabajar con este cliente" y "Reglas".
