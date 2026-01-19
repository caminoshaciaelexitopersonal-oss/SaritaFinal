
# Informe de Impacto y Plan de Reconstrucción: Panel de Administración

**Fecha:** 2024-07-27
**Autor:** Jules, Ingeniero de Software IA

## 1. Resumen Ejecutivo

Durante la fase de auditoría y estabilización del sistema "Sarita", se ha identificado un defecto arquitectónico crítico en el panel de control del **Administrador**. El panel actual, ubicado en `/dashboard/admin/mi-negocio`, no es una implementación funcional diseñada para las necesidades del administrador. En su lugar, es una **copia directa e inoperante** del panel del **Proveedor de Servicios Turísticos** (`/dashboard/prestador/mi-negocio`).

Este defecto impide por completo que el rol de Administrador realice cualquier función de gestión sobre la plataforma, ya que toda la lógica, las llamadas a la API y las rutas de navegación están incorrectamente cableadas a las funcionalidades del proveedor.

Este informe detalla el impacto de este problema y propone un plan estratégico para la reconstrucción completa y correcta del panel de Administración.

## 2. Análisis del Defecto Arquitectónico

La investigación se centró en el módulo de **Gestión Comercial** como caso de estudio, pero la evidencia sugiere que el problema se extiende a todos los demás módulos de gestión (Contable, Financiero, Archivístico y Operativo).

### 2.1. Evidencia Clave

1.  **Estructura de Carpetas Idéntica:** El árbol de directorios de `frontend/src/app/dashboard/admin/mi-negocio/` es un espejo exacto de `frontend/src/app/dashboard/prestador/mi-negocio/`.
2.  **Código Reutilizado Incorrectamente:** El código fuente de los componentes es idéntico. Por ejemplo, el archivo `page.tsx` en `.../admin/mi-negocio/gestion-comercial/` es el mismo que el de la ruta `.../prestador/mi-negocio/gestion-comercial/`.
3.  **Enlaces Rotos y Lógica Cruzada:** El hallazgo más contundente es el botón "Nueva Factura" en el panel de administración, que contiene un enlace (`Link`) apuntando a la ruta del proveedor:
    ```jsx
    <Link href="/dashboard/prestador/mi-negocio/gestion-comercial/ventas/nueva" passHref>
      <Button>
        <PlusCircle className="mr-2 h-4 w-4" />
        Nueva Factura
      </Button>
    </Link>
    ```
    Esto prueba que el panel de administración no puede funcionar de forma independiente y, en su estado actual, solo puede romper la experiencia del usuario o, peor aún, corromper datos al intentar realizar acciones en el contexto equivocado.

## 3. Impacto en el Sistema

El impacto de este defecto es de **alta severidad**:

-   **Funcionalidad Nula para el Administrador:** El rol más importante del sistema, responsable de la supervisión y gestión de la plataforma, no tiene ninguna herramienta funcional a su disposición.
-   **Riesgo de Corrupción de Datos:** Si un administrador intentara usar estas herramientas (y si las APIs lo permitieran por error), podría estar modificando datos en el contexto de un proveedor aleatorio o de su propia entidad "Sarita" de forma no intencionada.
-   **Bloqueo para el Crecimiento:** Sin un panel de administración funcional, es imposible implementar características clave como la gestión de suscripciones de proveedores, la supervisión de transacciones financieras de la plataforma, la configuración del sitio o la gestión de usuarios.
-   **Deuda Técnica Masiva:** La arquitectura actual de "copiar y pegar" introduce una deuda técnica significativa que debe ser abordada antes de poder construir cualquier funcionalidad nueva sobre ella.

## 4. Plan de Reconstrucción Estratégico

No se recomienda aplicar parches temporales. La única solución viable es una **reconstrucción completa y desacoplada** del panel de Administración. La estrategia propuesta es la siguiente:

### Fase 1: Definición de Requisitos y Diseño de API

1.  **Análisis de Requisitos del Administrador:** Definir claramente las funciones que el administrador debe poder realizar en cada módulo de "Mi Negocio" desde su perspectiva (ej. ver finanzas de la plataforma, no las de un solo proveedor).
2.  **Diseño de Endpoints de API Específicos:** Crear un nuevo conjunto de URLs y vistas en el backend de Django, bajo una ruta como `/api/admin/plataforma/`, que sirvan los datos y ejecuten las acciones que el administrador necesita. Estos endpoints deben estar protegidos por permisos que verifiquen que el usuario es un administrador.
3.  **Diseño de Servicios de Backend:** Desarrollar una capa de servicios en el backend (ej. `GestionPlataformaService`) que orqueste la lógica de negocio para el administrador. Este servicio interactuará con los módulos existentes de `mi_negocio` pero desde una perspectiva de gestión global.

### Fase 2: Desarrollo del Frontend (Panel de Administración)

1.  **Creación de Componentes Desacoplados:** Construir un nuevo conjunto de componentes de React en `frontend/src/app/dashboard/admin/` que sean específicos para las vistas del administrador. Estos componentes no deben reutilizar la lógica de los componentes del proveedor.
2.  **Implementación de Vistas del Administrador:** Desarrollar las páginas del panel de administración utilizando los nuevos componentes y conectándolas a los nuevos endpoints de la API del administrador.
3.  **Creación de Hooks de Datos Específicos:** Desarrollar nuevos hooks (ej. `useAdminApi`) para encapsular la lógica de obtención de datos para el panel de administración, separados de los hooks del proveedor (`useMiNegocioApi`).

### Fase 3: Pruebas y Validación

1.  **Pruebas Unitarias y de Integración:** Escribir pruebas para los nuevos servicios de backend y los componentes de frontend para garantizar que funcionen como se espera.
2.  **Pruebas E2E (End-to-End):** Crear pruebas con Playwright para simular el flujo completo de un administrador utilizando su nuevo panel, desde el inicio de sesión hasta la ejecución de acciones clave.
3.  **Validación Manual:** Realizar una validación manual completa de todas las funcionalidades del nuevo panel de administración.

## 5. Conclusión

El estado actual del panel de administración representa un bloqueo crítico para el proyecto "Sarita". La solución propuesta de reconstrucción completa, aunque significativa, es el único camino para establecer una base de código sólida, segura y escalable que permita el desarrollo futuro y garantice la operatividad del sistema.
