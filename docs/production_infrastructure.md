# Arquitectura de Infraestructura de Producción - SARITA v1.0

## 1. Topología del Sistema
El ecosistema SARITA opera bajo una arquitectura de alta disponibilidad (HA) distribuida en capas, garantizando resiliencia y escalabilidad elástica.

```text
Internet
   │
[CDN / WAF (Cloudflare)] <--- Caché estático, SSL, Mitigación DDoS
   │
[Global Load Balancer (AWS ALB / Nginx)] <--- Distribución de tráfico y Health Checks
   │
[Kubernetes Cluster (EKS/GKE)]
   │   ├── [API Gateway (Kong/Ingress)] <--- Auth, Rate Limiting, Logging
   │   ├── [Stateless Backend Pods (Django)] <--- Escalamiento horizontal vía HPA
   │   └── [Worker Pods (Celery)] <--- Procesamiento asíncrono
   │
[Database Cluster (RDS PostgreSQL)] <--- Primary + Multi-AZ Replicas
   │
[Distributed Cache (Elasticache Redis)] <--- Sesiones, Queues, Cache de queries
   │
[Object Storage (S3 / Cloud Storage)] <--- Archivos, Imágenes, Backups
```

## 2. Componentes de Infraestructura

### Capa de Borde (Edge Layer)
*   **CDN/WAF**: Utilización de Cloudflare para la terminación SSL, optimización de latencia y filtrado de tráfico malicioso (Bot management).
*   **Load Balancer**: Distribuidor de carga que realiza Health Checks en tiempo real (Liveness/Readiness).

### Capa de Computación (Compute Layer)
*   **Orquestación**: Kubernetes (K8s) gestiona el ciclo de vida de los contenedores.
*   **Backend**: Implementado como servicios *stateless* para permitir el auto-escalado basado en demanda (CPU/Memory).

### Capa de Persistencia (Data Layer)
*   **Base de Datos**: PostgreSQL con replicación síncrona en múltiples zonas de disponibilidad. Backups automatizados con PITR (Point-in-Time Recovery).
*   **Caché**: Redis 7 para alta velocidad en lectura de sesiones y coordinación de tareas asíncronas.

## 3. Almacenamiento de Archivos
*   Uso de almacenamiento distribuido compatible con S3 para documentos legales y evidencias del POS/Mobile.

---
**Resultado**: La infraestructura está diseñada para soportar miles de conexiones simultáneas con un tiempo de recuperación mínimo.
