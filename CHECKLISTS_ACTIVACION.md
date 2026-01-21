# Checklists de Activación - Fase 11

Este documento contiene los checklists obligatorios que deben ser completados por el Administrador antes de activar cualquier nueva funcionalidad de cara al mercado.

---

## 1. Checklist Técnico de Pre-Activación

| Punto de Verificación | Estado (✅/❌) | Observaciones |
| :--- | :--- | :--- |
| **Rendimiento** | | |
| El tiempo de carga de la página es < 3s | | |
| Las APIs relacionadas tienen latencia estable | | |
| El caché está activado para los datos estáticos | | |
| No se han introducido nuevas regresiones N+1 | | |
| **Seguridad** | | |
| El endpoint está protegido por autenticación y autorización | | |
| Los permisos son los mínimos necesarios para la operación | | |
| No hay exposición de datos sensibles | | |
| **Gobernabilidad** | | |
| La funcionalidad puede ser activada/desactivada por el Admin | | |
| Los cambios son reversibles sin necesidad de despliegue | | |
| **Estabilidad** | | |
| Las pruebas de regresión pasan para el módulo afectado | | |
| El manejo de errores es robusto | | |

---

## 2. Checklist Legal de Pre-Activación

| Punto de Verificación | Estado (✅/❌) | Observaciones |
| :--- | :--- | :--- |
| **Privacidad de Datos** | | |
| El manejo de datos cumple con la política de privacidad | | |
| Si se capturan nuevos datos, se informa al usuario | | |
| **Pagos (si aplica)** | | |
| Los términos y condiciones del servicio son claros | | |
| Se cumple con la normativa local sobre transacciones | | |
| **Contenido** | | |
| El contenido no infringe derechos de autor | | |

---

## 3. Checklist de UX (Experiencia de Usuario) de Pre-Activación

| Punto de Verificación | Estado (✅/❌) | Observaciones |
| :--- | :--- | :--- |
| **Claridad** | | |
| La propuesta de valor es clara e inequívoca | | |
| El texto (copy) es fácil de entender y no tiene errores | | |
| **Funcionalidad** | | |
| Todos los CTAs (Llamadas a la Acción) son funcionales | | |
| Los enlaces no están rotos | | |
| El flujo del usuario es intuitivo | | |
| **Diseño y Responsividad** | | |
| La experiencia en dispositivos móviles es óptima | | |
| Las imágenes y videos cargan correctamente | | |
| El diseño es consistente con el resto de la plataforma | | |
