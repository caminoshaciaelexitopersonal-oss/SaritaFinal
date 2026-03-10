# IMPLEMENTATION PLAN: FUNCTIONAL PARITY ALIGNMENT

## Fase 1: Estandarización de Componentes (Semanas 1-2)
- [ ] Extraer componentes UI base (`Button`, `Card`, `Input`) de `interfaz/src/components/ui` a `sarita-platform/shared-ui`.
- [ ] Implementar un sistema de temas (Tailwind config compartido) para garantizar consistencia visual.

## Fase 2: Alineación Dashboard Prestador (Semanas 3-4)
- [ ] **Desktop:** Implementar `RegionalAnalyticsScreen` adaptando los gráficos de la Web.
- [ ] **Mobile:** Refinar `BusinessAccountingScreen` para permitir la creación de asientos manuales (N6 integration).

## Fase 3: Alineación Descubre Turismo (Semanas 5-6)
- [ ] **Desktop:** Implementar la versión completa de `DiscoveryDashboard` consumiendo el SDK de mapas compartido.
- [ ] **Mobile:** Integrar `VirtualGuideScreen` directamente con la navegación de `ExploreStack`.

## Fase 4: Alineación Dashboard Gobierno (Semanas 7-8)
- [ ] **Desktop:** Implementar `TorreControlAdmin` con acceso a `UserManager` y `AuditLog`.
- [ ] **Mobile:** Crear `GovernmentAlertsScreen` para notificaciones P0 en tiempo real.

---
*Roadmap proposed by Jules.*
