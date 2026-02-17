# Definición del Stack Tecnológico - Sistema SARITA

## 1. Backend y Lógica de Negocio
- **Lenguaje Principal:** Python 3.12+
- **Framework Web:** Django 5.1 con Django REST Framework (DRF).
- **Asincronía:** Celery con Redis para tareas en segundo plano.

## 2. Frontend y Presentación
- **Framework:** Next.js 15 (App Router).
- **Lenguaje:** TypeScript.
- **Estilos:** Tailwind CSS con componentes Shadcn/ui.
- **Gestión de Estado:** React Context API / TanStack Query.

## 3. Inteligencia Artificial (SADI)
- **Modelos de Lenguaje (LLMs):** OpenAI GPT-4o, Claude 3.5 Sonnet (vía API).
- **Orquestación:** LangChain / LangGraph.
- **Embeddings:** OpenAI text-embedding-3-small.

## 4. Persistencia y Datos
- **Base de Datos Transaccional:** PostgreSQL 16.
- **Base de Datos de Documentos / Cache:** Redis.
- **Base de Datos Vectorial:** Pinecone o pgvector (en PostgreSQL).
- **Almacenamiento de Archivos:** AWS S3 / Google Cloud Storage.

## 5. Infraestructura y DevOps
- **Contenedores:** Docker.
- **Orquestación:** Kubernetes (EKS/GKE).
- **CI/CD:** GitHub Actions.
- **Infraestructura como Código (IaC):** Terraform.

## 6. Observabilidad y Monitoreo
- **Logging:** ELK Stack (Elasticsearch, Logstash, Kibana) o Grafana Loki.
- **Métricas:** Prometheus y Grafana.
- **Trazabilidad:** OpenTelemetry con Jaeger.

## 7. Escalabilidad
- **Escalado Horizontal:** Auto-scaling de pods en Kubernetes basado en CPU/Memoria.
- **Balanceo de Carga:** AWS ALB / Nginx Ingress Controller.
- **Estrategia Multi-Región:** Replicación de base de datos de lectura en regiones secundarias para baja latencia global.

## 8. Tolerancia a Fallos
- **Backups Automáticos:** Diarios con retención de 30 días.
- **Disponibilidad:** Despliegue en múltiples zonas de disponibilidad (Multi-AZ).
- **Protocolo de Recuperación ante Desastres (DRP):** Tiempo de recuperación (RTO) < 4 horas.
