# Checklist de Interoperabilidad Frontend: Gestión Comercial

## 1. Alineación con el Sistema General

| Criterio | Estado | Observaciones |
| :--- | :--- | :--- |
| **Layout y Navegación Consistente** | ✅ **OK** | La página de `gestion-comercial` y sus sub-páginas utilizan el layout principal del dashboard, incluyendo el `Sidebar` y el `Header`. La navegación es coherente. |
| **Breadcrumbs (Migas de Pan)** | ❕ **NO IMPLEMENTADO** | El sistema en general carece de un sistema de breadcrumbs, por lo que este módulo es consistente con el resto, pero es una mejora de UX a considerar globalmente. |
| **Estilos y Componentes de UI** | ✅ **OK** | Se utilizan los componentes reutilizables de `components/ui` (Button, Card, Table, etc.), manteniendo la consistencia visual. No hay "islas de UX". |

## 2. Validación de Flujo de Datos

| Criterio | Estado | Observaciones |
| :--- | :--- | :--- |
| **Datos Provienen Exclusivamente del Backend** | ✅ **OK** | Todas las vistas (`Listar Facturas`, `Nueva Factura`) consumen datos de la API a través de los hooks `useComercialApi` o `useMiNegocioApi`. |
| **Ausencia de Mock Data** | ✅ **CORREGIDO** | El formulario de `Nueva Factura` utilizaba `mockProductos`. Esto fue corregido en la Fase 2 para usar el endpoint `getProductos`. |
| **Ausencia de Lógica de Negocio en Componentes**| ❕ **MEJORABLE** | El formulario `NuevaVentaPage.tsx` calcula el total de la línea (`cantidad * precio_unitario`) en el JSX. Si bien es menor, esta lógica debería delegarse idealmente al backend para ser la única fuente de verdad. Se documenta como una recomendación, ya que no rompe la funcionalidad. |

## 3. Integración con Otros Módulos en UI

| Módulo Externo | Integración Esperada | Estado | Observaciones |
| :--- | :--- | :--- | :--- |
| 📦 **Inventario** | El formulario de `Nueva Factura` debe listar productos del inventario. | ✅ **OK** | El `Select` de productos ahora consume el endpoint de `getProductos`, mostrando los productos reales del tenant. |
| 📒 **Contabilidad**| Una factura creada debe ser visible/trazable en un módulo de contabilidad. | ❕ **NO IMPLEMENTADO** | Como la UI de `gestion_contable` no existe, no es posible verificar esta trazabilidad visualmente. La integración a nivel de backend sí funciona. |
| 💰 **Finanzas** | El registro de un pago a una factura debe ser visible/trazable en un módulo financiero. | ❕ **NO IMPLEMENTADO** | La UI para registrar pagos y ver transacciones financieras no está completamente implementada, por lo que no se puede verificar visualmente. La integración a nivel de backend sí funciona. |

## Conclusión

El frontend de `gestion_comercial` está **razonablemente bien integrado**. Respeta la UX global y consume datos reales. Sin embargo, su integración visual con otros módulos está **limitada por la ausencia de las interfaces de usuario** para dichos módulos (Contabilidad, Finanzas).
