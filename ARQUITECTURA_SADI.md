# Arquitectura SADI (Sistema de Acceso y Despliegue Inteligente)

## 1. Visión General

El principio rector de SADI es permitir que el 100% de las operaciones administrativas del sistema Sarita puedan ser ejecutadas mediante comandos de voz en lenguaje natural. Esto se logra a través de una arquitectura de servicios desacoplada, donde la lógica de negocio reside en el backend y es agnóstica a la interfaz de usuario.

## 2. Arquitectura Jerárquica

La inteligencia de SADI se estructura en una jerarquía de tres niveles, diseñada para procesar, validar y ejecutar comandos de forma segura y auditable.

### Nivel 1: Orquestador SADI (El Cerebro)

Es el componente central y el único punto de entrada para los comandos de voz. Sus responsabilidades son:
*   **Recepción:** Recibe el comando en formato de texto plano desde la interfaz (capa de Speech-to-Text).
*   **Clasificación de Intención:** Utiliza un Modelo de Lenguaje Grande (LLM) a través de `langchain` para interpretar el lenguaje natural y traducirlo a una acción estructurada (JSON) con un comando y sus parámetros. Ej: `"Sarita, publica la página de inicio"` -> `{ "accion": "publicar_pagina", "parametros": { "slug": "inicio" } }`.
*   **Validación de Permisos:** Verifica que el usuario autenticado tiene los roles y permisos necesarios para ejecutar la acción solicitada.
*   **Gestión de Confirmación:** Para acciones clasificadas como `Críticas` o de `Escritura`, el orquestador no ejecuta la acción de inmediato. En su lugar, devuelve una pregunta de confirmación al usuario (Ej: "¿Estás seguro de que deseas desactivar este plan? Esta acción no se puede deshacer.").
*   **Auditoría:** Registra cada comando recibido y su resultado (éxito, fallo, pendiente de confirmación) en un log de auditoría (`SadiAuditLog`).

### Nivel 2: Tácticos (Intérpretes Especializados)

*En la implementación inicial, el Orquestador se comunicará directamente con los Ejecutores. Los Tácticos representan una capa de especialización futura.*

Los Tácticos son módulos especializados en dominios de negocio específicos. Un `Táctico de Contenidos`, por ejemplo, sabría cómo manejar secuencias complejas como "crea una nueva página, asígnale esta plantilla y publícala en el menú principal". Descomponen estas órdenes complejas en llamadas simples a los Ejecutores.

### Nivel 3: Ejecutores (Los Brazos)

Son los servicios de negocio ya existentes en la arquitectura de Sarita. Cada servicio expone funciones atómicas que realizan una única operación de negocio bien definida.
*   **Ejemplos:** `PaymentService`, `OrderService`, `gestion_plataforma_service`, `api_services`.
*   **Responsabilidad:** Contienen la lógica de negocio final para interactuar con los modelos de Django y la base de datos. Son la única capa que puede mutar el estado del sistema.

## 3. Flujo de un Comando

1.  **Entrada:** El usuario emite un comando de voz.
2.  **Traducción:** La UI convierte la voz a texto y la envía al endpoint `/api/sadi/command/`.
3.  **Orquestación:** El `SadiOrquestadorService` recibe el texto.
4.  **Proceso:** Clasifica la intención, valida permisos y, si la acción no es crítica, la delega al Ejecutor correspondiente. Si es crítica, solicita confirmación.
5.  **Ejecución:** El servicio Ejecutor realiza la operación.
6.  **Auditoría:** El Orquestador registra el resultado en `SadiAuditLog`.
7.  **Respuesta:** El Orquestador devuelve una respuesta en lenguaje natural (Ej: "Página publicada con éxito") que la UI convierte de texto a voz para el usuario.
