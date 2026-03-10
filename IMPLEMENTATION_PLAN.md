# IMPLEMENTATION PLAN - PLATFORM PARITY

## FASE 1: ESTANDARIZACIÓN DE ESTRUCTURA (7 días)
- **Acción:** Crear los stubs de carpetas faltantes para asegurar la arquitectura `dashboard-admin`, `dashboard-prestador`, `descubre-turismo` en todas las plataformas.
- **Nomenclatura:** Unificar nombres de rutas y servicios.

## FASE 2: SHARED-UI INITIALIZATION (14 días)
- **Acción:** Migrar componentes básicos (Buttons, Inputs, Spinners) de la Web al `shared-sdk` o a una nueva carpeta `shared-ui` si se opta por un monorepo real.
- **Herramienta:** Tailwind CSS para estilos consistentes.

## FASE 3: CIERRE DE BRECHAS - DESKTOP (10 días)
- **Acción:** Implementar `DiscoveryDashboard` en Desktop consumiendo las APIs existentes de `Atractivos` y `Rutas`.
- **Objetivo:** Lograr que el Ciudadano pueda usar Desktop para planear su viaje.

## FASE 4: CIERRE DE BRECHAS - MOBILE (10 días)
- **Acción:** Implementar `RegionalAnalytics` en el `AdminDashboard` de Mobile.
- **Objetivo:** Permitir que el Gobierno tome decisiones desde el territorio.

## FASE 5: VALIDACIÓN Y CERTIFICACIÓN (5 días)
- **Acción:** Pruebas cruzadas de sincronización (Ej: Venta en Desktop -> Ver en Mobile -> Reporte en Web).
