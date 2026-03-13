# Modelos de Predicción Turística

## 1. Predicción de Demanda (Demand Forecast)
El modelo `TourismDemandForecast` actúa como la base para la planificación.

**Variables de Entrada:**
- Reservas históricas (Catálogo Universal).
- Consultas de disponibilidad en Marketplace.
- Eventos institucionales (Calendario Cultural).

**Salida:**
- Volumen estimado de turistas por destino/fecha.

## 2. Segmentación de Comportamiento (Tourist Segmentation)
Se basa en el modelo `TouristBehaviorProfile`.

**Clasificación Automática:**
- **Aventurero**: >60% de reservas en categorías de Tours/Naturaleza.
- **Gastronómico**: Ticket promedio alto en Restaurantes.
- **Familiar**: Reservas de grupos >3 personas de forma recurrente.

## 3. Algoritmo de Precios Dinámicos
**Lógica de Cálculo:**
1. **Temporada Alta**: Multiplicador x1.20 (Basado en `TourismSeasonality`).
2. **Ocupación Crítica**: Si ocupación < 20% -> Reducción x0.85 sugerida.
3. **Reputación**: Bonus de incremento de precio para servicios con rating > 4.8.

## 4. Flujos Turísticos (Flow Analytics)
Cruza el origen de la transacción con la ubicación del prestador para identificar:
- Corredores turísticos principales.
- Mercados emisores dominantes (ej: turistas de Bogotá vs turistas locales).

---
**Arquitectura de Datos SARITA — 2026**
