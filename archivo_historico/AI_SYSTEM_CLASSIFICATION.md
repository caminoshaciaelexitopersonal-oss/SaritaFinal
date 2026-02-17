# CLASIFICACIÓN LEGAL DE SISTEMAS DE IA Y AUTÓNOMOS (AI SYSTEM CLASSIFICATION)

**Versión:** 1.0 (Fase Z-LEGAL)
**Estado:** OFICIAL
**Objetivo:** Establecer una jerarquía de riesgo y requisitos legales para el despliegue de sistemas autónomos.

---

## 1. NIVELES DE AUTONOMÍA Y CARGA LEGAL

SARITA clasifica los sistemas según su capacidad de impacto sobre derechos y bienes:

| Nivel | Descripción | Requisitos Legales SARITA | Ejemplo de Uso |
| :--- | :--- | :--- | :--- |
| **L0** | **Asistencial** | Registro declarativo. No requiere auditoría forense obligatoria. | Chatbots informativos, traducción de textos. |
| **L1** | **Decisión Recomendada** | Trazabilidad de recomendaciones. Registro en el Log Ejecutivo. | Propuestas de marketing, sugerencias de precios. |
| **L2** | **Decisión Condicionada** | **Auditoría periódica.** Requiere validación humana por defecto. | Optimización operativa de hoteles, gestión de tareas. |
| **L3** | **Decisión Autónoma** | **Supervisión humana en tiempo real.** Registro XAI obligatorio para cada acción. | Ajustes financieros, cambios en políticas operativas. |
| **L4** | **Infraestructura Crítica** | **Certificación Internacional.** Bloqueo sistémico ante fallo de integridad (MDN). | Gestión de soberanía, coordinación interestatal, defensa. |

## 2. MATRIZ DE RESPONSABILIDAD TÉCNICA

*   **L0 - L1:** La responsabilidad recae principalmente en el operador que acepta o solicita la información.
*   **L2 - L3:** Responsabilidad compartida. El sistema debe probar que proporcionó la información necesaria para la supervisión humana (Derecho a Explicación).
*   **L4:** Responsabilidad Institucional Máxima. El Nodo Nacional o Supranacional asume la custodia legal total del núcleo.

## 3. REQUISITOS POR NIVEL (ENFORCEMENT)

### A. Registro Internacional de IA (RII)
Todos los sistemas L1 o superior deben estar inscritos en el RII de SARITA, indicando su versión, dominio de actuación y niveles de riesgo declarados.

### B. Derecho a Retiro (Kill Switch)
Para niveles L3 y L4, el sistema **debe** tener un mecanismo de interrupción inmediata (Sovereignty Flags) accesible por una autoridad humana autorizada. Un sistema sin Kill Switch no puede ser certificado legalmente por SARITA.

### C. Explicabilidad Forzada (XAI)
Para niveles L2 en adelante, ninguna acción es legalmente válida si no contiene los 5 puntos de decisión:
1. **Hallazgo:** ¿Qué se detectó?
2. **Datos:** ¿En qué se basa?
3. **Regla:** ¿Qué norma o política se aplicó?
4. **Alternativas:** ¿Qué se descartó?
5. **Resultado:** ¿Qué impacto se espera?

## 4. RELACIÓN CON LA JERARQUÍA DE AGENTES
- **Tenientes:** Operan en L1 - L2.
- **Capitanes:** Operan en L2 - L3.
- **Coroneles y General:** Operan en L3 - L4.

---
**"La ley no prohíbe la autonomía, prohíbe la autonomía sin rendición de cuentas."**
