# DIRECTRIZ TÉCNICA: CONGELAMIENTO CONTROLADO (FASE 0)

**Fecha:** 2026
**Estado:** ACTIVO
**Objetivo:** Detener el crecimiento de la deuda técnica y estabilizar la arquitectura antes de iniciar la cirugía estructural.

---

## 1. DECLARACIÓN FORMAL
A partir de este momento, queda suspendido el desarrollo funcional en los módulos estructuralmente comprometidos. El sistema entra en modo **Estructural**, no creativo.

**Módulos bajo congelamiento:**
*   `admin_plataforma`
*   `mi_negocio`
*   `sarita_agents`

---

## 2. REGLAS DE OPERACIÓN

### ✅ PERMITIDO (Bajo el tag [STRUCTURAL])
*   Refactorización estructural para desacoplamiento.
*   Eliminación de código muerto o duplicado.
*   Migración de lógica y modelos hacia `core_erp`.
*   Escritura de pruebas de integridad y regresión estructural.
*   Documentación técnica y diagramación de flujos.

### ❌ PROHIBIDO
*   Creación de nuevos Endpoints.
*   Implementación de nuevas funcionalidades (Features).
*   Creación de nuevos Modelos de Base de Datos (fuera de `core_erp`).
*   Nuevas migraciones funcionales.
*   Nuevas integraciones con servicios externos.
*   Nuevas automatizaciones o capacidades de IA.

---

## 3. DISCIPLINA DE COMMITS
Todo commit realizado durante esta fase debe seguir el formato obligatorio:
`[STRUCTURAL-CONSOLIDATION][Fase] Motivo técnico`

**Ejemplo:**
`[STRUCTURAL-CONSOLIDATION][F0] Setup baseline metrics and import blocks`

---

## 4. BLOQUEO TÉCNICO DE IMPORTS
Se prohíbe terminantemente el establecimiento de nuevos acoplamientos entre:
1.  `admin_plataforma` ↔ `mi_negocio`
2.  `sarita_agents` → `mi_negocio` (Importaciones directas)

---

## 5. CRITERIO DE SALIDA
La Fase 0 se considerará finalizada cuando se disponga del snapshot estructural completo, se hayan validado los bloqueos técnicos y el equipo esté alineado con los principios arquitectónicos no negociables.

**Firmado:**
Jules
*Senior Software Engineer*
