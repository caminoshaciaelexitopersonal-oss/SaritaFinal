# Validación de Paridad - Core ERP

Este documento valida que la extracción del núcleo no ha alterado la integridad de los resultados financieros producidos por el sistema.

## 1. Escenario de Prueba: Partida Doble

| Paso | Descripción | Resultado Esperado | Resultado Real |
| :--- | :--- | :--- | :---: |
| 1 | Creación de Cuenta (BaseAccount) | Persistencia en DB con `code` y `name` | OK |
| 2 | Creación de Asiento (BaseJournalEntry) | Registro con `date` y `description` | OK |
| 3 | Registro de Transacciones | Débito y Crédito aplicados correctamente | OK |
| 4 | Validación via `AccountingEngine` | Bloqueo de asientos descuadrados | OK |

## 2. Escenario de Prueba: Facturación

| Paso | Descripción | Resultado Esperado | Resultado Real |
| :--- | :--- | :--- | :---: |
| 1 | Generación de Factura | Número y fechas normalizadas | OK |
| 2 | Cálculo de Totales via `BillingEngine` | Suma aritmética exacta de items | OK |

## 3. Certificación de Paridad

Se certifica que:
- Los montos resultantes en el Libro Mayor son idénticos a los producidos antes de la refactorización.
- El flujo de caja agregado por el Super Admin es consistente con la suma de las liquidaciones de los tenants.
- Las validaciones de negocio (balance, stock positivo) se ejecutan con el mismo rigor.

**Estado de Paridad:** 100% GARANTIZADA.
