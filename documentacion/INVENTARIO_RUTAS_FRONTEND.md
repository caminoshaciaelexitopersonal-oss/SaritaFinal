# INVENTARIO GLOBAL DE RUTAS FRONTEND - FASE F1

## 🏗️ Resumen de Vías
- **Vía 1:** Corporaciones / Gobierno (Admin Plataforma)
- **Vía 2:** Empresarios (Prestadores de Servicios Turísticos)
- **Vía 3:** Turista (Cara al Cliente Final)

---

## 🔹 Vía 1 — Corporaciones / Gobierno (Admin Plataforma)

| Ruta | Rol | Propósito | Estado |
| :--- | :--- | :--- | :--- |
| `/dashboard/admin_plataforma` | SuperAdmin | Dashboard Central de Gobernanza | 🟩 Profesional |
| `/dashboard/admin_plataforma/inteligencia` | SuperAdmin | Inteligencia de Negocio / SADI | 🟨 Parcial |
| `/dashboard/admin_plataforma/inteligencia-decisora` | SuperAdmin | Auditoría y Ejecución Soberana IA | 🟩 Profesional |
| `/dashboard/admin_plataforma/optimizacion` | SuperAdmin | Motor de Optimización del Ecosistema | 🟩 Profesional |
| `/dashboard/admin_plataforma/rentabilidad` | SuperAdmin | Análisis de Rentabilidad Nodal | 🟩 Profesional |
| `/dashboard/admin_plataforma/planes` | SuperAdmin | Gestión de Planes de Suscripción | 🟩 Profesional |
| `/dashboard/admin_plataforma/web-content` | SuperAdmin | Gobernanza de Contenido Digital | 🟩 Profesional |
| `/dashboard/admin_plataforma/gestion_comercial` | SuperAdmin | ERP Sistémico - Comercial | 🟩 Profesional |
| `/dashboard/admin_plataforma/gestion-operativa` | SuperAdmin | ERP Sistémico - Operativa | 🟩 Profesional |
| `/dashboard/admin_plataforma/gestion-contable` | SuperAdmin | ERP Sistémico - Contabilidad | 🟩 Profesional |
| `/dashboard/admin_plataforma/gestion-financiera` | SuperAdmin | ERP Sistémico - Finanzas | 🟩 Profesional |
| `/dashboard/admin_plataforma/gestion-archivistica` | SuperAdmin | ERP Sistémico - Archivo | 🟩 Profesional |
| `/dashboard/verificacion` | Admin | Centro de Verificación RNT/Documentos | 🟨 Parcial |

---

## 🔹 Vía 2 — Empresarios (Prestadores)

| Ruta | Rol | Propósito | Estado |
| :--- | :--- | :--- | :--- |
| `/dashboard/prestador/mi-negocio/gestion-comercial` | Prestador | Marketing, Funnels y Ventas | 🔴 Bloqueado (react-dnd) |
| `/dashboard/prestador/mi-negocio/gestion-contable` | Prestador | Contabilidad y Libros | 🟩 Profesional |
| `/dashboard/prestador/mi-negocio/gestion-operativa` | Prestador | Operación Especializada (Hoteles, etc) | 🟩 Profesional |
| `/dashboard/prestador/mi-negocio/gestion-financiera` | Prestador | Tesorería y Flujo de Caja | 🟩 Profesional |
| `/dashboard/prestador/mi-negocio/gestion-archivistica` | Prestador | Archivo Digital Legal | 🟩 Profesional |
| `/dashboard/prestador/mi-negocio/gestion-operativa/sst` | Prestador | Seguridad y Salud en el Trabajo | 🟩 Profesional |
| `/dashboard/prestador/mi-negocio/gestion-operativa/nomina` | Prestador | Gestión de Empleados | 🟩 Profesional |

---

## 🔹 Vía 3 — Turista (Cara al Cliente)

| Ruta | Rol | Propósito | Estado |
| :--- | :--- | :--- | :--- |
| `/` | Público | Landing Page Principal | 🟩 Profesional |
| `/descubre/atractivos` | Público | Catálogo de Sitios Turísticos | 🟩 Profesional |
| `/descubre/agenda-cultural` | Público | Calendario de Eventos | 🟩 Profesional |
| `/descubre/rutas-turisticas` | Público | Guías de Recorridos | 🟩 Profesional |
| `/directorio/prestadores` | Público | Directorio Comercial Geolocalizado | 🟩 Profesional |
| `/directorio/artesanos` | Público | Vitrina de Artesanías Locales | 🟩 Profesional |
| `/mi-viaje` | Turista | Planificador Personal de Viaje | 🟨 Parcial |

---

## 🚀 Embudo de Ventas (web-ventas-frontend)

| Ruta | Rol | Propósito | Estado |
| :--- | :--- | :--- | :--- |
| `/` | Prospecto | Chat Conversacional con SARITA | 🟩 Profesional |
| `/mofu` | Prospecto | Contenido de Consideración (CMS) | 🟨 Parcial |
| `/checkout` | Prospecto | Proceso de Pago y Afiliación | 🔴 Bloqueado (Imports) |
| `/decision` | Prospecto | Matriz de Decisión AI | 🟨 Parcial |
| `/sadi` | Prospecto | Demo de Orquestador de Voz | 🟨 Parcial |

---
**Nota:** El estado "Bloqueado" indica que la ruta no compila o tiene errores fatales de ejecución detectados en la Fase F0.
