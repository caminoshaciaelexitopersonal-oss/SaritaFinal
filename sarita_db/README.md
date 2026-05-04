# SARITA ERP - Módulo "Mi Negocio" (Fase 10.4)

## Arquitectura de Gestión Empresarial

Este submódulo de la base de datos implementa la lógica completa de un ERP soberano para prestadores de servicios turísticos y otros negocios del ecosistema SARITA.

### Dominios Implementados

- `30_mi_negocio/`: Núcleo transaccional de operaciones.
- `31_gestion_comercial/`: CRM, oportunidades y contratos.
- `32-33 operativa/`: Tareas, incidentes y asignación de recursos.
- `34_gestion_archivistica/`: Gestión documental con trazabilidad forense.
- `35_gestion_contable/`: Contabilidad de doble entrada integrada.
- `36-37 financiera/`: Pagos, flujo de caja y analítica predictiva.
- `38-39 catálogos/`: Maestros de clientes y productos/servicios.
- `40_facturacion/`: Facturación electrónica integrada.
- `41_costos/`: Análisis de estructuras de costos.

## Reglas de Operación Real

1. **Atomicidad**: Toda operación comercial debe impactar simultáneamente la contabilidad y el event store.
2. **Cumplimiento**: No se permiten facturas sin operación, ni asientos descuadrados.
3. **Trazabilidad**: Uso obligatorio de `trace_id` para reconstruir el ciclo de vida: `Cliente -> Venta -> Operación -> Factura -> Contabilidad`.
4. **Seguridad**: RLS estricto por `tenant_id` en todas las capas del ERP.
