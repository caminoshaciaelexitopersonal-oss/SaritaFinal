# Plan de Correcciones - Fase 5

Este documento clasifica los hallazgos de la Fase 4 y define el plan de acción para la Fase 5, enfocado en corregir errores y consolidar la funcionalidad sin introducir nuevas features.

## 1. Clasificación de Hallazgos

| ID | Hallazgo | Módulo | Severidad | Justificación |
| :--- | :--- | :--- | :--- | :--- |
| **BUG-01** | Enlaces del menú llevan a 404. | `gestion-contable`, `productos-servicios` | **CRÍTICO (P0)** | Flujo de usuario roto. La UI promete una funcionalidad que resulta en un error. |
| **BUG-02** | Página "Editar Cliente" carga la lista completa. | `gestion-operativa` (Clientes) | **MEDIO (P2)** | Ineficiencia de rendimiento y mala práctica de API, pero no rompe la funcionalidad. |
| **DEUDA-01**| Lógica de cálculo de total en el frontend. | `gestion-comercial` | **BAJO (P3)** | Anti-patrón, pero no causa un bug visible. La corrección implicaría refactorizar, lo cual está fuera de alcance. |
| **DEUDA-02**| Falta de estrategia de expiración de tokens. | `Autenticación` | **BAJO (P3)** | Es un riesgo de seguridad a largo plazo, pero no un bug funcional. Su corrección requiere una nueva feature (refresh tokens). |
| **DEUDA-03**| Warnings de `key` en listas y paginación no ordenada. | Múltiples | **BAJO (P3)** | Buenas prácticas, pero no afectan el comportamiento funcional del sistema. |

## 2. Plan de Acción para Fase 5

Basado en la clasificación y las reglas de la fase, el plan es el siguiente:

1.  **Corregir BUG-01 (P0):**
    *   **Acción:** Crear páginas de marcador de posición (`placeholder`) para las rutas `/gestion-contable` y `/gestion-operativa/genericos/productos-servicios`.
    *   **Resultado Esperado:** Eliminar los errores 404 y proporcionar feedback coherente al usuario, cerrando el flujo roto.

2.  **Corregir BUG-02 (P2):**
    *   **Acción:** Implementar un endpoint `retrieve` en el `ClienteViewSet` del backend y una función `getClienteById` en el `useMiNegocioApi` hook del frontend. Refactorizar la página de edición para usar esta nueva función.
    *   **Resultado Esperado:** Mejorar el rendimiento y la eficiencia de la API sin cambiar la funcionalidad visible para el usuario.

3.  **Acciones Excluidas (Fuera de Alcance):**
    *   **DEUDA-01, DEUDA-02, DEUDA-03 (P3):** Estos ítems no se corregirán en esta fase. Se clasifican como deuda técnica que requiere refactorización o nuevas funcionalidades, lo cual está explícitamente prohibido por las reglas de la Fase 5. Serán documentados en el informe final como "trabajo pendiente".
