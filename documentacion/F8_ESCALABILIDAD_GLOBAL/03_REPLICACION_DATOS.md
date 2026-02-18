# Estrategia de Replicación de Datos Globales

SARITA emplea una estrategia de replicación diferenciada por la naturaleza y criticidad del dato, garantizando el cumplimiento de los RPO y RTO definidos.

## 1. Base Transaccional (PostgreSQL / Aurora Global)
Gestión del núcleo (MCP, WPA, Auditoría).

- **Replicación Intra-Región:** Síncrona entre 3 Zonas de Disponibilidad (Multi-AZ). Alta disponibilidad inmediata.
- **Replicación Inter-Región:** Asíncrona (Aurora Global Database).
  - **Latencia de replicación:** < 1 segundo.
  - **Conflict Resolution:** Last Writer Wins (basado en timestamp de alta precisión).
- **RPO (Recovery Point Objective):** < 1 minuto.
- **RTO (Recovery Time Objective):** < 15 minutos (Promoción de réplica secundaria).

## 2. Base Analítica (ClickHouse Global)
Reportes de inteligencia estratégica (Memoria Estratégica).

- **Estrategia:** Replicación eventual distribuida.
- **Flujo:** Los microservicios escriben logs analíticos en el clúster regional.
- **Agregación:** Un proceso programado consolida los datos en el Nodo de Gobernanza Central (`us-east-1`) para reportes globales mensuales.
- **Optimización:** Procesamiento regional para evitar transferencias masivas de datos entre regiones.

## 3. Vector Store (Memoria Semántica)
Embeddings de decisiones y aprendizaje adaptativo.

- **Tecnología:** Pinecone Global o clústeres pgvector replicados.
- **Sincronización:** Por lotes (Batch) cada 15 minutos.
- **Validación:** Cada lote sincronizado incluye un hash de integridad para asegurar que el aprendizaje adaptativo sea consistente en todo el mundo.

## 4. Cache Distribuida (Redis Global)
Contexto operativo y sesiones.

- **Estrategia:** Replicación Multi-Master o Sharding Geográfico.
- **TTL Operativo:** 24 horas.
- **Uso:** Sincronización de estados de misiones críticas que pueden migrar de una región a otra ante un failover.

## 5. Gobierno de la Consistencia
- **Eventual Consistency:** Aceptable para reportes y aprendizaje no crítico.
- **Strong Consistency:** Obligatoria para movimientos financieros y auditoría de identidad (gestionada mediante bloqueos distribuidos en Redis/Postgres).
- **Control de Sharding:** Los datos de usuarios europeos (`eu-central-1`) tienen prohibida la replicación completa a regiones fuera de la UE para cumplir con GDPR, excepto metadatos de auditoría anonimizados.
