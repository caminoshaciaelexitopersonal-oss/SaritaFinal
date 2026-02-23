# INTERFACES FORMALES DE SERVICIO - FASE 5 (SARITA 2026)

Para garantizar que las aplicaciones dependan de abstracciones y no de implementaciones concretas, se definen los siguientes contratos en `core_erp.interfaces`.

## 1. `ICommercialService` (Contrato de Ventas y Suscripciones)
```python
class ICommercialService:
    def create_lead(self, data: dict) -> UUID: ...
    def convert_lead(self, lead_id: UUID) -> dict: ...
    def create_subscription(self, tenant_id: UUID, plan_code: str) -> UUID: ...
    def calculate_pricing(self, items: list) -> dict: ...
```

## 2. `IAccountingService` (Contrato Contable)
```python
class IAccountingService:
    def post_journal_entry(self, entry_data: dict) -> UUID: ...
    def validate_balance(self, entry_id: UUID) -> bool: ...
    def get_account_balance(self, account_code: str, period_id: UUID) -> Decimal: ...
    def close_fiscal_period(self, period_id: UUID) -> bool: ...
```

## 3. `ITenantService` (Contrato de Gestión de Inquilinos)
```python
class ITenantService:
    def provision_tenant(self, tenant_data: dict) -> UUID: ...
    def suspend_tenant(self, tenant_id: UUID, reason: str) -> bool: ...
    def update_resource_limits(self, tenant_id: UUID, limits: dict) -> bool: ...
```

## 4. REGLAS DE CONSUMO
1. **Inyección de Dependencias:** Las apps deben inyectar la implementación concreta (ej: `DianAccountingService`) en tiempo de ejecución.
2. **Prohibición de Instanciación:** Ninguna vista en `admin_plataforma` o `mi_negocio` debe instanciar modelos del Core directamente; siempre debe llamar al Servicio correspondiente que implemente estas interfaces.
3. **Persistencia Oculta:** La lógica de base de datos vive dentro del servicio en `core_erp`, no en la aplicación que lo consume.

---
**Diseño de interfaces realizado por Jules.**
