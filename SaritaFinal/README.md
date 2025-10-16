# Proyecto SaritaUnificado - Documentación Funcional Definitiva

## 1. Introducción

**SaritaUnificado** es una plataforma turística integral de "triple vía" diseñada para crear un ecosistema digital cohesivo entre turistas, empresarios del sector y las entidades gubernamentales que regulan la actividad turística.

1.  **Vía del Turista:** Un portal público y atractivo para descubrir, planificar y reservar experiencias en la región.
2.  **Vía del Empresario:** Un potente panel de control privado para que los prestadores de servicios y artesanos gestionen su negocio, su oferta y su interacción con los clientes.
3.  **Vía de la Gobernanza:** Herramientas para que las entidades administrativas (secretarías, direcciones de turismo, etc.) supervisen, validen y fomenten el ecosistema turístico.

Este documento sirve como guía completa de todas las funcionalidades del sistema, segmentadas por el tipo de usuario y su rol.

---

## 2. Arquitectura del Sistema

*   **Backend:** API RESTful robusta construida con **Django** y **Django REST Framework**.
*   **Frontend:** Aplicación de Página Única (SPA) moderna y reactiva, construida con **Next.js 15** y **TypeScript**.
*   **Base de Datos:** SQLite para desarrollo, preparada para PostgreSQL en producción.

---

## 3. Funcionalidades para el Turista (Cara al Público)

El portal público es la puerta de entrada para los visitantes y el escaparate de la oferta turística de la región.

### 3.1. Páginas de Contenido y Descubrimiento

| Página | Funcionalidad |
| :--- | :--- |
| **Inicio** | Una página de bienvenida dinámica con componentes visuales (banners, sliders) que destacan los principales atractivos y noticias. |
| **Conoce Nuestro Municipio**| Una sección rica en contenido que incluye: la **historia** del municipio, una guía de **sitios de interés** y un listado de **atractivos turísticos** detallados con fotos y descripciones. |
| **Rutas Turísticas** | Un apartado dedicado a las rutas turísticas oficiales, donde cada ruta tiene su propia página con descripción, mapa y los atractivos y prestadores que la componen. |
| **Páginas Institucionales**| Secciones dedicadas a las entidades gubernamentales, como la **Secretaría de Turismo**, la **Dirección de Turismo** y el **Consejo Municipal de Turismo**, donde publican información oficial, políticas y noticias. |
| **Directorio Turístico** | El corazón del portal. Un buscador potente que permite a los turistas encontrar y filtrar todo tipo de **prestadores de servicios** (hoteles, restaurantes, agencias, etc.) y **artesanos**. |

### 3.2. Interacción y Planificación

| Funcionalidad | Descripción |
| :--- | :--- |
| **Perfil Público del Prestador**| Cada prestador y artesano tiene una página de detalle con su información completa: descripción, datos de contacto, redes sociales, **galería de fotos**, y un mapa con su ubicación. |
| **Catálogo de Servicios** | El perfil público muestra los **productos, paquetes o servicios** que el empresario ha configurado en su panel privado, permitiendo al turista conocer la oferta. |
| **Calendario de Disponibilidad**| En el perfil de prestadores que ofrecen servicios reservables (hoteles, guías), el turista puede ver un **calendario en tiempo real** que muestra los días disponibles y ocupados. |
| **Sistema de Reservas** | El turista puede seleccionar una fecha disponible en el calendario y enviar una **solicitud de reserva** directamente al prestador. |
| **Sistema de Valoraciones** | Después de su visita, el turista puede dejar una **calificación con estrellas y un comentario** en el perfil del prestador, que será visible públicamente una vez aprobado por un administrador. |
| **Registro y "Mi Viaje"** | Al crear una cuenta de "Turista", el usuario puede guardar sus atractivos y prestadores favoritos en una sección personalizada para planificar su viaje. |

---

## 4. Guía de Roles de Usuario

El sistema define roles específicos con permisos y funcionalidades adaptadas a cada necesidad.

### 4.1. Rol Turista

| Panel / Vista | Funcionalidades |
| :--- | :--- |
| **Sitio Público** | Acceso a todas las funcionalidades descritas en la sección 3. |
| **Panel "Mi Viaje"**| Tras iniciar sesión, accede a un panel sencillo para ver y gestionar los elementos que ha guardado como favoritos. |

### 4.2. Rol Artesano

| Panel / Vista | Funcionalidades |
| :--- | :--- |
| **Panel de Artesano** | Un panel de control privado que incluye: gestión de **perfil** (nombre del taller, descripción, fotos), gestión de **productos artesanales**, y visualización de **valoraciones** recibidas. |

### 4.3. Rol Prestador de Servicios Turísticos

El panel de administración más completo, con módulos que se activan según la categoría del negocio.

#### Módulos Genéricos (Para todos los prestadores)

| Módulo | Funcionalidad Detallada |
| :--- | :--- |
| **Perfil** | CRUD completo de la información pública del negocio. |
| **Productos/Servicios** | CRUD del catálogo de ofertas. |
| **Clientes (CRM)** | CRUD de la base de datos de clientes para seguimiento y fidelización. |
| **Galería** | CRUD de la galería de imágenes del perfil público. |
| **Documentos** | Subida de documentos legales y visualización de su estado de verificación. |
| **Valoraciones** | Visualización de reseñas y la capacidad de escribir una respuesta pública. |
| **Estadísticas** | Visualización de métricas de rendimiento (reservas, ingresos, etc.). |
| **Reservas (RAT)** | Calendario interactivo para gestionar todas las reservas con `drag-and-drop` y estados visuales. |

#### Módulos Específicos (Activados por Categoría)

| Categoría | Módulos Específicos |
| :--- | :--- |
| 🏨 **Hotel** | **Habitaciones:** CRUD para gestionar tipos de habitaciones, capacidad y precios. |
| 🍽️ **Restaurante** | **Menú/Carta** y **Mesas:** CRUD para gestionar categorías, productos y mesas del local. |
| 🧭 **Guía Turístico**| **Mis Rutas:** CRUD para gestionar las rutas y tours que ofrece. |
| 🚐 **Transporte** | **Vehículos:** CRUD para gestionar la flota de vehículos. |
| 🏝️ **Agencia de Viajes**| **Paquetes:** CRUD para crear y gestionar paquetes turísticos. |

### 4.4. Roles Administrativos

Gestionan el sistema desde un panel de administración central (Django Admin) con distintos niveles de permisos.

| Rol | Capacidades Principales |
| :--- | :--- |
| 👑 **Admin General** | **Control total.** Puede gestionar usuarios, contenido, configuraciones del sitio, categorías, y tiene acceso a todas las funcionalidades de los roles inferiores. Es el superusuario del sistema. |
| 🏛️ **Admin de Entidad** | **Gestión a nivel de su entidad (Municipal o Departamental).** Puede aprobar prestadores y artesanos dentro de su jurisdicción, gestionar contenido relacionado con su entidad y supervisar la actividad local. |
| 👔 **Funcionario Directivo**| **Rol de supervisión y aprobación.** Puede aprobar publicaciones y contenido generado por funcionarios profesionales antes de que pasen a la aprobación final del Admin. Tiene acceso a reportes y estadísticas. |
| 💼 **Funcionario Profesional**| **Rol de creación de contenido.** Es el encargado de crear y gestionar el contenido de las páginas públicas (atractivos, rutas, noticias, eventos). Su trabajo pasa por un flujo de aprobación. |