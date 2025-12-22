# Informe Final y Detallado de la Fase 5: QA Funcional - Módulo de Gestión Contable

## 1. Resumen Ejecutivo

Esta fase se centró en la validación funcional del módulo de **Gestión Contable**, una pieza crítica del ERP "Mi Negocio". Durante las pruebas de interoperabilidad con el módulo **Comercial** (creación de facturas de venta), se descubrió una **vulnerabilidad crítica de seguridad y de aislamiento de datos (multi-tenancy)**.

El objetivo principal de la fase se reorientó para corregir esta vulnerabilidad, asegurando que los datos contables de cada Prestador de Servicios (tenant) quedaran estrictamente aislados. La corrección fue implementada, validada exitosamente y la integridad del sistema fue restaurada.

## 2. Descubrimiento de la Vulnerabilidad Crítica

### 2.1. Problema Identificado

Al probar la creación de una factura de venta (`FacturaVenta`), que debe generar automáticamente un asiento contable (`JournalEntry`), se observó el siguiente comportamiento anómalo:

-   El sistema intentaba crear el asiento contable utilizando un **Plan de Cuentas (`ChartOfAccount`) genérico y compartido** para todos los usuarios.
-   Esto provocaba un error `DoesNotExist` porque el Plan de Cuentas no estaba asociado al perfil del prestador que emitía la factura.
-   Más importante aún, este diseño implicaba que, si hubiera funcionado, **todos los prestadores habrían compartido el mismo plan contable**, permitiendo la filtración de datos y la corrupción de la información financiera entre tenants. Un usuario podría, teóricamente, acceder o registrar asientos en cuentas contables de otro negocio.

### 2.2. Causa Raíz

La causa raíz se localizó en el modelo `ChartOfAccount` (`gestion_contable/sub_modulos/contabilidad/models.py`). Este modelo carecía de una relación directa con el perfil del prestador (`ProviderProfile`), convirtiéndolo en un recurso global en lugar de un recurso específico del tenant.

## 3. Proceso de Corrección y Refactorización

Para solucionar la vulnerabilidad, se ejecutaron los siguientes pasos de manera metódica:

1.  **Modificación del Modelo `ChartOfAccount`**:
    -   Se añadió un campo `ForeignKey` al modelo `ProviderProfile`.
    -   ```python
        perfil = models.ForeignKey(
            ProviderProfile,
            on_delete=models.CASCADE,
            related_name='plan_de_cuentas'
        )
        ```
    -   Esto asegura que cada cuenta contable pertenezca inequívocamente a un único prestador.

2.  **Regeneración de Migraciones**:
    -   Se eliminaron las migraciones existentes para el módulo de contabilidad que eran inconsistentes.
    -   Se generó una nueva migración inicial (`0001_initial.py`) que reflejaba la nueva estructura de datos multi-tenant.
    -   Se aplicaron las migraciones a la base de datos para actualizar el esquema.

3.  **Adaptación de la Lógica de Negocio**:
    -   Se actualizó el `ViewSet` de `ChartOfAccount` (`ChartOfAccountViewSet`) para filtrar el `queryset` basado en el `perfil_prestador` del usuario autenticado, asegurando que un usuario solo pueda ver y gestionar su propio plan de cuentas.
    -   Se modificó la lógica de creación de asientos contables (`JournalEntry`) en el módulo comercial para que, al crear una factura, se busque la cuenta contable correcta (ej. "Cuentas por Cobrar") dentro del plan de cuentas del prestador correspondiente.

## 4. Validación y Pruebas de Regresión

Se diseñó y ejecutó un riguroso protocolo de pruebas para validar la corrección y asegurar que no se introdujeron regresiones:

1.  **Test de Aislamiento (Multi-Tenant)**:
    -   **Escenario**: Se crearon dos empresas (`Empresa A` y `Empresa B`) con dos usuarios prestadores distintos (`prestador_a` y `prestador_b`).
    -   **Acción**: Se crearon planes de cuenta únicos y separados para cada empresa. Luego, `prestador_a` intentó crear una factura.
    -   **Resultado Esperado**: El sistema debía usar únicamente el plan de cuentas de la `Empresa A` y registrar el asiento contable correctamente.
    -   **Resultado Obtenido**: **ÉXITO**. La factura y el asiento se crearon utilizando exclusivamente los datos de la `Empresa A`. No hubo ninguna fuga o acceso a los datos de la `Empresa B`. La prueba se repitió para la `Empresa B` con el mismo resultado exitoso.

2.  **Test de Regresión del Flujo de Facturación**:
    -   **Escenario**: Se verificó el flujo completo de creación de facturas que se había estabilizado en fases anteriores.
    -   **Acción**: Se creó un cliente, un producto, una bodega, stock inicial y finalmente una factura de venta.
    -   **Resultado Obtenido**: **ÉXITO**. El flujo completo funcionó sin errores, confirmando que la refactorización del módulo contable no afectó la funcionalidad del módulo comercial.

## 5. Estado Final del Sistema (Post-Fase 5)

-   **Seguridad**: La vulnerabilidad de multi-tenancy ha sido **completamente cerrada**. El sistema ahora garantiza un aislamiento estricto de los datos contables entre los diferentes prestadores de servicios.
-   **Funcionalidad**: El flujo de integración entre los módulos **Comercial** y **Contable** es ahora funcional y seguro. La creación de una factura de venta genera correctamente el asiento contable correspondiente en el plan de cuentas del tenant correcto.
-   **Frontend**: El frontend para la gestión de `clientes` y `facturas` (`gestion-comercial`) funciona correctamente. El frontend para `gestion-contable` (plan de cuentas, informes) sigue marcado como **trabajo futuro**, ya que su implementación no era el objetivo de esta fase.
-   **Código Base**: El código ha quedado más robusto, seguro y alineado con las mejores prácticas para aplicaciones SaaS multi-tenant.

## 6. Conclusión y Próximos Pasos

La Fase 5 ha sido un éxito crítico. Aunque el objetivo inicial era una QA general, la detección y corrección de la vulnerabilidad de seguridad representa un avance mucho más significativo para la plataforma "Sarita". El núcleo del sistema ERP es ahora más seguro y fiable.

Los próximos pasos recomendados son continuar con la implementación de los módulos de frontend restantes (Contabilidad, Financiero, etc.) sobre esta base backend ahora estabilizada y segura.