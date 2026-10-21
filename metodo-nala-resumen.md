# Método Nala: resumen operativo para gestionar campañas de Meta Ads

> Contexto para el asistente: este documento resume el "Método Nala" (guía de un curso de Meta Ads de Sol, Nala Basics) y suma notas de implementación. Todo lo que **no** sale de la guía original está marcado como **[Recomendación adicional]**. Usalo como marco para analizar, armar y optimizar las campañas de esta cuenta.

---

## 1. Idea central

- En adquisición, Meta encuentra al comprador mejor que una segmentación manual. Se usa **público abierto Advantage+** y el foco está en las **creatividades**.
- El contenido del anuncio (hook, copy, título) funciona como señal de segmentación.
- El ciclo es **testear → analizar → optimizar → escalar**, y se repite.
- Las decisiones se toman con **importe gastado, compras, CPA y ROAS**, nunca por likes, reproducciones o clics.

---

## 2. Estructura de campañas

| Campaña | Función | Público | Exclusiones |
|---|---|---|---|
| **CBO \| TESTEO DE ANUNCIOS** | Probar ~10 creatividades distintas | Abierto Advantage+, 1 solo conjunto, solo el país | Ninguna |
| **CBO \| ANUNCIOS GANADORES** | Concentrar la inversión en los anuncios que vendieron en el testeo | Abierto Advantage+ | Ninguna |
| **CBO \| MOFU** | Volver a impactar a quienes ya interactuaron con la marca | **Cerrado**: públicos personalizados combinados en 1 conjunto | Compradores **[Recomendación adicional]** |
| **BOFU (remarketing)** | Recuperar carritos y pagos abandonados | **Cerrado**: Add to Cart de 7 o 14 días (o Initiate Checkout) | Compradores del período (sale de la guía) |

**No hace falta tener las 4 activas desde el inicio.** Depende del presupuesto y del tráfico. Primero va el testeo, después los ganadores, y MOFU y BOFU se suman en la semana 2 si el volumen de audiencia lo justifica.

### CBO vs ABO
- La guía prefiere **CBO** (presupuesto a nivel campaña).
- En testeo se usa una CBO con **un único conjunto**: todo el presupuesto va ahí y Meta reparte entre los anuncios.
- ABO no está mal, pero fragmenta el presupuesto.
- **Con presupuestos chicos, concentrar y no dividir.** Por ejemplo, nunca 5 conjuntos de USD 2.

---

## 3. Públicos y exclusiones

### Adquisición (testeo y ganadores)
- Público abierto Advantage+.
- Sin intereses ni públicos similares.
- Solo las condiciones necesarias, como el país de venta.

### MOFU (cerrado)
- **Incluir** (todo combinado en un solo conjunto):
  - Visitantes de la web, 30 días
  - Engagement de Instagram, 60 días
  - Add to Cart, 60 días
- **Sin expansión**: la guía pide verificar que la configuración no permita expandirse fuera de los públicos elegidos.
- **Excluir compradores recientes**, de 30 a 180 días según el ciclo de recompra **[Recomendación adicional]**. La guía no menciona exclusiones para MOFU.
- Si BOFU está activa al mismo tiempo, se puede **excluir Add to Cart de 7–14 días** de MOFU para que no se superpongan **[Recomendación adicional]**.
- **Anuncios:** beneficios, testimonios auténticos, demostraciones, promociones, envíos.

### BOFU (cerrado)
- **Incluir:** Add to Cart de 7 o 14 días, o Initiate Checkout.
- **Excluir:** los compradores del mismo período.
- **Sin expansión.**
- **Anuncios:** resolver las últimas objeciones (cuotas sin interés, medios de pago, envíos, cambios, testimonios).
- **Ejemplo de anuncio:**
  - **Texto principal:** "¿Todavía estás pensando en llevarte tus favoritos? Descubrí nuestra colección y completá tu compra. Tenemos 6 cuotas sin interés y envíos a todo el país."
  - **Título:** "6 cuotas sin interés"
  - **CTA:** Comprar

### Cómo dejar un conjunto cerrado en el Administrador [Recomendación adicional]
- En el conjunto, si aparece "Público Advantage+", elegir **"Usar opciones de público originales"**.
- Cargar los públicos personalizados en **Incluir** y los compradores en **Excluir**.
- Revisar que no quede activa ninguna opción de expansión o de "llegar a más personas".

### Clientes existentes en adquisición [Recomendación adicional]
- En la configuración de la cuenta publicitaria se puede definir quiénes son los clientes actuales, para limitar cuánto gasto va a ellos.

---

## 4. CBO de testeo, paso a paso

1. **Campaña:** objetivo Ventas, nombre `CBO | TESTEO DE ANUNCIOS`, presupuesto a nivel campaña. Referencia: **~USD 14 diarios**.
2. **Conjunto:** 1 solo, con público abierto Advantage+.
3. **Anuncios:** 10, que **no** sean casi idénticos. Distribución sugerida:
   - Ads 1–2: dolores y problemas
   - Ads 3–4: beneficios del producto
   - Ads 5–6: demostraciones
   - Ads 7–8: oferta comercial
   - Ads 9–10: otros ángulos (testimonios, comparaciones, lanzamientos, estilo de vida)
4. **No se asigna presupuesto por anuncio.** Meta reparte de forma desigual, así que un anuncio con poco gasto todavía no está "malo".
5. **Revisión diaria:** importe gastado, compras, CPA, ROAS. Como complemento: CTR, CPC y frecuencia.

---

## 5. Cuándo apagar un anuncio y cuándo es ganador

- **Filtro rápido:** si un anuncio gastó **más que el ticket promedio sin ninguna venta**, considerar apagarlo.
  - Ejemplo: ticket de USD 6, anuncio con USD 8–9 gastados y 0 ventas → apagar.
- **Ejemplo de decisiones durante el testeo** (resultados ficticios de la guía):
  - USD 8 gastados, 3 compras → mantener
  - USD 9 gastados, 0 compras → apagar
  - USD 6 gastados, 1 compra → evaluar
  - USD 3 gastados, 0 compras → observar
- **Ganador:** sigue generando compras a un CPA rentable y no solo consiguió una venta aislada. Los ganadores pasan a `CBO | ANUNCIOS GANADORES`.
- **El testeo sigue activo** en paralelo para seguir buscando creatividades nuevas.

### Gasto sin compras con un CPA objetivo de USD 10
| Gasto sin compras | Acción |
|---|---|
| USD 5 | Observar |
| USD 10 | Revisar señales |
| USD 20 | Considerar pausa |
| USD 30 | Priorizar diagnóstico y posible pausa |

### Tiempos
- **Días 1–3:** verificar que entregue bien. Solo se corrigen errores evidentes, como una URL rota o un checkout que no funciona.
- **Días 4–7:** empezar a evaluar con gasto acumulado, compras, CPA y ROAS.
- **Nunca apagar por un solo día malo.**

---

## 6. Presupuestos de referencia

| Presupuesto diario | Uso orientativo |
|---|---|
| USD 5–10 | Pruebas muy limitadas |
| USD 10–20 | Testeo inicial concentrado |
| USD 20–50 | Mayor capacidad de testeo |
| USD 50–100 | Testeo y escalado |
| +USD 100 | Escalado con control de rentabilidad |

- Conviene pensar el presupuesto en compras. Ejemplo: con un CPA máximo de USD 10 y USD 20 por día, el presupuesto alcanza para unas 2 compras diarias a ese CPA.

---

## 7. Métricas

**Orden de prioridad:** importe gastado → compras → CPA → ROAS. Después se miran CTR, CPC, frecuencia y CPM.

- **CPA** = gasto ÷ compras.
- **CTR del enlace:**
  - Menos de 0,8%: revisar la creatividad
  - 0,8–1,5%: aceptable según el contexto
  - 1,5–2%: buena señal
  - Más de 2%: objetivo
- **CPC del enlace (referencia LatAm):**
  - Menos de USD 0,20: muy económico
  - USD 0,20–0,50: atractivo
  - USD 0,50–1,00: evaluar según ventas
  - USD 1,00–1,50: revisar contexto y rentabilidad
  - Más de USD 1,50: puede requerir optimización
- **Frecuencia:** si sube, el CTR cae y el CPA empeora durante varios días, hay que renovar creatividades. En remarketing es normal que sea más alta.
- **CPM alto:** no significa que el anuncio sea malo. Puede ser por la competencia, la audiencia o la temporada.

### ROAS Break Even
- **Fórmula:** ROAS Break Even = 1 ÷ margen de contribución.
- **Ejemplo:**
  - Precio de venta: USD 50
  - Costos variables: USD 30 (producto 20 + packaging 2 + comisiones 3 + otros 5)
  - Margen: 40%
  - Break Even: 1 ÷ 0,40 = **2,5**
- Además del Break Even se define un **ROAS objetivo** más alto (por ejemplo, 3,5–4).
- El ROAS de Meta usa su propio modelo de atribución. Hay que compararlo con las ventas reales que registra la tienda.

### Diagnóstico
- **CTR bajo + CPC alto:** el problema está en la creatividad (hook, mensaje, propuesta).
- **CTR alto + pocas compras:** el problema está después del clic (web, precio, pagos, envío).
- **Muchos carritos + pocas compras:** hay que revisar el checkout y los costos de envío, y sumar BOFU.
- **Buen ROAS con pocas compras:** no es suficiente para escalar.
- **CPA sube y ROAS cae durante varios días:** revisar frecuencia, CTR y CPC por posible fatiga creativa.

---

## 8. Escalado

### Vertical
- Subir el presupuesto **20–30%**, evaluando **cada 48–72 horas**.
- Solo si hay volumen de compras y los resultados son rentables y estables.
- Si los resultados empeoran de forma sostenida: mantener, volver al presupuesto anterior o revisar la estrategia.

### Horizontal
- Hacer nuevas creatividades sobre el ángulo que ganó.
- Probar otros productos o nuevas ubicaciones geográficas.
- Duplicar campañas **no** es una estrategia de escalado automática.

### Las 5 preguntas antes de escalar
1. ¿Cuánto lleva gastado?
2. ¿Cuántas compras generó?
3. ¿El CPA está dentro del objetivo?
4. ¿El ROAS está por encima del Break Even y, mejor todavía, del objetivo?
5. ¿Los resultados se mantienen estables varios días?

### Decisiones con Break Even 2,5 y ROAS objetivo 3,5
| Situación | Decisión |
|---|---|
| ROAS 4,5, compras estables y CPA rentable | Evaluar un aumento del 20–30% |
| ROAS 3,6 y resultados estables | Posible aumento del 20% |
| ROAS 3,0 (debajo del objetivo) | Mantener y observar |
| ROAS 2,2 durante varios días | Revisar y considerar reducir |
| ROAS 1,5 con gasto significativo | Priorizar diagnóstico y posible pausa |

---

## 9. Creatividades

- **Estructura:** hook (0–3 s) → problema (3–7 s) → producto y solución (7–14 s) → beneficios y oferta (14–18 s) → CTA (18–20 s).
- **Hooks:** cortos, concretos y ligados a un dolor o deseo real.
  - Ejemplo: "¿Cansada de bikinis que no se ajustan bien?"
- **Comunicar beneficios, no solo características.**
  - "Tiras regulables" se convierte en "ajustás el calce a tu gusto".
- **Formatos:** video, imagen estática, carrusel y catálogo. Se elige según cuál vende, no según la moda.
- **Texto principal:** claro, con los beneficios y las condiciones (cuotas, envíos).
- **Título:** la propuesta comercial (por ejemplo, "6 cuotas sin interés").
- **CTA:** "Comprar".
- **Coherencia con la web:** lo que promete el anuncio tiene que estar en la tienda (precio, cuotas, producto).

---

## 10. Rutina

- **Todos los días:** gasto, compras, CPA, ROAS, qué anuncios reciben presupuesto y pausar los que gastan sin vender. Comparar con períodos más amplios antes de decidir.
- **Cada 48–72 horas:** evaluar aumentos de presupuesto.
- **Una vez por semana:**
  - Qué anuncios ganaron y cuáles dejaron de funcionar
  - Qué creatividades nuevas hacen falta
  - Si el remarketing es rentable o está saturado
  - Planificar los próximos testeos
- **Semana sugerida:**
  - Lunes: revisión general
  - Martes: optimización y nuevos testeos
  - Miércoles: presupuestos y escalado
  - Jueves: creatividades y remarketing
  - Viernes: rentabilidad y planificación

## 11. Plan de 21 días
- **Semana 1 (preparar y testear):**
  - Calcular el Break Even
  - Preparar 10 anuncios
  - Lanzar la CBO de testeo
- **Semana 2 (decidir):**
  - Apagar los anuncios que gastaron sin vender
  - Armar la CBO de ganadores
  - Sumar MOFU y BOFU si corresponde
  - Preparar creatividades nuevas
- **Semana 3 (escalar):**
  - Confirmar que los ganadores se mantienen estables
  - Subir el presupuesto 20–30% cada 48–72 horas
  - Evaluar el escalado horizontal

## 12. Errores a evitar
- Segmentar de más en adquisición.
- Apagar por un solo día malo.
- Escalar por una única compra.
- No conocer el Break Even.
- Fragmentar el presupuesto.
- Mantener anuncios activos solo por su CTR.
- Hacer anuncios sin propuesta de valor.
- No renovar creatividades.
- Escalar demasiado rápido.
- Ignorar la experiencia de compra en la tienda.

---

## 13. Plan de migración desde una estructura existente [Recomendación adicional]

Objetivo: pasar al método **sin apagar de golpe lo que ya vende**.

### Paso 0: preparación
1. Calcular el ROAS Break Even y el ROAS objetivo.
2. Verificar que el píxel registre bien Purchase, AddToCart e InitiateCheckout.
3. Crear los públicos personalizados:
   - Web Visitors, 30 días
   - Engagement de IG, 60 días
   - Add to Cart, 60 días
   - Add to Cart, 7 o 14 días
   - Compradores, 180 días

### Paso 1: auditoría
Revisar cada anuncio activo con datos de los últimos 14–30 días:
- **Vendió con ROAS por encima del Break Even:** candidato a ganador.
- **Gastó más que el ticket promedio sin ventas:** apagar.
- **Gastó poco:** no hay datos, así que se puede reciclar en el testeo.

### Paso 2: armar las campañas nuevas sin apagar las viejas
- `CBO | ANUNCIOS GANADORES` con los candidatos.
  - Cargarlos con **"Usar publicación existente"** (ID de la publicación) para conservar la prueba social.
- `CBO | TESTEO` con 10 anuncios nuevos o con los que no tuvieron datos suficientes.
- MOFU y BOFU solo si hay suficiente tráfico o audiencia.

### Paso 3: pasar el presupuesto de forma gradual
- Durante la primera semana conviven las campañas viejas y las nuevas.
- A medida que las nuevas muestran compras rentables, se bajan o apagan las viejas (las de intereses o con muchos conjuntos).

### Paso 4: aplicar el plan de 21 días (sección 11)

### Datos que hay que pedirle al usuario para personalizar la migración
- Campañas activas actuales: cantidad, estructura, si usan intereses o público abierto.
- Gasto diario total.
- Ticket promedio y costos variables (para el Break Even).
- Tráfico mensual de la web, para decidir si conviene activar MOFU y BOFU.
