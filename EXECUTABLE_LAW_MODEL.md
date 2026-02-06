# MODELO DE NORMAS EJECUTABLES (EXECUTABLE LAW MODEL)

**Versión:** 1.0 (Fase Z-LEGAL)
**Estado:** ESTRUCTURAL / OBLIGATORIO
**Visión:** Convertir mandatos jurídicos en condiciones de ejecución de software.

---

## 1. EL ESQUEMA DE LA NORMA TÉCNICA
Para que una norma jurídica sea procesada por el Legal Kernel (LK) de SARITA, debe ser traducida al siguiente esquema de objetos:

| Campo | Descripción | Ejemplo (EU AI Act) |
| :--- | :--- | :--- |
| **Objeto Legal** | Identificador único de la norma o artículo. | `EU-AI-ACT-ART-13` |
| **Sistema Afectado** | Los módulos o nodos sobre los que aplica. | `SARITA-AGENTS-L3` |
| **Condición Verificable** | La expresión lógica/matemática que define el cumplimiento. | `XAI_EXPLANATION_PRESENT == TRUE` |
| **Evento Esperado** | Acción que el sistema debe realizar para cumplir. | `AUDIT_LOG_ENTRY_CREATED` |
| **Evento Prohibido** | Acción que dispara un incumplimiento inmediato. | `AUTONOMOUS_OPTIMIZATION_WITHOUT_XAI` |
| **Nivel de Riesgo** | Impacto legal si la norma se rompe. | `HIGH` |
| **Tipo de Evidencia** | El tipo de registro que se guardará como prueba. | `CHAINED_FORENSIC_LOG` |

## 2. PROCESO DE TRADUCCIÓN (LEGAL-TO-LOGIC)
SARITA prohíbe la interpretación automática de la ley por parte de la IA. La traducción sigue este flujo institucional:
1.  **Revisión Jurídica:** Abogados internacionales definen los parámetros de cumplimiento.
2.  **Mapeo Técnico:** Ingenieros identifican los eventos de sistema (System Events) correspondientes.
3.  **Codificación DSL:** Se genera el archivo de norma en el lenguaje de dominio específico (DSL) de SARITA.
4.  **Carga en LK:** El SuperAdmin firma la nueva norma para su activación.

## 3. EJEMPLOS DE NORMAS EJECUTABLES

### A. Transparencia y Explicabilidad
*   **Mandato:** "Los sistemas de IA deben proporcionar explicaciones significativas de sus decisiones."
*   **Modelo Executable:**
    - `IF intention_level >= 2`
    - `THEN REQUIRE execution_report.has_xai_field == TRUE`
    - `ELSE RAISE Alerta_Incumplimiento`

### B. Soberanía de Datos (GDPR/Ley 1581)
*   **Mandato:** "Los datos sensibles no deben salir de la jurisdicción nacional."
*   **Modelo Executable:**
    - `IF event.data_classification >= 3`
    - `AND event.destination_node.jurisdiction != local_node.jurisdiction`
    - `THEN BLOCK event`
    - `AND LOG EVIDENCE_VAULT("INTENTO_EXFILTRACION")`

## 4. REGLAS DE VALIDACIÓN
- **Unicidad:** No puede haber dos normas activas con la misma condición y diferentes consecuencias para un mismo evento.
- **Trazabilidad de Norma:** Cada reporte de cumplimiento debe incluir el hash de la versión de la norma aplicada en ese momento.
- **Inviolabilidad:** Una norma no puede auto-modificarse ni ser modificada por un agente de IA.

---
**"Una ley que no puede modelarse técnicamente, es un deseo diplomático, no una norma operativa."**
