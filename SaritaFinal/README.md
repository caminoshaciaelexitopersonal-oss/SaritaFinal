# Proyecto SaritaUnificado - Documentación Funcional

## 1. Introducción

**SaritaUnificado** es una plataforma turística integral diseñada para conectar a turistas, prestadores de servicios y entidades administrativas en un ecosistema digital unificado. El sistema está construido como una "plataforma de triple vía", sirviendo a:

1.  **Turistas:** Ofreciendo un portal completo para descubrir, planificar y reservar experiencias turísticas.
2.  **Prestadores de Servicios:** Proporcionando un panel de administración privado y potente para gestionar su negocio.
3.  **Entidades Administrativas:** Otorgando herramientas para la supervisión, validación y gestión del ecosistema turístico.

Este documento detalla todas las funcionalidades del sistema desde la perspectiva de cada rol de usuario.

---

## 2. Arquitectura del Sistema

*   **Backend:** API RESTful desarrollada con **Django** y **Django REST Framework**.
*   **Frontend:** Aplicación de Página Única (SPA) desarrollada con **Next.js 15**, **React 19** y **TypeScript**.
*   **Base de Datos:** SQLite para desarrollo, con capacidad para PostgreSQL en producción.

---

## 3. Guía de Funcionalidades por Rol

### 👤 Para el Turista (Sitio Público)

El turista interactúa con el portal público, que está diseñado para ser intuitivo y rico en información.

| Funcionalidad | Descripción |
| :--- | :--- |
| **Directorio de Servicios** | Un buscador unificado que permite a los turistas encontrar y filtrar prestadores por categoría (Hoteles, Restaurantes, Guías, etc.), ubicación o nombre. |
| **Perfil del Prestador** | Cada prestador tiene una página de detalle pública donde el turista puede ver toda su información: descripción, datos de contacto, redes sociales, y ubicación en un mapa. |
| **Galería Multimedia** | Los turistas pueden ver una galería de fotos de alta calidad subidas por el prestador para conocer mejor sus instalaciones, productos o servicios. |
| **Visualización de Servicios** | La página de detalle muestra los productos, paquetes o rutas turísticas que ofrece el prestador, con sus descripciones y precios. |
| **Calendario de Disponibilidad** | Se integra un calendario interactivo (RAT) que muestra la disponibilidad en tiempo real de los servicios del prestador (ej. habitaciones de hotel, tours de un guía). |
| **Sistema de Reservas** | Los turistas pueden seleccionar una fecha disponible en el calendario y realizar una solicitud de reserva directamente desde la página del prestador. |
| **Sistema de Valoraciones** | Los turistas pueden dejar reseñas y calificaciones (de 1 a 5 estrellas) en el perfil de los prestadores con los que han interactuado. |
| **Registro y Mi Viaje** | Los usuarios pueden registrarse como "Turistas" para acceder a funcionalidades personalizadas, como guardar prestadores o atractivos favoritos en una sección de "Mi Viaje". |

### 🏢 Para el Prestador de Servicios (Panel de Administración Privado)

Tras iniciar sesión, el prestador accede a un panel de control privado (`/dashboard`) con un menú de herramientas adaptado a su tipo de negocio.

#### Módulos Genéricos (Disponibles para todos los prestadores)

| Módulo | Funcionalidad Detallada | Beneficio para el Empresario |
| :--- | :--- | :--- |
| **Inicio** | Página de bienvenida al panel. | Acceso rápido y centralizado. |
| **Mi Perfil** | Formulario para editar toda la información pública del negocio: nombre, descripción, teléfonos, redes sociales, dirección y ubicación en el mapa (lat/lon). | Control total sobre su imagen de marca y datos de contacto. |
| **Productos/Servicios** | CRUD completo para crear, editar y eliminar los productos o servicios que ofrece, con nombre, descripción y precio. | Gestión de su catálogo de ofertas de forma sencilla. |
| **Clientes (CRM)** | CRUD completo para gestionar una base de datos de clientes con nombre, email, teléfono y notas internas. | Fidelización y seguimiento de clientes recurrentes. |
| **Galería** | Interfaz para subir, visualizar y eliminar imágenes que se mostrarán en la galería de su perfil público. | Enriquecer su perfil público para atraer más clientes. |
| **Documentos** | Módulo para subir documentos oficiales (RNT, Cámara de Comercio, etc.) y ver su estado de verificación (Pendiente, Aprobado, Rechazado) por parte de la administración. | Centralizar la gestión de su documentación legal y cumplir con los requisitos. |
| **Valoraciones** | Visualización de las reseñas y comentarios dejados por los turistas, con la opción de escribir una respuesta pública a cada valoración. | Gestionar su reputación online e interactuar con sus clientes. |
| **Estadísticas** | Panel con métricas clave: total de reservas, total de clientes, ingresos del último mes y un gráfico de distribución de reservas por estado. | Obtener una visión rápida del rendimiento de su negocio. |

#### Módulo de Reservas (RAT) y Calendario

| Funcionalidad | Descripción | Beneficio para el Empresario |
| :--- | :--- | :--- |
| **Calendario Interactivo** | Un calendario visual que muestra todas las reservas con códigos de color según su estado (Pendiente, Confirmada, Cancelada, Completada). | Vista centralizada y clara de la ocupación y planificación. |
| **Gestión de Reservas** | Permite crear reservas manualmente (ej. por teléfono), editar los detalles de una reserva existente (cliente, fechas, personas) o eliminarla. | Control total sobre el flujo de reservas de su negocio. |
| **Reprogramación Fácil** | Funcionalidad de "arrastrar y soltar" (`drag-and-drop`) para cambiar las fechas de una reserva directamente en el calendario. | Agilidad para gestionar cambios y reprogramaciones. |

#### Módulos Específicos (Según categoría del prestador)

| Categoría | Módulo | Funcionalidad Detallada |
| :--- | :--- | :--- |
| **Hotel** | **Habitaciones** | CRUD para gestionar los tipos de habitaciones del hotel, su capacidad y precios. |
| **Restaurante** | **Menú/Carta** | CRUD para crear categorías (ej. Entradas, Platos Fuertes) y añadir productos a cada una. |
| **Restaurante** | **Mesas** | CRUD para definir las mesas del establecimiento, su número y capacidad. |
| **Guía Turístico**| **Mis Rutas** | CRUD para crear y gestionar las rutas o tours que ofrece, con su descripción y si son públicos. |
| **Transporte** | **Vehículos** | CRUD para registrar los vehículos de su flota, con detalles como placa, marca, modelo y capacidad. |
| **Agencia de Viajes**| **Paquetes** | CRUD para crear y gestionar paquetes turísticos que combinan diferentes servicios. |

### 👑 Para los Roles Administrativos (Panel de Django)

Los usuarios con roles administrativos (Admin, Funcionario, etc.) gestionan el ecosistema desde el panel de administración de Django, que provee una interfaz potente para la supervisión y gestión de datos.

| Funcionalidad | Roles Permitidos | Descripción |
| :--- | :--- | :--- |
| **Gestión de Usuarios** | Admin, Funcionario | Crear, editar, y eliminar usuarios de cualquier rol. Asignar roles y permisos. |
| **Aprobación de Prestadores**| Admin, Funcionario | Revisar los perfiles de los nuevos prestadores de servicios registrados y aprobarlos para que sean visibles en el directorio público. |
| **Verificación de Documentos**| Admin, Funcionario | Acceder a los documentos subidos por los prestadores, revisarlos y cambiar su estado a "Aprobado" o "Rechazado", añadiendo observaciones. |
| **Gestión de Contenido** | Admin | Gestionar el contenido general del sitio, como publicaciones, noticias, eventos, páginas institucionales y los elementos del menú principal. |
| **Gestión de Categorías** | Admin | Crear y editar las categorías de prestadores de servicios (Hotel, Restaurante, etc.) y los tipos de documentos de verificación. |
| **Supervisión de Valoraciones** | Admin | Moderar las reseñas dejadas por los turistas, aprobándolas para que sean públicas o eliminando las que sean inapropiadas. |
| **Estadísticas Globales** | Admin | Acceder a vistas de analítica y reportes con datos agregados de todo el ecosistema turístico (funcionalidad futura). |
| **Configuración del Sitio**| Admin | Modificar parámetros globales del sitio, como el nombre de la entidad, logos, y claves de API de servicios externos. |