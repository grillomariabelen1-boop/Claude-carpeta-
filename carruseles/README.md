# Carruseles e imágenes

Acá se arman los carruseles y las placas para Instagram. El armado se hace
en esta carpeta; la edición final la hacés vos en Canva.

## El circuito

```
1. Se arma acá          → un archivo .html por carrusel, una diapositiva por página
2. Se pushea a GitHub   → queda en una URL pública
3. Se importa a Canva   → cada página entra como diapositiva editable
4. Lo terminás vos      → ponés tus fotos, ajustás tipografías y publicás
```

Lo que llega a Canva **no es una imagen plana**: los textos son textos, los
bloques de color son bloques. Se puede editar todo.

## El formato

- **1080 × 1350 px** (4:5). Es el que ocupa más pantalla en el feed de Instagram.
- Entre 8 y 10 diapositivas. La 1 es la que decide si alguien entra.
- Los recuadros gris claro que dicen **FOTO** son huecos: en Canva arrastrás tu
  imagen encima y listo.

## Sistema visual

| Elemento | Valor |
|---|---|
| Fondo claro | `#F4EFE7` (crudo) |
| Fondo oscuro | `#111111` |
| Tinta | `#1C1917` |
| Acento | `#C9922E` (dorado — sale de tu Warm Spring) |
| Alerta | `#D4715A` (terracota) |
| Titulares | Playfair Display |
| Texto | DM Sans |

Los colores del sistema son la marca. Los colores que aparecen como muestras
adentro de una diapositiva son **contenido**: cambian en cada carrusel.

## Estructura de un carrusel

| Diapositiva | Función |
|---|---|
| 1 | **Gancho.** Foto arriba, frase abajo sobre negro. Nada más. |
| 2 | **La tensión.** Por qué el tema importa. Sin resolverlo todavía. |
| 3-7 | **El contenido.** Una idea por diapositiva, siempre con la misma estructura. |
| 8 | **El error.** Lo que casi nadie mira. Es la diapositiva que genera el guardado. |
| 9 | **Cierre.** "Guardalo para…" + el handle. Nunca "seguime". |

## Hacer uno nuevo

Se copia la carpeta de un carrusel existente y se cambia el contenido. Todo el
sistema visual está adentro del propio `.html`, así que cada carrusel es
autónomo y no se rompe si tocás otro.

## Carruseles armados

| Carpeta | Carril | Estado |
|---|---|---|
| [`01-negro-combinaciones/`](01-negro-combinaciones/) | Autoridad — color | Listo para Canva |
