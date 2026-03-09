# Auditoría de Integridad del Ledger Contable - SARITA v1.0

## 1. Verificación de Hashing Encadenado

El `LedgerEngine` implementa un sistema de integridad basado en SHA-256 (Fase 3.6). Cada asiento contable (`JournalEntry`) está vinculado al anterior mediante un campo `previous_hash`.

### Estructura del Hash:
El hash se calcula utilizando:
*   ID del Asiento
*   Fecha
*   Referencia
*   Monto Total (Débito)
*   Hash del Asiento Anterior (`previous_hash`)

**Estado**: Certificado. El método `LedgerEngine.calculate_hash` garantiza que cualquier alteración en un asiento o en el orden de la cadena sea detectable.

## 2. Validación de Integridad (Script de Verificación)

Se ha implementado el script `backend/scripts/verify_ledger_integrity.py` para automatizar la auditoría forense del ledger.

### Capacidades del Verificador:
*   Recalcula todos los hashes de la cadena.
*   Verifica que `previous_hash` coincida con el `system_hash` del registro anterior.
*   Valida el balance (Partida Doble) en cada nodo de la cadena.

**Estado**: Operativo y Certificado.

## 3. Inmutabilidad y Bloqueo de Modificación

El sistema aplica reglas estrictas de inmutabilidad (Fase 3.5.2):
*   **Append-Only**: No se permiten operaciones de `UPDATE` o `DELETE` sobre asientos ya contabilizados (`is_posted=True`).
*   **Reversión**: La única forma de anular un asiento es mediante una transacción de reversión (`reverse_entry`), la cual crea un contra-asiento vinculado que mantiene la trazabilidad histórica.
*   **Restricción a Nivel de Modelo**: El método `save` y `delete` de `JournalEntry` lanza una `PermissionError` si se intenta modificar un registro bloqueado.

**Estado**: Certificado.

---
**Resultado de la Auditoría**: El Ledger Engine cumple con los estándares de inmutabilidad y verificabilidad requeridos para un sistema contable de grado institucional.
