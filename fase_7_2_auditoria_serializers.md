
# Fase 7.2: Auditoría de Serializers Existentes (Activos Fijos)

**Fecha:** 2024-07-27
**Autor:** Jules, Ingeniero de Software IA

## 1. Propósito

Este documento detalla la estructura y comportamiento de los serializers existentes para los modelos `CategoriaActivo` y `ActivoFijo` antes de la implementación de los campos polimórficos.

## 2. Archivo Analizado

-   **Ruta:** `backend/apps/prestadores/mi_negocio/gestion_contable/activos_fijos/serializers.py`

## 3. Análisis de Serializers

### 3.1. `CategoriaActivoSerializer`

-   **Clase Base:** `serializers.ModelSerializer`
-   **Modelo Asociado:** `CategoriaActivo`
-   **Campos Expuestos:**
    -   `id` (lectura)
    -   `nombre` (lectura/escritura)
    -   `descripcion` (lectura/escritura)
-   **Campos `read_only` / `write_only`:** Ninguno explícito, `id` es de solo lectura por defecto.
-   **Validaciones Personalizadas:** No se observan.
-   **Uso del campo `perfil`:** El campo `perfil`, que será reemplazado por `owner`, no está actualmente expuesto en este serializer.

### 3.2. `ActivoFijoSerializer`

-   **Clase Base:** `serializers.ModelSerializer`
-   **Modelo Asociado:** `ActivoFijo`
-   **Campos Expuestos:**
    -   `id` (lectura)
    -   `nombre` (lectura/escritura)
    -   `categoria` (ID, escritura)
    -   `categoria_nombre` (string, **solo lectura**, obtenido de `categoria.nombre`)
    -   `descripcion` (lectura/escritura)
    -   `fecha_adquisicion` (lectura/escritura)
    -   `costo_adquisicion` (lectura/escritura)
    -   `valor_residual` (lectura/escritura)
    -   `vida_util_meses` (lectura/escritura)
    -   `metodo_depreciacion` (lectura/escritura)
    -   `depreciacion_acumulada` (**solo lectura**)
    -   `valor_en_libros` (**solo lectura**)
-   **Campos `read_only` explícitos:** `('depreciacion_acumulada', 'valor_en_libros')`
-   **Validaciones Personalizadas:** No se observan.
-   **Uso del campo `perfil`:** Al igual que en `CategoriaActivoSerializer`, el campo `perfil` no está expuesto en la API, lo que simplifica la introducción del nuevo campo `owner` sin romper la compatibilidad con los clientes existentes.

### 3.3. `CalculoDepreciacionSerializer`

-   Aunque no es objeto directo de la modificación, se observa que utiliza `serializers.CurrentUserDefault()` para el campo `creado_por`, un patrón útil a tener en cuenta.

## 4. Conclusión de la Auditoría

Ambos serializers son `ModelSerializer` estándar. La ausencia del campo `perfil` en la representación de la API actual es una ventaja significativa, ya que significa que la introducción del nuevo campo `owner` no entrará en conflicto con ningún campo existente expuesto a los clientes de la API.

La estrategia de extender estos serializers con un mixin para añadir el campo `owner` es viable y no debería introducir cambios disruptivos.
