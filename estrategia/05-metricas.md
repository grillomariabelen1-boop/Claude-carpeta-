# Métricas, criterios de salida y árbol de decisión

## Qué se mide y qué se ignora

**Se mide:**

| Métrica | Dónde | Por qué importa |
|---|---|---|
| **Retención a 3s** | Analytics > por video | La que decide si pasás el pool. La #1. |
| **Tasa de finalización** | Analytics > por video | La segunda en peso. |
| **Watch time promedio** | Analytics > por video | Confirma las dos anteriores. |
| **Saves** | Por video | Señal de valor. Alta en colorimetría y combis. |
| **Shares** | Por video | La señal secundaria más fuerte. |
| **Views** | Por video | Resultado, no causa. Se mira, no se persigue. |
| **Seguidores netos** | Semanal | Tendencia a mediano plazo. |

**Se ignora durante la recuperación:** likes, cantidad de comentarios,
seguidores por video, y cualquier métrica de la app que no esté acá arriba.

> Los likes son la señal de menor peso del algoritmo. Un video con muchos
> likes y baja finalización no pasa el pool. Uno con pocos likes y alta
> finalización, sí.

## Línea de base (completar en Semana 0)

Resultados de los 4 tests de [`01-diagnostico.md`](01-diagnostico.md).

```
Fecha de medición:      ____________

TEST 1 — Retención a 3s, promedio últimos 10 videos:   ______ %
         ¿Mayor a 50% de caída?                        SÍ / NO

TEST 2 — ¿La grilla se lee como "color y estilo"?      SÍ / NO

TEST 3 — Hauls + combis en los últimos 20 videos:      ______ / 20
         ¿Menos de 8?                                  SÍ / NO

TEST 4 — Días sin postear en los últimos 30:           ______
         Racha más larga sin postear:                  ______ días

Views promedio últimos 10 videos:                      ______
Views del mejor video últimos 30 días:                 ______
Finalización promedio últimos 10 videos:               ______ %
Seguidores actuales:                                   ______
```

Sin esto no hay forma de saber si el plan funcionó.

## Registro semanal

Usar [`../plantillas/tracking-semanal.csv`](../plantillas/tracking-semanal.csv).
Una fila por video, cargada **72 horas después** de publicar (antes de las 72h
los números todavía se mueven mucho).

Al cierre de cada semana, calcular:

- Retención a 3s promedio de la semana
- Finalización promedio de la semana
- Views promedio y views del mejor video
- Cuántos videos superaron 500 views
- Cuántos superaron 1.000 views

## Criterios de salida del modo recuperación

Salís de modo recuperación cuando se cumplen **los cuatro** al mismo tiempo:

- [ ] **3 de los últimos 5 videos** superan las **1.000 views**
- [ ] **Retención a 3s ≥ 50%** sostenida dos semanas seguidas
- [ ] **Al menos 1 video > 3.000 views** en los últimos 14 días
- [ ] **Seguidores netos semanales positivos** tres semanas seguidas

Tres de cuatro no alcanza. El cuarto criterio es el que distingue una
recuperación real de un video suelto que tuvo suerte.

## Señales tempranas (antes de los criterios de salida)

Estas aparecen antes y confirman que el plan va bien aunque las views todavía
no se muevan. **No detener el plan si aparecen sólo estas:**

- Retención a 3s sube aunque las views sigan planas → **el gancho funciona,
  falta acumular historial limpio**. Seguir igual.
- Sube la proporción de views de "Para vos" vs. seguidores → el modelo está
  volviendo a distribuir en frío. Muy buena señal.
- Aparecen saves en videos que antes no tenían → señal de valor percibido.
- Un solo video rompe a 800-1.500 y el resto sigue en 300 → **normal**. Así
  arranca la recuperación: primero picos aislados, después el piso sube.

## Árbol de decisión — Revisión de Semana 4

### Escenario A — Retención subió Y hay picos de views
> Retención a 3s subió 10+ puntos vs. línea de base, y al menos un video
> superó las 800 views.

**Está funcionando.** Seguir el calendario tal cual. En la semana 5 duplicar el
formato ganador como está previsto. No tocar nada más.

---

### Escenario B — Retención subió PERO las views siguen planas
> Retención a 3s subió, ningún video superó las 500 views.

**El contenido está bien, falta historial limpio.** El diagnóstico de Promote
era correcto y la acumulación todavía no llegó al umbral.

Acción: **extender el plan 3 semanas más sin cambiar nada.** Este es el
escenario donde el error más caro es cambiar de estrategia justo antes de que
funcione.

---

### Escenario C — Retención NO subió
> Retención a 3s igual o peor que la línea de base.

**El gancho es el problema y no se resolvió.** Ni Promote ni el algoritmo:
los primeros 2 segundos.

Acciones, en este orden:

1. Frenar todo formato que no sea haul o combinación de color durante 2 semanas.
2. Rehacer sólo el gancho: tomar los 3 videos con **mejor** retención histórica
   de la cuenta y copiar su primer frame literalmente, mismo encuadre, misma
   distancia, misma energía.
3. Bajar todo a **15 segundos máximo**, sin excepción.
4. Publicar 5 hauls seguidos en 5 días y medir sólo retención a 3s.

Si después de esas 2 semanas la retención sigue sin moverse, el problema no es
de formato sino de producción (luz, encuadre, calidad de imagen) y hay que
atacar eso antes de volver al calendario.

## Después de la salida

Cuando se cumplan los cuatro criterios:

1. Aflojar el ratio: bajar hauls a 40%, subir colorimetría y las series.
2. Recuperar duraciones largas donde el formato lo pida.
3. Abrir el carril de **AdSense**: repurposing hacia afuera de la plataforma
   (ver [`06-colabs-y-monetizacion.md`](06-colabs-y-monetizacion.md)).
4. Empujar el ebook con CTA hablado, no sólo en descripción.
5. Reactivar Promote **sólo** sobre videos que ya funcionaron orgánicamente,
   nunca sobre videos nuevos. Amplificar un ganador es distinto de comprar
   alcance para uno que no arrancó — es la diferencia entre las dos formas de
   usar Promote y la razón del hueco que estamos reparando.
