# MANUAL DEL AUDITOR EXTERNO

**Sistema:** SARITA
**Perfil:** Auditor / Ente Regulatorio

## 1. MODO AUDITOR
Active el **Modo Auditor** en el Centro GRC para:
- Visualizar el sistema en **Solo Lectura**.
- Ver datos sensibles enmascarados.
- Forzar el rastro de auditoría en cada clic.

## 2. VERIFICACIÓN DE INTEGRIDAD
Para certificar que los datos no han sido manipulados:
- Verifique el **Integrity Hash** en los logs de gobernanza.
- El sistema utiliza encadenamiento de hashes (SHA-256) donde cada log depende del anterior.
- Cualquier modificación manual en la base de datos romperá la cadena y será detectada inmediatamente.

## 3. AUDITORÍA DE IA
- Revise el **Registro de Autonomía**.
- Cada acción de los agentes SARITA tiene una explicación XAI asociada.
- Verifique que se hayan respetado los límites diarios y financieros autorizados.

---
**Transparencia Radical y No-Repudio.**
