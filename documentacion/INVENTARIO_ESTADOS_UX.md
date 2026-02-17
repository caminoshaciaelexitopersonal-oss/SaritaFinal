# INVENTARIO DE ESTADOS UX - FASE F1

## 🚦 Resumen de Cobertura UX
- **Loading:** Bajo nivel de implementación (falta de skeletons/spinners consistentes).
- **Error:** Casi inexistente (depende de toasts genéricos).
- **Vacío:** Implementado parcialmente en algunos módulos core.

---

## 🏛️ Vía 1 — Admin Plataforma

| Estado | Calidad | Observación |
| :--- | :--- | :--- |
| **Loading** | 🔴 Pobre | Las tablas de gobernanza quedan en blanco mientras cargan. |
| **Error** | 🟨 Aceptable | Utiliza `react-hot-toast` para reportar fallos de API. |
| **Vacío** | 🟩 Buena | Mensajes descriptivos cuando no hay propuestas o auditorías. |
| **Timeout** | 🟩 Buena | Implementado globalmente en `DashboardLayout` (8s). |

---

## 💼 Vía 2 — Prestador (ERP)

| Estado | Calidad | Observación |
| :--- | :--- | :--- |
| **Loading** | 🔴 Pobre | El ERP financiero y operativo no muestra indicadores de carga. |
| **Error** | 🔴 Crítica | Fallos de red pueden dejar la pantalla sin feedback al usuario. |
| **Vacío** | 🟨 Aceptable | Implementado en Archivística con iconografía; ausente en Comercial. |
| **Sin Permisos** | 🟨 Aceptable | Redirige al login o muestra mensaje genérico de acceso denegado. |

---

## 🌴 Vía 3 — Turista (Portal)

| Estado | Calidad | Observación |
| :--- | :--- | :--- |
| **Loading** | 🟨 Aceptable | El directorio usa skeletons básicos para las cards. |
| **Error** | 🟨 Aceptable | Mensajes de "Vuelva a intentar más tarde" en Atractivos. |
| **Vacío** | 🟩 Buena | Mensajes amigables de "No hay resultados para tu búsqueda". |

---

## 📋 Diagnóstico de Experiencia de Usuario
1. **Falta de Continuidad Visual:** La carga de datos causa "saltos" en el layout debido a la falta de skeletons dimensionados.
2. **Fragilidad en Errores:** No existen pantallas de error (Error Boundaries) personalizadas para fallos de dominio específicos.
3. **Dependencia de Red:** El sistema se comporta de forma impredecible en modo offline o con latencia alta, exceptuando el timeout global.
