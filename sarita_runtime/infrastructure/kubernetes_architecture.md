# ARQUITECTURA KUBERNETES SOBERANA

## 1. NAMESPACES
- `sarita-core`: API, Event Bus, Database.
- `sarita-runtime`: Workers, Orquestación, AI Agents.
- `sarita-monitoring`: Prometheus, Grafana, Loki.

## 2. SEGREGACIÓN DE RUNTIME
Los agentes de IA de alta jerarquía corren en pools de nodos dedicados con aislamiento de red y recursos (Taints/Tolerations) para asegurar que un desborde en el Marketplace no afecte la toma de decisiones soberana.

## 3. SCALING
- **HPA (Horizontal Pod Autoscaler):** Basado en métricas de `queue_depth` de Kafka y CPU de los workers.
- **VPA (Vertical Pod Autoscaler):** Para agentes de IA que requieren picos de memoria durante el razonamiento complejo.
