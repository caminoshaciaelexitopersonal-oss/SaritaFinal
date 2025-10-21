# Informe de Auditoría de Proyectos

## Resumen Ejecutivo

Este informe detalla los hallazgos del análisis de los tres proyectos: `Sarita`, `Turismoapp` y `SaritaUnificado`. El objetivo es evaluar su estado actual para guiar la refactorización y unificación en `SaritaUnificado`.

**Conclusión Clave:** `SaritaUnificado` es una copia parcial de `Sarita` con una estructura de frontend incipiente para "Mi Negocio", pero carece de la lógica de negocio presente en `Turismoapp`. La refactorización es necesaria y factible.

---

## 1. Análisis del Proyecto `Sarita`

`Sarita` es un sistema de gestión turística con un backend en Django y un frontend en Next.js.

### 1.1. Estructura y Funcionamiento

*   **Backend:** Construido con Django, utiliza una única app (`api`) para gestionar toda la lógica, incluyendo usuarios, perfiles, publicaciones, atractivos turísticos, configuración del sitio y más.
*   **Frontend:** Desarrollado con Next.js, presenta una estructura de páginas públicas (`/descubre`, `/directorio`) y un panel de administración (`/dashboard`).

### 1.2. Problema del Menú Principal

*   **Síntoma:** El menú de navegación principal a menudo no se carga, mostrando un esqueleto de carga indefinidamente (el "círculo" que mencionaste).
*   **Causa Raíz:** El componente `Header.tsx` del frontend obtiene los ítems del menú desde el endpoint `/api/config/menu-items/`. Este endpoint, gestionado por `MenuItemViewSet` en el backend, devuelve una lista de los objetos `MenuItem` almacenados en la base de datos.
*   **Diagnóstico:** El problema no es un error de código. Ocurre porque la tabla `MenuItem` en la base de datos está vacía. No existen migraciones que creen datos iniciales para el menú. Sin datos, el backend devuelve una lista vacía, y el frontend espera indefinidamente.
*   **Solución (Propuesta):** Crear un comando de gestión en Django (`management/command`) para poblar la base de datos con los ítems del menú iniciales.

---

## 2. Análisis del Proyecto `Turismoapp`

`Turismoapp` es una aplicación de escritorio desarrollada con el framework Flet de Python, enfocada en la gestión empresarial para prestadores de servicios turísticos.

### 2.1. Estructura y Componentes

*   **Tecnología:** Flet (Python). No es una aplicación web, por lo que su lógica debe ser reimplementada, no integrada directamente.
*   **Módulos de Gestión Identificados:** La carpeta `turismo_app/views/empresa/` contiene una rica lógica de negocio que debe ser migrada a `SaritaUnificado`.
    *   **Módulos Genéricos:**
        *   Gestión de Productos/Eventos (`empresa_gestion_productos_view.py`)
        *   Registro de Clientes (CRM) (`empresa_registro_clientes_view.py`)
        *   Gestión de Inventario (`gestion_inventario_view.py`)
        *   Gestión de Costos (`gestion_costos_view.py`)
    *   **Módulos Especializados:**
        *   **Restaurante:** Gestión de Menú, Mesas, TPV (Terminal Punto de Venta) y KDS (Kitchen Display System).
        *   **Agencia de Viajes:** Gestión de Paquetes Turísticos y Reservas.
        *   **Hotel (implícito):** El dashboard muestra lógica para configurar habitaciones y gestionar reservas.
*   **Dashboard Dinámico:** El panel principal (`empresa_dashboard_view.py`) carga los módulos de forma dinámica según el tipo de empresa (hotel, restaurante, agencia), un concepto clave a replicar.

---

## 3. Análisis del Proyecto `SaritaUnificado`

Este es el proyecto objetivo de la integración. Es una fusión de `Sarita` con la intención de incorporar la lógica de `Turismoapp`.

### 3.1. Estructura del Backend

*   **Estado:** Es una copia casi exacta del backend de `Sarita`, pero con una estructura de apps modularizada en la carpeta `backend/apps/` (`empresa`, `prestadores`, `restaurante`, `turismo`). Sin embargo, estas apps están mayormente vacías o contienen modelos básicos sin la lógica de `Turismoapp`.
*   **Panel del Prestador (`Mi Negocio`):**
    *   **Inexistente.** La app `prestadores` tiene una estructura simple sin la carpeta `mi_negocio`. La refactorización física y lógica no se ha iniciado.
*   **DIVIPOLA (Departamentos y Municipios):**
    *   **Comando Existente:** El comando `load_locations.py` existe en `api/management/commands/`.
    *   **Archivo de Datos Faltante:** El script requiere que se le pase la ruta a un archivo `divipola_data.csv` como argumento. Este archivo no está incluido en el repositorio, lo cual es una dependencia externa que debe ser gestionada. Los modelos `Department` y `Municipality` no se encuentran definidos en el `models.py` de `api`.

### 3.2. Estructura del Frontend

*   **Estado:** Es una copia del frontend de `Sarita`.
*   **Panel del Prestador (`Mi Negocio`):**
    *   La estructura de carpetas ha sido creada parcialmente: `src/app/(dashboard)/prestador/mi-negocio/`.
    *   **`gestion-operativa`:** Existe, pero solo contiene un módulo de `estadisticas` vacío. Las carpetas para módulos `genericos` y `especializados` no existen.
    *   **`gestion-comercial` y `gestion-contable`:** No existen.
*   **Conclusión:** La estructura del frontend está iniciada pero completamente vacía y no funcional.

---

## 4. Conclusiones y Próximos Pasos

1.  **Estado Actual:** `SaritaUnificado` tiene la base de `Sarita` pero carece de casi toda la lógica de negocio de `Turismoapp`. El trabajo de integración realizado hasta ahora es principalmente estructural y está incompleto.
2.  **Informe de Existencias:**
    *   **Existe:** Una estructura de carpetas básica e incompleta para "Mi Negocio" en el frontend.
    *   **No Existe:**
        *   La estructura de carpetas `mi_negocio` en el backend.
        *   Los módulos de gestión genéricos (Clientes, Inventario, etc.) en el backend o frontend.
        *   Los módulos de gestión especializados (Restaurante, Hotel, Agencia, etc.) en el backend o frontend.
        *   Los modelos `Department` y `Municipality` y el archivo de datos `divipola_data.csv`.
        *   Datos para el menú principal, causando el mismo problema que en `Sarita`.

Ahora que tenemos un diagnóstico claro, el siguiente paso es crear un plan de acción detallado para la refactorización y la implementación de las funcionalidades faltantes en `SaritaUnificado`.
