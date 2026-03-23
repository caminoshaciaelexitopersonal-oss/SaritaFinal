# REGISTRO DE SEÑALES DEFENSIVAS (S-1.1)

## 1. Fuentes de Señal (Sensores)

| Sensor | Origen | Tipo de Datos | Descripción |
| :--- | :--- | :--- | :--- |
| **S-UI** | Frontend Logs | Eventos de DOM, JS Errors | Captura intentos de XSS y mutaciones no autorizadas. |
| **S-KERNEL** | GovernanceKernel | Intenciones rechazadas | Detecta intentos de violar niveles de autoridad. |
| **S-AGENT** | SaritaAgents | Errores de misión / Retry | Monitorea si un agente está en bucle o desalineado. |
| **S-API** | API / AuditLog | Frecuencia de peticiones | Detecta patrones de abuso, scraping o fuerza bruta. |
| **S-VOICE** | SADI Engine | NLP Semantic Anomaly | Identifica inyecciones de comandos en lenguaje natural. |

## 2. Clasificación de Anomalías

### A. Repetición Anormal
- **Criterio:** > 10 intentos fallidos en < 1 minuto.
- **Riesgo:** 🟡 Riesgo leve (Posible Brute Force).

### B. Secuencias Imposibles
- **Criterio:** Acceso a `/api/v1/facturacion/` sin haber pasado por `/api/v1/auth/`.
- **Riesgo:** 🟠 Riesgo sistémico (Logic Bypass).

### C. Accesos Fuera de Rol
- **Criterio:** Un rol `PRESTADOR` intentando acceder a `PLATFORM_SUSPEND_USER`.
- **Riesgo:** 🔴 Ataque activo (Privilege Escalation).

### D. Mutaciones Ilegítimas
- **Criterio:** Inyección de nodo `<script>` detectada por `SecurityShield`.
- **Riesgo:** 🔴 Ataque activo (XSS).

### E. Evasión del Kernel
- **Criterio:** Intento de modificar `GovernancePolicy` sin token de SuperAdmin.
- **Riesgo:** 🔴 Ataque activo (Sovereignty Threat).

## 3. Matriz de Intensidad
- **🟢 RUIDO:** Eventos aislados sin patrón malicioso.
- **🟡 RIESGO LEVE:** Patrones sospechosos de baja intensidad.
- **🟠 RIESGO SISTÉMICO:** Amenazas dirigidas a la disponibilidad o lógica.
- **🔴 ATAQUE ACTIVO:** Intento de compromiso total o exfiltración.

---
**"La IA puede reaccionar más rápido que el humano, pero nunca puede redefinir las reglas del sistema."**
