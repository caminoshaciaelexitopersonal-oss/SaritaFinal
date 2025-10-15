# Proyecto SaritaUnificado

Este es el repositorio del proyecto SaritaUnificado, una plataforma integral de turismo que unifica las funcionalidades de los sistemas Sarita y Turismoapp.

## Arquitectura

El proyecto sigue una arquitectura de monorepo con dos componentes principales:

*   **Backend**: Una API RESTful construida con Django y Django REST Framework.
*   **Frontend**: Una Single-Page Application (SPA) construida con Next.js y React.

## Panel de Administración del Prestador de Servicios Turísticos

El sistema incluye un panel de administración robusto y modular para que los prestadores de servicios turísticos (hoteles, restaurantes, guías, etc.) gestionen sus operaciones. El panel es accesible desde la ruta `/dashboard`.

La navegación y los módulos disponibles se adaptan dinámicamente según la categoría del prestador que ha iniciado sesión.

### Módulos Genéricos (Comunes a todos los Prestadores)

Estos módulos están disponibles para cualquier tipo de prestador de servicios:

| Módulo              | Descripción                                               |
| ------------------- | --------------------------------------------------------- |
| **Inicio**          | Vista general y resumen de actividad.                     |
| **Mi Perfil**       | Edición de datos básicos del negocio (nombre, contacto, etc.). |
| **Productos/Servicios** | Catálogo de servicios o productos ofrecidos.              |
| **Clientes**        | Registro y gestión de clientes o visitantes.              |
| **Reservas**        | Gestión de reservas o solicitudes de servicio.            |
| **Valoraciones**    | Visualización de comentarios y calificaciones de clientes. |
| **Documentos**      | Carga y gestión de certificaciones (RNT, etc.).           |

### Módulos Específicos (Por Tipo de Prestador)

Estos módulos se activan según la categoría del prestador:

#### 🏨 Hoteles y Alojamientos

| Módulo         | Descripción                                    |
| -------------- | ---------------------------------------------- |
| **Habitaciones** | Gestión de habitaciones, precios y disponibilidad. |

#### 🍽️ Restaurantes y Bares

| Módulo      | Descripción                             |
| ----------- | --------------------------------------- |
| **Menú/Carta**  | Creación y gestión de los menús del local. |
| **Pedidos**   | Registro de pedidos y consumo (TPV).    |
| **Mesas**     | Gestión de mesas y su estado.           |

#### 🧭 Guías Turísticos

| Módulo      | Descripción                                |
| ----------- | ------------------------------------------ |
| **Mis Rutas** | Definición de recorridos, horarios y costos. |

#### 🚐 Transporte Turístico

| Módulo      | Descripción                                         |
| ----------- | --------------------------------------------------- |
| **Vehículos** | Registro de vehículos (placa, capacidad, etc.).     |

#### 🏝️ Agencias de Viajes y Operadores

| Módulo    | Descripción                                             |
| --------- | ------------------------------------------------------- |
| **Paquetes** | Creación y gestión de paquetes turísticos integrados. |