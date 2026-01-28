# INFORME TÉCNICO DETALLADO: ACOPLAMIENTO Y ESTABILIZACIÓN DEL ERP SISTÉMICO
**Estado de la Fase 1: Auditoría de Colisiones y Bloqueos de Diseño**

## 1. Resumen Ejecutivo
Se ha completado la auditoría profunda de los módulos de `admin_plataforma`. El sistema presenta una "clonación masiva" de modelos del dominio de Prestadores hacia el dominio de Administración de Plataforma. Esta estructura causa colisiones fatales en el registro de modelos de Django (ORM) debido al uso duplicado de `app_label = 'prestadores'`.

## 2. Inventario de Colisiones Críticas (Reverse Accessor & Model Name Clashes)

El sistema intenta registrar modelos con el mismo nombre dentro de la misma aplicación lógica (`prestadores`), lo cual es ilegal en Django.

| Modelo en `admin_plataforma` | Modelo en `prestadores` | Estado de Colisión | Razón Técnica |
| :--- | :--- | :--- | :--- |
| `Product` | `Product` | **CRÍTICA** | Mismo nombre y `app_label`. Conflicto en tabla intermedia `product_operational_tags`. |
| `Amenity` | `Amenity` | **CRÍTICA** | Mismo nombre en `hoteles`. |
| `RoomType` | `RoomType` | **CRÍTICA** | Mismo nombre en `hoteles`. |
| `KitchenStation` | `KitchenStation` | **CRÍTICA** | Mismo nombre en `restaurantes`. |
| `RestaurantTable` | `RestaurantTable` | **CRÍTICA** | Mismo nombre en `restaurantes`. |
| `Skill` | `Skill` | **CRÍTICA** | Mismo nombre en `guias`. |
| `Vehicle` | `Vehicle` | **CRÍTICA** | Mismo nombre en `transporte`. |
| `InventoryItem` | `InventoryItem` | **CRÍTICA** | Mismo nombre en `inventario`. |

### Análisis de Relaciones (Reverse Accessors)
Los modelos `TenantAwareModel` en ambos dominios apuntan a `ProviderProfile`. Al tener el mismo nombre de clase, Django intenta crear selectores inversos (ej. `provider.product_items`) que colisionan entre sí, ya que ambos dominios intentan usar el mismo `related_name` dinámico (`%(class)s_items`).

## 3. Acciones de Estabilización Ejecutadas (Fase 1)

### A. Implementación de Infraestructura de Gobernanza
Se han creado los componentes base para permitir que el Super Admin opere de forma sistémica:
- **`IsSuperAdmin` Permission:** Nuevo permiso en `api/permissions.py` que valida si el usuario es `ADMIN` o `superuser`.
- **`GestionPlataformaService`:** Servicio para recuperar el perfil de la organización "Gobierno" (ID:1).
- **`SystemicERPViewSetMixin`:** Mixin que fuerza el filtrado de datos hacia el perfil de plataforma, permitiendo que el Super Admin vea "su" ERP sin interferir con los datos de los prestadores.

### B. Corrección de Importaciones Obsoletas
Se detectó que los módulos clonados intentaban importar `BaseModel` y `ProviderProfile` de `api.models`, donde ya no existen.
- Se redirigieron masivamente las importaciones a: `apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models`.

### C. Acoplamiento de la "Triple Vía" en Frontend
- El **Sidebar** ha sido actualizado para mostrar el menú "ERP SISTÉMICO" exclusivamente al Super Admin.
- Se han renombrado los directorios en `frontend/src/app/dashboard/admin_plataforma/` para coincidir con la semántica de gobernanza.

## 4. Diagnóstico de Código "Fantasma" (Shadow Code)
Existen submódulos en `admin_plataforma/gestion_comercial` (como `automation`, `funnels`, `marketing`) que:
1. Tienen código completo de modelos y vistas.
2. **NO están registrados en `INSTALLED_APPS`.**
3. Esto significa que sus tablas NO existen en la base de datos actual.
4. **Recomendación:** No activar estos módulos hasta que se defina si el Super Admin usará los mismos funnels que los prestadores o si requiere una infraestructura separada.

## 5. Próximos Pasos Recomendados (Post-Auditoría)

1. **Unificación de Modelos (Refactorización Permitida en Fase 2):** Eliminar los archivos `models.py` duplicados en `admin_plataforma` y hacer que sus Views importen los modelos directamente desde `apps.prestadores`. Esto elimina todas las colisiones de ORM.
2. **Migración de Datos Sistémicos:** Asegurar que el perfil con ID:1 contenga los datos de configuración global de la plataforma.
3. **Activación Selectiva de URLs:** Restaurar los `include()` en `admin_plataforma/urls.py` una vez que la unificación de modelos sea segura.

---
**Informe final de la Fase 1.**
**Auditado por Jules.**
