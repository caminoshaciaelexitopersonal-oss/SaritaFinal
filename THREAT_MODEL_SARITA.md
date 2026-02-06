# MODELO DE AMENAZAS SARITA (S-4.0) — BLINDAJE TOTAL

## 1. Introducción
Este documento actualiza el panorama de amenazas incorporando vectores de ataque avanzados identificados en la Fase de Blindaje Total.

## 2. Nuevos Vectores de Ataque Identificados

### Subfase A.1: Abuso por Roles Legítimos
*   **Amenaza:** Un Prestador intentando acceder a métricas de la competencia mediante manipulación de parámetros de filtrado o fuerza bruta en UUIDs correlacionados.
*   **Mitigación:** Validación estricta de Ownership en cada consulta (Query-Level Security).

### Subfase A.2: Scraping y Crawling Agresivo
*   **Amenaza:** Extracción masiva de inventarios turísticos o datos de precios por parte de terceros no autorizados.
*   **Mitigación:** Rate limiting por IP/Sesión y detección de patrones de navegación no humanos.

### Subfase A.3: Ataques de Repetición (Replay)
*   **Amenaza:** Interceptación y reenvío de peticiones de aprobación financiera o cambios de estado en misiones de agentes.
*   **Mitigación:** Implementación de Nonces y Timestamps en intenciones críticas.

### Subfase A.4: Inyección en Agentes (Prompt Injection)
*   **Amenaza:** Usuarios intentando "engañar" a SARITA para que ejecute acciones fuera de su política de gobernanza mediante lenguaje natural.
*   **Mitigación:** Gobernanza por Kernel (Hard Guardrails) que valida la intención física, no solo el comando lógico.

## 3. Clasificación de Actores Actualizada
| Actor | Motivación | Capacidad |
| :--- | :--- | :--- |
| **Atacante Externo** | Lucro / Sabotaje | Alta (Automatización) |
| **Usuario Interno** | Fraude / Espionaje | Media (Acceso Legítimo) |
| **Crawler Malicioso** | Robo de Datos | Alta (Velocidad) |
| **APT / Infiltrado** | Control Soberano | Muy Alta |

---
**"Soberanía es la capacidad de decidir quién entra, quién se queda y quién es expulsado del sistema."**
