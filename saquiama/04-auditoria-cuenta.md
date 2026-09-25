# Auditoría de la cuenta de Meta: primer corte

*Datos: exportación a nivel anuncio del 1 al 25 de septiembre de 2026
([`datos/meta-anuncios-2026-09-01_2026-09-25.csv`](datos/meta-anuncios-2026-09-01_2026-09-25.csv)).
Son 25 días, no 90, así que es una primera lectura.*

## Los números del período

| | Según Meta |
|---|---|
| Inversión | $247.615 (unos $9.900 por día) |
| Compras | 37 |
| Valor de las compras | $4.113.650 |
| ROAS | **16,6** (no 20) |
| Costo por compra | $6.692 |
| Ticket promedio | **$111.180** |
| Anuncios con gasto | 18, todos en la misma campaña |

## 5 hallazgos

### 1 · Hay un número que no cierra: el ticket promedio
La marca dice que su ticket promedio es de **$80.000**. Meta dice **$111.180**,
un 39% más. Además hay dos compras llamativas, las dos en anuncios de un pantalón
que sale $49.500:

- "Pantalon Fran": **1 compra de $374.000**
- "Pantalon Fran Video": **1 compra de $297.500**

Pueden ser clientas que compraron mucho de una vez, o pueden ser las compras
que Meta cuenta de más. **Es lo primero que hay que preguntarle a la marca**:
¿tuvieron en septiembre pedidos por $374.000 y $297.500? Si no, es la prueba
concreta de lo que sospechaban.

### 2 · Un solo producto sostiene la cuenta
Los anuncios del **vestido Anny** se llevan el 68% de la inversión y dan **29
de las 37 compras** (72% del valor). "Video Anny II" solo trae 16 compras
con ROAS 22.

**Riesgo:** si el Anny se agota o se cansa, la cuenta se cae. Hay que encontrar
el segundo producto ganador.

### 3 · Uno de cada cuatro pesos va a anuncios que no vendieron nada
**10 de los 18 anuncios no tuvieron ninguna venta**, y se llevaron el **26%
de la inversión** ($64.848). Los más caros:

| Anuncio | Gasto | Ventas |
|---|---|---|
| Mono alegra Publicacion | $20.764 | 0 |
| Camisero Anita | $15.010 | 0 |
| Vestido Anny IA | $8.098 | 0 |
| Vestido Alegra IA | $7.767 | 0 |

El mono Alegra tiene **tres anuncios y ninguna venta** ($23.567 en total).

### 4 · Los videos reales venden y los de IA no
Mismo producto, distinto creativo:

| Producto | Video real | Versión con IA |
|---|---|---|
| Vestido Anny | 6 ventas (ROAS 11) | 0 ventas |
| Vestido Alegra | 1 venta (ROAS 6,3) | 0 ventas |

Con pocos datos no es concluyente, pero va en la misma línea que lo que dijo
la marca: **los videos de la dueña son los que funcionan.** Por ahora no
conviene seguir invirtiendo en creativos hechos con IA.

### 5 · Con tan pocas ventas, cada anuncio chico es ruido
"Pantalon Fran" tiene ROAS 180 con **una** venta. "Liquidación" tiene ROAS 61
con 5. Con 1 a 5 ventas, un número así no dice nada. Solo "Video Anny II",
"Video Anny" y "Vestido Anny Video" tienen volumen para sacar conclusiones.

## Qué propongo con esto

1. **No tocar "Video Anny II" ni "Video Anny".** Son la cuenta.
2. **Pedir 3 o 4 variaciones del video del Anny**: mismo formato, otros colores
   y otro arranque. Ver [plan, sección 4b](01-plan-de-pauta.md).
3. **Pausar los anuncios que gastaron sin vender**, empezando por los de IA y
   los del mono Alegra. Se hace **después** de las dos semanas de observación y
   de a uno.
4. **Buscar el segundo producto:** probar videos reales, del estilo del Anny,
   con 2 o 3 productos más en la campaña de prueba.

## Lo que falta para cerrar la auditoría

- [ ] **Preguntarle a la marca:** ¿cuántas ventas web tuvieron del 1 al 25 de
      septiembre y por cuánto en total? ¿Hubo pedidos por $374.000 y $297.500?
      Con eso se compara directo con las 37 ventas y los $4,1 millones de Meta.
- [ ] Una exportación de 90 días con **impresiones, alcance, frecuencia, CTR y
      CPM**. Esta tiene solo gasto y ventas.
- [ ] La misma exportación con **"Comparar ventanas de atribución"**, para
      separar las ventas por clic de las por visualización o interacción.
