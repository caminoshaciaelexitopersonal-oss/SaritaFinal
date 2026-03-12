# PREPARACIÓN PARA LA IMPLEMENTACIÓN DE AWS
**Estado:** LISTO

## Arquitectura de Despliegue Sugerida
- **Amazon EKS:** Orquestación de contenedores para backend, workers y frontend.
- **Amazon RDS (PostgreSQL 15):** Base de datos persistente multi-tenant.
- **Amazon ElastiCache (Redis):** Broker para Celery y cache de middleware.
- **Amazon S3:** Almacenamiento de archivos media y documentos archivísticos.
- **AWS WAF:** Protección perimetral para la API.

## Validación de Artefactos
- **Docker:** Dockerfile multi-stage optimizado para producción.
- **Kubernetes:** Manifestos de Deployment, Service y HPA listos para EKS.
- **Configuración:** Soporte de variables de entorno para secretos y endpoints de AWS.

## Acciones Requeridas
1. Configurar OIDC para IAM Roles for Service Accounts (IRSA) en EKS.
2. Implementar AWS Secrets Manager para claves JWT y Pepper de encriptación.
3. Configurar CloudFront como CDN para el frontend y S3.
