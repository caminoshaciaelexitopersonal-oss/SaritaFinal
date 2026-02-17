# GUÍA DE AUDITORÍA LEGAL INTERNACIONAL (INTERNATIONAL AUDIT GUIDE)

**Versión:** 1.0 (Fase Z-LEGAL)
**Audiencia:** Organismos Acreditados, Estados Firmantes y Cortes Internacionales.
**Visión:** SARITA como infraestructura de auditoría técnica neutral y distribuida.

---

## 1. TAXONOMÍA DE AUDITORÍAS LEGALES
SARITA permite la ejecución de cuatro tipos de auditoría sobre la infraestructura de IA:

| Tipo | Propósito | Desencadenante |
| :--- | :--- | :--- |
| **Preventiva** | Validar que el Legal Kernel tiene cargadas las normas correctas. | Antes del despliegue de un nuevo nodo. |
| **Periódica** | Certificar el cumplimiento continuo de tratados internacionales. | Cronograma anual o semestral. |
| **Por Denuncia** | Investigar un presunto comportamiento abusivo o discriminatorio de la IA. | Petición de un Estado o ciudadano afectado. |
| **Post-Incidente** | Reconstruir los hechos tras un fallo técnico o ataque de seguridad. | Detección de brecha o activación de MDN. |

## 2. ACTORES AUTORIZADOS PARA AUDITAR
- **Organismos Acreditados:** Entes técnicos internacionales (ej. auditores ISO, comisiones de la ONU).
- **Estados Parte:** Autoridades nacionales con soberanía sobre un nodo específico o bajo un tratado de cooperación.
- **Cortes Internacionales:** Tribunales con jurisdicción sobre disputas transfronterizas.

## 3. PROCEDIMIENTO ESTÁNDAR DE AUDITORÍA (SOP-AUDIT)

### Paso 1: Solicitud de Mandato
El auditor debe presentar una credencial digital firmada que especifique el alcance de la auditoría (ej: "Auditoría de cumplimiento de privacidad en Nodo Gaitán").

### Paso 2: Validación de Acceso
El **Governance Kernel** verifica que el mandato sea legalmente válido según los tratados cargados. Si es válido, emite una llave temporal de consulta para el **Evidence Vault (EV)**.

### Paso 3: Extracción de Evidencia (Audit Bundle)
El sistema genera un paquete de datos que incluye:
1.  **Bitácora Forense:** Registros de eventos asociados al alcance.
2.  **Normas Aplicadas:** El código legal ejecutado por el LK en el periodo auditado.
3.  **Logs de Explicabilidad (XAI):** La justificación de las decisiones de la IA.

### Paso 4: Verificación de Integridad
El auditor utiliza herramientas externas para validar que los hashes encadenados del bundle coinciden con los anclajes de blockchain o sellos temporales.

## 4. ESTÁNDARES DE PRUEBA NEUTRAL
- **No Inferencia:** SARITA no emite juicios de valor. Los reportes se limitan a "Evento detectado", "Regla aplicada" y "Resultado lógico".
- **Privacidad por Diseño:** El proceso de auditoría debe usar técnicas de anonimización para proteger datos sensibles que no sean objeto de la investigación.

## 5. RESOLUCIÓN DE DISCORDANCIAS
Si el Nodo Auditado objeta el reporte, SARITA provee un entorno de **"Replicación Forense"** (Sandbox) donde el auditor puede re-ejecutar los mismos eventos sobre una copia aislada del Kernel para verificar si el resultado es reproducible.

---
**"La auditoría en SARITA no es una inspección de buena fe, es una validación matemática de la verdad legal."**
