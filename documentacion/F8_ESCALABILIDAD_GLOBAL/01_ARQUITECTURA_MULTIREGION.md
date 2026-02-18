# Arquitectura Multi-Región Activa - Sistema SARITA

## 1. Visión General
Para alcanzar una escala internacional real, SARITA evoluciona hacia una arquitectura **Activo-Activo con Partición por Dominio**. El sistema se despliega simultáneamente en múltiples regiones geográficas, distribuyendo la carga de trabajo y garantizando que una caída regional no interrumpa el servicio global.

## 2. Modelo de Despliegue: Activo-Activo con Partición
A diferencia de un modelo Activo-Pasivo tradicional, SARITA utiliza todas las regiones disponibles para procesar tráfico en tiempo real.

- **Partición por Dominio (Sharding Geográfico):** Las solicitudes se dirigen a la región más cercana al usuario para minimizar la latencia.
- **Soberanía de Datos:** Ciertos datos (identidad, legal) permanecen anclados a su región de origen, mientras que los datos estratégicos se replican globalmente.
- **Interoperabilidad Inter-regional:** Los microservicios de la Región A pueden invocar servicios en la Región B si un recurso específico (ej. un hotel) reside físicamente en esa zona.

## 3. Selección de Regiones Críticas

| Rol | Región AWS | Ubicación | Razón |
| :--- | :--- | :--- | :--- |
| **Primaria (Latam)** | `us-east-1` | N. Virginia | Centro de operaciones principal y mayor conectividad. |
| **Secundaria (Europa)** | `eu-central-1` | Frankfurt | Cumplimiento estricto de GDPR y baja latencia en EU. |
| **Contingencia (Asia/Pacific)** | `ap-southeast-1` | Singapur | Resiliencia ante fallos masivos en el hemisferio occidental. |

## 4. Componentes de Escalabilidad Global

### 4.1 DNS Inteligente (Amazon Route 53)
- **Geoproximity Routing:** Dirige el tráfico basándose en la distancia física.
- **Latency-Based Routing:** Selecciona la región con menor tiempo de respuesta en milisegundos.

### 4.2 Global Accelerator
Provee direcciones IP estáticas que actúan como puntos de entrada fijos, utilizando la red troncal de AWS para evitar la congestión de la internet pública.

### 4.3 Clústeres EKS Regionales
Cada región mantiene su propio clúster de Kubernetes independiente, sincronizado a nivel de configuración (GitOps), pero autónomo en su ejecución operativa.

## 5. Optimización de Latencia (Edge Strategy)
- **CDN Global (CloudFront):** Almacenamiento en caché de interfaces y activos estáticos en 200+ puntos de presencia.
- **Edge Functions:** Validación de tokens JWT y seguridad básica realizada en el "borde" antes de llegar a la región de cómputo.
