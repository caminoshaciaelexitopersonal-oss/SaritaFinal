# ESTRATEGIA TEMPORAL.IO PARA SARITA

## 1. NAMESPACES
- `sarita-finance`: Workflows financieros críticos.
- `sarita-tourism`: Orquestación de reservas y servicios.
- `sarita-infra`: Tareas de mantenimiento y escalamiento autónomo.

## 2. ACTIVIDADES (ACTIVITIES)
Las actividades son las unidades de trabajo real ejecutadas por los workers:
- `ProcessPayment`
- `UpdateInventory`
- `GenerateInvoice`
- `TriggerAIAnalysis`

## 3. TIMEOUTS Y RETRIES
Cada actividad tiene políticas de reintento granulares, permitiendo que una falla en una API externa de pagos no mate todo el proceso de reserva, sino que lo reintente de forma inteligente.
