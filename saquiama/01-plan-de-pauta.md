# Plan de pauta: Saquiama

## La idea central

> **Con un ROAS de 20, el riesgo no es no crecer. El riesgo es romper lo que ya
> funciona.**

Una cuenta que rinde 20 veces lo que gasta no necesita una reestructura. Hay
que entender por qué rinde y cuidarlo. Lo nuevo se prueba de a una cosa por vez
y en un espacio chico.

---

## 0 · Cómo está la cuenta hoy

> **Una sola campaña, con todos los anuncios juntos. Sin públicos
> personalizados, sin retargeting, sin segmentación.**

Parece desprolijo, pero **no está mal armado para este presupuesto**. Es casi la
estructura que conviene: una campaña sola junta todas las ventas y Meta aprende
rápido. No hay que "profesionalizarla" agregando campañas.

Tiene tres puntos ciegos, y ninguno se arregla tocando la campaña:

| Qué pasa | Por qué importa | Qué hacer |
|---|---|---|
| **No hay públicos creados** | No se puede saber si le vende a clientas nuevas o a las 120.000 seguidoras que ya iban a comprar. Es la pregunta clave del ROAS de 20 | Crear los públicos y cargarlos en la configuración de la cuenta, como "clientas existentes" y "audiencia interactuada". **No toca la campaña**: solo habilita el reporte. Ver abajo |
| **Todos los anuncios están juntos** | Meta pone casi toda la plata en 2 o 3 anuncios y el resto no recibe nada. El ROAS de 20 probablemente sale de esos pocos | Mirar cómo se reparte la inversión por anuncio. **No apagar ni borrar nada** |
| **Los anuncios nuevos se suben a la misma campaña** | Cada anuncio nuevo compite con los ganadores y puede reiniciar el aprendizaje. Así no se sabe si un video nuevo es bueno o si no lo dejaron salir | Probar los videos nuevos en una campaña de testeo aparte. Ver sección 3 |

### Los públicos a crear (semana 1, riesgo cero)

No son para segmentar: la campaña sigue en público amplio. Sirven para
**medir** y, más adelante, para **excluir**.

| Público | Fuente |
|---|---|
| Compradoras de la web, 180 días | Píxel: Purchase |
| Visitantes de la web, 30 y 180 días | Píxel: todo el tráfico |
| Interactuaron con @saquiama, 365 días | Instagram: cuenta profesional |
| Lista de clientas | Un CSV de mails y teléfonos, si la marca lo tiene (web y showroom) |

Después, en la **configuración de la cuenta publicitaria**, se cargan como
"clientas existentes" (compradoras y lista) y "audiencia interactuada"
(visitantes e interacciones). Desde ahí el reporte muestra qué parte de las
ventas viene de cada grupo.

### Retargeting: todavía no

Con USD 10 por día, no se abre una campaña de retargeting. La campaña amplia ya
les muestra los anuncios a las seguidoras, y probablemente de ahí sale buena
parte del ROAS. Se reconsidera solo si el reporte muestra que la pauta casi no
llega a la gente caliente.

---

## 1 · Primero entender el ROAS de 20 (semana 1)

Un ROAS de 20 es muy alto para moda. Puede ser real, pero antes de prometer que
lo sostenés tenés que saber de dónde sale. Hay tres explicaciones posibles y no
se excluyen:

| Hipótesis | Cómo se chequea |
|---|---|
| **Le vende a gente que ya iba a comprar.** 120.000 seguidoras más retargeting: Meta se atribuye ventas que igual hubieran pasado | Mirá qué porcentaje de las ventas viene de clientas existentes o de seguidoras. En Advantage+ está el reporte por tipo de audiencia (nueva, interactuó, clienta existente) |
| **La ventana de atribución es generosa.** Con "1 día de visualización" se cuenta como venta a quien vio el anuncio y después compró por otro camino | Compará el ROAS con "7 días de clic" solo contra "7 días de clic y 1 de visualización" |
| **Las compras se cuentan doble.** El píxel y la API de conversiones mandan el mismo evento sin deduplicar | En el Administrador de eventos: el evento Purchase tiene que tener `event_id` y la cobertura tiene que decir que deduplica. Además, las compras que reporta Meta tienen que ser **iguales o menos** que las reales de la web |

**El número que importa es el MER:** las ventas totales de la web dividido la
inversión total en pauta. No depende de cómo atribuye Meta. Si el ROAS dice 20 y
el MER da 6, tu base real es 6, y conviene saberlo antes de que te midan.

### Qué exportar del Business Manager

- Los últimos 90 días, por campaña, conjunto y anuncio: inversión, compras,
  valor de compra, ROAS, CPM, CTR y frecuencia.
- Los 10 anuncios que más vendieron: ¿son todos videos de la dueña? ¿Cuánto
  hace que están activos?
- La configuración de cada campaña: objetivo, tipo (Advantage+ o manual),
  presupuesto, públicos y ventana de atribución.

---

## 2 · Las reglas para tomar la cuenta

1. **Dos semanas sin tocar nada de lo que vende.** Ni presupuesto, ni público,
   ni anuncios. Solo mirar.
2. **Nunca apagues un anuncio que vende para "ordenar".** Si está viejo pero
   rinde, queda.
3. **Los cambios de presupuesto, de a 20% como máximo** y no más de una vez
   cada 3 o 4 días. Los saltos grandes reinician el aprendizaje.
4. **Un cambio por vez**, así sabés qué movió el número.
5. **Lo nuevo se prueba aparte**, en una campaña de testeo con presupuesto
   propio y nunca adentro de la que vende.

---

## 3 · Estructura: pocas campañas

Con USD 10 por día, el problema es la fase de aprendizaje. Meta necesita unas
**50 compras por semana en un mismo conjunto** para salir de ahí.

Con un ticket de $80.000 y ROAS de 20, cada venta cuesta unos **$4.000 ARS**.
Con USD 10 diarios, según el dólar, salen unas 2 o 4 ventas por día, o sea unas
15 a 25 por semana. **Ni siquiera un conjunto solo llega a 50.** Si partís el
presupuesto en cinco campañas, cada una junta 4 ventas y ninguna aprende.

### Propuesta

| Campaña | % | USD/día | Qué hace |
|---|---|---|---|
| **Ventas principal.** Lo que ya funciona, o Advantage+ de ventas si todavía no existe | 80% | 8 | Los 4 a 6 mejores anuncios. Acá está la plata |
| **Testeo de creativos** | 20% | 2 | 2 o 3 anuncios nuevos por semana. El que le gana a los de la principal pasa a la principal |

- **Sin campaña de retargeting aparte.** Con 120.000 seguidoras y este
  presupuesto, Advantage+ ya le muestra los anuncios a la gente caliente.
  Separarla fragmenta los datos.
- **Público amplio:** mujeres de Argentina (o las zonas donde envían), sin
  intereses. La segmentación la hace el creativo: si en el video aparece una
  mujer de 40, Meta encuentra mujeres de 40.
- **Edad:** si usás Advantage+, ponela como sugerencia, no como límite duro.
  Dejá que Meta encuentre compradoras de 55 si las hay.
- **Ubicaciones automáticas.** Para 40 a 50 años, **Facebook no es relleno**:
  es donde está buena parte de ese público. No lo saques.
- **Límite para clientas existentes** (una opción de Advantage+): empezá en
  20–30%. Si el reporte de la semana 1 muestra que casi todo es gente que ya
  compraba, esto obliga a buscar clientas nuevas.

**En la práctica:** la campaña que ya existe *es* la principal y no se toca. Lo
único que se agrega es la de testeo. El 20% sale de subirle presupuesto a la
cuenta o de bajarle a la principal de a poco, nunca de golpe.

---

## 4 · Creativos: lo que ya sabemos

> **Funcionan los videos orgánicos de la dueña.** No hay que "mejorarlos"
> haciéndolos más producidos. Hay que hacer más de eso.

La gente de 30 a 50 compra ropa online cuando se imagina con la prenda puesta y
confía en quien se la vende. La dueña hablando le da las dos cosas.

### Cómo usarlos

- **Anuncios desde publicaciones existentes** (usando el ID de la
  publicación). Así los likes y comentarios del orgánico quedan en el anuncio.
  La prueba social se acumula en vez de empezar de cero.
- **Los reels orgánicos son tu laboratorio gratis.** El que rinde mejor orgánico
  en 48 horas pasa a la campaña de testeo.

### Qué pedirle a la marca, por semana

Tres videos nuevos, cada uno probando **una sola cosa distinta**:

| Ángulo | Ejemplo de primer segundo |
|---|---|
| **Talle real** | "Mido 1,60 y uso talle 42, así me queda" |
| **Un look, tres ocasiones** | La misma prenda para oficina, almuerzo y salida |
| **Problema del cuerpo** | "Si no te gusta mostrar los brazos, mirá esta manga" |
| **Detalle de calidad** | Primer plano de la tela, las costuras, el forro |
| **Showroom** | Clientas probándose ropa: prueba social en vivo |
| **Respuesta a un comentario** | "Me preguntaron si esto le queda a alguien con cadera" |

Reglas para todos:

- **Primer segundo = la prenda puesta**, nunca un logo ni una intro.
- **Mujeres de la edad del público.** Si modela alguien de 25, el anuncio le
  habla a alguien de 25.
- **Precio y cuotas en el copy o en pantalla.** Con un ticket de $80.000, las
  cuotas sin interés son parte del mensaje.
- Formato 9:16, subtitulado, porque mucho se mira sin sonido.

### Cuándo cambiar un anuncio

Por **fatiga**, no por antigüedad: frecuencia mayor a 3 en 7 días **y** el CTR
o el ROAS bajando dos semanas seguidas. Si no pasan las dos cosas, se queda.

---

## 4b · Cómo escalar los ganadores

> **Con USD 300 fijos, escalar no es gastar más. Es sacar más ventas del mismo
> presupuesto y conseguir los argumentos para que la marca lo suba.**

Hay tres palancas, en este orden.

### Palanca 1 · Escalar el creativo (la principal)

**Lo que gana no es el archivo, es la idea**: el primer segundo, el ángulo, quién
habla, cómo muestra la prenda. De un ganador salen 4 o 5 versiones cambiando
**una sola cosa por vez**:

| Qué se cambia | Ejemplo |
|---|---|
| **El gancho** (los primeros 3 segundos) | El mismo video con otro arranque: la prenda puesta, una pregunta o el precio en pantalla |
| **La prenda** | El mismo guion, la misma forma de filmar, otro producto |
| **Quién la usa** | La dueña, una clienta del showroom, otro cuerpo, otra edad |
| **El largo** | Una versión de 15 segundos y otra de 30 |
| **El formato** | Un fotograma del video como imagen fija, o un carrusel con las prendas que aparecen |
| **El texto del anuncio** | Otro enfoque: talle, ocasión, precio y cuotas, calidad |

Esto es lo que se le pide a la marca cada semana: **no videos nuevos al azar,
sino variaciones del que ganó.** Los ganadores se gastan con el tiempo (sube la
frecuencia y baja el rendimiento). Las variaciones los reemplazan antes de que
eso pase.

### Palanca 2 · Pasar el ganador a la campaña principal

**Qué cuenta como ganador** en la campaña de testeo:

- Gastó al menos lo que cuestan 2 o 3 ventas. Menos que eso es suerte.
- ROAS igual o mayor al promedio de la principal, **en 7 días**, no en un día bueno.
- El CTR y el costo por compra acompañan. Una sola venta grande no alcanza.

**Cómo pasarlo:**

- Se sube **con el mismo ID de publicación**, así se lleva los likes y
  comentarios que juntó.
- **Una vez por semana, todos juntos.** Cada cambio en la principal la mueve un
  poco, así que conviene cambiar una vez y no cinco.
- **No se apaga ningún anuncio de la principal para hacerle lugar.** Si el nuevo
  es mejor, Meta solo le va a pasar la plata.

### Palanca 3 · Subir el presupuesto (necesita el OK de la marca)

**El argumento:** si un peso invertido devuelve 20 (o 6, o lo que dé el MER
real), el límite de ventas hoy es el presupuesto, no los anuncios.

**Cómo proponerlo sin riesgo:**

1. Primero calcular el MER real (sección 1). Con eso se sabe cuánto margen hay.
2. Proponer una prueba acotada: **+20% por 2 semanas**. Si el MER se sostiene,
   otro +20%. Si cae, se vuelve atrás.
3. **Nunca subir de golpe.** Los saltos grandes reinician el aprendizaje y el
   ROAS se desploma unos días, que es justo cuando la marca se asusta.

**Qué esperar:** el ROAS **va a bajar** al subir el presupuesto, y es normal. Los
primeros pesos llegan a las compradoras más fáciles y los siguientes a gente
más fría. La pregunta no es si el ROAS baja. Es si **cada peso extra sigue dando
ganancia**. Hay que avisarlo antes de subir, no después.

### Lo que no se hace

- **Duplicar la campaña o el conjunto ganador** para "escalar
  horizontalmente". Con este presupuesto parte los datos y las dos copias
  compiten por la misma gente.
- **Segmentar por intereses** para "encontrar público nuevo". El público lo
  encuentra el creativo, no la segmentación.
- **Tocar el anuncio ganador** para "mejorarlo" (texto, botón). Se reinicia y
  pierde lo aprendido. Las mejoras van en una variación aparte.

### Cuándo frenar

- La frecuencia pasa de 3 y el CPM sube: la gente ya lo vio.
- El % de clientas nuevas cae: la pauta está reciclando seguidoras.
- El MER baja dos semanas seguidas aunque el ROAS de Meta se vea bien.

---

## 5 · El tablero semanal

| Métrica | Para qué | Señal de alarma |
|---|---|---|
| **MER** (ventas totales web / inversión) | El número real del negocio | Cae dos semanas seguidas |
| ROAS en Meta | Comparar anuncios entre sí | — |
| Costo por compra | Salud de la campaña | Sube más de 30% |
| % de clientas nuevas | Si la pauta trae gente o recicla | Menos del 40% |
| CTR del enlace | Si el creativo engancha | Menos de 1% |
| Tasa de conversión web (compras / visitas) | Si la web frena la venta | Menos de 1%. Ver [`02-web-mejoras.md`](02-web-mejoras.md) |
| Frecuencia (7 días) | Fatiga | Más de 3 |

---

## 6 · Cómo te conviene que te midan

Todavía no está definido. Propuesta para llevarle a la marca:

- **No aceptes que te midan por el ROAS de Meta.** Si arrancás con un 20
  inflado y lo corregís (deduplicando o ajustando la atribución), va a parecer
  que empeoraste aunque el negocio esté igual o mejor.
- **Proponé el MER y las ventas totales de la web** de los 3 meses anteriores
  como línea de base, medidos mes a mes.
- **Aclarás que USD 300 es un presupuesto de mantenimiento.** Sirve para
  sostener, no para escalar. Si quieren crecer, el paso siguiente es subir el
  presupuesto de a 20% mientras el MER se sostenga.

---

## 7 · Primeros 30 días

| Semana | Qué hacer |
|---|---|
| **1** | Pedir accesos. Exportar datos. **Crear los públicos y cargarlos en la configuración de la cuenta.** Chequear la deduplicación del píxel y de la API de conversiones. Calcular el MER. Pedir la URL y auditar la web. **No tocar campañas** |
| **2** | Diagnóstico con los datos: qué anuncios venden, cuánto es de clientas nuevas. Pedir los primeros 3 videos. Presentar la propuesta de medición |
| **3** | Armar la campaña de testeo (20%) con los 3 videos nuevos. La principal queda igual |
| **4** | Primer informe: MER, ganadores del testeo, propuesta de mejoras web. Pasar el mejor creativo nuevo a la principal |
