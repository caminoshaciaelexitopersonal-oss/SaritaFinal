# REPORTE DE AUDITORÍA DE DEPENDENCIAS — FASE A: REFRACTOR ESTRUCTURAL PROFUNDO

## 1. OBJETIVO DE LA AUDITORÍA
Identificar todos los acoplamientos que violan el principio de **Bounded Context** y la directriz de **aislamiento de dominios**. El objetivo es detectar imports directos de modelos, servicios y señales entre los dominios de Gobernanza (Super Admin), Operativo (Inquilinos), Comercial y Financiero.

---

## 2. HALLAZGOS DE ACOPLAMIENTO CRÍTICO (VIOLACIONES)

### 2.1 DOMINIO GOBERNANZA → DOMINIO OPERATIVO (TENANTS)
*   **Archivo:** `backend/apps/admin_plataforma/models.py`
    *   **Import:** `from apps.domain_business.operativa.models import ProviderProfile`
    *   **Impacto:** El núcleo de la administración depende de la estructura de perfiles de inquilinos.
*   **Archivo:** `backend/apps/admin_plataforma/gestion_contable/nomina/models.py`
    *   **Import:** `from apps.domain_business.operativa.models import ProviderProfile`
    *   **Impacto:** El sistema de nómina de la holding está vinculado directamente a modelos operativos de inquilinos.
*   **Archivo:** `backend/apps/admin_plataforma/gestion_contable/activos_fijos/models.py`
    *   **Import:** `from apps.domain_business.operativa.models import ProviderProfile`
*   **Archivo:** `backend/apps/admin_plataforma/services/interoperability_bridge.py`
    *   **Import:** `apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.reservas.models.Reserva` (vía `import_string`).
    *   **Impacto:** Aunque usa `import_string`, existe un acoplamiento lógico duro.

### 2.2 DOMINIO GOBERNANZA → DOMINIO COMERCIAL
*   **Archivo:** `backend/apps/admin_plataforma/serializers.py` y `views.py`
    *   **Import:** `from apps.comercial.models import Plan, Subscription`
    *   **Impacto:** El panel administrativo maneja directamente modelos comerciales en lugar de usar una interfaz de servicio o DTO.

### 2.3 ACOPLAMIENTO INTRA-DOMINIO (ADMIN) SIN CONTRATOS
*   **Hallazgo:** Módulos como `nomina`, `inventario`, `compras` y `activos_fijos` importan directamente `JournalEntry`, `Transaction` y `ChartOfAccount` de `admin_plataforma/gestion_contable/contabilidad/models.py`.
*   **Riesgo:** Si bien están en el mismo macro-dominio, la falta de una capa de servicio/contrato impide que estos módulos se conviertan en microservicios autónomos en el futuro.

---

## 3. DERIVA DE ESQUEMA (DATOS)
*   **Spanish Naming:** Detectado en `admin_nomina`, `admin_activos_fijos`, `admin_compras`, `admin_inventario`.
    *   Ejemplos: `Empleado`, `Contrato`, `ActivoFijo`, `FacturaCompra`.
*   **Integer IDs:** Módulos de nómina y activos fijos aún utilizan IDs incrementales por defecto, lo que rompe la estandarización UUID v4 de `core_erp`.

---

## 4. MATRIZ DE RIESGO DE ACOPLAMIENTO

| Relación | Tipo de Acoplamiento | Nivel de Riesgo | Recomendación |
| :--- | :--- | :---: | :--- |
| Admin -> Operativa | Import Directo Modelos | **Crítico** | Reemplazar por UUID + DTO |
| Admin -> Comercial | Import Directo Modelos | **Alto** | Usar Service Layer (Contract) |
| Sarita Agents -> Mi Negocio | Import Sargentos/Models | **Crítico** | Migrar a Event Bus (Stage 3) |
| Intra-Admin | Import Directo Contabilidad| **Medio** | Implementar FinancialContract |

---

## 5. CONCLUSIÓN DE LA ETAPA 1
El sistema presenta un acoplamiento masivo que impide la independencia de dominios. La **Fase A** debe priorizar la eliminación de imports directos de `apps.domain_business.operativa` y `apps.comercial`, sustituyéndolos por referencias de identidad (UUID) y contratos de comunicación.

**Auditoría finalizada por Jules.**
