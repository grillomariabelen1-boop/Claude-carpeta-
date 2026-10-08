# Mensaje al desarrollador · error en anuncios y velocidad (8/10/2026)

Hola! Te escribo por un error que apareció en los anuncios de Meta y por la velocidad de la web.

**Qué pasó:** hoy cerca de las 12:59, al tocar un anuncio desde Instagram en el celular, la página del producto no cargó. Mostró "Página web no disponible" con el error `net::ERR_HTTP_RESPONSE_CODE_FAILURE`. La dirección era:
`https://saquiama.com.ar/product/camisero-anita/?v=c582dec943ff&utm_source=ig&utm_medium=paid_social...`

Probándola después carga, pero muy lenta. Como estas visitas vienen de anuncios pagos, necesitamos que no se repita.

**Te pido que revises:**

1. **Velocidad (lo más importante):** la página de producto tarda entre 2 y 13 segundos en empezar a responder (con o sin parámetros) y no se sirve desde caché: no aparece el encabezado de LiteSpeed Cache y Cloudflare marca `cf-cache-status: DYNAMIC`. ¿Podés activar la caché de página de LiteSpeed para productos y categorías? Y en LiteSpeed Cache → "Drop Query String", agregar: `utm_source, utm_medium, utm_campaign, utm_content, fbclid, v`, así las visitas que vienen de anuncios también reciben la página desde caché.

2. **Registros del servidor (LiteSpeed)** de hoy entre las 12:50 y las 13:10: si hubo errores 5xx, 403 o 429 en ese momento.

3. **Cloudflare → Seguridad → Eventos:** si se bloqueó o se le pidió verificación a tráfico desde el navegador de Instagram o Facebook, o al rastreador de Meta (`facebookexternalhit`). Si es así, que no se bloqueen.

4. **El parámetro "?v=":** toda la web redirige con 307 a una dirección con `?v=código`. Viene de WooCommerce → Ajustes → General → Ubicación predeterminada del cliente → "Geolocalizar (con soporte de caché de página)". Suma un salto en cada clic y los anuncios guardan códigos viejos. Si no usamos la geolocalización para precios o impuestos, ¿se puede pasar a "Geolocalizar" sin soporte de caché, o desactivar?

5. **Que las páginas de producto respondan bien con parámetros de anuncio**, por ejemplo `?utm_source=ig&utm_medium=paid&utm_campaign=...&fbclid=...`, sin redirecciones de más.

Cuando lo revises, contame qué encontraste y qué cambiaste, y si podés, cuánto tarda la página después del cambio. ¡Gracias!
