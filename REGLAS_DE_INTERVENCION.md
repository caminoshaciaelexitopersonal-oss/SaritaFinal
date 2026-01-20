
# Reglas de Intervención para el Desarrollo en Sarita

**Última actualización:** 2024-07-27

## 1. Propósito

Este documento establece un conjunto de reglas operativas para guiar el desarrollo futuro del sistema Sarita. El objetivo es asegurar que las nuevas funcionalidades se construyan de manera segura, aislada y sin introducir regresiones en el sistema existente.

Estas reglas son el complemento práctico al documento `ZONAS_PROTEGIDAS.md`.

## 2. Principio Fundamental: Desarrollo Aislado y Aditivo

**Nunca modifiques código existente para introducir nueva funcionalidad mayor.** En su lugar, crea nuevos módulos, componentes o servicios que funcionen en paralelo. La modificación de código compartido solo se permite para correcciones de errores (bugs) que no alteren la firma de las funciones o el comportamiento esperado.

---

## 3. Reglas para el Desarrollo del Frontend

### 3.1. Panel de Administración vs. Panel de Proveedor

-   **PROHIBIDO:** Reutilizar, importar o referenciar cualquier componente, hook o servicio de la carpeta `frontend/src/app/dashboard/prestador/` dentro del nuevo panel de administración.
-   **OBLIGATORIO:** Todo el código relacionado con el nuevo panel de administración debe residir exclusivamente dentro de `frontend/src/app/dashboard/admin_plataforma/`.

### 3.2. Consumo de Activos Visuales

-   **PROHIBIDO:** Copiar, modificar, optimizar o regenerar cualquier activo de las zonas protegidas (`/public`, `/assets`, `/media`).
-   **PERMITIDO:** Referenciar los activos directamente en los componentes de React usando rutas relativas a la raíz del sitio.
    -   **Ejemplo Correcto:** `<Image src="/assets/logos/logo_principal.svg" ... />`
    -   **Ejemplo Incorrecto:** `<Image src="../admin_plataforma/assets/logo_copiado.svg" ... />`

### 3.3. Estilos y Componentes de UI

-   **RECOMENDADO:** Utilizar los componentes de UI genéricos de `frontend/src/components/ui/` (ej. `Button`, `Card`) para mantener la consistencia visual.
-   **PROHIBIDO:** Modificar estos componentes genéricos para adaptarlos a una necesidad específica del nuevo panel de administración. Si se requiere una variación, se debe crear un nuevo componente que extienda el original o uno completamente nuevo dentro del directorio del `admin_plataforma`.

---

## 4. Reglas para el Desarrollo del Backend

### 4.1. APIs del Administrador

-   **PROHIBIDO:** Modificar los `views`, `serializers` o `urls` de las APIs existentes que sirven al proveedor (`/api/v1/mi-negocio/`).
-   **OBLIGATORIO:** Todos los nuevos endpoints para el panel de administración deben crearse dentro de la aplicación `apps.admin_plataforma` y exponerse bajo el namespace `/api/admin/plataforma/`.

### 4.2. Lógica de Negocio y Modelos

-   **PROHIBIDO:** Alterar los modelos de la base de datos existentes. No se deben añadir, eliminar o modificar campos en las tablas que actualmente están en producción.
-   **OBLIGATORIO:** La nueva lógica de negocio del administrador debe encapsularse en **nuevos servicios** (ej. `GestionPlataformaService`). Estos servicios pueden *leer* datos de los modelos existentes, pero cualquier escritura debe realizarse a través de nuevos modelos o de una manera que no interfiera con la lógica del proveedor.
-   **PROHIBIDO:** Realizar migraciones de base de datos que no sean aditivas (es decir, que no se limiten a crear nuevas tablas).

## 5. Proceso de Cambio

1.  **Identificar la Necesidad:** ¿La nueva funcionalidad requiere interactuar con una zona protegida o modificar lógica existente?
2.  **Consultar este Documento:** Revisar las reglas para determinar el enfoque correcto.
3.  **Aplicar el Principio de Aislamiento:** Diseñar la solución creando nuevos archivos/módulos en lugar de modificar los existentes.
4.  **Validar:** Asegurarse de que los cambios no violan ninguna de las reglas aquí descritas antes de solicitar una revisión de código.
