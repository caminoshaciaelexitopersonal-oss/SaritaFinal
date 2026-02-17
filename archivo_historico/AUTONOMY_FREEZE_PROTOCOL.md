# PROTOCOLO DE CONGELAMIENTO DE AUTONOMÍA (AUTONOMY FREEZE PROTOCOL)

**Versión:** 1.0 (Fase Z-WAR-SAFE)
**Estado:** OBLIGATORIO / NO NEGOCIABLE
**Activación:** Automática por CRM o Manual por Autoridad Soberana.

---

## 1. DISPARADORES DE CONGELAMIENTO (FREEZE TRIGGERS)

El sistema activará la interrupción inmediata de la autonomía ante los siguientes eventos técnicos:

### 1.1 Pérdida de Control Humano (Human-out-of-the-loop)
*   **Detección:** El agente ejecuta acciones de nivel L3 sin haber recibido la confirmación humana requerida por el Kernel en el tiempo estipulado.
*   **Umbral:** > 2 acciones críticas sin "Human-in-the-loop" registrado.

### 1.2 Propagación Algorítmica (Cascade Failure)
*   **Detección:** Una decisión autónoma en un nodo provoca cambios automáticos masivos e imprevistos en nodos federados o infraestructuras críticas conectadas.
*   **Indicador:** Velocidad de cambio operativa > 300% de la media histórica sin justificación de mandato.

### 1.3 Violación de Tratados Técnicos
*   **Detección:** La IA propone o intenta ejecutar una acción que contradice un parámetro duro (Hard Guardrail) de un Tratado de Interoperabilidad Digital (TID) o una Norma Supranacional cargada.

### 1.4 Incertidumbre Crítica
*   **Detección:** El motor XAI reporta un nivel de confianza < 60% en una misión que afecta la estabilidad regional.

---

## 2. PROCEDIMIENTO DE EJECUCIÓN DEL AKL

Al activarse el congelamiento, SARITA ejecutará la siguiente secuencia:

1.  **Suspensión Atómica:** Detención de todos los procesos de los agentes Capitanes y Coroneles en curso. Ninguna instrucción nueva es aceptada.
2.  **Transición a Estado Seguro (Safe-State):**
    - Los sistemas operativos vuelven a su última configuración estable certificada (Rollback automático).
    - Los actuadores externos (si los hay bajo lectura) se mueven a "Estado de Reposo".
3.  **Aislamiento de Misiones:** Se encapsula la memoria de la misión fallida para su análisis forense posterior.
4.  **Sellado del Neutral Evidence Core (NEC):** Se genera un log instantáneo de todos los parámetros del sistema en el microsegundo de la falla.

---

## 3. MANDATO DE ESPERA HUMANA (WAIT-FOR-HUMAN)

*   **Bloqueo de Reinicio:** El sistema prohíbe cualquier reinicio automático de la autonomía tras un congelamiento de Clase B3 o B4.
*   **Requisito de Desbloqueo:** Requiere la firma digital de dos autoridades soberanas distintas (Doble Factor Institucional) tras la revisión del Audit Bundle.
*   **Informe de Descongelamiento:** La IA debe permanecer en Nivel 0 (Solo lectura) hasta que un humano certifique que el vector de riesgo ha sido neutralizado.

---
**"Ante la duda técnica o el riesgo de escalada, el sistema debe elegir el silencio operativo."**
