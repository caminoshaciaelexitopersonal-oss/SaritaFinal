# Arquitectura del Frontend: Panel "Mi Negocio"

Este directorio (`app/[locale]/dashboard/prestador/mi-negocio/`) contiene toda la interfaz de usuario y la lógica del frontend para el panel de administración "Mi Negocio".

## Principios de Diseño

La arquitectura sigue los principios de Next.js 14 (App Router) y está diseñada para ser progresiva y desacoplada (PCA - Progressive Client Application).

- **Enrutamiento por Carpetas:** Cada módulo o submódulo tiene su propia carpeta, que se mapea directamente a una ruta en la URL (ej. `.../mi-negocio/gestion-operativa/perfil/`).
- **Componentes de Cliente y Servidor:** Se aprovecha el modelo de componentes de React Server Components, aislando la lógica de cliente (hooks, interactividad) en componentes marcados con `"use client"` para optimizar el rendimiento.
- **Gestión de Estado Centralizada:** El estado global de autenticación y datos de usuario se gestiona a través de React Contexts (`AuthContext`, `EntityContext`, etc.).

## Estructura de Carpetas

La estructura refleja la organización de la API del backend:

```
mi-negocio/
├── gestion-operativa/
│   ├── genericos/
│   │   ├── perfil/
│   │   │   └── page.tsx
│   │   └── ... (y así sucesivamente para cada módulo)
│   └── especializados/
│
├── gestion-comercial/
│   └── page.tsx  (Placeholder)
├── gestion-contable/
│   └── page.tsx  (Placeholder)
├── gestion-financiera/
│   └── page.tsx  (Placeholder)
└── gestion-archivistica/
    └── page.tsx  (Placeholder)
└── hooks/
    └── useMiNegocioApi.ts
```

## Hook de API (`useMiNegocioApi.ts`)

Para estandarizar y centralizar la comunicación con el backend, se ha creado el hook `useMiNegocioApi`.

- **Uso:** Proporciona funciones para operaciones CRUD (`fetchData`, `createData`, `updateData`, `deleteData`).
- **Autenticación:** Gestiona automáticamente la inyección del token de autenticación (JWT) en las cabeceras de las peticiones.
- **Estado de Carga y Errores:** Expone estados (`isLoading`, `error`) para facilitar la creación de interfaces de usuario reactivas.

### Ejemplo de Uso:

```typescript
import { useMiNegocioApi } from '@/app/[locale]/dashboard/prestador/mi-negocio/hooks/useMiNegocioApi';

function PerfilComponent() {
  const { data: perfil, isLoading, error, fetchData } = useMiNegocioApi<PerfilData>();

  useEffect(() => {
    fetchData('operativa/perfil');
  }, [fetchData]);

  if (isLoading) return <p>Cargando...</p>;
  if (error) return <p>Error: {error}</p>;

  return <div>{perfil?.nombre_comercial}</div>;
}
```
