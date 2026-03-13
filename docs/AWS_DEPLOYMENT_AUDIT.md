# PREPARACIÓN PARA LA IMPLEMENTACIÓN DE AWS (SARITA v1.0)
**Estado:** LISTO

## Arquitectura de Despliegue Sugerida
- **Amazon EKS:** Orquestación de contenedores para backend, workers y frontend.
- **Amazon RDS (PostgreSQL 15):** Base de datos persistente multi-tenant con backups automatizados.
- **Amazon ElastiCache (Redis):** Broker para Celery y cache de middleware (Hardening).
- **Amazon S3:** Almacenamiento de archivos media, documentos archivísticos y backups.
- **AWS WAF:** Protección perimetral para la API contra ataques comunes (SQLi, XSS).

## Validación de Artefactos
- **Docker:** Dockerfile multi-stage optimizado para producción con usuario no-root.
- **Kubernetes:** Manifestos de Deployment, Service y HPA (Horizontal Pod Autoscaler) listos para EKS.
- **Configuración:** Soporte de variables de entorno para secretos y endpoints de AWS.

## Acciones Requeridas para Go-Live
1. Configurar OIDC para IAM Roles for Service Accounts (IRSA) en EKS.
2. Implementar AWS Secrets Manager para claves JWT (RS256 Private Key).
3. Configurar CloudFront como CDN para el frontend web y activos de S3.
