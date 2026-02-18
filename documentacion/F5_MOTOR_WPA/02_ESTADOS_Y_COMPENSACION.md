# Modelo de Estados y Compensación (WPA)

El WPA garantiza la integridad del sistema incluso ante fallos parciales mediante una máquina de estados robusta y un motor de compensación basado en Sagas.

## 1. Ciclo de Vida del Workflow

| Estado | Descripción |
| :--- | :--- |
| **`CREATED`** | Instancia creada y lista para ser programada. |
| **`RUNNING`** | Pasos en ejecución activa. |
| **`WAITING`** | Pausado a la espera de un evento externo o aprobación adicional del MCP. |
| **`COMPLETED`** | Todos los pasos y sus verificaciones terminaron con éxito. |
| **`FAILED`** | Un paso crítico falló y se agotaron los reintentos. |
| **`COMPENSATING`** | Ejecutando acciones de reversión para los pasos previamente exitosos. |
| **`ROLLED_BACK`** | Sistema restaurado al estado anterior al workflow (lógicamente). |
| **`CANCELLED`** | Detenido manualmente por el MCP antes de finalizar. |

## 2. El Patrón SAGA (Compensación Transaccional)
Dado que el sistema es distribuido (microservicios), no podemos usar transacciones ACID globales. Usamos Sagas:

### 2.1 Definición de Paso (Step)
Cada paso en el workflow debe definir:
- **Acción:** La tarea técnica a realizar.
- **Compensación:** La tarea necesaria para "deshacer" la acción (ej: si la acción es "Cargar Pago", la compensación es "Reembolsar Pago").

### 2.2 Flujo de Fallo
1. **Paso N falla.**
2. El WPA marca el workflow como `FAILING`.
3. El Motor de Compensación identifica los Pasos **1 a N-1** que fueron exitosos.
4. Se ejecutan las **Compensaciones 1 a N-1** en orden inverso.
5. Si una compensación falla, se eleva a **Intervención Humana Soberana**.

## 3. Políticas de Resiliencia

### 3.1 Reintentos (Retries)
- **Backoff Exponencial:** 2s, 4s, 8s, 16s...
- **Jitter:** Añade ruido aleatorio para evitar el efecto manada.

### 3.2 Timeouts
- Cada paso tiene un tiempo máximo de ejecución. Si se supera, se considera fallo del paso.

### 3.3 Circuit Breaker
- Si el WPA detecta que un servicio externo falla repetidamente para múltiples workflows, abre el circuito y falla inmediatamente los pasos nuevos que dependan de ese servicio, evitando degradación en cascada.
