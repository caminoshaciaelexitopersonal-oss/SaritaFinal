# FASE Z: INTELIGENCIA Y SEGURIDAD POR VOZ — REPORTE DE IMPLEMENTACIÓN

**Fecha:** 2024-07-30

**Estado:** `FINALIZADO`

---

### 1. Objetivo de la Fase

El objetivo de la Fase Z fue transformar el sistema de voz de SARITA de un simple procesador de comandos a una entidad cognitiva gobernada. Esto implicó la implementación de tres pilares fundamentales:
1.  **Seguridad Voice-First:** Asegurar que solo los usuarios autorizados puedan ejecutar acciones.
2.  **Soporte Multi-Idioma:** Permitir que SARITA entienda y responda en múltiples idiomas.
3.  **Entrenamiento Semántico:** Reemplazar la lógica de `regex` por un motor de interpretación basado en intenciones y entidades.

### 2. Arquitectura Implementada

Para cumplir con estos objetivos, se introdujeron varios componentes nuevos y se refactorizó la arquitectura existente.

#### 2.1. Modelos de la Base de Datos

Se implementó una nueva infraestructura de datos en `sadi_agent/models.py`:
-   **`VoicePermission`**: Modelo para el control de acceso basado en roles (RBAC), que asocia roles de usuario (`CustomUser.Role`) con acciones (`Intent`) en dominios (`SemanticDomain`).
-   **Motor Semántico**:
    -   `SemanticDomain`: Define dominios de conocimiento (ej. "prestadores").
    -   `Intent`: Define las acciones que se pueden realizar (ej. "ONBOARDING_PRESTADOR").
    -   `Example`: Almacena frases de ejemplo en múltiples idiomas para entrenar al motor.
-   **`VoiceInteractionLog`**: Un modelo de auditoría exhaustivo que registra cada paso de una interacción por voz, desde el hash del audio de entrada hasta la respuesta final.

#### 2.2. Nuevos Servicios Desacoplados

-   **`SemanticEngine` (`semantic_engine.py`):**
    -   Reemplaza por completo la lógica de `regex`.
    -   Su método `interpret(text)` busca en los `Example` de la base de datos para identificar la `Intent` del usuario.
    -   Utiliza `regex` específicos de la intención para extraer entidades (`nombre`, `email`).
    -   Implementa un "fallback inteligente" al devolver `None` si la intención no está clara.

-   **`TranslationService` (`translation_service.py`):**
    -   Utiliza la librería `googletrans-py` para la traducción.
    -   `normalize_to_base_language()`: Traduce el texto transcrito al idioma base del sistema (español).
    -   `translate_response()`: Traduce la respuesta final de SARITA de vuelta al idioma original del usuario.

-   **`VoiceSecurity` (`security.py`):**
    -   Implementa el Filtro de Seguridad Pre-Misión.
    -   Su método `is_authorized(user, intent)` consulta el modelo `VoicePermission` para verificar si el rol del usuario le permite ejecutar la acción solicitada.

#### 2.3. Detección de Idioma

-   El `WhisperProvider` fue actualizado para utilizar el `response_format="verbose_json"`, lo que permite capturar el idioma detectado por Whisper y devolverlo junto con el texto transcrito.

### 3. Flujo de Orquestación de la Fase Z

El `VoiceOrchestrator` fue refactorizado masivamente para orquestar el nuevo flujo de ejecución:

1.  **Auditoría Inicial:** Se crea un registro en `VoiceInteractionLog`.
2.  **Transcripción:** `WhisperProvider` transcribe el audio y detecta el idioma.
3.  **Normalización:** `TranslationService` traduce el texto al español.
4.  **Interpretación:** `SemanticEngine` determina la `Intent` y extrae las `Entities`.
5.  **Autorización:** `VoiceSecurity` verifica si el usuario tiene permiso para la `Intent` detectada.
    -   Si se deniega, el flujo se detiene, se genera una respuesta de "permiso denegado" y se audita.
6.  **Ejecución:** Si está autorizado, se construye una directiva y se invoca la API asíncrona de SARITA.
7.  **Respuesta:** La respuesta de la misión se traduce de vuelta al idioma original del usuario.
8.  **Síntesis:** `OpenAITTSProvider` genera el audio de la respuesta final.
9.  **Auditoría Final:** Se completa el registro en `VoiceInteractionLog` con todos los detalles de la interacción.

### 4. Verificación y Pruebas

-   **Población de Datos:** Se creó un nuevo comando, `seed_phase_z_data`, para poblar la base de datos con permisos y ejemplos de entrenamiento en español, inglés y portugués.
-   **Herramienta de Verificación:** El comando `run_voice_flow_from_audio` fue actualizado para ser compatible con el nuevo `VoiceOrchestrator`, permitiendo la inyección de todos los servicios y la simulación de peticiones con diferentes usuarios (`--user`).
-   **Pruebas de Seguridad:** Se verificó que un usuario con rol `ADMIN` puede ejecutar la acción `ONBOARDING_PRESTADOR`, mientras que un usuario con rol `TURISTA` es bloqueado por el `VoiceSecurity`, recibiendo una respuesta de "permiso denegado".
-   **Pruebas Multi-Idioma:** Se realizaron pruebas con audios en inglés, que fueron correctamente transcritos, normalizados a español, procesados por el motor semántico y respondidos en inglés.

### 5. Conclusión de la Fase

La Fase Z ha sido completada con éxito. El sistema de voz de SARITA ha evolucionado de un simple transcriptor a una entidad cognitiva gobernada. La arquitectura ahora es segura, multilingüe, semánticamente consciente y totalmente auditable, cumpliendo con todos los objetivos estratégicos de la directiva. El sistema está preparado para un despliegue productivo controlado.
