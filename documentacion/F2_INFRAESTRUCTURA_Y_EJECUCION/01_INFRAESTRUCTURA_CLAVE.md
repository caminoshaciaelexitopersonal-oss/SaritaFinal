# Documento de Infraestructura y Selección de Entorno - Sistema SARITA

## 1. Modelo de Infraestructura
Se selecciona una **Infraestructura de Cloud Pública con Arquitectura Multi-Región**.

Esta decisión se basa en la necesidad de:
- **Disponibilidad Global:** Baja latencia para usuarios en diferentes geografías.
- **Tolerancia a Fallos:** Capacidad de failover entre regiones en caso de caída masiva.
- **Escalabilidad Infinita:** Aprovechamiento de la infraestructura bajo demanda.

## 2. Evaluación de Proveedor Cloud
Se ha realizado una comparativa técnica entre los principales proveedores:

| Criterio | Amazon Web Services (AWS) | Google Cloud Platform (GCP) | Microsoft Azure |
| :--- | :---: | :---: | :---: |
| **K8s Administrado** | EKS (Excelente/Maduro) | GKE (Líder en facilidad) | AKS (Bueno) |
| **IAM & Seguridad** | Muy Robusto (Granular) | Muy Integrado | Basado en AD |
| **Presencia Global** | Líder (245+ Servicios) | Alta (IA fuerte) | Alta (Empresarial) |
| **Bases de Datos** | RDS / Aurora (Líder) | Cloud SQL | Azure SQL |

**Selección Oficial:** **Amazon Web Services (AWS)**.
*Razón:* EKS es el estándar de la industria para microservicios de gran escala, su ecosistema de seguridad (IAM/KMS) es el más granular y su capacidad de replicación global (Global Tables, Aurora Global) es superior para el modelo SARITA.

## 3. Estrategia de Regiones y Disponibilidad
- **Región Primaria:** `us-east-1` (N. Virginia).
- **Región Secundaria (DR):** `us-west-2` (Oregon) o `eu-central-1` (Frankfurt).
- **Zonas de Disponibilidad (AZ):** Mínimo 3 AZs por región para garantizar alta disponibilidad (HA).

## 4. Servicios Gestionados Seleccionados
- **Cómputo:** AWS EKS (Elastic Kubernetes Service).
- **Base de Datos:** AWS RDS (PostgreSQL) con Multi-AZ.
- **Cache:** AWS ElastiCache (Redis).
- **Almacenamiento:** AWS S3 (Simple Storage Service).
- **Red:** AWS VPC, Route 53, CloudFront (CDN).
- **Seguridad:** AWS IAM, Secrets Manager, AWS WAF, AWS Shield.

## 5. Modelo de Carga y Costos
- **Uso de Reserved Instances / Savings Plans:** Para el núcleo del sistema (MCP).
- **Spot Instances:** Para tareas de procesamiento asíncrono no críticas (SADI - Workers).
