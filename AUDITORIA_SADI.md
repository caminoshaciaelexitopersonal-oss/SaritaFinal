# Documento de Auditoría SADI

## 1. Propósito

El sistema SADI (Sistema de Acceso y Despliegue Inteligente) está diseñado para ejecutar acciones administrativas significativas a través de comandos de voz. Dada la naturaleza crítica de estas operaciones, es fundamental mantener un registro inmutable y detallado de cada comando procesado. Este documento describe el mecanismo de auditoría implementado para garantizar la trazabilidad, la seguridad y la capacidad de análisis post-mortem.

## 2. El Modelo `SadiAuditLog`

La auditoría se centraliza en el modelo `SadiAuditLog` de Django, ubicado en la aplicación `sadi_agent`. Cada vez que un comando de voz es recibido por el `SadiOrquestadorService`, se crea una nueva instancia de este modelo para registrar el ciclo de vida completo de la petición.

### 2.1. Estructura del Modelo

La estructura del modelo `SadiAuditLog` es la siguiente:

```python
class SadiAuditLog(models.Model):
    # El administrador que ejecutó el comando.
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, ...)

    # El texto original del comando de voz.
    comando_original = models.TextField(...)

    # La acción estructurada que el LLM interpretó.
    accion_ejecutada = models.JSONField(...)

    # El resultado de la operación.
    resultado = models.TextField(...)

    # Timestamp de la ejecución.
    timestamp = models.DateTimeField(auto_now_add=True, ...)
```

### 2.2. Descripción de los Campos

*   **`usuario`**: Un `ForeignKey` al modelo `CustomUser`. Identifica qué administrador emitió el comando. Es un campo `SET_NULL` para que, si un usuario es eliminado, sus registros de auditoría persistan.
*   **`comando_original`**: Un campo de texto (`TextField`) que almacena la transcripción literal del comando de voz recibido por la API. Esto es crucial para entender la intención original del usuario.
*   **`accion_ejecutada`**: Un campo `JSONField` que almacena la interpretación estructurada del comando por parte del LLM. Guarda la "intención" y los "parámetros" extraídos. Ejemplo: `{"accion": "CREAR_PLAN", "parametros": {"nombre": "premium", ...}}`.
*   **`resultado`**: Un campo de texto que almacena el resultado final del procesamiento. Guarda tanto los mensajes de éxito como los de error, proporcionando un feedback claro de lo que ocurrió.
*   **`timestamp`**: Un `DateTimeField` que se establece automáticamente (`auto_now_add=True`) en el momento en que se crea el registro. Garantiza una línea de tiempo cronológica precisa de todos los comandos.

## 3. Flujo de Auditoría en el Orquestador

El `SadiOrquestadorService` garantiza la auditoría siguiendo estos pasos:

1.  **Registro Inmediato:** Tan pronto como se recibe un comando en el método `process_voice_command`, se crea inmediatamente una entrada en `SadiAuditLog` con el `comando_original`, el `usuario` y un estado inicial como "Procesando...".
2.  **Actualización Post-Interpretación:** Después de que el LLM (simulado o real) interpreta el comando, el campo `accion_ejecutada` del registro se actualiza con la estructura JSON.
3.  **Registro del Resultado Final:** Una vez que el comando se ejecuta (ya sea con éxito o con un error), el campo `resultado` se actualiza con el mensaje final que se devolverá al usuario.

Este enfoque garantiza que incluso los comandos fallidos queden registrados, lo que es vital para la depuración y la seguridad.
