# AUDITORÍA ESTRUCTURAL - BLOQUE 1: CONTROL DE DERIVA DE ESQUEMA (SARITA)

## 1. MÓDULOS CON NOMENCLATURA EN ESPAÑOL (MIGRACIÓN A ENGLISH REQUERIDA)

| Módulo | Clase Actual | Clase Propuesta | Riesgo |
| :--- | :--- | :--- | :--- |
| **G. Operativa** | `Reserva` | `OperationalBooking` | Alto (Clon de Mi Negocio) |
| **G. Operativa** | `Cliente` | `OperationalCustomer`| Alto (Clon de Mi Negocio) |
| **G. Operativa** | `Valoracion` | `OperationalReview` | Medio |
| **G. Operativa** | `DocumentoOperativo`| `OperationalDocument`| Bajo |
| **G. Comercial** | `OperacionComercial`| `CommercialOperation`| Alto (Duplicidad con Sales) |
| **G. Comercial** | `FacturaVenta` | `SalesInvoice` | Crítico (Schema Drift) |
| **G. Contable (Nómina)** | `Empleado` | `Employee` | Alto |
| **G. Contable (Nómina)** | `Contrato` | `EmploymentContract`| Alto |
| **G. Contable (Activos)** | `ActivoFijo` | `FixedAsset` | Alto |

## 2. MÓDULOS CON IDs ENTEROS (MIGRACIÓN A UUID v4 REQUERIDA)

Todos los modelos en las siguientes carpetas que no heredan de `BaseErpModel` o no definen `UUIDField(primary_key=True)`:

1. `apps/admin_plataforma/gestion_operativa/modulos_genericos/*`
2. `apps/admin_plataforma/gestion_operativa/modulos_especializados/*`
3. `apps/admin_plataforma/gestion_contable/nomina/*`
4. `apps/admin_plataforma/gestion_contable/activos_fijos/*`
5. `apps/admin_plataforma/gestion_contable/inventario/*`
6. `apps/admin_plataforma/gestion_contable/compras/*`

## 3. DEPENDENCIAS CRUZADAS CRÍTICAS (DEUDA TÉCNICA)

- **Circularidad:** `sarita_agents` <-> `mi_negocio` (Debe romperse via EventBus).
- **Acoplamiento Directo:** `QuintupleERPService` importa directamente modelos de `mi_negocio`.
- **Mirroring Injustificado:** `admin_plataforma/gestion_operativa` es un mirror de `prestadores/mi_negocio/gestion_operativa`.

## 4. ESTADO DE LA VENTANA DE CONGELACIÓN (FREEZE)
- **Estado:** ACTIVADA.
- **Restricción:** No se permiten nuevas migraciones en `admin_plataforma` que no incluyan la normalización a UUID y English.

---
**Auditado por Jules.**
