# Arquitectura del Motor WPA (Workflow de Procesamiento Autónomo)

## 1. Visión General
El WPA es el "músculo" del Sistema SARITA. Su responsabilidad es la ejecución técnica y coordinada de los planes de acción aprobados por el MCP. Opera como un motor de orquestación de procesos asíncronos, garantizando la consistencia mediante el patrón SAGA y proporcionando observabilidad total sobre cada paso ejecutado.

## 2. Componentes Nucleares

### 2.1 Engine Core (El Cerebro Operativo)
- **Interprete de Definiciones:** Lee esquemas JSON que definen los pasos, dependencias y políticas de error de un workflow.
- **Gestor de Instancias:** Crea y persiste el estado de cada ejecución única (`WorkflowInstance`).
- **Planificador (Scheduler):** Determina qué pasos pueden ejecutarse en paralelo y cuáles requieren dependencias previas.

### 2.2 Executor Layer (La Capa de Acción)
- **Service Invoker:** Realiza llamadas a microservicios del PCA, APIs externas o módulos internos.
- **Circuit Breaker:** Protege el sistema evitando llamadas a servicios saturados o caídos.
- **Retrier:** Implementa reintentos con backoff exponencial para fallos transitorios.

### 2.3 State Machine (Máquina de Estados)
- Mantiene la verdad absoluta sobre el progreso del workflow.
- Asegura que las transiciones de estado sean atómicas y persistentes.

### 2.4 Compensation Motor (Gestor de Rollbacks)
- Implementa el **Patrón SAGA**.
- Si un paso falla y agota sus reintentos, el motor activa en orden inverso las acciones de compensación definidas para los pasos ya completados.

## 3. Flujo de Trabajo
1. **Disparo:** El MCP envía una orden de ejecución al WPA con un `workflow_id` y parámetros.
2. **Inicialización:** WPA valida la definición y crea la instancia en estado `CREATED`.
3. **Ejecución:** Se procesan los pasos según el grafo de dependencias.
4. **Monitoreo:** Cada paso reporta éxito o fallo al State Machine.
5. **Cierre:** Al finalizar todos los pasos (o compensaciones), se notifica al MCP y se marca como `COMPLETED` o `ROLLED_BACK`.

## 4. Integración con el Ecosistema
- **MCP:** Único autorizador de workflows.
- **PCA:** Proveedor de inteligencia durante la ejecución si surgen ambigüedades.
- **Audit:** Registro inmutable de cada cambio de estado y ejecución de paso.
