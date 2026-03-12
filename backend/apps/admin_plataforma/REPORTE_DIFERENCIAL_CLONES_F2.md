# REPORTE DIFERENCIAL DE CLONES (FASE 2) — 2026

## 1. DOMINIO COMERCIAL
Comparativa entre `admin_plataforma.gestion_comercial` y `mi_negocio.gestion_comercial`.

| Componente | Diferencia Detectada | Acción de Unificación |
| :--- | :--- | :--- |
| **Modelos (OperacionComercial, Factura, Recibo)** | `admin_plataforma` usa `app_label` específico y `admin_` prefix en related names. `mi_negocio` incluye campos de integración DIAN. | Consolidar en `domain_business.comercial`. Usar esquema de `mi_negocio` (más completo) y asegurar herencia de `BaseErpModel`. |
| **Integración DIAN** | Solo presente de forma robusta en `mi_negocio`. | Mover a `domain_business.comercial.services.dian`. |
| **Signals** | Mirroring de señales de impacto contable. | Centralizar en `domain_business.comercial.signals`. |

## 2. DOMINIO OPERATIVO
Comparativa entre `admin_plataforma.gestion_operativa` y `mi_negocio.gestion_operativa`.

| Componente | Diferencia Detectada | Acción de Unificación |
| :--- | :--- | :--- |
| **Módulos Genéricos (Reservas, Clientes, Inventario)** | `admin_plataforma` tiene versiones esqueléticas. `mi_negocio` tiene implementación completa con "Sargentos". | Consolidar en `domain_business.operativa`. Adoptar el patrón de Sargentos para lógica de negocio compartida. |
| **Módulos Especializados (Hoteles, Agencias, etc.)** | `admin_plataforma` tiene carpetas duplicadas (algunas vacías). | Consolidar definiciones en `domain_business.operativa.specialized`. |

## 3. DECISIONES DE DISEÑO NO NEGOCIABLES
1.  **Naming:** Se usará el esquema de `mi_negocio` como base, pero normalizado a Inglés Técnico donde aplique (Ej: `OperacionComercial` -> `CommercialOperation`).
2.  **Identificadores:** Todos los modelos migrarán a **UUID v4**.
3.  **Segregación:** Se usará `organization_id` (o `tenant_id`) para separar datos de la Holding de los de los Tenants dentro de las mismas tablas.
4.  **Localización:** La lógica específica de la DIAN (Colombia) se mantendrá pero desacoplada vía interfaces para permitir futura expansión internacional.

---
**Generado por:** Jules
**Estado:** Auditoría Finalizada - Fase 2.1
