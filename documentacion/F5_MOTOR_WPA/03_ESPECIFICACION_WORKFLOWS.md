# Especificación de Definición de Workflows (WPA)

Los workflows en SARITA se definen mediante un esquema JSON que describe la secuencia de tareas, sus dependencias y las acciones de compensación necesarias para garantizar la consistencia sistémica.

## 1. Estructura del Esquema JSON

```json
{
  "workflow_id": "WF_PROCESS_SALE",
  "version": 1,
  "description": "Procesa una venta, descuenta inventario y emite factura",
  "steps": [
    {
      "name": "RESERVE_STOCK",
      "action": "inventory_service.reserve",
      "compensation": "inventory_service.release",
      "timeout": 30,
      "max_retries": 3
    },
    {
      "name": "CHARGE_PAYMENT",
      "action": "payment_service.charge",
      "compensation": "payment_service.refund",
      "timeout": 60,
      "max_retries": 2,
      "depends_on": ["RESERVE_STOCK"]
    },
    {
      "name": "GENERATE_INVOICE",
      "action": "billing_service.generate",
      "compensation": "billing_service.annul",
      "timeout": 30,
      "max_retries": 5,
      "depends_on": ["CHARGE_PAYMENT"]
    }
  ],
  "on_failure": "COMPENSATE",
  "priority": "HIGH"
}
```

## 2. Tipos de Paso (Step Types)

### 2.1 Secuenciales
Pasos que dependen del éxito del paso anterior (`depends_on`).

### 2.2 Paralelos (Fan-out)
Pasos que no tienen dependencias entre sí y pueden ser ejecutados simultáneamente por diferentes workers.

### 2.3 Condicionales
Pasos que se activan solo si el output de un paso anterior cumple con ciertos criterios (ej: "Si monto > 5000, activar PASO_AUDITORIA_MANUAL").

## 3. Políticas de Compensación
- **COMPENSATE (Defecto):** Activa el motor SAGA para revertir pasos previos.
- **RETRY_FOREVER:** Continúa intentando el paso fallido hasta que tenga éxito (solo para pasos no bloqueantes).
- **IGNORE:** Marca el paso como fallido pero continúa con el resto del workflow.

## 4. Versionado de Definiciones
Las definiciones son inmutables. Si se requiere un cambio en la lógica, se debe crear una nueva versión del workflow. El MCP decidirá qué versión invocar basándose en la fecha de la orden o configuración del prestador.
