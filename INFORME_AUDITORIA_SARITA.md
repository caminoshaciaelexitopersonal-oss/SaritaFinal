# Informe de Auditoría del Sistema "Sarita"

**Fecha:** 22 de Enero de 2026
**Autor:** Jules, Ingeniero de Software IA

## 1. Resumen Ejecutivo

El sistema "Sarita" es una plataforma de turismo de "triple vía" con una arquitectura tecnológicamente moderna (Django + Next.js). La auditoría revela un sistema **parcialmente implementado pero funcional en su núcleo**. La Vía 1 (Gobierno) y la Vía 3 (Turista) tienen un soporte de backend y frontend coherente y funcional. La Vía 2 (Prestadores) es la que presenta la mayor **discrepancia**: tiene un frontend muy detallado y completo que no se corresponde con la implementación del backend, donde dos de los cinco módulos de gestión empresarial (`Comercial` y `Contable`) son inexistentes.

La arquitectura de agentes de IA es un *blueprint* o diseño a futuro, muy detallado a nivel conceptual pero sin implementación funcional. El sistema base es estable, ejecutable y los flujos críticos como la autenticación son robustos.

## 2. Arquitectura "Triple Vía"

El sistema está claramente estructurado para servir a tres audiencias distintas:

*   **Vía 1: Corporaciones/Gobierno:** Gestionada a través del panel `/dashboard/admin`. Esta área permite la administración de contenidos (rutas, atractivos), usuarios, y la verificación de prestadores. Es el centro de control de la plataforma.
*   **Vía 2: Empresarios de Turismo (Prestadores):** Gestionada en `/dashboard/prestador/mi-negocio`. El objetivo es ofrecer 5 módulos de gestión empresarial.
*   **Vía 3: Turista:** Es el portal público (`/descubre`, `/directorio`, etc.), que consume la información gestionada por la Vía 1 y la Vía 2.

## 3. Estado del Backend

El backend está construido con Django y Django Rest Framework, siguiendo una arquitectura modular por aplicaciones.

### 3.1. Mapeo de Aplicaciones Django

*   **`admin_plataforma`**: Funcional. Gestiona la plataforma como un SaaS (planes, configuración de IA).
*   **`audit`**: Funcional. Provee logs de auditoría de acciones de usuarios.
*   **`cart`, `orders`, `payments`**: Funcional. Sistema de e-commerce para la compra de planes.
*   **`companies`**: Funcional. Gestión de empresas clientes, con un fuerte enfoque en seguridad.
*   **`prestadores`**: Contenedor. Su lógica ha sido refactorizada a `mi_negocio`.
*   **`sadi_agent`**: Funcional. Registra la auditoría de los comandos de voz.
*   **`web_funnel`**: Funcional. Permite construir páginas dinámicas desde el admin.

### 3.2. Auditoría del Módulo "Mi Negocio" (Vía 2)

El estado de los 5 módulos de gestión empresarial es dispar:

*   **`gestion_operativa`**: **Implementado y Funcional.** Es el núcleo de la Vía 2, conteniendo el modelo `ProviderProfile` (el "inquilino" del sistema).
*   **`gestion_archivistica`**: **Implementado y Funcional.** Módulo avanzado para la gestión de documentos, con preparación para integración blockchain.
*   **`gestion_financiera`**: **Implementación Básica.** Contiene modelos esenciales para cuentas bancarias y órdenes de pago.
*   **`gestion_comercial`**: **NO Implementado.** No existen modelos, serializadores, vistas ni servicios. Es un placeholder.
*   **`gestion_contable`**: **NO Implementado.** Al igual que el comercial, es solo una estructura de carpetas vacía a nivel de lógica de negocio.

### 3.3. Arquitectura de Agentes de IA

*   **Estructura:** El sistema en `backend/agents/` define una arquitectura jerárquica muy detallada y granular (Coronel -> Capitán -> Teniente), alineada con las tres vías y los módulos de gestión.
*   **Estado de Implementación:** **No Funcional (Blueprint).** Todos los archivos de agentes son copias de una plantilla (`captain_template.py`) sin lógica de negocio real. Son un andamiaje que define la intención arquitectónica, pero no tienen ninguna capacidad operativa actual. La desconexión es máxima en los módulos `gestion_comercial` y `gestion_contable`.

## 4. Estado del Frontend

El frontend está construido con Next.js 14 (App Router) y es robusto y moderno.

### 4.1. Estructura de Rutas y Componentes

*   **Coherencia:** La estructura de rutas en `frontend/src/app/` se corresponde perfectamente con la arquitectura de triple vía.
*   **Discrepancia Crítica:** Se ha construido una **interfaz de usuario completa y detallada** para los módulos de `gestion-comercial` y `gestion-contable` (Vía 2), a pesar de que estos **no tienen ningún soporte en el backend**. Esto representa una cantidad significativa de trabajo en el frontend que actualmente es inoperativo.

### 4.2. Auditoría de Componentes Clave

*   **Menú de Navegación:**
    *   **Problema:** El menú que a veces no carga se debe a que el componente `Header.tsx` depende de una llamada a la API (`GET /api/menu/`). Si esta API falla o no está disponible, el menú no se renderizará.
    *   **Gestión:** Existe un componente `MenuManager.tsx` en el panel de administración para gestionar los ítems del menú. Su funcionamiento también depende de la misma API.
    *   **Diagnóstico:** El problema no está en el frontend (que maneja bien los estados de carga y error), sino en la fiabilidad del endpoint `/api/menu/` del backend.
*   **Flujo de Autenticación (Login y Registro):**
    *   **Estado:** **Implementado y Robusto.** El flujo es completo y gestionado centralmente por `AuthContext.tsx`.
    *   **Características:** Soporta múltiples roles, registro condicional basado en rol, persistencia de sesión con `localStorage`, y un flujo de Multi-Factor Authentication (MFA).
    *   **Dependencia:** Su funcionamiento correcto depende de los endpoints de autenticación del backend (`/api/auth/...`).

## 5. Verificación de Funcionalidad Básica

*   **Entorno:** Las dependencias del backend (`requirements.txt`) y del frontend (`package.json`) se instalan correctamente.
*   **Base de Datos:** La base de datos está sincronizada con los modelos (migraciones al día) y puede ser poblada con datos de prueba a través del comando `setup_test_data`.
*   **Smoke Test:** **Exitoso.** Ambos servidores, Django (backend) y Next.js (frontend), se inician y responden a peticiones básicas. El sistema es **ejecutable**.

## 6. Conclusión General y Próximos Pasos

El sistema "Sarita" tiene una base sólida y bien arquitecturada. Los flujos para el turista (Vía 3) y el administrador (Vía 1) son mayormente funcionales. El principal problema y la mayor deuda técnica se encuentran en la **Vía 2 (Prestadores)**, donde se debe tomar una decisión estratégica:

1.  **Implementar el Backend Faltante:** Desarrollar los modelos, servicios y APIs para los módulos de `gestion_comercial` y `gestion_contable` para que la UI existente en el frontend pueda funcionar.
2.  **Implementar los Agentes de IA:** Dar vida a la arquitectura de agentes, reemplazando la lógica placeholder con llamadas reales a los servicios del backend.

Se recomienda proceder con un plan por fases que aborde primero la implementación del backend faltante para luego poder conectar la lógica de los agentes.
