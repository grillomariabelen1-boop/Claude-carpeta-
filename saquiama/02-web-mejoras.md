# Auditoría de la web: saquiama.com.ar

*Relevada el 25/9/2026, navegando la web desde un iPhone 13 simulado. Capturas
en [`capturas-web/`](capturas-web/).*

## Cómo está hecha

| | |
|---|---|
| Plataforma | WordPress 7.1 + WooCommerce 11.1 |
| Diseño | Elementor Pro, tema Kadence |
| Píxel de Meta | Plugin **PixelYourSite**, un píxel (`868160216021939`), con API de conversiones activada y `event_id` para deduplicar |
| Otros | Google Tag Manager (`GTM-KM9JWL46`), Site Kit de Google, botón de WhatsApp (Joinchat), muestras de color y talle |
| Medios de pago | Transferencia (15% off), Mercado Pago, tarjeta |
| Envío | CABA $7.000 · "Precio fijo" $10.000 · retiro en showroom gratis · gratis desde $140.000 |

> **Qué significa para el desarrollador:** es una plataforma estándar. Todo lo
> que sigue se resuelve desde la configuración de WooCommerce y Elementor, sin
> programar desde cero.

---

## Lo que está bien (hay que decirlo en la presentación)

- **La tabla de talles de la ficha está en centímetros** (busto, cadera y
  largo por talle). Es lo que más necesita una clienta de 30 a 50.
- **Las fotos son de Marce en el showroom**, con la prenda puesta. Son
  coherentes con los anuncios que funcionan.
- **Dice la tela** en la ficha.
- **La política de cambios es clara y generosa**: 20 días, cambio por correo o
  en el showroom, cupón sin vencimiento por la diferencia.
- **Hay botón de WhatsApp** y tres medios de pago.

---

## Mejoras, ordenadas por impacto

Impacto: 🔴 alto · 🟡 medio · ⚪ bajo. Esfuerzo: para el desarrollador.

| # | Qué pasa hoy | Qué cambiar | Impacto | Esfuerzo |
|---|---|---|---|---|
| 1 | **El checkout arranca con el país en "Estados Unidos"** y la provincia muestra estados de EE.UU. Cada clienta tiene que cambiarlo a mano. Algunas van a abandonar ahí, y otras van a dejar el pedido con datos mal cargados ([captura](capturas-web/03-checkout-pais-eeuu.png)) | Fijar Argentina como país por defecto. Si solo venden en Argentina, sacar el campo | 🔴 | Bajo: es una opción de WooCommerce |
| 2 | **En el celular, el encabezado (logo, carrito y buscador) queda fijo y ocupa casi un tercio de la pantalla.** En el checkout tapa los campos mientras la clienta los llena ([captura](capturas-web/04-checkout-header-tapa-campos.png)) | Achicar el encabezado fijo en el celular: una sola línea, con el buscador adentro del menú. Como mínimo, que no quede fijo en el checkout | 🔴 | Bajo o medio |
| 3 | **El descuento por transferencia (15%) y el envío gratis desde $140.000 solo aparecen en un banner que rota arriba.** No están en la ficha ni en el carrito | Mostrar en la ficha: "$ 86.000 · **$ 73.100 con transferencia**". En el carrito: "Te faltan $X para el envío gratis" | 🔴 | Bajo: hay plugins para las dos cosas |
| 4 | **No se ven las cuotas** en ningún lado, con un ticket de $80.000 | Si Mercado Pago o la tarjeta ofrecen cuotas sin interés, mostrarlo en la ficha y en el listado. Si no ofrecen, evaluar sumarlas: con este ticket es una razón de compra | 🔴 | Bajo para mostrarlo. Tener cuotas es una decisión comercial |
| 5 | **El costo de envío recién aparece en el checkout**, y las opciones son confusas: "Envío a domicilio en CABA" le aparece también a alguien de provincia, y la otra opción se llama "Precio fijo" | Renombrar a "Envío a todo el país: $10.000". Mostrar la opción de CABA solo si la dirección es de CABA. Poner el costo en la ficha, debajo del botón de comprar | 🟡 | Bajo |
| 6 | **La ficha no dice qué talle usa Marce ni cuánto mide.** Los talles son "1, 2, 3" sin equivalencia (en otros productos son S, M, L, XL) | Agregar "Marce mide 1,xx y usa talle 2". Unificar la nomenclatura o poner la equivalencia (1 = S/M…) | 🟡 | Bajo: es texto |
| 7 | **No hay videos en la ficha**, aunque los videos de Marce son lo que vende en Instagram y en la pauta | Sumar el reel de cada prenda a su ficha | 🟡 | Bajo: se carga el video en la galería |
| 8 | **El botón "Buscar" se ve cortado** en el celular ("Busc…"), y el carrito se sale del borde con montos grandes | Ajustar el ancho en Elementor para celular | ⚪ | Bajo |
| 9 | **El showroom es uno solo, pero figura escrito de tres formas**: la ficha dice "2105, **CABA**", el pie dice "2105, Avellaneda" y la página de cambios dice "**2101**, Piñeyro" | Unificarla en todos lados | ⚪ | Bajo: es texto |
| 10 | **Textos en español de España o en inglés**: "Apellidos", "Población", "¿Tienes un cupón?", y el aviso de privacidad del checkout está en inglés | Pasar a español rioplatense: "Apellido", "Localidad", "¿Tenés un cupón?" | ⚪ | Bajo |
| 11 | **La página de inicio muestra solo 6 productos** y no tiene ninguna frase que diga qué es Saquiama ni por qué comprar ahí | Sumar una línea de propuesta de valor ("Ropa cómoda para mujeres reales · talles del 1 al 3 · cambios en 20 días") y los accesos a Nuevos, Más vendidos y Sale | ⚪ | Medio |
| 12 | **No se ven productos relacionados** ni "completá el look" en la ficha | Activar productos relacionados o armar looks. Sube el ticket promedio | ⚪ | Bajo |

---

## ⚠️ Para revisar con un profesional (no es tema de diseño)

- **Botón de arrepentimiento.** No aparece en ninguna parte del código de la
  página de inicio. La [Resolución 424/2020](https://www.argentina.gob.ar/normativa/nacional/resoluci%C3%B3n-424-2020-342869/texto)
  exige un link visible desde la página de inicio para quien vende por web.
- **"No hacemos devolución de dinero".** El art. 34 de la Ley 24.240 le da a
  quien compra a distancia 10 días corridos para revocar la compra, contados
  desde la entrega ([resumen de la
  Defensoría CABA](https://defensoria.org.ar/archivo_noticias/paginas-y-aplicaciones-web-deberan-incorporar-un-boton-de-arrepentimiento/)).
  La frase de la política de cambios puede chocar con eso.

No soy abogado: esto es para que la marca lo consulte con su contador o
abogado. No va en la presentación como recomendación de pauta, sino como un
aviso aparte.

---

## Lo que no pude medir desde acá

- **La velocidad real.** El entorno desde el que navegué bloquea los servicios
  externos (Google, Meta), así que el tiempo de carga que medí no es el de una
  clienta. **Falta pasar la web por [PageSpeed
  Insights](https://pagespeed.web.dev/)** desde tu compu y guardar el
  resultado del celular.
- **Qué hay adentro del Google Tag Manager.** No lo pude abrir. Ver
  [`03-auditoria-medicion.md`](03-auditoria-medicion.md).
- **El paso de pago de Mercado Pago:** no hice ninguna compra.
