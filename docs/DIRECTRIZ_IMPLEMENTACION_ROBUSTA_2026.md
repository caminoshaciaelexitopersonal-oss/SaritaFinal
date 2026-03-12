# DIRECTRIZ MAESTRA DE IMPLEMENTACIÓN ROBUSTA: ECOSISTEMA MULTI-CLIENTE SARITA 2026-2028

**Versión:** 3.0 - Perfección Funcional, UX Parity y Orquestación IA (N1-N7)
**Estado:** MANDATARIO (NIVEL DE CUMPLIMIENTO 10)
**Fecha:** 22 de Mayo de 2024 (Revisión Estratégica)

---

## 1. MISIÓN DE ROBUSTEZ Y PERFECCIÓN
Esta directriz establece el estándar absoluto para las aplicaciones **Mobile (React Native/Expo)** y **Desktop (Electron)** del ecosistema SARITA. El objetivo es alcanzar la paridad total con el Frontend Web oficial, asegurando que los usuarios de las tres vías (Gubernamental, Empresarial y Turística) tengan una experiencia de clase mundial, interoperable y potenciada por Inteligencia Artificial Autónoma.

---

## 2. MAPA DE COBERTURA TOTAL DE PANTALLAS (UX PARITY 100%)

Se exige que ambas aplicaciones implementen las siguientes pantallas, consumiendo las APIs correspondientes del backend centralizado Django:

### 2.1. Vía 1: Ciudadanos y Turistas (Viajero Digital)
| Módulo | Pantallas Mobile (Requeridas) | Pantallas Desktop (Requeridas) | Propósito |
| :--- | :--- | :--- | :--- |
| **Descubrimiento** | `Explore`, `TourDetail`, `AISearch`, `ARDiscovery` | `CatalogExplorer`, `MapDashboard` | Búsqueda y visualización de experiencias. |
| **Reservas** | `Booking`, `BookingsList`, `TripPlanner` | `BookingsCalendar`, `PlannerDesktop` | Gestión del ciclo de vida del viaje. |
| **Finanzas** | `WalletHome`, `WalletBalance`, `TopUp`, `Rewards` | `WalletDashboard`, `TransactionManager` | Pagos, recargas y recompensas. |
| **Servicios** | `DeliveryHome`, `OrderTracking`, `Transport` | `DeliveryAdmin`, `UrbanServices` | Comida local y transporte regional. |
| **Identidad** | `Passport`, `TravelFeed`, `Loyalty`, `Profile` | `IdentityProfile`, `AchievementCenter` | Pasaporte digital y red social viajera. |

### 2.2. Vía 2: Empresarios y Prestadores (Mi Negocio ERP)
| Módulo | Pantallas Mobile (Requeridas) | Pantallas Desktop (Requeridas) | Propósito |
| :--- | :--- | :--- | :--- |
| **Gestión Comercial** | `BusinessDashboard`, `Services`, `Customers` | `CommercialDashboard`, `CRM_Manager` | Control de ventas, clientes y servicios. |
| **Contabilidad** | `AccountingEntries`, `LedgerView` | `BalanceSheet`, `IncomeStatement`, `Ledger` | Libro Mayor, Diario y Balances reales. |
| **Finanzas** | `FinanceSummary`, `CashFlow` | `FinanceDashboard`, `Indicators`, `Ratios` | Flujo de caja y salud financiera. |
| **Operaciones** | `OperationalOrders`, `LiveTour`, `SST` | `OperationsDashboard`, `ResourceScheduler` | Logística en campo y cumplimiento SST. |
| **Archivística** | `Documents`, `Scanner` | `ArchiveDashboard`, `DocumentViewer` | Gestión documental inmutable (SHA-256). |

### 2.3. Vía 3: Gubernamental y Super Admin (Cerebro Global)
| Módulo | Pantallas Mobile (Requeridas) | Pantallas Desktop (Requeridas) | Propósito |
| :--- | :--- | :--- | :--- |
| **Inteligencia** | `GlobalAIDashboard`, `GlobalAnalytics` | `SimulationEngine`, `DigitalTwin` | IA predictiva y gemelo digital turístico. |
| **Gobernanza** | `ControlCenter`, `GlobalAlerts` | `GovernanceDashboard`, `MassiveEvents` | Monitoreo de crisis y flujos masivos. |
| **Admin** | `AdminDashboard`, `Observability` | `SuperAdminTerminal`, `Infrastructure` | Salud del sistema y métricas macro. |

---

## 3. ORQUESTACIÓN DE AGENTES IA (N1-N7) DESDE CLIENTES

La interfaz debe ser el canal de ejecución para la jerarquía militar de agentes:

*   **Comandos de Voz/Chat (N7-N6 Soldados):** Ejecución de tareas simples (Reservar tour, consultar saldo).
*   **Comando de Orquestación (N1-N3 Generales/Coroneles):** Acceso a la "Consola de Comando" en Desktop para orquestar la expansión regional y provisionar nuevos servicios (Zero-Touch Onboarding).
*   **Asistente Copiloto (N2-N3):** Notificaciones proactivas en el ERP sobre irregularidades contables o picos de demanda previstos.
*   **Sincronización Invisible (N5 Sargento):** Gestión resiliente de colas offline garantizando que ninguna orden se pierda.

---

## 4. ESTÁNDARES TÉCNICOS DE INTEROPERABILIDAD

1.  **Shared SDK Central:** Uso obligatorio de `@sarita/shared-sdk` para evitar lógica de negocio replicada.
2.  **UX Unificado (Design System):** Uso de componentes estándar (`Card`, `Button`, `Input`) para asegurar paridad visual entre Web, Mobile y Desktop.
3.  **Seguridad RS256:** Todas las llamadas al API deben incluir el token JWT gestionado por el `TokenManager` del SDK.
4.  **Resiliencia Offline:** Implementación mandatoria de `SyncSargento` en Mobile para operaciones en zonas de baja conectividad.
5.  **Hardware Bridge (Desktop):** Interacción obligatoria vía IPC para periféricos (impresión fiscal y escaneo de identidad) sincronizando el estado con el backend.

---

## 5. RECOMENDACIÓN FINAL PARA PERFIL "WORLD-CLASS"
Para que un prestador sea de clase mundial, su herramienta (Mobile/Desktop) debe ser **predictiva, autónoma y resiliente**. Debe anticipar necesidades del cliente, gestionar la contabilidad con precisión quirúrgica y operar sin interrupciones sin importar la calidad de la red, siempre respaldado por la jerarquía de inteligencia SARITA.

**Estado de la Directriz:** IMPLEMENTACIÓN INMEDIATA.
