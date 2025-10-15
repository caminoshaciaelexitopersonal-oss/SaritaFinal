# Proyecto SaritaUnificado

Este proyecto es una plataforma integral de gestión turística, diseñada para servir a corporaciones de turismo, prestadores de servicios y turistas. Este documento proporciona una visión general de la arquitectura y los módulos implementados.

## Arquitectura del Backend (Django)

El backend está construido con Django y Django REST Framework, siguiendo una arquitectura modular basada en aplicaciones.

### Módulos Implementados

#### App `empresa` (Módulos Genéricos para Prestadores)
- **Ruta Base:** `/api/empresa/`
- **Módulos:**
    - `productos/`: Gestión de productos o servicios generales.
    - `clientes/`: Registro y seguimiento de clientes.
    - `inventario/`: Control de inventario.
    - `costos/`: Gestión de costos operativos.
    - `recursos/`: Administración de recursos (humanos, logísticos).
    - `reglas-precio/`: Definición de precios dinámicos.
    - `vacantes/`: Portal de empleo.

#### App `restaurante` (Módulos para Restaurantes)
- **Ruta Base:** `/api/restaurante/`
- **Módulos:**
    - `categorias-menu/`: Gestión de categorías del menú.
    - `productos-menu/`: Gestión de los platos del menú.
    - `mesas/`: Gestión de mesas y su estado.
    - `pedidos/`: Creación y seguimiento de pedidos (TPV).

#### App `turismo` (Módulos de Turismo y Hotel)
- **Ruta Base:** `/api/turismo/`
- **Módulos:**
    - `hoteles/`: Perfil y gestión de hoteles.
    - `habitaciones/`: Gestión de habitaciones de un hotel.

## Arquitectura del Frontend (Next.js)

El frontend está construido con Next.js y TypeScript, utilizando el App Router.

### Panel del Prestador

- **Ruta Base:** `/dashboard`
- **Descripción:** Un panel de control unificado para que los prestadores de servicios gestionen sus operaciones. El panel utiliza un layout principal ubicado en `src/app/(dashboard)/layout.tsx` y renderiza dinámicamente los diferentes módulos.
- **Módulos Implementados:**
    - **Generales:** Productos, Clientes, Inventario, Costos, Recursos, Reglas de Precios.
    - **Restaurante:** Gestión de Menú, Gestión de Mesas, Pedidos (TPV).
    - **Hotel:** Gestión de Habitaciones.

## Cómo Levantar el Entorno de Desarrollo

1.  **Backend:**
    - Navegar a `SaritaUnificado/backend/`.
    - Crear un archivo `.env` con `DJANGO_DEBUG=True`.
    - Instalar dependencias: `pip install -r requirements.txt`.
    - Aplicar migraciones: `python manage.py migrate`.
    - Cargar datos iniciales: `python manage.py load_locations SaritaUnificado/backend/api/data/divipola_data.csv`.
    - (Opcional) Cargar datos de prueba: `python manage.py seed_data`.
    - Iniciar el servidor: `python manage.py runserver`.

2.  **Frontend:**
    - Navegar a `SaritaUnificado/frontend/`.
    - Instalar dependencias: `npm install`.
    - Iniciar el servidor: `npm run dev`.