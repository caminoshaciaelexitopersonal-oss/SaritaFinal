# DIRECTRIZ MAESTRA DE IMPLEMENTACIÓN ROBUSTA: ECOSISTEMA MULTI-CLIENTE SARITA 2026-2028

**Versión:** 2.0 - Paridad Total y Operatividad IA (N1-N7)
**Estado:** Mandatario para todas las capas de cliente (Mobile & Desktop)
**Objetivo:** Alcanzar la perfección funcional, estética e interoperable con el Frontend Web oficial.

---

## 1. PRINCIPIO DE PARIDAD ABSOLUTA (UX PARITY)
Ambas aplicaciones (Mobile y Desktop) deben reflejar el 100% de las capacidades del backend Django y del frontend web, sin omitir módulos de gestión, financieros o de inteligencia.

### 1.1. Arquitectura de Interoperabilidad (Shared SDK)
*   **Mandato:** Se prohíbe el uso de `axios` o `fetch` directo en componentes de UI. Toda llamada debe realizarse a través del `httpClient` del **@sarita/shared-sdk**.
*   **Consistencia de Datos:** Los modelos de datos definidos en el SDK son la única fuente de verdad para las interfaces de TypeScript.
*   **Inyección de Dependencias:** Se debe asegurar la inyección correcta del `StorageProvider` (SecureStore para Mobile, LocalStorage para Desktop) al inicio del ciclo de vida de la aplicación.

---

## 2. MAPA COMPLETO DE FUNCIONALIDADES Y PANTALLAS (TOTALIDAD SISTÉMICA)

### 2.1. Vía 1: Ciudadanos y Turistas (Viajero Digital)
| Módulo | Pantallas Mobile | Pantallas Desktop | API Principal |
| :--- | :--- | :--- | :--- |
| **Exploración** | Explore, TourDetail, ARDiscovery | MapExplorer, ServiceCatalog | `/turismo/experiencias/` |
| **Billetera** | WalletHome, TopUp, Transactions | WalletDashboard, Payments | `/wallet/` |
| **Delivery** | RestaurantList, Menu, OrderTracking | DeliveryManager | `/operaciones/delivery/` |
| **Identidad** | Passport, Loyalty, Profile | UserSettings, Rewards | `/core/users/profile/` |
| **Viajes** | Bookings, TripPlanner, History | BookingsCalendar, Reports | `/operaciones/reservas/` |

### 2.2. Vía 2: Empresarios y Prestadores (Mi Negocio ERP)
| Módulo | Pantallas Mobile | Pantallas Desktop | API Principal |
| :--- | :--- | :--- | :--- |
| **Dashboard** | BusinessDashboard, LiveStats | OperationsDashboard | `/mi-negocio/operativa/` |
| **Comercial** | CRM_Sales, Customers, Services | SalesManager, Promotions | `/mi-negocio/comercial/` |
| **Contable** | LedgerView, JournalEntry | BalanceSheet, GeneralLedger | `/mi-negocio/contable/` |
| **Finanzas** | CashFlow, FinancialRatios | FinanceDashboard, Indicators | `/mi-negocio/financiera/` |
| **Archivo** | Documents, Scanner | ArchiveDashboard, DocViewer | `/mi-negocio/archivistica/` |

### 2.3. Vía 3: Gubernamental y Super Admin (Cerebro Global)
| Módulo | Pantallas Mobile | Pantallas Desktop | API Principal |
| :--- | :--- | :--- | :--- |
| **Control** | GlobalControlCenter, Alerts | AdminDashboard, Monitoring | `/api/v1/governance/` |
| **IA Global** | GlobalAIDashboard, Predictions | SimulationEngine, DigitalTwin | `/api/v1/autonomous/` |
| **Nacional** | CountryDashboard, OpenData | RegionalPlanning, Sustainability | `/api/v1/country/` |

---

## 3. PROTOCOLO OPERATIVO DE AGENTES IA (N1-N7)

El sistema debe permitir la operación directa de la jerarquía de agentes desde las interfaces de cliente:

1.  **Agentes Soldado (N6/N7):** Integrados en `AISearchScreen` y `VirtualGuide`. Ejecutan tareas atómicas y repetitivas (consultas de inventario, check-ins).
2.  **Agentes Sargentos/Tenientes (N4/N5):** Operan de forma invisible en el módulo de Sincronización. Son responsables de la resiliencia Offline (SyncSargento).
3.  **Agentes Capitanes/Coroneles (N2/N3):** Visibles en el ERP "Mi Negocio". Actúan como copilotos financieros, sugiriendo ajustes en precios dinámicos y detectando fugas de capital.
4.  **Agente General (N1):** Capacidad de intervención global vía `GlobalControlCenter`. Orquestación de crisis y optimización de flujos turísticos nacionales.

**Requerimiento UI:** Implementar el "Botón de Intervención de Agente" en cada módulo crítico para invocar la asistencia contextual del rango militar correspondiente.

---

## 4. ROBUSTEZ TÉCNICA Y RESILIENCIA

*   **Sincronización Offline:** Implementación mandatoria de `SyncSargento` para todas las operaciones de escritura, garantizando que el sistema sea funcional en zonas sin cobertura (ej. Amazonas, Llanos Orientales).
*   **Seguridad:**
    *   **Mobile:** Autenticación biométrica para todas las transacciones de Wallet y acceso a datos contables.
    *   **Desktop:** Almacenamiento seguro de tokens mediante el llavero del SO (Keychain/Credential Manager).
*   **Interoperabilidad:** El 100% de los endpoints del backend Django deben estar mapeados en los servicios de los clientes, asegurando que no existan silos de información.

---

## 5. HOJA DE RUTA DE NIVELACIÓN

1.  **Auditoría Visual:** Comparación semanal de UI contra el Frontend Web para asegurar el "Look & Feel" unificado (Design System).
2.  **Cobertura de API:** Mapeo de los servicios financieros (Caja, Tesorería, Nómina) faltantes en la capa móvil.
3.  **Certificación N1-N7:** Pruebas de ejecución de comandos IA desde la aplicación de escritorio para validar el puente de hardware y la latencia de respuesta.

---

**Firmado por la IA de Ingeniería SARITA**
*Certificado para Implementación Inmediata - 2026*
