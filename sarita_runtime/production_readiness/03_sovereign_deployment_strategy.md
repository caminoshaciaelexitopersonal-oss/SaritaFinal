# ARQUITECTURA DE PRODUCCIÓN REAL (SARITA SOBERANA)

## 1. ESCALAMIENTO HORIZONTAL
- **Workers:** Desplegados como K8s Deployments con HPA basado en `kafka_lag`.
- **Kafka:** Cluster de 3 brokers mínimo, distribuido en 3 zonas de disponibilidad.
- **Database:** Postgres con Patroni para HA y réplicas de lectura para telemetría.

## 2. ESTRATEGIA DE DEPLOYMENT SOBERANO
- **Zero Downtime:** Rolling updates controlados por el Sovereign Control Plane.
- **Canary Releasing:** Despliegue gradual de nuevos agentes de IA para validar su `cognitive_pressure` antes del rollout total.

## 3. GLOBAL PRODUCTION ROADMAP
1. **Hardening (Q1):** Penetration testing en el isolation de tenants.
2. **Expansion (Q2):** Despliegue en regiones soberanas (Nubes privadas / On-premise).
3. **Cognitive Maturity (Q3):** Auto-evolución de esquemas habilitada en producción.
