# FASE X: ORQUESTACIÓN POR VOZ — REPORTE DE IMPLEMENTACIÓN Y VERIFICACIÓN

**Fecha:** 2024-07-29

**Estado:** `FINALIZADO`

---

### 1. Objetivo de la Fase

El objetivo principal de la Fase X fue implementar un "Voice Gateway" (Pasarela de Voz) capaz de recibir un comando en lenguaje natural, traducirlo a una directiva estructurada para el sistema de agentes SADI, invocar la API asíncrona de misiones, y generar una respuesta final en lenguaje natural para el usuario.

Esta fase se centró en crear el *middleware* de orquestación, no en la tecnología de transcripción de voz (speech-to-text), que se asume como un componente externo.

### 2. Componentes Implementados

Para cumplir con el objetivo, se desarrollaron los siguientes componentes clave dentro del módulo `sadi_agent`:

#### 2.1. `VoiceOrchestrator` (`voice_orchestrator.py`)

- **Propósito:** Es la clase central que encapsula toda la lógica de orquestación. Gestiona el flujo completo desde la recepción del texto hasta la generación de la respuesta final.
- **Estructura:**
  - **`__init__(self, api_token, api_base_url)`:** Inicializa el orquestador con el token de autenticación y la URL de la API de SARITA.
  - **`handle_voice_command(self, text)`:** Es el método principal que ejecuta la secuencia de pasos de orquestación.

#### 2.2. Intérprete de Intención (`_translate_intent_to_directive`)

- **Función:** Simula un motor de procesamiento de lenguaje natural (NLP/NLU). Utiliza expresiones regulares (`regex`) para identificar la intención del usuario y extraer las entidades necesarias (ej. nombre del prestador, NIT) del texto.
- **Resultado:** Genera un diccionario Python (JSON) que representa la `Directiva` que la API de SARITA espera.

#### 2.3. Integración con la API de SARITA

- **`_invoke_sarita_api(self, directive)`:**
  - Envía la directiva generada al endpoint `POST /api/sarita/directive/`.
  - Maneja la respuesta `202 ACCEPTED` y extrae el `mission_id`.
  - Incluye manejo de errores para respuestas inesperadas de la API.
- **`_poll_mission_status(self, mission_id)`:**
  - Realiza un sondeo (polling) periódico al endpoint `GET /api/sarita/missions/{mission_id}/`.
  - Espera hasta que el estado de la misión sea `COMPLETADA`, `FALLIDA` o `CANCELADA`.
  - Implementa un `timeout` para evitar bucles infinitos.

#### 2.4. Generador de Respuesta Hablada (`_generate_spoken_response`)

- **Función:** Convierte el objeto de estado final de la misión en una frase coherente y en lenguaje natural.
- **Lógica:** Genera diferentes respuestas según el estado final (`COMPLETADA` vs. `FALLIDA`) e incluye el `reporte_final` de la misión para dar un feedback claro al usuario.

#### 2.5. Herramienta de Verificación (`run_voice_command`)

- **Tipo:** Comando de gestión de Django (`management command`).
- **Uso:** `python backend/manage.py run_voice_command "<texto del comando>"`
- **Funcionalidad:**
  - Permite simular un comando de voz desde la línea de comandos.
  - Obtiene automáticamente el token de API para un usuario (por defecto, `sadi`).
  - Instancia y ejecuta el `VoiceOrchestrator`, mostrando logs del proceso.
  - Imprime la respuesta final, validando el flujo de extremo a extremo.

### 3. Flujo de Ejecución Verificado

El flujo de datos y control es el siguiente:

1.  Un usuario (o el script de prueba) invoca el sistema con un comando: `"Sarita, necesito registrar un nuevo prestador. Se llama 'La Fonda Paisa' y su NIT es 900.123.456-7."`
2.  El `VoiceOrchestrator` recibe este texto.
3.  `_translate_intent_to_directive` lo procesa y genera la directiva: `{ "mision": "onboard_prestador", "parametros": { ... } }`.
4.  `_invoke_sarita_api` envía esta directiva a la API de SARITA, que la acepta y devuelve un `mission_id`.
5.  `_poll_mission_status` comienza a consultar el estado de la misión usando el `mission_id`.
6.  Mientras tanto, el motor de agentes SADI (Celery, etc.) ejecuta la misión de forma asíncrona.
7.  Una vez la misión concluye, el polling detecta el estado final (`COMPLETADA`).
8.  `_generate_spoken_response` toma el resultado final y genera la respuesta: `"Misión completada con éxito. El prestador 'La Fonda Paisa' ha sido creado con ID 123."`
9.  Esta respuesta final se devuelve al usuario.

### 4. Conclusión de la Fase

La Fase X ha sido completada con éxito. Se ha establecido una pasarela de voz robusta y desacoplada que se integra perfectamente con la arquitectura de agentes asíncrona existente. El sistema es ahora capaz de ser controlado mediante comandos en lenguaje natural, cumpliendo con todos los objetivos definidos.

La funcionalidad ha sido verificada de extremo a extremo utilizando la herramienta `run_voice_command`, demostrando la correcta orquestación entre el nuevo módulo de voz, la API de SARITA y el motor de ejecución de misiones.
