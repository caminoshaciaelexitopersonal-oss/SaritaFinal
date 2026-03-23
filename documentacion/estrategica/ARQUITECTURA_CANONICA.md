# Diseño de Arquitectura Canónica y Grafo de Dependencias

Este documento define la arquitectura de aplicaciones canónica para el ERP Sarita, con el objetivo de eliminar las dependencias circulares y establecer un orden de carga y migración claro y robusto.

---

## 1. Inventario Lógico de Apps por Capas

| Capa | App / Módulo | Responsabilidad Principal |
| :--- | :--- | :--- |
| **Capa 0** | `django.contrib.*` | Framework base de Django. |
| **Capa 0** | `allauth`, `rest_framework`, etc. | Librerías de terceros. |
| --- | --- | --- |
| **Capa 1** | `companies` | Define el `Company` (Tenant). |
| **Capa 1** | `api` | Define el `CustomUser` y `ProviderProfile`. |
| --- | --- | --- |
| **Capa 2** | `prestadores` | Modelos operativos genéricos (`Product`, `Reserva`). |
| **Capa 2** | `gestion_contable` (core) | Modelos contables fundamentales. |
| --- | --- | --- |
| **Capa 3** | `gestion_financiera` | Lógica de movimientos de dinero. |
| **Capa 3** | `gestion_comercial` | Lógica del ciclo de ventas. |
| **Capa 3** | Subdominios (`nomina`, `empresa`) | Módulos de negocio específicos. |
| --- | --- | --- |
| **Capa 4** | `gestion_archivistica` | Servicio transversal de archivado. |
| **Capa 4** | `audit` | Servicio transversal de auditoría. |

---

## 2. Grafo de Dependencias Final

El siguiente grafo define las dependencias a nivel de `ForeignKey` y de importación de modelos, ahora implementado. Una flecha `A --> B` significa "`A` depende de `B`".

-   `api` --> `companies`
-   `prestadores` --> `api`
-   `gestion_contable` (subdominios) --> `api`
-   `gestion_financiera` --> `prestadores`, `gestion_contable`, `api`
-   `gestion_comercial` --> `prestadores`, `api`
-   **Servicios Transversales (`gestion_archivistica`, `audit`)**: No tienen dependencias `ForeignKey` entrantes de capas inferiores.

**Visualización del Grafo:**

```
[ Capa 4: Servicios (audit, gestion_archivistica) ]
      ^
      | (Invocados por, sin FK)
      |
[ Capa 3: Apps de Negocio (gestion_financiera, gestion_comercial) ]
      ^
      | (Dependen de)
      |
[ Capa 2: Módulos Base (prestadores, gestion_contable) ]
      ^
      | (Dependen de)
      |
[ Capa 1: Núcleo (api, companies) ]
```

Este grafo es **acíclico** y ha sido la base para la reconstrucción exitosa de las migraciones.

---

## 3. Estrategias de Ruptura de Ciclos Implementadas

Se implementaron las siguientes estrategias:
-   **Referencias por ID:** Todas las `ForeignKey` entre módulos core fueron reemplazadas por campos `UUIDField` (ej. `perfil_ref_id`).
-   **`GenericForeignKey`:** Se utilizó para relaciones polimórficas como el `beneficiario` de una `OrdenPago`.
-   **Invocación de Servicios:** Las relaciones con servicios transversales como el `ArchivingService` se manejan exclusivamente a través de llamadas de servicio, pasando IDs como parámetros.

---

## 4. Orden Canónico de Migraciones Validado

El procedimiento de "hard reset" y la generación/aplicación de migraciones por capas fue exitoso, validando el diseño arquitectónico.
