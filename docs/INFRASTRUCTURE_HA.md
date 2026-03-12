# Arquitectura de Alta Disponibilidad (HA) - Sarita EOS

## 1. Uptime Objetivo: 99.99%
Para garantizar menos de 52 minutos de inactividad anual, el sistema implementa una infraestructura distribuida y redundante.

## 2. Componentes de Infraestructura
### 2.1 Global Load Balancer
Utiliza **Cloudflare** o **AWS Route53 + Global Accelerator** para:
- Terminación SSL en el edge.
- Detección de fallos a nivel de región.
- Redirección automática al clúster saludable más cercano.

### 2.2 API Gateway (Ingress Control)
Implementado con **NGINX Ingress Controller** o **Kong**:
- Rate Limiting basado en ID de Tenant.
- Protección DDoS y filtrado de cabeceras maliciosas.
- Enrutamiento inteligente hacia microservicios.

### 2.3 Orquestación con Kubernetes (K8s)
El sistema se despliega en clústeres regionales:
- **Autoescalado (HPA):** Los pods de Backend y Frontend escalan dinámicamente cuando el uso de CPU supera el 70%.
- **Resiliencia de Pods:** K8s reinicia automáticamente contenedores que fallan los healthchecks (`/api/v1/infra/health/liveness/`).
- **Zero Downtime Deployments:** Estrategia Rolling Update con validación de Readiness.

## 3. Capa de Datos Resiliente
### 3.1 Base de Datos (PostgreSQL High Availability)
- **Topología:** Primario + 2 Réplicas de lectura en diferentes zonas de disponibilidad.
- **Failover:** Gestión automática vía **Patroni** o servicio gestionado (RDS/Cloud SQL).
- **Connection Pooling:** Uso de **PgBouncer** para manejar picos masivos de conexiones.

### 3.2 Cache y Colas (Redis Cluster)
- Redis operando en modo Cluster con persistencia AOF habilitada.
- Separación física de instancias para sesiones, caché de reportes y colas Celery.

## 4. Observabilidad Total
- **Prometheus:** Recolección de métricas desde `/api/v1/infra/metrics/`.
- **Loki:** Agregación centralizada de logs de contenedores.
- **Grafana:** Dashboard ejecutivo integrado en la Torre de Control para visualización de salud sistémica.
