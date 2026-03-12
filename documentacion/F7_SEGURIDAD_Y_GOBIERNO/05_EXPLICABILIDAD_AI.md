# Explicabilidad AI y Transparencia - Sistema SARITA

## 1. El Explainability Log
Cada decisión tomada por el sistema SARITA debe ser explicable en términos humanos y técnicos.

### 1.1 Estructura del Log
```json
{
  "decision_id": "UUID",
  "outcome": "APPROVED | REJECTED",
  "reasoning_chain": [
    {
      "agent": "AgenteRiesgo",
      "input": "Monto $5000",
      "logic": "Excede umbral histórico de $3000 para este prestador.",
      "vote": "REJECT"
    },
    {
      "agent": "AgenteComercial",
      "input": "Temporada Alta",
      "logic": "Alineado con demanda de mercado.",
      "vote": "APPROVE"
    }
  ],
  "final_justification": "Aunque comercialmente es viable, el riesgo supera el límite de confianza histórica del 85%."
}
```

## 2. Transparencia para el Usuario
- **Nivel Ejecutivo:** Reportes legibles que explican por qué una reserva fue bloqueada o un pago rechazado.
- **Nivel Técnico:** Acceso al grafo de decisiones completo en el Shadow Ledger.

## 3. Auditoría de Sesgos
Trimestralmente, el Agente Auditor genera un informe de correlación para detectar si ciertos agentes están tomando decisiones sesgadas basándose en variables protegidas (e.g., origen del prestador, tipo de moneda), forzando el ajuste de los pesos PCA si se detecta desviación ética.

## 4. Derecho a la Explicación (Alineación Legal)
SARITA cumple con el artículo 22 de GDPR, permitiendo que cualquier usuario afectado por una decisión automatizada solicite la intervención humana y una explicación clara de la lógica utilizada.
