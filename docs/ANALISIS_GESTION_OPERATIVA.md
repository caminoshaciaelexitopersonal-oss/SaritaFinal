# Informe de Análisis de Brechas: Módulo de Gestión Operativa

**Fecha de Análisis:** 2025-11-09
**Auditor:** Jules
**Sistema de Referencia:** `tourism_core`

## 1. Resumen Ejecutivo

El módulo de **Gestión Operativa** en el proyecto Sarita existe como una estructura de directorios y modelos de datos muy básicos, pero carece de casi toda la funcionalidad, arquitectura y robustez presentes en el código de referencia `tourism_core`. La brecha entre la implementación actual y el objetivo es del **95%**.

Sarita tiene placeholders para los módulos especializados (Hotel, Restaurante, etc.), pero estos están vacíos. Los módulos genéricos (Productos, Inventario) son implementaciones simplistas. Las características más críticas y fundamentales del sistema de referencia, como la **arquitectura multi-inquilino a prueba de fallos**, el **modelo de datos polimórfico**, los **servicios de lógica de negocio desacoplados** y los **componentes de UI operativa en tiempo real**, están completamente ausentes.

Este documento detalla las brechas identificadas y servirá como base para un plan de implementación exhaustivo.

---

## 2. Brechas Arquitectónicas Fundamentales (Backend)

Estas son las brechas más críticas que afectan a todo el módulo.

*   **Arquitectura Multi-Inquilino:**
    *   **Sarita:** No existe. Las consultas a la base de datos no están aisladas por proveedor, lo que representa una **vulnerabilidad de seguridad crítica** donde un proveedor podría acceder a los datos de otro.
    *   **Referencia (`tourism_core`):** Implementa un sistema robusto con un `TenantMiddleware` que identifica al proveedor en cada petición y un `TenantManager` que filtra automáticamente **todas** las consultas a la base de datos. Principio de "fallo seguro".
*   **Modelos de Datos Base:**
    *   **Sarita:** No tiene modelos base. Cada modelo repite campos como `id`, `created_at`, etc.
    *   **Referencia:** Utiliza un `BaseModel` abstracto para campos de auditoría comunes y un `TenantAwareModel` que es la piedra angular de la arquitectura multi-inquilino.
*   **Lógica de Negocio Desacoplada:**
    *   **Sarita:** La lógica tiende a estar dentro de las vistas de la API.
    *   **Referencia:** Abstrae toda la lógica de negocio compleja en un `services.py`, permitiendo que sea reutilizable, comprobable y atómica (con transacciones).

---

## 3. Análisis de Brechas por Módulo

### 3.1. Módulos Especializados (Hotel, Restaurante, Guía, Transporte, Agencia, Artesano)

*   **Sarita:**
    *   **Backend:** Los archivos `models.py` para todos estos módulos están **completamente vacíos**. No existe ninguna lógica de negocio.
    *   **Frontend:** Las páginas correspondientes (ej. `.../hoteles/page.tsx`) solo contienen un placeholder `<h1>Módulo en Desarrollo</h1>`.
*   **Referencia (`tourism_core`):**
    *   **Backend:** Define modelos de datos ricos y especializados para cada tipo de negocio (ej. `Room`, `RoomType`, `Amenity` para Hotel; `RestaurantTable`, `KitchenStation` para Restaurante, etc.). Implementa APIs y servicios específicos para operaciones como check-in, asignación de guías, etc.
    *   **Frontend:** Proporciona un conjunto completo de componentes de interfaz de usuario operativa en tiempo real (ej. `HousekeepingBoard`, `FloorPlan`, `KDSBoard`, `AssignmentScheduler`).
*   **Brecha:** **Total (100%).** Se debe implementar toda la funcionalidad desde cero.

### 3.2. Módulos Genéricos

*   **Producto/Servicio:**
    *   **Sarita:** Tiene un modelo `ProductoServicio` monolítico y simple.
    *   **Referencia:** Utiliza un modelo `Product` polimórfico y central, que se especializa con otros modelos (`RoomType`, `MenuItemDetail`) y se conecta a sistemas de configuración como `PricingRule`, `Tax`, y `CancellationPolicy`.
    *   **Brecha:** Muy alta. El modelo de Sarita debe ser reemplazado por la arquitectura polimórfica y extensible de la referencia.
*   **Inventario:**
    *   **Sarita:** Un único modelo `Inventario` muy simple.
    *   **Referencia:** El concepto de inventario está integrado en el modelo `Product` (`stock`) y en un sistema de recetas (`RecipeBuilder`) que descuenta consumibles automáticamente.
    *   **Brecha:** Alta. La lógica de inventario de Sarita es rudimentaria y no está conectada a la operación real.
*   **Personal y Roles (`TeamMember`, `StaffRole`):**
    *   **Sarita:** No implementado.
    *   **Referencia:** Sistema completo para gestionar miembros del equipo, asignar roles jerárquicos y permisos granulares.
    *   **Brecha:** Total (100%).
*   **Reservas y Órdenes (`Reservation`, `Order`):**
    *   **Sarita:** Existe un módulo de `reservas` básico.
    *   **Referencia:** Modelos robustos con flujos de estado, manejo de pagos, y lógica polimórfica para gestionar reservas de hotel, tours o pedidos de productos.
    *   **Brecha:** Alta. El sistema de reservas de Sarita necesita ser expandido para soportar los diferentes flujos de negocio.

---

## 4. Brechas de Funcionalidad Transversal

*   **Tareas Asíncronas (Celery):**
    *   **Sarita:** No hay uso de Celery en el módulo operativo.
    *   **Referencia:** Utiliza Celery extensivamente para tareas de mantenimiento (alertas de vencimiento), generación de reportes (PDFs, CSVs) y notificaciones.
*   **Tiempo Real (WebSockets con Channels):**
    *   **Sarita:** No implementado.
    *   **Referencia:** Utiliza WebSockets para paneles operativos en vivo como el `KDSBoard` y el `HousekeepingBoard`, donde las actualizaciones se reflejan instantáneamente.
*   **Pruebas (Pytest):**
    *   **Sarita:** No existen pruebas para el módulo operativo.
    *   **Referencia:** Cuenta con una suite de pruebas exhaustiva que blinda la arquitectura multi-inquilino y valida la lógica de negocio en los servicios.

## 5. Conclusión del Análisis

El módulo de **Gestión Operativa** de Sarita es actualmente un cascarón. Para alcanzar el nivel del código de referencia, se requiere una reimplementación casi total, empezando por la capa de seguridad multi-inquilino y continuando con cada módulo especializado. El trabajo a realizar es sustancial pero el código de referencia proporciona un plano claro y de alta calidad a seguir.
