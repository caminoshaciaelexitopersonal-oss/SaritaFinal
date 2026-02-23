# ESTÁNDARES DE HERENCIA Y NOMENCLATURA - FASE 3 (SARITA 2026)

Para garantizar la integridad y coherencia del núcleo ERP, se establecen los siguientes estándares obligatorios para todos los modelos en `core_erp`.

## 1. ESTÁNDAR TÉCNICO DE MODELOS

Todos los modelos deben heredar de `BaseErpModel` (o sus derivados en Core) y cumplir con:

1.  **Identificador Único:** `UUIDField(primary_key=True, default=uuid.uuid4, editable=False)`.
2.  **Naming Convention:** 100% Technical English para nombres de clases y campos (ej: `is_posted` en lugar de `esta_contabilizado`).
3.  **Trazabilidad (Audit Fields):** `created_at`, `updated_at` (incluidos en `BaseErpModel`).
4.  **Integridad Forense:** Campo `integrity_hash` para modelos críticos (opcional pero recomendado para Ledger).
5.  **Soft Delete:** Se debe implementar `is_deleted` y `deleted_at` en la base del core.

## 2. ACTUALIZACIÓN PROPUESTA A `BaseErpModel`

```python
class BaseErpModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Soft Delete Standard
    is_deleted = models.BooleanField(default=False, db_index=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
```

## 3. MODELOS LEGACY A ELIMINAR/MIGRAR

| Modelo Legacy | Problema Detectado | Acción |
| :--- | :--- | :--- |
| `Reserva` (Admin/Tenant) | Spanish Naming, Duplicate | Migrar a `operational_domain.BaseBooking` |
| `FacturaVenta` (Admin/Tenant) | Spanish Naming, Mirroring | Migrar a `commercial_domain.BaseInvoice` |
| `Empleado` (Admin) | Spanish Naming, Integer PK | Migrar a `operational_domain.BaseEmployee` |
| `Cuenta` (Tenant) | Spanish Naming, Partial Core | Migrar a `accounting_domain.LedgerAccount` |

## 4. REGLA DE CI (CONTINUOUS INTEGRATION)
Se implementará un check que rechace cualquier PR que introduzca modelos en `core_erp` o dominios ERP de las apps con:
- Llaves primarias de tipo `AutoField` / `BigAutoField` (Integer).
- Campos en español.

---
**Ratificado por Jules.**
