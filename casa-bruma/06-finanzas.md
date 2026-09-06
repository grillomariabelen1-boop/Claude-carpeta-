# Casa Bruma — finanzas

Qué cuesta cada cosa, cuánto deja, y cuánto hay que vender para no poner plata.

Todo lo que sigue sale de tres planillas del Drive (`CASA BRUMA/Planillas`):
`PRECIOS Y COSTOS 2026`, `CASABRUMA - datos` e `INVERSIONES-GASTOS Y DETALLE`.
**Los precios y los costos son de enero de 2026.** Con la inflación de los meses
que pasaron, los números de acá sirven para ver la *estructura* — qué producto
deja y cuál no, y por qué. Los valores absolutos hay que reajustarlos.

---

## 1 · El error que ordena todo lo demás

La columna «COSTO REAL X UNIDAD» de la planilla de precios **no es el costo
real**: son los insumos y nada más. Faltan cuatro cosas, y las cuatro salen de
tu propia plata:

| Qué falta | Cuánto | De dónde sale el dato |
|---|---|---|
| **Mano de obra** | $2.000 por unidad | Está en `CASABRUMA - datos`, pero no se traslada al costo |
| **Packaging** | 3% a 6% del precio | La regla está en `05-packaging.md` |
| **Comisión de cobro minorista** | **12,55%** | Mercado Pago, en `CASABRUMA - datos` |
| **Comisión de cobro mayorista** | 2% + IVA = 2,42% | Tiendanube / transferencia, misma planilla |

La comisión minorista es la más cara de las cuatro y la más fácil de olvidar,
porque no la pagás vos: te la descuentan antes de que la plata llegue.

**Costo real = insumos + mano de obra + packaging + comisión.**
Lo que queda después de eso es el **margen de contribución**: la plata que cada
venta aporta para pagar la estructura del mes.

---

## 2 · Cuánto deja cada vela — minorista

Precio de una unidad, packaging al 4%, comisión al 12,55%.

| Producto | Precio | Insumos | M. obra | Pack. | Comisión | **Contribución** | **%** |
|---|---:|---:|---:|---:|---:|---:|---:|
| Vela nudo 60g | 15.000 | 1.340 | 2.000 | 600 | 1.883 | **9.177** | **61,2%** |
| Torre vertical 140g | 20.500 | 2.965 | 2.000 | 820 | 2.573 | **12.142** | **59,2%** |
| Bubble 200g | 20.500 | 3.700 | 2.000 | 820 | 2.573 | **11.407** | **55,6%** |
| Arco 200g | 20.500 | 4.206 | 2.000 | 820 | 2.573 | **10.901** | **53,2%** |
| Tennesse color 200g | 22.500 | 6.672 | 2.000 | 900 | 2.824 | **10.104** | **44,9%** |
| Tennesse transp. 200g | 12.900 | 5.335 | 2.000 | 516 | 1.619 | **3.430** | **26,6%** |
| **Vela cuenco 100g** | **8.500** | **4.790** | **2.000** | **340** | **1.067** | **303** | **3,6%** |

### Los tres problemas que se ven acá

**1 · La vela cuenco no deja plata.** $303 por unidad. Vender cien te deja
$30.300, que es menos de lo que cuesta un mes de tienda online. Es la única de
la lista que hay que tocar sí o sí.

**2 · El contenedor cuesta más que la cera.** El cuenco de 100 g cuesta $4.790 y
la Tennesse de 200 g cuesta $5.335. La mitad de producto por casi el mismo
costo: lo que estás pagando es el envase. La consecuencia práctica es que
**bajar el gramaje no baja el costo**, y por eso los productos chicos son los
que peor margen tienen. Si querés una línea de entrada barata, tiene que ser
barata *de contenedor*, no de cera.

**3 · Tres velas distintas al mismo precio.** Torre, Bubble y Arco valen las
tres $20.500 con costos de $2.965, $3.700 y $4.206. El precio no está construido
sobre el costo: está puesto a ojo. Funciona mientras el margen sea grande, pero
esconde cuál te conviene empujar. Hoy la Torre te deja $1.241 más que el Arco
por el mismo trabajo de venta.

---

## 3 · Cuánto deja cada vela — mayorista

Packaging al 2% (más simple), comisión al 2,42%.

| Producto | Cant. | Precio | Insumos | M. obra | Pack. | Com. | **Contribución** | **%** |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Tennesse color 200g | x25 | 11.990 | 6.672 | 2.000 | 240 | 290 | **2.788** | **23,3%** |
| Arco 200g | x10 | 8.500 | 4.206 | 2.000 | 170 | 206 | **1.918** | **22,6%** |
| Bubble 200g | x10 | 7.500 | 3.700 | 2.000 | 150 | 182 | **1.468** | **19,6%** |
| Tennesse transp. 200g | x25 | 8.900 | 5.335 | 2.000 | 178 | 215 | **1.172** | **13,2%** |
| Torre vertical 140g | x10 | 6.000 | 2.965 | 2.000 | 120 | 145 | **770** | **12,8%** |
| Vela nudo 60g | x25 | 4.000 | 1.340 | 2.000 | 80 | 97 | **483** | **12,1%** |

El mayorista está calculado con un markup del 100% sobre insumos —eso es
coherente en toda la planilla— pero el markup se calculó **antes de sumar la
mano de obra**. Cuando la sumás, la mitad de la lista queda entre 12% y 13%.

Un 12% de contribución en un negocio con esta inflación no alcanza para reponer
el insumo del mes siguiente. Es producir para financiar al proveedor de cera.

---

## 4 · La regla de descuento rompe dos productos

La planilla autoriza «hasta 60%» y «hasta 65%» de descuento sobre el precio de
lista. Aplicado, contra insumos + mano de obra solamente:

| Producto | Lista | Con 65% off | Insumo + m. obra | **Resultado** |
|---|---:|---:|---:|---:|
| Torre vertical 140g | 20.500 | 7.175 | 4.965 | +2.210 |
| Arco 200g | 20.500 | 7.175 | 6.206 | +969 |
| **Tennesse color 200g** | 22.500 | 7.875 | 8.672 | **−797** |
| **Vela cuenco 100g** | 8.500 | 2.975 | 6.790 | **−3.815** |

Los dos últimos venden por debajo del costo. Y todavía no descontamos packaging
ni comisión.

> **El descuento máximo no puede ser un porcentaje único para todos los
> productos.** Tiene que ser un piso en pesos, calculado por producto: el precio
> por debajo del cual no se vende, y punto.

---

## 5 · Cuánto hay que vender para no poner plata

Costos fijos del mes, según `CASABRUMA - datos`:

| | |
|---|---:|
| Tienda online (mayorista + minorista) | 50.000 |
| Mejoras de la tienda | 10.000 |
| Publicidad | 100.000 |
| **Total** | **160.000** |

No incluye la línea de teléfono (sin definir) ni ningún retiro para vos.

| Canal | Contribución promedio | **Unidades/mes para empatar** |
|---|---:|---:|
| Minorista | 8.209 | **20** |
| Mayorista | 1.433 | **112** |

Veinte velas al mes contra ciento doce. **Cinco veces y media más producción
para el mismo resultado.**

Y eso es solo empatar. Para que Casa Bruma te pague algo a vos, sumá tu retiro
al numerador: si querés sacar $300.000 por mes, el minorista pasa a 57 unidades
y el mayorista a 321.

---

## 6 · La tensión que hay que resolver

Las planillas de enero describen un negocio, y el Notion y el resto de esta
carpeta describen otro:

| | Planillas (enero) | Notion y `01-base.md` (septiembre) |
|---|---|---|
| Qué se vende | Velas y difusores en volumen | Piezas únicas numeradas |
| A quién | Emprendedoras que revenden | Consumidora final |
| Cantidad | Packs de 10, 25, 50, 100, 200 | Drops de 6 a 10 |
| Argumento | Mínimo bajo, márgenes para el revendedor | Escasez y criterio |
| Precio | Es el argumento | «El precio no es el argumento» |
| Contribución | 12% a 23% | 45% a 61% |

No son dos etapas de lo mismo: son dos negocios con economías opuestas. El
mayorista pide volumen, stock y publicidad constante. El de piezas únicas pide
poca producción y un margen que aguanta la inflación.

**Los números dicen lo mismo que el branding.** El modelo de drops es el que
cierra: 20 unidades al mes en vez de 112, sin stock muerto y sin depender de los
$100.000 de publicidad para mover volumen.

Eso no obliga a matar el mayorista mañana. Obliga a decidir qué es cada cosa:

- **Si el mayorista se queda**, tiene que dejar de ser el negocio y pasar a ser
  producción de fondo, con precios recalculados con la mano de obra adentro y un
  mínimo real de contribución (30%, no 12%). Y con su propia identidad: el
  mayorista no puede usar el packaging ni el discurso de escasez, porque son
  contradictorios.
- **Si el mayorista se va**, se liberan los $25.000 de la tienda mayorista y
  buena parte de la publicidad, y la estructura fija baja de $160.000 a algo
  cercano a $60.000. El punto de equilibrio pasa de 20 unidades a 8.

---

## 7 · Lo que hay que hacer, en orden

1. **Poner un piso en pesos por producto.** Reemplaza a la regla de «hasta 65%».
   Ninguna venta por debajo de insumos + mano de obra + 30%.
2. **Sacar o rehacer la vela cuenco.** O sube a un precio con margen, o cambia el
   contenedor, o sale de la lista. A $8.500 es trabajo gratis.
3. **Recalcular todos los precios con la mano de obra adentro.** El markup del
   100% sobre insumos es el error de origen de toda la tabla mayorista.
4. **Actualizar los costos de insumos a hoy.** Son de enero; ya no valen eso.
5. **Decidir qué pasa con el mayorista.** Es la decisión que más plata mueve de
   todas las de esta lista.
6. **Escribir el acuerdo con Luis.** Ver abajo.

---

## 8 · La sociedad

`INVERSIONES-GASTOS Y DETALLE` registra:

| Quién | Fecha | Concepto | Monto |
|---|---|---|---:|
| Luis | Noviembre | Inicial | 400.000 |
| Luis | 12/1/26 | Reposición | 100.000 |
| **Belu** | — | — | **(vacío)** |

Medio millón de pesos puestos por una sola persona, sin nada escrito sobre qué
es eso. Un aporte de capital, un préstamo y un regalo se parecen mucho al
principio y no se parecen en nada cuando el negocio empieza a facturar.

**Hay que definir tres cosas, por escrito, antes de la primera venta grande:**

1. **Qué es la plata de Luis** — capital que da participación, préstamo que se
   devuelve, o aporte familiar sin contrapartida.
2. **Cuánto vale tu trabajo** — si vos ponés la mano de obra, el diseño, el
   contenido y la venta, eso es un aporte y tiene que estar valuado. Que no haya
   entrado plata tuya no significa que no hayas aportado.
3. **Cómo se reparte** — y cuándo. Si primero se recupera el capital y después se
   reparte, o si se reparte desde el peso uno.

No hace falta una sociedad formal para esto. Alcanza un documento de dos
carillas firmado por los dos. Lo caro no es hacerlo: es discutirlo dentro de dos
años sin nada escrito.

---

## Supuestos — qué está confirmado y qué no

| Dato | Estado |
|---|---|
| Costos de insumos por unidad | ✅ De la planilla, enero 2026 |
| Precios mayorista y minorista | ✅ De la planilla, enero 2026 |
| Comisión Mercado Pago 12,55% | ✅ De la planilla |
| Comisión mayorista 2% + IVA | ✅ De la planilla |
| Costos fijos $160.000/mes | ✅ De la planilla |
| Aportes de Luis | ✅ De la planilla |
| **Mano de obra $2.000/unidad** | ⚠️ Está en la planilla pero sin unidad de medida — **confirmar si es por unidad o por tanda** |
| **Packaging 4% / 2%** | ⚠️ Es la regla de `05-packaging.md`, no un costo medido — **falta el número en pesos** |
| **Ventas reales por mes** | ❌ No hay dato en ningún lado |
| **Mix de productos** | ❌ Los promedios de la sección 5 son simples, no ponderados |
| **Situación fiscal** | ❌ Sin dato — cambia todos los números si hay IVA de por medio |
| **Costo de envío y quién lo paga** | ❌ `04-identidad-verbal.md` dice $6.000 Andreani; falta si se cobra o se absorbe |

Los cuatro que faltan son los que convierten esto de un diagnóstico en un
tablero. Los tres primeros se contestan de memoria; el fiscal lo confirma un
contador.
