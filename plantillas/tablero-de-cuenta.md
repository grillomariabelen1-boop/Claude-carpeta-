# Tablero de cuenta: instrucciones para Claude

Copiá este archivo entero en una sesión nueva de Claude Code, uno por cliente. Antes, completá los datos del cliente en la sección **"Datos del cliente"**. Claude arma el tablero como artifact, le carga los datos y te pasa el link.

---

## Qué tenés que hacer, Claude

Armá un **artifact** (una página HTML publicada con la herramienta Artifact) que sirva de **tablero de trabajo** para la cuenta publicitaria de este cliente. El dueño de la cuenta lo usa para:

1. no perderse con los cambios y sus fechas;
2. ordenar las tareas por etapa;
3. entender cuánto hay que facturar, vender y pautar para llegar al objetivo;
4. ver cómo está armada la cuenta de Meta y cómo viene cada mes.

### Reglas de trabajo

- Todo en **español de Argentina**, con voseo y frases cortas. Nada de jerga técnica sin explicar.
- **No inventes datos.** Si falta un número, dejalo vacío y avisá qué falta. Si algo es una estimación, marcalo como "aproximado" en la nota de esa fila.
- Antes de armar, **pedí los datos que falten** (ver "Qué pedirle al usuario"). Si no los tiene, armá igual con lo que haya.
- Guardá los datos en la capacidad **`db`** del artifact (no en localStorage), así el usuario los ve desde cualquier dispositivo y vos los podés leer y actualizar después.
- Los datos iniciales se cargan con la herramienta **ArtifactData** después de publicar, nunca escritos en el HTML.
- Al terminar, hacé una lectura de control de una colección y pasale al usuario el link y en una línea qué cargaste y qué quedó aproximado.
- Si existe `village-polo-club/tablero-village.html` en el repositorio, usalo como base: cambiá el título, la marca, los textos y las referencias del cliente.

---

## Datos del cliente (completar antes de pegar)

- **Cliente / marca:**
- **Rubro y producto principal:**
- **Tienda online (plataforma y URL):**
- **Objetivo de facturación mensual:**
- **Margen aproximado** (si no se sabe, usar un supuesto del rubro y marcarlo):
- **Presupuesto mensual de pauta actual:**
- **Campañas activas en Meta** (nombre, conjuntos, presupuesto diario de cada uno):
- **Cupones o promos activas:**
- **Cambios recientes en la cuenta, con fecha:**
- **Tareas o pendientes que ya conocés:**

---

## Qué pedirle al usuario si no lo pegó

1. **Meta Ads:** exportación del Administrador de anuncios del último mes y de los últimos 7 días, a nivel campaña, conjunto y anuncio (CSV). Columnas: gasto, compras, valor de conversión, agregados al carrito, clics en el enlace, CPM, CPC, alcance, frecuencia, nombre del conjunto.
2. **Tienda:** visitas, ventas, facturación y ticket promedio del último mes y del anterior (captura del panel de estadísticas o exportación de ventas).
3. **Margen** o, si no lo tiene, el rubro para usar un supuesto.
4. **Objetivo** de facturación mensual.

---

## Cómo calcular (calculadora)

**Facturación = visitas que compran × conversión × ticket promedio**

- **Visitas que compran:** las visitas totales de la tienda **menos** las que trae una campaña de tráfico o de perfil, que casi no compran. Restá los clics de esa campaña.
- **Conversión real:** ventas ÷ visitas que compran.
- **Visitas pagas necesarias** = (ventas necesarias ÷ conversión) − visitas no pagas (orgánico, mails, directo).
- **Pauta necesaria** = visitas pagas × costo por visita (gasto de la campaña de ventas ÷ clics en el enlace).
- **Costo por venta máximo** = ticket × margen.
- **Costo por venta objetivo** = ticket × (margen − 15 puntos).
- **Queda después de la pauta** = facturación × margen − pauta. Semáforo: verde si queda 10% o más, amarillo entre 0 y 10%, rojo si es negativo.

La calculadora tiene campos editables (objetivo, ticket, conversión %, visitas no pagas, costo por visita, margen %) que se guardan solos, y dos botones: **"Cargar mes real"** (con los datos del último mes) y **"Cargar objetivo"**.

---

## Estructura de la página

**Arriba, siempre visible (tres indicadores):**
- **Último cambio en la cuenta:** fecha, hace cuántos días, y "esperá antes de volver a tocar" si pasaron menos de 3 días.
- **Próxima revisión:** el cambio con fecha de revisión más cercana sin resultado cargado.
- **Tareas:** abiertas, en curso y hechas.

**Cuatro pestañas** (navegación con `#bitacora`, `#tareas`, `#calculadora`, `#cuenta`):

1. **Bitácora** (la pestaña principal). Formulario: fecha (hoy por defecto), dónde (lista: Meta · Prospecting, Meta · Retargeting, Meta · Testeo, Meta · Tráfico, Meta · General, Creativos, Web / Tienda, Cupones y promos, Google Ads, Mails, Otro), qué se cambió, por qué, revisar el (fecha), qué pasó. Lista de más nuevo a más viejo, con etiqueta "Revisar ya" cuando llega la fecha y "Revisado" cuando tiene resultado. Regla escrita arriba: cada conjunto se toca como mucho una vez cada 3 o 4 días, salvo para apagar algo que no funciona.
2. **Tareas** en cuatro etapas: **1 · Conversión y ticket**, **2 · Creativos nuevos y UGC**, **3 · Escalar pauta**, **4 · Fecha fuerte** (Navidad, Hot Sale, Día del Padre, etc., según el cliente). Cada tarea tiene estado (pendiente → en curso → hecha, se cambia tocando la etiqueta) y quién.
3. **Calculadora**, según la sección anterior.
4. **Cuenta y meses:**
   - Tabla de estructura de Meta: campaña, conjunto, qué lleva, presupuesto por día, estado (activo / apagado), con total activo por día y por mes.
   - Tabla mes a mes: visitas, ventas, conversión, ticket, facturación, gasto en Meta, ROAS real (facturación de la tienda ÷ gasto) y % del objetivo.

Todas las listas permiten **agregar, editar en el lugar y borrar** (con confirmación dentro de la página, sin `confirm()`).

---

## Datos en `db`

| Colección / documento | Campos |
|---|---|
| `bitacora` | fecha (AAAA-MM-DD), area, cambio, motivo, revisar, resultado, creado |
| `tareas` | titulo, etapa ("1" a "4"), estado ("pendiente", "en curso", "hecha"), quien, creado |
| `estructura` | campania, conjunto, contenido, presupuesto (número), estado, orden |
| `meses` | mes (AAAA-MM), visitas, ventas, facturacion, gasto, nota |
| `config/calc` | objetivo, ticket, conversion, organicas, cpv, margen |

Publicar con `capabilities: {db: {}}`. Escuchar cada colección una sola vez con `onSnapshot`, con un aviso a los 10 segundos si no conecta. Guardar la calculadora con una espera de ~1 segundo después de escribir.

## Qué cargar al principio

- **Bitácora:** los cambios recientes que pasó el usuario, con su fecha. Si la fecha es dudosa, ponelo en "por qué" como "fecha aproximada".
- **Tareas:** las del plan para este cliente. Si no hay plan, estas por defecto:
  - Etapa 1: compra de prueba hasta pagar; revisar segmentación y CPM de cada conjunto; confirmar margen real; ideas para subir el ticket (packs, combos, envío gratis como meta).
  - Etapa 2: elegir 3 ángulos según las trabas reales del cliente; guiones; brief para creadores UGC; iterar el anuncio ganador.
  - Etapa 3: simplificar la cuenta a pocos conjuntos; subir pauta 20–25% por semana mientras el costo por venta real esté dentro del objetivo; Google Ads con conversión de compra.
  - Etapa 4: creativos y mails para la próxima fecha fuerte; fecha límite de envío.
- **Estructura:** las campañas y conjuntos actuales con su presupuesto.
- **Meses:** los meses con datos reales de la tienda.
- **`config/calc`:** el objetivo del cliente y los supuestos.

## Diseño

Página de trabajo, sobria y clara. Colores de la marca del cliente si se conocen (si no, neutros con un acento). Tipografía legible, números alineados (`tabular-nums`), modo claro y oscuro, y que funcione en el celular. Título de la página: "[Marca] a $[objetivo]" o el nombre que pida el usuario.
