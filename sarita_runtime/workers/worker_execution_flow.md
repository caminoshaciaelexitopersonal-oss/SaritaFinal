# FLUJO DE EJECUCIÓN DE WORKERS

## 1. COORDINACIÓN DISTRIBUIDA
Los workers utilizan **Redis** o **Etcd** para la coordinación de locks distribuidos cuando se requiere exclusividad sobre un `tenant_id` o `resource_id`.

## 2. CONCURRENCIA
- Modelo de concurrencia basado en **Goroutines** (Go) para alta densidad de tareas I/O.
- Límites de concurrencia (Throttling) configurables por tipo de worker para evitar saturación de la base de datos central.

## 3. TASK CLAIMING
```mermaid
sequenceDiagram
    Event Bus->>Worker: Envía Evento
    Worker->>Distributed Lock: Intenta adquirir Lock(resource_id)
    Note over Worker: Si lock exitoso...
    Worker->>Worker: Ejecuta Lógica
    Worker->>Event Bus: Ack Evento
    Worker->>Distributed Lock: Libera Lock
```
