# Especificación de APIs Base - Sistema SARITA

## 1. Estándares de Diseño
SARITA sigue el principio de **API-First Design**.

### 1.1 Estilo Arquitectónico
- **RESTful API:** Para operaciones CRUD y lógica de negocio estándar.
- **GraphQL:** (Opcional) Para consultas de datos complejos en el dashboard que requieran múltiples relaciones.
- **gRPC:** Para comunicación de alta eficiencia entre microservicios internos.

### 1.2 Formatos de Datos
- **JSON:** Formato estándar para intercambio de datos.
- **UTF-8:** Codificación obligatoria.
- **ISO 8601:** Formato de fecha y hora (`YYYY-MM-DDTHH:mm:ssZ`).

## 2. Versionado
- El versionado se maneja a través de la URL: `https://api.sarita.com/v1/...`
- Las versiones antiguas se mantienen por un periodo de transición (mínimo 6 meses) tras el lanzamiento de una nueva versión.

## 3. Estructura de Respuesta Estándar
Todas las respuestas de la API deben seguir esta estructura:

```json
{
  "status": "success | error",
  "data": { ... },
  "meta": {
    "trace_id": "UUID",
    "timestamp": "ISO-8601",
    "pagination": { ... }
  },
  "error": {
    "code": "STRING_CODE",
    "message": "Mensaje legible",
    "details": [ ... ]
  }
}
```

## 4. Endpoints Nucleares (Core)
- `/auth/`: Gestión de identidad y tokens.
- `/governance/intentions/`: Registro y consulta de intenciones de negocio.
- `/agents/dispatch/`: Punto de entrada para interactuar con la jerarquía de agentes.
- `/providers/`: Gestión de perfiles de prestadores turísticos.

## 5. Manejo de Errores
- **400 Bad Request:** Error de validación de cliente.
- **401 Unauthorized:** Token faltante o inválido.
- **403 Forbidden:** Falta de permisos (Nivel de autoridad insuficiente).
- **404 Not Found:** Recurso inexistente.
- **429 Too Many Requests:** Límite de tasa excedido.
- **500 Internal Server Error:** Error inesperado en el servidor.
