# DISEÑO TÉCNICO - BLOQUE 3: OPERATIONAL SNAPSHOT ENGINE (SARITA)

## 1. MODELO: `SystemSnapshot`

```python
class SystemSnapshot(BaseErpModel):
    """
    Captura periódica del estado de salud y rendimiento del Holding y sus Tenants.
    """
    # Métricas de Inquilinos
    total_tenants = models.IntegerField()
    active_tenants = models.IntegerField()
    churned_tenants_last_30d = models.IntegerField()

    # Métricas Financieras (Agregadas desde el Ledger)
    total_mrr = models.DecimalField(max_digits=18, decimal_places=2)
    total_arr = models.DecimalField(max_digits=18, decimal_places=2)
    failed_payments_count = models.IntegerField()

    # Métricas de Salud Técnica
    system_health_score = models.FloatField(help_text="0.0 a 1.0")
    active_critical_alerts = models.IntegerField()
    avg_response_time_ms = models.IntegerField()

    # Metadatos del Snapshot
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    snapshot_type = models.CharField(max_length=20, default='DAILY') # HOURLY, DAILY, MONTHLY
```

## 2. MOTOR DE AGREGACIÓN (SNAPSHOT ENGINE)

El servicio `SnapshotEngine` ejecutará tareas programadas (Celery) para:
1. Consultar el `FinancialLedgerEntry` para métricas monetarias.
2. Consultar el `Identity Core` para conteo de tenants.
3. Consultar los logs de errores y alertas para el `system_health_score`.
4. Persistir el objeto `SystemSnapshot`.

## 3. DASHBOARD INSTITUCIONAL (FRONTEND)

El Dashboard en `interfaz/admin-plataforma/analitica/holding` consumirá estos snapshots para mostrar:
- **Línea de Tiempo de MRR:** Basada en la serie histórica de snapshots.
- **Mapa de Calor de Salud:** Basado en el `system_health_score` por región/dominio.
- **Alertas Críticas:** Listado de impedimentos activos.

---
**Diseño propuesto por Jules.**
