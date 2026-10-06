# Village Polo Club — notas de trabajo

- **La tarjeta de Notion del cliente tiene una sección "Propuestas a los dueños"**, que vive en
  `05-propuestas-a-los-duenos.md`. Cada propuesta nueva que requiera decisión de los dueños (precios, envío, stock, políticas)
  se suma ahí con qué se pide, por qué, cuánto cuesta y estado (🟡 Propuesta · 🟢 Aprobada · 🔴 Rechazada · ✅ Hecha).
- **Claude no escribe en Notion.** Siempre entrega el markdown listo para pegar, y se carga a mano (o con
  Claude in Chrome). El markdown de la tarjeta incluye la sección "Propuestas a los dueños". Usar markdown que Notion pegue bien: títulos `##`, tablas simples, listas y
  checkboxes `- [ ]`. Nada de HTML.
- **Flujo de aprobación:** las ideas, ángulos y guiones de creativos primero se presentan en el chat para aprobar, en formato
  corto. Recién con la aprobación se arma el markdown para Notion. No pasar markdown de Notion de algo no aprobado.
- **No armar entregables (presentaciones, documentos, markdown) hasta que se pida explícitamente.** Primero se cierra y aprueba
  TODO el plan en el chat; recién ahí se arma el documento completo.
- **Son dos presentaciones:** (1) para el **equipo de redes**, que ejecuta los creativos (guiones, grabación, piezas,
  cronograma); (2) para los **dueños**, con las propuestas que ellos deciden (fechas grandes, ofertas, stock, composturas).
  Redes: https://claude.ai/artifact/K3bw2Q6BK9iN4MUg13YMQj · Dueños: https://claude.ai/artifact/SKidYEdP2Vu9Lf2SAFnurZ
  (armadas el 30/9 con todo lo aprobado).
- Datos confirmados (24/9/2026):
  - Hechter: Village lo **revende como distribuidor oficial**. No lo fabrica.
  - Ambos: vienen por talles, son **saco y pantalón**, y tienen **composturas gratis**. Drop 6: saco 50 lleva pantalón 44.
  - Envío gratis: se propone a los dueños bajar el umbral a **$120.000**.
  - Preguntas frecuentes de la web: ya corregidas (24/9).
  - **Talles: es el cuello de botella y los dueños no pasan medidas.** El plan para resolverlo sin ellos está en `07-talles.md`.
- Google Ads (6/10/2026): primera campaña (Máximo rendimiento / IA de Google), presupuesto **aparte** del de Meta:
  **$15.000 por día** (~$456.000 por mes). Idioma español, Argentina, sin la marca ni competidores en los temas de búsqueda.
  Revisar a las 2-3 semanas cuánto cuesta cada venta real antes de subir.
  - Estado 6/10: la campaña "Campaign #1" quedó ACTIVA aunque el asistente se trabó (hay que pausarla). Trabada en el paso de la etiqueta (Tiendanube no tiene campo de Google Ads).
    Ya tienen Analytics 4. Pendiente: cargar ID G- y secreto de API en Tiendanube → Códigos externos, vincular GA4 con
    Ads, importar la conversión "purchase", combinar la etiqueta G- con AW-18498611602 y recién ahí publicar.
