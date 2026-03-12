# Plan de Respuesta a Incidentes de Seguridad - SARITA v1.0

## 1. Clasificación de Incidentes
| Nivel | Tipo | Descripción | Tiempo de Respuesta |
| :--- | :--- | :--- | :--- |
| **CRÍTICO** | Brecha de Datos | Acceso no autorizado a DB o filtración. | Inmediato (< 30 min) |
| **ALTO** | Ataque DDoS | Degradación masiva de disponibilidad. | < 1 hora |
| **MEDIO** | Anomalía de IA | Comportamiento inesperado de agentes. | < 4 horas |
| **BAJO** | Spam / Abuso | Mal uso de formularios o búsqueda. | < 24 horas |

## 2. Fase de Contención y Respuesta
### 2.1 Protocolo ante Brecha de Seguridad
1.  **Aislamiento**: Rotación inmediata de llaves RS256 y API Keys.
2.  **Cuarentena**: Bloqueo de sesiones de usuarios sospechosos mediante `ForensicSecurityLog`.
3.  **Auditoría**: Análisis forense de la cadena de bloques contable para verificar integridad financiera.

### 2.2 Protocolo ante Ataque DDoS
1.  **Escalamiento**: Activación de "Under Attack Mode" en Cloudflare.
2.  **Filtrado**: Bloqueo geográfico (Geo-blocking) de países no operativos.
3.  **HPA**: Forzar escalamiento máximo de Pods en Kubernetes.

## 3. Comunicación de Crisis
*   Notificación a usuarios afectados en menos de 72 horas (Cumplimiento GDPR).
*   Reporte a autoridades regionales competentes.

## 4. Post-Mortem y Mejora
Cada incidente debe generar un reporte detallado con:
*   Causa Raíz.
*   Línea de Tiempo.
*   Acciones Correctivas Permanentes.

---
**Protocolo oficial de ciberseguridad SARITA.**
*Jules, Lead AI & Security Architect.*
