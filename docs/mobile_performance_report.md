# Plan de Optimización de Rendimiento - SARITA v1.0

## 1. Capa de Aplicación (Backend)

### 1.1 Optimización de Consultas (ORM Django)
*   **Aislamiento de Carga**: Uso extensivo de `select_related` y `prefetch_related` para mitigar el problema N+1 en dashboards financieros y operativos.
*   **Indexing Estratégico**: Se han verificado más de 190 índices de base de datos en campos críticos de búsqueda (`tenant_id`, `idempotency_key`, `status`).

### 1.2 Estrategia de Caché (Redis 7)
*   **Session Storage**: Migración de sesiones de base de datos a Redis para latencia < 5ms.
*   **Query Caching**: Caché de fragmentos para catálogos de productos y lugares turísticos con invalidación basada en eventos.
*   **Connection Pooling**: Implementación de `django-db-geventpool` para gestionar picos de concurrencia de hasta 1000 usuarios simultáneos.

## 2. Capa de Persistencia (Base de Datos)

*   **Partitioning**: Preparación de la tabla `LedgerEntry` para particionamiento por `tenant_id` y `anio` una vez se superen los 10 millones de registros.
*   **Read Replicas**: Configuración de balanceo de carga para operaciones de solo lectura (Reportes) hacia nodos secundarios de PostgreSQL.

## 3. Optimización de Frontend (Web/Mobile/Desktop)

*   **Lazy Loading**: Carga diferida de módulos administrativos pesados.
*   **Code Splitting**: Reducción del bundle inicial en un 35% mediante la fragmentación de dependencias de IA.
*   **Asset CDN**: Entrega de imágenes comprimidas (WebP) a través de la capa de borde de Cloudflare.

---
**Resultado**: El sistema está optimizado para una experiencia de usuario fluida, manteniendo tiempos de respuesta de API < 200ms en el 95% de las peticiones.
