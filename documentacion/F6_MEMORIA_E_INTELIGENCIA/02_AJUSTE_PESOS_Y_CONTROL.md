# Ajuste Dinámico de Pesos y Control de Cambios Adaptativos

El Sistema SARITA evoluciona ajustando dinámicamente la influencia de sus componentes basándose en datos reales de desempeño, bajo un marco de control estricto que impide cambios caprichosos o inseguros.

## 1. Ajuste Dinámico de Pesos (PCA)

### 1.1 El Índice de Precisión del Agente (API - Agent Precision Index)
Se calcula como el ratio entre votos exitosos (alineados con el resultado final del MCP) y el total de votos emitidos en misiones cerradas.

$$API = \frac{Votos\_Correctos}{Votos\_Totales}$$

### 1.2 Reglas de Ajuste
- **Degradación:** Si $API < 0.60$ durante 10 misiones consecutivas, se genera una propuesta de reducción del multiplicador de peso en un 10%.
- **Promoción:** Si $API > 0.95$ durante 20 misiones, el motor sugiere un incremento del 5% en su peso base (hasta un límite de 1.2x).
- **Recuperación:** Un agente degradado puede recuperar su peso original demostrando precisión en misiones supervisadas por un Agente de Nivel 3.

## 2. Control de Cambios Adaptativos (Adaptive Governance)

### 2.1 Flujo de Aprobación
1. **Generación:** El `AdaptiveEngine` detecta una anomalía o una oportunidad de mejora y crea una `AdaptiveProposal`.
2. **Validación Forense:** El Agente Auditor verifica que el cambio propuesto no viola ninguna política regulatoria (ej. No puede reducirse el peso del Agente de Cumplimiento por debajo de 1.0).
3. **Soberanía Humana:** Todas las propuestas de ajuste de pesos o cambios en umbrales de riesgo se notifican al Administrador Superior. El cambio solo se aplica (`is_applied=True`) tras firma digital humana.

## 3. Seguridad y Anti-Bucle
Para evitar que el sistema entre en bucles de aprendizaje erróneo (Positive Feedback Loops):
- **Límites de Peso:** Ningún agente operativo puede superar el peso de un agente coordinador.
- **Ventana de Observación:** No se permiten más de dos ajustes de peso al mismo agente en un periodo de 30 días.
- **Rollback de Aprendizaje:** El sistema mantiene versiones de los pesos. Si el rendimiento global decae tras un ajuste, el MCP puede forzar un retorno a la versión "Estable" anterior.

## 4. Auditoría de Inteligencia
Cada ajuste de peso queda registrado con:
- Razonamiento lógico del AIM.
- Datos históricos que sustentan la decisión.
- Identificador del administrador que aprobó la aplicación.
