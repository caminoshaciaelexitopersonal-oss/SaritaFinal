# Auditoría Estructural del Core Backend - SARITA v1.0

## 1. Mapeo de Dependencias Internas

El sistema SARITA sigue una arquitectura de "Cerebro Centralizado" donde el módulo `core_erp` provee las capacidades transversales.

### Relaciones de Dependencia:
*   **core_erp**: Módulo base. Provee `TenantAwareModel`, `EventBus`, `AccountingEngine` y `LedgerEngine`.
*   **wallet**: Depende de `core_erp` para la persistencia de impactos financieros y auditoría. Se comunica vía `EventBus`.
*   **delivery**: Depende de `wallet` para liquidación de pagos y de `core_erp` para auditoría operativa.
*   **comercial**: Depende de `core_erp` para la gestión de suscripciones y facturación base.
*   **nomina**: Depende de `core_erp` para la causación de prestaciones y pagos mediante el `LedgerEngine`.
*   **prestadores (Mi Negocio)**: Depende de todos los anteriores para la operación integral.

### Hallazgos de Integridad:
*   **Dependencias Circulares**: No se detectaron dependencias circulares críticas gracias al uso extensivo de `EventBus` y el patrón *Service Layer*. Las importaciones dentro de los modelos están protegidas o desacopladas mediante señales y eventos.
*   **Servicios Duplicados**: Se identificó una transición de servicios legacy a servicios unificados en `wallet`. Se recomienda eliminar `WalletAccountService` en favor de `WalletService`.
*   **Lógica Repetida**: La lógica de validación de balances está centralizada en `LedgerEngine`, evitando duplicidad en los dominios de nómina y facturación.

## 2. Validación de Separación de Capas

### API Layer
*   Las vistas (`views.py`) en `wallet` y `api` actúan como controladores delgados.
*   Utilizan `GovernanceKernel` o servicios específicos para la ejecución.
*   **Estado**: Certificado.

### Service Layer
*   Lógica compleja centralizada en `services.py` de cada módulo (ej. `WalletService`, `JournalService`).
*   Desacoplamiento total de la lógica de negocio de las vistas DRF.
*   **Estado**: Certificado.

### Domain / Data Layer
*   Los modelos (`models.py`) implementan restricciones de integridad y seguridad (ej. Irreversibilidad en `JournalEntry`).
*   Se utiliza `TenantAwareModel` para garantizar el aislamiento de datos (Data Isolation).
*   **Estado**: Certificado.

## 3. Manejo Global de Excepciones

El sistema cuenta con un sistema de normalización de respuestas en `apps/common/`:
*   **Middleware/Handler**: `enterprise_exception_handler` captura errores estándar (400, 401, 403, 404, 500) y los mapea a códigos empresariales (`INVALID_DATA`, `UNAUTHORIZED`, etc.).
*   **Renderer**: `EnterpriseJSONRenderer` garantiza que todas las respuestas sigan el formato:
    ```json
    {
      "success": boolean,
      "data": object | null,
      "meta": object,
      "errors": array | null
    }
    ```
*   **Estado**: Certificado.

---
**Resultado de la Auditoría**: Estructura sólida y modular. Lista para escalamiento en producción.
