# Blueprint de Arquitectura Global SARITA v1.0

## 1. Visión General de Microservicios
La plataforma evoluciona de un monolito modular a un ecosistema de microservicios distribuidos, optimizando la escalabilidad y el aislamiento de fallos.

### 1.1 Catálogo de Servicios
| Servicio | Stack | Base de Datos | Tipo |
| :--- | :--- | :--- | :--- |
| **Auth Service** | Django / JWT | PostgreSQL (Auth) | Núcleo |
| **Ledger Service** | Go / Python | PostgreSQL (Ledger) | Crítico |
| **Wallet Service** | Node.js | MongoDB / Redis | Transaccional |
| **Inventory Service** | Python | PostgreSQL (Ops) | Operativo |
| **Notification Service** | Go | Redis (Queue) | Borde |
| **AI Agent Service** | Python / LangGraph | Vector DB (Pinecone) | Inteligencia |

## 2. Capa de Comunicación e Interoperabilidad

### 2.1 Comunicación Síncrona (gRPC / REST)
*   **gRPC**: Utilizado para comunicación interna de alta velocidad entre el Ledger Service y el Wallet Service (latencia < 10ms).
*   **REST**: Interfaz pública para clientes Web, Mobile y Desktop a través del API Gateway.

### 2.2 Columna Vertebral de Eventos (Kafka)
Implementación de una arquitectura **Event-Driven** mediante Apache Kafka.
*   **Topic: `sales.v1.completed`**: Dispara simultáneamente la actualización de inventario, el posteo contable y la notificación al cliente.
*   **Patrón Outbox**: Garantiza que los eventos se publiquen solo si la transacción local en la base de datos del servicio fue exitosa.

## 3. Infraestructura Cloud Nativa

### 3.1 Orquestación y Escalado
*   **Kubernetes (K8s)**: Gestión de pods con **Horizontal Pod Autoscaler (HPA)** configurado para escalar ante picos de tráfico regional (ej. temporadas turísticas).
*   **Service Mesh (Istio)**: Implementación de **Circuit Breakers** y trazabilidad distribuida.

### 3.2 Estrategia Multi-Región
Despliegue distribuido para reducción de latencia y recuperación ante desastres:
*   **Región A (Latam-South)**: Nodo principal de procesamiento.
*   **Región B (Latam-North)**: Réplica de lectura y failover automático.

## 4. Gestión de Datos y Big Data

*   **Data Lake**: Ingesta de eventos de Kafka hacia un Data Warehouse (BigQuery/Redshift) para análisis macroeconómico regional.
*   **Caché Distribuida**: Cluster de Redis para gestión de estado global y rate limiting.

---
**Arquitectura aprobada para escalamiento a millones de usuarios.**
*Jules, Lead AI Architect.*
