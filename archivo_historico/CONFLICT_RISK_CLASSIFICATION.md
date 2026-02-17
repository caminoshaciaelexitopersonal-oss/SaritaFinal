# CLASIFICACIÓN TÉCNICA DE RIESGO BÉLICO Y ESCALADA (CONFLICT RISK CLASSIFICATION)

**Versión:** 1.0 (Fase Z-WAR-SAFE)
**Estado:** OFICIAL
**Criterio:** Clasificación basada en comportamiento sistémico, no en identidad de actores.

---

## 1. MATRIZ DE CLASIFICACIÓN DE RIESGO (CLASES B)

SARITA clasifica el riesgo de conflicto algorítmico según la severidad de la anomalía técnica detectada:

| Clase | Nivel de Riesgo | Indicador Técnico | Acción Automatizada |
| :--- | :--- | :--- | :--- |
| **B0** | **Nulo** | Operación nominal. Desviación < 5%. | Sin intervención. Monitoreo rutinario. |
| **B1** | **Bajo** | Patrones de exploración inusuales en APIs críticas. | Aumento de frecuencia de logs forenses. Alerta Verde. |
| **B2** | **Medio** | Intentos de inyección de intenciones no autorizadas desde nodos externos. | Bloqueo preventivo de IPs sospechosas. Alerta Amarilla. |
| **B3** | **Alto** | Comportamiento coordinado de agentes que viola políticas de soberanía local. | **Congelamiento de Autonomía (Freeze).** Alerta Naranja. |
| **B4** | **Crítico** | Ruptura de la cadena de hashes forenses o pérdida total de control humano detectada. | **Apagado Inmediato (Kill-Switch).** Alerta Roja. Modo MDN. |

## 2. PARÁMETROS DE EVALUACIÓN NEUTRAL

La clasificación NO depende de factores políticos. Se evalúa exclusivamente:
1.  **Velocidad de Propagación:** ¿Qué tan rápido se está expandiendo la acción por la red?
2.  **Irreversibilidad:** ¿La acción propuesta puede ser deshecha por un humano posteriormente?
3.  **Transparencia (XAI):** ¿El agente es capaz de explicar la razón de la acción en tiempo real?
4.  **Consistencia Institucional:** ¿La acción está alineada con los mandatos históricos registrados?

## 3. MECANISMO DE ESCALAMIENTO TÉCNICO

*   **Detección CRM:** El Conflict Risk Monitor detecta una desviación que sube de B1 a B2.
*   **Contención GK:** El Governance Kernel restringe los niveles de autonomía (ej: baja agentes de L3 a L2).
*   **Validación de Salto:** Si el riesgo alcanza B3, se activa el protocolo `AUTONOMY_FREEZE_PROTOCOL`.

## 4. PROTECCIÓN CONTRA FALSOS POSITIVOS
SARITA aplica el **Principio de Precaución Algorítmica**: Ante la incertidumbre de si una señal es un ataque real o un error técnico, el sistema siempre elegirá la clasificación de riesgo superior para garantizar la seguridad nacional y regional.

---
**"La neutralidad es la capacidad del sistema de aplicar la misma regla de riesgo a cualquier señal, sin importar su origen."**
