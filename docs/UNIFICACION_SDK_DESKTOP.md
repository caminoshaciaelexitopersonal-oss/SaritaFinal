# UNIFICACIÓN SDK DESKTOP - SARITA
**Estado:** VALIDADO

## 1. CENTRALIZACIÓN DE CONSUMO
Se ha verificado la unificación de los contratos API para la aplicación de Escritorio.

| Módulo Desktop | Estado de Migración | Dependencia |
| :--- | :---: | :--- |
| **Auth** | 100% | `@sarita/shared-sdk` |
| **ERP (Business)** | 100% | `@sarita/shared-sdk/api` |
| **Fintech (Wallet)** | 100% | `@sarita/shared-sdk/wallet` |
| **Logistics** | 100% | `@sarita/shared-sdk/delivery` |

## 2. INTEGRIDAD DE CONTRATOS
- **Modelos:** Desktop comparte los tipos TypeScript definidos en el Shared SDK.
- **Validaciones:** Se utiliza el mismo pipeline de interceptores de Axios para el manejo de Nonce (`X-Sarita-Nonce`) y rotación de JWT.
- **Sync Engine:** Las operaciones offline de Desktop (almacenadas en SQLite local via `electron-db`) utilizan el mismo protocolo de reconciliación que Mobile.

## 3. BENEFICIOS OBTENIDOS
- Eliminación de discrepancias en payloads de pedidos.
- Garantía de que las reglas de negocio (precios dinámicos, impuestos) se aplican de forma idéntica en POS Web y POS Desktop.
- Facilidad de mantenimiento: un cambio en el SDK se refleja en todas las plataformas.

**Conclusión:** Desktop ahora opera como un cliente puro del ecosistema SARITA, sin lógica de API redundante.
