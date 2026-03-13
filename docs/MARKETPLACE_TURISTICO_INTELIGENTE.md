# Fase 8.7 — Marketplace Turístico Inteligente

## 1. Introducción
La Fase 8.7 convierte a SARITA en una plataforma de marketplace turístico de clase mundial, similar a Airbnb, Booking o Tripadvisor. Introduce algoritmos de ranking, sistemas de reputación y motores de recomendación para conectar de forma óptima a turistas con prestadores locales.

## 2. Arquitectura del Dominio
El dominio `apps.tourism_marketplace` actúa como una capa de inteligencia sobre el catálogo universal (`apps.turismo`).

### Modelos Principales
- **ProviderReputation**: Centraliza la confiabilidad del prestador basada en cumplimiento y calidad.
- **TourismReview**: Sistema de reseñas de 1 a 5 estrellas con verificación de compra.
- **ProductRanking**: Índices calculados para el motor de búsqueda y descubrimiento.
- **TourismPromotion**: Gestión de ofertas y servicios destacados (institucionales o pagados).
- **TourismConversionMetrics**: KPIs de embudo de ventas (visitas -> reservas).

## 3. Capacidades de Inteligencia
- **Algoritmo de Discovery**: Prioriza servicios basados en reputación (40%), popularidad (30%) y conversión (20%).
- **Recomendación Personalizada**: Sugiere experiencias basadas en el perfil y comportamiento del turista.
- **Detección de Fraude**: (Estructural) Monitoreo de actividad anómala en reseñas y cancelaciones.

## 4. Beneficios Estratégicos
1. **Confianza**: El sistema de reputación protege al turista.
2. **Visibilidad**: Los mejores prestadores suben automáticamente en el ranking.
3. **Analítica SADI**: Los datos de conversión alimentan la inteligencia territorial para el gobierno.

---
**SARITA v1.0 — 2026**
