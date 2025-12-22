# QA Funcional por Ruta: Mi Negocio (Fase 4)

Este documento registra los hallazgos del QA manual realizado en cada una de las rutas principales del ERP "Mi Negocio".

## 1. /gestion-comercial

- **Estado General:** ✅ **Funcional pero Incompleto**
- **Hallazgos:**
    - **Listar Facturas:** Funciona correctamente. La tabla muestra los datos de la API.
    - **Crear Factura:** El formulario es funcional y crea la factura en el backend.
    - **Ver Detalle / Editar:** ❕ **NO IMPLEMENTADO.** No existen botones ni enlaces en la UI para estas acciones.

## 2. /gestion-operativa

- **Estado General:** 🟡 **Parcialmente Implementado**
- **Hallazgos:**
    - **Clientes:** Funcionalidad CRUD completa y robusta.
    - **Productos/Servicios:** 🔴 **NO IMPLEMENTADO.** El enlace en el menú lleva a una página 404.
    - **Mi Perfil:** Funcional. El formulario carga y actualiza los datos del perfil.
    - **Otras secciones (Reservas, Galería, etc.):** 🔴 **NO IMPLEMENTADO.** Los enlaces llevan a páginas 404.

## 3. /gestion-contable

- **Estado General:** 🔴 **NO IMPLEMENTADO**
- **Hallazgos:**
    - El enlace del menú lleva a una página 404. No existe ninguna interfaz de usuario para este módulo.

## 4. /gestion-financiera

- **Estado General:** ✅ **Funcional pero Incompleto**
- **Hallazgos:**
    - **Cuentas Bancarias:** Funcionalidad CRUD completa a través de un modal.
    - **Transacciones:** ❕ **NO IMPLEMENTADO.** La página de detalle para ver transacciones por cuenta no está completamente funcional o no existe.

## 5. /gestion-archivistica

- **Estado General:** ✅ **Funcional**
- **Hallazgos:**
    - La tabla de documentos se carga correctamente.
    - El modal para subir nuevos documentos está presente y es funcional.
