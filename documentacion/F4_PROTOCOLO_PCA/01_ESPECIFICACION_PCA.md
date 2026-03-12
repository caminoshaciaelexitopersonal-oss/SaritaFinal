# Especificación Formal del Protocolo de Coordinación de Agentes (PCA)

## 1. Definición del Protocolo
El PCA es el estándar estructural de comunicación e inteligencia colectiva del Sistema SARITA. Su propósito es garantizar que la interacción entre agentes sea formal, auditable y esté orientada al consenso bajo la supervisión del MCP.

## 2. Contrato de Mensajes (PCA Message Schema)
Todo mensaje intercambiado en el PCA debe seguir estrictamente este esquema JSON:

```json
{
  "header": {
    "message_id": "UUID",
    "correlation_id": "UUID (ID Global MCP)",
    "sender": {
      "agent_id": "STRING",
      "role": "STRING",
      "authority_level": "INT"
    },
    "target": "STRING (AgentID | BROADCAST)",
    "timestamp": "ISO-8601",
    "signature": "SHA256_RSA/HMAC"
  },
  "interaction": {
    "type": "QUERY | VALIDATION | CONTRADICTION | PROPOSAL | CONFIRMATION",
    "priority": "LOW | MEDIUM | HIGH | CRITICAL"
  },
  "payload": {
    "intent": "STRING",
    "parameters": { ... },
    "content": { ... },
    "evidence_ref": [ "UUID_LOG", ... ]
  },
  "intelligence": {
    "confidence_score": "FLOAT (0.0 - 1.0)",
    "reasoning": "STRING (Justificación lógica)",
    "consensus_vote": "APPROVE | REJECT | ABSTAIN"
  }
}
```

## 3. Tipos de Interacción
- **QUERY (Consulta):** Un agente solicita información o criterio a otro especialista.
- **VALIDATION (Validación):** Un agente verifica una propuesta de otro agente basándose en su propia base de conocimientos.
- **CONTRADICTION (Contradicción):** Un agente presenta una objeción formal a una decisión en curso, obligatoriamente adjuntando razonamiento.
- **PROPOSAL (Propuesta Alternativa):** Ante un rechazo o bloqueo, un agente sugiere una vía de acción distinta.
- **CONFIRMATION (Confirmación Final):** Cierre de la interacción tras alcanzar consenso.

## 4. Seguridad del Protocolo
- **Autenticación Mutua:** Cada agente debe autenticarse ante el PCA Broker usando tokens efímeros firmados.
- **Integridad de Mensaje:** El hash del payload se incluye en la firma para detectar manipulaciones en tránsito.
- **Aislamiento:** Los agentes no pueden comunicarse directamente por fuera del PCA Broker. Cualquier intento de "bypass" es registrado por el Agente Auditor como una brecha de seguridad.

## 5. Message Broker Interno (Lógica)
El Broker no es solo un transportador; es un validador de contratos:
1. **Validación de Esquema:** Rechaza mensajes mal formados.
2. **Control de Autoridad:** Bloquea mensajes si el emisor intenta realizar una acción fuera de su ámbito de competencia.
3. **Persistencia:** Todo mensaje se almacena en la tabla `Agent_Interactions` antes de ser entregado al destinatario.
