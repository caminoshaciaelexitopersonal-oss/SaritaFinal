# ARQUITECTURA TÉCNICA COMPLETA — SARITA ERP (FASE 3)

## 1. Motor Multi-Tenancy
- **Implementación:** Aislamiento de datos mediante `TenantAwareModel`.
- **Gobernanza:** Filtrado automático por `tenant_id` en todas las consultas de la API y acciones de agentes.

## 2. Seguridad y Comunicaciones
- **Autenticación:** JWT centralizado con rotación de tokens.
- **Shared SDK:** Cliente HTTP unificado para Web, Mobile y Desktop con manejo de interceptores de seguridad.

## 3. Blindaje Criptográfico (Blockchain)
- **Hashing Operativo:** SHA-256 para sellado inmediato de documentos y transacciones.
- **Notarización:** Procesamiento por lotes (Batch processing) mediante Árboles de Merkle anclados a la red Polygon.

## 4. Orquestación de Agentes IA
- **Jerarquía:** 6 niveles de mando.
- **Estándar N6 Oro V2:** Ejecución determinística, atómica e idéntica en todos los nodos del sistema.

## 5. Ecosistema de Servicios
- **Wallet:** Gestión de créditos y pagos integrados.
- **Delivery:** Logística de última milla vinculada a la operativa de restaurantes.
- **Orquestador de Viajes:** Planificación autónoma basada en perfiles de turista.

## 6. Sincronización Multi-Plataforma
- **Event Bus:** Comunicación en tiempo real mediante WebSockets y tareas asíncronas (Celery/Redis).
- **Offline Resilience:** Estrategia de sincronización para dispositivos móviles en zonas remotas.
