# ESTÁNDAR DE EVIDENCIA TÉCNICA NEUTRAL (NEUTRAL EVIDENCE STANDARD)

**Versión:** 1.0 (Fase Z-WAR-SAFE)
**Estado:** OBLIGATORIO PARA INVESTIGACIONES
**Principio:** SARITA no emite juicios; provee hechos inalterables.

---

## 1. EL AUDIT BUNDLE DE CONFLICTO

En caso de un incidente de nivel B3 o B4, SARITA generará automáticamente un paquete de evidencia neutral diseñado para tribunales u organismos internacionales. Este estándar prohíbe explícitamente el uso de lenguaje incriminatorio o interpretativo.

### 1.1 Estructura del Bundle
1.  **Línea de Tiempo Técnica (TTL):** Registro de milisegundos que precede al incidente, detallando carga de CPU, latencia de red y cambios de estado de memoria.
2.  **Logs de Intención (Intent Registry):** Copia exacta de las instrucciones de negocio recibidas y la validación del Kernel.
3.  **Cadena XAI Inalterada:** La justificación técnica original generada por los agentes, sin procesar.
4.  **Prueba de Control Humano (PHC):** Registro de las últimas interacciones humanas validadas (quién confirmó qué y cuándo).
5.  **Hash de Integridad Global:** Firma del nodo que acredita que el bundle no fue modificado tras la captura.

## 2. LA REGLA DE NO-CONCLUSIÓN (NON-JUDGMENTAL RULE)

Queda prohibido que el reporte de SARITA incluya:
- ❌ **Atribución de Culpabilidad:** Ej. "El Nodo X inició el ataque". (Debe decir: "Se detectó tráfico desde IP [X] hacia Endpoint [Y]").
- ❌ **Calificación de Intención:** Ej. "Acción maliciosa". (Debe decir: "Evento que viola la Regla de Seguridad ID-44").
- ❌ **Recomendaciones de Sanción:** El sistema no sugiere castigos, solo reporta desviaciones objetivas de tratados.

## 3. SELLADO CRIPTOGRÁFICO Y CADENA DE CUSTODIA
Para asegurar la validez jurídica de la evidencia:
- **Anclaje Blockchain:** El hash del bundle debe anclarse en una red distribuida neutral en el momento de la captura.
- **Doble Firma:** El bundle solo es admisible si cuenta con la firma del Nodo Nacional emisor y el sello de verificación del Supranational Kernel (si aplica).

## 4. SOPORTE PROBATORIO PARA INVESTIGACIONES
SARITA permite a los investigadores internacionales:
- **Simulación Post-Hoc:** Re-ejecutar los datos del bundle en un entorno aislado para verificar que el sistema se comportó según sus reglas programadas.
- **Verificación de Sesgos:** Analizar si el Legal Kernel aplicó las mismas restricciones a todas las partes en conflicto.

---
**"La evidencia neutral es el único lenguaje que los Estados en conflicto pueden compartir sin desconfianza."**
