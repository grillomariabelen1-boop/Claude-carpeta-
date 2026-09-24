# Village Polo Club — Análisis de anuncios Meta, 1 al 23/9/2026

*Fuente: exportación de anuncios del Administrador de Meta (nivel anuncio). Atribución de Meta, sin cruzar con Tiendanube.*

---

## Totales del período

| Métrica | Valor |
|---|---|
| Gasto | $901.908 (~$39.200 por día; proyecta ~$1,18M en el mes) |
| Compras atribuidas | 20 |
| Valor de compras | $2.580.858 |
| **ROAS** | **2,86** (el objetivo es 6) |
| Costo por compra | $45.095 |
| Ticket atribuido | $129.043 |
| CTR del enlace | 2,41% |
| CPM | $2.622 |
| Clics → carrito | 3,9% (321 de 8.287) |
| **Carrito → compra** | **6,2% (20 de 321)** |

## Por anuncio

| Anuncio | Gasto | % del gasto | Compras | ROAS | Costo/compra | Ticket | CTR | CPM | Frec. | Calidad |
|---|---|---|---|---|---|---|---|---|---|---|
| **Winter sale \| enfoque ambos** | $302.891 | 33,6% | **9** | **4,38** | $33.655 | $147.493 | 2,54% | **$1.879** | 2,43 | Promedio |
| TOP 3 - WINTER SALE | $302.138 | 33,5% | 4 | **1,65** | $75.535 | $124.762 | 2,20% | $3.261 | 1,97 | Promedio |
| PLACA 2 WINTER SALE IA | $148.490 | 16,5% | 4 | 3,49 | $37.122 | $129.618 | 3,02% | $5.016 | **3,11** | **Por debajo del promedio** |
| 3 prendas invierno | $136.153 | 15,1% | 3 | 1,73 | $45.384 | $78.633 | 2,02% | $2.364 | 1,50 | Promedio |
| 6 anuncios restantes | $12.235 | 1,4% | 0 | — | — | — | — | — | — | — |

Los 6 restantes son: PLACA 1 WINTER SALE, Ambos_ocasiones de uso, Ambos consideración, Ambo lavable 200mil, Ambo compra
directa descuento y ARRANCO winter sale.

---

## Lo que se puede afirmar

1. **El ROAS real es 2,86, no 6.** Para llegar a 6 hay que duplicar el rendimiento. Antes de fijarlo como objetivo conviene saber
   cuál es el ROAS de equilibrio según el margen.
2. **Un anuncio trae la mitad de la venta.** "Winter sale | enfoque ambos" tiene el 45% de las compras y el 51% del valor, con el
   CPM más bajo. Meta encuentra a su público de forma más barata.
3. **"TOP 3 - WINTER SALE" gasta lo mismo que el ganador y rinde casi 3 veces menos** (ROAS 1,65 contra 4,38). Es el primer
   candidato a pausar o bajar.
4. **"PLACA 2 IA" está saturando.** Frecuencia de 3,1, calidad por debajo del promedio y el CPM más alto. Su ROAS de 3,49 es
   bueno, pero está en caída.
5. **"3 prendas invierno" no subió el ticket.** Da el ticket más bajo ($78.633). Los compradores no se llevaron el combo.
6. **Los 6 anuncios restantes no se testearon.** Recibieron menos de $4.000 cada uno. **No hay datos para descartar** ningún
   ángulo de ambos ("ocasiones de uso", "consideración", "lavable 200mil", "compra directa descuento"). Meta los dejó sin
   entrega dentro de un conjunto compartido.

## Lo que todavía no se puede afirmar

- **Las muestras son chicas.** Con 20 compras en total, la diferencia entre 9 y 4 compras es direccional, no concluyente.
- **Qué compraron.** El pixel atribuye la compra al anuncio, no al producto. El ticket de "enfoque ambos" ($147.493) es menor
  que el precio del ambo ($200.000), así que puede que esas compras hayan sido otras prendas.
- **Si el pixel mide bien.** Pasar del carrito a la compra en un 6,2% es muy bajo (en moda suele estar entre 20% y 40%). Puede
  ser un problema del checkout (costo de envío, talle, medios de pago) **o que el pixel no esté registrando todas las compras**.
  Hay que cruzarlo con los pedidos de Tiendanube del mismo período.
- **La estructura.** La exportación es por anuncio. No muestra si hay campañas o conjuntos de prospección y de retargeting, ni la
  segmentación.

## Conclusión provisoria

**El cuello de botella no es la atención sino lo que pasa después del clic.** El CTR (2,4%) es sano; lo que se cae es el paso
del carrito a la compra. Antes de sumar ángulos nuevos:

1. Validar el pixel contra Tiendanube.
2. Revisar el checkout: costo de envío por debajo de $150.000, info de talles, medios de pago.
3. Redistribuir el gasto: bajar TOP 3 y darle presupuesto propio al ganador y a los anuncios de ambos que no se testearon.

## Datos pendientes para cerrar el análisis

- [ ] Pedidos y facturación de Tiendanube del 1 al 23/9 (para validar el pixel)
- [ ] Qué muestra cada anuncio: producto, formato (video, imagen, carrusel) y copy
- [ ] Exportación a nivel conjunto de anuncios: nombre, segmentación y presupuesto
- [ ] Precio de los ambos y cuánto pesan en la venta
- [ ] Margen aproximado, para calcular el ROAS de equilibrio
