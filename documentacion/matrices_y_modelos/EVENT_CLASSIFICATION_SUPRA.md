# CLASIFICACIÓN DE EVENTOS SUPRANACIONALES (EVENT CLASSIFICATION SUPRA)

**Versión:** 1.0 (Fase Z-SUPRA)
**Estado:** OFICIAL
**Propósito:** Estandarizar la comunicación de hitos entre Estados y el Nodo Supranacional.

---

## 1. JERARQUÍA DE EVENTOS SUPRANACIONALES

SARITA categoriza toda interacción interestatal en cinco niveles de significancia institucional:

| Tipo de Evento | Descripción | Ejemplo Típico | Acción del Sistema |
| :--- | :--- | :--- | :--- |
| **Evento Informativo** | Reporte rutinario de datos estadísticos. | Reporte mensual de flujo turístico regional. | Registro en bitácora histórica y actualización de KPIs. |
| **Evento de Compromiso** | Hito que marca la asunción de una nueva obligación. | Firma digital de un anexo técnico al tratado. | Emisión de Certificado de Compromiso firmado por el SGK. |
| **Evento de Riesgo** | Detección de una desviación técnica objetiva. | Los niveles de emisión superan el umbral del tratado por 3 días. | Generación de Alerta Institucional a todos los firmantes. |
| **Evento de Controversia** | Discrepancia formal entre Estados sobre un dato. | El País A objeta la veracidad de los eventos reportados por el País B. | Bloqueo temporal del KPI afectado y escalamiento a mediación. |
| **Evento de Retiro** | Acción soberana de salida de un acuerdo. | Notificación formal de cese de participación en el bloque. | Revocación de credenciales y cierre de canales NC. |

## 2. ATRIBUTOS OBLIGATORIOS DEL EVENTO
Para ser procesado por el Supranational Kernel, cada evento debe portar:
1.  **Origen Certificado:** Firma digital del Nodo Nacional emisor.
2.  **Referencia a Tratado:** ID del TID que autoriza el flujo.
3.  **Hash de Integridad:** Para asegurar que el evento no fue alterado en tránsito.
4.  **Marca de Tiempo (NTP):** Sincronizada globalmente.

## 3. PROCESAMIENTO Y VISIBILIDAD
*   **Logs Diplomáticos:** Todos los eventos de nivel "Riesgo" o superior se registran en una bitácora de alta disponibilidad para auditoría cruzada.
*   **Consistencia Regional:** El sistema utiliza estos eventos para generar el "Mapa de Salud de Acuerdos", permitiendo a los organismos multilaterales visualizar el cumplimiento global en tiempo real.

---
**"La claridad en los eventos es la base de la justicia técnica internacional."**
