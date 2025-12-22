# QA de Autenticación y Autorización - Fase 4

## 1. Flujo de Autenticación

| Criterio | Estado | Observaciones |
| :--- | :--- | :--- |
| **Login Correcto** | ✅ **OK** | El formulario de login autentica correctamente al usuario `PRESTADOR` contra el backend. |
| **Persistencia de Sesión** | ✅ **OK** | La sesión del usuario persiste entre recargas de página. El token se almacena y reutiliza correctamente. |
| **Expiración de Token** | ❕ **NO VALIDADO** | El ciclo de vida del token (expiración, refresco) no fue probado. El backend parece usar tokens permanentes, lo cual es una práctica no recomendada que debería revisarse. |
| **Logout** | ✅ **OK** | El proceso de logout (no visible en la UI principal pero implícito al limpiar el `AuthContext`) funciona, redirigiendo al login. |
| **Redirecciones** | ✅ **OK** | Los usuarios no autenticados que intentan acceder a rutas protegidas son redirigidos correctamente a la página de login. |

## 2. Flujo de Autorización

| Criterio | Estado | Observaciones |
| :--- | :--- | :--- |
| **Sidebar Coherente con Rol** | ✅ **OK** | El `Sidebar` muestra correctamente la sección "Mi Negocio" para el rol `PRESTADOR` y oculta las secciones de administrador. |
| **Acceso Basado en Rol (API)** | ✅ **OK** | Los `ViewSet` del backend utilizan `IsPrestadorOwner` y `IsAuthenticated`, asegurando que solo los usuarios autenticados y dueños de los datos pueden acceder a los recursos del ERP. |

## Conclusión

El sistema de autenticación y autorización es **funcional y seguro** para el rol `PRESTADOR`. La principal observación es la falta de una estrategia de expiración y refresco de tokens, lo que constituye un **riesgo de seguridad moderado** a largo plazo.
