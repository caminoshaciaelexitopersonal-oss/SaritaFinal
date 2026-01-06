# INFORME TÉCNICO – FASE 8: Cierres, Reportes y Fiscalización

## 1. Introducción

Esta fase implementa las funcionalidades críticas para que el sistema sea contablemente cerrable, auditable y fiscalmente coherente.

## 2. Módulo de Cierres Contables

*   **Cómo se cierra:** A través de un endpoint (`/api/v1/mi-negocio/contable/cierres/periodos/{id}/cerrar/`) que invoca al `CierreContableService`.
*   **Qué valida:** El servicio valida que todos los asientos contables del período estén balanceados (débitos = créditos).
*   **Cómo se reapertura:** A través de un endpoint (`.../reabrir/`), accesible solo por administradores.

## 3. Listado de Reportes

| Reporte | Fuente Contable | Período |
|---|---|---|
| Balance General | `Transaction` (Cuentas 1, 2, 3) | `periodo_id` (cerrado) |
| Estado de Resultados | `Transaction` (Cuentas 4, 5, 6) | `periodo_id` (cerrado) |
| Reporte de IVA | `Transaction` (Cuentas 2408, etc.) | `periodo_id` (cerrado) |

## 4. Mapa Fiscal

*   **IVA Generado:** Impactado por el crédito a la cuenta `2408` en el asiento de venta.
*   **IVA Descontable:** Impactado por el débito a las cuentas de IVA en compras.
*   **Gastos de Nómina:** Impactados por los débitos a las cuentas de gasto (`5XXX`) en el asiento de liquidación de nómina.

## 5. Confirmación Explícita

Se confirma que: **"El sistema puede generar reportes fiscales coherentes y auditables"**. Todos los reportes se generan a partir de los datos del módulo de contabilidad (`JournalEntry`, `Transaction`) y solo sobre períodos cerrados.

## 6. Pruebas

Se han añadido pruebas de integración que validan:
*   La correcta generación de asientos contables.
*   La lógica de los reportes.
*   Los controles de bloqueo (no reportes sin cierre).
