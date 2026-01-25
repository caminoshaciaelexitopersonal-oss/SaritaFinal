# Reporte de Ejecución - Fase VW (Motor de Agentes y API)

## 1. Resumen de la Fase

Esta fase tuvo como objetivo transformar a SARITA en un motor de agentes robusto, asíncrono y consumible a través de una API REST. Se implementó la infraestructura para la ejecución de tareas en segundo plano (Celery + Redis) y se expusieron los endpoints necesarios para lanzar y monitorear misiones.

El flujo se ejecutó con éxito, validando que el motor de agentes puede operar de forma asíncrona sin romper la jerarquía y que la capa de API actúa como una puerta de enlace delgada y desacoplada.

## 2. Decisiones de Diseño y Arquitectura

- **Asincronía (Celery):** Se eligió Celery por su madurez e integración con Django. La asincronía se introdujo en dos niveles:
    1.  **Nivel de API:** La vista `DirectiveView` encola una tarea (`ejecutar_mision_completa`) y responde inmediatamente, desacoplando la solicitud HTTP de la ejecución de la misión.
    2.  **Nivel de Teniente:** El `CapitanTemplate` encola las tareas de los tenientes (`ejecutar_tarea_teniente`), permitiendo que la planificación sea rápida y la ejecución de tareas de E/S ocurra en segundo plano.
- **Robustez:** Se configuraron reintentos automáticos a nivel de tarea de Celery para manejar fallos transitorios. Se implementó una clave de idempotencia a nivel de `Mision` para prevenir la duplicación de solicitudes.
- **Logging Estructurado:** Todas las sentencias `print()` fueron reemplazadas por el sistema de logging de Django, añadiendo contexto de la misión y la tarea a cada mensaje.
- **Capa de API:** Se diseñó una capa de API delgada y sin estado. La vista de creación solo valida la entrada y delega, mientras que la vista de estado actúa como una ventana de solo lectura hacia la capa de persistencia. La seguridad se garantiza con la autenticación por token de DRF.
- **Flujo de Trabajo Asíncrono (`chord`):** Para resolver el problema de la finalización prematura de las misiones, se implementó un `chord` de Celery. El Capitán ahora define un grupo de tareas de Tenientes que se ejecutan en paralelo, y una tarea de `consolidar_plan_tactico` se ejecuta como *callback* solo cuando todas las tareas del grupo han terminado. Esta tarea de consolidación, a su vez, encola la tarea final `finalizar_mision`, garantizando que la misión solo se marque como `COMPLETADA` cuando todo el trabajo ha finalizado.
- **Transacciones de Base de Datos:** Se utilizó `transaction.on_commit` para asegurar que las tareas de Celery solo se enquen *después* de que la transacción de base de datos que crea la `Mision` se haya confirmado, evitando condiciones de carrera.

## 3. Evidencia de Ejecución Real (vía API)

### 3.1. Petición POST para Iniciar la Misión

**Comando:**
```bash
curl -X POST \
  -H "Authorization: Token <tu_token>" \
  -H "Content-Type: application/json" \
  -d '{"domain": "prestadores", "mission": {"type": "ONBOARDING_PRESTADOR", "datos": {"nombre": "Hotel Final Transaction", "email": "contacto@finaltransaction.com"}}}' \
  http://127.0.0.1:8000/api/sarita/directive/
```

**Respuesta (202 Accepted):**
```json
{
  "mission_id": "3090429a-dd50-431d-907d-816ff351d8bc",
  "status": "EN_COLA"
}
```

### 3.2. Petición GET para Consultar el Estado Final

**Comando:**
```bash
curl -X GET \
  -H "Authorization: Token <tu_token>" \
  http://127.0.0.1:8000/api/sarita/missions/3090429a-dd50-431d-907d-816ff351d8bc/
```

**Respuesta (200 OK):**
```json
{
    "id": "3090429a-dd50-431d-907d-816ff351d8bc",
    "planes_tacticos": [
        {
            "id": "...",
            "tareas": [
                {
                    "id": "...",
                    "logs_ejecucion": [
                        {
                            "exitoso": true,
                            "resultado": {
                                "status": "SUCCESS",
                                "message": "Datos básicos validados correctamente."
                            }
                        }
                    ],
                    "estado": "COMPLETADA"
                },
                {
                    "id": "...",
                    "logs_ejecucion": [
                        {
                            "exitoso": true,
                            "resultado": {
                                "status": "SUCCESS",
                                "message": "Prestador creado exitosamente.",
                                "prestador_id": "..."
                            }
                        }
                    ],
                    "estado": "COMPLETADA"
                }
            ],
            "estado": "COMPLETADO"
        }
    ],
    "estado": "COMPLETADA",
    "resultado_final": {
        "status": "FORWARDED",
        "captain_report": {
            "captain": "CapitanOnboardingPrestador",
            "status": "COMPLETADO",
            "details": "..."
        },
        "report_from": "Coronel (prestadores)"
    }
}
```

## 4. Conclusiones

La Fase VW ha sido completada con éxito. Se ha demostrado que la arquitectura SARITA puede:
- Operar de forma asíncrona sin comprometer la jerarquía.
- Ser expuesta de forma segura y controlada a través de una API REST.
- Mantener una trazabilidad completa de cada misión.
- Manejar correctamente el estado de la misión a lo largo del flujo de trabajo asíncrono.

El motor de agentes está ahora listo para ser escalado con nuevas misiones y para ser consumido por otros servicios del sistema.
