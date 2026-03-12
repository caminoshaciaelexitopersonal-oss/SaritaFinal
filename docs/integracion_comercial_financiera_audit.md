# Auditoría de Integración Comercial ↔ Financiera (Super Administrador)

## 1. Mapeo de Flujos Identificados

### 1.1 Activación de Suscripciones
- **Módulo Origen:** `apps.comercial.engines.subscription_engine`
- **Módulo Destino:** `apps.admin_plataforma.gestion_contable.contabilidad`
- **Evidencia Técnica:** El `BillingEngine.generate_invoice` invoca a `_create_accounting_impact` tras validar una factura.
- **Impacto Contable:** Se genera un asiento en el ERP de Sarita (Holding) afectando:
  - **Débito:** Cuenta 130505 (Clientes Nacionales SaaS)
  - **Crédito:** Cuenta 413501 (Ingresos por Suscripciones)

### 1.2 Facturación Recurrente
- El `BillingEngine` está diseñado para ciclos mensuales y anuales.
- Calcula excesos de uso (ej. Almacenamiento GB) mediante `UsageMetric` y aplica `PricingRule`.

### 1.3 Estado de Integración Real
| Componente | Estado | Hallazgo Crítico |
|------------|--------|-------------------|
| Modelos BD | 🟢 Maduro | Estructura de cuentas y asientos alineada con Core ERP. |
| Motores (Engines) | 🟡 Parcial | El `BillingEngine` está acoplado pero requiere hardening en el manejo de errores. |
| Integración Contable | 🔴 Crítico | Existen discrepancias entre el esquema físico de SQLite y las definiciones de Django (conflictos de nombres de columnas y tipos de datos en `admin_contabilidad`). |

## 2. Autonomía Financiera de Sarita

- **Plan de Cuentas:** Independiente y desacoplado de los tenants. Utiliza `organization_id` vinculada al `ProviderProfile` de Sarita Holding.
- **Capacidad de Reportes:** Estructuralmente capaz de generar Balance General y Estado de Resultados, pero actualmente bloqueado por inconsistencias en la base de datos física.

## 3. Diagnóstico de Vacíos y Riesgos

1. **Riesgo Técnico:** La base de datos `default` tiene tablas de `admin_contabilidad` con columnas en español (`codigo`, `debito`) mientras que los modelos esperan inglés (`code`, `debit`), producto de una refactorización incompleta.
2. **Vacío Funcional:** No se detectó lógica de ajuste automático para ingresos diferidos en cancelaciones a mitad de ciclo.
3. **Integración de Excesos:** La captura de métricas de uso está implementada, pero no hay un proceso programado (Celery) visible que automatice la facturación masiva al cierre del mes.

## 4. Recomendaciones Inmediatas

1. **Saneamiento de BD:** Forzar la recreación de las tablas de `admin_contabilidad` usando UUIDs consistentes.
2. **Hardening de Signals:** Asegurar que `handle_subscription_accounting` sea idempotente para evitar duplicidad de asientos contables.
3. **Frontend:** Exponer los KPIs de MRR y Churn Rate que ya se calculan en `DashboardService`.

---
*Auditoría realizada por Jules.*
