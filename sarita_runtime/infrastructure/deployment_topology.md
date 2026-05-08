# TOPOLOGÍA DE DESPLIEGUE

## 1. SERVICIOS CRÍTICOS
- **PostgreSQL Cluster:** HA mediante Patroni / Repmgr.
- **Kafka Cluster:** Desplegado en Strimzi Operator.
- **Temporal Server:** Orquestador central del runtime.
- **Redis Cluster:** Caché y Locks distribuidos.

## 2. RED Y SEGURIDAD
- **Ingress:** Nginx / Istio para Service Mesh.
- **Secrets:** Vault para la gestión de llaves API de IA y certificados financieros.
- **Isolation:** Network Policies para restringir que los workers solo hablen con los servicios necesarios.
