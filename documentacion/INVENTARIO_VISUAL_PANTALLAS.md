# INVENTARIO VISUAL DE PANTALLAS - FASE F1

## 🏁 Resumen de Madurez Visual
- 🟩 **Profesional:** Diseño Enterprise, componentes UI pulidos, layouts coherentes.
- 🟨 **Parcial:** Funcional pero con elementos visuales básicos o incompletos.
- 🟥 **Prototipo:** Solo estructura básica, mucho texto de relleno o placeholders.

---

## 🏛️ Vía 1 — Admin Plataforma (Gobernanza)

### 1. Dashboard Central de Soberanía (`/dashboard/admin_plataforma`)
- **Layout:** Sidebar lateral, Header con estatus del Kernel, Grid de KPIs.
- **Componentes:**
    - Cards de KPIs (Ingresos, Prestadores, ROI, Confianza IA).
    - Monitor de Salud (Barras de progreso para ROI y Eficiencia).
    - Alertas de Gobernanza (Feed lateral con severidad).
- **Madurez:** 🟩 Profesional.

### 2. Inteligencia Decisora (`/dashboard/admin_plataforma/inteligencia-decisora`)
- **Layout:** Tabla central de recomendaciones.
- **Componentes:**
    - Botón "Ejecutar Auditoría IA" (Brain icon).
    - Tabla de propuestas con badges de riesgo y botones de acción (Aprobar/Ejecutar).
- **Madurez:** 🟩 Profesional.

### 3. Gobernanza Web (`/dashboard/admin_plataforma/web-content`)
- **Layout:** Catálogo de páginas y assets multimedia.
- **Componentes:**
    - Tabla de páginas (Título, Slug, Estatus Publicación).
    - Card de Optimización SEO.
    - Grid de Assets Multimedia (Dropzone placeholder).
- **Madurez:** 🟩 Profesional.

---

## 💼 Vía 2 — Prestador (ERP Mi Negocio)

### 1. Tesorería y Finanzas (`/dashboard/prestador/mi-negocio/gestion-financiera`)
- **Layout:** Dashboard financiero con grid de KPIs y tablas de movimientos.
- **Componentes:**
    - Hero Card (Saldo Total Consolidado).
    - Ratios Financieros (Liquidez, Margen, etc).
    - Listado de Cuentas Bancarias y Movimientos de Caja.
- **Madurez:** 🟩 Profesional.

### 2. Gestión Comercial (Dashboard) (`/dashboard/prestador/mi-negocio/gestion-comercial`)
- **Layout:** Centro de mando con navegación por tabs.
- **Componentes:**
    - KPIs comerciales (Ingresos, Leads, Conversión).
    - Cards de acceso rápido a Arquitecto de Embudos y Marketing.
- **Madurez:** 🟩 Profesional (El layout), pero bloqueado funcionalmente.

### 3. Gestión Archivística (`/dashboard/prestador/mi-negocio/gestion-archivistica`)
- **Layout:** Tabla de documentos con visualización de certificados.
- **Componentes:**
    - Data table con búsqueda y filtros.
    - Diálogo de carga de documentos.
- **Madurez:** 🟩 Profesional.

---

## 🌴 Vía 3 — Turista (Portal Público)

### 1. Catálogo de Atractivos (`/descubre/atractivos`)
- **Layout:** Grid de tarjetas con filtros superiores.
- **Componentes:**
    - Filtros por categoría (Cultural, Urbano, Natural).
    - Cards con imagen, badge de categoría, descripción corta y botón "Ver más".
- **Madurez:** 🟩 Profesional.

### 2. Agenda Cultural (`/descubre/agenda-cultural`)
- **Layout:** Calendario reactivo de pantalla completa.
- **Componentes:**
    - `react-big-calendar` integrado.
    - Tooltips de eventos.
- **Madurez:** 🟩 Profesional.

---

## 🚀 Embudo de Ventas (web-ventas-frontend)

### 1. Landing Conversacional (`/`)
- **Layout:** Chat interactivo centrado.
- **Componentes:**
    - Header con estatus del motor SADI.
    - Burbujas de chat con micro-animaciones.
    - Control center con botón de voz (Mic).
- **Madurez:** 🟩 Profesional.

### 2. Checkout (`/checkout`)
- **Layout:** Carrito de compras con resumen lateral.
- **Componentes:**
    - Listado de planes seleccionados.
    - Botón de "Proceder al Pago".
- **Madurez:** 🟨 Parcial (Faltan validaciones visuales de pasarela real).
