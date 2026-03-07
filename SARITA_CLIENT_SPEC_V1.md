# SARITA CLIENT SPEC v1: Especificación de Interfaz Unificada

**Versión:** 1.0.0
**Estado:** Definido
**Objetivo:** Garantizar la UX Parity (Paridad de Experiencia) entre Web, Mobile y Desktop.

---

## 1. LAYOUT Y NAVEGACIÓN CONCEPTUAL

| Concepto | Web (Dashboard) | Mobile (App) | Desktop (Electron) |
| :--- | :--- | :--- | :--- |
| **Navegación Principal** | Barra Lateral (Sidebar) Izquierda | Barra Inferior (Bottom Tabs) | Barra Lateral (Icon-only) |
| **Punto de Entrada** | Dashboard (Resumen) | Inicio (Vista Rápida) | Control Tower (Métricas) |
| **Búsqueda/Exploración** | Barra Superior | Pestaña "Explorar" | Panel Lateral de Filtros |
| **Gestión de Sesión** | Menú Perfil (Top Right) | Pestaña "Perfil" | Esquina Inferior Izquierda |

---

## 2. RUTAS Y FLUJOS EQUIVALENTES

| Ruta Concepto | Web Path | Mobile Tab | Desktop View |
| :--- | :--- | :--- | :--- |
| **Inicio / Estado** | `/dashboard` | `Home` | `Dashboard` |
| **Explorar Servicios** | `/descubre` | `Explore` | `ServiceMap` |
| **Reservas / Actividad**| `/reservas` | `Bookings` | `ActivityLog` |
| **Mensajería SADI** | `/mensajes` | `Messages` | `ChatCenter` |
| **Configuración** | `/perfil` | `Profile` | `Settings` |

---

## 3. COMPONENTES DEL DESIGN SYSTEM (Propuesta)

Para mantener la consistencia, todos los clientes deben implementar:
*   **SaritaButton:** Variantes (Primary, Secondary, Outline, Ghost).
*   **SaritaCard:** Contenedor estándar con elevación suave para servicios turísticos.
*   **SaritaInput:** Campos de texto con validación centralizada en el SDK.
*   **SaritaBadge:** Etiquetas de estado (Pendiente, Confirmado, Cancelado) con colores unificados.

---

## 4. FLUJO DE AUTENTICACIÓN UNIFICADO

1.  **Login:** Todos los clientes apuntan a `/api/v1/token/`.
2.  **Persistencia:**
    *   **Web:** localStorage / Cookies.
    *   **Mobile:** `expo-secure-store`.
    *   **Desktop:** SafeStorage (Electron).
3.  **Refresco:** El SDK maneja el `refresh_token` de forma transparente antes de la expiración.

---

## 5. REGLAS DE ORO PARA EL DESARROLLO

1.  **Paginación:** Siempre usar `PaginationEngine`. No se permiten offsets locales.
2.  **Modelos:** Prohibido definir interfaces `Tour` o `User` fuera del `@sarita/shared-sdk`.
3.  **Errores:** El manejo de errores 401 y 500 es responsabilidad del SDK; el cliente solo reacciona a la notificación visual.

---
**Aprobado por:** Arquitectura SARITA
**Fecha:** Marzo 2026
