# PROTOCOLO DE GESTIÓN DE INCIDENTES CRÍTICOS

**Sistema:** SARITA

## 1. DEFINICIÓN DE INCIDENTE CRÍTICO
Se considera incidente crítico cualquier evento que:
- Comprometa la integridad de los datos financieros.
- Muestre una desviación de la IA fuera de sus límites pre-autorizados.
- Represente un riesgo R1 activo por más de 30 minutos.

## 2. PROCEDIMIENTO DE RESPUESTA
1. **Detección:** El Observador Sistémico dispara una alerta al SuperAdmin.
2. **Contención:** Activación inmediata del **Kill Switch** (Global o de Dominio).
3. **Aislamiento:** El nodo afectado se pone en modo mantenimiento.
4. **Auditoría Reconstructiva:** Uso del rastro de auditoría con hashes para identificar el punto exacto de la falla.
5. **Corrección y Rollback:** El SuperAdmin revierte los cambios sistémicos mediante el comando de Intervención Soberana.

## 3. REPORTES
Todo incidente crítico genera un informe automático que incluye el rastro XAI de los agentes involucrados y la evidencia de control GRC.

---
**Resiliencia Sistémica.**
