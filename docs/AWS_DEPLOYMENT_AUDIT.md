# AWS DEPLOYMENT AUDIT - SARITA
**Propósito:** Evaluación de preparación para despliegue en Amazon Web Services.

## 1. SERVICIOS AWS REQUERIDOS

### Amazon EKS (Kubernetes)
- **Estado:** LISTO. Los archivos en `k8s/` contemplan réplicas, límites de recursos (CPU/Memoria) y sondas de salud compatibles con EKS.
- **Acción:** Configurar `aws-load-balancer-controller` para el Ingress.

### Amazon RDS (PostgreSQL 15)
- **Estado:** LISTO. El backend soporta `DATABASE_URL` y utiliza migraciones estándar de Django.
- **Configuración:** Se recomienda Multi-AZ para alta disponibilidad y backups automáticos.

### Amazon S3 (Media & Static)
- **Estado:** LISTO. El backend integra `django-storages` y `whitenoise`.
- **Configuración:** Habilitar CloudFront como CDN para el bucket de S3.

### Amazon ElastiCache (Redis)
- **Estado:** LISTO. Utilizado para Celery y Rate-limiting.
- **Seguridad:** Desplegar en subredes privadas con acceso restringido por Security Groups.

## 2. SEGURIDAD Y CUMPLIMIENTO
- **AWS WAF:** Se recomienda habilitar frente al Application Load Balancer para mitigar ataques SQLi y XSS adicionales a los del middleware interno.
- **IAM Roles:** Utilizar IRSA (IAM Roles for Service Accounts) para que los pods accedan a S3/RDS sin hardcodear credenciales.

## 3. ESTIMACIÓN DE ESCALABILIDAD
Basado en los límites de K8s:
- **Baseline:** 3 Pods Backend (3 vCPU / 3GB RAM total).
- **HPA Target:** 70% CPU para escalar hasta 10 Pods.
- **Capacidad Estimada:** ~1,500 requests/segundo concurrentes.
