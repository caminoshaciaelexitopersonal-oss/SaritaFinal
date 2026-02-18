# Modelo de Autoridad y Motor de Consenso (PCA)

## 1. Modelo de Autoridad Jerárquica
La autoridad en SARITA no es uniforme. Se define mediante una matriz de pesos basada en la jerarquía militar y la especialidad técnica.

### 1.1 Niveles de Autoridad (L)
- **Nivel 3 (Soberano):** Peso Base = 1.0 (Ej. Agente Auditor, Cumplimiento).
- **Nivel 2 (Coordinador):** Peso Base = 0.7 (Ej. Agente Coordinador/Coronel).
- **Nivel 1 (Operativo):** Peso Base = 0.4 (Ej. Tenientes Especialistas).

### 1.2 Factor de Especialidad (S)
El peso de un voto se incrementa si la intención del comando coincide con la especialidad del agente.
- **Match de Especialidad:** S = 1.5
- **No Match:** S = 1.0

## 2. Algoritmo de Consenso Ponderado
Para una decisión dada, el PCA calcula el **Consenso Final (CF)**:

$$CF = \frac{\sum (Voto_i \times L_i \times S_i)}{\sum (L_i \times S_i)}$$

Donde:
- $Voto_i$: +1 para APPROVE, -1 para REJECT.
- $L_i$: Nivel de autoridad del agente $i$.
- $S_i$: Factor de especialidad del agente $i$.

### 2.1 Umbrales de Aprobación
- **Aprobación Estándar:** $CF > 0.5$
- **Aprobación Crítica:** $CF > 0.8$ (Requiere casi unanimidad o votos de alta autoridad).
- **Bloqueo Automático:** Si un Agente de Nivel 3 emite un REJECT en su ámbito de competencia ($S=1.5$), el comando se bloquea independientemente de otros votos (Derecho a Veto).

## 3. Motor de Consenso (Lógica de Ejecución)
1. **Recolección:** El PCA Broker abre una ventana de tiempo (Timeout) para recibir votos.
2. **Evaluación de Divergencia:** Si la desviación estándar de los votos es alta, se activa el Protocolo de Resolución de Conflictos.
3. **Cálculo:** Se aplica la fórmula de consenso ponderado.
4. **Informe al MCP:** Se entrega el resultado final con un `Confidence Score`.

## 4. Matriz de Pesos por Especialidad (Ejemplo)

| Agente | Especialidad | Peso Base (L) | Ámbito Primario |
| :--- | :--- | :---: | :--- |
| **Auditor** | Auditoría | 1.0 | Seguridad, Trazabilidad |
| **Cumplimiento** | Legal/DIAN | 1.0 | Fiscal, Normativo |
| **Riesgo** | Finanzas | 0.8 | Transacciones, Crédito |
| **Coordinador** | General | 0.7 | Flujos de Trabajo |
| **Ventas** | Comercial | 0.4 | Marketing, Tarifas |
