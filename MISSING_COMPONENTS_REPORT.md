# MISSING COMPONENTS REPORT

## 1. BRECHAS CRÍTICAS (DEBEN IMPLEMENTARSE)

### 1.1 Desktop: Módulo "Descubre Turismo"
- Falta la capacidad de explorar destinos y realizar reservas desde la aplicación de escritorio.
- **Componentes requeridos:** `DiscoveryLayout`, `DestinationCard`, `SearchFilters`.

### 1.2 Mobile: Módulo "Analítica Territorial"
- El gobierno no puede ver reportes de impacto regional en tiempo real desde la app móvil.
- **Componentes requeridos:** `RegionalChart`, `MetricSummary`, `ImpactHeatmap`.

### 1.3 Desktop: Módulo "Gestión Archivística Full"
- Falta la capacidad de notarizar documentos localmente y sincronizar con Blockchain desde Desktop.
- **Componentes requeridos:** `BlockchainSigner`, `DocumentVault`.

## 2. INCONSISTENCIAS DE UI
- Los Dashboards de Prestador no comparten el mismo "Look & Feel" en las tres plataformas.
- Las tablas de datos en Web son altamente funcionales (sort/filter), mientras que en Desktop son estáticas.

## 3. DUPLICIDAD DE LÓGICA
- La lógica de cálculo de impuestos se encuentra duplicada en `interfaz/src/services` y `apps/desktop/renderer/src/services`.
