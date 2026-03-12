# AUDITORÍA DE ACOPLAMIENTO - BLOQUE 4: REDUCCIÓN DE ACOPLAMIENTO (SARITA)

## 1. CUELLOS DE BOTELLA POR IMPORTACIÓN DIRECTA (Riesgo Alto)

| Archivo Origen | Componente Importado | Dominio Destino | Riesgo |
| :--- | :--- | :--- | :--- |
| `QuintupleERPService` | `Reserva`, `AsientoContable`, `OrdenPago`, `OperacionComercial` | Mi Negocio (Múltiples) | Crítico (Acoplamiento Total) |
| `InteroperabilityBridge` | `Reserva` | Mi Negocio (Operativo) | Medio |
| `Sarita Agents` (Tasks) | `SargentoContable`, `SargentoComercial`, `SargentoOperativo` | Mi Negocio (Sargentos) | Alto |
| `Sarita Agents` (Soldados)| `Cuenta`, `Transaccion`, `Presupuesto` | Mi Negocio (Contable/Fin) | Medio |

## 2. ACOPLAMIENTO CIRCULAR DETECTADO

- **Ciclo:** `mi_negocio/gestion_comercial/domain/sargentos.py` importa `sarita_agents/orchestrator.py`, y `sarita_agents/tasks.py` importa sargentos de `mi_negocio`.
- **Efecto:** Imposibilidad de separar paquetes o desplegar microservicios sin romper la integridad del sistema.

## 3. ESTRATEGIA DE DESACOPLAMIENTO (MIGRACIÓN A EVENTOS)

Se deben reemplazar las importaciones directas en `QuintupleERPService` y `sarita_agents` por:

1. **`EventBus.emit(event_type, payload)`**: Para notificar impactos financieros y operativos.
2. **`ServiceInterfaces`**: Definidas en `core_erp` para que los dominios registren sus capacidades sin que el orquestador conozca las clases concretas.
3. **`Proxy Models`**: Uso de referencias por UUID en lugar de `ForeignKey` directas a modelos de otros dominios.

---
**Análisis de acoplamiento realizado por Jules.**
