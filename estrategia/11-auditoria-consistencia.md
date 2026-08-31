# Auditoría de consistencia — 31/8

Revisión completa de los 21 archivos del repositorio buscando **contradicciones
internas**: lugares donde un documento sigue diciendo una cosa que otro ya
corrigió.

## Por qué hacía falta

El 30/8 los datos reales dieron vuelta el supuesto central del plan
([`10-datos-reales.md`](10-datos-reales.md)): de **haul-first** a
**color-first**. Ese giro se aplicó a los documentos principales, pero quedaron
restos del plan viejo repartidos por el resto de los archivos —y, en algunos
casos, adentro de documentos cuyo propio encabezado decía "actualizado".

Un plan que se contradice a sí mismo no se ejecuta: cuando llega el martes a la
mañana y hay que decidir qué grabar, dos instrucciones opuestas se resuelven
haciendo lo de siempre.

---

## Lo que se detectó

**14 inconsistencias y 4 huecos.** Ordenadas por costo: arriba las que te
hubieran hecho grabar el video equivocado.

### Críticas — te mandaban a grabar hauls

| # | Dónde | Qué decía | Qué dice ahora |
|---|---|---|---|
| 1 | `03-formatos.md` | **"1. Haul — MOTOR"**, *"el que históricamente mejor performa"*, **2-3 por semana** | Haul es el formato 11 y es **marginal**: máx. 1 cada 2 semanas |
| 2 | `04-calendario` → distribución total | Haul **13 posteos (43%)**, "motor 63%" | Haul **1 de 30 (3%)**, y opcional. Tabla rehecha por slot y por carril |
| 3 | `04-calendario` → semana 5 | *"Si el ganador es el haul —lo más probable—"* | El ganador probable es la fórmula del color, que es la que tiene evidencia |
| 4 | `04-calendario` → semana 0 | "Grabar en bloque **2 hauls completos**" | Colchón de 5: 2 fórmula de color, 2 guía de compra, 1 bajitas |
| 5 | `05-metricas.md` → escenario C | *"Publicar **5 hauls seguidos** en 5 días"* | 5 videos de la fórmula del color, un color distinto cada día |
| 6 | `05-metricas.md` → después de la salida | "bajar hauls a 40%" | Bajar color de 45% a 35%; los hauls ya no tienen porcentaje |

Las seis apuntaban en la misma dirección: **el documento que te dice qué grabar
cada día seguía siendo el plan viejo**, aunque su encabezado dijera lo
contrario.

### De números — tres repartos distintos conviviendo

| # | Dónde | El conflicto | Resolución |
|---|---|---|---|
| 7 | `07-pilares` vs `10-datos` | Autoridad **40%** vs Autoridad **45%** vs "color 40% + vida y bajitas 25%" | Son el mismo reparto con **bajitas (5%) contado de distinto lado**. Queda canónico: **45 / 20 / 20 / 15**, bajitas en Autoridad |
| 8 | `07-pilares` | *"el 60% de los videos tiene que tener forma de haul"* junto a una tabla que suma 100% sin hauls | El 60% se sacó. La **estructura de revelación** se aplica a todos los formatos motor y no lleva porcentaje propio |
| 9 | `banco-de-ideas/README` | Consumo **40% "el motor"**, autoridad **20% "el ancla"** | Autoridad 45% (el motor), guía de compra 20%, vida 20%, proceso 15% |
| 10 | `00-contexto.md` | "la asesoría de imagen baja a un **20%**" | El carril de Autoridad es el **45%**. Lo que baja es la pose de experta, no el tema |
| 11 | `banco-de-ideas/03-autoridad.md` | "El **20%** que le da peso a todo lo demás" | El 45%: es el carril más grande |

### De calendario

| # | Dónde | El conflicto | Resolución |
|---|---|---|---|
| 12 | `07-pilares`, `09-perfil`, `banco/04-proceso` | Proceso arranca en la **semana 3** | **Semana 2**, como ya decía el hallazgo 9 del 30/8. Tiene el viernes fijo |
| 13 | `09-perfil.md` → Instagram | *"Durante la recuperación **no es prioridad**"* | Contradecía de plano el hallazgo 5 (IG rinde 2× y con material reciente). Todo va a las dos plataformas, siempre |
| 14 | `01-diagnostico` test 3 vs `05-metricas` test 3 | Uno contaba **videos de color**, el otro **hauls + combis**, los dos con el mismo umbral de 8 | Los dos cuentan videos de color. Los hauls quedan como dato de control |

### Estructurales

- `07-pilares-y-voz.md` tenía **dos encabezados `## Reparto`**, y el primero
  estaba vacío: el carril 4 (Proceso) quedaba colgando adentro de una sección
  de porcentajes en vez de al lado de los otros tres carriles.
- El mismo documento decía "los **tres** carriles" con cuatro carriles listados,
  y `banco-de-ideas/README.md` decía "los **tres** archivos" con cuatro.
- `03-formatos.md` se llamaba "Los seis formatos" mientras `00-contexto.md`
  listaba ocho.

---

## Los cuatro huecos

Más caro que las contradicciones: **el calendario pedía todas las semanas tres
formatos que no existían en ningún lado.** Ni ficha, ni gancho, ni plantilla.

| Hueco | Cuándo lo pedía el calendario | Qué se armó |
|---|---|---|
| **La fórmula del color** | Todos los lunes. Es el formato #1 de la cuenta | Ficha (formato 1 de [`03-formatos.md`](03-formatos.md)) + [`guion-formula-color.md`](../plantillas/guion-formula-color.md), con las 6 variantes de título y la cola de 20 colores |
| **Guía de compra** | Todos los jueves. Es el 20% del plan y lo más compartible | Ficha (formato 3) + [`guion-guia-de-compra.md`](../plantillas/guion-guia-de-compra.md) |
| **Tips para bajitas** | Ancla, miércoles por medio. Es el video #1 histórico | Ficha (formato 4) + [`guion-bajitas.md`](../plantillas/guion-bajitas.md), serializado |
| **"Le armo el look a ___"** | Todos los viernes desde la semana 2. El diferencial | Ficha (formato 9) + [`guion-le-armo-el-look.md`](../plantillas/guion-le-armo-el-look.md) |

Existía plantilla de **haul** —el formato que ahora se hace una vez cada dos
semanas— y no existía de la fórmula del color, que se hace todas las semanas.

---

## Números canónicos

De acá en adelante, cuando dos documentos digan cosas distintas, gana este
cuadro.

### Reparto por carril (durante la recuperación)

| Carril | % | Slot fijo |
|---|---|---|
| **Autoridad** — color, colorimetría, bajitas | **45%** | Lunes + miércoles |
| **Guía de compra** — tiendas, reglas, calzado | **20%** | Jueves |
| **Vida con ropa** — incluye peinados y Serie de Estilos | **20%** | Martes |
| **Proceso y publicidad** — desde la semana 2 | **15%** | Viernes |

Fuente: [`07-pilares-y-voz.md`](07-pilares-y-voz.md) → Reparto.
Bajitas cuenta en **Autoridad**.

### Cadencia

- **5 videos por semana**, lunes a viernes. Fin de semana libre.
- **Cada video va a TikTok y a Instagram.** 30 videos = 60 publicaciones.
- **Colchón de 5** grabados y sin publicar, siempre.

### Los tres formatos que sostienen la semana

1. **La fórmula del color** — lunes
2. **Guía de compra** — jueves
3. **Bajitas** (ancla) — miércoles por medio

Si un día no sabés qué grabar, es uno de esos tres.

### Lo que bajó

- **Haul:** máximo 1 cada 2 semanas, y **nunca con el código en el título**.
- **Promote:** cero, hasta cumplir los cuatro criterios de salida.

---

## Lo que sigue abierto — no es una inconsistencia, es un dato que falta

Sigue faltando lo mismo que marcaba el 30/8, y sin eso el plan no se puede
evaluar:

- **Retención a 3 segundos** de los últimos 10 videos
- **Tasa de finalización** de los últimos 10 videos

Están en TikTok → Analytics, por video. Es el único casillero de la línea de
base de [`05-metricas.md`](05-metricas.md) que no se puede completar leyendo
este repositorio, y es el que decide si los videos de agosto fallan por gancho
o por tema.

Segundo pendiente, comercial y no de contenido: **confirmar si la colaboración
con SHEIN tiene entregables comprometidos** (cantidad de videos, fechas,
aprobación previa). De eso depende si la excepción escrita en
[`00-contexto.md`](00-contexto.md) se sostiene o hay que convertirla a afiliado.
Ver [`09-perfil-y-diferencial.md`](09-perfil-y-diferencial.md), corrección 7.
