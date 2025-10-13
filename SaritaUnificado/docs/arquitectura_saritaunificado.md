# Arquitectura del Sistema SARITA Unificado

## 1. Visión General

El proyecto SARITA Unificado es una plataforma web completa que integra un backend robusto basado en Django REST Framework con un frontend moderno y desacoplado construido con Next.js. El sistema está diseñado para ser una plataforma de turismo inteligente, modular y escalable, con un potente sistema de agentes jerárquicos para la gestión de tareas y la interacción con el usuario.

## 2. Estructura de Carpetas

El repositorio está organizado en una estructura monorepo para facilitar el desarrollo y el despliegue coordinado del backend y el frontend.

```
SaritaUnificado/
├── backend/      # Proyecto Django (API REST)
└── frontend/     # Proyecto Next.js (UI)
```

### 2.1. Backend (Django)

Ubicado en `SaritaUnificado/backend/`, el backend está construido con Django y Django REST Framework. Sus responsabilidades principales son:

*   **API REST:** Exponer endpoints para la gestión de datos (usuarios, prestadores, atractivos, etc.).
*   **Autenticación y Permisos:** Manejar el registro, inicio de sesión y control de acceso basado en roles mediante JWT (JSON Web Tokens).
*   **Sistema de Agentes Jerárquicos:** Orquestar la lógica de negocio y las tareas complejas a través de una cadena de mando de agentes inteligentes construidos con LangGraph.
*   **Lógica de Negocio y Base de Datos:** Gestionar la persistencia de datos en una base de datos PostgreSQL y encapsular las reglas de negocio.

### 2.2. Frontend (Next.js)

Ubicado en `SaritaUnificado/frontend/`, el frontend es una aplicación moderna de React construida con Next.js 15. Sus características clave incluyen:

*   **Renderizado Híbrido:** Utiliza SSR (Server-Side Rendering) y SSG (Static Site Generation) para un excelente SEO y rendimiento en páginas públicas, y CSR (Client-Side Rendering) para paneles de administración dinámicos.
*   **Stack Moderno:** Construido con TypeScript, TailwindCSS para el estilizado y ShadCN/UI para un sistema de componentes profesionales y accesibles.
*   **Paneles por Rol:** Ofrece interfaces de usuario diferenciadas y seguras para cada tipo de usuario (Administrador, Funcionario, Prestador, Artesano, Turista).
*   **Preparado para PWA:** La estructura está diseñada para ser fácilmente convertible en una Progressive Web App instalable.

## 3. Arquitectura de Agentes

El corazón del sistema SARITA es su arquitectura de agentes jerárquicos, que sigue una cadena de mando militar:

1.  **Sarita Nación (General):** Es el punto de entrada para todas las solicitudes de alto nivel. Supervisa y delega tareas a los agentes departamentales según la jurisdicción.
2.  **Sarita Departamento (General de Dept.):** Recibe directivas de Sarita Nación y las descompone en órdenes estratégicas para los Coroneles de los municipios de su departamento.
3.  **Coronel (Municipal):** Gestiona las operaciones a nivel municipal. Recibe órdenes del General de Departamento y las delega a su tropa de agentes especialistas (Capitanes).
4.  **Tropa (Capitanes, Tenientes, Sargentos):** Unidades especializadas que ejecutan tareas específicas (ej. gestionar contenido, buscar información, interactuar con herramientas externas).

Este diseño permite una alta modularidad, una clara separación de responsabilidades y la capacidad de gestionar tareas complejas de forma autónoma y coordinada.