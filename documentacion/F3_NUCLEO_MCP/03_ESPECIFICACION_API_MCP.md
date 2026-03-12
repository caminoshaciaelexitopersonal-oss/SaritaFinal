# Especificación de la API Interna del MCP

## 1. Endpoints de Control

### 1.1 `POST /api/mcp/command/`
Punto de entrada para todas las acciones que requieren orquestación.
- **Payload:**
  ```json
  {
    "command": "STRING",
    "params": { ... },
    "metadata": {
      "origin": "STRING",
      "signature": "SHA256_HMAC"
    }
  }
  ```
- **Respuesta:** `202 Accepted` + `ID_GLOBAL`.

### 1.2 `POST /api/mcp/evaluate/`
Invoca manualmente al motor de evaluación para pre-chequeos.
- **Respuesta:** Nivel de riesgo y plan de acción sugerido.

### 1.3 `GET /api/mcp/status/{id_global}/`
Consulta el estado actual de una orquestación y su historial.

### 1.4 `POST /api/mcp/rollback/{id_global}/`
Fuerza el inicio del protocolo de compensación para una transacción específica.

### 1.5 `POST /api/mcp/cancel/{id_global}/`
Detiene una orquestación en curso (si el estado lo permite).

## 2. Estructura de Respuesta Estándar
```json
{
  "id_global": "UUID",
  "status": "EXECUTED | FAILED | IN_PROGRESS",
  "timestamp": "ISO-8601",
  "security": {
    "risk_level": "LOW | MEDIUM | HIGH",
    "confidence_score": 0.95
  },
  "audit": {
    "hash_chain": "SHA256_LINK",
    "decisions": [ ... ]
  }
}
```

## 3. Códigos de Error MCP
- `MCP-001`: Error de firma digital.
- `MCP-002`: Riesgo inaceptable detectado.
- `MCP-003`: Conflicto de agentes no resuelto.
- `MCP-004`: Tiempo de espera (timeout) en orquestación.
