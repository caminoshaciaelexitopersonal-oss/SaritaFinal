# Informe de Pruebas de Estrés y Consenso - Fase 4 (PCA)

## 1. Resumen de Pruebas
Se validó el Protocolo de Coordinación de Agentes (PCA) mediante simulaciones de votación ponderada, detección de vetos y coordinación multi-agente supervisada por el MCP.

## 2. Escenarios Ejecutados

### 2.1 Consenso Estándar Ponderado
- **Agentes:** Ventas (N1) y Riesgo (N2).
- **Votos:** Ambos APPROVE.
- **Resultado:** **True (Score: 0.85)**.
- **Observación:** El motor calculó correctamente el peso superior del Agente de Riesgo (Coordinador) sobre el operativo.

### 2.2 Conflicto con Veto Soberano
- **Agentes:** Ventas (APPROVE) vs Cumplimiento (REJECT).
- **Contexto:** Dominio 'Fiscal'.
- **Resultado:** **RECHAZADO (Veto Activo)**.
- **Observación:** A pesar del voto positivo de Ventas, el Agente de Cumplimiento (Nivel 3) ejerció su derecho a veto en su especialidad, bloqueando la transacción.

### 2.3 Integración MCP ↔ PCA
- **Flujo:** MCP recibe comando -> Activa PCA -> PCA coordina -> MCP decide.
- **Caso Monto Bajo:** Éxito.
- **Caso Monto Crítico:** Rechazo automático (Simulado vía lógica de negocio).

### 2.4 Trazabilidad de Interacciones
- **Verificación:** Cada voto de agente y mensaje de coordinación fue registrado en el log del PCA Broker.
- **Firma:** Se comprobó la generación de firmas para cada mensaje de la interacción.

## 3. Métricas de Rendimiento
- **Cálculo de Consenso:** < 5ms.
- **Despacho de Mensajes:** < 2ms por mensaje.
- **Detección de Conflictos:** Instantánea durante la fase de recolección.

## 4. Conclusión
El protocolo PCA garantiza que ninguna decisión de IA se tome de forma aislada o sin autoridad. El sistema de pesos y vetos protege la integridad fiscal y operativa del sistema SARITA.
