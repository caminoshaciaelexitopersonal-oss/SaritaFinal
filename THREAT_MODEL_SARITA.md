# MODELO DE AMENAZAS SARITA (S-0.1)

## 1. Introducción
Este documento define el panorama de amenazas para el ecosistema SARITA, cubriendo desde la interfaz de usuario hasta el núcleo de gobernanza y los agentes de inteligencia.

## 2. Análisis por Capas

### Capa 1: Interfaz de Usuario (UI)
*   **Amenazas:**
    *   **XSS (Cross-Site Scripting):** Inyección de scripts maliciosos para robar tokens de sesión o manipular la vista del SuperAdmin.
    *   **Inyección de Estados:** Manipulación del contexto de React/Context para saltar protecciones visuales o permisos locales.
    *   **Mutación del DOM:** Alteración ilegítima de elementos de la interfaz para engañar al usuario (clickjacking avanzado).
*   **Clasificación:** Externa / Automatizada.

### Capa 2: Interfaz de Programación (API)
*   **Amenazas:**
    *   **Abuso de Endpoints (Rate Limiting):** Ataques de denegación de servicio o fuerza bruta sobre endpoints críticos (Login, Onboarding).
    *   **Replay Attacks:** Captura y re-envío de peticiones firmadas para duplicar transacciones financieras.
    *   **IDOR (Insecure Direct Object Reference):** Acceso a datos de otros "Tenants" mediante manipulación de UUIDs en la URL.
*   **Clasificación:** Externa / Automatizada / Persistente.

### Capa 3: Núcleo de Gobernanza (Governance Kernel)
*   **Amenazas:**
    *   **Intenciones Falsas:** Intento de inyectar intenciones de negocio directamente al kernel saltando la validación de rol.
    *   **Logic Bypass:** Aprovechar debilidades en la cadena de integridad (hashes) para modificar la bitácora de auditoría.
    *   **Policy Override:** Manipulación de los parámetros de `GovernancePolicy` para desactivar bloqueos soberanos.
*   **Clasificación:** Interna / Persistente.

### Capa 4: Agentes IA (SARITA Agents)
*   **Amenazas:**
    *   **Escalado de Permisos:** Un Teniente intentando ejecutar una misión reservada para un Coronel o el General.
    *   **Misiones Maliciosas:** Inyección de directivas que causen daño económico o reputacional mediante la automatización.
    *   **Exfiltración de Datos:** Uso de agentes para recopilar y enviar información sensible fuera del entorno institucional.
*   **Clasificación:** Interna / IA-Automated.

### Capa 5: Orquestación de Voz (SADI)
*   **Amenazas:**
    *   **Prompt Injection:** Comandos de voz diseñados para confundir al motor semántico y ejecutar acciones no autorizadas.
    *   **Intent Hijacking:** Redirección de una intención legítima hacia una acción crítica mediante ambigüedad fonética.
*   **Clasificación:** Externa / Humana.

## 3. Clasificación de Actores
| Actor | Motivación | Capacidad |
| :--- | :--- | :--- |
| **Atacante Externo** | Lucro / Sabotaje | Alta (Automatización) |
| **Usuario Interno Malicioso** | Fraude / Espionaje | Media (Acceso Legítimo) |
| **IA Desalineada (Agente)** | Error de Lógica / Escalado | Alta (Velocidad de Ejecución) |
| **Actor Persistente (APT)** | Control Soberano | Muy Alta (Infiltración Silenciosa) |

---
**"Todo lo que no esté explícitamente autorizado, será detectado, contenido y neutralizado."**
