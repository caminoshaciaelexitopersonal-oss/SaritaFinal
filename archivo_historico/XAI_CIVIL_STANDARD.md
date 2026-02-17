# ESTÁNDAR DE EXPLICABILIDAD CIVIL (XAI CIVIL STANDARD)

**Versión:** 1.0 (Fase Z-CIVIL)
**Estado:** OBLIGATORIO PARA INTERFACES CIUDADANAS
**Principio:** Una explicación que no se entiende, no es una explicación.

---

## 1. REQUISITOS DE LENGUAJE Y FORMATO

SARITA prohíbe el uso de términos puramente técnicos en las justificaciones dirigidas a personas físicas.

### 1.1 Prohibiciones Explícitas (Red Lines)
- ❌ **No Jerga Técnica:** Prohibido usar términos como "Redes Neuronales", "Pesos", "Backpropagation", "API", "Tokens".
- ❌ **No Justificación Propietaria:** Prohibido usar "Es un secreto comercial" o "El modelo lo decidió así" como explicación.
- ❌ **No PDFs Incomprensibles:** La explicación debe estar integrada en la interfaz, ser legible y amigable.

## 2. ESTRUCTURA OBLIGATORIA (CADENA CIVIL)

Toda explicación generada por SARITA para un ciudadano debe seguir la estructura **Causa -> Efecto -> Alternativa**:

### A. Causa (Basada en Hechos)
*   **Pregunta:** ¿Qué datos reales provocaron esta decisión?
*   **Ejemplo:** "Hemos detectado que su Registro Nacional de Turismo (RNT) expiró hace 48 horas."

### B. Efecto (Impacto Directo)
*   **Pregunta:** ¿Cómo afecta esto al usuario?
*   **Ejemplo:** "Debido a esto, su perfil de prestador ha sido ocultado temporalmente del portal de atractivos."

### C. Alternativa (Acción Correctiva)
*   **Pregunta:** ¿Qué puede hacer el usuario para cambiar el resultado?
*   **Ejemplo:** "Si actualiza su documento en el panel de Gestión Archivística, su perfil será reactivado automáticamente en menos de 5 minutos."

## 3. VERIFICACIÓN DE COMPRENSIÓN
El sistema monitoriza si las explicaciones son efectivas:
- Si un usuario apela una decisión tras leer el XAI, el sistema registra el punto de fricción.
- Los Agentes Auditores realizan pruebas de Turing invertidas para asegurar que las explicaciones son indistinguibles de una respuesta humana profesional.

## 4. REGISTRO DE VERDAD LÓGICA
Aunque la explicación sea en lenguaje natural, debe estar vinculada a una **Prueba de Lógica** en el `Evidence Vault`:
- `USER_EXPLANATION_ID: "XAI-CIV-902"`
- `LOGICAL_PROOF_HASH: "sha256:abc123..."` (Para que un experto pueda verificar que la explicación amigable coincide con la matemática del modelo).

---
**"La transparencia es el puente entre el código del sistema y la confianza del ciudadano."**
