# Documento Oficial de Arquitectura - Sistema SARITA

## 1. Visión General
El Sistema SARITA está diseñado como una plataforma de escala global para la gestión turística y empresarial, integrando inteligencia artificial avanzada con un núcleo operativo robusto. La arquitectura se fundamenta en la soberanía de datos, la trazabilidad absoluta y la escalabilidad horizontal.

## 2. Tipo de Arquitectura Base
Se define formalmente el uso de una **Arquitectura de Microservicios con Event Bus Central**.

- **Microservicios:** Cada dominio de negocio (Hoteles, Transporte, Agencias, Finanzas, etc.) opera como un servicio independiente, permitiendo despliegues desacoplados y escalado selectivo.
- **Event Bus Central:** La comunicación entre servicios se realiza de forma asíncrona mediante un bus de eventos (e.g., RabbitMQ o Kafka), garantizando la consistencia eventual y reduciendo el acoplamiento directo.
- **Arquitectura Híbrida (Operacional):** Para el núcleo de gestión inmediata (ERP), se utiliza un enfoque de "Monolito Modular" que facilita la integridad transaccional, mientras que los servicios periféricos y de IA se despliegan como microservicios.

## 3. Diseño de Capas del Sistema

### Capa 1 — Presentación
- **Interfaces:** Aplicaciones Web (Next.js 15), Aplicaciones Móviles nativas y Dashboards de administración.
- **APIs Externas:** Gateways para integración con terceros (Pasarelas de pago, GDS turísticos).
- **SDKs:** Librerías para que proveedores externos consuman servicios de SARITA.

### Capa 2 — Orquestación
- **Coordinador Principal:** Gestiona el flujo de trabajo entre servicios.
- **Gateway de Agentes AI:** Punto de entrada único para solicitudes de inteligencia artificial.
- **Motor de Reglas:** Validador centralizado de políticas de negocio y gobernanza.

### Capa 3 — Servicios de Dominio
- **Lógica de Negocio:** Implementación de las verticales turísticas (Hoteles, Bares, Guías, Transporte, Agencias).
- **Servicios Independientes:** Facturación, Inventario, Nómina, Contabilidad.
- **Validadores:** Componentes que aseguran la integridad de los datos antes de la persistencia.

### Capa 4 — Capa de Inteligencia Artificial (SADI)
- **Agentes Especializados:** Entidades autónomas para tareas específicas (Logística, Ventas, Auditoría).
- **Motor de Razonamiento:** Procesamiento de lenguaje natural y toma de decisiones lógica.
- **Motor de Memoria:** Persistencia de contexto a corto y largo plazo para interacciones coherentes.
- **Motor de Aprendizaje Adaptativo:** Mejora continua basada en el feedback del sistema y usuarios.

### Capa 5 — Persistencia
- **Base de Datos Transaccional:** PostgreSQL con soporte para multitenancy.
- **Base de Datos Analítica:** ClickHouse para reportes masivos y análisis de tendencias.
- **Almacenamiento de Logs:** Registro inmutable de eventos y auditoría forense.
- **Almacenamiento de Embeddings:** Bases de datos vectoriales (e.g., Pinecone o pgvector) para memoria de agentes.

### Capa 6 — Infraestructura
- **Contenedores:** Docker para empaquetamiento de servicios.
- **Orquestador:** Kubernetes (K8s) para gestión de clústeres y auto-escalado.
- **Balanceadores:** Nginx / HAProxy para distribución de carga.
- **Monitoreo:** Prometheus y Grafana para observabilidad total.

## 4. Definición de Límites Operativos
- **Aislamiento de Datos:** Cada prestador tiene su propio esquema/dominio de datos.
- **Soberanía:** Los datos de identidad residen en el nodo de origen.
- **Atomicidad:** Las transacciones financieras deben ser atómicas y verificadas por el GovernanceKernel.
