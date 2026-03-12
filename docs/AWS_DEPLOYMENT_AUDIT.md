# AWS DEPLOYMENT AUDIT (SARITA v1.0)
**Estado de Preparación de Infraestructura:** ✅ LISTO (READY)

## 1. Auditoría de Recursos K8s (Amazon EKS)
- **Despliegue:** 3 réplicas base configuradas con HPA hasta 10 pods.
- **Recursos:** Límites definidos (1024Mi RAM / 1000m CPU) para evitar OOMKills.
- **Health Checks:** Liveness y Readiness probes configurados en el puerto 8000.

## 2. Servicios de Datos (RDS / S3)
- **RDS:** Configuración para PostgreSQL 15 multi-tenant validada.
- **S3:** Bucket de archivos estáticos y media con política de acceso restringida verificado.

## 3. Seguridad Perimetral
- **AWS WAF:** Reglas de protección básica contra SQLi y XSS integradas en la directiva de despliegue.
- **JWT:** Firma RS256 mediante llaves privadas en Amazon Secrets Manager o volumen montado.

## 4. Observabilidad
- **Prometheus/Grafana:** El endpoint `/metrics` está expuesto para raspado (scraping) de métricas operacionales.

---
**Veredicto:** La infraestructura está 100% lista para soportar la carga en Amazon Web Services bajo un esquema de alta disponibilidad.
