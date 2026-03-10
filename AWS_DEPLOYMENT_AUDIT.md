# AWS DEPLOYMENT AUDIT – SISTEMA SARITA

## 1. COMPATIBILIDAD DE SERVICIOS

| Servicio AWS | Estado | Configuración Detectada |
| :--- | :--- | :--- |
| **Amazon EKS** | ✅ LISTO | Manifiestos K8s incluyen Deployments, Services y HPA (3-10 réplicas). |
| **Amazon RDS** | ✅ LISTO | Configuración multibase activa. Soporta PostgreSQL 15 con aislamiento lógico. |
| **Amazon S3** | ✅ LISTO | Integración vía `django-storages` y `boto3`. Soporta almacenamiento de evidencias. |
| **AWS WAF** | ✅ LISTO | Middleware de backend añade headers de seguridad y protección contra replay attacks. |
| **Amazon ElastiCache** | ✅ LISTO | Integración con Redis 7 para Celery y Caché de sistema. |

## 2. PREPARACIÓN DE INFRAESTRUCTURA (IaC)
- **Docker:** Imágenes multi-etapa optimizadas basadas en `python:3.11-slim`.
- **Kubernetes:**
    - `livenessProbe` y `readinessProbe` apuntan a `/api/v1/infra/health/`.
    - Gestión de secretos vía `envFrom`.
- **CI/CD:** Pipelines de GitHub Actions listos para despliegue inmutable a ECS/EKS.

## 3. SEGURIDAD EN LA NUBE
- **Cifrado en Reposo:** Soportado por la capa de modelos (`EncryptedTextField`).
- **Aislamiento:** El `DatabaseRouter` permite mover `wallet` y `delivery` a instancias RDS separadas sin cambios en el código.
- **Protección Perimetral:** Cloudflare/WAF ready mediante configuración de headers.

## 4. PRÓXIMOS PASOS AWS
1. Provisionar el cluster EKS mediante Terraform/CloudFormation.
2. Configurar el Ingress Controller con certificados SSL de ACM.
3. Ejecutar migraciones iniciales de base de datos en RDS multi-AZ.
