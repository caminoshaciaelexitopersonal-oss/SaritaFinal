# ESTRATEGIA DE DESACOPLAMIENTO Y EVENTOS - FASE 4 (SARITA 2026)

Para romper las dependencias directas entre `admin_plataforma` y `mi_negocio`, se implementarán los siguientes patrones dirigidos por eventos.

## 1. PUNTOS DE DESACOPLAMIENTO PRIORITARIOS

| Proceso Actual | Acoplamiento Directo | Nueva Acción (EventBus) |
| :--- | :--- | :--- |
| **Venta SaaS** | `commercial_engine` llama a `AccountingEngine` | Emitir `INVOICE_CREATED` -> Listener Contable genera asiento. |
| **Pago Recibido**| `wallet` llama a `ReciboCaja` (clon) | Emitir `PAYMENT_RECEIVED` -> Listener Tesorería aplica saldo. |
| **Cambio de Plan**| `Subscription` modifica `Company` | Emitir `PLAN_UPGRADED` -> Listener Infra ajusta límites. |
| **Impacto Multi-ERP**| `QuintupleERPService` importa 5 modelos | Emitir `SYSTEM_IMPACT_INTENT` -> Listeners por dominio. |

## 2. MAPEO DE FLUJOS INTER-DOMINIO

### Flujo: Activación de Suscripción (Holding -> Tenant)
1. `CommercialEngine` procesa el pago.
2. `EventBus.emit('SUBSCRIPTION_ACTIVATED', {tenant_id: UUID, plan_code: 'GOLD'})`.
3. **Subscribers:**
   - `AccountingListener`: Registra Ingreso Diferido (Cta 2705).
   - `TenantListener`: Activa permisos de acceso y límites de almacenamiento.
   - `AnalyticsListener`: Actualiza el MRR del Snapshot Engine.

### Flujo: Facturación Operativa (Tenant)
1. `OperacionComercial` se confirma en Mi Negocio.
2. `EventBus.emit('INVOICE_CREATED', {invoice_id: UUID, amount: 500000})`.
3. **Subscribers:**
   - `FinancialLedgerListener`: Registra la transacción en el Ledger Central (Sarita).
   - `DianService`: Encola el envío del XML a la DIAN.
   - `AuditListener`: Genera el hash de integridad en la Blockchain interna.

## 3. PROHIBICIÓN DE IMPORTACIÓN LATERAL
Queda prohibido:
- `from apps.prestadores.mi_negocio import ...` dentro de `admin_plataforma`.
- `from apps.admin_plataforma import ...` dentro de `mi_negocio`.

Toda comunicación debe pasar por `core_erp.event_bus` o por la `Domain Service Layer`.

---
**Estrategia definida por Jules.**
