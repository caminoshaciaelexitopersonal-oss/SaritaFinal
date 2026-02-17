# PLAN DE INDEPENDENCIA DE PROVEEDORES Y DEGRADACIÓN CON DIGNIDAD

**Objetivo:** Garantizar que SARITA siga operando si los proveedores externos (OpenAI, Google, AWS, etc.) dejan de estar disponibles o bloquean el acceso.

## 1. INDEPENDENCIA DE MODELOS DE LENGUAJE (LLM)
SARITA está diseñado con una **Capa de Abstracción de IA**.
- **Plan A (Actual):** OpenAI (GPT-4o) para máxima precisión semántica.
- **Plan B (Soberanía):** Despliegue de modelos locales (Llama 3 o Mistral) en servidores propios.
- **Plan C (Degradación):** Uso de motores basados en reglas y gramáticas locales para el procesamiento de comandos de voz básicos.

## 2. REEMPLAZO DE APIS EXTERNAS
| Servicio Externo | Función | Alternativa Local / Soberana |
| :--- | :--- | :--- |
| **STT (Whisper/OpenAI)** | Voz a Texto | Vosk u OpenAI Whisper (Local Server) |
| **TTS (Google/Azure)** | Texto a Voz | Piper o Coqui TTS (Local) |
| **Maps (Google)** | Geocodificación | OpenStreetMap + Pelias |
| **Email (SendGrid)** | Notificaciones | Servidor SMTP Propio / Postfix |

## 3. PROTOCOLO DE DEGRADACIÓN CON DIGNIDAD
Si un servicio crítico falla:
1. **Detección de Timeout:** El `httpClient` del frontend y los servicios backend detectan la caída en < 15 segundos.
2. **Modo Offline/Local:** El sistema notifica al usuario: "IA Avanzada fuera de línea. Operando con Motor de Emergencia Local".
3. **Persistencia en Cola:** Las acciones que requieran procesamiento pesado se encolan en Redis/Celery para su ejecución posterior cuando se restaure la conectividad.

## 4. PROHIBICIÓN DE DEPENDENCIA SILENCIOSA
Se prohíbe la inclusión de librerías o servicios que:
- Requieran conexión obligatoria a internet para el arranque del sistema.
- Cuenten con "Kill Switches" remotos controlados por el fabricante.
- No permitan la exportación total de datos en formatos abiertos (JSON, CSV, SQL).

---
**Soberanía Tecnológica Garantizada.**
