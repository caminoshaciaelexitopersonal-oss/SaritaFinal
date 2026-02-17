# CONGELACIÓN DE ARQUITECTURA BASE (ARCH-FREEZE-BASELINE)

**Estado:** CONGELADO PARA CERTIFICACIÓN
**Versión Baseline:** 1.0.0-RC-S
**Política de Cambio:** Requiere Auditoría de Impacto Nivel 3.

---

## 1. COMPONENTES DEL NÚCLEO INMUTABLE (FROZEN CORE)

Los siguientes componentes no pueden ser modificados sin romper la certificación de soberanía y seguridad:

### 1.1 Gobernanza y Seguridad
- **Governance Kernel:** La lógica de validación de intenciones y niveles de autoridad.
- **Middleware de Blindaje:** `SecurityHardeningMiddleware` (Backend) y `middleware.ts` (Frontend).
- **Registro Forense:** El esquema de hashes encadenados en `ForensicSecurityLog`.

### 1.2 Estructura de Datos Base (Capa 1)
- **CustomUser & Roles:** La jerarquía de roles institucionalizada en `api.models.CustomUser`.
- **Multi-Tenancy:** El modelo `companies.Company` y su mecanismo de aislamiento criptográfico.
- **Triple Vía:** La separación física y lógica de las rutas para Gobierno, Empresarios y Turistas.

---

## 2. REQUISITOS DE INTEGRIDAD TÉCNICA
Para mantener la certificación, cualquier adición debe cumplir con:
1. **Zero Circularity:** No se permiten dependencias circulares entre apps (Capa 3 no puede ser importada por Capa 1).
2. **UUID References:** Las relaciones entre dominios autónomos deben realizarse vía `UUIDField` (ref_id), nunca vía FK directa.
3. **Audit Trail:** Cada nueva acción de escritura debe emitir un evento al `AuditLog` o `ForensicSecurityLog`.

---

## 3. PUNTOS DE EXTENSIÓN (EXTENSIBILITY)

El sistema permite crecimiento en las siguientes áreas sin comprometer el núcleo:

- **Nuevos Módulos ERP (Capa 3):** Se pueden añadir subdominios (ej: Gestión de Nómina, Inventarios específicos) siempre que hereden de `SystemicERPViewSetMixin`.
- **Cuerpo de Agentes IA:** Creación de nuevos `Coroneles`, `Capitanes` o `Tenientes` dentro de la jerarquía SARITA.
- **Frontend Components:** Adición de nuevas vistas de dashboard o componentes de UI que utilicen el sistema de diseño corporativo.
- **Integraciones Externas:** Nuevas pasarelas de pago o proveedores de LLM configurables en `UserLLMConfig`.

---

## 4. PROTOCOLO DE DESCONGELACIÓN
Si se requiere una modificación en el Core (Capa 1 o 2):
1. Justificación técnica y de negocio ante el Comité de Gobernanza.
2. Análisis de impacto en la integridad de datos.
3. Re-certificación total de seguridad (Pen-Testing).
4. Actualización del Hash de Integridad de Arquitectura.

---
**"La estabilidad es la base de la confianza. El cambio sin control es entropía."**
