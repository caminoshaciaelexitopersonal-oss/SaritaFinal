# Arquitectura del Backend: Panel "Mi Negocio"

Este directorio (`apps/prestadores/mi_negocio/`) contiene toda la lógica de backend para el panel de administración del Prestador de Servicios Turísticos, conocido como "Mi Negocio".

## Principios de Diseño

La arquitectura sigue un enfoque modular y de Componentes Autocontenidos (CPA), donde cada funcionalidad de negocio está encapsulada en su propio módulo.

- **Modularidad:** Cada módulo (ej. `perfil`, `inventario`) vive en su propio directorio y contiene sus propios modelos, vistas, y serializadores.
- **Descubrimiento Centralizado:** El archivo principal `prestadores/models.py` es responsable de importar todos los modelos de los submódulos para que Django pueda descubrirlos.
- **Enrutamiento Jerárquico:** Las rutas de la API se agrupan bajo el prefijo `/api/v1/prestadores/mi-negocio/`, con sub-rutas para cada gestión (ej. `/operativa/`).

## Estructura de Carpetas

La estructura está organizada por áreas de gestión:

```
mi_negocio/
├── gestion_operativa/
│   ├── modulos_genericos/
│   │   ├── perfil/
│   │   │   ├── models/
│   │   │   ├── serializers/
│   │   │   └── views/
│   │   ├── productos_servicios/
│   │   ├── clientes/ (Gestionado via `crm.py`)
│   │   ├── inventario/
│   │   └── ... (y así sucesivamente para cada módulo)
│   └── modulos_especializados/
│       └── ... (módulos para hoteles, restaurantes, etc.)
│
├── gestion_comercial/   (Placeholder)
├── gestion_contable/    (Placeholder)
├── gestion_financiera/  (Placeholder)
└── gestion_archivistica/ (Placeholder)
```

## Migraciones

El historial de migraciones para la aplicación `prestadores` y `api` ha sido reseteado y regenerado para asegurar la consistencia después de la refactorización física. Cualquier cambio en los modelos dentro de esta estructura requerirá la generación de nuevas migraciones.
