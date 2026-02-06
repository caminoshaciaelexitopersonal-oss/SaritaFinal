# CLASIFICACIÓN DE IMPACTO HUMANO (HUMAN IMPACT CLASSIFICATION)

**Versión:** 1.0 (Fase Z-CIVIL)
**Estado:** OFICIAL
**Criterio:** Prioridad del bienestar humano sobre la eficiencia técnica.

---

## 1. NIVELES DE IMPACTO (CLASES H)

SARITA clasifica cada intención algorítmica según su potencial para afectar la vida, los derechos o la dignidad de las personas:

| Clase | Nivel de Impacto | Descripción | Acción del Sistema (HRK) |
| :--- | :--- | :--- | :--- |
| **H0** | **Nulo** | Procesamiento puramente técnico sin efectos sobre personas. | Sin restricciones adicionales. |
| **H1** | **Bajo** | Afecta preferencias no críticas o información general. | Notificación al usuario sobre el uso de IA. |
| **H2** | **Medio** | Afecta el acceso a servicios o la visibilidad de ofertas. | **Explicación XAI obligatoria** y registro de intención. |
| **H3** | **Alto** | Afecta derechos económicos, laborales o de reputación. | **Revisión humana obligatoria (Confirmación).** |
| **H4** | **Crítico** | Afecta la salud, seguridad física o libertades fundamentales. | **Bloqueo Automático** y escalamiento inmediato a tribunal civil. |

## 2. CONTEXTOS SENSIBLES (HIGH-PROTECTION ZONES)

SARITA eleva automáticamente el nivel de impacto de cualquier acción cuando ocurre dentro de los siguientes dominios institucionales:

*   **Salud y Sanidad:** Cualquier recomendación médica o gestión de datos de pacientes (Nivel mínimo: H3).
*   **Justicia y Policía:** Perfilamiento o análisis sensorial para seguridad ciudadana (Nivel mínimo: H4).
*   **Trabajo y Nómina:** Decisiones sobre contratación, despidos o penalizaciones laborales (Nivel mínimo: H3).
*   **Finanzas y Crédito:** Scoring para acceso a financiamiento o beneficios económicos (Nivel mínimo: H2).
*   **Educación:** Evaluación de desempeño o acceso a programas de formación (Nivel mínimo: H2).
*   **Migración:** Procesos de identificación o permisos de tránsito regional (Nivel mínimo: H4).

## 3. MECANISMO DE ELEVACIÓN AUTOMÁTICA
Si un agente de IA intenta ejecutar una misión en un contexto sensible sin el nivel de protección adecuado, el **Civil Impact Monitor (CIM)** interviene:
1.  **Interceptación:** Detiene la ejecución.
2.  **Recategorización:** Asigna el nivel H obligatorio.
3.  **Habilitación de Barreras:** Fuerza la generación de XAI y la solicitud de firma humana.

## 4. AUDITORÍA DE IMPACTO
SARITA genera informes trimestrales sobre la distribución de las Clases H, permitiendo a los reguladores civiles observar qué proporción de las decisiones institucionales son autónomas versus supervisadas.

---
**"La eficiencia nunca es una excusa para el riesgo humano."**
