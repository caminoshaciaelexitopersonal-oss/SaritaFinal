# GUARDRAILS DE ESCALAMIENTO CONTROLADO (SCALING-GUARDRAILS)

**Estado:** VIGENTE
**Versión:** 1.0
**Enfoque:** Crecimiento Orgánico y Soberano.

---

## 1. LÍMITES DE CAPACIDAD POR NODO (Puerto Gaitán Baseline)

Para garantizar la calidad del servicio y la integridad de la auditoría en tiempo real, se definen los siguientes límites por nodo operativo:

| Métrica | Límite Máximo | Acción al Superar |
| :--- | :--- | :--- |
| **Entidades (Tenants)** | 20 | Despliegue de nuevo Nodo Regional. |
| **Prestadores por Entidad** | 150 | Auditoría de carga y optimización de índices. |
| **Turistas Concurrentes** | 1,000 | Activación de Modo Caché Estático en Vía 3. |
| **Misiones de Agentes** | 50 concurrentes | Escalado de Workers de Celery. |

---

## 2. SEÑALES DE SATURACIÓN (Sovereign Health Signals)

El sistema monitorea las siguientes señales para alertar sobre la necesidad de escalamiento o restricción:

- **Latencia de API (p95):** Si supera los 1,500ms de forma sostenida.
- **Cola de Misiones (Celery):** Si el tiempo de espera en cola supera los 30 segundos.
- **Tasa de Errores (HTTP 5xx):** Si supera el 0.5% del tráfico total.
- **Carga Forense:** Si el volumen de logs de seguridad supera los 10GB/mes (Indica ataque masivo o mala configuración).

---

## 3. PROTOCOLO DE ESCALAMIENTO

### 3.1 Escalamiento Vertical (Recursos)
- Priorizar el aumento de memoria para el caché de seguridad y el motor de IA.
- Incrementar el almacenamiento de la base de datos de auditoría (`audit_log`).

### 3.2 Escalamiento Horizontal (Federación)
- En lugar de un solo nodo masivo, SARITA favorece la **Federación de Nodos Soberanos**.
- Cada nuevo departamento o municipio debe contar con su propio Kernel de Gobernanza y base de datos aislada, conectándose vía API institucional.

---

## 4. CONDICIONES DE "NO ESCALAMIENTO" (Hard Stops)

Se prohíbe el escalamiento en los siguientes escenarios:

1. **Integridad Comprometida:** Si la cadena de hashes forenses presenta rupturas.
2. **Brecha de Seguridad Activa:** Mientras un vector de ataque no haya sido neutralizado.
3. **Inconsistencia Analítica:** Si el "Trust Index" sistémico cae por debajo del 90%.
4. **Falta de ROI:** Si el costo de operación del nodo supera la rentabilidad generada para los prestadores del mismo.

---
**"Crecer sin control es una patología. Escalar con soberanía es una estrategia."**
