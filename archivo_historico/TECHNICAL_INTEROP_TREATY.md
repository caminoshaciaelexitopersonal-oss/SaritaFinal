# TRATADO DE INTEROPERABILIDAD TÉCNICA (TIT)

**Versión:** 1.0 (Fase Z-OPERATIONAL-TREATIES)
**Estatus:** ESTÁNDAR TÉCNICO VINCULANTE
**Propósito:** Definir el lenguaje común y las garantías de integridad para el intercambio de señales entre nodos soberanos.

---

## 1. ESTÁNDARES DE SEÑALIZACIÓN
Toda señal emitida o recibida a través de Peace-Net debe cumplir con el formato **Diplomatic Signal Object (DSO)**:

- **Estructura:** JSON Schema v1.0.
- **Explicabilidad Obligatoria:** Cada señal debe incluir un campo `reasoning_chain` con los 5 puntos de XAI (Hallazgo, Datos, Regla, Alternativas, Resultado).
- **Sellado de Integridad:** Firma SHA-256 basada en la llave privada del nodo nacional emisor.

## 2. REQUISITOS DEL GOVERNANCE KERNEL
Los nodos participantes se comprometen a:
1. Mantener una versión compatible del **Kernel de Gobernanza**.
2. Publicar periódicamente los hashes de sus políticas de red para verificación mutua.
3. No alterar la cadena de auditoría forense (`ForensicSecurityLog`).

## 3. PROHIBICIÓN DE DATOS CRUDOS
Queda estrictamente prohibido:
- El envío de IDs de ciudadanos, nombres reales o datos de contacto.
- La transferencia de datasets de entrenamiento propietarios.
- La ejecución de misiones remotas que modifiquen el estado de persistencia del nodo vecino.

---
**"La interoperabilidad técnica es el puente que permite la cooperación sin sacrificar la independencia."**
