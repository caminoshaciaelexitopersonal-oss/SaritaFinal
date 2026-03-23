# DISEÑO TÉCNICO - BLOQUE 2: CENTRAL LEDGER (SARITA HOLDING)

## 1. MODELO: `FinancialLedgerEntry`

Ubicación propuesta: `apps/core_erp/base_models.py` (como clase abstracta) o `apps/admin_plataforma/gestion_contable/models.py`.

```python
class FinancialLedgerEntry(BaseErpModel):
    """
    Libro Mayor Centralizado (Single Source of Truth) para la Holding.
    Captura todo movimiento financiero de cualquier dominio.
    """
    entity_id = models.UUIDField(db_index=True, help_text="ID del Tenant o Entidad responsable.")
    entity_type = models.CharField(max_length=50, db_index=True) # TENANT, HOLDING, PARTNER

    transaction_type = models.CharField(max_length=50, db_index=True) # SUBSCRIPTION, COMMISSION, FEE, REVENUE

    amount = models.DecimalField(max_digits=18, decimal_places=2)
    currency = models.CharField(max_length=3, default='COP')

    direction = models.CharField(max_length=10, choices=[('IN', 'Inbound'), ('OUT', 'Outbound')])

    reference_model = models.CharField(max_length=100) # ej: SaaSInvoice, PaymentOrder
    reference_id = models.UUIDField(db_index=True)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    metadata = models.JSONField(default=dict, blank=True)

    # Audit chaining (RC-S)
    integrity_hash = models.CharField(max_length=64, null=True, blank=True)
```

## 2. EVENTOS FINANCIEROS (FEEDERS)

Los siguientes eventos en el `EventBus` deben disparar una entrada en el Ledger:

1. **`SUBSCRIPTION_ACTIVATED`**: Registro de Revenue inicial.
2. **`PAYMENT_RECEIVED`**: Liquidación de factura y entrada de caja.
3. **`COMMISSION_CALCULATED`**: Registro de gasto por comisión de pasarela o partner.
4. **`USAGE_BILLED`**: Registro de ingresos variables por consumo.
5. **`TRANSFER_EXECUTED`**: Movimientos entre cuentas de la holding.

## 3. POLÍTICA DE INTEGRIDAD
- **Inmutabilidad:** Las entradas en el Ledger no se editan ni eliminan. Solo se anulan mediante una entrada de compensación.
- **Cálculo Derivado:** El MRR y ARR del Dashboard Institucional se consultará mediante:
  `SELECT SUM(amount) FROM FinancialLedgerEntry WHERE transaction_type='SUBSCRIPTION' AND timestamp >= ...`

---
**Diseño propuesto por Jules.**
