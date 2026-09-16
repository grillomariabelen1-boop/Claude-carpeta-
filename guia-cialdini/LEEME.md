# Guía de estudio: los seis principios de Cialdini

Guía en español sobre *Influence: The Psychology of Persuasion*, de Robert B. Cialdini.
Resumen, análisis de los experimentos y aplicaciones a marketing. **No es una traducción
del libro**: es material propio escrito sobre sus ideas.

## Contenido

Diez capítulos: cómo usar la guía, la idea central (clic-zumbido y el principio de
contraste), uno por cada principio (reciprocidad, compromiso y coherencia, prueba social,
simpatía, autoridad, escasez), el cierre, y una referencia rápida de una página.

Cada principio trae la idea en una frase, por qué existe el atajo, los experimentos con
sus números, las tácticas que se construyen encima, las condiciones que lo amplifican, la
defensa que propone Cialdini y una sección de aplicaciones a marketing.

## Generar el PDF

    ./construir.sh

Produce `Cialdini-GUIA-A5.pdf`: 80 páginas A5 (148 × 210 mm) con márgenes espejados y
lomo de 20 mm, listas para imprimir a doble faz y anillar. Los capítulos abren siempre en
página impar.

Si tu chromium está en otra ruta:

    CHROME=/ruta/a/chrome ./construir.sh

## Editar

Todo el texto y el diseño están en `guia.html`. Los saltos de página y el espejado de
márgenes se resuelven con CSS (`@page` y `@page :left`). Los `<div class="relleno">`
son hojas de guarda en blanco que empujan cada capítulo a página impar; si editás el
texto y cambia la paginación, hay que reubicarlos.
