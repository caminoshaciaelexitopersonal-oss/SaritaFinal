# EVALUACIÓN DE RIESGO ESTRUCTURAL (FASE 0)

## 1. RIESGOS OPERATIVOS INMEDIATOS
Identificación de puntos críticos que podrían verse afectados durante la cirugía estructural.

| Riesgo | Impacto | Mitigación |
| :--- | :---: | :--- |
| **Migraciones en Vuelo** | Alto | Prohibir nuevas migraciones funcionales durante F0-F6. Solo migraciones de esquema técnico (UUID). |
| **Integración DIAN** | Crítico | Mantener el `InvoicingEngine` intacto en `core_erp` y solo refactorizar los conectores. |
| **Consistencia de Datos** | Alto | Realizar snapshots de base de datos antes de cada fase de migración de modelos legacy. |
| **Idempotencia IA** | Medio | Validar que el `EventBus` registre correctamente las intenciones para evitar ejecuciones dobles durante el desacoplamiento. |

---

## 2. PUNTOS DE FALLO CRÍTICOS
*   **QuintupleERPService:** Actualmente centraliza el impacto sistémico pero está altamente acoplado. Su fallo detiene toda la contabilidad del sistema.
*   **Sarita Orchestrator:** Depende de los `Sargentos` de `mi_negocio`. Un cambio en la firma de un sargento rompería la orquestación IA.

---

## 3. PLAN DE CONTINGENCIA
En caso de fallo estructural grave durante la consolidación:
1.  **Reversión Automática:** Uso de Git para volver al estado Snapshot Baseline.
2.  **SAGA Compensation:** El motor WPA (`wpa_core.py`) debe estar activo para revertir cualquier impacto parcial en el ERP si un workflow de consolidación falla.

---
**Evaluación realizada por:** Jules
**Estado:** Monitoreo Activo
