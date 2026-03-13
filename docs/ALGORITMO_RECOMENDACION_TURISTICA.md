# Algoritmo de Recomendación y Ranking Turístico

## 1. El Score de Ranking (Product Score)
Cada producto en el marketplace recibe un `score_total` calculado mediante la siguiente fórmula:

```
Score = (0.4 * R) + (0.3 * P) + (0.2 * C) + (0.1 * A)
```

Donde:
- **R (Reputación)**: Rating promedio del prestador y su índice de confiabilidad.
- **P (Popularidad)**: Volumen de reservas históricas (normalizado).
- **C (Conversión)**: Tasa de conversión (reservas / visitas).
- **A (Actividad)**: Actividad económica reciente o promociones institucionales.

## 2. Lógica del Motor de Recomendación
El `TourismRecommendationService` utiliza tres tuberías principales:

### A. Recomendados para Ti
- Cruza las categorías favoritas del turista con los productos de mayor ranking.
- Filtra por disponibilidad en tiempo real.

### B. Tendencias del Destino
- Identifica productos con el mayor crecimiento de reservas en los últimos 7 días.
- Ignora el ranking histórico para permitir el surgimiento de nuevos éxitos locales.

### C. Experiencias Populares
- Basado estrictamente en el índice de popularidad (volumen acumulado).

## 3. Optimización para SADI
El algoritmo no solo busca la venta, sino el impacto regional. Se pueden inyectar pesos adicionales por:
- **Territorialidad**: Priorizar municipios menos visitados para distribuir el flujo.
- **Calidad Certificada**: Bonus de +0.2 en reputación para prestadores con certificaciones vigentes.

---
**Documentación Técnica SARITA — 2026**
