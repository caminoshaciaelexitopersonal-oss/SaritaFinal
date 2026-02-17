# MODO DE DEFENSA NACIONAL (MDN) — PROTOCOLO DE AISLAMIENTO

**Versión:** 1.0 (Fase Z-DEF)
**Estado:** ESTRATÉGICO / OBLIGATORIO
**Activación:** SuperAdmin o Kernel Autónomo ante Amenaza Crítica.

---

## 1. QUÉ ES EL MODO DE DEFENSA NACIONAL
El MDN es el estado de "Resiliencia Extrema" de SARITA. Se activa cuando el sistema detecta un ataque coordinado, una brecha en la cadena de hashes forenses o por orden directa de la autoridad soberana ante una crisis nacional.

## 2. RESTRICCIONES OPERATIVAS (CONGELAMIENTO)
Tras la activación del MDN, SARITA impone las siguientes reglas de forma inmediata:

1.  **Estado de Solo Lectura:** Se bloquean todas las operaciones de escritura (POST, PUT, DELETE) para todos los usuarios, excepto la autoridad de emergencia.
2.  **IA Asesora Pasiva:** Todos los agentes SARITA (Funcionarios Digitales) pasan de un estado operativo (Nivel 2) a un estado puramente informativo (Nivel 0). Ninguna misión de optimización puede ser ejecutada.
3.  **Doble Soberanía:** Cualquier cambio en la configuración de seguridad requiere la aprobación de dos (2) firmas digitales de alto nivel.
4.  **Aislamiento de Módulos:** El sistema activa el "Sandboxing" de los módulos sospechosos, replicándolos para análisis forense mientras se cortan sus conexiones con el Núcleo.

## 3. SEÑALIZACIÓN EN INTERFACES (FRONTEND)
El frontend debe reflejar el estado MDN de forma explícita e inocultable:
*   **Banner Institucional Rojo:** Visible en todas las pantallas con el mensaje "MODO DE DEFENSA NACIONAL ACTIVO - SISTEMA CONGELADO POR SEGURIDAD".
*   **Identificador de Alerta:** Muestra el ID del vector de ataque detectado (ej: `AEIN-APT-04`).
*   **UI Degradada:** Se eliminan los botones de acción y formularios, dejando solo visualizaciones de datos históricos.

## 4. GOBERNANZA DE RECUPERACIÓN (RECOVERY)
El retorno al "Modo Normal" no es automático:
1.  **Certificación Forense:** El sistema debe certificar que la integridad del registro (Chained Hash) ha sido restaurada o que el vector ha sido neutralizado.
2.  **Mandato de Reapertura:** Solo una instrucción humana firmada puede desactivar el MDN.
3.  **Registro de Reinicio:** El evento de salida del MDN queda registrado con máxima prioridad en la bitácora estatal.

---
**"En Modo Defensa, el sistema prefiere morir temporalmente antes que ser capturado permanentemente."**
