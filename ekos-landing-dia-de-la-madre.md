# Landing Ekos Yoga · Yoga + Merienda · Día de la Madre

> **Instrucciones para Claude in Chrome**
> - Construí una landing de **una sola página** siguiendo este documento, en la plataforma que te indique (por ejemplo Carrd) o como HTML/CSS si te lo piden.
> - Usá **exactamente** los textos de este documento. No inventes datos, precios, testimonios ni reseñas.
> - Todo lo que esté entre `[CORCHETES]` es un dato pendiente: dejalo visible como marcador para completarlo después.
> - **No reveles el contenido del regalito sorpresa** (no nombrar velita ni ebook en ninguna parte).
> - Diseño **mobile first**: casi todo el tráfico llega desde anuncios de Instagram en el celular.
> - Antes de publicar o de cargar cualquier pago, **pedime confirmación**.

---

## 1. Identidad visual

Basada en la invitación original de Caro: delicada, femenina, estilo "té en taza de porcelana con flores".

### Colores

| Uso | Color | Hex |
|---|---|---|
| Principal (títulos, botones) | Bordó | `#8C2F4B` |
| Principal oscuro (hover de botones) | Bordó oscuro | `#6E2239` |
| Fondo de secciones alternas | Rosa suave | `#F7EAEF` |
| Fondo general | Crema blanca | `#FFFBF8` |
| Acento suave (bordes, separadores) | Rosa empolvado | `#E8C7D2` |
| Texto | Gris cálido oscuro | `#3A2E32` |
| Texto secundario | Gris cálido | `#6B5B60` |

### Tipografías (Google Fonts)

- **Acentos en cursiva** (frases como "Un sí para vos", "Día de la Madre"): `Great Vibes` o `Parisienne`. Usarla poco, solo 1 o 2 palabras por sección.
- **Títulos**: `Cormorant Garamond` (serif elegante), peso 500 a 600.
- **Texto**: `Nunito` o `Lato`, peso 400, tamaño mínimo 16 px en celular.

### Estilo

- Mucho aire, bordes redondeados (12 a 16 px), sombras muy suaves.
- Detalle decorativo: pequeña ilustración de flores de línea fina (como la de la invitación) entre secciones.
- Botones: fondo bordó, texto blanco, redondeados, grandes y fáciles de tocar (alto mínimo 48 px).
- Fotos con bordes redondeados. Nada de stock frío: priorizar fotos reales de Ekos.

---

## 2. Datos del evento (fuente única)

| Dato | Valor |
|---|---|
| Nombre | Yoga + Merienda · Día de la Madre |
| Fecha | Sábado 24 de octubre |
| Horario | 15 a 17 h (aprox.) |
| Lugar | Ekos Yoga · Donado 2301, Villa Urquiza, CABA |
| Incluye | Clase de yoga suave para todos los niveles + merienda casera (budines, galletitas, té o café) + regalito sorpresa |
| Qué llevar | Solo ropa cómoda. Mats y todo lo demás lo pone Ekos |
| Precio individual | $55.000 |
| Precio de a dos | $85.000 (la segunda paga solo $30.000) |
| Cupo | 10 lugares (el pack de a dos ocupa 2) |
| Pago | Mercado Pago |
| WhatsApp | `[NÚMERO DE WHATSAPP DE EKOS]` |
| Instagram | `[USUARIO DE INSTAGRAM DE EKOS]` |

---

## 3. Estructura de la página

### Sección 1 · Portada (hero)

- **Fondo**: foto de Caro y Belu del piloto `[FOTO PILOTO — mientras tanto usar imagen provisoria]`, con una capa crema/rosa semitransparente para que el texto se lea bien.
- **Línea en cursiva**: *Día de la Madre*
- **Título**: Este año, regalale una tarde.
- **Subtítulo**: Una clase de yoga y una merienda en Ekos, para regalarle a mamá o para venir juntas.
- **Etiqueta**: 📅 Sábado 24/10 · 15 h · Villa Urquiza
- **Botón principal**: `Quiero mi lugar` → baja a la sección de precios (#precios)
- **Texto chico debajo del botón**: Solo 10 lugares

### Sección 2 · La idea

- **Título**: No es un objeto. Es un rato juntas.
- **Texto**: Un rato para parar, respirar y estar juntas. Sin exigencias, sin importar la edad, la flexibilidad o la experiencia.

### Sección 3 · La experiencia (fondo rosa suave)

- **Título**: Dos horas en tres momentos
- **3 tarjetas** (en celular, una debajo de la otra):
  1. **01 · Llegada** — Te recibimos con los mats listos y el espacio preparado para ustedes.
  2. **02 · Clase** — Clase suave para todos los niveles. No hace falta experiencia.
  3. **03 · Merienda** — Té, café y algo casero para merendar en una mesa linda y quedarse charlando.
- **Debajo, destacado**: 🎁 Y un regalito sorpresa para cada una.

### Sección 4 · Los detalles

Lista con íconos simples:

- 📅 **Sábado 24 de octubre**
- 🕒 **15 a 17 h** (aprox.)
- 📍 **Donado 2301, Villa Urquiza, CABA** → link a Google Maps
- 🧘‍♀️ **Qué llevar**: solo ropa cómoda. Los mats los ponemos nosotras.
- ☕ **Incluye**: clase + merienda + regalito sorpresa

### Sección 5 · Precios (id: `precios`)

- **Título**: Elegí cómo venir
- **Dos tarjetas lado a lado en compu, una debajo de la otra en celular:**

**Tarjeta A · Individual**
- Precio: **$55.000**
- Texto: Para regalar o regalarte.
- Botón: `Reservar mi lugar` → `[LINK MERCADO PAGO INDIVIDUAL]`

**Tarjeta B · De a dos** (destacada, con etiqueta "La más elegida")
- Precio: **$85.000**
- Texto destacado: **La segunda paga solo $30.000**
- Texto: Para venir con tu mamá, tu hija o quien quieras.
- Botón: `Reservar para dos` → `[LINK MERCADO PAGO DE A DOS]`

- **Texto debajo de las tarjetas**: Pagás de forma segura con Mercado Pago. Solo 10 lugares.

### Sección 6 · Para regalar

- **Línea en cursiva**: *Un sí para vos*
- **Título**: ¿Es un regalo?
- **Texto**: Reservá su lugar y te enviamos por WhatsApp una gift card digital para que se la entregues el domingo 18. El 24 la esperamos en Ekos.
- `[CONFIRMAR CON CARO: cómo y cuándo se envía la gift card]`

### Sección 7 · Quién te recibe

- **Foto**: Caro, real, con luz natural `[FOTO DE CARO]`
- **Título**: Quién te recibe
- **Texto** (respetar tal cual):

> Soy Caro. Me recibí de profesora de yoga a los 24, y después la vida siguió su curso: la familia, otras realidades.
>
> Cuando volví a mi práctica descubrí un cuerpo ni mejor ni peor, sino diferente, con una historia que había que redescubrir y habitar, sin fórmulas ni recetas. No buscaba reencontrarme con aquella Caro, sino con esta, que cambia día a día.
>
> Por eso en **Ekos** creamos un espacio para **cuerpos reales**: cada persona encuentra su ritmo, sin exigencias, sin importar la edad, la flexibilidad o la experiencia.
>
> Esta tarde la pensé con el corazón de mamá, y ahora quiero compartirla con ustedes: un rato para parar, respirar y estar juntas, con una clase, una merienda y un regalito sorpresa para llevarse de recuerdo.
>
> **Te espero el 24 💜**

### Sección 8 · Galería (opcional)

- 3 a 6 fotos del piloto de Caro y Belu: clase, risas, merienda. `[FOTOS PILOTO]`
- Si todavía no hay fotos, ocultar esta sección.

### Sección 9 · Preguntas frecuentes (acordeón)

1. **¿Necesito experiencia en yoga?**
   No. Es una clase suave, pensada para todos los niveles y todas las edades.
2. **¿Qué tengo que llevar?**
   Solo ropa cómoda. Los mats, la merienda y todo lo demás lo ponemos nosotras.
3. **¿Puedo ir sola?**
   ¡Claro! Podés venir sola, con tu mamá, tu hija o con quien quieras.
4. **¿Cómo pago?**
   Con Mercado Pago: tarjeta de crédito, débito o dinero en cuenta.
5. **¿Cómo recibo la gift card si es un regalo?**
   Después de pagar te la enviamos por WhatsApp para que se la entregues.
6. **¿Qué pasa si no puedo ir?**
   Mirá nuestra política de cancelación más abajo.
7. **Tengo otra pregunta**
   Escribinos por WhatsApp → botón `Escribinos` → `[LINK WHATSAPP]`

### Sección 10 · Política de cancelación

- **Título**: Política de cancelación
- **Texto**:
  - Hasta el **miércoles 21/10**: te devolvemos el total o podés pasar tu lugar a otra persona.
  - Desde el **jueves 22/10**: no hay devolución, pero podés pasar tu lugar a otra persona avisándonos por WhatsApp.
  - Si Ekos suspende el evento, te devolvemos el total.
- `[CONFIRMAR CON CARO]`

### Sección 11 · Clase de prueba gratis (fondo rosa suave)

- **Título**: ¿No podés el 24?
- **Texto**: Vení a conocer Ekos con una clase de prueba gratis.
- **Botón**: `Quiero mi clase de prueba` → WhatsApp con mensaje armado:
  `https://wa.me/[NÚMERO]?text=Hola!%20Quiero%20reservar%20una%20clase%20de%20prueba%20gratis%20en%20Ekos`

### Sección 12 · Cierre

- **Línea en cursiva**: *Te esperamos*
- **Título**: Una tarde para ustedes.
- **Etiqueta**: Sábado 24/10 · 15 h · Villa Urquiza
- **Botón**: `Quiero mi lugar` → #precios

### Pie de página

- Ekos Yoga · Donado 2301, Villa Urquiza, CABA
- Íconos: WhatsApp `[LINK]` · Instagram `[LINK]`

### Botón flotante

- Botón redondo de WhatsApp abajo a la derecha, visible siempre.
- Mensaje armado: "Hola! Tengo una consulta sobre Yoga + Merienda del Día de la Madre"

---

## 4. Página de "Gracias" (aparte)

Se muestra después de pagar si Mercado Pago lo permite; si no, enlazarla desde el mensaje de confirmación.

- **Línea en cursiva**: *¡Gracias!*
- **Título**: Tu lugar está reservado 💜
- **Texto**: Te esperamos el sábado 24 de octubre a las 15 h en Donado 2301, Villa Urquiza. Solo traé ropa cómoda.
- **Paso siguiente**: Para confirmar tu reserva, mandanos tu comprobante por WhatsApp.
- **Botón**: `Enviar comprobante` → WhatsApp con mensaje armado:
  "Hola! Reservé mi lugar para Yoga + Merienda del 24/10. Mi nombre es ___"
- **Texto chico**: Si es un regalo, te mandamos la gift card digital por WhatsApp.

---

## 5. Requisitos técnicos

- **Título de la página (SEO)**: Yoga + Merienda · Día de la Madre | Ekos Yoga
- **Descripción**: Regalale una tarde: clase de yoga suave y merienda en Ekos, Villa Urquiza. Sábado 24/10. Solo 10 lugares.
- **Imagen para compartir (Open Graph)**: foto principal del hero.
- **Píxel de Meta**: dejar preparado el lugar para pegar el código `[ID DEL PÍXEL]`.
  - Evento `ViewContent` al cargar la página.
  - Evento `InitiateCheckout` al tocar cualquier botón de Mercado Pago.
  - Evento `Contact` al tocar botones de WhatsApp.
- Carga rápida: imágenes comprimidas (WebP, máximo ~200 KB cada una).
- Todas las imágenes con texto alternativo descriptivo.
- Probar en celular antes de publicar.

---

## 6. Pendientes antes de publicar

- [ ] Foto real de Caro
- [ ] Fotos o video del piloto de Caro y Belu
- [ ] Link de Mercado Pago individual ($55.000)
- [ ] Link de Mercado Pago de a dos ($85.000)
- [ ] Número de WhatsApp de Ekos
- [ ] Usuario de Instagram de Ekos
- [ ] Confirmación de Caro de la política de cancelación
- [ ] Confirmación de cómo se envía la gift card
- [ ] ID del Píxel de Meta
