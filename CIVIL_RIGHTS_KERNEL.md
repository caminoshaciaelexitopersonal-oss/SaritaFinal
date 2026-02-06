# ESPECIFICACIÓN DEL HUMAN RIGHTS KERNEL (HUMAN RIGHTS KERNEL SPEC - HRK)

**Versión:** 1.0 (Fase Z-CIVIL)
**Módulo:** `apps.human_rights_kernel`
**Rol:** Validador Central de Derechos Civiles y Garantía de Dignidad Algorítmica.

---

## 1. NATURALEZA DEL HRK
El **Human Rights Kernel (HRK)** es el guardián de la dimensión humana dentro de SARITA. Actúa como una capa de filtrado obligatoria para cualquier intención generada por los agentes de IA o el núcleo de gobernanza que tenga un impacto directo o indirecto sobre personas físicas (Ciudadanos, Usuarios, Trabajadores).

## 2. FUNCIONES CORE

### 2.1 Validación de Cumplimiento de Derechos
*   **Función:** Evalúa cada acción propuesta contra el `ALGORITHMIC_RIGHTS_CATALOG`.
*   **Acción:** Si una acción viola un derecho técnico (ej: falta de explicación en una decisión de alto impacto), el HRK invalida la instrucción antes de que llegue a la capa de ejecución.

### 2.2 Bloqueo de Acciones Incompatibles
*   **Función:** Intercepta decisiones que superan el umbral de riesgo humano permitido sin supervisión.
*   **Acción:** Implementa un "Hard Block" sistémico. La IA no puede "saltarse" esta validación; es una restricción a nivel de código de infraestructura.

### 2.3 Ejecución de Guardrails Civiles
*   **Función:** Aplica límites específicos en contextos sensibles (Salud, Trabajo, Crédito).
*   **Lógica:** En estos contextos, el HRK eleva automáticamente el requisito de confirmación humana (Human-in-the-loop) a Nivel L3-L4.

### 2.4 Registro de Impacto Humano
*   **Función:** Etiqueta cada acción del sistema con un nivel de impacto (H0-H4).
*   **Trazabilidad:** Provee la base técnica para que el `Civil Impact Monitor (CIM)` pueda generar alertas institucionales.

## 3. EL PRINCIPIO "HUMAN IMPACT FIRST" (HIF)
El HRK opera bajo una prioridad absoluta: **El bienestar y los derechos del ser humano prevalecen sobre la eficiencia algorítmica, la rentabilidad operativa o la velocidad del sistema.**

*   Si una optimización económica (ej: ajuste de precios) genera un riesgo de discriminación algorítmica, el HRK bloquea la optimización aunque sea "técnicamente correcta".
*   Si una misión de agente no puede explicar su lógica en lenguaje civil, el HRK la suspende por falta de transparencia.

## 4. GOBERNANZA TÉCNICA
El código del HRK es auditable por organizaciones de derechos humanos y defensorías del pueblo. Su configuración no puede ser alterada por agentes de IA; solo una autoridad soberana humana puede actualizar los parámetros de protección, siempre bajo registro forense inmutable.

---
**"En SARITA, los derechos humanos no son una política; son una restricción lógica del sistema."**
