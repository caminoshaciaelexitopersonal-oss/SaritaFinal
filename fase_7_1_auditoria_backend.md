
# Fase 7.1: Auditoría Estructural del Backend

**Fecha:** 2024-07-27
**Autor:** Jules, Ingeniero de Software IA

## 1. Propósito

Este documento presenta un mapa de dependencias y una evaluación de riesgos del backend del sistema Sarita, como parte de la Fase 7.1 de fortalecimiento estructural. El objetivo es entender la arquitectura actual antes de introducir cambios controlados.

## 2. Aplicaciones Instaladas (`INSTALLED_APPS`)

La arquitectura del backend se compone de una mezcla de aplicaciones de Django, paquetes de terceros y aplicaciones personalizadas.

### 2.1. Django y Terceros
- **Django Core:** `admin`, `auth`, `contenttypes`, `sessions`, `messages`, `staticfiles`, `sites`.
- **Autenticación y API:** `rest_framework`, `authtoken`, `allauth` (completo), `dj_rest_auth`, `corsheaders`.
- **Utilidades:** `drf_spectacular` (documentación de API), `anymail` (emails), `django_filters`, `modeltranslation`.

### 2.2. Aplicaciones Propias
- `api`: App principal que parece manejar la lógica central de usuarios y configuraciones.
- `apps.prestadores`: App que agrupa la lógica de los proveedores de servicios.
- `apps.companies`: Funcionalidad de "compañías", posiblemente relacionada con la multi-tenancy.
- `apps.audit`: App para el registro de logs de auditoría.
- `apps.admin_plataforma`: **(Nueva)** La app aislada para la lógica del administrador de la plataforma.

### 2.3. Módulos de "Mi Negocio" (Sub-aplicaciones)
El núcleo empresarial reside en una estructura compleja de sub-aplicaciones dentro de `apps.prestadores.mi_negocio`. Estas no son apps de Django independientes en `INSTALLED_APPS` de la manera tradicional, sino módulos que se cargan a través de `AppConfig`.

- **Gestión Comercial:** `...gestion_comercial`
- **Gestión Financiera:** `...gestion_financiera`
- **Gestión Archivística:** `...gestion_archivistica`
- **Gestión Contable:**
    - `...empresa`
    - `...nomina`
    - `...cierres`
    - `...activos_fijos`
    - `...compras`
    - `...contabilidad`
    - `...inventario`
- **Facturación:** `...facturacion` (Separada, pero relacionada)

## 3. Mapa de Dependencias y Relaciones Clave

- **`ProviderProfile` es el Modelo Central:** El modelo `ProviderProfile` (ubicado en `.../perfil/models.py`) actúa como el ancla para casi toda la lógica de "Mi Negocio". Prácticamente todos los demás modelos en los módulos de gestión (ej. `ActivoFijo`, `FacturaVenta`, `Empleado`) tienen una `ForeignKey` apuntando a `ProviderProfile`.
- **`CustomUser` y `ProviderProfile`:** El modelo `api.CustomUser` tiene una relación directa con `ProviderProfile`, vinculando la identidad del usuario con su perfil empresarial.
- **Dependencias Cruzadas en "Mi Negocio":** Existe un alto acoplamiento entre los módulos de "Mi Negocio". Por ejemplo, `facturacion` probablemente depende de `gestion_comercial` (clientes, productos) y `gestion_contable` (cuentas). La refactorización de un módulo sin entender su impacto en los demás es de alto riesgo.
- **`ContentType` (Polimorfismo):** El framework de `ContentType` de Django ya se usa en algunas áreas (ej. `audit`), lo que indica que la introducción de relaciones genéricas es un patrón aceptado en el proyecto.

## 4. Riesgos Detectados

1.  **Alto Acoplamiento en `mi_negocio`:** El principal riesgo es la interdependencia de los módulos de "Mi Negocio". Un cambio en un modelo compartido (como `Cliente` o `Producto`, si existieran de forma centralizada) podría tener efectos en cascada impredecibles en la contabilidad, las finanzas y la operación. **Mitigación:** La estrategia de no tocar el backend existente es la correcta para evitar este riesgo.
2.  **Complejidad de Importaciones:** Como se descubrió en fases anteriores, la estructura de archivos anidada hace que encontrar las definiciones de modelos y serializadores sea difícil y propenso a errores. Esto aumenta el tiempo de desarrollo y el riesgo de importaciones incorrectas. **Mitigación:** La creación de la app aislada `admin_plataforma` evita tener que navegar por esta complejidad para el nuevo desarrollo.
3.  **Migraciones No Aplicadas:** El comando `showmigrations` reveló una gran cantidad de migraciones sin aplicar en el entorno de desarrollo. Esto no es un riesgo inmediato, pero indica que la base de datos local no está sincronizada, lo que podría ocultar problemas que solo aparecerían en un entorno limpio. **Mitigación:** Asegurarse de ejecutar `migrate` antes de las pruebas es crucial.
4.  **Warnings del Sistema:** El comando `check` arrojó dos warnings:
    - `(account.W001) ACCOUNT_LOGIN_METHODS conflicts with ACCOUNT_SIGNUP_FIELDS`: Un problema de configuración de `django-allauth` que debe ser revisado, pero no es crítico para la fase actual.
    - `(staticfiles.W004) The directory '/app/backend/static' does not exist`: La configuración de `STATICFILES_DIRS` apunta a un directorio inexistente. Esto podría causar problemas con los archivos estáticos y debe corregirse, aunque no es un bloqueante inmediato.

## 5. Conclusión

La auditoría confirma que la arquitectura del backend, especialmente en la sección "Mi Negocio", es compleja y altamente acoplada. La estrategia de aislar todo el nuevo desarrollo del administrador en la app `admin_plataforma` es la forma más segura y efectiva de proceder, ya que evita los principales riesgos identificados.
